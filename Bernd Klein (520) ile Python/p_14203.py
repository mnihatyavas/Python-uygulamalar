# coding:iso-8859-9 T�rk�e
# p_14203.py: Polinom s�n�f�n�n otomatik ve klasik �a�r�lan callable fonksiyonu �rne�i.

class Polinom:
    def __init__ (self, *katsay�lar): self.katsay�lar = katsay�lar [::-1]
    def __call__ (self, x):
        sonu� = 0
        for endeks, k in enumerate (self.katsay�lar): sonu� += k * x** endeks
        return sonu�

# Sabit bir fonksiyon: y=42
p1 = Polinom (42)

# D�z bir �izgi: y=0.75x+2
p2 = Polinom (0.75, 2)

# ���nc� dereceden bir  Polinom: y=1x^3-0.5x^2+0.75x+2
p3 = Polinom (1, -0.5, 0.75, 2)

print ("p1=42  p2=0.75*i+2  p3=1*i**3-0.5*i**2+0.75*i+2\n", "-"*47, sep="")
for i in range (1, 11): print ("{:2d} {} {:4.2f} {:6.2f}" .format (i, p1 (i), p2 (i), p3 (i)) )
#----------------------------------------------------------------------------------------------------

print ("\nOtomatik callable s�n�f fonksiyonu yerine, klasik s�n�f.fonksiyon(arg�man) kullan�m�:")
for i in range (1, 11): print ("{:2d} {} {:4.2f} {:6.2f}" .format (i, p1.__call__ (i), p2.__call__ (i), p3.__call__ (i)) )



"""��kt�:
>python p_14203.py
p1=42  p2=0.75*i+2  p3=1*i**3-0.5*i**2+0.75*i+2
-----------------------------------------------
 1 42 2.75   3.25
 2 42 3.50   9.50
 3 42 4.25  26.75
 4 42 5.00  61.00
 5 42 5.75 118.25
 6 42 6.50 204.50
 7 42 7.25 325.75
 8 42 8.00 488.00
 9 42 8.75 697.25
10 42 9.50 959.50

Callable fonksiyon s�n�f yerine, klasik s�n�f.fonksiyon(arg�man) kullan�m�:
 1 42 2.75   3.25
 2 42 3.50   9.50
 3 42 4.25  26.75
 4 42 5.00  61.00
 5 42 5.75 118.25
 6 42 6.50 204.50
 7 42 7.25 325.75
 8 42 8.00 488.00
 9 42 8.75 697.25
10 42 9.50 959.50
"""