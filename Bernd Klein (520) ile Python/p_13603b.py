# coding:iso-8859-9 T�rk�e
# p_13603b.py: unittest.main()'le verili setUp de�erleriyle fib fonksiyonu ve sonucunu test �rne�i.

import unittest
from p_13603x import fib1

class FibonakiyiDene (unittest.TestCase):
    def setUp (self):
        self.fib1_elemanlar� = ( (0,0), (1,1), (2,1), (3,2), (4,3), (5,5), (10,55), (20,6765) )
        print ("setUp i�letildi!")

    def tearDown (self):
        self.fib1_elemanlar� = None
        print ("tearDown i�letildi!")

    def testEt (self):
        for (n, sonu�) in self.fib1_elemanlar�:
            self.assertEqual (fib1 (n), sonu�)


if __name__ == "__main__": 
    unittest.main()

"""��kt�:
>python p_13603b.py
setUp i�letildi!
tearDown i�letildi!
.
----------------------------------------------------------------------
Ran 1 test in 0.003s

OK
"""