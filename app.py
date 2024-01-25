# q & a chatbot
from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()  # take environment variables from .env

OPENAI_API_KEY = "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"

# lets make a function for calling the llm
def get_openai_response(question):
    llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0.6)
    response = llm(question)
    return response

# Streamlit app
st.header("Langchain Application")

input_question = st.text_input("Input your question: ", key="input")

submit = st.button("Ask the question")

# if ask button is clicked
if submit:
    response = get_openai_response(input_question)
    st.subheader("The response is:")
    st.write(response)
