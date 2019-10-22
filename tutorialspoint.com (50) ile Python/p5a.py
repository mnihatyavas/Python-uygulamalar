# coding:iso-8859-9 Türkçe
# 5: Python 3 - Loops

liste = [1,2,3,4,5,6,7,8,9,10]
tara = iter (liste) # Bir Iterator/tarayıcı nesnesi kurulur...

# Tarayıcı nesnesi düzenli for döngüsüyle taratılabilir...

for x in tara: print (x, end=" ")
print("\n")

# veya  while döngülü next() fonksiyonu denenebilir...
import sys
tara = iter (liste) # Tarayıcı tekrar başa alınır...

while True:
    try: print (next (tara), end=", ")
    except StopIteration:
        print ("\n\nListede taranacak eleman kalmadı!")
        sys.exit()
