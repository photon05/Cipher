import random

def gcd(a, b):
    # Calculate the greatest common divisor (GCD) of two numbers.
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    # Calculate the modular inverse of a number modulo m
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def is_prime(n, k=5):
    # Check if a number is prime using the Miller-Rabin primality test.
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as d * 2^r + 1
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Perform Miller-Rabin primality test
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def random_prime(bits):
    # Generate a random prime number of specified bit length
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p
        
def generate_keypair(bits):
    # Generate a key pair for RSA encryption
    # Choose two large prime numbers
    p = random_prime(bits)
    q = random_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose a random integer e such that 1 < e < phi and gcd(e, phi) = 1
    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            break

    # Compute the modular inverse of e modulo phi
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    # Encrypt a message using RSA encryption
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    # Decrypt a message using RSA decryption
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

# Example usage:
plaintext = "Hello, world!"
public_key, private_key = generate_keypair(8)
print("Public key:", public_key)
print("Private key:", private_key)

encrypted_message = encrypt(public_key, plaintext)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(private_key, encrypted_message)
print("Decrypted message:", decrypted_message)
