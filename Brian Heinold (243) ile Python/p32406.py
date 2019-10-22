# coding:iso-8859-9 T�rk�e

from collections import Counter
import re

metin = open ("p32406x2.txt").read()
# �sterseniz "p32406x1.txt" T�rk�e metin dosyas�n� da kullanabilirsiniz...
print ("Dosyadan okunan metin:\n", metin)

sayar1 = Counter (metin)
print ("\nMetnin karakterlerinin tekrarlanma s�kl���:\n", list (sayar1.items()) )

kelimeler = re.findall ("\w+", metin)
print ("\nMetnin kelimeler listesi:\n", kelimeler)

sayar2 = Counter (kelimeler)
print ("\nKelimelerin tekrar s�kl���:\n", list (sayar2.items()) )
#-----------------------------------------------------------------------------------------

print ("\nEn �ok tekrarlanan 10 kelime azalan s�rada:", sep="")
for (kelime, s�kl�k) in sayar2.most_common(10): print (kelime, ':', s�kl�k)

print ("\nEn �ok tekrarlanan 10 kelime artan s�rada:", sep="")
for (kelime, s�kl�k) in sayar2.most_common()[9::-1]: print (kelime, ':', s�kl�k)
# HATA: �ift tekrarlanma s�kl��� tersi [10-->9] bir d���k gerektiriyor...
