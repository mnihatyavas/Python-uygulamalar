# coding:iso-8859-9 T�rk�e

G�nler = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print ("G�nler listesi:", G�nler)

G�nler = {"Ocak":31, "�ubat":28, "Mart":31, "Nisan":30, "May�s":31, "Haziran":30, "Temmuz":31, "A�ustos":31, "Eyl�l":30, "Ekim":31, "Kas�m":30, "Aral�k":31}
print ("\nG�nler s�zl���:", G�nler)

print()
s = {} # Bo� s�zl�k...
print (s)
s = {"A":100, "B":200} # key/anahtar ve value/de�er �ifti...
print (s)
print (s["B"], s["A"])
s["A"] = 400
s["C"] = 500
s["AB"] = 300 # Anahtar farkl�ysa sona ekler (ayr�ca append veya += gerekmez)...
s["C"] = 500 # Anahtar ayn�ysa eklemez, mevcudu (de�erini) de�i�tirir...
print (s)
del s["B"] # Anahtar-de�er �ifti silinir...
print (s)