# coding:iso-8859-9 T�rk�e
# p_13401.py: Liste, iter-next taray�c� ve s�zl�k d�k�mleri �rne�i.

�ehirler = ["Ankara", "�stanbul", "�zmir", "Mersin", "Adana", "Bursa", "Samsun", "Konya", "Diyarbak�r", "Antalya"]
print ("�ehirler listesi:")
for �ehir in �ehirler: print ("-->�ehir: " + �ehir)
#----------------------------------------------------------------------------------------------------

uzmanl�klar = ["Acemi", "Ba�lang��", "Orta", "Usta", "Tecr�beli", "�leri"]
taray�c� = iter (uzmanl�klar)
print ("\nUzmanl�k dereceleri:")
try:
    print ("-->Derece: " + next (taray�c�) )
    print ("-->Derece: " + next (taray�c�) )
    print ("-->Derece: " + next (taray�c�) )
    print ("-->Derece: " + next (taray�c�) )
    print ("-->Derece: " + next (taray�c�) )
    print ("-->Derece: " + next (taray�c�) )
    print ("-->Derece: " + next (taray�c�) )
except StopIteration: print ("Taray�c� listesi sonuna ula��ld�...")
#----------------------------------------------------------------------------------------------------

�ehirler2 = ["Malatya", "Mu�la", "Nev�ehir", "Erzincan", "Amasya", "I�d�r", "Sinop", "Edirne", "Hatay", "Rize"]

taray�c�2 = iter (�ehirler2)
print ("\nDi�er �ehirler:")
while taray�c�2:
    try: print (next (taray�c�2))
    except: break
#----------------------------------------------------------------------------------------------------

ba��ehirler = {"Fransa":"Paris", "Hollanda":"Amsterdam", "Almanya":"Berlin", "�svi�re":"Bern", "Avusturya":"Viyana", "T�rkiye":"Ankara", "�ngiltere":"Londra", "�talya":"Roma", "Yunanistan":"Atina", "Ukrayna":"Kiev"}
print ("\n�e�itli ba��ehirler:")
for �lke in ba��ehirler: print ("-->" + �lke + "'n�n ba�kenti: " + ba��ehirler [�lke] )


"""��kt�:
>python p_13401.py
�ehirler listesi:
-->�ehir: Ankara
-->�ehir: �stanbul
-->�ehir: �zmir
-->�ehir: Mersin
-->�ehir: Adana
-->�ehir: Bursa
-->�ehir: Samsun
-->�ehir: Konya
-->�ehir: Diyarbak�r
-->�ehir: Antalya

Uzmanl�k dereceleri:
-->Derece: Acemi
-->Derece: Ba�lang��
-->Derece: Orta
-->Derece: Usta
-->Derece: Tecr�beli
-->Derece: �leri
Taray�c� listesi sonuna ula��ld�...

Di�er �ehirler:
Malatya
Mu�la
Nev�ehir
Erzincan
Amasya
I�d�r
Sinop
Edirne
Hatay
Rize

�e�itli ba��ehirler:
-->Fransa'n�n ba�kenti: Paris
-->Hollanda'n�n ba�kenti: Amsterdam
-->Almanya'n�n ba�kenti: Berlin
-->�svi�re'n�n ba�kenti: Bern
-->Avusturya'n�n ba�kenti: Viyana
-->T�rkiye'n�n ba�kenti: Ankara
-->�ngiltere'n�n ba�kenti: Londra
-->�talya'n�n ba�kenti: Roma
-->Yunanistan'n�n ba�kenti: Atina
-->Ukrayna'n�n ba�kenti: Kiev
"""