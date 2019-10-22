# coding:iso-8859-9 Türkçe

from random import randint
from math import trunc

# Virgüllerle ayrık 2 ayrı veri giriş yöntemi
a, b = eval (input ('Virgüllerle ayrık 2 sayı girin: '))
if a<b: a,b=b,a # (küçük/büyük) kontrolsüz, biçimsiz sonuçlar üretebiliyor...
print (a, "+", b, "=", a+b)
print (a, "-", b, "=", a-b)
print (a, "*", b, "=", a*b)
print (a, "/", b, "=", a/b)
""" Her 2 sayının da negatif olması durumunda, sonucun pozitif ve 
sıfırdan büyük çıkmasını isterseniz negatif küçüğü üste alabilirsiniz:
Yani eğer a=-5, b=-15 ise a, b'den büyük olduğu halde
print (b, "/", a, "=", b/a)
ifadesi sonucu +3 yansıtır
"""
print (a, "^", b, "=", a**b)
print (a, "%", b, "=", a%b)
print (a, "yüzde", b, "= %", (a-b)/b*100)

""" Çoklu yorum satırı
     Program adı: Tek ve çok satırlı python yorumları
     Kodlayan: M.Nihat Yavaş
     Tarih: 29.09.2018-23:23 """

""" veya
Çoklu yorum satırı
Program adı: Tek ve çok satırlı python yorumları
Kodlayan: M.Nihat Yavaş
Tarih: 29.09.2018-23:23
"""
Çıktı=""" veya
Çoklu yorum satırı
Program adı: Tek ve çok satırlı python yorumları
Kodlayan: M.Nihat Yavaş
Tarih: 29.09.2018-23:23
"""