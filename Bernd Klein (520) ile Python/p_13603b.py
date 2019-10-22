# coding:iso-8859-9 Türkçe
# p_13603b.py: unittest.main()'le verili setUp değerleriyle fib fonksiyonu ve sonucunu test örneği.

import unittest
from p_13603x import fib1

class FibonakiyiDene (unittest.TestCase):
    def setUp (self):
        self.fib1_elemanları = ( (0,0), (1,1), (2,1), (3,2), (4,3), (5,5), (10,55), (20,6765) )
        print ("setUp işletildi!")

    def tearDown (self):
        self.fib1_elemanları = None
        print ("tearDown işletildi!")

    def testEt (self):
        for (n, sonuç) in self.fib1_elemanları:
            self.assertEqual (fib1 (n), sonuç)


if __name__ == "__main__": 
    unittest.main()

"""Çıktı:
>python p_13603b.py
setUp işletildi!
tearDown işletildi!
.
----------------------------------------------------------------------
Ran 1 test in 0.003s

OK
"""