from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

def initialize_guidelines():
    # Mock Clinical Guidelines
    guidelines = [
        "Hypertension: If BP > 140/90, prescribe Lisinopril 10mg.",
        "Diabetes: Target HbA1c should be below 7.0%."
    ]
    docs = [Document(page_content=t) for t in guidelines]
    vectorstore = Chroma.from_documents(
        documents=docs, 
        embedding=OpenAIEmbeddings(),
        persist_directory="./chroma_db"
    )
    return vectorstore.as_retriever()