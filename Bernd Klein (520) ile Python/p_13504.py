# coding:iso-8859-9 T�rk�e
# p_13504.py: try-except-else ile hata y�netimli dosya okuma �rne�i.

import sys

dosyaAd� = sys.argv[1]
metin = ""
try:
    dosya = open (dosyaAd�, 'r')
    metin = dosya.read().strip()
    dosya.close() # Her�� sat�rdan biri IOError istisnas�n� f�rlatabilir...
except IOError: print (dosyaAd�, "adl� dosyay� a�am�yorum!")

if metin: print (metin[:100] )
print ("-"*75, "\n", sep="")
#-----------------------------------------------------------------------------------------------------

metin = []
try: dosya = open (dosyaAd�, 'r') # Sadece bu sat�r IOError istisnas�n� f�rlatabilir...
except IOError: print (dosyaAd�, "adl� dosyay� a�am�yorum!")
else:
    metin = dosya.readlines()
    dosya.close()

if metin: print (metin[0] )

"""��kt�:
>python p_13504.py p_13504.py
# coding:iso-8859-9 T�rk�e

import sys

dosyaAd� = sys.argv[1]
metin = ""
try:
    dosya = open (dos
---------------------------------------------------------------------------

# coding:iso-8859-9 T�rk�e

>python p_13504.py p_13504.p  ** TEKRAR **
p_13504.p adl� dosyay� a�am�yorum!
---------------------------------------------------------------------------

p_13504.p adl� dosyay� a�am�yorum!
"""