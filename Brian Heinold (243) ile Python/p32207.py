# coding:iso-8859-9 Türkçe

from pprint import pprint

L = [[0]*10 for j in range (20)]
pprint (L)

"""
L = [[0]*100 for j in range (200)]
pprint (L)

L = [[0]*200 for j in range (250)]
pprint (L)

L = [[0]*10000000 for j in range (20000000)]
pprint (L)
"""

print()
L = []
print ("Liste =", L)

print()
S = {(10, 12): 47, (100, 245): 18, (10000000, 20000000): 25}
print ("Sözlük =", S)
print ("\nS(10,12) =", S[10,12], "\nS(100,245) =", S[100,245],
    "\nS(10000000,20000000) =", S[10000000,20000000],
    "\nTüm diğer sözlük endeks değerleri = 0")

# pip -m install NumPy/NumberPython ve SciPy/SciencePython modülleri
