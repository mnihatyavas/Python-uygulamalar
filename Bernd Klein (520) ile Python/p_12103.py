# coding:iso-8859-9 Türkçe
# p_12103.py: Fibonaki sınıflı cağrılabilir bellekli fibonaki ve lukas sayıları dökümü örneği.

from random import randint

class Fibonaki:
    def __init__ (self, i1=0, i2=1):
        self.bellek = {0:i1, 1:i2}

    def __call__ (self, n):
        if n not in self.bellek: self.bellek [n] = self.__call__ (n-1) + self.__call__ (n-2)  
        return self.bellek [n]

fibonaki = Fibonaki()
lukas = Fibonaki (2, 1)

sayı = randint (0, 20)
print (sayı, "sayısının callable/çağrılabilir sınıf Fibonaki ve Lukas serileri (alt-alta):")
for i in range(0, sayı+1): print (i, ": ", fibonaki (i), " - ", lukas (i), sep="")


"""Çıktı:
>python p_12103.py
12 sayısının callable/çağrılabilir sınıf Fibonaki ve Lukas serileri (alt-alta):
0: 0 - 2
1: 1 - 1
2: 1 - 3
3: 2 - 4
4: 3 - 7
5: 5 - 11
6: 8 - 18
7: 13 - 29
8: 21 - 47
9: 34 - 76
10: 55 - 123
11: 89 - 199
12: 144 - 322
"""