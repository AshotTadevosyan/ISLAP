import os
import sqlite3
import xml.etree.ElementTree as ET

DB_PATH = "backend/data/sanctions.db"
XML_FILE = "backend/data/cons_enhanced-2.xml"
NS = {
    "ns": "https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/ENHANCED_XML"
}

def parse_and_load():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sanctions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            country TEXT,
            date_of_birth TEXT,
            program TEXT
        )
    """)

    tree = ET.parse(XML_FILE)
    root = tree.getroot()

    for entity in root.findall(".//ns:entity", NS):
        translation = entity.find(".//ns:translation", NS)
        first_name = translation.findtext("ns:formattedFirstName", default="", namespaces=NS).strip() if translation is not None else ""
        last_name = translation.findtext("ns:formattedLastName", default="", namespaces=NS).strip() if translation is not None else ""

        country_elem = entity.find(".//ns:address/ns:country", NS)
        country = country_elem.text.strip() if country_elem is not None else ""

        program_elem = entity.find(".//ns:sanctionsProgram", NS)
        program = program_elem.text.strip() if program_elem is not None else ""

        dob = ""
        for feature in entity.findall(".//ns:feature", NS):
            type_elem = feature.find("ns:type", NS)
            if type_elem is not None and type_elem.text == "Birthdate":
                dob_elem = feature.find("ns:value", NS)
                dob = dob_elem.text.strip() if dob_elem is not None else ""
                break

        if first_name or last_name:
            cursor.execute("""
                INSERT INTO sanctions (first_name, last_name, country, date_of_birth, program)
                VALUES (?, ?, ?, ?, ?)
            """, (first_name, last_name, country, dob, program))

    conn.commit()
    conn.close()
    return "Data loaded successfully."

if __name__ == "__main__":
    print(parse_and_load())