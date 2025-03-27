from flask import Flask, request, jsonify
from search.db_loader import load_names_from_db
from search.search_engine import find_best_matches

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search_name():
    input_name = request.args.get('name', '').strip()

    if not input_name:
        return jsonify({"error": "Name cannot be empty"}), 400

    if len(input_name) < 3:
        return jsonify({"error": "Name must be at least 3 characters long"}), 400

    try:
        db_names = load_names_from_db()
        matches = find_best_matches(input_name, db_names)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    if not matches:
        return jsonify({"message": "No matches found"}), 404

    return jsonify([
        {"name": name, "score": round(score * 100, 2)} for name, score in matches
    ])

if __name__ == '__main__':
    app.run(debug=True)