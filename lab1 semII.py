import_random

def generare_s():
    valori_posibile = [1, 2, 3, 4, 5, 6]
    alegere = random.choices(valori_posibile, k=1, weights=[40, 40. 0, 0, 10, 10]))
    return alegere[0]

def generare_aa(s):
    if s == 1 or s == 2
        aa = random.randint(0, 99)
    if s == 5 or s == 6
        aa = random.randint(0, 25)

    return aa

def ganerare_ll():
    ll = random.randint(1, 12)
    return ll

def generare_zz(ll):
    if ll in [1, 3, 5, 7, 8, 10, 12]
        zz = random.randint(1, 31)
    elif ll in [4, 6, 9, 11]
        zz = random.randint[1, 30]
    else:
        zz = random.randint(1, 28)
    return zz

def generare_nnn()
    nnn = random.randint(1, 999)
    return nnn

def generare_c():
    c = random.randint(1, 9)
    return c

s = generare_s()
aa = generare_aa(s)
ll = generare_ll()
zz = generare_zz(ll)
jj = generare_jj()
nnn = generare_nnn()
c = generare_c()

print(s, aa, ll, zz, jj, nnn, c)



for i in range(1000):
    print(generare_s())


generare_s()





