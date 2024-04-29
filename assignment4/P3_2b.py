# Given values
p = 139
q = 191
N = p * q
plaintext = "CITY OF LAKE"

# Convert the string to a single integer representation
M = int.from_bytes(plaintext.encode(), 'big')

# Print the integer representation
print("Integer representation:", M)

# Encryption
C = pow(M, 2, N)

# Decryption
mp1 = pow(C, (p + 1) // 4, p)
mp2 = p - mp1
mq1 = pow(C, (q + 1) // 4, q)
mq2 = q - mq1

# Combine square roots using the Chinese Remainder Theorem
r1 = (mp1 * q * pow(q, -1, p) + mq1 * p * pow(p, -1, q)) % N
r2 = (mp2 * q * pow(q, -1, p) + mq1 * p * pow(p, -1, q)) % N
r3 = (mp1 * q * pow(q, -1, p) + mq2 * p * pow(p, -1, q)) % N
r4 = (mp2 * q * pow(q, -1, p) + mq2 * p * pow(p, -1, q)) % N

# Print results
print("Public modulus N:", N)
print("Ciphertext C:", C)
print("Decrypted messages:", r1, r2, r3, r4)
