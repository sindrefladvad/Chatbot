from ast import alias
import threading
import socket
from bots import *
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a client socket using TCP/IP protocol
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()
IP = str(sys.argv[1])           # first argument after the script is the ip adress
port = int(sys.argv[2])         # second argument after the script is the port number
client.connect((IP, port))      # connect to server with host and port number
print("Welcome to the chatroom - Bots are listening to your conversations!")

alias = input('Choose a nickname: ')     # get nickname for user

def client_receive():
    while True:
        try: 
            message = client.recv(1024).decode('utf-8')  # receive message from server (UTF-8 encoding)
            if  message == "alias?":
                client.send(alias.encode('utf-8'))       # send message to server (UTF-8 encoding)
            else:
                print(message)                           # display message from server
        except:
            print('Error')
            client.close()  # close client socket
            break

def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target = client_receive)
receive_thread.start()

send_thread = threading.Thread(target = client_send)
send_thread.start()