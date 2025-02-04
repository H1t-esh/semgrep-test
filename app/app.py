#VULNERABLE CODE:

# from flask import Flask, request
# import sqlite3

# app = Flask(__name__)

# @app.route('/login', methods=['GET'])
# def login():
#     username = request.args.get('username')  # No validation!
#     conn = sqlite3.connect("users.db")
#     query = f"SELECT * FROM users WHERE username = '{username}'"  # SQL Injection Risk!
#     result = conn.execute(query).fetchall()
#     return str(result)

# if __name__ == "__main__":
#     app.run(debug=True)

#FIXED CODE
from flask import Flask, request, jsonify
import sqlite3
import re

app = Flask(__name__)

def is_valid_username(username):
    """Checks if username is alphanumeric and less than 20 characters."""
    return bool(re.match(r"^[a-zA-Z0-9]{1,20}$", username))

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')

    # Input validation
    if not username or not is_valid_username(username):
        return jsonify({"error": "Invalid username"}), 400

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Use parameterized query to prevent SQL Injection
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = cursor.fetchall()

    conn.close()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
