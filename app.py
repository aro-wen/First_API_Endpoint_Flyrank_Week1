from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message" : "Welcome to my first backend API"
    })

@app.route("/about")
def about():
    return jsonify({
        "Name" : "Leila Arowen A. Dumindin",
        "Degree" : "Bachelor of Science in Computer Engineering",
        "Current target career" : "AI and Systems Engineer",
        "Long-term goal" : "Future IP Lawyer and Technology Policymaker"
    })

if __name__ == "__main__":
    app.run(debug=True)