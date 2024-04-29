import hashlib
import random

def gcd(a, b):
    # Calculate the greatest common divisor (GCD) of two numbers
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
    # Check if a number is prime using the Miller-Rabin primality test
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

def generate_prime(bits):
    # Generate a random prime number of specified bit length
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

def generate_keypair(bits):
    # Generate a key pair for RSA encryption
    # Choose two large prime numbers
    p = generate_prime(bits)
    q = generate_prime(bits)
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

def sign(private_key, message):
    # Create a digital signature for a message using RSA
    d, n = private_key
    hashed_message = hashlib.sha256(message.encode()).digest()
    signature = pow(int.from_bytes(hashed_message, byteorder='big'), d, n)
    return signature

def verify(public_key, message, signature):
    # Verify the digital signature of a message using RSA
    e, n = public_key
    hashed_message = hashlib.sha256(message.encode()).digest()
    decrypted_signature = pow(signature, e, n)
    return int.from_bytes(hashed_message, byteorder='big') == decrypted_signature

# Example usage:
message = "Hello, world!"
public_key, private_key = generate_keypair(8)
print("Public key:", public_key)
print("Private key:", private_key)

signature = sign(private_key, message)
print("Signature:", signature)

valid = verify(public_key, message, signature)
print("Signature is valid:", valid)
