# coding:iso-8859-9 T�rk�e

X = [[1,2,3],  
       [4,5,6],  
       [7,8,9]]  

Y = [[10,11,12],  
       [13,14,15],  
       [16,17,18]]  

Sonu� = [[0,0,0],  
                [0,0,0],  
                [0,0,0]]  

for i in range (len (X)):  
    for j in range (len (X[0])):  
        Sonu�[i][j] = X[i][j] + Y[i][j]

print ("�ki matrisin TOPLAMI (X + Y):\n=============================")
for s in Sonu�: print (s)
print()

for i in range (len(X)):  
    for j in range (len(Y[0])):  
        for k in range (len(Y)):  
            Sonu�[i][j] += X[i][k] * Y[k][j]  

print ("�ki matrisin �ARPIMI (X * Y):\n=============================")
for s in Sonu�: print (s)

print()
# Elenecek noktalamalar� belirleyelim:
noktalama = '''''!()-[]{};:'"\,<>./?@#$%^&*+_~='''  

c�mle1 = input ("Noktalamal� c�mlenizi girin: ")  
c�mle2 = ""  

for k in c�mle1:
    if k not in noktalama: c�mle2 = c�mle2 + k

print ("Noktalamalar� elenmi� c�mlem: [" + c�mle2 + "]") 

print()
kelimeler = c�mle2.split() # Kelimeleri arabo�luklardan b�l�p liste yapar...
kelimeler.sort() # kelimeler listesini a->z s�ralar
print ("Artan s�ralamal� kelimeler listesi:\n===================================")
for kelime in kelimeler: print (kelime)
