# coding:iso-8859-9 Türkçe
# p_13206.py: reduce(lambda fonk, liste) ile liste elemanlarının toplamı, çarpımı min-max'ı örneği.

from random import randint
from functools import reduce

print ("'reduce' ile liste elemanlarını toplama:", "\n", "-"*40, sep="")
print ("[47,11,42,13] 4 adet liste elemanları toplamı:", reduce (lambda x,y: x+y, [47,11, 42,13]) )
print ("[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597] 18 adet sıralı fibonaki liste elemanları toplamı:", reduce (lambda x,y: x+y, [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597]) )
print ("[randint(200) for i range(100)] 100 adet rasgele kapsamlı liste elemanları toplamı:", reduce (lambda x,y: x+y, [randint (0, 200) for i in range (100)]) )
#---------------------------------------------------------------------------------------------------------

print ("\n'reduce' ile liste elemanlarının büyük veya küçüğünün tespiti:", "\n", "-"*61, sep="")
lambdam = lambda a,b: a if (a > b) else b
print ("[47,11,42,102,13] liste elemanlarının büyüğü:", reduce (lambdam, [47,11,42,102,13]) )
print ("[47,11,42,102,13] liste elemanlarının küçüğü:", reduce (lambda a,b: a if (a<b) else b, [47,11,42,102,13]) )
#---------------------------------------------------------------------------------------------------------

print ("\n'reduce' ile sıralı liste elemanlarının toplamı ve çarpımı:", "\n", "-"*58, sep="")
print ("İlk 100 sayı listesinin toplamı:", reduce (lambda x,y: x+y, [i for i in range (1, 101)]) )
print ("İlk 100 sayı listesinin çarpımı:", reduce (lambda x,y: x*y, [i for i in range (1, 101)]) )
#---------------------------------------------------------------------------------------------------------

print ("\nPiyangoda 49 çekilişten 6'sını kazanma şansı:", end=" ")
print (reduce (lambda x, y: x*y, range (44, 50)) / reduce (lambda x, y: x*y, range (1, 7)), "'da 1'dir.", sep="" )

"""Çıktı:
>python p_13206.py
'reduce' ile liste elemanlarını toplama:
----------------------------------------
[47,11,42,13] 4 adet liste elemanları toplamı: 113
[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597] 18 adet sıralı fibonaki liste elemanları toplamı: 4180
[randint(200) for i range(100)] 100 adet rasgele kapsamlı liste elemanları toplamı: 10169

'reduce' ile liste elemanlarının büyük veya küçüğünün tespiti:
-------------------------------------------------------------
[47,11,42,102,13] liste elemanlarının büyüğü: 102
[47,11,42,102,13] liste elemanlarının küçüğü: 11

'reduce' ile sıralı liste elemanlarının toplamı ve çarpımı:
----------------------------------------------------------
İlk 100 sayı listesinin toplamı: 5050
İlk 100 sayı listesinin çarpımı: 93326215443944152681699238856266700490715968264
38162146859296389521759999322991560894146397615651828625369792082722375825118521
0916864000000000000000000000000

Piyangoda 49 çekilişten 6'sını kazanma şansı, dese de zırva: 13983816.0'da 1'dir.
"""