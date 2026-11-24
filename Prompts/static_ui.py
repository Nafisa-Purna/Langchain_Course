from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

# import os
load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

st.header("Research Tool") 

user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):

    # model invoke -> with user prompt

    result = model.invoke(user_input)

    # show result -> st.write 
    st.write(result.content)

# print(bool(os.getenv("GROQ_API_KEY")))

# available_models = [
#     "openai/gpt-oss-120b",
#     "openai/gpt-oss-20b",
#     "qwen/qwen3.6-27b",
#     "llama-3.3-70b-versatile",
#     "llama-3.1-8b-instant"
# ]