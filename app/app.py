from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')  # No validation!
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username = '{username}'"  # SQL Injection Risk!
    result = conn.execute(query).fetchall()
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
