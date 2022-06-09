import math

n = 0

def bigMod(e, x, mod):
    if x == 0:
        return 1
    p = bigMod(e,x//2,mod)
    p = (p*p)%mod
    if x%2:
        p = (p*e)%mod
    return p


def MultiplicativeInverse(r1, r2):
    r,q,s,t = 0,0,0,0
    if r1<r2:
        tem = r2
        r2 = r1
        r1 = tem
    rr = max(r1, r2)
    s1,s2,t1,t2 = 1,0,0,1

    while r2>0:
        r = r1%r2
        q = int(r1/r2)
        s = s1-q*s2
        t = t1-q*t2
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t
        r1 = r2
        r2 = r
    if t1<0:
        t1+=rr
    return t1

def RSA_Key_Generation():

    p = int(input("Enter a Prime: ")) ### Take very Big Primes
    q = int(input("Enter Another Prime: ")) ### Take very Big Primes
    global n
    n = p*q
    phi = (p-1)*(q-1)
    e = phi-1
    d = MultiplicativeInverse(phi, e)
    # e is public key
    # d is private key
    return e,d
p=0
q=0
d=0
phi=0
e=0
e,d = RSA_Key_Generation()
print(f"Public Key: {e}\nPrivate Key: {d}\n")

###########  Encryption ##########
P = (input("Enter a Plain Text: "))
C=""
cl = []
for cc in P:
    id = ord(cc)
    cipher = bigMod(id, e, n)
    ch = chr(cipher)
    C+=ch
    cl.append(cipher)
print(f"Cipher : {C}")
PP=""
###########  Decryption ##########

for cc in cl:
    id = cc
    plain = bigMod(id, d, n)
    #plain+=ord('a')
    ch = chr(plain)
    PP+=ch
print(f"Plain Text is: {PP}")
# Take any Input
