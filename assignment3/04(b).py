import itertools

def exhaustive_search_substitution(ciphertext):
    for key in itertools.permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        mapping = dict(zip(key, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        decrypted_text = ''.join(mapping.get(char, char) for char in ciphertext)
        print(f"Key: {''.join(key)}\nDecrypted Text: {decrypted_text}\n")
        # Break if you find a readable plaintext, or use a scoring mechanism to determine the best plaintext.

# Example usage:
ciphertext = "NVTUO EB XOBXHZH OBH RHVD LHAHEZBRO VBDXHAZ NVTUO EB XOBXHZH OBH RHVD LHAHEZBRO VBDXHAZ"
exhaustive_search_substitution(ciphertext)
