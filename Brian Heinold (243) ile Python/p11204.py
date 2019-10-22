# coding:iso-8859-9 T�rk�e

L1 = [sat�r.strip() for sat�r in open ('sorular.txt')]
L2 = [sat�r.split (' ') for sat�r in L1]
L3 = [L2[i][j] for i in range (len (L2)) for j in range (len (L2[0])) ]
print (L3)
print ("\nListe kelimelerini uzunluklar�na g�re artan d�k�m:\n", "-"*50, sep="")
for i in range (20):
    yazd�= False
    for j in range (len (L3)):
        if len (L3[j]) == i + 1:
            print ((i+1), ":", L3[j])
            yazd� = True
    if yazd�: print()
print ("="*61)
saya� = 0
for kelime in L3:
    if kelime[0].lower() in 'aeio�u�': saya� +=1
print ("Listedeki SESL� harfle ba�layan kelimelerin y�zdesi: % {:.2f}" .format (100 * saya� / len (L3)) )

saya� = 0
for kelime in L3:
    if kelime[0].lower() not in 'aeio�u�': saya� +=1
print ("Listedeki SESS�Z harfle ba�layan kelimelerin y�zdesi: % {:.2f}" .format (100 * saya� / len (L3)) )
print ("="*61)

enuzun = 0
for kelime in L3:
    for k in kelime:
        if k not in 'znu': break
    else:
        if len (kelime) > enuzun:
            enuzun = len (kelime)
            enuzunKelime = kelime
print ("\n'znu' i�eren enuzun kelime ve uzunlu�u:", enuzunKelime, "-->", enuzun)
