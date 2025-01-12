from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import os
import uuid
import base64
from cryptography.fernet import Fernet
import pandas as pd
from sklearn.ensemble import IsolationForest

# Save and load keys securely
def save_key_to_file_securely(key, filename, password=None):
    if isinstance(key, rsa.RSAPrivateKey):
        encryption_algorithm = (
            serialization.BestAvailableEncryption(password) if password else serialization.NoEncryption()
        )
        key_data = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=encryption_algorithm
        )
    elif isinstance(key, rsa.RSAPublicKey):
        key_data = key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    else:
        key_data = key

    with open(filename, "wb") as key_file:
        key_file.write(key_data)


def load_private_key_securely(filename, password=None):
    with open(filename, "rb") as key_file:
        return serialization.load_pem_private_key(
            key_file.read(),
            password=password,
            backend=default_backend()
        )


def load_public_key_securely(filename):
    with open(filename, "rb") as key_file:
        return serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

# Load a raw key from a file (e.g., AES key)
def load_key_from_file(filename):
    with open(filename, "rb") as key_file:
        return key_file.read()

# Data Obfuscation: Pseudonymization and Tokenization
def pseudonymize(data):
    return {original: str(uuid.uuid4()) for original in data}

def reverse_pseudonymization(pseudonymized_data):
    return {pseudonym: original for original, pseudonym in pseudonymized_data.items()}

def tokenize(data):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    tokens = {original: cipher.encrypt(original.encode()).decode() for original in data}
    return tokens, cipher

def detokenize(tokens, cipher):
    return [cipher.decrypt(token.encode()).decode() for token in tokens]

# AI Anomaly Detection Model
def train_ai_model():
    # Simulate training data (e.g., network traffic logs)
    normal_data = pd.DataFrame({
        "feature1": [0.1, 0.2, 0.1, 0.3],
        "feature2": [100, 150, 120, 130]
    })
    anomaly_data = pd.DataFrame({
        "feature1": [5.0, 6.0],
        "feature2": [500, 600]
    })

    data = pd.concat([normal_data, anomaly_data])
    labels = [0] * len(normal_data) + [1] * len(anomaly_data)

    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(data)
    return model

# Integrated Workflow
def integrated_workflow(input_file, aes_key, rsa_public_key, rsa_private_key, model):
    # Step 1: Read and Obfuscate Input
    with open(input_file, "r") as f:
        content = f.read().splitlines()
    pseudonymized_data = pseudonymize(content)
    tokens, cipher = tokenize(list(pseudonymized_data.values()))

    # Step 2: Encrypt Obfuscated Data
    tokenized_str = "\n".join(tokens.values())
    encoded_tokenized_data = base64.b64encode(tokenized_str.encode())
    iv = os.urandom(16)
    cipher_aes = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher_aes.encryptor()
    ciphertext = iv + encryptor.update(encoded_tokenized_data) + encryptor.finalize()

    # Step 3: Save Encrypted Data
    encrypted_file = input_file + ".enc"
    with open(encrypted_file, "wb") as f:
        f.write(ciphertext)

    print(f"File '{input_file}' encrypted to '{encrypted_file}'.")

    # Step 4: AI Analysis on Encrypted Data
    # Simulate feature extraction and prediction
    features = pd.DataFrame({
        "feature1": [0.1],
        "feature2": [100]
    })
    prediction = model.predict(features)
    print(f"AI Prediction: {'Anomaly Detected' if prediction[0] == -1 else 'Normal'}")

    # Step 5: Decrypt and Deobfuscate
    with open(encrypted_file, "rb") as f:
        ciphertext = f.read()
    iv = ciphertext[:16]
    cipher_aes = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher_aes.decryptor()
    decrypted_data = decryptor.update(ciphertext[16:]) + decryptor.finalize()
    decoded_data = base64.b64decode(decrypted_data).decode()
    detokenized_data = detokenize(decoded_data.split("\n"), cipher)
    original_data = {pseudonym: original for pseudonym, original in zip(detokenized_data, pseudonymized_data.keys())}

    # Save Deobfuscated Data
    output_file = "decrypted_" + input_file
    with open(output_file, "w") as f:
        for line in original_data.values():
            f.write(line + "\n")
    print(f"File '{encrypted_file}' decrypted and deobfuscated to '{output_file}'.")

if __name__ == "__main__":
    # Generate keys and model
    aes_key = os.urandom(32)
    rsa_private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    rsa_public_key = rsa_private_key.public_key()
    model = train_ai_model()

    # Save keys
    save_key_to_file_securely(aes_key, "aes_key.key")
    save_key_to_file_securely(rsa_private_key, "private_key.pem", password=b"securepassword")
    save_key_to_file_securely(rsa_public_key, "public_key.pem")

    # Run the integrated workflow
    with open("sample.txt", "w") as f:
        f.write("Name: John Doe\nAddress: 123 Main St\nSSN: 123-45-6789")

    integrated_workflow("sample.txt", aes_key, rsa_public_key, rsa_private_key, model)
