def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a%b)
    

def fermat_little_theorem(a,b,p):
    if gcd(a,p) == 1:
        print(f"Fermat's Little Theorem holds for p = {p} and a = {a}:")
        c = b // (p-1)
        d = b - c*(p-1)
        return pow(a,d,p)
    else:
        print(f"Fermat's Little Theorem does not hold for p = {p} and a = {a}")
        return "Can't Calculate using Fermat's Little Theorem"


# (c) 2^20 + 3^30 + 4^40 + 5^50 + 6^60 mod 7
ans_i = 0
ans = 0
for i in range (2,7):
    ans_i = fermat_little_theorem(i,10*i,7)
    print(f"{i}^{10*i} mod 7 = {ans_i%7}")
    ans = (ans + ans_i) % 7


print(f"\n2^20 + 3^30 + 4^40 + 5^50 + 6^60 mod 7 = {ans}")



