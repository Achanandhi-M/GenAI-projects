import streamlit as st
from model import qa_chain

st.title("Student Query System")

query = st.text_input("Ask a question about students:")
if query:
    response = qa_chain.run(query)
    st.write(response)
