# 🚀 LUCA Validator – Agentic Validation System

## 📌 Overview

LUCA Validator is an AI-powered validation system built using **LangGraph + FastAPI**.
It performs dynamic rule-based validation on SFT/data files using intelligent agents.

---

## ⚙️ Features

* 🤖 Agent-based validation pipeline
* 📊 Rule-driven data validation
* ⚡ FastAPI backend with auto docs
* 🔗 LangGraph workflow integration
* 📁 File processing & classification
* 🔍 Detailed validation reports

---

## 🗂️ Project Structure

```
luca_validator/
│
├── main.py                  # FastAPI entry point
├── requirements.txt         # Dependencies
├── langgraph_workflow.py    # Core workflow
│
├── agents/                  # AI agents
│   ├── analysis_agent.py
│   ├── execution_agent.py
│   ├── file_classifier.py
│   ├── report_generator.py
│   └── rule_matcher.py
│
├── utils/                   # Utility modules
│   ├── file_handlers.py
│   ├── rule_parser.py
│   └── drive_downloader.py
│
└── downloaded_dataset/      # Sample data
```

---

## 🚀 Setup & Installation

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 2️⃣ Run the application

```
python main.py
```

---

### 3️⃣ Open in browser

```
http://localhost:8000/docs
```

---

## 🔐 Environment Variables

Create a `.env` file or add secrets:

```
OPENAI_API_KEY=your_api_key_here
```

---

## 📡 API Endpoints

| Endpoint    | Method | Description             |
| ----------- | ------ | ----------------------- |
| `/`         | GET    | Health check            |
| `/docs`     | GET    | Swagger UI              |
| `/validate` | POST   | Run validation pipeline |

---

## 🧠 Tech Stack

* FastAPI
* LangGraph
* Python
* Pydantic
* Uvicorn

---

## 📌 Notes

* Ensure all folders (`agents`, `utils`) are present
* Use correct Python version (3.10–3.11 recommended)
* Add API keys in Replit Secrets

---

## 💡 Future Improvements

* UI dashboard
* Multi-file validation
* Real-time monitoring
* Cloud storage integration

---

## 👨‍💻 Author

**Rakesh Namineni**


---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
