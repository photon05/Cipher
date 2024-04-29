def frequency_analysis_substitution(ciphertext):
    letter_frequency = {}
    for char in ciphertext:
        if char.isalpha():
            if char.upper() in letter_frequency:
                letter_frequency[char.upper()] += 1
            else:
                letter_frequency[char.upper()] = 1

    # Assuming most frequent letter in ciphertext corresponds to 'E' in plaintext
    most_frequent_cipher_letter = max(letter_frequency, key=letter_frequency.get)
    key_shift = ord(most_frequent_cipher_letter) - ord('E')

    mapping = {}
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        shifted = (ord(char) - ord('A') - key_shift) % 26
        mapping[chr(ord('A') + shifted)] = char

    decrypted_text = ''.join(mapping.get(char.upper(), char) for char in ciphertext)
    print(f"Frequency Analysis Decrypted Text: {decrypted_text}")
    return key_shift

def exhaustive_search_substitution(ciphertext):
    def decrypt_with_key(ciphertext, key):
        mapping = {}
        for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            shifted = (ord(char) - ord('A') - key) % 26
            mapping[chr(ord('A') + shifted)] = char
        return ''.join(mapping.get(char.upper(), char) for char in ciphertext)

    for key in range(26):
        decrypted_text = decrypt_with_key(ciphertext, key)
        print(f"Key Shift: {key}\nDecrypted Text: {decrypted_text}")

# Example ciphertext:
ciphertext = "YIFQFMZRWQFYVECFMDZPCVMRZWNMDZVEJBTXCDDUMJNDIFEFMDZCDMQZKCEYFCJMYRNCWJCSZREXCHZUNMXZNZUCDRJXYYSMRTMEYIFZWDYVZVYFZUMRZCRWNZDZJJXZWGCHSMRNMDHNCMFQCHZJMXJZWIEJYUCFWDJNZDIRKNUALMDDEEEOPDMHHEIESRERNADRAMBAHNOIPTALKD"

print("Using Frequency Analysis:")
key_shift = frequency_analysis_substitution(ciphertext)
print("\nUsing Exhaustive Search:")
exhaustive_search_substitution(ciphertext)
