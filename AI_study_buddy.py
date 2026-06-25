# AI Rule - based Chatbot (Personal Assistant)

import datetime
import time

name = input("Welcome, Enter Your Name: ")
currentHour = datetime.datetime.now().hour

if 5 <= currentHour <= 11:
    print(currentHour,name)
elif 11 <= currentHour <= 17:
    print(currentHour,name)
elif 17 <= currentHour <= 20:
    print(currentHour,name)
else:
    print("Good Night, ", name)



print("Hello ! I Am Your Study Buddy Helper.")
print("If you feel to leave the chat, type Bye to exit!")
print("What's On Your Mind?")

# chatbot responses
responses = {
    "hello" : "Hey, what's up? How can I help you today?",
    "help me" : "Sure, In which context do you need help?",
    "who are you": "I am smart AI chatbot",
    "how are you": "I am fine. What you are going to do this weekend?",
    "what's the color of the sky":"Easy! The color of the sky is skyblue.",
    "happy": "Great to hear that!",
    "motivate me": "All power is within you. You can do anything and everything.",
}

# Function that takes questions and generate responses.
def responseGenerator(userQuestion):
    userQuestion = userQuestion.lower()
    
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "Sorry, I can't Understand."

    
while True:
    userInput = input("You: ")

    if "bye" in userInput.lower():
        print("Study Buddy: Goodbye!")
        break

    result = responseGenerator(userInput)
    print("Study Buddy:", result)