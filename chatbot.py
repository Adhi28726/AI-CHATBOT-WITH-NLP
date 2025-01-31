import spacy
from collections import defaultdict

def load_nlp_model():
    return spacy.load("en_core_web_sm")

def get_response(user_input, response_dict, nlp):
    doc = nlp(user_input.lower())
    for keyword, response in response_dict.items():
        if keyword in doc.text:
            return response
    return "I'm sorry, I don't understand that."

def chatbot():
    nlp = load_nlp_model()
    response_dict = {
        "hello": "Hi there! How can I help you?",
        "hi": "Hello! What can I do for you?",
        "bye": "Goodbye! Have a great day!",
        "name": "I'm a chatbot created using spaCy!",
        "weather": "I can't check the weather right now, but it's always a good idea to look outside!",
        "help": "I'm here to assist you. You can ask me general questions!"
    }
    
    print("Chatbot: Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input, response_dict, nlp)
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()
