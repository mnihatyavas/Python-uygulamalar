# coding:iso-8859-9 T�rk�e

ad = input ("Okunacak dosya ad�n� girin: ")
if ad == "": ad = "p32502x.txt"

try:
    with open (ad, 'r') as dosya:
        metin = dosya.read()
except IOError: print ("\nHATA:", ad, "adl� dosyay� bulup da a�amad�m!")
else: print ("\n", ad, " adl� dosya metni:\n\n", metin, sep="")
finally: print ("\n'finally/sonu�ta' ifadeleri try-except-else hatas� olsa da olmasa da i�letilir!")
