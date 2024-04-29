import random
import math

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

def generate_prime(bits):
    # Generate a random prime number of specified bit length
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

def generate_keys(bits):
    # Generate public and private keys
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    N = p * q
    return (N, p, q)

def encrypt(M, N):
    # Encrypt plaintext
    # m = int.from_bytes(plaintext.encode(), 'big')
    return pow(M, 2, N)

def legendre_symbol(a, p):
    # Compute the Legendre symbol (a/p
    ls = pow(a, (p - 1) // 2, p)
    if ls == p - 1:
        return -1
    return ls

def tonelli_shanks(n, p):
    # Compute square roots modulo a prime using Tonelli-Shanks algorithm
    if legendre_symbol(n, p) != 1:
        return None

    Q, S = p - 1, 0
    while Q % 2 == 0:
        Q //= 2
        S += 1

    if S == 1:
        return pow(n, (p + 1) // 4, p)

    z = 2
    while legendre_symbol(z, p) != -1:
        z += 1
    c = pow(z, Q, p)
    R, t = pow(n, (Q + 1) // 2, p), pow(n, Q, p)
    while t != 1:
        for i in range(1, S):
            if pow(t, 2**i, p) == 1:
                break
        b = pow(c, 2**(S - i - 1), p)
        R, t, c = R * b % p, t * b**2 % p, b**2 % p
    return R

def decrypt(ciphertext, N, p, q):
    # Decrypt ciphertext
    mp = tonelli_shanks(ciphertext, p)
    mq = tonelli_shanks(ciphertext, q)
    if mp is None or mq is None:
        return None
    yp = (mp * pow(p, -1, q)) % N
    yq = (mq * pow(q, -1, p)) % N
    r1 = (yp * q + yq * p) % N
    r2 = N - r1
    r3 = (yp * q - yq * p) % N
    r4 = N - r3
    return r1, r2, r3, r4

# Example usage:
plaintext = 741
print("Plaintext:", plaintext)

# Generate keys
# N, p, q = generate_keys(64)
p = 43
q = 47
N = p*q

# Encrypt plaintext
ciphertext = encrypt(plaintext, N)
print("Ciphertext:", ciphertext)

# Decrypt ciphertext
decrypted_messages = decrypt(ciphertext, N, p, q)
for message in decrypted_messages:
    if message is not None:
        print("Decrypted message:", message.to_bytes((message.bit_length() + 7) // 8, 'big').decode())
