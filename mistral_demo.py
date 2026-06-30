from langchain_ollama import ChatOllama

try:
    llm = ChatOllama(model="mistral") #Will not execute because of space and it should be pulled in cmd using ollama pull mistral command.
    
    questions = input("Enter the question: ")
    response = llm.invoke(questions)

    print(response.content)

except Exception as e:      
    print("Error: ", e)