# coding:iso-8859-9 T�rk�e
# p_30401.py: Python listesi ve numpy.array ile toplama ��karma �arpma b�lme ve �s �rne�i.

import numpy as np

liste = [2, 3, 7.9, 3.3, 6.9, 0.11, 10.3, 12.9]
print ("Liste:", liste)
print ("Toplama [de�er+2 for de�er in liste]:", [de�er + 2 for de�er in liste])
print ("��karma [de�er-1.38 for de�er in liste]:", [de�er - 1.38 for de�er in liste])
print ("�arpma [de�er*2.2 for de�er in liste]:", [de�er * 2.2 for de�er in liste])
print ("B�lme [de�er/2.69 for de�er in liste]:", [de�er / 2.69 for de�er in liste])
print ("�s [de�er**2.37 for de�er in liste]:", [de�er ** 2.37 for de�er in liste])

dizi = np.array (liste)
print ("\nDizi (dizi=np.array(liste):", dizi)
print ("Toplama (dizi+2):", (dizi + 2) )
print ("��karma (dizi-1.38):", (dizi - 1.38) )
print ("�arpma (dizi*2.2):", (dizi * 2.2) )
print ("B�lme (dizi/2.69):", (dizi / 2.69) )
print ("�s (dizi**2.37):", (dizi ** 2.37) )



"""��kt�:
>python p_30401.py
Liste: [2, 3, 7.9, 3.3, 6.9, 0.11, 10.3, 12.9]
Toplama [de�er+2 for de�er in liste]: [4, 5, 9.9, 5.3, 8.9, 2.11, 12.3, 14.9]
��karma [de�er-1.38 for de�er in liste]: [0.6200000000000001, 1.62, 6.5200000000000005, 1.92, 5.5200000000000005, -1.2699999999999998, 8.920000000000002, 11.52]
�arpma [de�er*2.2 for de�er in liste]: [4.4, 6.6000000000000005, 17.380000000000003, 7.26, 15.180000000000001, 0.24200000000000002, 22.660000000000004, 28.380000000000003]
B�lme [de�er/2.69 for de�er in liste]: [0.7434944237918216, 1.1152416356877324, 2.9368029739776955, 1.2267657992565055, 2.5650557620817844, 0.040892193308550186, 3.8289962825278816, 4.795539033457249]
�s [de�er**2.37 for de�er in liste]: [5.169411322549969, 13.513796467360295, 134.08376813230757, 16.93862048045867, 97.29092781170381, 0.005346882788392535, 251.43412623384276, 428.6448531516967]

Dizi (dizi=np.array(liste): [ 2.    3.    7.9   3.3   6.9   0.11 10.3  12.9 ]
Toplama (dizi+2): [ 4.    5.    9.9   5.3   8.9   2.11 12.3  14.9 ]
��karma (dizi-1.38): [ 0.62  1.62  6.52  1.92  5.52 -1.27  8.92 11.52]
�arpma (dizi*2.2): [ 4.4    6.6   17.38   7.26  15.18   0.242 22.66  28.38 ]
B�lme (dizi/2.69): [0.74349442 1.11524164 2.93680297 1.2267658  2.56505576 0.04089219 3.82899628 4.79553903]
�s (dizi**2.37): [5.16941132e+00 1.35137965e+01 1.34083768e+02 1.69386205e+01 9.72909278e+01 5.34688279e-03 2.51434126e+02 4.28644853e+02]
"""