import random

def generate_private_key(p):
    # Generate a random private key in the range [1, p-1].
    return random.randint(1, p-1)

def compute_public_key(g, private_key, p):
    # Compute the public key using the private key and parameters g and p
    return pow(g, private_key, p)

def compute_shared_secret(public_key, private_key, p):
    # Compute the shared secret using the other party's public key and own private key.
    return pow(public_key, private_key, p)

# Common parameters (known to both parties)
p = 23  # Prime number
g = 5   # Primitive root modulo p

# Party A
private_key_a = generate_private_key(p)
public_key_a = compute_public_key(g, private_key_a, p)
print("Party A:")
print("Private Key:", private_key_a)
print("Public Key:", public_key_a)

# Party B
private_key_b = generate_private_key(p)
public_key_b = compute_public_key(g, private_key_b, p)
print("\nParty B:")
print("Private Key:", private_key_b)
print("Public Key:", public_key_b)

# Shared secret computation
shared_secret_a = compute_shared_secret(public_key_b, private_key_a, p)
shared_secret_b = compute_shared_secret(public_key_a, private_key_b, p)

print("\nShared Secret (Party A):", shared_secret_a)
print("Shared Secret (Party B):", shared_secret_b)
