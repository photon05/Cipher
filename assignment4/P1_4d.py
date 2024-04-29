def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a%b)
    

def fermat_little_theorem(x,b,p):
    if gcd(x,p) == 1:
        print(f"Fermat's Little Theorem holds for p = {p} and a = {x}:")
        c = b // (p-1)
        d = b - c*(p-1)
        return pow(x,d,p)
    else:
        print(f"Fermat's Little Theorem does not hold for p = {p} and a = {x}")
        return "Can't Calculate using Fermat's Little Theorem"


# (a) Find the value of 2^2024 mod 11 using Fermat's Little Theorem
p = 11
x = 0 
b = 103

while x<11:
    mod_value = fermat_little_theorem(x,b,p)
    print(f"value of {x}^{b} mod {p} = ",mod_value)
    if mod_value == 4:
        print(f"The value of x for which x^103 mod 11 = 4 is: {x}")
        break
    x = x+1
    