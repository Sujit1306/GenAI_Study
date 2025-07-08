import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "STREAMLIT_DEMO"

from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistanct, please respond to the question asked."),
        ("user","Question: {input}")
    ]
)

# Streamlit framework
st.title("Langchain demo with Gemma2")
input_text = st.text_input("What question do you have in mind?")

# calling LLM model
llm = ChatGroq(model = "gemma2-9b-it")

parser = StrOutputParser()
chain = prompt|llm|parser

if input_text:
    st.write(chain.invoke({"input":input_text}))