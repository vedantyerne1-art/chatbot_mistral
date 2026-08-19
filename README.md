<div align="center">

🤖 Mistral AI Chatbot

💬 A Modern Conversational AI Assistant Powered by Mistral AI

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Mistral%20AI-LLM-FF7000?style=for-the-badge" alt="Mistral AI">
  <img src="https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Status-Active-22C55E?style=for-the-badge" alt="Status">
</p>

<p>
  <b>Ask questions • Get intelligent answers • Experience conversational AI</b>
</p>

<p>
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a>
</p>

</div>

✨ Overview

Mistral AI Chatbot is a lightweight conversational AI application built with Python, Streamlit, and the Mistral AI API.

The project provides a clean chat experience where users can communicate with a powerful large language model through a simple web interface.

🎯 Goal: Build a simple, practical, and extensible foundation for AI-powered conversational applications.

🖥️ Application Flow

                         ┌─────────────────────┐
                         │       👤 USER       │
                         │   Sends a message   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   🎨 STREAMLIT UI   │
                         │   Chat Interface    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   🐍 PYTHON APP     │
                         │ Request Processing  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    🧠 MISTRAL AI    │
                         │   Language Model    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   💬 AI RESPONSE    │
                         │  Returned to User   │
                         └─────────────────────┘

🚀 Features

Feature

Description

🤖 AI Chat

Conversational interaction with Mistral AI

💬 Chat UI

Simple and intuitive Streamlit interface

⚡ Fast

Lightweight Python implementation

🔐 Secure Secrets

API credentials can be managed through Streamlit secrets

🐍 Python Based

Easy to understand and customize

🧩 Extensible

Ready for memory, RAG, authentication and more

🧰 Tech Stack

<div align="center">

Technology

Role

🐍 Python

Core application

🧠 Mistral AI

Large Language Model

🎨 Streamlit

Web interface

🔑 API Key

Secure API authentication

📦 pip

Dependency management

</div>

📂 Project Structure

chatbot_mistral/
│
├── 🤖 MistralChatBot.py       # Main chatbot application
├── 📦 requirements.txt        # Python dependencies
├── 🔐 secrets.toml            # Local secrets configuration
├── 📖 README.md               # Project documentation
└── 🚫 .gitignore              # Ignored files and secrets

Security note: Never commit real API keys or secret credentials to GitHub.

⚙️ Installation

1️⃣ Clone the Repository

git clone https://github.com/vedantyerne1-art/chatbot_mistral.git
cd chatbot_mistral

2️⃣ Create a Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

Linux / macOS

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

🔐 API Configuration

Create a Streamlit secrets file:

.streamlit/
└── secrets.toml

Add your API key:

MISTRAL_API_KEY = "your_api_key_here"

🚨 Important

Do not upload your real API key to GitHub.

Add the following to .gitignore:

.streamlit/secrets.toml
secrets.toml
venv/
__pycache__/
*.pyc

▶️ Run the Chatbot

Start the application:

streamlit run MistralChatBot.py

Then open the local Streamlit URL shown in your terminal.

💬 Example

┌──────────────────────────────────────────────┐
│              🤖 MISTRAL CHATBOT              │
├──────────────────────────────────────────────┤
│                                              │
│  👤 You                                      │
│  └─ Explain Artificial Intelligence simply.  │
│                                              │
│  🤖 Mistral                                  │
│  └─ Artificial Intelligence is the ability   │
│     of computers to perform tasks that       │
│     normally require human intelligence.     │
│                                              │
└──────────────────────────────────────────────┘

🧠 How It Works

User Input
    │
    ▼
Streamlit Chat Interface
    │
    ▼
Python Application
    │
    ├── Validate / process request
    │
    ▼
Mistral AI API
    │
    ▼
Language Model
    │
    ▼
Generated Response
    │
    ▼
Streamlit
    │
    ▼
User

🌱 Future Roadmap

This project can evolve into a more complete AI assistant.

🟢 Phase 1 — Core Chatbot

Mistral AI integration

Streamlit interface

User prompts

AI responses

🟡 Phase 2 — Smart Assistant

Conversation memory

Persistent chat history

Multiple model selection

Custom system prompts

Token / response monitoring

🔵 Phase 3 — RAG

PDF upload

Document parsing

Embeddings

Vector database

Retrieval-Augmented Generation

🟣 Phase 4 — Production

User authentication

Rate limiting

Logging & monitoring

Prompt-injection protection

Docker deployment

Cloud deployment

🛡️ Security Best Practices

For production deployment:

🔑 Keep API keys outside source code.

🚫 Never commit secrets to GitHub.

🧹 Add secret files to .gitignore.

👤 Add authentication for public applications.

🚦 Implement rate limiting.

📝 Add application logging.

🛡️ Validate user input.

🔍 Monitor API usage and failures.

📈 Project Vision

The long-term goal is to transform this simple chatbot into a production-ready AI assistant platform with:

                 ┌─────────────────────────┐
                 │     🤖 AI ASSISTANT     │
                 └────────────┬────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   💬 Chat                📚 RAG                🧠 Memory
        │                     │                     │
        ▼                     ▼                     ▼
   🔎 Search              📄 PDFs              💾 History
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              ▼
                    🚀 Production Platform

📚 Resources

Mistral AI

Mistral AI Documentation

Streamlit

Python

👨‍💻 Author

<div align="center">

Vedant Yerne

Computer Science & Engineering | AI & Software Development

<a href="https://github.com/vedantyerne1-art">
  <img src="https://img.shields.io/badge/GitHub-vedantyerne1--art-181717?style=for-the-badge&logo=github" alt="GitHub">
</a>

</div>

<div align="center">

⭐ If you found this project useful, consider starring the repository!

Built with 🐍 Python + 🧠 Mistral AI + 🎨 Streamlit

</div>
