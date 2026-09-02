from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
# hum yeh temprature ko set 0 sa 1.8 tak kar sakte aur 0.5 acha temp hai aur max completion token ma bata sakte hai humhe apne response kitne words hoga
chatmodel=ChatOpenAI(model="gpt-4", temperature=0.5, max_tokens=10)

result=chatmodel.invoke("what is the capital of pakistan")
# ager khali content dekhna hai toh result .content
print(result.content)