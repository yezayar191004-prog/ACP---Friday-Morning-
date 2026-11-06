# setup_db.py  —  run ONCE to make library.db with 3 books
from pathlib import Path
import sqlite3

conn = sqlite3.connect(Path(__file__).resolve().with_name("library.db"))
conn.execute("DROP TABLE IF EXISTS books")
conn.execute("""
    CREATE TABLE books (
        id     INTEGER PRIMARY KEY,
        title  TEXT,
        author TEXT,
        year   INTEGER
    )
""")
conn.executemany(
    "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
    [
        ("Think Python", "Allen Downey", 2024),
        ("Clean Code", "Robert Martin", 2008),
        ("The Pragmatic Programmer", "Hunt and Thomas", 2019),
    ],
)
conn.commit()
conn.close()
print("library.db is ready with 3 books")
