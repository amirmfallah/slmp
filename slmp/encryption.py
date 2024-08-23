from cryptography.fernet import Fernet

class Encryption:
    def __init__(self, key=None):
        self.key = key if key else Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_message(self, message):
        return self.cipher.encrypt(message.encode())

    def decrypt_message(self, encrypted_message):
        return self.cipher.decrypt(encrypted_message).decode()

    def get_key(self):
        return self.key
