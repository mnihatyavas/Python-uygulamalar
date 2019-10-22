# coding:iso-8859-9 T�rk�e
# p_21002.py: Polinom s�n�f�yla katsay�lar, toplama ve ��karma sonucu grafi�in �izilmesi �rne�i.

class Polinom:
    def __init__ (self, *katsay�lar�m�z):
        # Katsay� verilerinin giri�i: a_n, ...a_1, a_0 �eklindedir...
        self.katsay�lar = katsay�lar�m�z [::-1] # for-range verimlili�i gere�i ters listeye d�n��t�r�l�p saklan�r...

    def __str__ (self): # ��kt� tekrar d�z listeye �evrilir...
        return "Polinom " + str (self.katsay�lar [::-1])

    def __call__ (self, x): # Callable/�a�r�labilir fonksiyon...
        sonu� = 0
        for endeks, katsay� in enumerate (self.katsay�lar): sonu� += katsay� * x** endeks
        return sonu�
            
    def __add__ (self, di�eri):
        k1 = self.katsay�lar
        k2 = di�eri.katsay�lar
        sonu� = [sum (t) for t in Polinom.enuzun (k1, k2)]
        return Polinom (*sonu�)

    def __sub__ (self, di�eri):
        k1 = self.katsay�lar
        k2 = di�eri.katsay�lar
        sonu� = [t1 - t2 for t1, t2 in Polinom.enuzun (k1, k2)]
        return Polinom (*sonu�)

    @staticmethod
    def enuzun (k1, k2, fillchar=None):    
        for i in range (max (len (k1), len (k2))):
            if i >= len (k1): yield (fillchar, k2 [i])
            elif i >= len (k2): yield (k1 [i], fillchar)
            else: yield (k1 [i], k2 [i])
            i += 1

    def t�rev (self):
        t�revliKatsay�lar = []
        �s = 1
        for i in range (1, len (self.katsay�lar)):
            t�revliKatsay�lar.append (self.katsay�lar [i] * �s)
            �s += 1
        return Polinom (*t�revliKatsay�lar [::-1])


if __name__ == "__main__":
    p = Polinom (1, 0, -4, 3, 0) # x^4 - 4x^2 + 3x
    print (p) # p i�in: __str__ �a�r�l�r...

    print ("\nx=[-3,4] aras� p(x) de�erleri:\nx, p(x) =")
    for x in range (-3, 5): print (x, p(x) ) # p(x) i�in: __call__ �a�r�l�r...

    import numpy as np
    import matplotlib.pyplot as mp
    mp.style.use ("dark_background")
    X = np.linspace (-3, 4, 100, endpoint=True)
    F = p (X)
    mp.plot (X, F)
    mp.show()


"""��kt�:
>python p_21002.py
Polinom (1, 0, -4, 3, 0)

x=[-3,4] aras� p(x) de�erleri:
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