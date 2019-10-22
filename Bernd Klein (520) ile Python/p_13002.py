# coding:iso-8859-9 Türkçe
# p_13002.py: Disk ve internet dosyasından re.search araması örneği.

import re

ajanda = open ("p_13002x.txt")
print ("'p_13002x.txt' adlı telefon rehberindeki 'J.*Neu' uyanlar listesi:")
for satır in ajanda:
    if re.search (r"J.*Neu", satır): print (satır.rstrip() )
ajanda.close()
print ("-"*75, "\n")
#-----------------------------------------------------------------------------------------------------

from urllib.request import urlopen

print ("'https://www.python-course.eu/simpsons_phone_book.txt' adlı telefon rehberindeki 'J.*Neu' uyanlar listesi:")
with urlopen ('https://www.python-course.eu/simpsons_phone_book.txt') as ajanda:
    for satır in ajanda:
        # Bir byte dizgesi olan satırı utf-8'e çevirelim...
        satır = satır.decode ('utf-8').rstrip()
        if re.search (r"J.*Neu", satır): print (satır)

"""Çıktı:
>python p_13002.py
'p_13002x.txt' adlı telefon rehberindeki 'J.*Neu' uyanlar listesi:
Jack Neu 555-7666
Jeb Neu 555-5543
Jennifer Neu 555-3652
---------------------------------------------------------------------------

'https://www.python-course.eu/simpsons_phone_book.txt' adlı telefon rehberindeki
 'J.*Neu' uyanlar listesi:
Jack Neu 555-7666
Jeb Neu 555-5543
Jennifer Neu 555-3652
"""