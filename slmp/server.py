import socket
from slmp.encryption import Encryption
from slmp.authentication import Authentication
from slmp.key_exchange import KeyExchange

class SLMPServer:
    def __init__(self, host='localhost', port=9999, secret_key='my_secret'):
        self.host = host
        self.port = port
        self.key_exchange = KeyExchange()
        self.authentication = Authentication(secret_key)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"SLMP Server running on {self.host}:{self.port}")

        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr}")

            # Step 1: Exchange public keys
            client_public_key_bytes = client_socket.recv(1024)
            server_public_key_bytes = self.key_exchange.get_public_key()
            client_socket.send(server_public_key_bytes)

            # Step 2: Generate shared key
            shared_key = self.key_exchange.generate_shared_key(client_public_key_bytes)
            self.encryption = Encryption(key=shared_key)

            # Now continue with the encrypted communication...
            encrypted_message = client_socket.recv(1024)
            message = self.encryption.decrypt_message(encrypted_message)

            token, username, client_message = message.split(';')
            if self.authentication.verify_token(token, username):
                print(f"Authenticated message from {username}: {client_message}")
                response = f"Message received: {client_message}"
                client_socket.send(self.encryption.encrypt_message(response))
           
