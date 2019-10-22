# coding:iso-8859-9 Türkçe

Günler = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print ("Günler listesi:", Günler)

Günler = {"Ocak":31, "Şubat":28, "Mart":31, "Nisan":30, "Mayıs":31, "Haziran":30, "Temmuz":31, "Ağustos":31, "Eylül":30, "Ekim":31, "Kasım":30, "Aralık":31}
print ("\nGünler sözlüğü:", Günler)

print()
s = {} # Boş sözlük...
print (s)
s = {"A":100, "B":200} # key/anahtar ve value/değer çifti...
print (s)
print (s["B"], s["A"])
s["A"] = 400
s["C"] = 500
s["AB"] = 300 # Anahtar farklıysa sona ekler (ayrıca append veya += gerekmez)...
s["C"] = 500 # Anahtar aynıysa eklemez, mevcudu (değerini) değiştirir...
print (s)
del s["B"] # Anahtar-değer çifti silinir...
print (s)