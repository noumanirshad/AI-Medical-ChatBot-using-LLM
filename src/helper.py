from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
import sys
from Exception.logger import logging
from Exception.exception import CustomException


def load_pdf(data):
    try:
        logging.info("Loading PDF")
        loader = DirectoryLoader(data,
                    glob = "*.pdf",
                    loader_cls = PyPDFLoader)
        documents = loader.load()
        logging.info("Successfully Loading PDF file.")
        return documents
    
    except Exception as e:
        logging.error(f"An error occurred in helper file: {e}")
        raise CustomException(e, sys)


def Text_Split(extract_data):
    try:
        logging.info("Creating Chunks of text...")
        text_splitter = RecursiveCharacterTextSplitter(
            # Set a really small chunk size, just to show.
            chunk_size=500,
            chunk_overlap=20,
            length_function=len,
            is_separator_regex=False,
        )
    
        text_chunks = text_splitter.split_documents(extract_data)
        logging.info("Successfully Created Chunks of text...")
        return(text_chunks)
    
    except Exception as e:
        logging.error(f"An error occurred in helper file: {e}")
        raise CustomException(e, sys)


model_name = "sentence-transformers/all-MiniLM-L6-v2"
def download_hugging_face_embd():
    try:
        logging.info("Downloading Embeddings...")
        embeddings = HuggingFaceEmbeddings(model_name=model_name)
        logging.info("Successfully Downloading Embedding from HuggingFace")
        return embeddings
    except Exception as e:
        logging.error(f"An error occurred in helper file: {e}")
        raise CustomException(e, sys)