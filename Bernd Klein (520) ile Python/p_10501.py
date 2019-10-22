# coding:iso-8859-9 Türkçe
# p_10501.py: Veri tipleri, değişken adları, hazır anahtarkelimeler ve etkileşim kabuğu örneği.

x = 42
print ("x değişkeni tamsayıdır:", x)

x = 42.85
print ("x değişkeni şimdi kayan noktadır:", x)

x = "42.Cadde"
print ("x değişkeni şimdi dizgedir:", x)

x = True
print ("x değişkeni şimdi boolean'dır:", x)

y = x = 42
print ("\nx={}, y={}; id(x)={}, id(y)={}" .format (x, y, id (x), id (y)) )

y = 43
print ("x={}, y={}; id(x)={}, id(y)={}" .format (x, y, id (x), id (y)) )

a = 1
A = 2
_a = 3
__a = 4
__a_ = 5
ğç25 = 6
a_aA5 = 7
print ("\nGeçerli değişken adları: a={}, A={}, _a={}, __a={}, __a_={}, ğç25={}, a_aA5={}"\
    .format (a, A, _a, __a, __a_, ğç25, a_aA5) )

python_anahtar_kelimeleri = """\
   and, as, assert, break, class, continue, def, del, elif, else,
    except, False, finally, for, from, global, if, import, in, is, 
    lambda, None, nonlocal, not, or, pass, raise, return, True, try, 
    while, with, yield
"""
print ("\nPyton anahtar kelimeleri:\n", python_anahtar_kelimeleri)

print ("'>python' ile etkileşim iletisine '>>>' geçilir; 'exit()' ile çıkılır.\n",
    ">>>'help()' ile yardım istenir; 'quit' ile çıkılır.", sep="")


"""Çıktı:
>python p_10501.py
x değişkeni tamsayıdır: 42
x değişkeni şimdi kayan noktadır: 42.85
x değişkeni şimdi dizgedir: 42.Cadde
x değişkeni şimdi boolean'dır: True

x=42, y=42; id(x)=1542077328, id(y)=1542077328
x=42, y=43; id(x)=1542077328, id(y)=1542077344

Geçerli değişken adları: a=1, A=2, _a=3, __a=4, __a_=5, ğç25=6, a_aA5=7

Pyton anahtar kelimeleri:
    and, as, assert, break, class, continue, def, del, elif, else,
    except, False, finally, for, from, global, if, import, in, is,
    lambda, None, nonlocal, not, or, pass, raise, return, True, try,
    while, with, yield

'>python' ile etkileşim iletisine '>>>' geçilir; 'exit()' ile çıkılır.
>>>'help()' ile yardım istenir; 'quit' ile çıkılır.

"""