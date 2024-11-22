import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load API key from environment variable
load_dotenv()

api_key = os.getenv("HUGGINGFACE_API_KEY")

if not api_key:
    raise ValueError("API key not found. Set the 'HUGGINGFACE_API_KEY' environment variable.")

client = InferenceClient(api_key=api_key)

# Function to check if the query is education-related

def is_education_related(question):
    education_keywords = ["education", "learn", "school", "university", "college", "teaching", "studying", "academic", "course"]
    return any(keyword in question.lower() for keyword in education_keywords)

# User query
user_query = input("What I can help with? :")

if is_education_related(user_query):
    messages = [
        {"role": "user", "content": user_query}
    ]

    # Get the response
    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.2-1B-Instruct",
        messages=messages,
        max_tokens=500
    )

    print(completion.choices[0].message)
else:
    print("Sorry, this model is configured to answer only education-related questions.")
