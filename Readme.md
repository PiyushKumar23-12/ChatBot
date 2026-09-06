# 🤖 LangChat — LangChain Chatbot

A simple AI chatbot built using **LangChain** and **Streamlit**, supporting both cloud-based and local Large Language Models (LLMs).

This project was built to understand the fundamentals of **LangChain, LLM integration, prompt templates, chains, output parsers, Streamlit, environment variables, LangSmith tracing, and local LLMs using Ollama**.

---

## 🚀 Features

* ☁️ Chatbot using **Google Gemini API**
* 🖥️ Chatbot using **Ollama + Llama 2**
* 🔗 LangChain-based LLM pipeline
* 📝 Prompt templating using `ChatPromptTemplate`
* 📤 Output processing using `StrOutputParser`
* ⛓️ LangChain Expression Language (`|`)
* 🎨 Interactive UI using Streamlit
* 🔐 API key management using `.env`
* 🔎 LangSmith tracing, debugging, monitoring, and evaluation
* 🔄 Ability to switch between cloud and local LLMs

---

# 🛠️ Technologies Used

* Python
* LangChain
* LangChain Core
* LangChain Google GenAI
* LangChain Community
* Google Gemini
* Ollama
* Llama 2
* Streamlit
* LangSmith
* python-dotenv

---

# 📂 Project Structure

```text
LangChat/
│
├── app.py              # Gemini API chatbot
├── localama.py         # Ollama + Llama 2 chatbot
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .gitignore
├── .env                # API keys (not committed)
└── venv/               # Python virtual environment
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/PiyushKumar23-12/ChatBot/tree/main
cd chatbot
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

All dependencies are listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

---

# ☁️ Gemini API Setup

The cloud chatbot uses Google's Gemini model through LangChain.

Create a Gemini API key using Google AI Studio.

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
```

Load the environment variables in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
```

Create the Gemini LLM:

```python
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    api_key=api_key
)
```

> ⚠️ Never commit your `.env` file or expose your API key publicly.

---

# 🖥️ Local LLM with Ollama

The project also demonstrates how to run an LLM **locally** using Ollama.

## 1. Install Ollama

Install Ollama on your system and verify the installation:

```bash
ollama --version
```

## 2. Download and Run Llama 2

```bash
ollama run llama2
```

This downloads the Llama 2 model and runs it locally.

## 3. Connect Ollama to LangChain

```python
from langchain_community.llms import Ollama

llm = Ollama(
    model="llama2"
)
```

The local architecture is:

```text
User
 ↓
Streamlit
 ↓
LangChain
 ↓
Ollama
 ↓
Llama 2
 ↓
Response
```

No cloud API key is required for the local LLM.

---

# 🔗 LangChain Chain

The core concept learned in this project is the **LangChain chain**.

The application connects the prompt, LLM, and output parser:

```python
chain = prompt | llm | output_parser
```

The pipeline is:

```text
ChatPromptTemplate
        ↓
       LLM
        ↓
StrOutputParser
        ↓
    Response
```

The `|` operator connects the components together and passes the output of one component to the next.

---

# 📝 ChatPromptTemplate

`ChatPromptTemplate` is used to create structured and reusable prompts.

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

The `{question}` variable is dynamically replaced with the user's input.

For example:

```text
Question: What is LangChain?
```

---

# 🤖 LLM Integration

LangChain provides a consistent way to interact with different LLM providers.

### Gemini

```python
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    api_key=api_key
)
```

### Ollama

```python
llm = Ollama(
    model="llama2"
)
```

This makes it possible to change the underlying LLM while keeping much of the application pipeline unchanged.

```text
                  ┌── Gemini API
                  │
LangChain ────────┤
                  │
                  └── Ollama → Llama 2
```

---

# 📤 StrOutputParser

`StrOutputParser` converts the LLM output into a simple string that can be easily displayed or processed.

```python
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()
```

It is then added to the chain:

```python
chain = prompt | llm | output_parser
```

---

# ▶️ Invoking the Chain

The chain is executed using:

```python
chain.invoke({
    "question": input_text
})
```

The complete flow is:

```text
User Input
    ↓
Prompt Template
    ↓
LLM
    ↓
Output Parser
    ↓
Final Response
```

---

# 🎨 Streamlit

Streamlit is used to create the web interface for the chatbot using Python.

Example:

```python
import streamlit as st

st.title("LangChat")

input_text = st.text_input("Ask your question")

if input_text:
    response = chain.invoke({
        "question": input_text
    })

    st.write(response)
```

Run the Gemini chatbot:

```bash
streamlit run app.py
```

Run the Ollama chatbot:

```bash
streamlit run localama.py
```

---

# 🔎 LangSmith — Tracing, Debugging & Monitoring

**LangSmith** is used to observe and analyze LangChain applications.

It provides capabilities for:

* 🔍 **Tracing** — See how each component of the LangChain application executes
* 🐛 **Debugging** — Identify where problems occur in a chain
* 📊 **Monitoring** — Observe application runs and behavior
* 🧪 **Evaluation** — Analyze and evaluate LLM outputs
* 📋 **Inspection** — View prompts, model inputs, outputs, and execution flow

For example, for:

```python
chain = prompt | llm | output_parser
```

LangSmith can show the execution:

```text
Chain
 │
 ├── ChatPromptTemplate
 │      ↓
 │   Generated Prompt
 │
 ├── LLM
 │      ↓
 │   Model Response
 │
 └── StrOutputParser
        ↓
   Final Response
