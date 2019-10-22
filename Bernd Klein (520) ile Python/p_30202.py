# coding:iso-8859-9 Türkçe
# p_30202.py: numpy.linspace ile numpy.arange benzeri ardışık değerler üretme örneği.

import numpy as np

print (type (np.linspace (1, 50)) )
print (np.linspace (1, 50) ) # [1->50] arasında ((50-1)/49=1) varsayılı 50 değer...
print (np.linspace (1, 10) ) # [1->10] arasında ((10-1)/49=1.18367347) varsayılı 50 değer...
print (np.linspace (1, 10, 7) ) # [1->10] arasında ((10-1)/6=1.5) 7 değer...
print (np.linspace (1, 10, 7, endpoint=False) ) # [1->10) arasında ((10-1)/7=1.28571429) 7 değer...
#---------------------------------------------------------------------------------------------

diziElemanları, aralık = np.linspace (1, 50, retstep=True) # Varsayılı retstep=False'dır...
print ("\n[1->50] arası varsayılı 50 değer aralığı:", aralık)

diziElemanları, aralık = np.linspace (1, 10, retstep=True)
print ("[1->10] arası varsayılı 50 değer aralığı:", aralık)

diziElemanları, aralık = np.linspace (1, 10, 7, endpoint=True, retstep=True)
print ("[1->10] arası varsayılı 7 değer aralığı:", aralık)

diziElemanları, aralık = np.linspace (1, 10, 7, endpoint=False, retstep=True)
print ("[1->10) arası varsayılı 7 değer aralığı:", aralık)



"""Çıktı:
>python p_30202.py
<class 'numpy.ndarray'>
[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15. 16. 17. 18.
 19. 20. 21. 22. 23. 24. 25. 26. 27. 28. 29. 30. 31. 32. 33. 34. 35. 36.
 37. 38. 39. 40. 41. 42. 43. 44. 45. 46. 47. 48. 49. 50.]
[ 1.          1.18367347  1.36734694  1.55102041  1.73469388  1.91836735
  2.10204082  2.28571429  2.46938776  2.65306122  2.83673469  3.02040816
  3.20408163  3.3877551   3.57142857  3.75510204  3.93877551  4.12244898
  4.30612245  4.48979592  4.67346939  4.85714286  5.04081633  5.2244898
  5.40816327  5.59183673  5.7755102   5.95918367  6.14285714  6.32653061
  6.51020408  6.69387755  6.87755102  7.06122449  7.24489796  7.42857143
  7.6122449   7.79591837  7.97959184  8.16326531  8.34693878  8.53061224
  8.71428571  8.89795918  9.08163265  9.26530612  9.44897959  9.63265306
  9.81632653 10.        ]
[ 1.   2.5  4.   5.5  7.   8.5 10. ]
[1.         2.28571429 3.57142857 4.85714286 6.14285714 7.42857143
 8.71428571]

[1->50] arası varsayılı 50 değer aralığı: 1.0
[1->10] arası varsayılı 50 değer aralığı: 0.1836734693877551
[1->10] arası varsayılı 7 değer aralığı: 1.5
[1->10) arası varsayılı 7 değer aralığı: 1.2857142857142858
"""