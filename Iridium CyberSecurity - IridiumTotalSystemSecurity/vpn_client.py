import socket

def main():
    # Client configuration
    server_ip = '127.0.0.1'
    server_port = 12345

    # Create a client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    while True:
        # Simulated user input
        user_input = input("Enter data to send to the server: ")
        if user_input == 'exit':
            break

        # Send data to the server
        client_socket.send(user_input.encode())

        # Receive data from the server
        server_data = client_socket.recv(4096)
        print(f"Received from server: {server_data.decode()}")

    client_socket.close()

if __name__ == '__main__':
    main()
