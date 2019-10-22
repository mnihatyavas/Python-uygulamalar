# coding:iso-8859-9 T�rk�e
# p_13403.py: yield-next fonksiyonda raise veya return istisna y�netimi �rne�i.

def �rete�1():
    yield 1
    yield 2
    yield 3
    raise StopIteration (42) # return, return 42, raise, raise 42
    yield 4
    yield 5

�r�n = �rete�1()

print ("raise'li �rete� elementleri:")

try:
    print ("-->�r�n:", next (�r�n) )
    print ("-->�r�n:", next (�r�n) )
    print ("-->�r�n:", next (�r�n) )
    print ("-->�r�n:", next (�r�n) )
    print ("-->�r�n:", next (�r�n) )
    print ("-->�r�n:", next (�r�n) )
except Exception as ist: print ("HATA:", ist, "(yield sonu veya raise/return'e rastlan�ld�...)")
#---------------------------------------------------------------------------------------------

def �rete�2():
    yield 1
    yield 2
    yield 3
    raise #return 42
    yield 4
    yield 5

�r�n = �rete�2()

print ("\nreturn'l� �rete� elementleri:")

try:
    print ("-->�r�n:", next (�r�n) )
    print ("-->�r�n:", next (�r�n) )
    print ("-->�r�n:", next (�r�n) )
    print ("-->�r�n:", next (�r�n) )
    print ("-->�r�n:", next (�r�n) )
    print ("-->�r�n:", next (�r�n) )
except: print ("HATA: yield sonu veya raise/return'e rastlan�ld�...")

"""��kt�:
>python p_13403.py
raise'li �rete� elementleri:
-->�r�n: 1
-->�r�n: 2
-->�r�n: 3
HATA: generator raised StopIteration (yield sonu veya raise/return'e rastlan�ld�...)

return'l� �rete� elementleri:
-->�r�n: 1
-->�r�n: 2
-->�r�n: 3
HATA: yield sonu veya raise/return'e rastlan�ld�...
"""