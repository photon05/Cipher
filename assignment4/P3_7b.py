def gcd_extended(a, b):
    # Extended Euclidean Algorithm
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = gcd_extended(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    # Modular Multiplicative Inverse
    gcd, x, y = gcd_extended(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def encrypt_rsa(M, e, N):
    # Encrypt message using RSA
    return pow(M, e, N)

def decrypt_rsa(C, d, N):
    # Decrypt ciphertext using RSA
    return pow(C, d, N)

# Given values
p = 3
q = 11
e = 3
M = 0b011101011

# Step 1: Compute N
N = p * q

# Step 2: Compute phi(N)
phi_N = (p - 1) * (q - 1)

# Step 3: Choose e

# Step 4: Compute d (modular multiplicative inverse of e modulo phi(N))
d = mod_inverse(e, phi_N)

# Step 5: Encrypt the message
C = encrypt_rsa(M, e, N)

# Step 6: Decrypt the ciphertext
decrypted_M = decrypt_rsa(C, d, N)

# Print results
print("Public modulus N:", N)
print("Encryption exponent e:", e)
print("Decryption exponent d:", d)
print("Ciphertext C:", C)
print("Decrypted message:", decrypted_M)
