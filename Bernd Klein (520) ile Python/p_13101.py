# coding:iso-8859-9 T�rk�e
# p_13101.py: re.findall ile �oklu sonu�lar� bulma �rne�i.

import re

dizge = "Ne yak�z ki �are 10 pare, ���ldar hare, �ekillenir kare, tekrarlan�r �aresiz hare."
kal�p = "[�phkfy]are"
sonu� = re.findall (kal�p, dizge)
print ("Bulunan uyumlu ibareler:", sonu�)
print ("-"*75, "\n")
#-------------------------------------------------------------------------------------------------------

kurslar = "Yeni ba�layanlar i�in Python E�itim Kursu: 15/A�ustos/2019 - 19/A�ustor/2019; Orta seviyeliler i�in Python E�itim Kursu: 12/Aral�k/2019 - 16/Aral�k/2019; Python Metin ��leme Kursu: 31/Ekim/2019 - 4/Kas�m/2019"
print ("Bulunan Python kurslar� listesi:", sonu�)
sonu� = re.findall ("([^:]*):([^;]*;?)", kurslar)
print ("\nBulunan Python kurslar� 2 elemanl� t�pleli listesi:", sonu�)
print ("-"*75, "\n")
#-------------------------------------------------------------------------------------------------------

dizge = "Python kurslar� i�in kararla�t�r�lan �ehirler Paris, Londra ve �stanbul!"
sonu� = re.search (r"�ehir.*(Londra|Paris|Zurich|Strasbourg|�stanbul)", dizge)
if sonu�: print ("D�zenlenecek kurslar� kapsayan", sonu�.group() )

"""��kt�:
>python p_13101.py
Bulunan uyumlu ibareler: ['�are', 'pare', 'hare', 'kare', '�are', 'hare']
---------------------------------------------------------------------------

Bulunan Python kurslar� listesi: ['Yeni ba�layanlar i�in Python E�itim Kursu:
15/A�ustos/2019 - 19/A�ustor/2019;', ' Orta seviyeliler i�in Python E�itim Kursu:
12/Aral�k/2019 - 16/Aral�k/2019;', ' Python Metin ��leme Kursu: 31/Ekim/2019 -
4/Kas�m/2019']

Bulunan Python kurslar� 2 elemanl� t�pleli listesi: [('Yeni ba�layanlar i�in Python
E�itim Kursu', ' 15/A�ustos/2019 - 19/A�ustor/2019;'), (' Orta seviyeliler i�in
Python E�itim Kursu', ' 12/Aral�k/2019 - 16/Aral�k/2019;'), (' Python Metin
��leme Kursu', ' 31/Ekim/2019 - 4/Kas�m/2019')]
---------------------------------------------------------------------------

D�zenlenecek kurslar� kapsayan �ehirler Paris, Londra ve �stanbul
"""