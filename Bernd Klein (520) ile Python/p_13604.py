# coding:iso-8859-9
# p_13604.py: doctest.testmod()'la hızlı ve özyinelemeli yavaş fib fonksiyonları testi örneği.

import doctest

def fib1 (n):
    """ 
    n.inci fibonaki sayısını hızlı bulur...
    >>> fib1(0)
    0
    >>> fib1(1)
    1
    >>> fib1(5)
    6
    >>> fib1(10)
    55
    >>> fib1(15)
    610
    >>> fib1 (20)
    6765
    >>> fib1 (40)
    102334155
    """
    a, b = 0, 1
    for i in range (n): a, b = b, a + b
    return a

def fib2 (n):
    """
    n.inci fibonaki sayısını çok yavaş bulur...
    >>> fib2 (0)
    0
    >>> fib2 (1)
    1
    >>> fib2 (5) 
    5
    >>> fib2 (10)
    56
    >>> fib2 (15)
    610
    >>> fib2 (20)
    6765
    """
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib2 (n-1) + fib2 (n-2)

if __name__ == "__main__": 
    doctest.testmod()

"""Çıktı:
>python p_13604.py
**********************************************************************
File "p_13604.py", line 12, in __main__.fib1
Failed example:
    fib1(5)
Expected:
    6
Got:
    5
**********************************************************************
File "p_13604.py", line 36, in __main__.fib2
Failed example:
    fib2 (10)
Expected:
    56
Got:
    55
**********************************************************************
2 items had failures:
   1 of   7 in __main__.fib1
   1 of   6 in __main__.fib2
***Test Failed*** 2 failures.
"""