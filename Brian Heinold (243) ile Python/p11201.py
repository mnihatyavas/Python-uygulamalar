# coding:iso-8859-9 Turkish

# Liste'ye okuturken strip() gerekir..
L = [sat�r.strip() for sat�r in open ("�rnek1.txt")] # Veya rstrip() / lstrip()
print (L)

print()
for k in L: print (k)

print()
metin = open ("C:/Users/pc/Desktop/MyFiles/4. Dersler/python/i�lenmi� �rnekler/Brian Heinold/.txt dosyalar�/demo1.txt").read()
print (metin)

print() # Metin dizgesine okutmada strip()'lemeye gerek yok...
metin = open ("C:/Users/pc/Desktop/MyFiles/4. Dersler/python/�rnek1.txt").read()
print (metin)

dosya = open ("�rnek2.txt", "w")
for i in range (10): print ("Dosyaya eklenen sat�r no:", i, file = dosya)
dosya.close()

print()
metin = open ("�rnek2.txt").read()
print (metin)

dosya = open ("�rnek2.txt", "w")
for derece in range (0, 101, 10): print (derece, "derece =", (derece*9/5+32), "fahrenhayt", file = dosya)
dosya.close()

print()
metin = open ("�rnek2.txt").read()
print (metin)

