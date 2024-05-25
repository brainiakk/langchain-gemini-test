import os
from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI

load_dotenv()

llm = ChatVertexAI(model_name="gemini-1.5-pro-001", temperature=0.4)

while True:
    text = input("Enter your query here >>>> ")
    response = llm.invoke(text)
    print(response.content)