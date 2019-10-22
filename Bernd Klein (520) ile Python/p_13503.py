# coding:iso-8859-9 Türkçe
# p_13503.py: try-except-except...finally ile hata yönetimi örneği.

try:
    x = float (input ("Herhangibir sayı girin: "))
    tersi = 1.0 / x
    print ("\nGirilen sayının tersi:", tersi)
except: pass
finally: print ("Bir istisna oluşsa da oluşmasa da finally işletilir.")

print ("-"*75, "\n", sep="")
#-----------------------------------------------------------------------------------------------------

try:
    x = float (input ("Herhangibir sayı girin: "))
    tersi = 1.0 / x
    print ("\nGirilen sayının tersi:", tersi)
except ValueError: print ("Geçersiz bir sayı girdiniz!")
except ZeroDivisionError: print ("Sıfır girdiniz, tersi sonsuzdur!")
finally: print ("Bir istisna oluşsa da oluşmasa da finally işletilir.")

"""Çıktı:
>python p_13503.py
Herhangibir sayı girin: 0
Bir istisna oluşsa da oluşmasa da finally işletilir.
---------------------------------------------------------------------------

Herhangibir sayı girin: 0
Sıfır girdiniz, tersi sonsuzdur!
Bir istisna oluşsa da oluşmasa da finally işletilir.

>python p_13503.py  ** TEKRAR **
Herhangibir sayı girin: qq
Bir istisna oluşsa da oluşmasa da finally işletilir.
---------------------------------------------------------------------------

Herhangibir sayı girin: qq
Geçersiz bir sayı girdiniz!
Bir istisna oluşsa da oluşmasa da finally işletilir.

>python p_13503.py  ** TEKRAR **
Herhangibir sayı girin: 2

Girilen sayının tersi: 0.5
Bir istisna oluşsa da oluşmasa da finally işletilir.
---------------------------------------------------------------------------

Herhangibir sayı girin: 4

Girilen sayının tersi: 0.25
Bir istisna oluşsa da oluşmasa da finally işletilir.
"""