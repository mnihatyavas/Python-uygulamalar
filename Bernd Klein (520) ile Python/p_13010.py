# coding:iso-8859-9 Türkçe
# p_13010.py: İngiliz harfle-rakamla başlayan ikili grup PK'yı re.search'le uygunluk testi örneği.

import re

kodListesi = ["SW1A 0AA", # Avam Kamarası
                 "SW1A 1AA", # Buckingham Sarayı
                 "SW1A 2AA", # Downing Caddesi
                 "BX3 2BB", # Barclays Bankası
                 "DH98 1BT", # Britanya Telekomünikasyonu
                 "N1 9GU", # Guardian Gazatesi
                 "E98 1TT", # The Times Meydanı
                 "TIM E22", # Sahte postakodu
                 "A B1 A22", # Sahte postakodu
                 "EC2N 2DB", # Alman Deutsche Bank
                 "SE9 2UG", # Greenwhich Üniversitesi
                 "N1 0UY", # Islington, London
                 "EC1V 8DS", # Clerkenwell, London
                 "WC1X 9DT", # WC1X 9DT
                 "B42 1LG", # Birmingham
                 "B28 9AD", # Birmingham
                 "W12 7RJ", # London, BBC Haber Merkezi
                 "BBC 007" ] # Sahte postakodu

kalıp = r"[A-z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}"

print ("Birkaç İngiliz Posta Kodu Örneğinin Uygunluk Testi:", "\n", "-"*51, sep="")
for pk in kodListesi:
    sonuç = re.search (kalıp, pk)
    if sonuç: print (pk + " ==>UYGUN Posta Kodu!")
    else: print (pk + " ---->UYGUNSUZ Posta Kodu!")

"""Çıktı:
>python p_13010.py
Birkaç İngiliz Posta Kodu Örneğinin Uygunluk Testi:
---------------------------------------------------
SW1A 0AA ==>UYGUN Posta Kodu!
SW1A 1AA ==>UYGUN Posta Kodu!
SW1A 2AA ==>UYGUN Posta Kodu!
BX3 2BB ==>UYGUN Posta Kodu!
DH98 1BT ==>UYGUN Posta Kodu!
N1 9GU ==>UYGUN Posta Kodu!
E98 1TT ==>UYGUN Posta Kodu!
TIM E22 ---->UYGUNSUZ Posta Kodu!
A B1 A22 ---->UYGUNSUZ Posta Kodu!
EC2N 2DB ==>UYGUN Posta Kodu!
SE9 2UG ==>UYGUN Posta Kodu!
N1 0UY ==>UYGUN Posta Kodu!
EC1V 8DS ==>UYGUN Posta Kodu!
WC1X 9DT ==>UYGUN Posta Kodu!
B42 1LG ==>UYGUN Posta Kodu!
B28 9AD ==>UYGUN Posta Kodu!
W12 7RJ ==>UYGUN Posta Kodu!
BBC 007 ---->UYGUNSUZ Posta Kodu!
"""