```

This makes it much easier to understand what is happening inside an LLM application.

---

## LangSmith Configuration

Add your LangSmith API key to `.env`:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
```

Then enable tracing:

```python
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"] = "true"

os.environ["LANGCHAIN_PROJECT"] = "streamlit-chatbot"
```

### Environment Variables Explained

#### `LANGCHAIN_API_KEY`

```python
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
```

Provides authentication for LangSmith.

#### `LANGCHAIN_TRACING_V2`

```python
os.environ["LANGCHAIN_TRACING_V2"] = "true"
```

Enables LangChain tracing so application executions can be sent to LangSmith.

#### `LANGCHAIN_PROJECT`

```python
os.environ["LANGCHAIN_PROJECT"] = "streamlit-chatbot"
```

Specifies the LangSmith project where the application's traces are grouped.

All traces for this chatbot can therefore be viewed under:

```text
streamlit-chatbot
```

---

# 🔐 Environment Variables

The `.env` file can contain:

```env
GOOGLE_API_KEY=your_google_api_key

LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=streamlit-chatbot
```

Load the variables using:

```python
from dotenv import load_dotenv

load_dotenv()
```

### Security

Never commit `.env` to GitHub.

Your `.gitignore` should contain:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

# 🧠 What I Learned

This project helped me understand the fundamental building blocks of a LangChain application.

### 1. LLM Integration

How to connect applications with different LLM providers using LangChain.

```text
Application
     ↓
  LangChain
     ↓
     LLM
```

---

### 2. Prompt Templates

How to create reusable and structured prompts using:

```python
ChatPromptTemplate
```

---

### 3. LangChain Expression Language

How to combine components using the pipe operator:

```python
prompt | llm | output_parser
```

---

### 4. Output Parsers

How to process LLM responses using:

```python
StrOutputParser()
```

---

### 5. Local LLMs

How to run an open-source model locally using:

```text
Ollama + Llama 2
```

This helped me understand the difference between cloud and local LLM execution.

```text
Cloud:

Application
    ↓
LangChain
    ↓
Gemini API
    ↓
Cloud Model


Local:

Application
    ↓
LangChain
    ↓
Ollama
    ↓
Llama 2
    ↓
Local Machine
```

---

### 6. Switching LLM Providers

The project demonstrated that the same LangChain pipeline can work with different LLM providers.

```text
                 ┌── Gemini
                 │
LangChain ───────┤
                 │
                 └── Ollama + Llama 2
```

---

### 7. Streamlit

How to create an interactive AI application using Python without building a separate frontend.

---

### 8. Environment Variables

How to safely manage API keys using:

```text
.env
python-dotenv
```

instead of hardcoding secrets in source code.

---

### 9. LangSmith

How to trace, debug, monitor, and evaluate LangChain applications.

```text
LangChain Application
        ↓
    LangSmith
        ↓
Trace → Debug → Monitor → Evaluate
```

---

# 🚀 Running the Project

## Gemini Chatbot

Make sure your `.env` contains:

```env
GOOGLE_API_KEY=your_google_api_key
```

Then:

```bash
streamlit run app.py
```

---

## Ollama Chatbot

First run the local model:

```bash
ollama run llama2
```

Then start the application:

```bash
streamlit run localama.py
```

---

# 🔮 Future Improvements

This project is intentionally a basic LangChain chatbot and serves as the foundation for more advanced AI engineering projects.

Future improvements can include:

* 💬 Chat history and memory
* 📚 RAG
* 📄 Document ingestion
* 🗄️ Vector databases
* 🧪 RAG evaluation
* 🔗 LangGraph
* 🤖 Agentic AI
* 🛠️ Tool calling
* 🛡️ Guardrails
* 🔌 MCP
* ⚡ FastAPI backend
* 🐘 PostgreSQL
* ⚡ Redis
* 🐳 Docker
* ☁️ AWS deployment

---

# 🎯 Project Goal

The goal of this project was to understand the basic architecture of an LLM-powered application using LangChain.

```text
                         ┌──────────────┐
                         │   Streamlit  │
                         │      UI      │
                         └──────┬───────┘
                                ↓
                         ┌──────────────┐
                         │    Prompt    │
                         │   Template   │
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

                                │
                                ↓
                         ┌──────────────┐
                         │  LangSmith   │
                         │              │
                         │ Trace        │
                         │ Debug        │
                         │ Monitor      │
                         │ Evaluate     │
                         └──────────────┘
```

---

## 📌 Key Takeaway

**LangChain → Build and connect LLM application components**

**Streamlit → Build the user interface**

**Gemini → Cloud LLM**

**Ollama → Run LLMs locally**

**LangSmith → Trace, debug, monitor, and evaluate the application**
