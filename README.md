# 🌐 Data Obfuscation and Cybersecurity System

## 📖 Overview
This project implements an integrated **Data Obfuscation and Cybersecurity System**. The system combines data pseudonymization, tokenization, cryptographic encryption, and AI-based anomaly detection into a unified workflow to protect sensitive data and detect potential cyber threats.

## ✨ Features
### 🔒 **Data Obfuscation**
- **Pseudonymization**: Replaces sensitive information with unique identifiers (UUIDs).
- **Tokenization**: Encrypts pseudonymized data for additional security.

### 🛡️ **Cryptographic Algorithms**
- **AES Encryption**: Encrypts obfuscated data using AES symmetric encryption.
- **RSA Encryption**: Secures keys and provides asymmetric encryption for data exchange.

### 🤖 **AI-Based Anomaly Detection**
- **Isolation Forest**: Detects anomalies in data using machine learning.
- **Custom Features**: Simulated feature extraction for anomaly detection.

### 🔗 **Integrated Workflow**
- Reads sensitive data, applies obfuscation, and encrypts it.
- Detects anomalies in encrypted/obfuscated data using an AI model.
- Decrypts and deobfuscates the data to restore the original content.

## 📂 Workflow
1. **Input Data**: A file containing sensitive information.
2. **Obfuscation**:
   - Pseudonymization of sensitive text.
   - Tokenization with encryption.
3. **Encryption**: AES encrypts the obfuscated data.
4. **AI Analysis**: Detects anomalies in the obfuscated/encrypted data.
5. **Decryption and Deobfuscation**:
   - Decrypts the AES-encrypted data.
   - Restores original data through detokenization and reverse pseudonymization.

## 📁 File Structure
```
|-- cryptographic_algorithms.py  # Main script for integration
|-- sample.txt                   # Sample input file
|-- decrypted_sample.txt         # Output after decryption and deobfuscation
|-- aes_key.key                  # AES encryption key
|-- private_key.pem              # RSA private key (password-protected)
|-- public_key.pem               # RSA public key
```

## 🛠️ Requirements
- Python 3.8+
- Libraries:
  - `cryptography`
  - `pandas`
  - `scikit-learn`

Install dependencies:
```bash
pip install cryptography pandas scikit-learn
```

## 🚀 Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Artificial-Intelligence-Project.git
   cd Artificial-Intelligence-Project
   ```

2. Run the main script:
   ```bash
   python cryptographic_algorithms.py
   ```

3. Verify the output:
   - Check `sample.txt` and `decrypted_sample.txt` to confirm the workflow.

## 🔍 Key Features in Detail
### 🔒 Pseudonymization
- Maps original data to UUIDs for anonymity.
- Example:
  ```
  Original: Name: John Doe
  Pseudonymized: c992ffc7-aff9-4eec-a797-5ea1adabd0e1
  ```

### 🔑 Tokenization
- Encrypts pseudonymized data for security.
- Example:
  ```
  Token: gAAAAABng...
  ```

### 🛡️ AES Encryption
- Uses a 256-bit AES key for data encryption.
- Securely stores the encrypted file as `sample.txt.enc`.

### 🔐 RSA Key Management
- Password-protected RSA private key stored as `private_key.pem`.
- Public key stored as `public_key.pem`.

### 🤖 Anomaly Detection
- AI model predicts whether data is normal or anomalous.
- Example prediction:
  ```
  AI Prediction: Normal
  ```

## ✅ Tests and Validation
- The system has been tested with:
  - Sample text data (`sample.txt`).
  - Anomaly detection using a simulated dataset.
- Output files are validated to match original content.

## 🌟 Future Enhancements
- Support for additional file formats (e.g., JSON, CSV).
- Extend AI model to real network traffic datasets.
- Add a GUI or web interface for ease of use.



## 👥 Contributors
- **Nico M** - 
- **Geri R** - 


---
Thank you for exploring the **Data Obfuscation and Cybersecurity System**! 🎉

