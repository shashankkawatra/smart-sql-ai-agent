# 🧠 Smart SQL AI Agent

A **schema-aware, multi-dialect SQL generation backend** that converts natural language queries into **safe, executable SQL** using Large Language Models (LLMs).

This project is designed as a **production-style AI inference service**, focusing on backend architecture, correctness, and safety guardrails rather than UI.

---

## ✨ Key Features

- Natural language → SQL conversion
- Multi-dialect SQL support:
  - PostgreSQL
  - MySQL
  - SQLite
  - MSSQL
- Schema-aware prompting to reduce hallucinations
- Strict SQL safety guardrails (SELECT-only)
- Deterministic LLM generation (temperature = 0)
- LLM-provider agnostic design
- Backend-first API using FastAPI
- Interactive Swagger documentation

---

## 🏗️ Architecture Overview

```
Client (Swagger / cURL)
        ↓
FastAPI Endpoint
        ↓
Prompt Builder (Schema + Dialect Rules)
        ↓
LLM (Groq – LLaMA 3)
        ↓
Output Normalization
        ↓
SQL Safety Validator
        ↓
Final SQL Response
```

---

## 🔒 Safety & Guardrails

The system enforces multiple layers of protection:

- Only SELECT queries are allowed
- Destructive SQL operations are blocked:
  - DROP
  - DELETE
  - INSERT
  - UPDATE
  - ALTER
- Regex-based keyword validation prevents false positives (e.g. `created_at`)
- Empty or unsafe LLM responses fail gracefully

---

## 🧩 Tech Stack

- **Backend:** Python, FastAPI
- **LLM Provider:** Groq (LLaMA-3)
- **Validation:** Regex-based SQL safety checks
- **Docs:** Swagger (FastAPI `/docs`)
- **Config:** Environment variables via `.env`

---

## 🚀 Getting Started

### Clone the repository
```bash
git clone https://github.com/<your-username>/smart-sql-ai-agent.git
cd smart-sql-ai-agent
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Configure environment variables
Create a `.env` file:
```env
GROQ_API_KEY=your_groq_api_key
```

### Run the application
```bash
uvicorn app.main:app --reload
```

Open Swagger UI:
```
http://127.0.0.1:8000/docs
```

---

## 📡 API Example

### Request
```json
{
  "question": "List the 5 most recent orders",
  "dialect": "postgresql"
}
```

### Response
```json
{
  "sql": "SELECT * FROM orders ORDER BY created_at DESC LIMIT 5;"
}
```

---

## 🌐 Live Demo

The API is deployed and publicly accessible.

- **Swagger Docs:** https://your-app-name.onrender.com/docs  
- **Base URL:** https://your-app-name.onrender.com

> ⚠️ Note: This service runs on a free hosting tier and may take a few seconds to wake up after inactivity.

---

## 🛣️ Future Enhancements

- Dynamic schema input
- Multi-agent workflow
- SQL execution layer
- Error feedback loop

---

## 📌 Disclaimer

This system is intentionally **read-only** and designed for SQL generation, not execution in production environments without additional safeguards.

