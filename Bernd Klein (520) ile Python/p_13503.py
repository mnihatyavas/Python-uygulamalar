# coding:iso-8859-9 T�rk�e
# p_13503.py: try-except-except...finally ile hata y�netimi �rne�i.

try:
    x = float (input ("Herhangibir say� girin: "))
    tersi = 1.0 / x
    print ("\nGirilen say�n�n tersi:", tersi)
except: pass
finally: print ("Bir istisna olu�sa da olu�masa da finally i�letilir.")

print ("-"*75, "\n", sep="")
#-----------------------------------------------------------------------------------------------------

try:
    x = float (input ("Herhangibir say� girin: "))
    tersi = 1.0 / x
    print ("\nGirilen say�n�n tersi:", tersi)
except ValueError: print ("Ge�ersiz bir say� girdiniz!")
except ZeroDivisionError: print ("S�f�r girdiniz, tersi sonsuzdur!")
finally: print ("Bir istisna olu�sa da olu�masa da finally i�letilir.")

"""��kt�:
>python p_13503.py
Herhangibir say� girin: 0
Bir istisna olu�sa da olu�masa da finally i�letilir.
---------------------------------------------------------------------------

Herhangibir say� girin: 0
S�f�r girdiniz, tersi sonsuzdur!
Bir istisna olu�sa da olu�masa da finally i�letilir.

>python p_13503.py  ** TEKRAR **
Herhangibir say� girin: qq
Bir istisna olu�sa da olu�masa da finally i�letilir.
---------------------------------------------------------------------------

Herhangibir say� girin: qq
Ge�ersiz bir say� girdiniz!
Bir istisna olu�sa da olu�masa da finally i�letilir.

>python p_13503.py  ** TEKRAR **
Herhangibir say� girin: 2

Girilen say�n�n tersi: 0.5
Bir istisna olu�sa da olu�masa da finally i�letilir.
---------------------------------------------------------------------------

Herhangibir say� girin: 4

Girilen say�n�n tersi: 0.25
Bir istisna olu�sa da olu�masa da finally i�letilir.
"""