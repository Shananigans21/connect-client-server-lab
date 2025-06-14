from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Sample in-memory data store
events = [
    {"id": 1, "title": "Python Conference"},
    {"id": 2, "title": "AI Meetup"}
]

# Root route to serve front-end HTML
@app.route("/")
def home():
    return render_template("index.html")

# GET route for "/events"
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events)

# POST route for "/events"
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Missing 'title' in request body"}), 400

    new_id = max((event["id"] for event in events), default=0) + 1
    new_event = {"id": new_id, "title": data["title"]}
    events.append(new_event)
    return jsonify(new_event), 201

if __name__ == "__main__":
    app.run(debug=True)
