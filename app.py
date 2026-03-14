import streamlit as st
from chatbot_model import get_response

st.title("🎓 AI University Admission Chatbot")

user_input = st.text_input("Ask your question")

if st.button("Ask"):
    if user_input:
        response = get_response(user_input)
        st.write("### Bot Response:")
        st.success(response)