
from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app)

courses = [
    {
        "id": 1,
        "code": "ITAS 3228",
        "name": "Web and Mobile Development",
        "description": "Introduction to web and mobile applications"
    },
    {
        "id": 2,
        "code": "ITAS 3229",
        "name": "System Integration",
        "description": "Study of system integration and architecture"
    },
    {
        "id": 3,
        "code": "ITAS 3230",
        "name": "Database Management",
        "description": "Introduction to database design and management"
    },
    {
        "id": 4,
        "code": "ITAS 3231",
        "name": "Network Administration",
        "description": "Basic network configuration and administration"
    },
    {
        "id": 5,
        "code": "ITAS 3232",
        "name": "Information Security",
        "description": "Fundamentals of information security"
    }
]

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "success",
        "message": "Student Course API is running"
    }), 200

@app.route("/api/courses", methods=["GET"])
def get_courses():
    return jsonify(courses), 200

@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            return jsonify(course), 200

    return jsonify({
        "error": "Course not found"
    }), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
