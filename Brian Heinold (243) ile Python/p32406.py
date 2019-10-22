# coding:iso-8859-9 Türkçe

from collections import Counter
import re

metin = open ("p32406x2.txt").read()
# İsterseniz "p32406x1.txt" Türkçe metin dosyasını da kullanabilirsiniz...
print ("Dosyadan okunan metin:\n", metin)

sayar1 = Counter (metin)
print ("\nMetnin karakterlerinin tekrarlanma sıklığı:\n", list (sayar1.items()) )

kelimeler = re.findall ("\w+", metin)
print ("\nMetnin kelimeler listesi:\n", kelimeler)

sayar2 = Counter (kelimeler)
print ("\nKelimelerin tekrar sıklığı:\n", list (sayar2.items()) )
#-----------------------------------------------------------------------------------------

print ("\nEn çok tekrarlanan 10 kelime azalan sırada:", sep="")
for (kelime, sıklık) in sayar2.most_common(10): print (kelime, ':', sıklık)

print ("\nEn çok tekrarlanan 10 kelime artan sırada:", sep="")
for (kelime, sıklık) in sayar2.most_common()[9::-1]: print (kelime, ':', sıklık)
# HATA: Çift tekrarlanma sıklığı tersi [10-->9] bir düşük gerektiriyor...
