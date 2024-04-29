def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def find_key(message, ciphertext):
    m = ord(message.upper()) - ord('A')
    c = ord(ciphertext.upper()) - ord('A')
    m_inverse = mod_inverse(m, 26)
    if m_inverse is None:
        return "Multiplicative inverse does not exist"
    key = (c * m_inverse) % 26
    return key


message = input("Enter Message : ")
ciphertext = input("Enter valid cipher text : ")
key = find_key(message, ciphertext)
print(f"The key is: {key}")

