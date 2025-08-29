
# 🔐 ENCRYPT YOUR LOG
from cryptography.fernet import Fernet
import os

# Generate key (do once)
key = Fernet.generate_key()
with open("lizzymary_key.key", "wb") as key_file:
    key_file.write(key)

# Load key
with open("lizzymary_key.key", "rb") as f:
    key = f.read()

cipher_suite = Fernet(key)

# Encrypt your log
with open("lizzymary_tasks_2025-08-15.txt", "r") as f:
    file_data = f.read()

encrypted_data = cipher_suite.encrypt(file_data.encode())

with open("lizzymary_tasks_2025-08-15.txt", "wb") as f:
    f.write(encrypted_data)

print("✅ Your log is now encrypted.")
