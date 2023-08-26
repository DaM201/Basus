import socket
import threading, os, sys


enter_ip = input("Enter IP > ")
server_ip = f'{enter_ip}'
server_port = 8080

running = True

def conected():
    def receive_messages():
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                message = data.decode()
                print(message)
            except:
                break

    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()
    def message_server():
        response = client_socket.recv(1024).decode()
        print(response)


    while True:
        threading.Thread(target=message_server).start()
        message = input(f"prinder@{server_ip}:{server_port}> ")
        threading.Thread(target=message_server).start()
        print("You Write : " + message +"\n")

        client_socket.send(message.encode())

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    threading.Thread(target=conected).start()
except:
    
    print(f"{server_ip}:{server_port} nejde se připojit.")
