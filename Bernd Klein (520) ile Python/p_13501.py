# coding:iso-8859-9 T�rk�e
# p_13501.py: try-except ve fonksiyon i�i raise ile hata y�netimi �rne�i.

while True:
    try:
        n = input ("\nL�tfen bir tamsay� de�er girin: ")
        n = int (n)
        break
    except ValueError: print ("Ge�ersiz tamsay�! Tekrar deneyin...")

print ("Aferin, ge�erli bir tamsay� giri�i (", n, ") ger�ekle�tirdiniz!", sep="")
print ("-"*75, "\n", sep="")
#-----------------------------------------------------------------------------------------------------

import sys

try:
    dosya = open ('tamsay�.txt')
    sat�r = dosya.readline()
    tamsay� = int (sat�r.strip() )
except IOError as istisna:
    hataNo, hataA��klama = istisna.args
    print ("Okuma/Yazma hatas� ({0}): {1}" .format (hataNo, hataA��klama) )
    # "print (istisna)" veya "print (sys.exc_info()[0])" �eklinde de yaz�labilir... 
except ValueError: print ("Dosya sat�r� ge�erli tamsay� i�ermiyor.")
except:
    print ("Umulmayan di�er hatalar:", sys.exc_info()[0] )
    raise
print ("-"*75, "\n", sep="")
#-----------------------------------------------------------------------------------------------------

try:
    dosya = open ('tamsay�.txt')
    tamsay� = int (dosya.readline().strip() )
except (IOError, ValueError): print ("Okuma/Yazma veya De�erHatas� olu�tu.")
except: print ("Tahmin edilmeyen ba�ka bir hata olu�tu.")
print ("-"*75, "\n", sep="")
#-----------------------------------------------------------------------------------------------------

def fonk():
    try: x = int ("tamsay�")
    except ValueError as ist:
        print ("Fonksiyon i�inde yakalanan hata:", ist)

try: fonk()
except ValueError as ist:
    print ("Hata yakaland�:", ist)

print ("Hata y�netildi; devam edelim...")
print ("-"*75, "\n", sep="")
#-----------------------------------------------------------------------------------------------------

def fonk():
    try: x = int ("tamsay�")
    except ValueError as ist:
        print ("Fonksiyon i�inde yakalanan hata:", ist)
        raise # �a�r�lan yere d�ner...

try: fonk()
except ValueError as ist:
    print ("Hata yakaland�:", ist)

print ("Hata y�netildi; devam edelim...")

"""��kt�:
>python p_13501.py
L�tfen bir tamsay� de�er girin: 4
Aferin, ge�erli bir tamsay� giri�i (4) ger�ekle�tirdiniz!
---------------------------------------------------------------------------

Okuma/Yazma hatas� (2): No such file or directory
---------------------------------------------------------------------------

Okuma/Yazma veya De�erHatas� olu�tu.
---------------------------------------------------------------------------

Fonksiyon i�inde yakalanan hata: invalid literal for int() with base 10: 'tamsay�'
Hata y�netildi; devam edelim...
---------------------------------------------------------------------------

Fonksiyon i�inde yakalanan hata: invalid literal for int() with base 10: 'tamsay�'
Hata yakaland�: invalid literal for int() with base 10: 'tamsay�'
Hata y�netildi; devam edelim...
"""