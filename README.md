
# 💬 Project Manager Assistant Chatbot (Django + OpenAI)

This is an AI-powered chatbot that acts like a Technical/Non-Technical Project Manager. It helps users with job-related queries such as resume writing, cover letters, interview prep, role definitions, and project management guidance.

## 🚀 Features

- ChatGPT-powered responses using OpenAI API
- Structured, professional advice with markdown formatting
- Beautiful web-based chat UI built with HTML, CSS, and JS
- Editable messages (click to update a previous question)
- Copy-to-clipboard button for responses
- “PM is typing…” animation for real-time feedback
- Clear All Chat button
- Export conversation to PDF
- Suggestion buttons for quick question templates

## 🛠 Tech Stack

- 🐍 Django (Backend)
- 🎨 HTML/CSS/JavaScript (Frontend)
- 🧠 OpenAI API (GPT-3.5-turbo)
- 📦 dotenv (for secure API key handling)

---

## 🧪 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/pm-chatbot.git
cd pm-chatbot
```

### 2. Setup Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # on Windows
```

### 3. Install Dependencies

```bash
pip install django openai python-dotenv
```

### 4. Add OpenAI API Key

Create a file named `.env` in the root folder and add:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Run the Server

```bash
python manage.py runserver
```

Open in browser: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📎 Folder Structure

```
pmchatbot-project/
├── chatbot/
│   ├── views.py          ← GPT logic + frontend rendering
│   ├── urls.py           ← Local URL patterns
│   ├── static/chatbot/
│   │   ├── style.css     ← Chat UI styling
│   │   └── chat.js       ← Chat handling logic
│   └── templates/chatbot/
│       └── chat.html     ← Chat UI template
├── pmchatbot/
│   ├── settings.py       ← Configuration & OpenAI key loading
│   └── urls.py           ← Includes chatbot URLs
├── .env                  ← OpenAI API key (not committed)
├── manage.py
└── db.sqlite3
```

---

## ✨ Demo Prompts to Try

- "How do I write a resume summary for a junior developer?"
- "What are common project manager interview questions?"
- "What is the difference between Scrum and Kanban?"
- "Create a short cover letter for a frontend developer job"

---

## 📄 License

This project is open for educational/demo use.
