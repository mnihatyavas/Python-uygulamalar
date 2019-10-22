# coding:iso-8859-9 Türkçe
# p_13504.py: try-except-else ile hata yönetimli dosya okuma örneği.

import sys

dosyaAdı = sys.argv[1]
metin = ""
try:
    dosya = open (dosyaAdı, 'r')
    metin = dosya.read().strip()
    dosya.close() # Herüç satırdan biri IOError istisnasını fırlatabilir...
except IOError: print (dosyaAdı, "adlı dosyayı açamıyorum!")

if metin: print (metin[:100] )
print ("-"*75, "\n", sep="")
#-----------------------------------------------------------------------------------------------------

metin = []
try: dosya = open (dosyaAdı, 'r') # Sadece bu satır IOError istisnasını fırlatabilir...
except IOError: print (dosyaAdı, "adlı dosyayı açamıyorum!")
else:
    metin = dosya.readlines()
    dosya.close()

if metin: print (metin[0] )

"""Çıktı:
>python p_13504.py p_13504.py
# coding:iso-8859-9 Türkçe

import sys

dosyaAdı = sys.argv[1]
metin = ""
try:
    dosya = open (dos
---------------------------------------------------------------------------

# coding:iso-8859-9 Türkçe

>python p_13504.py p_13504.p  ** TEKRAR **
p_13504.p adlı dosyayı açamıyorum!
---------------------------------------------------------------------------

p_13504.p adlı dosyayı açamıyorum!
"""