# 🤖 LangChat — LangChain Chatbot

A simple AI chatbot built using **LangChain** and **Streamlit**, supporting both:

* ☁️ **Cloud LLM** using the Gemini API
* 🖥️ **Local LLM** using Ollama

This project was built to understand the fundamentals of LangChain, LLM integration, prompt templates, output parsers, chains, environment variables, Streamlit, and running open-source LLMs locally.

---

## 📌 Project Overview

The chatbot accepts a user's question, sends it through a LangChain pipeline, and returns the generated response.

### Cloud LLM Architecture

```text
User
  ↓
Streamlit UI
  ↓
ChatPromptTemplate
  ↓
LangChain Chain
  ↓
Gemini API
  ↓
StrOutputParser
  ↓
Response
```

### Local LLM Architecture

```text
User
  ↓
Streamlit UI
  ↓
ChatPromptTemplate
  ↓
LangChain Chain
  ↓
Ollama
  ↓
Llama 2
  ↓
StrOutputParser
  ↓
Response
```

---

# 🛠️ Technologies Used

* **Python**
* **LangChain**
* **LangChain Core**
* **LangChain Google GenAI**
* **LangChain Community**
* **Google Gemini API**
* **Ollama**
* **Llama 2**
* **Streamlit**
* **python-dotenv**

---

# 📂 Project Structure

```text
LangChat/
│
├── chatbot/
│   ├── app.py              # Cloud LLM chatbot
│   └── localama.py         # Local Ollama chatbot
│
├── .env                    # API keys (not committed)
├── requirements.txt        # Python dependencies
├── .gitignore
└── README.md
```

> The exact filenames may differ depending on your final project structure.

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/PiyushKumar23-12/ChatBot/tree/main
cd LangChat
```

---

## 2. Create a virtual environment

Create a Python virtual environment:

```bash
python -m venv venv
```


---

## 3. Install dependencies

All required Python packages are listed in `requirements.txt`.

Install them using:

```bash
pip install -r requirements.txt
```

---

# 🔑 Cloud LLM Setup — Gemini API

The cloud version of the chatbot uses Google's Gemini API through LangChain.

Create a Gemini API key from Google AI Studio.

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

The API key is loaded using `python-dotenv`:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
```

The key is then passed to the LangChain model:

```python
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    api_key=api_key
)
```

---

# 🖥️ Local LLM Setup — Ollama

One of the goals of this project was to understand how an LLM can be run **locally without relying on a cloud API**.

## 1. Install Ollama

Install Ollama on your system.

After installation, verify it from the terminal:

```bash
ollama --version
```

---

## 2. Download a local model

Run:

```bash
ollama run llama2
```

Ollama will download the Llama 2 model and run it locally.

Once downloaded, the model can be used without sending prompts to a cloud LLM provider.

---

## 3. Use Ollama with LangChain

The local chatbot uses LangChain's Ollama integration.

Example:

```python
from langchain_community.llms import Ollama

llm = Ollama(
    model="llama2"
)
```

The important difference is that the LLM is now running locally:

```text
LangChain
   ↓
Ollama
   ↓
Llama 2
   ↓
Local Machine
```

No Gemini/OpenAI API key is required for the local model.

---

# 🔗 Understanding the LangChain Chain

The main concept learned in this project is the **LangChain chain**.

The chatbot uses:

```python
chain = prompt | llm | output_parser
```

This represents a pipeline:

```text
Prompt
  ↓
LLM
  ↓
Output Parser
  ↓
Final Response
```

The `|` operator connects the individual components together.

---

# 📝 ChatPromptTemplate

Instead of directly sending a string to the model, a reusable prompt template can be created.

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Please respond to the user queries."
        ),
        (
            "user",
            "Question: {question}"
        )
    ]
)
```

Here:

```text
{question}
```

is a variable that gets replaced with the user's input.

For example:

```text
Question: What is LangChain?
```

---

# 🤖 LLM Integration

The LLM is the component responsible for generating the actual response.

For Gemini:

```python
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    api_key=api_key
)
```

For a local Ollama model:

```python
llm = Ollama(
    model="llama2"
)
```

The important idea is that **LangChain provides a common interface for interacting with different LLM providers**.

This allows the rest of the chain to remain largely unchanged while switching the underlying model.

---

# 📤 StrOutputParser

The LLM response may contain additional model-specific response information.

`StrOutputParser` converts the output into a simple string.

```python
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()
```

It is then added to the chain:

```python
chain = prompt | llm | output_parser
```

So the final result can be directly displayed to the user.

---

# 🔄 Invoking the Chain

The chain can be executed using:

```python
chain.invoke({
    "question": input_text
})
```

The data flows through the entire pipeline:

```text
input_text
    ↓
ChatPromptTemplate
    ↓
LLM
    ↓
StrOutputParser
    ↓
