# coding:iso-8859-9 T�rk�e
# p_13002.py: Disk ve internet dosyas�ndan re.search aramas� �rne�i.

import re

ajanda = open ("p_13002x.txt")
print ("'p_13002x.txt' adl� telefon rehberindeki 'J.*Neu' uyanlar listesi:")
for sat�r in ajanda:
    if re.search (r"J.*Neu", sat�r): print (sat�r.rstrip() )
ajanda.close()
print ("-"*75, "\n")
#-----------------------------------------------------------------------------------------------------

from urllib.request import urlopen

print ("'https://www.python-course.eu/simpsons_phone_book.txt' adl� telefon rehberindeki 'J.*Neu' uyanlar listesi:")
with urlopen ('https://www.python-course.eu/simpsons_phone_book.txt') as ajanda:
    for sat�r in ajanda:
        # Bir byte dizgesi olan sat�r� utf-8'e �evirelim...
        sat�r = sat�r.decode ('utf-8').rstrip()
        if re.search (r"J.*Neu", sat�r): print (sat�r)

"""��kt�:
>python p_13002.py
'p_13002x.txt' adl� telefon rehberindeki 'J.*Neu' uyanlar listesi:
Jack Neu 555-7666
Jeb Neu 555-5543
Jennifer Neu 555-3652
---------------------------------------------------------------------------

'https://www.python-course.eu/simpsons_phone_book.txt' adl� telefon rehberindeki
 'J.*Neu' uyanlar listesi:
Jack Neu 555-7666
Jeb Neu 555-5543
Jennifer Neu 555-3652
"""