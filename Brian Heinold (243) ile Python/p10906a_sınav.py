#coding:iso-8859-9 Türkçe

while not (input ("Şifre: ") == "mny957"): print("Yanlış!")
print ("Aferin, doğru şifre girişi...")

print ("\nNotların yanyana listesi==>")
from random import randint
A=toplam=kere=notlar=0
while (notlar+1):
    notlar = randint(-1,100)
    print ("%3d" % (notlar), end=" ")
    if notlar >= 90: A +=1
    if notlar >= 0: toplam +=notlar; kere +=1
print ("\nToplam", kere, "notun ortalaması:", round (toplam/kere, 2))
print ("Derecesi A olanların sayısı:", A)

print ("\nASCII tablo yanyana==>")
ascii = ""
for i in range (352): ascii = ascii + chr(i)
print (ascii)
while not input("\n[Devam:Ent]==>[Çık:TuşEnt]"):
    aranan = input ("Bulmak istediğiniz ASCII karakteri girin: ")
    try: endeks = ascii.index (aranan)
    except Exception: endeks = -1
    if endeks == -1: print ("Aradığınız [", aranan, "] bulunamadı.", sep="")
    else: print ("Aradığınız [", aranan, "] ASCII dizgesinin [", endeks+1, "].konumunda bulundu.", sep="")

        