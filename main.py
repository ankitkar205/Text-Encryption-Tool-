import aes_module
import des_module
import rsa_module

def main():
    print("\n🔐 Welcome to the Text Encryption Tool (CLI Mode)")
    print("Select Encryption Algorithm:\n1. AES\n2. DES\n3. RSA")
    choice = input("Enter choice [1/2/3]: ").strip()

    action = input("Encrypt or Decrypt? (e/d): ").strip().lower()
    text = input("\nEnter the text: ")

    if choice in ['1', '2']:
        key = input("Enter key: ")

    if choice == '1':
        if action == 'e':
            encrypted = aes_module.encrypt_aes(text, key)
            print("\n🔐 Encrypted (AES):", encrypted)
        else:
            decrypted = aes_module.decrypt_aes(text, key)
            print("\n🔓 Decrypted (AES):", decrypted)

    elif choice == '2':
        if action == 'e':
            encrypted = des_module.encrypt_des(text, key)
            print("\n🔐 Encrypted (DES):", encrypted)
        else:
            decrypted = des_module.decrypt_des(text, key)
            print("\n🔓 Decrypted (DES):", decrypted)

    elif choice == '3':
        if action == 'e':
            encrypted = rsa_module.encrypt_rsa(text)
            print("\n🔐 Encrypted (RSA):", encrypted)
        else:
            decrypted = rsa_module.decrypt_rsa(text)
            print("\n🔓 Decrypted (RSA):", decrypted)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
