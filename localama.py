from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

# for 3rd part integration
from langchain_community.llms import Ollama


import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"] = "streamlit-chatbot"


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please response to the user queries."),
        ("user","Question:{question}")
    ]
)

st.title('Langchain Demo with OpenAI API') 
input_text=st.text_input("Search the topic u want")


llm = Ollama(
    model="llama2" 
)
output_parser=StrOutputParser()

chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))

#first install OLLAMA FOR SETUP

# all modules in requirements.txt
# pip install -r requirements.txt


# extra import
# from langchain_community.llms import Ollama
# we changed the modal
# llm = Ollama(
#     model="llama2" 
# )

# in cmd
# ollama run llama2 
# it will download llama2 model locally 

# then again streamlit run localama.py