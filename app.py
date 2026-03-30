from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# ---------------- Gemini ----------------
genai.configure(api_key="AIzaSyABX0KYwyzO0-enqgHlKAEbgcSvrzrsRJM")

model = genai.GenerativeModel("gemini-2.5-flash", system_instruction="Only answer questions related to movies, actors, films, cinema.")


# ---------------- MongoDB ----------------
client = MongoClient("mongodb://localhost:27017/")
db = client["movie_chatbot"]
collection = db["chats"]

# ---------------- Allowed keywords ----------------
allowed_keywords = [
"movie","film","actor","actress","director","cinema",
"hollywood","bollywood","tollywood","story","plot","scene","songs","song"
]

# ---------------- Home ----------------
@app.route("/")
def home():
    return render_template("index.html")

# ---------------- Create Chat ----------------
@app.route("/new_chat")
def new_chat():

    session_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    collection.insert_one({
        "_id":session_id,
        "title":session_id,
        "messages":[]
    })

    return jsonify({"session_id":session_id})

# ---------------- Chat API ----------------
@app.route("/chat", methods=["POST"])
def chat():

    data = request.json
    message = data["message"]
    session_id = data["session_id"]

    if not any(k in message.lower() for k in allowed_keywords):
        return jsonify({
            "reply":"⚠ Please ask only movie related questions."
        })

    response = model.generate_content(message)

    bot_reply = response.text

    user_msg = {
        "role":"user",
        "message":message,
        "time":datetime.now().strftime("%H:%M")
    }

    bot_msg = {
        "role":"bot",
        "message":bot_reply,
        "time":datetime.now().strftime("%H:%M")
    }

    collection.update_one(
        {"_id":session_id},
        {"$push":{"messages":{"$each":[user_msg,bot_msg]}}}
    )

    return jsonify({"reply":bot_reply})

# ---------------- Load chats ----------------
@app.route("/chats")
def chats():

    chats = list(collection.find({},{"messages":0}))

    for chat in chats:
        chat["_id"]=str(chat["_id"])

    return jsonify(chats)

# ---------------- Load messages ----------------
@app.route("/chat/<session_id>")
def load_chat(session_id):

    chat = collection.find_one({"_id":session_id})

    if chat:
        return jsonify(chat["messages"])

    return jsonify([])

# ---------------- Run ----------------
if __name__ == "__main__":
    app.run(debug=True)
