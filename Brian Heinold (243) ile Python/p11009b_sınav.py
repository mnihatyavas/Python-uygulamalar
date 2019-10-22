# coding:iso-8859-9 Türkçe

deste = [i for i in range (0, 52)]
takım = ["Kupa", "Karo", "Maça", "Sinek"]
sayı = ["As", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz", "On", "Vale", "Kız", "Papaz"]
oyuncu = kazanan = toplam1 = 0
while not (2 <= oyuncu <= 26): oyuncu = abs (int (eval (input ("Oyuncu sayısını gir [2->26]: "))))
kart = (len (deste) + 1) // oyuncu
from random import shuffle
shuffle (deste)
for i in range (oyuncu):
    print(); toplam2 = 0
    print (i+1, ".oyuncunun elindeki kartlar:\n", "-"*30, sep="")
    for j in range (kart):
        print ("{:2d}: {} {}" .format (deste[i*kart + j] + 1, takım[deste[i*kart+j] // 13], sayı[deste[i*kart+j] % 13]) )
        toplam2 += (deste[i*kart+j] % 13) + 1
    print ("-->Toplamı:", toplam2)
    if toplam2 > toplam1: toplam1 = toplam2; kazanan = i+1
print ("\n==>En yüksek {} puanla {}.OYUNCU KAZANDI" .format (toplam1, kazanan))