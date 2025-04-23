#CourseTracker.py
import sqlite3
from flask import Flask, request, jsonify, render_template  # Add render_template

app = Flask(__name__)  # Define the app object here

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('course_tracker.db')
    conn.row_factory = sqlite3.Row  # Enable dictionary-like row access
    return conn

# Function to authenticate a user
def login(username, password):
    conn = get_db_connection()
    user = conn.execute(
        'SELECT * FROM users WHERE username = ? AND password = ?',
        (username, password)
    ).fetchone()
    conn.close()

    if user:
        print(f"Login successful! Welcome, {username}!")
        return {"name": user["name"], "track": user["track"]}
    else:
        print("Invalid username and/or password.")
        print("Try again.")
        return None

# New route to get user details and courses after login
@app.route('/api/user_data', methods=['POST'])
def get_user_data():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = login(username, password)
    if user:
        conn = get_db_connection()
        courses = conn.execute(
            'SELECT * FROM courses WHERE track = ?',
            (user["track"],)
        ).fetchall()
        conn.close()
        return jsonify({"name": user["name"], "courses": [dict(course) for course in courses]})
    return jsonify({"error": "Invalid credentials"}), 401

# Flask route to get all courses
@app.route('/api/courses', methods=['GET'])
def get_courses():
    conn = get_db_connection()
    courses = conn.execute('SELECT * FROM courses').fetchall()
    conn.close()
    return jsonify([dict(course) for course in courses])

# Flask route to get a specific course by ID
@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    conn = get_db_connection()
    course = conn.execute('SELECT * FROM courses WHERE id = ?', (course_id,)).fetchone()
    conn.close()
    if course:
        return jsonify(dict(course))
    return jsonify({"error": "Course not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
