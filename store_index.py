from src.helper import load_pdf, Text_Split, download_hugging_face_embd
import os
from pinecone import Pinecone, ServerlessSpec
from langchain.vectorstores import Pinecone as LangchainPinecone
from dotenv import load_dotenv
import sys
from Exception.logger import logging
from Exception.exception import CustomException

load_dotenv()


class MedicalChatbotIndex:
    def __init__(self, index_name="medical-chatbot"):
        load_dotenv()
        self.index_name = index_name
        self.pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.embeddings = download_hugging_face_embd()
        self.docsearch = None

    def setup_index(self):
        try:
            if self.index_name not in self.pc.list_indexes().names():
                logging.info(f"Creating new index: {self.index_name}")
                self.pc.create_index(
                    name=self.index_name,
                    dimension=384,
                    metric="cosine",
                    spec=ServerlessSpec(cloud="aws", region="us-east-1")
                )
            else:
                print(f"Index {self.index_name} already exists")
                logging.info(f"Index {self.index_name} already exists")

            self.index = self.pc.Index(self.index_name)
            index_stats = self.index.describe_index_stats()

            if index_stats.total_vector_count == 0:
                self.load_and_store_embeddings()
            else:
                logging.info(f"Index already contains {index_stats.total_vector_count} vectors. Skipping embedding storage.")
                self.docsearch = LangchainPinecone(self.index, self.embeddings, "text")
                return self.docsearch

        except Exception as e:
            logging.error(f"An error occurred in setup_index: {str(e)}")
            raise CustomException(e, sys)

    def load_and_store_embeddings(self):
        try:
            logging.info("Index is empty. Loading and storing embeddings.")
            extracted_data = load_pdf("data/")
            text_chunks = Text_Split(extracted_data)

            self.docsearch = LangchainPinecone.from_texts(
                texts=[t.page_content for t in text_chunks],
                embedding=self.embeddings,
                index_name=self.index_name
            )
            logging.info("Embeddings stored successfully")
            return self.docsearch
        
        except Exception as e:
            logging.error(f"An error occurred in load_and_store_embeddings: {str(e)}")
            raise CustomException(e, sys)

    def query_index(self, query):
        if self.docsearch is None:
            raise CustomException("Index not set up. Call setup_index() first.", sys)
        try:
            results = self.docsearch.similarity_search(query)
            return results
        except Exception as e:
            logging.error(f"An error occurred during query: {str(e)}")
            raise CustomException(e, sys)
