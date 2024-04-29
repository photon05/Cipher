x,y = 0,1

def gcdExtended(a,b):
    global x,y
    if(a==0):
        x=0
        y=1
        return b
    gcd = gcdExtended(b%a,a)
    x1=x
    y1=y
    x=y1-(b//a)*x1
    y=x1
    return gcd

def modInverse(A,M):
    g = gcdExtended(A,M)
    if(g!=1):
        return None
    else:
        res = (x%M-M)%M
        return res
        
def affine_encrypt(text, key):
    s=""
    for t in text:
        if t==' ':
            s+=t
        else:
            s+=chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) 
                  + ord('A'))
    return s

def affine_decrypt(cipher, key):
    s="";
    for c in cipher:
        if c!=' ':
            s+=chr((( modInverse(key[0], 26)*(ord(c) - ord('A') - key[1]))% 26) + ord('A'))
        else:
            s+=c
    return s

text = input("Enter plain text: ")
key=[]
a=int(input("Enter key k1: "))
b=int(input("Enter key k2: "))
key.append(a)
key.append(b)
affine_encrypted_text = affine_encrypt(text, key)
print('Encrypted Text: {}'.format( affine_encrypted_text ))
print('Decrypted Text: {}'.format( affine_decrypt(affine_encrypted_text, key) ))