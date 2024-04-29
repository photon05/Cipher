import random

# Function to generate a random private key in the range [1, p-1]
def generate_private_key(p):
    return random.randint(1, p-1)

# Function to compute the public key using the private key and parameters g and p.
def compute_public_key(g, secret_key, p):
    return pow(g, secret_key, p)

# Functoin to Compute the shared secret using the other party's public key and own private key.
def compute_shared_secret(public_key, secret_key, p):
    return pow(public_key, secret_key, p)

# Common parameters (known to both parties)
p = 47  # Prime number
g = 5   # Primitive root modulo p

# Alice's secret key (a) and public key (A)
a = 9       # Given
A = compute_public_key(g, a, p)

# Bob's secret key (b) and public key (B)
b = 14      # Given
B = compute_public_key(g, b, p)

# Shared secret computation
shared_secret_alice = compute_shared_secret(B, a, p)
shared_secret_bob = compute_shared_secret(A, b, p)

print("Common parameters (known to both parties):")
print("p:", p)
print("g:", g)

print("\nAlice's private key and public key:")
print("Private Key (Alice):", a)
print("Public Key (Alice):", A)

print("\nBob's private key and public key:")
print("Private Key (Bob):", b)
print("Public Key (Bob):", B)

print("\nShared Secret (Alice):", shared_secret_alice)
print("Shared Secret (Bob):", shared_secret_bob)

