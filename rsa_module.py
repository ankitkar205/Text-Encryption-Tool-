import rsa
import base64

(pub_key, priv_key) = rsa.newkeys(512)  # Generate keys on import

def encrypt_rsa(text):
    encrypted = rsa.encrypt(text.encode(), pub_key)
    return base64.b64encode(encrypted).decode()

def decrypt_rsa(encrypted_text):
    decrypted = rsa.decrypt(base64.b64decode(encrypted_text), priv_key)
    return decrypted.decode()
