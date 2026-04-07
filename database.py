import sqlite3

# ✅ Initialize DB
def init_db():
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        drive_link TEXT,
        result TEXT
    )
    """)

    conn.commit()
    conn.close()


# ✅ Save history
def save_history(drive_link, result):
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history (drive_link, result) VALUES (?, ?)",
        (drive_link, str(result))
    )

    conn.commit()
    conn.close()


# ✅ Get history
def get_history():
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM history ORDER BY id DESC")
    data = cursor.fetchall()

    conn.close()
    return data