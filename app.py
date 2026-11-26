
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample course data
courses = [
    {
        "id": 1,
        "course_code": "BSIT101",
        "name": "Introduction to Information Technology",
        "description": "Basic concepts of information technology."
    },
    {
        "id": 2,
        "course_code": "BSIT102",
        "name": "Programming Fundamentals",
        "description": "Introduction to programming and problem-solving."
    },
    {
        "id": 3,
        "course_code": "BSIT103",
        "name": "Database Management Systems",
        "description": "Introduction to databases and SQL."
    },
    {
        "id": 4,
        "course_code": "BSIT104",
        "name": "Web Development",
        "description": "Fundamentals of HTML, CSS, and JavaScript."
    },
    {
        "id": 5,
        "course_code": "BSIT105",
        "name": "Computer Networking",
        "description": "Introduction to computer networks and networking."
    }
]


# Homepage
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Student Course API is running!",
        "status": "success"
    })


# Health check
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "message": "API is working properly"
    })


# Get all courses
@app.route("/api/courses", methods=["GET"])
def get_courses():
    return jsonify(courses)


# Get a specific course by ID
@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            return jsonify(course)

    return jsonify({
        "error": "Course not found"
    }), 404


# Run the application
if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
