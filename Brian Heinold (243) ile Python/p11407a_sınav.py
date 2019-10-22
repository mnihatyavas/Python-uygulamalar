# coding:iso-8859-9 T�rk�e

class Yat�r�m:
    def __init__ (self, a, b):
        self.anapara = a
        self.faiz = b

    def d�n��_de�eri (self, y):
        return self.anapara * (1+self.faiz/100) ** y

    def __str__ (self):
        return "Anapara: ${:,d}, Y�ll�k faiz oran�: {:.2f}%".format (self.anapara, self.faiz)

from random import *
try: para = abs (int (eval (input ("Yat�r�m anaparas�n� girin: "))))
except Exception: para = randint (10000, 1000000)
try: oran = abs (eval (input ("Bankan�n teklif etti�i y�ll�k faiz oran�n� girin: ")))
except Exception: oran = randint (2, 25) + random()
try: y�l = abs (int (eval (input ("Yat�r�m y�l s�resini girin: "))))
except Exception: y�l = randint (1, 20)

print()
yat�r = Yat�r�m (para, oran)
print (yat�r.__str__()) # Veya k�saca: print (yat�r)
print ("{} y�ll�k bile�ik faizli d�nen para: {:,.2f}" .format (y�l, yat�r.d�n��_de�eri (y�l)) )
