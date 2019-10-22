# coding:iso-8859-9
# p_13701.py: Çeşitli sınıf nesneleri tipi (int, float, str, function, module, list, tuple, dict, class) örneği.

nesne1 = 42
nesne2 = 4.34
nesne3 = "M.Nihat Yavaş"
def fonk (x): return x + 1
nesne4 = fonk
nesne5 = fonk (8)
import math
nesne6 = math
nesne7 = [3, 6, 9]
nesne8 = (45, "abc")
nesne9 = {"ad":"nihat", "soyad":"yavaş", "yaş":62}
class Sınıf: pass
nesne10 = Sınıf()

print (nesne1, type (nesne1) )
print (nesne2, type (nesne2) )
print (nesne3, type (nesne3) )
print (nesne4, type (nesne4) )
print (nesne5, type (nesne5) )
print (nesne6, type (nesne6) )
print (nesne7, type (nesne7) )
print (nesne8, type (nesne8) )
print (nesne9, type (nesne9) )
print (nesne10, type (nesne10) )

"""Çıktı:
>python p_13701.py
42 <class 'int'>
4.34 <class 'float'>
M.Nihat Yavaş <class 'str'>
<function fonk at 0x006698A0> <class 'function'>
9 <class 'int'>
<module 'math' (built-in)> <class 'module'>
[3, 6, 9] <class 'list'>
(45, 'abc') <class 'tuple'>
{'ad': 'nihat', 'soyad': 'yavaş', 'yaş': 62} <class 'dict'>
<__main__.Sınıf object at 0x00AF1C30> <class '__main__.Sınıf'>
"""