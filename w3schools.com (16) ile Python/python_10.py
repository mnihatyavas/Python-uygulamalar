# coding:iso-8859-9 "T�rk�e"

import camelcase # C�mledeki t�m kelimelerin ilk harflerini b�y�kharf yapar

deve = camelcase.CamelCase()

c�mle = "import camelcase mod�l� c�mledeki t�m kelimelerin ilk harflerini b�y�kharf yapar."
print ("Orijinal c�mle: [" + c�mle + "]\n")
print ("CamelCase() c�mlesi: [" + deve.hump (c�mle))
