from ast import Mult

texts = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,. &1234567890-+#@$/*%='\"\\"

def MultiplicativeInverse(r1, r2):
    r,q,s,t = int(0), int(0), int(0), int(0)
    rr = r1
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


def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return 0
    if x%4 == 3:
        return 1
    return 0

def norm(x, mod):
    if x>mod or x == mod:
        x%=mod
    if x<0:
        x+=mod
    return x

def bigMod(e, x, mod):
    if x == 0:
        return 1
    p = norm(bigMod(e,x//2,mod), mod)
    p = norm(p*p, mod)
    if x%2:
        p = norm(p*e, mod)
    return p
    

def twoPrimes():
    p = -1
    q = -1
    for i in range(800, 1000000):
        if isPrime(i) == True:
            p = i
            break
        
    for i in range(p+1, 1000000):
        if isPrime(i) == True:
            q = i
            break
    return p,q
# Key Generation
p,q = twoPrimes() # Private Keys

#print(f"{p}, {q}")
P = input("Enter a Plain Text: ")
n = p*q #Public Key

###### Encryption #####

cl = []
C = ""
pl = ""

for cc in P:
    id = ord(cc)
    id = bigMod(id, 2, n)
    cl.append(id)
    C+=chr(id)
print(f"Ciphertext is: {C}")

###### Decryption #####
## Using, Chinese Remainder Theorem
for cc in cl:
    a = []
    a.append(bigMod(cc, (p+1)//4, p))
    a.append(p - a[0])
    a.append(bigMod(cc, (q+1)//4, q))
    a.append(q - a[2])
    for i in range(2):
        for j in range(2,4):
            Mod = p*q
            r = []
            r.append(a[i])
            r.append(a[j])
            m = []
            M = []
            x = []
            invM = []
            m.append(p)
            m.append(q)
            X = 0
            for k in range(2):
                M.append(int(Mod/m[k]))
                invM.append(int(MultiplicativeInverse(m[k], M[k])))
                x.append(int(norm(r[k] * M[k] * invM[k], int(Mod))))
                X = int(norm(X+x[k], int(Mod))) 
            #print(r)
            #print(m)
            print(f"Possible Plain Text is: {chr(X)}")

            if texts.find(chr(X))!=-1:
                pl+=chr(X)

            #print()

print(f"Plain Text is: {pl}")
# Take Any Input
