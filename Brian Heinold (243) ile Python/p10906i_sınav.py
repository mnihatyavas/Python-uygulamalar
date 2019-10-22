# coding:iso-8859-9 Türkçe

pay = int (eval (input ("Payı girin: ")))
payda = int (eval (input ("Paydayı girin: ")))
dizge = str (pay/payda)
küsürat = dizge[dizge.index (".")+1:]
if eval (küsürat) != 0:
    basamak = 0
    while not (1 <= basamak <= len (küsürat)): basamak = int (eval (input (str (len (küsürat)) + " haneli küsüratın kaçıncı basamağını göreceksin: ")))
    print (dizge, "-->", küsürat, "-->", küsürat[basamak-1])
else: print ("Bu bölümün küsüratı yok:", dizge)