Final string
```
# 🔎 LangSmith Tracing & Monitoring

This project can be connected to **LangSmith** to trace and monitor the LangChain application.

LangSmith helps track what happens inside the LangChain pipeline, making it easier to:

* Debug chains
* Inspect prompts and model responses
* Monitor application runs
* Understand execution flow
* Evaluate and improve the application

## Environment Variables

Add your LangSmith API key to the `.env` file:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
```

Then configure LangChain tracing in the application:

```python
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"] = "true"

os.environ["LANGCHAIN_PROJECT"] = "streamlit-chatbot"
```

### What each variable does

#### `LANGCHAIN_API_KEY`

```python
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
```

Provides the API key that allows the application to communicate with LangSmith.

#### `LANGCHAIN_TRACING_V2`

```python
os.environ["LANGCHAIN_TRACING_V2"] = "true"
```

Enables LangChain tracing so that the application's LangChain executions can be recorded in LangSmith.

#### `LANGCHAIN_PROJECT`

```python
os.environ["LANGCHAIN_PROJECT"] = "streamlit-chatbot"
```

Specifies the LangSmith project where the traces will be grouped.

In this project, all chatbot traces are associated with:

```text
streamlit-chatbot
```

## How the Flow Works

```text
User
  ↓
Streamlit
  ↓
LangChain
  ↓
Prompt → LLM → Output Parser
  ↓
Response

        │
        └──────────────→ LangSmith
                         ↓
                    Trace / Monitor
                    LangChain execution
```

## `.env` Example

Your `.env` file can contain:

```env
GOOGLE_API_KEY=your_google_api_key

LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=streamlit-chatbot
```


---

# 🎨 Streamlit

Streamlit was used to create the chatbot's web interface directly with Python.

Example:

```python
import streamlit as st

st.title("LangChat")

input_text = st.text_input("Ask your question")
```

When the user enters a question:

```python
if input_text:
    response = chain.invoke({
        "question": input_text
    })

    st.write(response)
```

The application can be started with:

```bash
streamlit run app.py
```

---

# 🧠 What I Learned

Through this project, I learned the following LangChain fundamentals:

### 1. LLM Integration

How to connect an application to an LLM using LangChain.

```text
Application → LangChain → LLM
```

---

### 2. API Keys & Environment Variables

How to securely store API keys in `.env` rather than hardcoding them.

```env
GOOGLE_API_KEY=...
```

and load them using:

```python
load_dotenv()
```

---

### 3. Prompt Templates

How to create reusable prompts using:

```python
ChatPromptTemplate
```

---

### 4. LangChain Expression Language

How components can be combined using the pipe operator:

```python
prompt | llm | output_parser
```

---

### 5. Output Parsers

How to convert LLM output into a format that can easily be consumed by the application.

```python
StrOutputParser()
```

---

### 6. Local LLMs

How to run an open-source LLM locally using:

```text
Ollama + Llama 2
```

This demonstrated the difference between:

```text
Cloud LLM
→ API request
→ Cloud provider
→ Response
```

and:

```text
Local LLM
→ Ollama
→ Local model
→ Response
```

---

### 7. Switching LLM Providers

The project demonstrated that the LangChain pipeline can be reused while changing the underlying LLM.

```text
                ┌── Gemini
                │
LangChain ──────┤
                │
                └── Ollama + Llama 2
```

---

### 8. Streamlit

How to create a simple interactive AI application using Python without building a separate frontend.

---

# 🚀 Running the Application

## Gemini Version

Make sure your `.env` contains:

```env
GOOGLE_API_KEY=your_api_key
```

Then:

```bash
streamlit run app.py
```

---

## Ollama Version

First make sure Ollama is installed and the model is available:

```bash
ollama run llama2
```

Then start the local chatbot:

```bash
streamlit run localama.py
```

---

# 🔐 Security

The `.env` file should **never** be committed to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

# 📦 Requirements

The project dependencies are stored in:

```text
requirements.txt
```

Install everything with:

```bash
pip install -r requirements.txt
```

Example dependencies include:

```text
langchain
langchain-core
langchain-google-genai
langchain-community
streamlit
python-dotenv
```

---

# 🎯 Future Improvements

This project is intentionally a basic LangChain chatbot and serves as a foundation for more advanced AI applications.

Possible future improvements include:

* Chat history / memory
* Conversation persistence
* Streaming responses
* RAG
* Vector databases
* Document ingestion
* RAG evaluation
* LangGraph
* Agentic AI
* Tool calling
* Guardrails
* MCP
* FastAPI backend
* PostgreSQL
* Redis
* Docker
* Cloud deployment

---

# 👨‍💻 Learning Goal

The primary goal of this project was not just to build a chatbot, but to understand the fundamental building blocks behind a LangChain application:

```text
                 ┌──────────────┐
                 │   Streamlit  │
                 │      UI      │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │    Prompt    │
                 │    Template  │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │     LLM      │
                 │              │
                 │ Gemini/Ollama│
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │    Output    │
                 │    Parser    │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │   Response   │
                 └──────────────┘
```

This project forms the foundation for the next stage of learning **RAG, LangGraph, Agentic AI, and production-ready AI applications**.
