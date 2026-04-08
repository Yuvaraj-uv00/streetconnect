from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Connect DB
def connect_db():
    return sqlite3.connect("database.db")

# Create table
@app.route('/init', methods=['GET'])
def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            food TEXT,
            location TEXT
        )
    ''')
    conn.commit()
    conn.close()
    return "Database Initialized"

# Add vendor
@app.route('/add_vendor', methods=['POST'])
def add_vendor():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vendors (name, food, location) VALUES (?, ?, ?)",
                   (data['name'], data['food'], data['location']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Vendor added"})

# Get vendors
@app.route('/get_vendors', methods=['GET'])
def get_vendors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vendors")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

app.run(debug=True)