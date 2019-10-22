# coding:iso-8859-9 Turkish

# Liste'ye okuturken strip() gerekir..
L = [satır.strip() for satır in open ("Örnek1.txt")] # Veya rstrip() / lstrip()
print (L)

print()
for k in L: print (k)

print()
metin = open ("C:/Users/pc/Desktop/MyFiles/4. Dersler/python/işlenmiş örnekler/Brian Heinold/.txt dosyaları/demo1.txt").read()
print (metin)

print() # Metin dizgesine okutmada strip()'lemeye gerek yok...
metin = open ("C:/Users/pc/Desktop/MyFiles/4. Dersler/python/Örnek1.txt").read()
print (metin)

dosya = open ("Örnek2.txt", "w")
for i in range (10): print ("Dosyaya eklenen satır no:", i, file = dosya)
dosya.close()

print()
metin = open ("Örnek2.txt").read()
print (metin)

dosya = open ("Örnek2.txt", "w")
for derece in range (0, 101, 10): print (derece, "derece =", (derece*9/5+32), "fahrenhayt", file = dosya)
dosya.close()

print()
metin = open ("Örnek2.txt").read()
print (metin)

