from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt(key, iv, plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

def aes_decrypt(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted

# Example usage:
key = get_random_bytes(32)  # 256-bit key
iv = get_random_bytes(16)   # 128-bit IV
plaintext = b'This is a secret message.'

# Encryption
encrypted = aes_encrypt(key, iv, plaintext)
print("Encrypted:", encrypted)

# Decryption
decrypted = aes_decrypt(key, iv, encrypted)
print("Decrypted:", decrypted.decode('utf-8'))
