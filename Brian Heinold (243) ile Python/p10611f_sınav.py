# coding:iso-8859-9 Türkçe

kelime = input ("k basamaklı şifreleme için dizge girin: ")
k = int (eval (input ("Kaçarlı şifreleme oluşturacaksın: ")))
if k > len (kelime)//2: k = len(kelime)//2
elif k < 2: k = 2
şifreli=deşifreli=''
for i in range (k-1, len(kelime), k):
    for j in range (i, i-k, -1): şifreli += kelime[j]
for i in range (len(kelime)%k): şifreli += kelime[-i-1]
print ("\n", k, "'li genel şifreleme: ", şifreli, sep="")

for i in range (k-1, len(şifreli), k):
    for j in range (i, i-k, -1): deşifreli += şifreli[j]
for i in range (len(şifreli)%k): deşifreli += şifreli[-i-1]
print ("\n", k, "'li genel deşifreleme: ", deşifreli, sep="")
