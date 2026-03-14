import streamlit as st
from chatbot_model import get_response

st.set_page_config(page_title="AI University Admission Chatbot")

st.title("🎓 AI University Admission Chatbot")

st.sidebar.title("About")
st.sidebar.info(
"""
This chatbot helps students with university admission questions.

Technologies used:
Python, NLP, Scikit-learn, Streamlit
"""
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ask a question about university admission")

if st.button("Send"):

    if user_input:

        with st.spinner("Thinking..."):
            response = get_response(user_input)

        st.session_state.messages.append(("You", user_input))
        st.session_state.messages.append(("Bot", response))

# Display chat
for sender, message in st.session_state.messages:
    if sender == "You":
        st.write(f"🧑 **You:** {message}")
    else:
        st.write(f"🤖 **Bot:** {message}")
