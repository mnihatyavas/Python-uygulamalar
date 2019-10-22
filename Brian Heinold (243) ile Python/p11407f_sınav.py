# coding:iso-8859-9 Türkçe

class Çevirici:
    def __init__ (self, birim, değer):
        self.b = birim
        self.d = değer
        if self.b == 1: self.d = self.d*10**(-3)
        elif self.b == 2: self.d = self.d*10**(-2)
        elif self.b == 4: self.d = self.d*10**(3)
        elif self.b == 5: self.d = self.d*0.0254
        elif self.b == 6: self.d = self.d*0.3048
        elif self.b == 7: self.d = self.d*0.9144
        elif self.b == 8: self.d = self.d*1609

    def mm (self): return self.d*1000
    def sm (self): return self.d*100
    def m (self): return self.d
    def km (self): return self.d*0.001
    def inç (self): return self.d*100/2.54
    def fit (self): return self.d*100/30.48
    def yard (self): return self.d*100/91.44
    def mil (self): return self.d/1609

from random import randint, random
birim1 = 0
while not (0<birim1<9):
    try: birim1 = abs (int (eval (input ("1.ölçü birimini gir [1:mm, 2:sm, 3:m, 4:km, 5:inç, 6:fit, 7:yard, 8:mil]: "))))
    except Exception: birim1 = randint (1, 8)

try: değer = abs (eval (input ("1.ölçekli değeri gir: ")))
except Exception: değer = randint (0, 40*10**3) + random()

birim2 = 0
while not (0<birim2<9):
    try: birim2 = abs (int (eval (input ("\n2.ölçü birimini gir [1:mm, 2:sm, 3:m, 4:km, 5:inç, 6:fit, 7:yard, 8:mil]: "))))
    except Exception: birim2 = randint (1, 8)

L = ["milimetre", "santimetre", "metre", "kilometre", "inç", "fit", "yard", "mil"]
çevir = Çevirici (birim1, değer)
#print ("\n{:,f} {} = {:,.2f} metre'dir.".format (değer, L[birim1-1], çevir.d ) )

print()
if birim2 == 1: print ("{:,.2f} {} = {:,.2f} mili metre'dir.".format (değer, L[birim1-1], çevir.mm(), L[birim2-1]) )
elif birim2 == 2: print ("{:,.2f} {} = {:,.2f} santi metre'dir.".format (değer, L[birim1-1], çevir.sm(), L[birim2-1]) )
elif birim2 == 3: print ("{:,.2f} {} = {:,.2f} metre'dir.".format (değer, L[birim1-1], çevir.m(), L[birim2-1]) )
elif birim2 == 4: print ("{:,.2f} {} = {:,.2f} kilo metre'dir.".format (değer, L[birim1-1], çevir.km(), L[birim2-1]) )
elif birim2 == 5: print ("{:,.2f} {} = {:,.2f} inç'dir.".format (değer, L[birim1-1], çevir.inç(), L[birim2-1]) )
elif birim2 == 6: print ("{:,.2f} {} = {:,.2f} fit'dir.".format (değer, L[birim1-1], çevir.fit(), L[birim2-1]) )
elif birim2 == 7: print ("{:,.2f} {} = {:,.2f} yard'dır.".format (değer, L[birim1-1], çevir.yard(), L[birim2-1]) )
elif birim2 == 8: print ("{:,.2f} {} = {:,.2f} mil'dir.".format (değer, L[birim1-1], çevir.mil(), L[birim2-1]) )
