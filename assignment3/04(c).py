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
    key_shift = ord(most_frequent_cipher_letter) - ord('o')

    mapping = {}
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        shifted = (ord(char) - ord('A') - key_shift) % 26
        mapping[chr(ord('A') + shifted)] = char

    decrypted_text = ''.join(mapping.get(char.upper(), char) for char in ciphertext)
    print(f"Key Shift: {key_shift}\nDecrypted Text: {decrypted_text}")

# Example usage:
ciphertext = "Skrwrq"
frequency_analysis_substitution(ciphertext)
