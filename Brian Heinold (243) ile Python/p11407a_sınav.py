# coding:iso-8859-9 Türkçe

class Yatırım:
    def __init__ (self, a, b):
        self.anapara = a
        self.faiz = b

    def dönüş_değeri (self, y):
        return self.anapara * (1+self.faiz/100) ** y

    def __str__ (self):
        return "Anapara: ${:,d}, Yıllık faiz oranı: {:.2f}%".format (self.anapara, self.faiz)

from random import *
try: para = abs (int (eval (input ("Yatırım anaparasını girin: "))))
except Exception: para = randint (10000, 1000000)
try: oran = abs (eval (input ("Bankanın teklif ettiği yıllık faiz oranını girin: ")))
except Exception: oran = randint (2, 25) + random()
try: yıl = abs (int (eval (input ("Yatırım yıl süresini girin: "))))
except Exception: yıl = randint (1, 20)

print()
yatır = Yatırım (para, oran)
print (yatır.__str__()) # Veya kısaca: print (yatır)
print ("{} yıllık bileşik faizli dönen para: {:,.2f}" .format (yıl, yatır.dönüş_değeri (yıl)) )
