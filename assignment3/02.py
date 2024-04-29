def decrypt_shift_cipher(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def frequency_analysis(ciphertext):
    # Count the frequency of each letter in the ciphertext
    letter_freq = {}
    for char in ciphertext:
        if char.isalpha():
            char = char.lower()  # Convert to lowercase for case insensitivity
            if char in letter_freq:
                letter_freq[char] += 1
            else:
                letter_freq[char] = 1
    
    # Find the most frequent letter in the ciphertext
    most_common_letter = max(letter_freq, key=letter_freq.get)
    
    # Calculate the shift value based on the most frequent letter (assuming it corresponds to 'e')
    shift = ord(most_common_letter) - ord('e')
    
    return shift

# Example ciphertext
ciphertext = "FMXVEDKAPHFERBNDKRXRSREFMORUDSDKDVSHVUFEDKAPRKDLYEVLRHHRH"

# Perform frequency analysis to retrieve the shift value
shift_value = frequency_analysis(ciphertext)

# Decrypt the ciphertext using the retrieved shift value
plaintext = decrypt_shift_cipher(ciphertext, shift_value)

print("Shift value:", shift_value)
print("Plaintext after decrypting shift part:", plaintext)
