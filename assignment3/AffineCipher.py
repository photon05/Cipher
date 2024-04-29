def encrypt_affine(plaintext, k1, k2):
    ciphertext = ''
    m = 26  # Size of the English alphabet
    for char in plaintext:
        if char.isalpha():
            char_index = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')
            encrypted_index = (k1 * char_index + k2) % m
            encrypted_char = chr(encrypted_index + ord('A')) if char.isupper() else chr(encrypted_index + ord('a'))
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

# Encrypt the plaintext "At" using the specified keys
plaintext = "Photon"
k1 = 2  # Multiplicative key
k2 = 1  # Shift key
ciphertext = encrypt_affine(plaintext, k1, k2)
print("Ciphertext:", ciphertext)
