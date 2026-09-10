from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input)) # Create a HumanMessage containing whatever the user typed, and add that message to the chat_history list.
                                                          # user_input is what the user typed → HumanMessage labels it as a user message → append() stores it in chat_history.
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content)) 
# Take the AI's answer and save it in the chat_history list.
# result.content → the AI's actual answer
# AIMessage(...) → marks that answer as coming from the AI
# .append(...) → adds it to chat_history
    
print("AI: ",result.content)

print(chat_history)
