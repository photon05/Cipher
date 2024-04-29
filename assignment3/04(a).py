import itertools

def brute_force_substitution(ciphertext):
    for key in itertools.permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        mapping = dict(zip(key, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        decrypted_text = ''.join(mapping.get(char, char) for char in ciphertext)
        print(f"Key: {''.join(key)}\nDecrypted Text: {decrypted_text}\n")

# Example usage:
ciphertext = "S"
brute_force_substitution(ciphertext)
