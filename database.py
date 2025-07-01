import sqlite3
import json

DB_PATH = "unitermy.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS unitermy (
                nazwa TEXT PRIMARY KEY,
                opis TEXT,
                data_zrownoleglenie TEXT,
                data_sekwencja TEXT,
                merged_choice INTEGER
            )
        """)
        conn.commit()
