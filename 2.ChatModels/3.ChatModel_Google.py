from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
Chat_model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-8b" )
result=Chat_model.invoke("what is the capital of pakistan")
print(result.content)