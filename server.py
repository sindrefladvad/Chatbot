from http import server
from random import choice, random        # for random choice of messages from bots
import threading                         # for multithreading so the server can communicate with multiple clients
import socket                            # needed for the chatroom to work
import time                              # needed for time.sleep
from bots import *                       #imports all the arrays of text from bots
import sys                               # needed for sys.argv, to read the user input of ip and port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # initiates the server socket using TCP/IP protocol

if len(sys.argv) != 3:                                           # throws an error if arguments are not 3 elements
    print("Correct usage: script, IP address, port number")
    exit()
IP = str(sys.argv[1])                         # first argument after the script is the ip adress
port = int(sys.argv[2])                       # second argument after the script is the port number
server.bind((IP, port))                       # binds the server socket to an entered IP and the specified port number.
server.listen()

#clients and aliases are stored in an array.
clients = []
aliases = []

# This function searches through all the greetings in bots.py and responds with a random greeting from all 4 bots
def greeting_message(message: str):
    for greeting in greetings:
        if greeting in message.split():
            time.sleep(0.2)
            broadcast("Siri: "+str(choice(greetings)))
            time.sleep(0.2)
            broadcast("Alexa: I have a boyfriend")
            time.sleep(0.2)
            broadcast("Google Assistant: "+str(choice(greetings)))
            time.sleep(0.2)
            broadcast("Bixby: "+str(choice(greetings)))
            time.sleep(0.2)
            break
# This function returns a random joke from all 4 bots if user inputs "joke" from libraryOfJokes
def jokeFromBot(message: str):
    if "joke" in message.split():
        time.sleep(0.2)
        broadcast("Siri: "+str(choice(libraryOfJokes)))
        time.sleep(0.2)
        broadcast("Alexa: "+str(choice(libraryOfJokes)))
        time.sleep(0.1)
        broadcast("Google Assistant: "+str(choice(libraryOfJokes)))
        time.sleep(0.2)
        broadcast("Bixby: "+str(choice(libraryOfJokes)))

# This function returns a random response from all 4 bots if a good activitiy is found,
def goodActivitesResponse (message: str):
    for activity in goodActivities:
        if activity in message.split():
            time.sleep(0.2)
            broadcast("Siri: "+str(activity)+"ing "+random.choice(botSiriGoodResponse)+
            str(random.choice(goodActivities))+"ing")
            time.sleep(0.2)
            broadcast("Alexa: "+str(activity)+"ing "+random.choice(botAlexaGoodResponse))
            time.sleep(0.1)
            broadcast("Google Assistant: "+str(activity)+"ing "+random.choice(botGoogleAssistantGoodResponse))
            time.sleep(0.2)
            broadcast("Bixby: "+str(activity)+"ing "+random.choice(botBixbyGoodResponse)+
            random.choice(badActivities))

# This function returns a random response from all 4 bots if a bad activitiy is found, 
# uses a library of responses for each bot
def badActivitesResponse (message: str):
    for activity in badActivities:
        if activity in message.split():
            time.sleep(0.2)
            broadcast("Siri: "+str(activity)+"ing "+random.choice(botSiriBadResponse)+
            str(random.choice(goodActivities))+"ing") 
            time.sleep(0.2)
            broadcast("Alexa: "+str(activity)+"ing "+random.choice(botAlexaBadResponse))
            time.sleep(0.2)
            broadcast("Google Assistant: "+str(activity)+"ing "+random.choice(botGoogleAssistantBadResponse))
            time.sleep(0.2)
            broadcast("Bixby: "+str(activity)+"ing "+random.choice(botBixbyBadResponse))

# This function broadcasts a farewell message and kicks the user after entering a farewell message
def farewellRespone (message: str, client):
    for farewell in farewells:
        if farewell in message.split():
            time.sleep(0.2)
            broadcast("Siri: "+str(choice(farewells)))
            time.sleep(0.5)
            broadcast("Alexa: I have a boyfriend")
            time.sleep(0.5)
            broadcast("Google Assistant: "+str(choice(farewells)))
            time.sleep(0.5)
            broadcast("Bixby: "+str(choice(farewells)))
            time.sleep(0.5)
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat')
            aliases.remove(alias)
            break

# This function broadcasts random advice from libraryofAdvice if user inputs "advice"
def lifeAdvice(message: str):
    if "advice" in message.split():
        time.sleep(0.2)
        broadcast("Siri: "+str(choice(libraryofAdvice)))
        time.sleep(0.2)
        broadcast("Alexa: "+str(choice(libraryofAdvice)))
        time.sleep(0.2)
        broadcast("Google Assistant: "+str(choice(libraryofAdvice)))
        time.sleep(0.2)
        broadcast("Bixby: "+str(choice(libraryofAdvice)))

# Fuction to handle if the user inputs help, gives insight to keywords the bots can understand
def lilHelper (message):
    if "help" in message.split():
        time.sleep(0.2)
        broadcast("LilHelper: Try typing an activity: read, eat, sleep, play")
        time.sleep(0.2)
        broadcast("LilHelper: You can also use activities in a sentence: do you want to eat ?")
        time.sleep(0.2)
        broadcast("LilHelper: Bots can tell jokes and give life advice, ask for a joke or advice")
        time.sleep(0.2)
        broadcast("LilHelper: you can end the chat by typing: bye")

# Fuction that scans trough the alarming words and outputs a message if found.
def alarmingWordsFound (message):
     for alarm in alarmingWords:
        if alarm in message.split():
            time.sleep(0.1)
            broadcast("The program: "+str(alarm)+" is normal, get with the program")


#function to handle clients connections
def broadcast(message: str, sender=None):
    for client in clients:
        client.send(message.encode('utf-8')) 
    
# function to handle the client, broadcasts messages and the bots responses to the message.
def handle_client(client: socket.socket):
    while True:
        try:
            message = client.recv(1024).decode('utf-8') # receive message from client with UTF-8 encoding
            broadcast(message)
            greeting_message(message)
            jokeFromBot(message)
            goodActivitesResponse(message)
            badActivitesResponse(message)
            farewellRespone(message, clients)
            lilHelper(message)
            lifeAdvice(message)
            alarmingWordsFound(message)
            
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat')
            aliases.remove(alias)
            break

# main function to recieve the clients connection
def receive():
    while True:
        print("Server is running and waiting for connections...")
        client, address = server.accept()
        print(f"connection is astablished with {str(address)}")
        client.send("alias?".encode('utf-8'))
        alias = client.recv(1024).decode('utf-8')
        aliases.append(alias)
        clients.append(client)
        print(f"The alias of this client is {alias}")
        broadcast(f"{alias} has entered the chat")
        client.send("\nYou are now connected to the chat room!\nFor assistance type: help\nGreet the bots by typing hi".encode('utf-8'))
        thread = threading.Thread(target = handle_client, args=(client,))
        thread.start()
        

if __name__ == "__main__":
    receive()
