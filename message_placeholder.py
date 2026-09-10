from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []
# load chat history
# This opens chat_history.txt and reads its contents
# readlines() → reads all lines from the file.
# extend() → adds those lines to chat_history.

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
# SYSTEM: You are a helpful customer support agent
# CHAT HISTORY: [previous conversation]
# HUMAN: Where is my refund?

prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})


print(prompt)
