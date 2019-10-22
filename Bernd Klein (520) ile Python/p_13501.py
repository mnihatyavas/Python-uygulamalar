# coding:iso-8859-9 Türkçe
# p_13501.py: try-except ve fonksiyon içi raise ile hata yönetimi örneği.

while True:
    try:
        n = input ("\nLütfen bir tamsayı değer girin: ")
        n = int (n)
        break
    except ValueError: print ("Geçersiz tamsayı! Tekrar deneyin...")

print ("Aferin, geçerli bir tamsayı girişi (", n, ") gerçekleştirdiniz!", sep="")
print ("-"*75, "\n", sep="")
#-----------------------------------------------------------------------------------------------------

import sys

try:
    dosya = open ('tamsayı.txt')
    satır = dosya.readline()
    tamsayı = int (satır.strip() )
except IOError as istisna:
    hataNo, hataAçıklama = istisna.args
    print ("Okuma/Yazma hatası ({0}): {1}" .format (hataNo, hataAçıklama) )
    # "print (istisna)" veya "print (sys.exc_info()[0])" şeklinde de yazılabilir... 
except ValueError: print ("Dosya satırı geçerli tamsayı içermiyor.")
except:
    print ("Umulmayan diğer hatalar:", sys.exc_info()[0] )
    raise
print ("-"*75, "\n", sep="")
#-----------------------------------------------------------------------------------------------------

try:
    dosya = open ('tamsayı.txt')
    tamsayı = int (dosya.readline().strip() )
except (IOError, ValueError): print ("Okuma/Yazma veya DeğerHatası oluştu.")
except: print ("Tahmin edilmeyen başka bir hata oluştu.")
print ("-"*75, "\n", sep="")
#-----------------------------------------------------------------------------------------------------

def fonk():
    try: x = int ("tamsayı")
    except ValueError as ist:
        print ("Fonksiyon içinde yakalanan hata:", ist)

try: fonk()
except ValueError as ist:
    print ("Hata yakalandı:", ist)

print ("Hata yönetildi; devam edelim...")
print ("-"*75, "\n", sep="")
#-----------------------------------------------------------------------------------------------------

def fonk():
    try: x = int ("tamsayı")
    except ValueError as ist:
        print ("Fonksiyon içinde yakalanan hata:", ist)
        raise # Çağrılan yere döner...

try: fonk()
except ValueError as ist:
    print ("Hata yakalandı:", ist)

print ("Hata yönetildi; devam edelim...")

"""Çıktı:
>python p_13501.py
Lütfen bir tamsayı değer girin: 4
Aferin, geçerli bir tamsayı girişi (4) gerçekleştirdiniz!
---------------------------------------------------------------------------

Okuma/Yazma hatası (2): No such file or directory
---------------------------------------------------------------------------

Okuma/Yazma veya DeğerHatası oluştu.
---------------------------------------------------------------------------

Fonksiyon içinde yakalanan hata: invalid literal for int() with base 10: 'tamsayı'
Hata yönetildi; devam edelim...
---------------------------------------------------------------------------

Fonksiyon içinde yakalanan hata: invalid literal for int() with base 10: 'tamsayı'
Hata yakalandı: invalid literal for int() with base 10: 'tamsayı'
Hata yönetildi; devam edelim...
"""