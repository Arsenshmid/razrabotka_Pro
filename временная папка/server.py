import socket
import json

def plot_graph(data):
    input1 = float(data['input1'])
    input2 = float(data['input2'])

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            data = json.loads(data)
            plot_graph(data)
