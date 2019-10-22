# coding:iso-8859-9 T�rk�e

from math import trunc

c�mle = input ("Herhangibir c�mle girin: ")

print ("C�mlenin uzunlu�u:", len (c�mle))

print ("C�mlenin ��lemesi:", c�mle*3)

if len (c�mle) > 0: print ("C�mlenin ilk karakteri:", c�mle[0])

print ("C�mlenin ilk 3 karakteri:", c�mle[:3])

print ("C�mlenin son 3 karakteri:", c�mle[-3:])

print ("C�mlenin tersi:", c�mle[::-1])

if len (c�mle) > 7: print ("C�mlenin 7.karakteri:", c�mle[6])
else: print ("C�mlenin uzunlu�u 7'den k�sa!")

print ("�lk ve son karakter hari� c�mleniz:", c�mle[1:-1])

print ("B�y�k harflerle c�mleniz:", c�mle.upper())

print ("[a<->�] de�i�en c�mleniz:", c�mle.replace ('a', '�'))

print ("Harfleri y�ld�zlanan c�mleniz: ", end="")
for k in c�mle:
    if k.isalpha(): print ('*', end="")
    else: print (k, end="")

print ("\nC�mlenizdeki tahmini kelime say�s�:", c�mle.count (" ")+1)

print ("C�mledeki '(' ve ')' say�lar�:", c�mle.count ('('), c�mle.count ('('))

saya�=0
for k in 'ae�io�u�': saya� += c�mle.count (k)
print ("C�mlenizdeki toplam sesli harf say�s�:", saya�)

print ("K���k harfli ve nokta-virg�lden ari c�mleniz:", c�mle.lower().replace (".", "").replace (",", ""))

ters = c�mle[::-1]
if len (c�mle) >2 and ters.lower() == c�mle.lower(): print ("C�mleniz palindrom'dur!")
else: print ("C�mleniz palindrom de�ildir!")

print ("C�mlenizin ard���k geni�leyen sat�r d�k�m�:")
for i in range (len (c�mle)): print (" "*i, c�mle[i], sep="")

print ("Her harfi �ift b�y�k ve alt-alta �ekilde c�mleniz:")
for i in range (len (c�mle)): print ((c�mle[i]*2).upper())

print ("Harfa��r�lar� b�y�k olan c�mleniz: ", end="")
for i in range (len (c�mle)):
    if i % 2 == 0: print (c�mle[i].lower(), end="")
    else: print (c�mle[i].upper(), end="")

print ("\n�kinciyar�n�n [", c�mle[trunc(len(c�mle)/2):], "] ilkyar�ya [", c�mle[:trunc(len(c�mle)/2)], "] tarakland��� c�mleniz: ", sep="", end="")
for i in range (trunc(len(c�mle)/2)):
    print (c�mle[i], c�mle[i+(trunc(len(c�mle)/2))], sep="", end="")
if len(c�mle) % 2 != 0: print (c�mle[len(c�mle)-1])

print ("\nKelimelerin b�y�kharfle ba�lad��� c�mleniz: ", end="")
if len(c�mle) > 0: print (c�mle[0].upper(), end="")
for i in range (1, len(c�mle)):
    if c�mle[i-1] == ' ': print (c�mle[i].upper(), end="")
    else: print (c�mle[i], end="")
