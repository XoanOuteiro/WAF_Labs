from flask import Flask, request
import sqlite3
import re
from waf import waf_filter  # Import WAF function
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR,"database.db")

def query_db(query):
    """Executes SQL query without parameterization (Vulnerable to SQL Injection)."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute(query)  # 🚨 Direct execution (bad practice!)
        result = cursor.fetchall()
    except Exception as e:
        result = str(e)
    conn.close()
    return result

@app.route("/", methods=["GET"])
def home():
    return '''
    <form action="/query" method="post">
        <input type="text" name="input" placeholder="Enter SQL query">
        <button type="submit">Submit</button>
    </form>
    '''

@app.route("/query", methods=["POST"])
def query():
    user_input = request.form.get("input", "")

    if waf_filter(user_input):  # Check input against WAF
        return "Blocked by WAF!", 403

    result = query_db(f"SELECT * FROM users WHERE name = '{user_input}'")  # 🚨 SQL Injection here
    return f"Results: {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

