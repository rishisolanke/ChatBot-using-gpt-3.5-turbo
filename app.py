import subprocess
import sys
from dotenv import load_dotenv
import os

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import langchain
except ImportError:
    install("langchain")
try:
    import openai
except ImportError:
    install("openai")
try:
    import streamlit as st
except ImportError:
    install("streamlit")
try:
    import dotenv
except ImportError:
    install("python-dotenv")

from langchain.llms import OpenAI
import streamlit as st
import openai

# Load environment variables from .env file if present
load_dotenv()

# Debugging: Print all environment variables to check if the secret is there
print("Environment Variables:", os.environ)

# Get the OpenAI API key from the environment variable
openai_api_key = os.getenv('OPEN_API_KEY')

# Check if the API key is available
if not openai_api_key:
    raise ValueError("OpenAI API key not found in environment variables")

openai.api_key = openai_api_key

def get_openai_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input_question = st.text_input("Input: ", key="input_key")

submit = st.button("Ask the question")

if submit:
    response = get_openai_response(input_question)
    st.subheader("The Response is")
    st.write(response)