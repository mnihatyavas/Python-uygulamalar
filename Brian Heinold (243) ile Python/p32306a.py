# coding:iso-8859-9 T�rk�e

def �ret1 (*say�lar):
    �arp = 1
    for i in say�lar: �arp *=i
    return �arp

def �ret2 (*say�lar):
    topla = 0
    for i in say�lar: topla +=i
    return topla

print ("De�i�ken say�l� fonksiyon arg�manlar�n�n �ARPIMI:", �ret1 (3, 9), �ret1 (2.5, 3.78, -4.32), �ret1 (0.657, -3/43, 7%4, -12.15**4//6), sep='\n')
print ("\nDe�i�ken say�l� fonksiyon arg�manlar�n�n TOPLAMI:", �ret2 (3, 9), �ret2 (2.5, 3.78, -4.32), �ret2 (0.657, -3/43, 7%4, -12.15**4//6), sep='\n')
#------------------------------------------------------------------------------------------

def �s1 (**s�zl�k):
    print (s�zl�k.items(), s�zl�k.keys(), s�zl�k.values(), "", sep="\n")
    for anahtar in s�zl�k:
        print (anahtar, "=", s�zl�k[anahtar], " ==>", anahtar, "**2.65: ", s�zl�k[anahtar]**2.65, sep="")

print("\nDe�i�ken say�l� fonksiyon arg�manlar�nda s�zl�k elemanlar�:")
print (�s1 (r=1.87, s=-3.5, t=0.78, x=3, y=4, z=-5) )
#------------------------------------------------------------------------------------------

def karma1 (a, b, c, *d):
    print (a+b+c)
    print (sum ([x for x in d]) )

def karma2 (d, e, a=0, b=2, c=3, **s):
    print (a+b+c+d+e)
    print (sum (s[anh]**2.5 for anh in s) )

print ("\nVarsay�l� de�erli arg�manlar:")
print (karma1 (1,2,3, 0,1,2,3,4,5,6,7) )
print()
print (karma2 (a=1, b=0, c=0, d=4, e=5, x=6,y=7,z=8) )
#------------------------------------------------------------------------------------------

def topla (a, b): print (a+b)

print ("\n2 arg�manl� fonksiyona de�i�ken de�erler aktarma:")
x = (3, 5)
print (topla (*x) )

�iftDe�erler = [(1,2), (3,4), (5,6), (7,8), (9,10)]
for i in range (len (�iftDe�erler)): print (topla (*�iftDe�erler[i]) )