from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline


llm= HuggingFacePipeline.from_model_id(
model_id="mistralai/Mistral-7B-Instruct-v0.3",
task="text-generation",
pipeline_kwargs={
    "max_new_tokens": 100,
    "temperature": 0.7,
}
)
model= ChatHuggingFace(llm=llm)
result = model.invoke("what is the capital of pakistan")
print(result.content)