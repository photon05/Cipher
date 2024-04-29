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

p_values = [23, 29, 101]
g_values = [5, 13, 7]
a_values = [6, 4, 8]
b_values = [15, 12, 10]


# Alice's public keys (A)
A = [0] * len(p_values)

# Bob's public keys (B)
B = [0] * len(p_values)


for i in range(len(p_values)):
    print(f"Case {i+1}")  
    A[i] = compute_public_key(g_values[i], a_values[i], p_values[i])
    B[i] = compute_public_key(g_values[i], b_values[i], p_values[i])
    # Shared secret computation
    shared_secret_alice = compute_shared_secret(B[i], a_values[i], p_values[i])
    shared_secret_bob = compute_shared_secret(A[i], b_values[i], p_values[i])


    print("Common parameters (known to both parties):")
    print("p:", p_values[i])
    print("g:", g_values[i])

    # print("\nAlice's private key and public key:")
    print("Private Key (Alice):", a_values[i])
    print("Public Key (Alice):", A[i])

    print("\nBob's private key and public key:")
    print("Private Key (Bob):", b_values[i])
    print("Public Key (Bob):", B[i])

    print("\nShared Secret (Alice):", shared_secret_alice)
    print("Shared Secret (Bob):", shared_secret_bob)
    print()

# End



