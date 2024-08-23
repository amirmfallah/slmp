import socket
from slmp.encryption import Encryption
from slmp.authentication import Authentication
from slmp.key_exchange import KeyExchange

class SLMPClient:
    def __init__(self, server_host='localhost', server_port=9999, secret_key='my_secret'):
        self.server_host = server_host
        self.server_port = server_port
        self.key_exchange = KeyExchange()
        self.authentication = Authentication(secret_key)

    def send_message(self, username, message):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.server_host, self.server_port))

        # Step 1: Exchange public keys
        client_public_key_bytes = self.key_exchange.get_public_key()
        client_socket.send(client_public_key_bytes)
        server_public_key_bytes = client_socket.recv(1024)

        # Step 2: Generate shared key
        shared_key = self.key_exchange.generate_shared_key(server_public_key_bytes)
        self.encryption = Encryption(key=shared_key)

        # Now continue with the encrypted communication...
        token = self.authentication.generate_token(username)
        encrypted_message = self.encryption.encrypt_message(f"{token};{username};{message}")
        client_socket.send(encrypted_message)

        response = client_socket.recv(1024)
        print("Response from server:", self.encryption.decrypt_message(response))

        client_socket.close()
