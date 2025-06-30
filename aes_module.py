from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def encrypt_aes(plain_text, key):
    key = key[:16].ljust(16)  # AES needs 16-byte key
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted = cipher.encrypt(padded_text.encode())
    return base64.b64encode(encrypted).decode()

def decrypt_aes(encrypted_text, key):
    key = key[:16].ljust(16)
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_text))
    return decrypted.decode().rstrip()
