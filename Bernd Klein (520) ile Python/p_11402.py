# coding:iso-8859-9 T�rk�e
# p_11402.py: if-elif ile k�pek ve insan ya�lar�n�n kar��la�t�r�lmas� �rne�i.

from random import randint

try: ya� = abs (int (eval (input ("K�pe�inizin ya�� ka�? "))))
except: ya� = randint (0, 15)

print()
if ya� < 1: print ("Bir y�ldan k���k k�pek ya��, yakla��k 5 insan ya��na e�de�erdir")
elif ya� == 1: print ("1 k�pek ya�� yakla��k 14 insan ya��na e�de�erdir")
elif ya� == 2:print ("2 k�pek ya�� yakla��k 22 insan ya��na e�de�erdir")
elif ya� > 2: print (ya�, "k�pek ya�� yakla��k", 22+(ya�-2)*5, "insan ya��na e�de�erdir")


"""��kt�:
>python p_11402.py
K�pe�inizin ya�� ka�?

6 k�pek ya�� yakla��k 42 insan ya��na e�de�erdir

>python p_11402.py  ** TEKRAR **
K�pe�inizin ya�� ka�? 15

15 k�pek ya�� yakla��k 87 insan ya��na e�de�erdir
"""