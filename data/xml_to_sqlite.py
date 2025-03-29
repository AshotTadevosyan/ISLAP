import os
import glob
import sqlite3
import xml.etree.ElementTree as ET

DB_PATH = 'data/sanctions.db'
ENHANCED_NS = {
    "ns": "https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/ENHANCED_XML"
}

def parse_sanctions_list(path, cursor):
    tree = ET.parse(path)
    root = tree.getroot()
    for entity in root.findall(".//ns:entity", ENHANCED_NS):
        translation = entity.find(".//ns:translation", ENHANCED_NS)
        if translation is not None:
            first = translation.findtext("ns:formattedFirstName", default="", namespaces=ENHANCED_NS).strip()
            last = translation.findtext("ns:formattedLastName", default="", namespaces=ENHANCED_NS).strip()
            full = translation.findtext("ns:formattedFullName", default="", namespaces=ENHANCED_NS).strip()
            if full:
                cursor.execute("INSERT INTO sanctions (first_name, last_name, full_name) VALUES (?, ?, ?)", (first, last, full))

def parse_sdn_file(path, cursor):
    tree = ET.parse(path)
    root = tree.getroot()
    for entry in root.findall(".//sdnEntry"):
        last = entry.findtext("lastName", default="").strip()
        first = entry.findtext("firstName", default="").strip()
        full = f"{first} {last}".strip()
        if full:
            cursor.execute("INSERT INTO sanctions (first_name, last_name, full_name) VALUES (?, ?, ?)", (first, last, full))

def parse_generic_xml(path, cursor):
    try:
        filename = os.path.basename(path).lower()
        if "sanctions_list" in filename or "enhanced" in filename or "advanced" in filename:
            parse_sanctions_list(path, cursor)
        elif "sdn" in filename:
            parse_sdn_file(path, cursor)
    except Exception as e:
        print(f"Error parsing {path}: {e}")

def load_all_to_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sanctions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            full_name TEXT NOT NULL
        )
    """)

    DATA_DIR = 'data/*.xml'
    xml_files = glob.glob(os.path.join(DATA_DIR, "*.xml"))
    for xml_file in xml_files:
        print(f"Processing: {xml_file}")
        parse_generic_xml(xml_file, cursor)

    conn.commit()
    conn.close()
    print("All files processed and loaded into sanctions.db")


if __name__ == '__main__':
    load_all_to_db()