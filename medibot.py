import streamlit as st
from transformers import pipeline

st.title("🩺 MediBot")

@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

model = load_model()

user_input = st.chat_input("Ask anything")

if user_input:
    st.chat_message("user").markdown(user_input)
    output = model(
        f"Rewrite this into a clear medical answer:\n{user_input}",
        max_new_tokens=150
    )
    st.chat_message("assistant").markdown(output[0]["generated_text"])
