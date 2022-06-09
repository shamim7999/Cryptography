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
    C+=str(id)
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
            #print(f"Possible Plain Text is: {chr(X)}")

            if texts.find(chr(X))!=-1:
                pl+=chr(X)

            #print()

print(f"Plain Text is: {pl}")
"""
    Enter a Plain Text: Bangladesh, to the east of India on the Bay of Bengal, is a South Asian country marked by lush greenery and many waterways. Its Padma (Ganges), Meghna and Jamuna rivers create fertile plains, and travel by boat is common. On the southern coast, the Sundarbans, an enormous mangrove forest shared with Eastern India, is home to the royal Bengal tiger.
Ciphertext is: 43569409121001060911664940910000102011322510816193610241345612321102413456108161020110241020194091322513456102412321104041024532912100100001102594091024123211210010241345610819604146411024960412321940913456102411025132251024980112321118811188112321121002116102462411210010241345610816102011024132251232113689134561081610201129961210010249801123219409132251345619361024134561081610201102468891368912100100009409129969604940912100132251936102494091210010241020112100123211299611881123211368913225102411881940912100106091299612321139241020110241040412321129961020113225134561024132251081694091299610201100001024141611102513456108161024476194091322513456102011299612100102453291210010000110259409193610241102513225102410816123211188110201102413456123211024134561081610201102412996123211464194091166410244356102011210010609940911664102413456110251060910201129962116
Plain Text is: Bangladesh, to the east of India on the Bay of Bengal, is a South Asian country marked by lush greenery and many waterways. Its Padma Ganges, Meghna and Jamuna rivers create fertile plains, and travel by boat is common. On the southern coast, the Sundarbans, an enormous mangrove forest shared with Eastern India, is home to the royal Bengal tiger.
"""
