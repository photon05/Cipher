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


# (a) Find the value of 2^2024 mod 11 using Fermat's Little Theorem
p = 11
a = 2
b = 2024
print(f"value of {a}^{b} mod {p} = ",fermat_little_theorem(a,b,p))

# (b) Find the value of 3^31 mod 7 using Fermat's Little Theorem
p = 7
a = 3
b = 31
print(f"value of {a}^{b} mod {p} = ",fermat_little_theorem(a,b,p))





