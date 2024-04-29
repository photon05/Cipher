# Extended Euclidean Algorithm for finding modular inverse
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

# Point addition on elliptic curve
def point_addition(P, Q, a, p):
    if P == "O":
        return Q
    elif Q == "O":
        return P
    else:
        if P[0] == Q[0] and P[1] != Q[1]:
            return "O"
        elif P != Q:
            m = ((Q[1] - P[1]) * mod_inverse((Q[0] - P[0]) % p, p)) % p
        else:
            m = ((3 * P[0]**2 + a) * mod_inverse((2 * P[1]) % p, p)) % p
        x = (m**2 - P[0] - Q[0]) % p
        y = (m * (P[0] - x) - P[1]) % p
        return (x, y)

# Scalar multiplication using repeated point addition
def scalar_multiplication(G, k, a, p):
    R = "O"
    while k > 0:
        if k % 2 == 1:
            R = point_addition(R, G, a, p)
        G = point_addition(G, G, a, p)
        k = k // 2
    return R

# Parameters
p = 17
a = 1
b = 7
G = (15, 13)
k = 6
result = scalar_multiplication(G, k, a, p)
print("Example 1 :")
print("For p =", p)
print("a =", a)
print("b =", b)
print("Base point G =", G)
print("Scalar k =", k)
print("Result of point multiplication kG =", result)
# example 2
p=17
a=2
b=2
Point1 = (5,1)
Point2 = ( 2,3)
print("\nExample 2 :")
print("For p =", p)
print("a =", a)
print("b =", b)
print("Point 1 =", Point1)
print("Point 2 =", Point2)
print("Result of point addition =", point_addition(Point1, Point2, a, p))
