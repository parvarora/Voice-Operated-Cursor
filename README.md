
# 🎙️ Voice-Operated Agentic Coding Assistant

**Stateful, Tool-Using AI with LangGraph & Persistent Memory**

A **voice-controlled, agentic coding assistant** built using **Python and LangGraph**, capable of **planning, reasoning, and executing multi-step file and command-line operations** while persisting state across sessions.

The system combines **LLM-driven decision making**, **tool execution**, and **durable task memory** using **MongoDB**, enabling long-running, resumable coding workflows.

---

## 🚀 Key Capabilities

### ✅ Implemented Features

* **Voice-Driven Interaction**

  * Real-time speech-to-text using `SpeechRecognition`
  * Hands-free coding and system control

* **Agentic Workflow via LangGraph**

  * Explicit state machine with conditional transitions
  * Separation of reasoning and tool execution
  * Deterministic control over agent behavior

* **Tool-Using Coding Agent**

  * Executes system commands via registered tools
  * Designed for file creation, project setup, and shell operations
  * Enforced workspace isolation (`chat_gpt/` directory)

* **Stateful Conversations**

  * Conversation history persisted using **MongoDB**
  * Supports resumable sessions across restarts
  * Checkpointed graph execution using `MongoDBSaver`

* **Gemini-Powered Reasoning**

  * Google Gemini used for planning and response generation
  * Tool decisions inferred from natural language input

* **Containerized Infrastructure**

  * MongoDB deployed via Docker Compose
  * Environment-agnostic local setup

---

## 🧠 System Architecture

```
Voice Input (Microphone)
        │
Speech Recognition
        │
LangGraph State Machine
        │
 ┌─────────────┐
 │   Chatbot   │  ←─ Gemini Reasoning
 └──────┬──────┘
        │ (conditional)
 ┌──────▼──────┐
 │ Tool Node   │  ←─ Command Execution
 └──────┬──────┘
        │
MongoDB Checkpointing
        │
 Persistent Agent State
```

---

## 🛠️ Tech Stack

| Layer             | Technology             |
| ----------------- | ---------------------- |
| Language          | Python                 |
| Agent Framework   | LangGraph              |
| LLM               | Google Gemini          |
| Speech            | SpeechRecognition      |
| State Persistence | MongoDB                |
| Tool Execution    | LangChain Tools        |
| Containerization  | Docker, Docker Compose |

---

## 📂 Project Structure

```
├── graph.py                 # LangGraph agent definition
├── main.py                  # Voice interaction + runtime loop
├── docker-compose.yml       # MongoDB container
├── requirements.txt
├── chat_gpt/                # Agent-created workspace
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/voice-agentic-coding-assistant.git
cd voice-agentic-coding-assistant
```

### 2️⃣ Environment Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

### 4️⃣ Start MongoDB

```bash
docker-compose up -d
```

### 5️⃣ Run the Assistant

```bash
python main.py
```

---

## 🎧 Example Usage

```
User (voice):
"Create a Python file that prints system information"

Assistant:
→ Plans task
→ Executes shell commands
→ Creates files inside chat_gpt/
→ Responds with execution result
```

The agent:

* Decides **when to use tools**
* Executes commands safely
* Persists state for future continuation

---

## 🧪 Current Limitations (Transparent)

* Text-to-Speech output not yet integrated
* Tooling currently limited to shell execution
* No permission sandboxing (local-only usage recommended)
* Qdrant-based codebase RAG planned but not yet wired

---

## 🛣️ Roadmap

### 🔜 Planned Enhancements

* Codebase-aware RAG using **Qdrant**
* Secure sandboxed command execution
* Text-to-Speech output
* Multi-agent task delegation
* IDE integration (VS Code / CLI plugin)

---

## 📌 Why This Project Is Important

This project demonstrates:

* **True agentic design** (not prompt chaining)
* **State machines for LLM control**
* **Persistent AI systems**
* **Tool-calling with real execution**
* **Voice-first developer interfaces**

It reflects **production-oriented agent engineering**, not demos.

---
