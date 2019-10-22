# coding:iso-8859-9 T�rk�e

import os

ibare = input ("Python dosyalar�nda bulunmas�n� istedi�iniz ibare: ")
if ibare == "": ibare = "Nihat"

dizin = "C:/Users/pc/Desktop/MyFiles/4. Dersler/python/i�lenmi� �rnekler/Brian Heinold/"
dosyalar = os.listdir (dizin)
print ("\n[", dizin, "] dizininde <", ibare, "> ibaresini i�eren dosyalar�n listesi:\n", "-"*79, sep="" )
for d in dosyalar:
    if os.path.isfile (dizin+d):
        dosya = open (dizin+d).read()
        if ibare.lower() in dosya.lower(): print (d)

print()
os.chdir ("C:/Users/pc/Desktop/MyFiles/4. Dersler/python/")
dosyalar = os.listdir()
for d in dosyalar:
    if os.path.isfile (d):
        try: # Baz� �rn.exe dosyalar okunam�yorsa esge�...
            dosya = open (d).read()
            if ibare.lower() in dosya.lower(): print (d)
        except Exception: continue
#----------------------------------------------------------------------------------------

print ("\nAkt�el dizinimiz: [", os.getcwd(), "]", sep="")
print ("\nDizinimizdeki t�m dosyalar�n listesi:")
for dosya in os.listdir(): print (dosya)
print ("\nDizinimizdeki alt-dizinlerin listesi:")
for dosya in os.listdir():
    if os.path.isdir (dosya): print (dosya)
print ("\nDizinimizdeki dosyalar�n listesi:")
for dosya in os.listdir():
    if os.path.isfile (dosya): print (dosya)
