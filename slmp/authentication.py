import hashlib

class Authentication:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def generate_token(self, username):
        return hashlib.sha256(f"{username}{self.secret_key}".encode()).hexdigest()

    def verify_token(self, token, username):
        return token == self.generate_token(username)
