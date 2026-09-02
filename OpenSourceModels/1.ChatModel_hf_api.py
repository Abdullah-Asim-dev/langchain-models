from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# .env file se token load karein
load_dotenv()

# Active aur supported model use karein
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
 
)

# ChatHuggingFace wrapper initialize karein
Chat_model = ChatHuggingFace(llm=llm)

# Query run karein
result = Chat_model.invoke("what is the capital of pakistan")
print(result.content)
