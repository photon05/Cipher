def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def decrypt_affine(ciphertext, mod_inv, k2):
    plaintext = ''
    m = 26  # Size of the English alphabet
    inv_k1 = mod_inv
    for char in ciphertext:
        if char.isalpha():
            char_index = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')
            decrypted_index = (inv_k1 * (char_index - k2)) % m
            decrypted_char = chr(decrypted_index + ord('A')) if char.isupper() else chr(decrypted_index + ord('a'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def exhaustive_affine(ciphertext):
    m = 26  # Size of the English alphabet
    for k1 in range(1, m):
        mod_inv = modinv(k1,m)
        if mod_inv is not None:
            for k2 in range(m):
                decrypted_text = decrypt_affine(ciphertext, mod_inv, k2)
                print(f"k1: {k1}, k2: {k2}, Decrypted Text: {decrypted_text}")

# Example ciphertext
ciphertext = "UWRGRO"
exhaustive_affine(ciphertext)
