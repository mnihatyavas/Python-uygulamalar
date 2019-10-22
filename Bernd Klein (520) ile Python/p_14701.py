# coding:iso-8859-9 T�rk�e
# p_14701.py: Arg�man� normal ve meta s�n�f olan s�n�f nesnesi �rne�i.

class MetaS�n�f (type): # "class MetaS�n�f (object)" de�il!..
    def __new__ (s�n�f, s�n�fAd�, s�perS�n�flar, �zellikS�zl���):
        print ("S�n�f ad�: ", s�n�fAd�)
        print ("S�per s�n�flar: ", s�perS�n�flar)
        print ("�zellikler s�zl���: ", �zellikS�zl���)
        return type.__new__ (s�n�f, s�n�fAd�, s�perS�n�flar, �zellikS�zl���)

class S: pass

class A (S, metaclass=MetaS�n�f): pass

a = A()



"""��kt�:
>python p_14701.py
S�n�f ad�:  A
S�per s�n�flar:  (<class '__main__.S'>,)
�zellikler s�zl���:  {'__module__': '__main__', '__qualname__': 'A'}
"""