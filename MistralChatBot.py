import streamlit as st
from mistralai import Mistral

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Mistral AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Free Mistral AI Chatbot")

# --------------------------------------------------
# Load API Key
# --------------------------------------------------

MISTRAL_API_KEY = st.secrets["MISTRAL"]["api_key"]

if not MISTRAL_API_KEY:
    st.error("Please add your API key to .streamlit/secrets.toml")
    st.stop()

# --------------------------------------------------
# Initialize Client
# --------------------------------------------------

client = Mistral(api_key=MISTRAL_API_KEY)

# --------------------------------------------------
# Chat Memory
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# Display Chat History
# --------------------------------------------------

for msg in st.session_state.messages:
    
    if msg["role"] == "user":
        with st.chat_message("user", avatar="👤"):
            st.write(msg["content"])

    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.write(msg["content"])

# --------------------------------------------------
# Chat Input
# --------------------------------------------------

prompt = st.chat_input("Type your message...")

if prompt:

    # Show user message
    with st.chat_message("user", avatar="👤"):
        st.write(prompt)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Send to Mistral
    with st.spinner("🤖 Thinking..."):

        response = client.chat.complete(
            model="mistral-small-latest",
            messages=st.session_state.messages
        )

        reply = response.choices[0].message.content

    # Display AI message
    with st.chat_message("assistant", avatar="🤖"):
        st.write(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )