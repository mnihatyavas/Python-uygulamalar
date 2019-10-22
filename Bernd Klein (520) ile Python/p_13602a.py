# coding:iso-8859-9
# p_13602a.py: doctest.testmod()'la fonksiyonların verili ve gerçek sonuçlarının testi örneği.

import doctest

def fib1 (n):
    """ 
    n.inci fibonaki sayısını bulur...
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
    >>> 
    """
    a, b = 0, 1
    for i in range (n): a, b = b, a + b
    return a

def fib2 (n):
    """ 
    n.inci fibonaki sayısını bulur...
    >>> fib2(0)
    0
    >>> fib2(1)
    1
    >>> fib2(5)
    5
    >>> fib2(10) 
    55
    >>> fib2(15)
    610
    >>> 
    """
    a, b = 1, 1
    for i in range (n): a, b = b, a + b
    return a


if __name__ == "__main__": 
    doctest.testmod()

"""Test
>python p_13602a.py
**********************************************************************
File "p_13602.py", line 12, in __main__.fib1
Failed example:
    fib1(5)
Expected:
    6
Got:
    5
**********************************************************************
File "p_13602.py", line 27, in __main__.fib2
Failed example:
    fib2(0)
Expected:
    0
Got:
    1
**********************************************************************
File "p_13602.py", line 31, in __main__.fib2
Failed example:
    fib2(5)
Expected:
    5
Got:
    8
**********************************************************************
File "p_13602.py", line 33, in __main__.fib2
Failed example:
    fib2(10)
Expected:
    55
Got:
    89
**********************************************************************
File "p_13602.py", line 35, in __main__.fib2
Failed example:
    fib2(15)
Expected:
    610
Got:
    987
**********************************************************************
2 items had failures:
   1 of   5 in __main__.fib1
   4 of   5 in __main__.fib2
***Test Failed*** 5 failures.
"""