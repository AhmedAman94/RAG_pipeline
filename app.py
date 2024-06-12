import streamlit as st
from rag_pipeline import *

# Streamlit UI
st.title("RAG Pipeline with GPT-4 Turbo")
st.write("Upload a PDF file and enter a query to get a response from the GPT-4 Turbo model.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
query = st.text_input("Enter your query:")

if uploaded_file is not None and query:
    with open("uploaded_file.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    file_path = "uploaded_file.pdf"
    response = rag_execute(file_path, query, chunk_size=500, chunk_overlap=50, model="gpt-4-turbo")
    st.write("Response:")
    st.write(response)
    
# import streamlit as st
# from rag_pipeline import rag_execute

# st.title("RAG Pipeline with GPT-4 Turbo")
# st.write("Upload a PDF file and enter a query to get a response from the GPT-4 Turbo model.")

# uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
# query = st.text_input("Enter your query:")

# if uploaded_file is not None and query:
#     with open("uploaded_file.pdf", "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     file_path = "uploaded_file.pdf"
#     response = rag_execute(file_path, query, chunk_size=500, chunk_overlap=50, model="gpt-4-turbo")
#     st.write("Response:")
#     st.write(response)

