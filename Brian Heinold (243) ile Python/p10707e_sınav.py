# coding:iso-8859-9 T�rk�e

from random import randint

mesaj = input ("�ifrelenecek mesaj� girin: ").lower()
if len(mesaj)==0: mesaj = "m.nihat yava�, 1957"
liste=[]
�ifreli=""
alfabe = "abc�defg�h�ijklmno�pqrs�tu�vwxyz"*2
for k in mesaj:
    if k.isalpha():
        kayma = randint (1, len (alfabe)/2)
        liste = liste + [kayma]
        �ifreli = �ifreli + alfabe[kayma + alfabe.index (k)]
    else: �ifreli = �ifreli + k
print ("\n�ifreli mesaj�m�z:", �ifreli)
de�ifreli=""
for k in �ifreli:
    if k.isalpha():
        if alfabe.index (k) > liste[0]: de�ifreli = de�ifreli + alfabe[alfabe.index (k) - liste[0]]
        else: de�ifreli = de�ifreli + alfabe[alfabe.index (k) + len (alfabe)//2 - liste[0]]
        del liste[0]
    else: de�ifreli = de�ifreli + k
print ("De�ifreli mesaj�m�z:", de�ifreli)

��kt�="""
�ifrelenecek mesaj� girin: M.Nihat Yava�; 17/04/1957; Ye�ilyurt-Malatya

�ifreli mesaj�m�z: �.tclty ckdhk; 17/04/1957; mbwjq�w�f-ayx�tb�
De�ifreli mesaj�m�z: m.nihat yava�; 17/04/1957; ye�ilyurt-malatya
"""