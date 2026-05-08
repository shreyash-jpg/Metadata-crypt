from cryptography.fernet import Fernet
import json, os

def encrypt_metadata(file_path, key=None):
    if not key:
        key = Fernet.generate_key().decode()
        print("Generated Key:", key)

    fernet = Fernet(key.encode())
    meta = {"example_field": "sensitive_info"}  # Replace with actual extract function
    encrypted = fernet.encrypt(json.dumps(meta).encode())
    with open(file_path + ".meta.enc", 'wb') as f:
        f.write(encrypted)
    print("Metadata encrypted and saved.")
