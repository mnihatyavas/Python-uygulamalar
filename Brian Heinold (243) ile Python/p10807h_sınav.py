#coding:iso-8859-9 Türkçe

# 5 haneli tesadüfi [2->20] rakam üretip, paralel endeks değerleri toplamının tamsayı ortalamasından yeni bir 5 haneli rakam türetelim...
from random import randint
L=[randint (10000,99999) for i in range (randint(2,20))]
dizge = ""
for n in L: dizge = dizge + str (n) + " "
L = dizge.split()
print ("Tesadüfi 5 haneli toplam", len(L), "adet rakamlarımız:", L)

n = 0
for i in range (5):
    toplam = 0
    for j in range (len(L)):
        kelime = L[j]
        toplam += int(kelime[i])
    n += (toplam // len(L)) * (10**(4-i))
print()
print (len(L), "adet ve 5 haneli paralel herbir hanenin tamsayı ortalamasından türetilen yeni rakamımız:", n)
