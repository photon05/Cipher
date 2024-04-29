def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a%b)


def count_keys(m):
    count = 0
    for k1 in range(1, m):
        if gcd(k1, m) == 1:
            count += m 
    return count

m=int(input("Enter the mod: "))
keys_count = count_keys(m)
print("Number of keys : ",keys_count)