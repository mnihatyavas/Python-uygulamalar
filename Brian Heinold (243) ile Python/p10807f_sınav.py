# coding:iso-8859-9 T�rk�e

from random import randint
L1 = [["feet","in�","yard","mil","mm","sm","m","km",], [1,12,1/3,1/6000,304.8,30.48,0.3048,0.0003048]]
try: a = abs (eval (input ("[1:feet; 2:in�; 3:yard; 4:mil; 5:mm; 6:sm; 7:m; 8:km] girin: "))) -1
except Exception: a = randint(0,7)
if a >=8 or a <= -1: a = randint(0,7)

try: b = abs (eval (input ("De�eri girin: ")))
except Exception: b = randint (1,100)

try: c = abs (eval (input ("�evirmek istedi�iniz �l�e�i girin: "))) -1
except Exception: c = randint(0,7)
if c >= 8 or c <= -1: c = randint(0,7)

if a != 0: d = b/L1[1][a]
else: d = 1
print (b, L1[0][a], "=", L1[1][c]*d, L1[0][c], "d�r")
