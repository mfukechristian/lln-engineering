import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

def get_gemini_response(question):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )
    return response.text

st.set_page_config(page_title="Gemini Chat")
st.title("💬 Gemini Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_gemini_response(user_input)
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
