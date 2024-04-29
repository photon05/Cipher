#Frequency Analysis
def frequency_analysis_decrypt(ciphertext):
    letter_frequency = {}
    for char in ciphertext:
        if char.isalpha():
            if char.lower() in letter_frequency:
                letter_frequency[char.lower()] += 1
            else:
                letter_frequency[char.lower()] = 1

    most_frequent_letter = max(letter_frequency, key=letter_frequency.get)
    key = ord(most_frequent_letter) - ord('o')
    if key < 0:
        key += 26

    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char

    return key, decrypted_text

# Example usage:
ciphertext = "Skrwrq"
key, decrypted_text = frequency_analysis_decrypt(ciphertext)
print(f"Key: {key}, Decrypted Text: {decrypted_text}")
