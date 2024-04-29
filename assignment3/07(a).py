def extendedEuclideanAlgo(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extendedEuclideanAlgo(b % a, a)
        return gcd, y - (b // a) * x, x

def find_inverse(a, m):
    gcd, x, y = extendedEuclideanAlgo(a, m)
    if gcd != 1:
        return None  # Inverse doesn't exist
    else:
        return x % m
    
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def multiplicative_decrypt(ciphertext, key, m):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            char_index = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')
            decrypted_index = (key * char_index) % m
            decrypted_char = chr(decrypted_index + ord('A')) if char.isupper() else chr(decrypted_index + ord('a'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def brute_force_multiplicative(ciphertext, m):
    for key in range(1, m):
        # Check if the key is coprime to m
        if gcd(key, m) == 1:
            invKey = find_inverse(key,m)
            decrypted_text = multiplicative_decrypt(ciphertext, invKey, m)
            if key<10:
             print(f"{key}     |   {decrypted_text}")
            else:
             print(f"{key}    |   {decrypted_text}")


# Example ciphertext
ciphertext = "CQQ"
m = 26  
print("Key   |  Decrypted Text")
print("______|________________")
brute_force_multiplicative(ciphertext, m)
