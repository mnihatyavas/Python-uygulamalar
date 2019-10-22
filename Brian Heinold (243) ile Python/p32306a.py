# coding:iso-8859-9 Türkçe

def üret1 (*sayılar):
    çarp = 1
    for i in sayılar: çarp *=i
    return çarp

def üret2 (*sayılar):
    topla = 0
    for i in sayılar: topla +=i
    return topla

print ("Değişken sayılı fonksiyon argümanlarının ÇARPIMI:", üret1 (3, 9), üret1 (2.5, 3.78, -4.32), üret1 (0.657, -3/43, 7%4, -12.15**4//6), sep='\n')
print ("\nDeğişken sayılı fonksiyon argümanlarının TOPLAMI:", üret2 (3, 9), üret2 (2.5, 3.78, -4.32), üret2 (0.657, -3/43, 7%4, -12.15**4//6), sep='\n')
#------------------------------------------------------------------------------------------

def üs1 (**sözlük):
    print (sözlük.items(), sözlük.keys(), sözlük.values(), "", sep="\n")
    for anahtar in sözlük:
        print (anahtar, "=", sözlük[anahtar], " ==>", anahtar, "**2.65: ", sözlük[anahtar]**2.65, sep="")

print("\nDeğişken sayılı fonksiyon argümanlarında sözlük elemanları:")
print (üs1 (r=1.87, s=-3.5, t=0.78, x=3, y=4, z=-5) )
#------------------------------------------------------------------------------------------

def karma1 (a, b, c, *d):
    print (a+b+c)
    print (sum ([x for x in d]) )

def karma2 (d, e, a=0, b=2, c=3, **s):
    print (a+b+c+d+e)
    print (sum (s[anh]**2.5 for anh in s) )

print ("\nVarsayılı değerli argümanlar:")
print (karma1 (1,2,3, 0,1,2,3,4,5,6,7) )
print()
print (karma2 (a=1, b=0, c=0, d=4, e=5, x=6,y=7,z=8) )
#------------------------------------------------------------------------------------------

def topla (a, b): print (a+b)

print ("\n2 argümanlı fonksiyona değişken değerler aktarma:")
x = (3, 5)
print (topla (*x) )

çiftDeğerler = [(1,2), (3,4), (5,6), (7,8), (9,10)]
for i in range (len (çiftDeğerler)): print (topla (*çiftDeğerler[i]) )