# db03_queries_condensed.py

# This script will run the .sql in the sql_queries folder and print each's result.

# queries_to_png.py
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DB_FILE     = Path("authors_books.sqlite3")
QUERIES_DIR = Path("sql_queries")
OUT_DIR     = Path("query_results")
MAX_ROWS    = 30   # keep PNGs readable


print("SQL files detected:")
for f in sorted(QUERIES_DIR.glob("*.sql")):
    print(" -", f.name)
    
def run_select_to_df(conn: sqlite3.Connection, sql_text: str) -> pd.DataFrame:
    """Run a single SELECT (assumes the file ends with a SELECT)."""
    sql_text = sql_text.strip()
    if sql_text.endswith(";"):
        sql_text = sql_text[:-1]
    return pd.read_sql_query(sql_text, conn)

def df_to_png(df: pd.DataFrame, out_path: Path, title: str):
    """Render the first MAX_ROWS rows of a DataFrame to a PNG."""
    shown = df.head(MAX_ROWS)
    note = "" if len(df) <= MAX_ROWS else f" (showing first {MAX_ROWS} of {len(df)})"

    # size scales with data so it stays readable
    fig_w = min(24, 1.2 + 0.6 * max(4, len(shown.columns)))
    fig_h = min(14, 1.2 + 0.45 * max(4, len(shown) + 1))

    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    ax.axis("off")
    ax.set_title(f"{title}{note}", fontsize=12, pad=10)

    table = ax.table(
        cellText=shown.values,
        colLabels=list(shown.columns),
        loc="center"
    )
    table.auto_set_font_size(False)
    table.set_fontsize(5)
    table.scale(1, 1.2)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close(fig)

def main():
    if not DB_FILE.exists():
        print(f"Database not found: {DB_FILE}")
        return
    if not QUERIES_DIR.exists():
        print(f"Queries folder not found: {QUERIES_DIR}")
        return

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_FILE) as conn:
        for sql_file in sorted(QUERIES_DIR.glob("*.sql")):
            print(f"→ Running {sql_file.name}")
            sql_text = sql_file.read_text(encoding="utf-8")

            try:
                df = run_select_to_df(conn, sql_text)
            except Exception as e:
                print(f"  Skipping {sql_file.name}: {e}")
                continue

            # save CSV (handy for diffing in Git)
            csv_path = OUT_DIR / f"{sql_file.stem}.csv"
            df.to_csv(csv_path, index=False, encoding="utf-8")

            # save PNG snapshot
            png_path = OUT_DIR / f"{sql_file.stem}.png"
            df_to_png(df, png_path, title=sql_file.stem.replace("_", " ").title())

            print(f"  Saved: {csv_path.name}, {png_path.name}")

    print("Done! Check the query_results/ folder.")

if __name__ == "__main__":
    main()
 