from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

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

# print(os.getenv("OPENAI_API_KEY"));
#streamlit framework
st.title('Langchain Demo with OpenAI API') 
input_text=st.text_input("Search the topic u want")


#OpenAI LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.environ["OPENAI_API_KEY"]
)
output_parser=StrOutputParser()

chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))
