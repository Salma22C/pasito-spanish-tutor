import streamlit as st
from tutor import get_tutor_response

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Pasito AI Tutor",
    page_icon="🇪🇸",
    layout="centered",
)

# -----------------------------
# State Initialization
# -----------------------------
# Keeps track of the chat history across reruns
if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# App header & Sidebar
# -----------------------------
st.title("🇪🇸 Pasito AI Tutor")
st.caption("A beginner-friendly AI Spanish tutor for CEFR A1 learners")
st.divider()

with st.sidebar:
    st.header("👤 Student Profile")
    student_name = st.text_input("Your name", value="Salma")
    spanish_level = st.selectbox("Spanish level", ["A1 Beginner"])
    explanation_language = st.selectbox("Explanation language", ["English", "Arabic"])
    
    st.divider()
    st.subheader("📊 Progress")
    st.progress(10)
    st.write("Completed topics: **2**")
    st.write("Current streak: **1 day**")

    # Optional: Clear history button
    if st.button("Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# -----------------------------
# Learning controls
# -----------------------------
st.subheader("Choose a learning mode")
mode = st.selectbox(
    "What would you like to do?",
    [
        "📚 Learn a topic",
        "✍️ Correct my sentence",
        "📝 Generate a quiz",
        "💬 Practice conversation",
    ],
)

# Dynamic placeholders
placeholders = {
    "📚 Learn a topic": "Example: Teach me Spanish greetings",
    "✍️ Correct my sentence": "Example: Yo soy vivo en Egipto",
    "📝 Generate a quiz": "Example: Greetings and introductions",
    "💬 Practice conversation": "Example: Introductions, food, family, or travel",
}

user_input = st.text_area(
    "Your request",
    placeholder=placeholders.get(mode, ""),
    height=100,
)

col1, col2 = st.columns(2)
with col1:
    difficulty = st.selectbox("Difficulty", ["Easy", "Normal"])
with col2:
    lesson_size = st.selectbox("Lesson size", ["Short", "Medium"])

ask_button = st.button("Ask Pasito 🚀", type="primary", use_container_width=True)

# -----------------------------
# Action & Response Handling
# -----------------------------
if ask_button:
    if not user_input.strip():
        st.warning("Please enter a topic, sentence, or request first.")
    else:
        # 1. Save the user's message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        # 2. Call the AI tutor
        with st.spinner("Pasito is thinking..."):
            try:
                tutor_response = get_tutor_response(
                    user_message=user_input,
                    explanation_language=explanation_language,
                )

                # 3. Save the tutor's response
                st.session_state.messages.append(
                    {"role": "assistant", "content": tutor_response}
                )

            except Exception as error:
                st.error(f"Something went wrong: {error}")
        

# -----------------------------
# Display Persistent Conversation
# -----------------------------
if st.session_state.messages:
    st.divider()
    st.subheader("💬 Conversation History")
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# -----------------------------
# Footer
# -----------------------------
st.divider()
st.caption("Pasito a pasito — step by step 🇪🇸")