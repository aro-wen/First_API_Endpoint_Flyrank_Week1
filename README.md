<<<<<<< HEAD


<!-- README-GEN:START profile-stats -->
![Profile Stats](https://github-readme-stats.vercel.app/api?username=FlyRank&show_icons=true)
<!-- README-GEN:END profile-stats -->

<!-- README-GEN:START repo-stats -->
### owner/repo
⭐ Stars: 0 | 🍴 Forks: 0 | 🐛 Issues: 0
<!-- README-GEN:END repo-stats -->

<!-- README-GEN:START visitor-badge -->
![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=owner.repo)
<!-- README-GEN:END visitor-badge -->

<!-- README-GEN:START streak -->
![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=flyrank&theme=default)
<!-- README-GEN:END streak -->
=======
# First Backend API

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![Git](https://img.shields.io/badge/Git-Version%20Control-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📖 About the Assignment

This project was created as part of an introductory backend development exercise.

The objective was to build the smallest possible backend application that exposes two JSON endpoints, test them using both a browser and `curl`, and publish the source code to GitHub.

The assignment focuses on understanding the HTTP request-response cycle from the server side. Instead of only consuming APIs, I implemented a server that receives requests and returns JSON responses.

---

## 🎯 Learning Objectives

Through this exercise, I aimed to understand:

* How a backend server works
* How HTTP requests reach an endpoint
* How routes are defined in Flask
* How JSON responses are returned to clients
* How to test APIs using a browser and `curl`
* How to manage and publish code using Git and GitHub

---

## 🛠️ Technologies Used

| Technology         | Purpose                 |
| ------------------ | ----------------------- |
| Python             | Programming Language    |
| Flask              | Backend Web Framework   |
| Git                | Version Control         |
| GitHub             | Code Hosting            |
| Visual Studio Code | Development Environment |

---

## 💭 Thought Process

When brainstorming ideas for the API, I considered creating endpoints related to:

* AWS AI Practitioner topics
* Internship information
* Productivity tracking

However, since the goal was to understand backend fundamentals rather than build a complex application, I chose a simple personal profile API.

This allowed me to focus on the core concepts:

1. Starting a server
2. Creating routes (endpoints)
3. Returning JSON data
4. Testing requests and responses
5. Publishing the project to GitHub

The emphasis of the assignment was not the complexity of the data but understanding the complete flow:

```text
Client
   ↓ Request
Flask Server
   ↓ Route Handling
JSON Response
   ↓
Client
```

---

## 🔗 API Endpoints

### 1. Home Endpoint

**Request**

```http
GET /
```

**Response**

```json
{
  "message": "Welcome to my first backend API"
}
```

---

### 2. About Endpoint

**Request**

```http
GET /about
```

**Response**

```json
{
  "name": "Leila Dumindin",
  "program": "BS Computer Engineering",
  "goal": "Backend Engineer and Future Lawyer"
}
```

---

## 🚀 Running the Project

### Install Dependencies

```bash
pip install flask
```

### Start the Server

```bash
python app.py
```

### Access Through Browser

```text
http://127.0.0.1:5000/
http://127.0.0.1:5000/about
```

### Test Using curl

```bash
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/about
```

---

## ✅ Results

Successfully developed a Flask backend application with two JSON endpoints.

The application demonstrates:

* Backend server initialization
* Route creation using Flask
* JSON response handling
* Browser-based API testing
* Command-line testing using `curl`
* Git and GitHub workflow integration

This project serves as my first hands-on experience building and exposing API endpoints and helped solidify my understanding of the HTTP request-response lifecycle.
>>>>>>> 39baa632c7233e57a4a363057a97fb852c8d3b7f
