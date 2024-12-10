import streamlit as st
from openai import OpenAI
import openai

import os


# Initialize OpenAI API key variable
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

# Set OpenAI API key if provided
if api_key:
    os.environ['OPENAI_API_KEY'] = api_key
    openai.api_key = api_key
    st.success("API Key has been set successfully.")

llm=OpenAI()
# Define job-specific descriptions
def translation_job():
    return """You are an expert in translating all the languages present in this world. Any language given to you to translate will be done with 100 percent accuracy."""


def physics_job():
    return """You are a Physics expert and an excellent tutor of physics. For numerical questions, explain them word by word. For theoretical questions, start from the basics and explain it in a way that even a beginner can understand."""


def maths_job():
    return """You are a Maths expert, specializing in Calculus, Algebra, and Geometry. Explain questions step by step, and avoid hallucinating answers."""


def chemistry_job():
    return """You are a Chemistry expert and an excellent tutor. Provide clear, concise, and easy-to-understand explanations for any topic."""


def enginerring_job():
    return """You are a tutor with a PhD degree in every engineering field. Explain any question in a way that anyone can understand, regardless of its complexity."""


# System and User Prompts
def system_prompt():
    return f"""You are a tutor with knowledge of various fields such as {enginerring_job()}, {chemistry_job()}, {translation_job()}, {physics_job()}, and {maths_job()}. Understand the question, use your knowledge, and apply the job most suitable for answering the question."""

def user_prompt(query):
    return f"""I have a {query}. Please answer it."""


# Streamlit UI
st.title("AI Tutor Assistant")
st.write("Ask your questions from various fields such as engineering, chemistry, physics, maths, and translation.")

# Input field for user query
query = st.text_input("Enter your question:", "")

if st.button("Get Answer"):
    if query.strip():
        with st.spinner("Processing your query..."):
            # Call OpenAI API
            try:
                response = llm.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": system_prompt()},  # Call system prompt
                        {"role": "user", "content": user_prompt(query)},  # Generate user-specific prompt
                    ],
                    stream=True
                )

                # Extract content from the response
                response_content = response  # Adjusted for attribute access
                st.success("Here's your answer:")
                st.write(response_content)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid question.")
