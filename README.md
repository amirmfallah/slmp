# Secure Lightweight Messaging Protocol (SLMP)

## Overview

The Secure Lightweight Messaging Protocol (SLMP) is designed to provide secure and efficient messaging for IoT (Internet of Things) and Machine-to-Machine (M2M) communication. SLMP enhances security over traditional protocols by incorporating features like Diffie-Hellman key exchange, end-to-end encryption using Fernet, and robust authentication mechanisms.

## Features

- **End-to-End Encryption**: Messages are securely encrypted using Fernet encryption.
- **Secure Key Exchange**: Keys are securely exchanged between client and server using Elliptic Curve Diffie-Hellman (ECDH).
- **Robust Authentication**: Authentication tokens are used to verify the identity of communicating parties.
- **Lightweight**: Optimized for environments with limited computational resources.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/amirmfallah/slmp.git
   cd slmp
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Server

To start the SLMP server, run:

```bash
python server_example.py
```

The server will start and listen for incoming connections.

### Running the Client

To send a message from the client, run:

```bash
python client_example.py
```

The client will connect to the server, perform a secure key exchange, and send an encrypted message.

### Example Output

```plaintext
SLMP Server running on localhost:9999
Connection from ('127.0.0.1', 54028)
Authenticated message from user1: Hello SLMP!
```

## Project Structure

```plaintext
SLMP/
│
├── slmp/
│   ├── server.py
│   ├── client.py
│   ├── encryption.py
│   ├── authentication.py
│   └── key_exchange.py
│
├── requirements.txt
└── README.md
```

## How It Works

### Key Exchange

SLMP uses Elliptic Curve Diffie-Hellman (ECDH) for secure key exchange. The client and server exchange public keys and derive a shared secret. This shared secret is then used to generate a Fernet-compatible encryption key using HKDF.

### Encryption and Decryption

Messages are encrypted and decrypted using the Fernet encryption scheme, which ensures that the data is secure and tamper-proof.

### Authentication

Each message includes an authentication token, which is verified by the server to ensure the identity of the client. This prevents unauthorized access and ensures that only trusted clients can communicate with the server.

### Sequence Diagram

[![](https://mermaid.ink/img/pako:eNqFk09vgzAMxb9KlHN72aYdOPSw_tmkqlI1rlzcxIVoYJiTdEJVv_tSBbapBcYJnJ_fk_PwWapao0ykxU-PpHBlIGeoMhLhaYCdUaYBcmJZGiR3X0-RT8gZxZNIzReLWE7EKxIyOBTrpdhiK_ZgOKKRCGjsGUNHdFMkLfb-UBp1hUck76gbtZ5bIZsTirQARh26FKO7keyNh9Fp3ceH-aENg12n8tZQLt62q820wVjPiNMLWHx-mocIQ56dhh64md5lgh9xWJPitnFih9ZCjuLLuEJskKm_quGMurYg3jX2BgOD_2MwHO-vwTvapiaLE3FEhx78ayFnskKuwOiwDeerQCZdgRVmMgmvGvgjkxldAgfe1WlLSiaOPc4k1z4vZHKE0oYv3-jwE3d79FNFbVzNu7hsqqajyeXlG-3WLZU?type=png)](https://mermaid.live/edit#pako:eNqFk09vgzAMxb9KlHN72aYdOPSw_tmkqlI1rlzcxIVoYJiTdEJVv_tSBbapBcYJnJ_fk_PwWapao0ykxU-PpHBlIGeoMhLhaYCdUaYBcmJZGiR3X0-RT8gZxZNIzReLWE7EKxIyOBTrpdhiK_ZgOKKRCGjsGUNHdFMkLfb-UBp1hUck76gbtZ5bIZsTirQARh26FKO7keyNh9Fp3ceH-aENg12n8tZQLt62q820wVjPiNMLWHx-mocIQ56dhh64md5lgh9xWJPitnFih9ZCjuLLuEJskKm_quGMurYg3jX2BgOD_2MwHO-vwTvapiaLE3FEhx78ayFnskKuwOiwDeerQCZdgRVmMgmvGvgjkxldAgfe1WlLSiaOPc4k1z4vZHKE0oYv3-jwE3d79FNFbVzNu7hsqqajyeXlG-3WLZU)

## Testing

Tests are currently under development and will be added soon. Stay tuned!
