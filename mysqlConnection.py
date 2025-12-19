from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="asliakin521",
    database="RestaurantFeedbackDatabase"
)
cursor = db.cursor(dictionary=True)

# Save Comment
@app.route("/comment", methods=["POST"])
def add_comment():
    data = request.get_json()
    comment = data.get("comment")

    cursor.execute("INSERT INTO comments (comment) VALUES (%s)", (comment,))
    db.commit()
    return jsonify({"success": True, "comment_id": cursor.lastrowid})

# Save Feedback
@app.route("/feedback", methods=["POST"])
def add_feedback():
    data = request.get_json()
    comment_id = data.get("comment_id")
    feedback = data.get("feedback")

    cursor.execute(
        "INSERT INTO feedbacks (feedback_id, feedback) VALUES (%s, %s)",
        (comment_id, feedback)
    )
    db.commit()
    return jsonify({"success": True, "feedback_id": cursor.lastrowid})

# List Comments
@app.route("/comments", methods=["GET"])
def get_comments():
    cursor.execute("SELECT * FROM comments")
    results = cursor.fetchall()
    return jsonify(results)

# List Feedbacks
@app.route("/feedbacks", methods=["GET"])
def get_feedbacks():
    cursor.execute("SELECT * FROM feedbacks")
    results = cursor.fetchall()
    return jsonify(results)

if __name__ == "__main__":
    app.run(port=5000, debug=True)