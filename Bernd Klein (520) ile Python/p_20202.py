# coding:iso-8859-9 T�rk�e
# p_20202.py: Veri giri� input'la .exe programlar� i�letme �rne�i.

import os

a = " "
while (a != "exit"):
    a = input ("Veri giri�i [��k��: exit]: ")
    dosya = os.popen (a)
    print (dosya.read())

print ("Heyyaah, bu i� bu kadar!..")

"""��kt�:
>python p_20202.py
Veri giri�i: M.Nihat Yava�
'M.Nihat' i� ya da d�� komut, �al��t�r�labilir
program ya da toplu i� dosyas� olarak tan�nm�yor.

Veri giri�i: write # WordPad a��l�r...

Veri giri�i: notepad # NotePad a��l�r...

Veri giri�i: mspaint # MSPaint a��l�r...

Veri giri�i: exit

Heyyaah, bu i� bu kadar!..
"""