
from ..db_loader import load_names_from_db
from ..search_engine import find_best_matches


def main():
    input_name = input("Enter a name to search: ").strip()
    db_names = load_names_from_db()

    matches = find_best_matches(input_name, db_names)

    print("\nTop Matches:")
    for name, score in matches:
        print(f"{name} - Score: {round(score * 100, 2)}%")

if __name__ == "__main__":
    main()