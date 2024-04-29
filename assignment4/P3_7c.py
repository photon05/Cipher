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
p = 93
q = 191
e = 71

# The code for Part 3 question 7(c), 7(d), 7(e) is same. 

M = "Tomorrow IS EXAM"   # Only change is the value of M

# Step 1: Compute N
N = p * q

# Step 2: Compute phi(N)
phi_N = (p - 1) * (q - 1)

# Step 3: Choose e

# Step 4: Compute d (modular multiplicative inverse of e modulo phi(N))
d = mod_inverse(e, phi_N)

# Step 5: Convert message to integer representation
M_int = int.from_bytes(M.encode(), 'big')

# Step 6: Encrypt the message
C = encrypt_rsa(M_int, e, N)

# Step 7: Decrypt the ciphertext
decrypted_M = decrypt_rsa(C, d, N)

# Step 8: Convert decrypted integer back to character representation
# decrypted_M = decrypted_M_int.to_bytes((decrypted_M_int.bit_length() + 7) // 8, 'big').decode()

# Print results
print("Public modulus N:", N)
print("Encryption exponent e:", e)
print("Decryption exponent d:", d)
print("Ciphertext C:", C)
print("Decrypted message:", decrypted_M)

