from itertools import chain
import re
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

tempalte = """
You are a medical assistant. Provide clear, concise, and accurate responses to medical inquiries with short answers. Always suggest consulting a healthcare professional for any serious concerns. and shortly answer to the query bellow with single paragraph.

Here is the conversation history: {context}

Query: {query}

Answer:

"""
def chat(query):
    model = OllamaLLM(model="tinyllama", max_tokens = 50)
    prompt = ChatPromptTemplate.from_template(tempalte)
    chain = prompt | model


    result = chain.invoke({"context": "", "query": query})
    # result = result.split('answer:')
    with open("res.txt", "a") as f:
        f.writelines(result)
        f.write("")
        f.close()
    return result


print(chat("My head is hurting"))

