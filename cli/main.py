
from search.db_loader import load_names_from_db
from search.search_engine import find_best_matches


def main():
    input_name = input("Enter a name to search: ").strip()

    if not input_name:
        print("Error: Name cannot be empty.")
        return
    
    if len(input_name) < 3:
        print("Error: Name must be at least 3 characters long.")
        return
    try:
        db_names = load_names_from_db()
    except Exception as e:
        print(f"Error loading database: {e}")
        return

    try:
        matches = find_best_matches(input_name, db_names)
    except Exception as e:
        print(f"Error during matching: {e}")
        return

    if not matches:
        print("No matches found.")
        return

    print("\nTop Matches:")
    for name, score in matches:
        print(f"{name} - Score: {round(score * 100, 2)}%")

if __name__ == "__main__":
    main()