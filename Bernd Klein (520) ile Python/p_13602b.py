# coding:iso-8859-9
# p_13602b.py: doctest.testmod()'la işlevsiz return'lü fonksiyon testi örneği.

import doctest

def fib1 (n):
    """ 
    n.inci fibonaki sayısını bulur...
    >>> fib1(0)
    0
    >>> fib1(1)
    1
    >>> fib1(5)
    5
    >>> fib1(10) 
    55
    >>> fib1(15)
    610
    >>> 
    """
    #a, b = 0, 1
    #for i in range (n): a, b = b, a + b
    return 0


if __name__ == "__main__": 
    doctest.testmod()

"""Test
>python p_13603.py
**********************************************************************
File "p_13602b.py", line 10, in __main__.fib1
Failed example:
    fib1(1)
Expected:
    1
Got:
    0
**********************************************************************
File "p_13603.py", line 12, in __main__.fib1
Failed example:
    fib1(5)
Expected:
    5
Got:
    0
**********************************************************************
File "p_13603.py", line 14, in __main__.fib1
Failed example:
    fib1(10)
Expected:
    55
Got:
    0
**********************************************************************
File "p_13603.py", line 16, in __main__.fib1
Failed example:
    fib1(15)
Expected:
    610
Got:
    0
**********************************************************************
1 items had failures:
   4 of   5 in __main__.fib1
***Test Failed*** 4 failures.
"""