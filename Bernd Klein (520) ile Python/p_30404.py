# coding:iso-8859-9 Türkçe
# p_30404.py: 2 matrisin numpy.dot ile vektörel/yönel çarpım uygunluğu örneği.

import numpy as np

print ("'np.dot(3,4)' 2 skalar sayınının çarpımı:", np.dot (3, 4))

#x = np.array ([3])
#y = np.array ([4])
print ("'np.dot([3],[4])' 2 vektörel sayının çarpımı:", np.dot ([3], [4]) )

#x = np.array ([3, -2])
#y = np.array ([-4, 1])
print ("'np.dot([3,-2],[-4,1])' 2 vektörel listenin çarpımı:", np.dot ([3, -2], [-4, 1]) )

x = np.array ([3, -2, 0, 10])
y = np.array ([-4, 1, 90000, 2])
print ("'np.dot([3,-2,0,10],[-4,1,90000,2])' 2 vektörel listenin çarpımı:", np.dot (x, y) )
print ("Dizi boyutu:", x.ndim)
print ("-"*70)
#---------------------------------------------------------------------------------------------------

A = np.array ([
    [1, 2, 3],
    [4, 5, 6] ]) # A(2,3)

B = np.array ([
    [2, 3, 4, -2],
    [1, -1, 2, 3],
    [1, 2, 3, 0] ]) # B(3,4)

# Matris çarpımı için ilkinin kolon sayısı ikincinin satır sayısına eşit olmalıdır...
print ("\nA matrisi:\n", A, sep="")
print ("B matrisi:\n", B, sep="")
print ("A.shape:", A.shape, " ve B.shape:", B.shape)
cevap = (A.shape[-1] == B.shape[0])
print ("İki matris çarpıma uygun mu?", cevap) 
if cevap: print ("\n'A(2,3)*B(3,4)=C(2,4)' matris çarpımı:\n", np.dot (A, B), sep="")



"""Çıktı:
>python p_30404.py
'np.dot(3,4)' 2 skalar sayınının çarpımı: 12
'np.dot([3],[4])' 2 vektörel sayının çarpımı: 12
'np.dot([3,-2],[-4,1])' 2 vektörel listenin çarpımı: -14
'np.dot([3,-2,0,10],[-4,1,90000,2])' 2 vektörel listenin çarpımı: 6
Dizi boyutu: 1
----------------------------------------------------------------------

A matrisi:
[[1 2 3]
 [4 5 6]]
B matrisi:
[[ 2  3  4 -2]
 [ 1 -1  2  3]
 [ 1  2  3  0]]
A.shape: (2, 3)  ve B.shape: (3, 4)
İki matris çarpıma uygun mu? True

'A(2,3)*B(3,4)=C(2,4)' matris çarpımı:
[[ 7  7 17  4]
 [19 19 44  7]]
"""