x, y = 0, 1

def gcdExtended(a, b):
    global x, y

    if a == 0:
        x = 0
        y = 1
        return b

    gcd = gcdExtended(b % a, a)
    x1 = x
    y1 = y

    x = y1 - (b // a) * x1
    y = x1

    return gcd

def modInverse(A, M):
    g = gcdExtended(A, M)
    res = (x % M + M) % M
    return res


def find_key(message, ciphertext, mod):
    message_num = ord(message.upper()) - 65 
    ciphertext_num = ord(ciphertext.upper()) - 65 

    if gcdExtended(message_num, mod) != 1:
        return -1

    inverse_plaintext = modInverse(message_num, mod)

    key = (ciphertext_num * inverse_plaintext) % mod
    return key

message = input("Enter Message : ")
ciphertext = input("Enter valid cipher text : ")
mod = int(input("Enter mod value : "))
key = -1

for i in range (len(message)):
    if(find_key(message[i],ciphertext[i],mod)!=-1):
        key = find_key(message[i],ciphertext[i],mod)
        break

if key==-1:
    print("Key does not exists")
else:
    print("The key is:", key)

