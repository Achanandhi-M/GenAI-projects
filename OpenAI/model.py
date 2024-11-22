import os
import pandas as pd
from dotenv import load_dotenv
from langchain.document_loaders import DataFrameLoader
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
import openai

# Load API key from environment variable
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Set the 'OPENAI_API_KEY' environment variable.")

openai.api_key = api_key

# Step 1: Load data from the Excel file
data_path = '/home/acha/Downloads/student_details.xlsx'
if not os.path.exists(data_path):
    raise FileNotFoundError(f"The specified file does not exist: {data_path}")

data = pd.read_excel(data_path)

# Step 2: Concatenate all columns for each row into a single string
data['combined'] = data.apply(lambda row: ' '.join(row.astype(str)), axis=1)

# Step 3: Initialize the DataFrameLoader with the combined text column
loader = DataFrameLoader(data, page_content_column='combined')
docs = loader.load()

# Step 4: Use OpenAI embeddings for document embedding
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# Step 5: Build the FAISS vector store
vectorstore = FAISS.from_documents(docs, embeddings)

# Step 6: Setup the retriever and Retrieval-based QA system
retriever = vectorstore.as_retriever()

# Define a function to query OpenAI GPT-3.5
def query_openai_gpt(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}],
        max_tokens=500
    )
    return response['choices'][0]['message']['content']

# Define the RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=query_openai_gpt,
    retriever=retriever
)

# Export qa_chain for external use
__all__ = ["qa_chain"]
