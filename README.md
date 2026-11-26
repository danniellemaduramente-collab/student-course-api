# Student Course API

## Project Description
Student Course API is a simple backend application developed for Laboratory 3 in System Integration and Architecture.

The application provides course information through REST API endpoints. It uses Python and Flask and returns data in JSON format.

## Objectives
- Create a backend API using Replit AI.
- Create REST API endpoints.
- Return course information in JSON.
- Test API responses.
- Prepare the project for deployment to Render.

## Technologies Used
- Python
- Flask
- Flask-Cors
- Gunicorn
- GitHub
- Render

## Course Information
The API contains five fictional courses:

1. ITAS 3228 - Web and Mobile Development
2. ITAS 3229 - System Integration
3. ITAS 3230 - Database Management
4. ITAS 3231 - Network Administration
5. ITAS 3232 - Information Security

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/health | Check API status |
| GET | /api/courses | Get all courses |
| GET | /api/courses/1 | Get a specific course |
| GET | /api/courses/9999 | Test invalid course ID |

## Sample API Response

### Health Check
```json
{
  "status": "success",
  "message": "Student Course API is running"
}
```

### Single Course
```json
{
  "id": 1,
  "code": "ITAS 3228",
  "name": "Web and Mobile Development",
  "description": "Introduction to web and mobile applications"
}
```

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

The application runs on port 5000 by default.

## Deployment on Render

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
gunicorn app:app
```

## Project Structure

```text
student-course-api/
│
├── app.py
├── requirements.txt
└── README.md
```

## Conclusion
This project demonstrates the basic implementation of a backend API using Flask. It shows how applications can communicate through REST endpoints and exchange data using JSON.

The project is a prototype and uses fictional sample data. It does not currently use a database or authentication system.
