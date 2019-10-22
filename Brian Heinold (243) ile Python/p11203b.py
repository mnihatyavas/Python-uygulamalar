# coding:iso-8859-9 Türkçe

from random import randint
dosya = open ("oyunlar.txt", "w")
for i in range (1000):
    print (str (randint (1,31)) + "/" + str (randint (1,12)) + "/" + str (randint (2000, 2018)),
        chr (randint (65, 90)) + str (randint (1, 100)), randint (1, 150),
        chr (randint (65, 90)) + str (randint (1, 100)), randint (1, 150), file = dosya)
dosya.close()

L1 = [satır.strip() for satır in open ('oyunlar.txt')]
L2 = [satır.split (' ') for satır in L1]
azamiFark = 0
for oyun in L2:
    fark = abs (int (oyun[2]) - int (oyun[4]))
    if fark > azamiFark: azamiFark = fark; detay = oyun
print ("Oyun: ", detay, "\nSkorlar farkı: ", azamiFark, sep="")
