import os
import glob
import sqlite3
import xml.etree.ElementTree as ET

DB_PATH = 'data/sanctions.db'

ENHANCED_NS = {
    "ns": "https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/ENHANCED_XML"
}

ADVANCED_NS = {
    "ns": "https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/ADVANCED_XML"
}

def parse_enhanced_file(path, cursor):
    tree = ET.parse(path)
    root = tree.getroot()
    print(f"[ENHANCED] Parsing: {path}")

    for entity in root.findall(".//ns:entity", ENHANCED_NS):
        translation = entity.find(".//ns:translation", ENHANCED_NS)
        full = translation.findtext("ns:formattedFullName", default="", namespaces=ENHANCED_NS).strip() if translation is not None else ""
        country = entity.findtext("ns:country", default="", namespaces=ENHANCED_NS).strip()
        uid = entity.findtext("ns:uid", default="", namespaces=ENHANCED_NS).strip()

        if full:
            print(f"[ENHANCED] Inserting: {full}, {country}, {uid}")
            cursor.execute(
                "INSERT INTO sanctions (full_name, country, sanction_id) VALUES (?, ?, ?)",
                (full, country, uid)
            )

def parse_advanced_file(path, cursor):
    tree = ET.parse(path)
    root = tree.getroot()
    print(f"[ADVANCED] Parsing: {path}")

    for party in root.findall(".//ns:DistinctParties/ns:distinctParty", ADVANCED_NS):
        name_node = party.find(".//ns:wholeName", ADVANCED_NS)
        country_node = party.find(".//ns:country", ADVANCED_NS)
        uid_node = party.find(".//ns:uid", ADVANCED_NS)

        full = name_node.text.strip() if name_node is not None else ""
        country = country_node.text.strip() if country_node is not None else ""
        uid = uid_node.text.strip() if uid_node is not None else ""

        if full:
            print(f"[ADVANCED] Inserting: {full}, {country}, {uid}")
            cursor.execute(
                "INSERT INTO sanctions (full_name, country, sanction_id) VALUES (?, ?, ?)",
                (full, country, uid)
            )

def parse_sdn_file(path, cursor):
    tree = ET.parse(path)
    root = tree.getroot()
    print(f"[SDN] Parsing: {path}")

    for entry in root.findall(".//sdnEntry"):
        first = entry.findtext("firstName", default="").strip()
        last = entry.findtext("lastName", default="").strip()
        full = f"{first} {last}".strip()

        country = entry.findtext("country", default="").strip()
        uid = entry.findtext("uid", default="").strip()

        if full:
            print(f"[SDN] Inserting: {full}, {country}, {uid}")
            cursor.execute(
                "INSERT INTO sanctions (full_name, country, sanction_id) VALUES (?, ?, ?)",
                (full, country, uid)
            )

def parse_generic_xml(path, cursor):
    filename = os.path.basename(path).lower()

    if "enhanced" in filename:
        parse_enhanced_file(path, cursor)
    elif "advanced" in filename:
        parse_advanced_file(path, cursor)
    elif "sdn" in filename or "consolidated" in filename:
        parse_sdn_file(path, cursor)

def load_all_to_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sanctions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            country TEXT,
            sanction_id TEXT
        )
    """)

    DATA_DIR = 'data'
    xml_files = glob.glob(os.path.join(DATA_DIR, "*.xml"))
    for xml_file in xml_files:
        print(f"Processing: {xml_file}")
        parse_generic_xml(xml_file, cursor)

    conn.commit()
    conn.close()
    print("All files processed and loaded into sanctions.db")

if __name__ == '__main__':
    load_all_to_db()