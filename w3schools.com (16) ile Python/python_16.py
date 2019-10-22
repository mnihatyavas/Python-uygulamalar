# coding:iso-8859-9 Türkçe

X = [[1,2,3],  
       [4,5,6],  
       [7,8,9]]  

Y = [[10,11,12],  
       [13,14,15],  
       [16,17,18]]  

Sonuç = [[0,0,0],  
                [0,0,0],  
                [0,0,0]]  

for i in range (len (X)):  
    for j in range (len (X[0])):  
        Sonuç[i][j] = X[i][j] + Y[i][j]

print ("İki matrisin TOPLAMI (X + Y):\n=============================")
for s in Sonuç: print (s)
print()

for i in range (len(X)):  
    for j in range (len(Y[0])):  
        for k in range (len(Y)):  
            Sonuç[i][j] += X[i][k] * Y[k][j]  

print ("İki matrisin ÇARPIMI (X * Y):\n=============================")
for s in Sonuç: print (s)

print()
# Elenecek noktalamaları belirleyelim:
noktalama = '''''!()-[]{};:'"\,<>./?@#$%^&*+_~='''  

cümle1 = input ("Noktalamalı cümlenizi girin: ")  
cümle2 = ""  

for k in cümle1:
    if k not in noktalama: cümle2 = cümle2 + k

print ("Noktalamaları elenmiş cümlem: [" + cümle2 + "]") 

print()
kelimeler = cümle2.split() # Kelimeleri araboşluklardan bölüp liste yapar...
kelimeler.sort() # kelimeler listesini a->z sıralar
print ("Artan sıralamalı kelimeler listesi:\n===================================")
for kelime in kelimeler: print (kelime)
