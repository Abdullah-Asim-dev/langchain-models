from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
# yeh batao ga ka open ai ka kon sa models sa baat karni hai 
llm = OpenAI(model="gpt-3.5-turbo-instruct")
# model ko invoke kiya yhe call kiya
result=llm.invoke("what is the capital of Pakistan?")
print(result)
