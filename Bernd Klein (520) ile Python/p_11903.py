#coding:iso-8859-9 T�rk�e
# p_11903.py: **s�zl�k format�yla s�zl�k anahtar ve de�erlerinin yazd�r�lmas� �rne�i.

print ("{1:s}'nin ba�kenti {0:s}'d�r." .format ("Ankara", "T�rkiye") )
print ("{�lke:s}'nin ba�kenti {�ehir:s}'d�r." .format (�ehir="Ankara", �lke="T�rkiye") )

s�zl�k = dict (�ehir="Ankara", �lke="T�rkiye")
print ("\nS�zl�k =", s�zl�k)
print ("{�lke:s}'nin ba�kenti {�ehir:s}'d�r." .format (**s�zl�k) )
#-----------------------------------------------------------------------------------------------------------

s�zl�k = {"T�rkiye": "Ankara",
    "G�rcistan": "Tiflis",
    "Ermenistan": "Erivan",
    "Na�civan": "Na�civan",
    "�ran": "Tahran",
    "Irak": "Ba�dat",
    "Suriye": "�am",
    "KKTC": "Lefko�e",
    "Yunanistan": "Atina",
    "Bulgaristan": "Sofya",
    "Ukrayna": "Kiev"}

print ("\nT�rkiye'nin ve kom�ular�n�n ba��ehirleri s�zl�k d�k�m�:")
for �lke in s�zl�k.keys():
    print ("{�lke:s}'nin ba�kenti {�ehir:s}'d�r." .format (�ehir=s�zl�k[�lke], �lke=�lke) )

print ("\nAyn� s�zl�k d�k�m�n�n farkl� yorumu:")
for �lke in s�zl�k.keys():
    dizge = �lke + ": {" + �lke + "}"
    print (dizge .format (**s�zl�k) )


"""��kt�:
>python p_11903.py
T�rkiye'nin ba�kenti Ankara'd�r.
T�rkiye'nin ba�kenti Ankara'd�r.

S�zl�k = {'�ehir': 'Ankara', '�lke': 'T�rkiye'}
T�rkiye'nin ba�kenti Ankara'd�r.

T�rkiye'nin ve kom�ular�n�n ba��ehirleri s�zl�k d�k�m�:
T�rkiye'nin ba�kenti Ankara'd�r.
G�rcistan'nin ba�kenti Tiflis'd�r.
Ermenistan'nin ba�kenti Erivan'd�r.
Na�civan'nin ba�kenti Na�civan'd�r.
�ran'nin ba�kenti Tahran'd�r.
Irak'nin ba�kenti Ba�dat'd�r.
Suriye'nin ba�kenti �am'd�r.
KKTC'nin ba�kenti Lefko�e'd�r.
Yunanistan'nin ba�kenti Atina'd�r.
Bulgaristan'nin ba�kenti Sofya'd�r.
Ukrayna'nin ba�kenti Kiev'd�r.

Ayn� s�zl�k d�k�m�n�n farkl� yorumu:
T�rkiye: Ankara
G�rcistan: Tiflis
Ermenistan: Erivan
Na�civan: Na�civan
�ran: Tahran
Irak: Ba�dat
Suriye: �am
KKTC: Lefko�e
Yunanistan: Atina
Bulgaristan: Sofya
Ukrayna: Kiev
"""