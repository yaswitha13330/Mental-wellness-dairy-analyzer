import os
import streamlit as st
import google.generativeai as genai

# Load Gemini API key from Hugging Face secrets
api_key = ("AIzaSyC2WVcvVWgT4Md9C9w-yYpL1Ixt0w839Z0")

if not api_key:
    st.error("🚨 Please set your GEMINI_API_KEY in Hugging Face Secrets.")
else:
    genai.configure(api_key=api_key)

    st.set_page_config(page_title="🧘 Gemini Mental Wellness Diary", layout="centered")
    st.title("🧘 Mental Wellness Diary Analyzer")
    st.markdown("Write your daily journal entry and get emotional insights + motivational support.")

    user_input = st.text_area("📝 How are you feeling today?", height=250, placeholder="I feel...")

    PROMPT = f"""
    Analyze the following journal entry:
    \"{user_input}\"
    1. What is the emotional tone?
    2. Are there any recurring thoughts or emotional themes?
    3. Give a short, personalized motivational message.
    """

    if st.button("Analyze"):
        if not user_input.strip():
            st.warning("Please enter something before analyzing.")
        else:
            with st.spinner("Gemini is analyzing your journal..."):
                try:
                    model = genai.GenerativeModel("gemini-pro")
                    response = model.generate_content(PROMPT)
                    st.subheader("🔍 Gemini's Insight")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"❌ Error from Gemini: {e}")
