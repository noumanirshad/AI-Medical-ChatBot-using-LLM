import os
from pinecone import Pinecone, ServerlessSpec
from langchain.vectorstores import Pinecone as LangchainPinecone
from dotenv import load_dotenv
from src.helper import load_pdf, Text_Split, download_hugging_face_embd
from Exception.logger import logging
from Exception.exception import CustomException
from store_index import MedicalChatbotIndex



def main():
    chatbot_index = MedicalChatbotIndex()
    chatbot_index.setup_index()
    
    # Example query
    query_results = chatbot_index.query_index("What are the symptoms of diabetes?")
    for result in query_results:
        print(result.page_content)

if __name__ == "__main__":
    main()