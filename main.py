from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

mykey =  os.getenv("openai_api")

# Set the Pinecone API key as an environment variable
os.environ["PINECONE_API_KEY"] = os.getenv("pinecone_api")

print(os.environ["PINECONE_API_KEY"] )
print(mykey)