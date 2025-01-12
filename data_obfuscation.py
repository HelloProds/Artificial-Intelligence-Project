import uuid
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Step 1: Pseudonymization
def pseudonymize(data):
    pseudonymized_data = {original: str(uuid.uuid4()) for original in data}
    return pseudonymized_data

# Reverse pseudonymization (for authorized access)
def reverse_pseudonymization(pseudonymized_data):
    reversed_data = {pseudonym: original for original, pseudonym in pseudonymized_data.items()}
    return reversed_data

# Step 2: Tokenization
def tokenize(data):
    tokens = {original: cipher.encrypt(original.encode()).decode() for original in data}
    return tokens

# Reverse tokenization

def detokenize(tokens):
    detokenized_data = {token: cipher.decrypt(token.encode()).decode() for token in tokens.values()}
    return detokenized_data

# Test the obfuscation techniques
if __name__ == "__main__":
    # Sample sensitive data
    sensitive_data = ["John Doe", "123-45-6789", "john.doe@example.com"]

    # Pseudonymization
    pseudonymized = pseudonymize(sensitive_data)
    print("Pseudonymized Data:", pseudonymized)

    reversed_pseudonyms = reverse_pseudonymization(pseudonymized)
    print("Reversed Pseudonymization:", reversed_pseudonyms)

    # Tokenization
    tokenized = tokenize(sensitive_data)
    print("Tokenized Data:", tokenized)

    detokenized = detokenize(tokenized)
    print("Detokenized Data:", detokenized)
