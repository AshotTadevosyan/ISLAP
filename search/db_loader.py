import sqlite3

def load_names_from_db(db_path="data/sanctions.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT full_name, country, sanction_id FROM sanctions")
    records = cursor.fetchall()
    conn.close()
    return records