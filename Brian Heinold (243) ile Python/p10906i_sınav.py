# coding:iso-8859-9 T�rk�e

pay = int (eval (input ("Pay� girin: ")))
payda = int (eval (input ("Payday� girin: ")))
dizge = str (pay/payda)
k�s�rat = dizge[dizge.index (".")+1:]
if eval (k�s�rat) != 0:
    basamak = 0
    while not (1 <= basamak <= len (k�s�rat)): basamak = int (eval (input (str (len (k�s�rat)) + " haneli k�s�rat�n ka��nc� basama��n� g�receksin: ")))
    print (dizge, "-->", k�s�rat, "-->", k�s�rat[basamak-1])
else: print ("Bu b�l�m�n k�s�rat� yok:", dizge)
