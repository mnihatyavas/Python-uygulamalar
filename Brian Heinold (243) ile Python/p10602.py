# coding:iso-8859-9 T�rk�e

s = ''
for i in range (10000):
    k = input ('Bir karakter gir [��k:q/Q]: ')
    if  k=='q' or k=='Q': break
    s = s + k
print ("-"*50, "\nGirdi�iniz c�mle: ", s, "\n", "-"*50, sep="")

if "�" in s: print ("Girdi�iniz c�mlede '�' harfi mevcuttur.")
if "Yava�" in s: print ("Girdi�iniz c�mlede 'Yava�' kelimesi mevcuttur.")
if ("�" or "�" or "�" or "�" or "�" or "�" or "�" or "�" or "�" or "�" or "�" or "�") in s:
    print ("Girdi�iniz c�mle T�rk�e karakter i�ermektedir.")
if ("." or "," or ":" or ";" or ".." or "...") in s:
    print ("Girdi�iniz c�mle noktalama karakteri i�ermektedir.")
