# coding:iso-8859-9 T�rk�e
# p_12901.py: ��i�e klas�rlerdeki py mod�llerini __init__.py vas�tas�yla �a��rma �rne�i.

# paketim klas�r�nde bo� __init__.py yeterli...
from paketim import mod�lA, mod�lB

print()
mod�lA.fonkA1()
mod�lA.fonkA2()

print()
mod�lB.fonkB1()
mod�lB.fonkB2()
print ("-"*70)
#--------------------------------------------------------------------------------------------------
"""
paketim klas�r�ndeki __init__.py i�ine
import paketim.mod�lA
import paketim.mod�lB
dahil edilince
"""
import paketim
print()
paketim.mod�lA.fonkA1()
paketim.mod�lA.fonkA2()

print()
paketim.mod�lB.fonkB1()
paketim.mod�lB.fonkB2()
print ("-"*70)
#--------------------------------------------------------------------------------------------------
"""
paketim klas�r�ndeki __init__.py i�ine
import paketim.paketim1.mod�l1A
import paketim.paketim1.mod�l1B
   import paketim.paketim2.mod�l2A
   import paketim.paketim2.mod�l2B
import paketim.paketim3.mod�l3A
import paketim.paketim3.mod�l3B
dahil edilince
"""

import paketim
print()
paketim.paketim1.mod�l1A.fonk11a()
paketim.paketim1.mod�l1A.fonk12a()
paketim.paketim1.mod�l1B.fonk11b()
paketim.paketim1.mod�l1B.fonk12b()

print()
paketim.paketim2.mod�l2A.fonk21a()
paketim.paketim2.mod�l2A.fonk22a()
paketim.paketim2.mod�l2B.fonk21b()
paketim.paketim2.mod�l2B.fonk22b()

print()
paketim.paketim3.mod�l3A.fonk31a()
paketim.paketim3.mod�l3A.fonk32a()
paketim.paketim3.mod�l3B.fonk31b()
paketim.paketim3.mod�l3B.fonk32b()



"""��kt�:
>python p_12901.py
paketim klas�r�nden mod�lA.py �a�r�l�yor...
paketim klas�r�nden mod�lB.py �a�r�l�yor...

paketim klas�r� mod�lA.py mod�l�nden fonkA1() fonksiyonuyum....
paketim klas�r� mod�lA.py mod�l�nden fonkA2() fonksiyonuyum....

paketim klas�r� mod�lA.py mod�l�nden fonkB1() fonksiyonuyum....
paketim klas�r� mod�lA.py mod�l�nden fonkB2() fonksiyonuyum....
----------------------------------------------------------------------

paketim klas�r� mod�lA.py mod�l�nden fonkA1() fonksiyonuyum....
paketim klas�r� mod�lA.py mod�l�nden fonkA2() fonksiyonuyum....

paketim klas�r� mod�lA.py mod�l�nden fonkB1() fonksiyonuyum....
paketim klas�r� mod�lA.py mod�l�nden fonkB2() fonksiyonuyum....
----------------------------------------------------------------------

paketim.paketim1 klas�r� mod�l1A.py mod�l�nden fonk11a() fonksiyonuyum....
paketim.paketim1 klas�r� mod�l1A.py mod�l�nden fonk12a() fonksiyonuyum....
paketim.paketim1 klas�r� mod�l1B.py mod�l�nden fonk11b() fonksiyonuyum....
paketim.paketim1 klas�r� mod�l1B.py mod�l�nden fonk12b() fonksiyonuyum....

paketim.paketim2 klas�r� mod�l2A.py mod�l�nden fonk21a() fonksiyonuyum....
paketim.paketim2 klas�r� mod�l2A.py mod�l�nden fonk22a() fonksiyonuyum....
paketim.paketim2 klas�r� mod�l2B.py mod�l�nden fonk21b() fonksiyonuyum....
paketim.paketim2 klas�r� mod�l2B.py mod�l�nden fonk22b() fonksiyonuyum....

paketim.paketim3 klas�r� mod�l3A.py mod�l�nden fonk31a() fonksiyonuyum....
paketim.paketim3 klas�r� mod�l3A.py mod�l�nden fonk32a() fonksiyonuyum....
paketim.paketim3 klas�r� mod�l3B.py mod�l�nden fonk31b() fonksiyonuyum....
paketim.paketim3 klas�r� mod�l3B.py mod�l�nden fonk32b() fonksiyonuyum....
"""