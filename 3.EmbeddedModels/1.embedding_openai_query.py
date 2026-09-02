from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

Embedding=OpenAIEmbeddings(model="text-embedding-3-large")
result=Embedding.embed_query("what is the capital of usa? ")
print(str(result))