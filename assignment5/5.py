import time


def logistic_map(x0, r, iterations):
    x = x0
    result = []
    for _ in range(iterations):
        x = r * x * (1 - x)
        result.append(x)
    return result


def encrypt(plaintext, chaotic_sequence):
    encrypted_message = ""
    for i, char in enumerate(plaintext):
        encrypted_char = chr(ord(char) ^ int(chaotic_sequence[i] * 256))
        encrypted_message += encrypted_char
    return encrypted_message


def decrypt(encrypted_message, chaotic_sequence):
    decrypted_message = ""
    for i, char in enumerate(encrypted_message):
        decrypted_char = chr(ord(char) ^ int(chaotic_sequence[i] * 256))
        decrypted_message += decrypted_char
    return decrypted_message


# Test the encryption and decryption

xo = 0.5
r = 3.99
iterations = 1000
plaintext = "HELLO HOW ARE YOU"

start_time = time.time()
chaotic_sequence = logistic_map(xo, r, iterations)
encrypted_message = encrypt(plaintext, chaotic_sequence)
end_time = time.time()

print("Encrypted Message:", encrypted_message)
print("Execution Time:", end_time - start_time, "seconds")

decrypted_message = decrypt(encrypted_message, chaotic_sequence)
print("Decrypted Message:", decrypted_message)

