# coding:iso-8859-9 T�rk�e
# p_12003.py: Return's�z, de�er d�nd�rmeyen ve d�nd�ren return'l� fonksiyonlar �rne�i.

from random import randint, random

def selam1 (a, b): dizge = "Selam sana, " + str (2019-b) + " ya��ndaki " + a;
def selam2 (a, b): dizge = "Selam sana, " + str (2019-b) + " ya��ndaki " + a; return;
def selam3 (a, b): dizge = "Selam sana, " + str (2019-b) + " ya��ndaki " + a; return dizge;

print ("Return'siz fonksiyon:", selam1 ("M.Nihat Yava�", 1957) )
print ("De�er g�ndermeyen return'l� fonksiyon:", selam2 ("M.Nihat Yava�", 1957) )
print ("De�er g�nderen return'l� fonksiyon:", selam3 ("M.Nihat Yava�", 1957) )


"""��kt�:
>python p_12003.py
Return'siz fonksiyon: None
De�er g�ndermeyen return'l� fonksiyon: None
De�er g�nderen return'l� fonksiyon: Selam sana, 62 ya��ndaki M.Nihat Yava�
"""