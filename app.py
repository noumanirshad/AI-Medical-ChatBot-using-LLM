from flask import Flask, render_template, jsonify, request
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from store_index import MedicalChatbotIndex
from src.prompt import *
from langchain.chat_models import ChatOpenAI
import os

app = Flask(__name__)

load_dotenv()

mykey = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key=mykey, model="gpt-3.5-turbo", temperature=0.5, model_kwargs={"top_p": 0.9})

def setup_qa():
    chatbot_index = MedicalChatbotIndex()
    docsearch = chatbot_index.setup_index()

    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain_type_kwargs = {"prompt": PROMPT}

    qa = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
        return_source_documents=True, 
        chain_type_kwargs=chain_type_kwargs)
    return qa

qa = setup_qa()

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    result = qa({"query": msg})
    return jsonify({"response": result["result"]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)