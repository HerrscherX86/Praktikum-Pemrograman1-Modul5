def hitung(nilai1,nilai2) :
    return nilai1-nilai2

def mutlak(angka) :
    return abs(angka)

a=int(input())
c=int(input())
b=int(input())
d=int(input())
hasil=hitung(a,b)+hitung(c,d)
print(mutlak(hasil))