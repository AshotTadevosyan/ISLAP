import sqlite3
import xml.etree.ElementTree as ET
import os

def load_xml_to_sqlite(xml_path="data/sanctions_list.XML", db_path="data/sanctions.db"):
    ns = {"ns": "https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/ENHANCED_XML"}

    if os.path.exists(db_path):
        os.remove(db_path)

    tree = ET.parse(xml_path)
    root = tree.getroot()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sanctions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            full_name TEXT NOT NULL
        )
    """)

    for entity in root.findall(".//ns:entity", ns):
        translation = entity.find(".//ns:translation", ns)
        if translation is not None:
            first = translation.findtext("ns:formattedFirstName", default="", namespaces=ns).strip()
            last = translation.findtext("ns:formattedLastName", default="", namespaces=ns).strip()
            full = translation.findtext("ns:formattedFullName", default="", namespaces=ns).strip()
            if full:
                cursor.execute(
                    "INSERT INTO sanctions (first_name, last_name, full_name) VALUES (?, ?, ?)",
                    (first, last, full)
                )

    conn.commit()
    conn.close()
    print("Sanctions data loaded successfully.")

if __name__ == "__main__":
    load_xml_to_sqlite()