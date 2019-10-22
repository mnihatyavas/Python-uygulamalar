# coding:iso-8859-9 T�rk�e
# p_12902.py: ��i�e klas�rlerdeki mod�l-i�i fonksiyonlar� __init__.py vas�tas�yla do�rudan �a��rma �rne�i.

from paketim import *

print ("\n ==>paketim.paketim1.mod�l1A fonksiyonlar� �a�r�l�yor:")
fonk11a()
fonk12a()
print (" ==>paketim.paketim1.mod�l1B fonksiyonlar� �a�r�l�yor:")
fonk11b()
fonk12b()

print ("\n ==>paketim.paketim2.mod�l2A fonksiyonlar� �a�r�l�yor:")
fonk21a()
fonk22a()
print (" ==>paketim.paketim2.mod�l2B fonksiyonlar� �a�r�l�yor:")
fonk21b()
fonk22b()

print ("\n ==>paketim.paketim3.mod�l3A fonksiyonlar� �a�r�l�yor:")
fonk31a()
fonk32a()
print (" ==>paketim.paketim3.mod�l3 fonksiyonlar� �a�r�l�yor:")
fonk31b()
fonk32b()

"""��kt�:
>python p_12902.py
paketim klas�r�nden mod�lA.py �a�r�l�yor...
paketim klas�r�nden mod�lB.py �a�r�l�yor...

 ==>paketim.paketim1.mod�l1A fonksiyonlar� �a�r�l�yor:
paketim.paketim1 klas�r� mod�l1A.py mod�l�nden fonk11a() fonksiyonuyum....
paketim.paketim1 klas�r� mod�l1A.py mod�l�nden fonk12a() fonksiyonuyum....
 ==>paketim.paketim1.mod�l1B fonksiyonlar� �a�r�l�yor:
paketim.paketim1 klas�r� mod�l1B.py mod�l�nden fonk11b() fonksiyonuyum....
paketim.paketim1 klas�r� mod�l1B.py mod�l�nden fonk12b() fonksiyonuyum....

 ==>paketim.paketim2.mod�l2A fonksiyonlar� �a�r�l�yor:
paketim.paketim2 klas�r� mod�l2A.py mod�l�nden fonk21a() fonksiyonuyum....
paketim.paketim2 klas�r� mod�l2A.py mod�l�nden fonk22a() fonksiyonuyum....
 ==>paketim.paketim2.mod�l2B fonksiyonlar� �a�r�l�yor:
paketim.paketim2 klas�r� mod�l2B.py mod�l�nden fonk21b() fonksiyonuyum....
paketim.paketim2 klas�r� mod�l2B.py mod�l�nden fonk22b() fonksiyonuyum....

 ==>paketim.paketim3.mod�l3A fonksiyonlar� �a�r�l�yor:
paketim.paketim3 klas�r� mod�l3A.py mod�l�nden fonk31a() fonksiyonuyum....
paketim.paketim3 klas�r� mod�l3A.py mod�l�nden fonk32a() fonksiyonuyum....
 ==>paketim.paketim3.mod�l3 fonksiyonlar� �a�r�l�yor:
paketim.paketim3 klas�r� mod�l3B.py mod�l�nden fonk31b() fonksiyonuyum....
paketim.paketim3 klas�r� mod�l3B.py mod�l�nden fonk32b() fonksiyonuyum....
"""

"""Not: paketim __init__.py i�eri�ine son eklenenler:
# coding:iso-8859-9 T�rk�e

from paketim.paketim1.mod�l1A import *
from paketim.paketim1.mod�l1B import *

from paketim.paketim2.mod�l2A import *
from paketim.paketim2.mod�l2B import *

from paketim.paketim3.mod�l3A import *
from paketim.paketim3.mod�l3B import *
"""

"""Tam paket �emas�:
paketim
    __init__.py
    mod�lA.py
        fonkA1()
        fonkA2()
    mod�lB.py
        fonkB1()
        fonkB2()
    paketim1
        mod�l1A.py
            fonk11a()
            fonk12a()
        mod�l1B.py
            fonk11b()
            fonk12b()
    paketim2
        mod�l2A.py
            fonk21a()
            fonk22a()
        mod�l2B.py
            fonk21b()
            fonk22b()
    paketim3
        mod�l3A.py
            fonk31a()
            fonk32a()
        mod�l3B.py
            fonk31b()
            fonk32b()
"""