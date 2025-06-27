import os
import streamlit as st
from dotenv import load_dotenv
from litellm import completion 

load_dotenv()
os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")

model = [
    "Select a model",
    "openrouter/google/gemini-2.0-flash-exp:free",
    "openrouter/deepseek/deepseek-r1-0528-qwen3-8b:free",
    "openrouter/meta-llama/llama-3.3-8b-instruct:free",
    "openrouter/microsoft/mai-ds-r1:free",
    "openrouter/nvidia/llama-3.3-nemotron-super-49b-v1:free"
    ]

st.set_page_config(page_title = "OpenRouter Multi Model Chat App", layout="centered")

st.title("OpenRouter Multi Model Chat App")
user_model = st.selectbox("Select a model", model)
user_prompt=st.text_area("Enter your prompt here:", height=100, placeholder="Type your message...")

if st.button("Get Response"):
    if user_prompt:
        with st.spinner("Generating response..."):
            try:
                response = completion(
                    model=user_model,
                    messages=[{
                        "role": "user", 
                        "content": user_prompt,
                        "language": "en"
                        }],
                )
                st.success("Response generated successfully!")
                content = response["choices"][0]["message"]["content"]
                st.write(content)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt before clicking the button.")
        