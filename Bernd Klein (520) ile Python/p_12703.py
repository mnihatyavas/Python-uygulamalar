# coding:iso-8859-9 T�rk�e
# p_12703.py: Pickle/tur�u a��lamaz dosyas�na pickle.dump ile yazma ve pickle.load ile okuma �rne�i.

import pickle

print ("'p-12701x.txt' �iir dosya i�eriklerini yeni bir dosyaya 'pickling/serializable' cinste tur�usunu kural�m, sonra da tekrar 'unpickling/unserialable' ��z�p okuyal�m==>")
metin = open ("p_12701x.txt", "r").read()
dosya = open ("�rnek3.tur�u", "wb")
pickle.dump (metin, dosya)
dosya.close()

print ("\n-->��lem tamam!\n�imdi de tekrar ��z�p okuyal�m==>")
dosya = open ("�rnek3.tur�u", "rb")
metin = pickle.load (dosya); dosya.close()
print (metin)

import os
os.remove ("�rnek3.tur�u")
print ("_"*75, "\n")
#----------------------------------------------------------------------------------------------------

print ("2 liste ve 1 t�pleyi teke nesnele�tirip tur�ulayal�m. Sonra da ��z�p 2 liste ve t�ple olarak g�r�nteleyelim==>")
�lkeler = ["Yunanistan", "Bulgaristan", "Bosna-Hersek", "Kazakistan", "Ukrayna", "Rusya", "Japonya", "Tayland", "Singapur", "Fas", "Brezilya", "Arjantin"]
�ehirler = ["Atina", "Sofya", "Saray-Bosna", "Astana", "Kiev", "Moskova", "Tokyo", "Bangkok", "Singapur", "Kazablanka", "Sao-Paola", "Rio-de-Jenerio"]
biletlerTL = (200, 200, 700, 850, 500, 850, 1200, 1250, 1250, 1300, 1500, 1600)
birle�ik = (�lkeler, �ehirler, biletlerTL)
dosya = open ("�rnek4.tur�u", "wb")
pickle.dump (birle�ik, dosya); dosya.close()

print ("\n-->��lem tamam!\n�imdi de tekrar ��z�p okuyal�m==>")
dosya = open ("�rnek4.tur�u", "rb")
(�lke, �ehir, bilet) = pickle.load (dosya); dosya.close()
print ("==>Gezilen �lkeler listesi:", �lke, "\n==>G�r�len �ehirler listesi:", �ehir, "\n==>2012 �ift-y�n bilet fiyatlar� (TL):", bilet)

os.remove ("�rnek4.tur�u")



"""��kt�:
>python p_12703.py
'p-12701x.txt' �iir dosya i�eriklerini yeni bir dosyaya 'pickling/serializable'
cinste tur�usunu kural�m, sonra da tekrar 'unpickling/unserialable' ��z�p okuyal�m==>

-->��lem tamam!
�imdi de tekrar ��z�p okuyal�m==>
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

2 liste ve 1 t�pleyi teke nesnele�tirip tur�ulayal�m. Sonra da ��z�p 2 liste ve
t�ple olarak g�r�nteleyelim==>

-->��lem tamam!
�imdi de tekrar ��z�p okuyal�m==>
==>Gezilen �lkeler listesi: ['Yunanistan', 'Bulgaristan', 'Bosna-Hersek', 'Kazakistan',
'Ukrayna', 'Rusya', 'Japonya', 'Tayland', 'Singapur', 'Fas', 'Brezilya', 'Arjantin']
==>G�r�len �ehirler listesi: ['Atina', 'Sofya', 'Saray-Bosna', 'Astana', 'Kiev', 'Moskova',
'Tokyo', 'Bangkok', 'Singapur', 'Kazablanka', 'Sao-Paola', 'Rio-de-Jenerio']
==>2012 �ift-y�n bilet fiyatlar� (TL): (200, 200, 700, 850, 500, 850, 1200, 1250,
1250, 1300, 1500, 1600)
"""