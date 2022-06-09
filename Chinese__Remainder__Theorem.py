import math


def norm(x, mod):
    if x>mod or x == mod:
        x%=mod
    if x<0:
        x+=mod
    return x

def isOk(ar):
    sz = len(ar)
    for i in range(sz):
        for j in range(i+1, sz):
            tem = math.gcd(ar[i], ar[j])
            if tem!=1:
                return False
    return True


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

a = []
m = []
M = []
invM = []
x = []
X = 0
n = int(input("Enter Number : "))

for i in range(n):
    print(f"Enter value of a{i+1}: ", end="")
    xx = int(input())
    a.append(xx)
print()
for i in range(n):
    print(f"Enter value of m{i+1}: ", end="")
    xx = int(input())
    m.append(xx)

# find X
if isOk(m) == False:
    print("Not Possible Because one of the pairs of m is not coprime with other.")
    exit()
Mod = 1
for i in range(n):
    Mod*=m[i]

for i in range(n):
    M.append(int(Mod/m[i]))
    invM.append(int(MultiplicativeInverse(m[i], M[i])))
    x.append(int(norm(a[i] * M[i] * invM[i], int(Mod))))
    X = int(norm(X+x[i], int(Mod)))
    
print(f"X is: {X}")

