# coding:iso-8859-9 Türkçe

from random import randint

kelime = input ("Anagram için herhangi BİR kelime girin: ").lower().replace (" ", "")
if len(kelime) < 3: kelime = "anagram"
for i in range (len(kelime)-1):
    k = kelime[i]
    sonuç = kelime[:i] + kelime[i+1] + k + kelime[i+2:]
    print ("Kelimenin ", i+1, "'.inci anagramı: ", sonuç, sep="")
print()
kelime = (kelime + " ")*3
şifreli=''
for i in range (0, len(kelime)-1, 2):
    şifreli= şifreli + kelime[i+1] + kelime[i]
print ("2'li şifreleme:", şifreli)
deşifreli=''
for i in range (0, len(şifreli)-1, 2):
    deşifreli= deşifreli + şifreli[i+1] + şifreli[i]
print ("2'li deşifreleme:", deşifreli)
print()
şifreli=deşifreli=''
for i in range (0, len(kelime)-2, 3):
    şifreli += kelime[i+2] + kelime[i+1] + kelime[i]
print ("3'lü şifreleme:", şifreli)
deşifreli=''
for i in range (0, len(şifreli)-2, 3):
    deşifreli += şifreli[i+2] + şifreli[i+1] + şifreli[i]
print ("3'lü deşifreleme:", deşifreli)
print()
k = int (eval (input ("Kaçarlı şifreleme oluşturacaksın: ")))
if k > len (kelime)-k: k = len(kelime)-k
elif k < 2: k = 2
şifreli=deşifreli=''
for i in range (0, len(kelime)+1-k, k):
    for j in range (i+k-1, i-1, -1):
        şifreli += kelime[j]
print (k, "'li genel şifreleme: ", şifreli, sep="")
for i in range (0, len(şifreli)+1-k, k):
    for j in range (i+k-1, i-1, -1):
        deşifreli += şifreli[j]
print (k, "'li genel deşifreleme: ", deşifreli, sep="")
