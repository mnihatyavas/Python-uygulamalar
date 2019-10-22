# coding:iso-8859-9 Türkçe
# p_13101.py: re.findall ile çoklu sonuçları bulma örneği.

import re

dizge = "Ne yakız ki çare 10 pare, ışıldar hare, şekillenir kare, tekrarlanır çaresiz hare."
kalıp = "[çphkfy]are"
sonuç = re.findall (kalıp, dizge)
print ("Bulunan uyumlu ibareler:", sonuç)
print ("-"*75, "\n")
#-------------------------------------------------------------------------------------------------------

kurslar = "Yeni başlayanlar için Python Eğitim Kursu: 15/Ağustos/2019 - 19/Ağustor/2019; Orta seviyeliler için Python Eğitim Kursu: 12/Aralık/2019 - 16/Aralık/2019; Python Metin İşleme Kursu: 31/Ekim/2019 - 4/Kasım/2019"
print ("Bulunan Python kursları listesi:", sonuç)
sonuç = re.findall ("([^:]*):([^;]*;?)", kurslar)
print ("\nBulunan Python kursları 2 elemanlı tüpleli listesi:", sonuç)
print ("-"*75, "\n")
#-------------------------------------------------------------------------------------------------------

dizge = "Python kursları için kararlaştırılan şehirler Paris, Londra ve İstanbul!"
sonuç = re.search (r"şehir.*(Londra|Paris|Zurich|Strasbourg|İstanbul)", dizge)
if sonuç: print ("Düzenlenecek kursları kapsayan", sonuç.group() )

"""Çıktı:
>python p_13101.py
Bulunan uyumlu ibareler: ['çare', 'pare', 'hare', 'kare', 'çare', 'hare']
---------------------------------------------------------------------------

Bulunan Python kursları listesi: ['Yeni başlayanlar için Python Eğitim Kursu:
15/Ağustos/2019 - 19/Ağustor/2019;', ' Orta seviyeliler için Python Eğitim Kursu:
12/Aralık/2019 - 16/Aralık/2019;', ' Python Metin İşleme Kursu: 31/Ekim/2019 -
4/Kasım/2019']

Bulunan Python kursları 2 elemanlı tüpleli listesi: [('Yeni başlayanlar için Python
Eğitim Kursu', ' 15/Ağustos/2019 - 19/Ağustor/2019;'), (' Orta seviyeliler için
Python Eğitim Kursu', ' 12/Aralık/2019 - 16/Aralık/2019;'), (' Python Metin
İşleme Kursu', ' 31/Ekim/2019 - 4/Kasım/2019')]
---------------------------------------------------------------------------

Düzenlenecek kursları kapsayan şehirler Paris, Londra ve İstanbul
"""