# coding:iso-8859-9 Türkçe

import os

ibare = input ("Python dosyalarında bulunmasını istediğiniz ibare: ")
if ibare == "": ibare = "Nihat"

dizin = "C:/Users/pc/Desktop/MyFiles/4. Dersler/python/işlenmiş örnekler/Brian Heinold/"
dosyalar = os.listdir (dizin)
print ("\n[", dizin, "] dizininde <", ibare, "> ibaresini içeren dosyaların listesi:\n", "-"*79, sep="" )
for d in dosyalar:
    if os.path.isfile (dizin+d):
        dosya = open (dizin+d).read()
        if ibare.lower() in dosya.lower(): print (d)

print()
os.chdir ("C:/Users/pc/Desktop/MyFiles/4. Dersler/python/")
dosyalar = os.listdir()
for d in dosyalar:
    if os.path.isfile (d):
        try: # Bazı örn.exe dosyalar okunamıyorsa esgeç...
            dosya = open (d).read()
            if ibare.lower() in dosya.lower(): print (d)
        except Exception: continue
#----------------------------------------------------------------------------------------

print ("\nAktüel dizinimiz: [", os.getcwd(), "]", sep="")
print ("\nDizinimizdeki tüm dosyaların listesi:")
for dosya in os.listdir(): print (dosya)
print ("\nDizinimizdeki alt-dizinlerin listesi:")
for dosya in os.listdir():
    if os.path.isdir (dosya): print (dosya)
print ("\nDizinimizdeki dosyaların listesi:")
for dosya in os.listdir():
    if os.path.isfile (dosya): print (dosya)
