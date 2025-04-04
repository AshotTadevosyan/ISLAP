import sqlite3

def load_names_from_db(db_path="data/sanctions.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT first_name, last_name, country, date_of_birth, program FROM sanctions
    """)
    
    rows = cursor.fetchall()
    conn.close()

    records = []
    for row in rows:
        first, last, country, dob, program = row
        full_name = f"{first} {last}".strip()
        is_org = not first.strip()
        records.append({
            "name": full_name,
            "first_name": first,
            "last_name": last,
            "country": country,
            "date_of_birth": dob,
            "program": program,
            "is_organization": is_org
        })

    return records