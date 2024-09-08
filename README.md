# AI-Medical-ChatBot-using-LLM

# Steps to run the Project:

### Clone the Repository:

```bash
git clone https://github.com/noumanirshad/AI-Medical-ChatBot-using-LLM.git
```

### Create a new virtual environment in window command prompt.
```bash
1: python -m venv myenv
```

### Activate the virtual environment
``` bash
2: myenv\Scripts\activate
```

### Install the 'requirements.txt' 
``` bash
3: pip install -r requirements.txt
```

### Create a .env file in the root directory and add your Pinecone credentials as follows:
```
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```
```
# run the following command
python store_index.py
# Finally run the following command
python app.py

```
### Now,

* open up localhost:
* Techstack Used:
* Python
* LangChain
* Flask
* Meta Llama2
* Pinecone

Download the pre-trained model:
Visit the following link: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
Download the quantized model file llama-2-7b-chat.ggmlv3.q4_0.bin and place it in the model directory.
Run indexing script (optional):

python store_index.py
This script helps pre-process the medical information for faster retrieval during chatbot interactions.

Run the chatbot:

python app.py

Access the chatbot:

Open http://localhost:5000/ in your web browser to interact with the medical chatbot.
