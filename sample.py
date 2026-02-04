from langchain_huggingface import HuggingFaceEndpoint
import os

HF_TOKEN = os.getenv("HF_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-v0.1",
    temperature=0.5,
    task="text-generation",
    model_kwargs={"token": HF_TOKEN},
    max_new_tokens=100,   # <-- pass explicitly here
)

response = llm.invoke("Tell me a joke")
print(response)
