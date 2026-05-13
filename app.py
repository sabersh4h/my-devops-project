from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# In-memory task list (acts as simple data store)
tasks = [
    {"id": 1, "title": "Learn Docker", "done": False},
    {"id": 2, "title": "Set up CI/CD", "done": False},
]

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get("title", "Untitled"),
        "done": False,
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)