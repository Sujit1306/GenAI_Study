from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from langchain_groq import ChatGroq
from langserve import add_routes #will help create APIs
import os 
from dotenv import load_dotenv
load_dotenv()

# Loading our llm
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model = "gemma2-9b-it")

# Create prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are an expert at languages."),
        ("user","convert the following from English to {language}: {text}."),
    ]
)

# Create output parser
parser = StrOutputParser()

# Create chain
chain = prompt|llm|parser

# Create a FastAPI app
app = FastAPI(title = "LangServe Demo",
              version = "1.0",
              description = "A simple API server using Langchain runnable interfaces")

# add chain routes
add_routes(
    app,
    chain,
    path = "/chain"
)

# finally executing this
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)