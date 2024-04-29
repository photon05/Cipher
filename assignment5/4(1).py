import time


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m


def generate_keypair(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    return (n, e), (n, d)


def encrypt(pk, plaintext):
    n, e = pk
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    n, d = pk
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)


p = 53
q = 59
e = 3
plaintext = "HI"

public_key, private_key = generate_keypair(p, q, e)
print("Public Key:", public_key)
print("Private Key:", private_key)

start_time = time.time()
encrypted_text = encrypt(public_key, plaintext)
end_time = time.time()
print("Encrypted Text:", encrypted_text)
print("Encryption Time:", end_time - start_time, "seconds")

start_time = time.time()
decrypted_text = decrypt(private_key, encrypted_text)
end_time = time.time()
print("Decrypted Text:", decrypted_text)
print("Decryption Time:", end_time - start_time, "seconds")
