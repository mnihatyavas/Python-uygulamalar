# coding:iso-8859-9 Türkçe
# p_21002.py: Polinom sınıfıyla katsayılar, toplama ve çıkarma sonucu grafiğin çizilmesi örneği.

class Polinom:
    def __init__ (self, *katsayılarımız):
        # Katsayı verilerinin girişi: a_n, ...a_1, a_0 şeklindedir...
        self.katsayılar = katsayılarımız [::-1] # for-range verimliliği gereği ters listeye dönüştürülüp saklanır...

    def __str__ (self): # Çıktı tekrar düz listeye çevrilir...
        return "Polinom " + str (self.katsayılar [::-1])

    def __call__ (self, x): # Callable/çağrılabilir fonksiyon...
        sonuç = 0
        for endeks, katsayı in enumerate (self.katsayılar): sonuç += katsayı * x** endeks
        return sonuç
            
    def __add__ (self, diğeri):
        k1 = self.katsayılar
        k2 = diğeri.katsayılar
        sonuç = [sum (t) for t in Polinom.enuzun (k1, k2)]
        return Polinom (*sonuç)

    def __sub__ (self, diğeri):
        k1 = self.katsayılar
        k2 = diğeri.katsayılar
        sonuç = [t1 - t2 for t1, t2 in Polinom.enuzun (k1, k2)]
        return Polinom (*sonuç)

    @staticmethod
    def enuzun (k1, k2, fillchar=None):    
        for i in range (max (len (k1), len (k2))):
            if i >= len (k1): yield (fillchar, k2 [i])
            elif i >= len (k2): yield (k1 [i], fillchar)
            else: yield (k1 [i], k2 [i])
            i += 1

    def türev (self):
        türevliKatsayılar = []
        üs = 1
        for i in range (1, len (self.katsayılar)):
            türevliKatsayılar.append (self.katsayılar [i] * üs)
            üs += 1
        return Polinom (*türevliKatsayılar [::-1])


if __name__ == "__main__":
    p = Polinom (1, 0, -4, 3, 0) # x^4 - 4x^2 + 3x
    print (p) # p için: __str__ çağrılır...

    print ("\nx=[-3,4] arası p(x) değerleri:\nx, p(x) =")
    for x in range (-3, 5): print (x, p(x) ) # p(x) için: __call__ çağrılır...

    import numpy as np
    import matplotlib.pyplot as mp
    mp.style.use ("dark_background")
    X = np.linspace (-3, 4, 100, endpoint=True)
    F = p (X)
    mp.plot (X, F)
    mp.show()


"""Çıktı:
>python p_21002.py
Polinom (1, 0, -4, 3, 0)

x=[-3,4] arası p(x) değerleri:
x, p(x) =
-3 36
-2 -6
-1 -6
0 0
1 0
2 6
3 54
4 204
"""