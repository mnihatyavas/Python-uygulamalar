# coding:iso-8859-9 T�rk�e

from random import randint
para = 100
i = 1
while True:
    while True:
        gir = input (str (i) + ".Yaz� m� tura m� [Y/T]? ").lower()
        if gir == "y" or gir == "t" or gir == "99": break
    if gir == "99": break
    tesad�f = randint (0,1)
    if tesad�f == 1 and gir == "y": para += 9
    else: para -= 10
    i +=1
    print ("Akt�el paran�z:", para); print()
    if para >= 200 or para <= 0: break
print()
if gir == "99": print ("Ayr�ld���n�z oyundan elinizde kalan:", para, "$'d�r.")
elif para >= 200: print ("BRAVO! Tam", para, "$ kazand�n�z.")
else: print ("Maalesef KAYBETT�N�Z! Kalan paran�z:", para, "$'d�r.")
