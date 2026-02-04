# from sentence_transformers import SentenceTransformer
# from langchain_community.vectorstores import FAISS
# from langchain_core.documents import Document
# import os

# DATA_PATH = "data"
# DB_PATH = "vectorstore/db_faiss"

# # Load embedding model
# model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# docs = []

# for file in os.listdir(DATA_PATH):
#     if file.endswith(".txt"):
#         with open(os.path.join(DATA_PATH, file), "r", encoding="utf-8") as f:
#             docs.append(Document(page_content=f.read()))

# db = FAISS.from_documents(docs, model)
# db.save_local(DB_PATH)

# print("✅ FAISS rebuilt successfully")


import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

DATA_PATH = "data"
DB_PATH = "vectorstore/db_faiss"

os.makedirs(DB_PATH, exist_ok=True)

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

texts = []

for file in os.listdir(DATA_PATH):
    if file.endswith(".txt"):
        with open(os.path.join(DATA_PATH, file), "r", encoding="utf-8") as f:
            texts.append(f.read())

if not texts:
    raise ValueError("No .txt files found in data/")

# Create embeddings
embeddings = model.encode(texts, show_progress_bar=True)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, os.path.join(DB_PATH, "index.faiss"))

# Save raw texts
with open(os.path.join(DB_PATH, "texts.pkl"), "wb") as f:
    pickle.dump(texts, f)

print("✅ Vector store created successfully (NO LangChain)")
