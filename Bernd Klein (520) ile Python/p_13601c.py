# coding:iso-8859-9 Türkçe
# p_13601c.py: name-main olmayan ve olan modül ve fonksiyonların import'u örneği.

import p_13601a

# __name__ == "__main__" kontrolsuz import (ana programı işletir)...

print (p_13601a.fib (-1) )
print (p_13601a.fib (0) )

try: print (p_13601a.fib (0.5) )
except TypeError as ist: print (ist)

print (p_13601a.fib (10) )
print (p_13601a.fib (55) )


print (p_13601a.fibliste (-8) )
print (p_13601a.fibliste (0) )
print (p_13601a.fibliste (10) )
print ("-"*75, "\n", sep="")
#----------------------------------------------------------------------------------------------------

import p_13601b
# __name__ == "__main__" kontrollu import (ana programı işletemez)...

print (p_13601b.fib (5) )
print (p_13601b.fibliste (5) )

"""Çıktı:
>python p_13601c.py
fib fonksiyonu testi başarılıdır!
0
0
'float' object cannot be interpreted as an integer
55
139583862445
[0, 1]
[0, 1]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
---------------------------------------------------------------------------

5
[0, 1, 1, 2, 3, 5]
"""