# coding:iso-8859-9 T�rk�e
# p_13206.py: reduce(lambda fonk, liste) ile liste elemanlar�n�n toplam�, �arp�m� min-max'� �rne�i.

from random import randint
from functools import reduce

print ("'reduce' ile liste elemanlar�n� toplama:", "\n", "-"*40, sep="")
print ("[47,11,42,13] 4 adet liste elemanlar� toplam�:", reduce (lambda x,y: x+y, [47,11, 42,13]) )
print ("[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597] 18 adet s�ral� fibonaki liste elemanlar� toplam�:", reduce (lambda x,y: x+y, [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597]) )
print ("[randint(200) for i range(100)] 100 adet rasgele kapsaml� liste elemanlar� toplam�:", reduce (lambda x,y: x+y, [randint (0, 200) for i in range (100)]) )
#---------------------------------------------------------------------------------------------------------

print ("\n'reduce' ile liste elemanlar�n�n b�y�k veya k�����n�n tespiti:", "\n", "-"*61, sep="")
lambdam = lambda a,b: a if (a > b) else b
print ("[47,11,42,102,13] liste elemanlar�n�n b�y���:", reduce (lambdam, [47,11,42,102,13]) )
print ("[47,11,42,102,13] liste elemanlar�n�n k�����:", reduce (lambda a,b: a if (a<b) else b, [47,11,42,102,13]) )
#---------------------------------------------------------------------------------------------------------

print ("\n'reduce' ile s�ral� liste elemanlar�n�n toplam� ve �arp�m�:", "\n", "-"*58, sep="")
print ("�lk 100 say� listesinin toplam�:", reduce (lambda x,y: x+y, [i for i in range (1, 101)]) )
print ("�lk 100 say� listesinin �arp�m�:", reduce (lambda x,y: x*y, [i for i in range (1, 101)]) )
#---------------------------------------------------------------------------------------------------------

print ("\nPiyangoda 49 �ekili�ten 6's�n� kazanma �ans�:", end=" ")
print (reduce (lambda x, y: x*y, range (44, 50)) / reduce (lambda x, y: x*y, range (1, 7)), "'da 1'dir.", sep="" )

"""��kt�:
>python p_13206.py
'reduce' ile liste elemanlar�n� toplama:
----------------------------------------
[47,11,42,13] 4 adet liste elemanlar� toplam�: 113
[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597] 18 adet s�ral� fibonaki liste elemanlar� toplam�: 4180
[randint(200) for i range(100)] 100 adet rasgele kapsaml� liste elemanlar� toplam�: 10169

'reduce' ile liste elemanlar�n�n b�y�k veya k�����n�n tespiti:
-------------------------------------------------------------
[47,11,42,102,13] liste elemanlar�n�n b�y���: 102
[47,11,42,102,13] liste elemanlar�n�n k�����: 11

'reduce' ile s�ral� liste elemanlar�n�n toplam� ve �arp�m�:
----------------------------------------------------------
�lk 100 say� listesinin toplam�: 5050
�lk 100 say� listesinin �arp�m�: 93326215443944152681699238856266700490715968264
38162146859296389521759999322991560894146397615651828625369792082722375825118521
0916864000000000000000000000000

Piyangoda 49 �ekili�ten 6's�n� kazanma �ans�, dese de z�rva: 13983816.0'da 1'dir.
"""