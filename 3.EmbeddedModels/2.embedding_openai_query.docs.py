from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

Embedding=OpenAIEmbeddings(model="text-embedding-3-large")
documents=[
    "pakistan is the capital of islamabad",
    "usa is the capital of washington",
    "the capital of india is new delhi"
]
result=Embedding.embed_documents(documents)
print(str(result))