from Crypto.Cipher import DES
import base64

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt_des(text, key):
    key = key[:8].ljust(8)  # DES uses 8-byte key
    des = DES.new(key.encode(), DES.MODE_ECB)
    padded_text = pad(text)
    encrypted = des.encrypt(padded_text.encode())
    return base64.b64encode(encrypted).decode()

def decrypt_des(encrypted_text, key):
    key = key[:8].ljust(8)
    des = DES.new(key.encode(), DES.MODE_ECB)
    decrypted = des.decrypt(base64.b64decode(encrypted_text))
    return decrypted.decode().rstrip()
