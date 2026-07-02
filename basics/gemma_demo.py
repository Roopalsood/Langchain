from langchain_ollama import ChatOllama


try:
    llm = ChatOllama(model="gemma:2b") #model is running locally so don't need an api key

    questions = input("Enter the question: ")

    response = llm.invoke(questions)
    # print(response) returns a response body with a lot of metadata.
    
    print(response.content)

except Exception as e:
    print("Error: ", e)