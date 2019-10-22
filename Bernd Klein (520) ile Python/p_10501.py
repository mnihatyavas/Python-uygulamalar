# coding:iso-8859-9 T�rk�e
# p_10501.py: Veri tipleri, de�i�ken adlar�, haz�r anahtarkelimeler ve etkile�im kabu�u �rne�i.

x = 42
print ("x de�i�keni tamsay�d�r:", x)

x = 42.85
print ("x de�i�keni �imdi kayan noktad�r:", x)

x = "42.Cadde"
print ("x de�i�keni �imdi dizgedir:", x)

x = True
print ("x de�i�keni �imdi boolean'd�r:", x)

y = x = 42
print ("\nx={}, y={}; id(x)={}, id(y)={}" .format (x, y, id (x), id (y)) )

y = 43
print ("x={}, y={}; id(x)={}, id(y)={}" .format (x, y, id (x), id (y)) )

a = 1
A = 2
_a = 3
__a = 4
__a_ = 5
��25 = 6
a_aA5 = 7
print ("\nGe�erli de�i�ken adlar�: a={}, A={}, _a={}, __a={}, __a_={}, ��25={}, a_aA5={}"\
    .format (a, A, _a, __a, __a_, ��25, a_aA5) )

python_anahtar_kelimeleri = """\
   and, as, assert, break, class, continue, def, del, elif, else,
    except, False, finally, for, from, global, if, import, in, is, 
    lambda, None, nonlocal, not, or, pass, raise, return, True, try, 
    while, with, yield
"""
print ("\nPyton anahtar kelimeleri:\n", python_anahtar_kelimeleri)

print ("'>python' ile etkile�im iletisine '>>>' ge�ilir; 'exit()' ile ��k�l�r.\n",
    ">>>'help()' ile yard�m istenir; 'quit' ile ��k�l�r.", sep="")


"""��kt�:
>python p_10501.py
x de�i�keni tamsay�d�r: 42
x de�i�keni �imdi kayan noktad�r: 42.85
x de�i�keni �imdi dizgedir: 42.Cadde
x de�i�keni �imdi boolean'd�r: True

x=42, y=42; id(x)=1542077328, id(y)=1542077328
x=42, y=43; id(x)=1542077328, id(y)=1542077344

Ge�erli de�i�ken adlar�: a=1, A=2, _a=3, __a=4, __a_=5, ��25=6, a_aA5=7

Pyton anahtar kelimeleri:
    and, as, assert, break, class, continue, def, del, elif, else,
    except, False, finally, for, from, global, if, import, in, is,
    lambda, None, nonlocal, not, or, pass, raise, return, True, try,
    while, with, yield

'>python' ile etkile�im iletisine '>>>' ge�ilir; 'exit()' ile ��k�l�r.
>>>'help()' ile yard�m istenir; 'quit' ile ��k�l�r.

"""