# coding:iso-8859-9 Türkçe

ad = input ("Okunacak dosya adını girin: ")
if ad == "": ad = "p32502x.txt"

try:
    with open (ad, 'r') as dosya:
        metin = dosya.read()
except IOError: print ("\nHATA:", ad, "adlı dosyayı bulup da açamadım!")
else: print ("\n", ad, " adlı dosya metni:\n\n", metin, sep="")
finally: print ("\n'finally/sonuçta' ifadeleri try-except-else hatası olsa da olmasa da işletilir!")
