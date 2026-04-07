# 🎬 cinemind

**CineMind** is an AI-powered movie chatbot that answers questions about movies, actors, directors, and cinema.

It uses **Google Gemini AI** to generate intelligent responses and **MongoDB** to store chat history.  
The interface is inspired by modern AI chat applications.

---

## 🚀 Features

- 🎥 Movie-only AI chatbot
- 💬 ChatGPT-style chat interface
- 🧠 AI responses powered by Google Gemini
- 📂 Chat session history stored in MongoDB
- 📜 Markdown rendering for formatted AI responses
- ⚡ Fast backend using Flask

---

## 🏗️ Project Architecture

Frontend (HTML + CSS + JavaScript)

↓

Backend API (Flask)

↓

AI Model (Google Gemini)

↓

Database (MongoDB)

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **JavaScript**
- **HTML**
- **CSS**
- **MongoDB**
- **Google Gemini API**
- **Marked.js**

---

## 📂 Project Structure

```
movie_chatbot/
│
├── app.py
│
├── templates/
│     └── index.html
│
└── static/
      ├── script.js
      └── style.css
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/narasimhamurthy4616/cinemind-ai.git
cd moviegpt
```

### 2️⃣ Install Dependencies

```
pip install flask pymongo google-generativeai
```

### 3️⃣ Start MongoDB

```
mongod
```

### 4️⃣ Add Gemini API Key

Inside `app.py` add your API key:

```
genai.configure(api_key="YOUR_API_KEY")
```

### 5️⃣ Run the Application

```
python app.py
```

Then open in your browser:

```
http://127.0.0.1:5000
```

---

## 💡 Example Questions

Users can ask questions like:

- "Tell me about the movie Titanic"
- "Who directed the movie Interstellar?"
- "Top Telugu action movies"
- "Actors in the movie Baahubali"

---

## 🔒 Domain Restriction

This chatbot only answers **movie-related questions**.

If a user asks something outside movies, it returns:

```
⚠ Please ask only movie related questions.
```

---

## 📊 Database Example

Example MongoDB document:

```
{
 "_id": "2026-03-15 10:47:12",
 "title": "2026-03-15 10:47:12",
 "messages": [
  {
   "role": "user",
   "message": "polisodu telugu movie"
  },
  {
   "role": "bot",
   "message": "Policeodu is the Telugu dubbed version of the Tamil movie Theri..."
  }
 ]
}
```

---

## 📌 Future Improvements

- Streaming AI responses (typing effect)
- Automatic movie posters
- Chat title generation using AI
- Chat delete / rename feature
- User authentication

---

## 👨‍💻 Author

**Nagu**  
Cyber Security Engineering Student]

---

## ⭐ Support

If you like this project, consider giving it a **⭐ on GitHub**.
