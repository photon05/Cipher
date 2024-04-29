def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_primitive_root(g, p):
    # Check if g is coprime to p-1
    if gcd(g, p-1) != 1:
        return False

    # Check if g^(p-1)/q is not congruent to 1 for all prime factors q of p-1
    for q in range(2, p):
        if pow(g, (p-1)//q, p) == 1:
            return False

    return True

def primitive_roots(p):
    roots = []
    for g in range(2, p):
        if is_primitive_root(g, p):
            roots.append(g)
    return roots

# Given primes
primes = [8]

# Find primitive roots modulo each prime
for p in primes:
    print(f"Primitive roots modulo {p}: {primitive_roots(p)}")
