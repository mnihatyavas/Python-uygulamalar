# coding:iso-8859-9 T�rk�e
# 5: Python 3 - Loops

liste = [1,2,3,4,5,6,7,8,9,10]
tara = iter (liste) # Bir Iterator/taray�c� nesnesi kurulur...

# Taray�c� nesnesi d�zenli for d�ng�s�yle tarat�labilir...

for x in tara: print (x, end=" ")
print("\n")

# veya  while d�ng�l� next() fonksiyonu denenebilir...
import sys
tara = iter (liste) # Taray�c� tekrar ba�a al�n�r...

while True:
    try: print (next (tara), end=", ")
    except StopIteration:
        print ("\n\nListede taranacak eleman kalmad�!")
        sys.exit()
