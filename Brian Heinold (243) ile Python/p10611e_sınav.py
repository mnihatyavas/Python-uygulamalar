# coding:iso-8859-9 T�rk�e

from random import randint

kelime = input ("Anagram i�in herhangi B�R kelime girin: ").lower().replace (" ", "")
if len(kelime) < 3: kelime = "anagram"
for i in range (len(kelime)-1):
    k = kelime[i]
    sonu� = kelime[:i] + kelime[i+1] + k + kelime[i+2:]
    print ("Kelimenin ", i+1, "'.inci anagram�: ", sonu�, sep="")
print()
kelime = (kelime + " ")*3
�ifreli=''
for i in range (0, len(kelime)-1, 2):
    �ifreli= �ifreli + kelime[i+1] + kelime[i]
print ("2'li �ifreleme:", �ifreli)
de�ifreli=''
for i in range (0, len(�ifreli)-1, 2):
    de�ifreli= de�ifreli + �ifreli[i+1] + �ifreli[i]
print ("2'li de�ifreleme:", de�ifreli)
print()
�ifreli=de�ifreli=''
for i in range (0, len(kelime)-2, 3):
    �ifreli += kelime[i+2] + kelime[i+1] + kelime[i]
print ("3'l� �ifreleme:", �ifreli)
de�ifreli=''
for i in range (0, len(�ifreli)-2, 3):
    de�ifreli += �ifreli[i+2] + �ifreli[i+1] + �ifreli[i]
print ("3'l� de�ifreleme:", de�ifreli)
print()
k = int (eval (input ("Ka�arl� �ifreleme olu�turacaks�n: ")))
if k > len (kelime)-k: k = len(kelime)-k
elif k < 2: k = 2
�ifreli=de�ifreli=''
for i in range (0, len(kelime)+1-k, k):
    for j in range (i+k-1, i-1, -1):
        �ifreli += kelime[j]
print (k, "'li genel �ifreleme: ", �ifreli, sep="")
for i in range (0, len(�ifreli)+1-k, k):
    for j in range (i+k-1, i-1, -1):
        de�ifreli += �ifreli[j]
print (k, "'li genel de�ifreleme: ", de�ifreli, sep="")
