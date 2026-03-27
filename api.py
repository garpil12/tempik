from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DB_FILE = "members.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

@app.route("/save", methods=["POST"])
def save():
    data = request.json
    chat_id = str(data["chat_id"])
    users = data["users"]

    db = load_db()

    if chat_id not in db:
        db[chat_id] = {}

    for u in users:
        db[chat_id][str(u["id"])] = u["name"]

    save_db(db)
    return {"status": "ok"}

@app.route("/get", methods=["GET"])
def get():
    chat_id = request.args.get("chat_id")
    db = load_db()
    return jsonify(db.get(chat_id, {}))

app.run(host="0.0.0.0", port=5000)
