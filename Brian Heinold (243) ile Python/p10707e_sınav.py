# coding:iso-8859-9 Türkçe

from random import randint

mesaj = input ("Şifrelenecek mesajı girin: ").lower()
if len(mesaj)==0: mesaj = "m.nihat yavaş, 1957"
liste=[]
şifreli=""
alfabe = "abcçdefgğhıijklmnoöpqrsştuüvwxyz"*2
for k in mesaj:
    if k.isalpha():
        kayma = randint (1, len (alfabe)/2)
        liste = liste + [kayma]
        şifreli = şifreli + alfabe[kayma + alfabe.index (k)]
    else: şifreli = şifreli + k
print ("\nŞifreli mesajımız:", şifreli)
deşifreli=""
for k in şifreli:
    if k.isalpha():
        if alfabe.index (k) > liste[0]: deşifreli = deşifreli + alfabe[alfabe.index (k) - liste[0]]
        else: deşifreli = deşifreli + alfabe[alfabe.index (k) + len (alfabe)//2 - liste[0]]
        del liste[0]
    else: deşifreli = deşifreli + k
print ("Deşifreli mesajımız:", deşifreli)

çıktı="""
Şifrelenecek mesajı girin: M.Nihat Yavaş; 17/04/1957; Yeşilyurt-Malatya

Şifreli mesajımız: ğ.tclty ckdhk; 17/04/1957; mbwjqüwşf-ayxütbğ
Deşifreli mesajımız: m.nihat yavaş; 17/04/1957; yeşilyurt-malatya
"""