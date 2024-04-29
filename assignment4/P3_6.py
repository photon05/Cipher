def extended_gcd(a, b):
    # Extended Euclidean Algorithm
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    # Modular Multiplicative Inverse
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def chinese_remainder_theorem(m, a):
    
    N = 1
    for mi in m:
        N *= mi

    result = 0
    for mi, ai in zip(m, a):
        Ni = N // mi
        result += ai * Ni * mod_inverse(Ni, mi)

    return result % N

# Example usage:
m = [4, 5, 7]  # Moduli
a = [3, 2, 6]   # Remainders

# Calculate the solution
solution = chinese_remainder_theorem(m, a)
print("Solution: x = ", solution)

