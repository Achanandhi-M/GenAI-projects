from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.document_loaders import DataFrameLoader
from langchain.embeddings import HuggingFaceEmbeddings  # Updated to HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
import pandas as pd
import os
from huggingface_hub import InferenceApi

# Load API key
load_dotenv()
api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not api_key:
    raise ValueError("API key not found. Set the 'HUGGINGFACE_API_TOKEN' environment variable.")

# Load data
data_path = '/home/acha/student_details.xlsx'
if not os.path.exists(data_path):
    raise FileNotFoundError(f"The specified file does not exist: {data_path}")

data = pd.read_excel(data_path)
data['combined'] = data.apply(lambda row: ' '.join(row.astype(str)), axis=1)

# Initialize DataFrameLoader
loader = DataFrameLoader(data, page_content_column='combined')
docs = loader.load()

# Use Hugging Face Embeddings (Serverless)
embedding_model_name = "sentence-transformers/multi-qa-MiniLM-L6-cos-v1"

# Instantiate HuggingFaceEmbeddings instead of HuggingFaceHubEmbeddings
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)

# Build FAISS Vector Store
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever()

# Set up inference API for Llama model (Serverless inference)
llama_api = InferenceApi(repo_id="meta-llama/Llama-3.2-1B-Instruct", token=api_key)

# Create a function to query the Llama model
def query_llama_model(prompt):
    response = llama_api(inputs=prompt, parameters={"max_new_tokens": 150, "temperature": 0.7, "top_k": 50})
    return response.get("generated_text", "No response from the model.")

# Setup HuggingFace Pipeline for language model (using the serverless inference method)
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B-Instruct")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-1B-Instruct")

# Create a text generation pipeline with adjusted parameters
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=150,  # Generate up to 150 new tokens
    temperature=0.7,  # Control randomness (lower values make output more deterministic)
    top_k=50  # Limit sampling to the top k tokens
)

# Wrap the pipeline in HuggingFacePipeline
llm = HuggingFacePipeline(pipeline=pipe)

# Setup RetrievalQA chain with the retriever and language model
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

# Export qa_chain for use
__all__ = ["qa_chain"]
