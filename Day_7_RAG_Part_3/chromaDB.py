from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import retriever
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma

#envriornment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

#embedding model
embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=api_key
)

# loading existing database
vector_db = Chroma(
    embedding_function=embedding_model,
    persist_directory="./chroma_db"
)

# retriever settings
retriever = vector_db.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10
    }
)

# questions to be asked
question = input("Ask a question: ")

retrieved_docs = retriever.invoke(question)

# retrieving context
context = "\n\n".join(
    doc.page_content
    for doc in retrieved_docs
)

# llm model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=api_key
)

# prompt
prompt = f"""
You are a PDF assistant. Answer the question using the information provided in the context. If the answer is not available in the context, say: "I could not find the answer in the PDF." Donot add information from outside.
Context:
{context}
Question/Query:
{question}
"""

# LLM Invocation
response = llm.invoke(prompt)

# printing the response
print("\nAnswer:")
print(response.content[0]['text'])
