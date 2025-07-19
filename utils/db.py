import sqlite3, pathlib

_DB = pathlib.Path("genztrendy.db")

def init():
    conn = sqlite3.connect(_DB)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS content_items(
        id TEXT PRIMARY KEY,
        source TEXT,
        title TEXT,
        summary TEXT,
        subjects TEXT,
        tags TEXT,
        class_prompt TEXT,
        published TEXT,
        link TEXT
    )
    """)
    conn.commit()
    return conn
