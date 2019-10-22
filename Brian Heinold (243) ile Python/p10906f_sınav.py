# coding:iso-8859-9 Türkçe

from random import randint
para = 100
i = 1
while True:
    while True:
        gir = input (str (i) + ".Yazı mı tura mı [Y/T]? ").lower()
        if gir == "y" or gir == "t" or gir == "99": break
    if gir == "99": break
    tesadüf = randint (0,1)
    if tesadüf == 1 and gir == "y": para += 9
    else: para -= 10
    i +=1
    print ("Aktüel paranız:", para); print()
    if para >= 200 or para <= 0: break
print()
if gir == "99": print ("Ayrıldığınız oyundan elinizde kalan:", para, "$'dır.")
elif para >= 200: print ("BRAVO! Tam", para, "$ kazandınız.")
else: print ("Maalesef KAYBETTİNİZ! Kalan paranız:", para, "$'dır.")
