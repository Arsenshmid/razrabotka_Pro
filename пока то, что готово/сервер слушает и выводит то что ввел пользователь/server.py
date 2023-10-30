import socket
import numpy as np
import matplotlib.pyplot as plt
import base64
import io

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 12345
server_socket.bind((host, port))
server_socket.listen(1)

while True:
    client_socket, client_address = server_socket.accept()

    try:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        values = data.split(',')
        n_ext = float(values[0])
        layers = int(values[1])

        print(f"Вы ввели: {data}")

        wl_data = np.linspace(400, 800, 1001)
        T_data = np.random.rand(1001)
        plt.figure()
        plt.plot(wl_data, T_data, color='purple')
        plt.title('Спектр пропускания слоистой структуры')
        plt.xlabel('Длина волны, нм')
        plt.ylabel('Коэффициент пропускания')
        plt.grid()
        plt.tight_layout()

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()
        image_data = base64.b64encode(buffer.getvalue()).decode()

        client_socket.send(image_data.encode('utf-8'))

    finally:
        client_socket.close()
