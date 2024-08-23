import base64
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, load_pem_public_key
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

class KeyExchange:
    def __init__(self):
        # Generate a private key using elliptic curve cryptography
        self.private_key = ec.generate_private_key(ec.SECP256R1())

    def get_public_key(self):
        # Return the public key in PEM format to be shared with the other party
        public_key = self.private_key.public_key()
        return public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)

    def generate_shared_key(self, peer_public_key_bytes):
        # Load the peer's public key from PEM format
        peer_public_key = load_pem_public_key(peer_public_key_bytes, backend=default_backend())
        
        # Perform the key exchange to generate a shared secret
        shared_secret = self.private_key.exchange(ec.ECDH(), peer_public_key)

        # Derive a 32-byte key using HKDF
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'handshake data',
            backend=default_backend()
        ).derive(shared_secret)

        # Base64 encode the derived key to make it compatible with Fernet
        fernet_key = base64.urlsafe_b64encode(derived_key)

        return fernet_key
