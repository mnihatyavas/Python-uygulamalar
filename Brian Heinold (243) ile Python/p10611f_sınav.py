# coding:iso-8859-9 T�rk�e

kelime = input ("k basamakl� �ifreleme i�in dizge girin: ")
k = int (eval (input ("Ka�arl� �ifreleme olu�turacaks�n: ")))
if k > len (kelime)//2: k = len(kelime)//2
elif k < 2: k = 2
�ifreli=de�ifreli=''
for i in range (k-1, len(kelime), k):
    for j in range (i, i-k, -1): �ifreli += kelime[j]
for i in range (len(kelime)%k): �ifreli += kelime[-i-1]
print ("\n", k, "'li genel �ifreleme: ", �ifreli, sep="")

for i in range (k-1, len(�ifreli), k):
    for j in range (i, i-k, -1): de�ifreli += �ifreli[j]
for i in range (len(�ifreli)%k): de�ifreli += �ifreli[-i-1]
print ("\n", k, "'li genel de�ifreleme: ", de�ifreli, sep="")
