# coding:iso-8859-9 T�rk�e
# p_12509.py: De�i�ken liste ve s�zl�k arg�manl� callable s�n�f fonksiyonu �rne�i.

class A:
    def __init__ (self): print ("Bir s�n�f A nesne tiplemesi ba�lat�lmaktad�r")
    def __call__ (self, *a, **b): print ("G�nderilen de�i�ken adetli t�ple ve s�zl�k arg�manlar�:", a, b)

print ("Fonksiyon arg�manl� callable/�a�r�labilir dekorat�r fonksiyon nesneleri oldu�u gibi, __call__ metodlu �a�r�labilir s�n�f nesnesi tiplemesi de olabilmektedir.")
s�n�fA = A()
print ("\n�imdi s�n�f A nesne tiplemesi �a�r�l�yor==>")
s�n�fA (3, 4, x=11, y=10)

print ("\nAyn� �ekilde tekrar �a��r�yoruz==>")
s�n�fA (3, 4, 5, 6, x=11, y=10, z=9)
print ("-"*75, "\n")
#-----------------------------------------------------------------------------------------------------

class Fibonaki:
    def __init__ (self): self.cepbellek = {}
    def __call__ (self, n):
        if n not in self.cepbellek:
            if n == 0: self.cepbellek[0] = 0
            elif n == 1: self.cepbellek[1] = 1
            else: self.cepbellek[n] = self.__call__ (n-1) + self.__call__ (n-2)
        return self.cepbellek[n]

fib = Fibonaki()
from random import randint
say� = randint (0, 100)
print (say�, "adet fibonaki seri a��l�m�: ", end="")
for i in range (say�): print (fib (i), end=", ")


"""��kt�:
>python p_12509.py
Fonksiyon arg�manl� callable/�a�r�labilir dekorat�r fonksiyon nesneleri oldu�u
gibi, __call__ metodlu �a�r�labilir s�n�f nesnesi tiplemesi de olabilmektedir.
Bir s�n�f A nesne tiplemesi ba�lat�lmaktad�r

�imdi s�n�f A nesne tiplemesi �a�r�l�yor==>
G�nderilen de�i�ken adetli t�ple ve s�zl�k arg�manlar�: (3, 4) {'x': 11, 'y': 10}

Ayn� �ekilde tekrar �a��r�yoruz==>
G�nderilen de�i�ken adetli t�ple ve s�zl�k arg�manlar�: (3, 4, 5, 6) {'x': 11, 'y': 10, 'z': 9}
---------------------------------------------------------------------------

84 adet fibonaki seri a��l�m�: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811,
514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733,
1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025,
20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717,
365435296162, 591286729879, 956722026041, 1548008755920, 2504730781961,
 4052739537881, 6557470319842, 10610209857723, 17167680177565, 27777890035288,
44945570212853, 72723460248141, 117669030460994, 190392490709135, 308061521170129,
498454011879264, 806515533049393, 1304969544928657, 2111485077978050,
3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221,
23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497,
"""