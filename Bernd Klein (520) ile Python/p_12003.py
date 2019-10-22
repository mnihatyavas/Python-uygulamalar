# coding:iso-8859-9 Türkçe
# p_12003.py: Return'süz, değer döndürmeyen ve döndüren return'lü fonksiyonlar örneği.

from random import randint, random

def selam1 (a, b): dizge = "Selam sana, " + str (2019-b) + " yaşındaki " + a;
def selam2 (a, b): dizge = "Selam sana, " + str (2019-b) + " yaşındaki " + a; return;
def selam3 (a, b): dizge = "Selam sana, " + str (2019-b) + " yaşındaki " + a; return dizge;

print ("Return'siz fonksiyon:", selam1 ("M.Nihat Yavaş", 1957) )
print ("Değer göndermeyen return'lü fonksiyon:", selam2 ("M.Nihat Yavaş", 1957) )
print ("Değer gönderen return'lü fonksiyon:", selam3 ("M.Nihat Yavaş", 1957) )


"""Çıktı:
>python p_12003.py
Return'siz fonksiyon: None
Değer göndermeyen return'lü fonksiyon: None
Değer gönderen return'lü fonksiyon: Selam sana, 62 yaşındaki M.Nihat Yavaş
"""