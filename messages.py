from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)

# This Python program is a very simple LangChain chatbot example that sends a fixed conversation to an OpenAI model and then adds the AI's response back into the conversation. First, from langchain_core.messages import SystemMessage, HumanMessage, AIMessage imports three types of messages: SystemMessage gives instructions to the AI, HumanMessage represents the user's message, and AIMessage represents the AI's response.
# SystemMessage(content='You are a helpful assistant') tells the AI how to behave, and HumanMessage(content='Tell me about LangChain') is the question being sent to the AI.
# Then result = model.invoke(messages) sends both messages together to the AI model, and the AI generates an answer, which is stored inside result.
# result.content contains only the actual text of the AI's answer. The line messages.append(AIMessage(content=result.content)) then creates an AIMessage containing that answer and adds it to the end of the messages list. Finally, print(messages) prints the complete conversation, which now looks conceptually like: System → "You are a helpful assistant", Human → "Tell me about LangChain", AI → "LangChain is...". 
