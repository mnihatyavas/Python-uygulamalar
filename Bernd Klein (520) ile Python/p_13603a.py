# coding:iso-8859-9 T�rk�e
# p_13603a.py: unittest.main()'le 3 fib fonksiyonun verili sonu�larla testi �rne�i.

import unittest

from p_13603x import fib1, fib2, fib3

class FibonakiyiDene (unittest.TestCase):
    def testDenemeleri1 (self):
        self.assertEqual (fib1 (0), 0)
        self.assertEqual (fib1 (1), 1)
        self.assertEqual (fib1 (5), 5)
        self.assertEqual (fib1 (10), 55)
        self.assertEqual (fib1 (20), 6765)

    def testDenemeleri2 (self):
        self.assertEqual (fib2 (0), 0)
        self.assertEqual (fib2 (1), 1)
        self.assertEqual (fib2 (5), 5)
        self.assertEqual (fib2 (10), 55)
        self.assertEqual (fib2 (20), 6765)

    def testDenemeleri3 (self):
        self.assertEqual (fib3 (0), 0)
        self.assertEqual (fib3 (1), 1)
        self.assertEqual (fib3 (5), 5)
        self.assertEqual (fib3 (10), 55)
        self.assertEqual (fib3 (20), 6765)

if __name__ == "__main__": 
    unittest.main()


"""��kt�:
>python p_13603a.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.003s

OK
"""