#coding:iso-8859-9 T�rk�e

while not (input ("�ifre: ") == "mny957"): print("Yanl��!")
print ("Aferin, do�ru �ifre giri�i...")

print ("\nNotlar�n yanyana listesi==>")
from random import randint
A=toplam=kere=notlar=0
while (notlar+1):
    notlar = randint(-1,100)
    print ("%3d" % (notlar), end=" ")
    if notlar >= 90: A +=1
    if notlar >= 0: toplam +=notlar; kere +=1
print ("\nToplam", kere, "notun ortalamas�:", round (toplam/kere, 2))
print ("Derecesi A olanlar�n say�s�:", A)

print ("\nASCII tablo yanyana==>")
ascii = ""
for i in range (352): ascii = ascii + chr(i)
print (ascii)
while not input("\n[Devam:Ent]==>[��k:Tu�Ent]"):
    aranan = input ("Bulmak istedi�iniz ASCII karakteri girin: ")
    try: endeks = ascii.index (aranan)
    except Exception: endeks = -1
    if endeks == -1: print ("Arad���n�z [", aranan, "] bulunamad�.", sep="")
    else: print ("Arad���n�z [", aranan, "] ASCII dizgesinin [", endeks+1, "].konumunda bulundu.", sep="")

        