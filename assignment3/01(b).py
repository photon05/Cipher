def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def exhaustive_search(ciphertext):
    for key in range(26):  # Try all possible shift values (0 to 25)
        decrypted_message = decrypt(ciphertext, key)
        print("Key = {}: Decrypted message = {}".format(key, decrypted_message))

# Example usage:
ciphertext = "Skrwrq"
exhaustive_search(ciphertext)
