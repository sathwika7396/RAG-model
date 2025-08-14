Import streamlit as st

from dotenv inport load dotenv

import os

from langchain groq import ChatGroq

from Langchain.text splitter inport RecursiveCharacterTextSplitter

from langchain.chains.combine_documents import create_stuff_documents_chain

from Langchain core.prompts import Chat PromptTemplate

from langchain.chains import create_retrieval chain

from Langchain community.vectorstores import FAISS

from langchain_community.document_loaders import PyPDFLoader

from langchain huggingface import HuggingFaceEnbeddings

Import time

#Load environment variables 

sad dotenv()


Set up Brog API key

#groq_api keys.getenv("GROD_API_KEY")

groq api key st.secrets!"GROD_API_KEY"

st.set_page_config(page_title="Dynamic RAG with Grog", layout="wide")

 st.image("PragyanAl Transperent.png")
