# coding:iso-8859-9 Türkçe
# p_12703.py: Pickle/turşu açılamaz dosyasına pickle.dump ile yazma ve pickle.load ile okuma örneği.

import pickle

print ("'p-12701x.txt' şiir dosya içeriklerini yeni bir dosyaya 'pickling/serializable' cinste turşusunu kuralım, sonra da tekrar 'unpickling/unserialable' çözüp okuyalım==>")
metin = open ("p_12701x.txt", "r").read()
dosya = open ("örnek3.turşu", "wb")
pickle.dump (metin, dosya)
dosya.close()

print ("\n-->İşlem tamam!\nŞimdi de tekrar çözüp okuyalım==>")
dosya = open ("örnek3.turşu", "rb")
metin = pickle.load (dosya); dosya.close()
print (metin)

import os
os.remove ("örnek3.turşu")
print ("_"*75, "\n")
#----------------------------------------------------------------------------------------------------

print ("2 liste ve 1 tüpleyi teke nesneleştirip turşulayalım. Sonra da çözüp 2 liste ve tüple olarak görünteleyelim==>")
ülkeler = ["Yunanistan", "Bulgaristan", "Bosna-Hersek", "Kazakistan", "Ukrayna", "Rusya", "Japonya", "Tayland", "Singapur", "Fas", "Brezilya", "Arjantin"]
şehirler = ["Atina", "Sofya", "Saray-Bosna", "Astana", "Kiev", "Moskova", "Tokyo", "Bangkok", "Singapur", "Kazablanka", "Sao-Paola", "Rio-de-Jenerio"]
biletlerTL = (200, 200, 700, 850, 500, 850, 1200, 1250, 1250, 1300, 1500, 1600)
birleşik = (ülkeler, şehirler, biletlerTL)
dosya = open ("örnek4.turşu", "wb")
pickle.dump (birleşik, dosya); dosya.close()

print ("\n-->İşlem tamam!\nŞimdi de tekrar çözüp okuyalım==>")
dosya = open ("örnek4.turşu", "rb")
(ülke, şehir, bilet) = pickle.load (dosya); dosya.close()
print ("==>Gezilen ülkeler listesi:", ülke, "\n==>Görülen şehirler listesi:", şehir, "\n==>2012 çift-yön bilet fiyatları (TL):", bilet)

os.remove ("örnek4.turşu")



"""Çıktı:
>python p_12703.py
'p-12701x.txt' şiir dosya içeriklerini yeni bir dosyaya 'pickling/serializable'
cinste turşusunu kuralım, sonra da tekrar 'unpickling/unserialable' çözüp okuyalım==>

-->İşlem tamam!
Şimdi de tekrar çözüp okuyalım==>
V. ad Lesbiam

VIVAMUS mea Lesbia, atque amemus,
rumoresque senum severiorum
omnes unius aestimemus assis!
soles occidere et redire possunt:
nobis cum semel occidit breuis lux,
nox est perpetua una dormienda.
da mi basia mille, deinde centum,
dein mille altera, dein secunda centum,
deinde usque altera mille, deinde centum.
dein, cum milia multa fecerimus,
conturbabimus illa, ne sciamus,
aut ne quis malus inuidere possit,
cum tantum sciat esse basiorum.
(GAIUS VALERIUS CATULLUS)
___________________________________________________________________________

2 liste ve 1 tüpleyi teke nesneleştirip turşulayalım. Sonra da çözüp 2 liste ve
tüple olarak görünteleyelim==>

-->İşlem tamam!
Şimdi de tekrar çözüp okuyalım==>
==>Gezilen ülkeler listesi: ['Yunanistan', 'Bulgaristan', 'Bosna-Hersek', 'Kazakistan',
'Ukrayna', 'Rusya', 'Japonya', 'Tayland', 'Singapur', 'Fas', 'Brezilya', 'Arjantin']
==>Görülen şehirler listesi: ['Atina', 'Sofya', 'Saray-Bosna', 'Astana', 'Kiev', 'Moskova',
'Tokyo', 'Bangkok', 'Singapur', 'Kazablanka', 'Sao-Paola', 'Rio-de-Jenerio']
==>2012 çift-yön bilet fiyatları (TL): (200, 200, 700, 850, 500, 850, 1200, 1250,
1250, 1300, 1500, 1600)
"""