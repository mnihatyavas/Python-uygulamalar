# coding:iso-8859-9 Türkçe
# p_12901.py: İçiçe klasörlerdeki py modüllerini __init__.py vasıtasıyla çağırma örneği.

# paketim klasöründe boş __init__.py yeterli...
from paketim import modülA, modülB

print()
modülA.fonkA1()
modülA.fonkA2()

print()
modülB.fonkB1()
modülB.fonkB2()
print ("-"*70)
#--------------------------------------------------------------------------------------------------
"""
paketim klasöründeki __init__.py içine
import paketim.modülA
import paketim.modülB
dahil edilince
"""
import paketim
print()
paketim.modülA.fonkA1()
paketim.modülA.fonkA2()

print()
paketim.modülB.fonkB1()
paketim.modülB.fonkB2()
print ("-"*70)
#--------------------------------------------------------------------------------------------------
"""
paketim klasöründeki __init__.py içine
import paketim.paketim1.modül1A
import paketim.paketim1.modül1B
   import paketim.paketim2.modül2A
   import paketim.paketim2.modül2B
import paketim.paketim3.modül3A
import paketim.paketim3.modül3B
dahil edilince
"""

import paketim
print()
paketim.paketim1.modül1A.fonk11a()
paketim.paketim1.modül1A.fonk12a()
paketim.paketim1.modül1B.fonk11b()
paketim.paketim1.modül1B.fonk12b()

print()
paketim.paketim2.modül2A.fonk21a()
paketim.paketim2.modül2A.fonk22a()
paketim.paketim2.modül2B.fonk21b()
paketim.paketim2.modül2B.fonk22b()

print()
paketim.paketim3.modül3A.fonk31a()
paketim.paketim3.modül3A.fonk32a()
paketim.paketim3.modül3B.fonk31b()
paketim.paketim3.modül3B.fonk32b()



"""Çıktı:
>python p_12901.py
paketim klasöründen modülA.py çağrılıyor...
paketim klasöründen modülB.py çağrılıyor...

paketim klasörü modülA.py modülünden fonkA1() fonksiyonuyum....
paketim klasörü modülA.py modülünden fonkA2() fonksiyonuyum....

paketim klasörü modülA.py modülünden fonkB1() fonksiyonuyum....
paketim klasörü modülA.py modülünden fonkB2() fonksiyonuyum....
----------------------------------------------------------------------

paketim klasörü modülA.py modülünden fonkA1() fonksiyonuyum....
paketim klasörü modülA.py modülünden fonkA2() fonksiyonuyum....

paketim klasörü modülA.py modülünden fonkB1() fonksiyonuyum....
paketim klasörü modülA.py modülünden fonkB2() fonksiyonuyum....
----------------------------------------------------------------------

paketim.paketim1 klasörü modül1A.py modülünden fonk11a() fonksiyonuyum....
paketim.paketim1 klasörü modül1A.py modülünden fonk12a() fonksiyonuyum....
paketim.paketim1 klasörü modül1B.py modülünden fonk11b() fonksiyonuyum....
paketim.paketim1 klasörü modül1B.py modülünden fonk12b() fonksiyonuyum....

paketim.paketim2 klasörü modül2A.py modülünden fonk21a() fonksiyonuyum....
paketim.paketim2 klasörü modül2A.py modülünden fonk22a() fonksiyonuyum....
paketim.paketim2 klasörü modül2B.py modülünden fonk21b() fonksiyonuyum....
paketim.paketim2 klasörü modül2B.py modülünden fonk22b() fonksiyonuyum....

paketim.paketim3 klasörü modül3A.py modülünden fonk31a() fonksiyonuyum....
paketim.paketim3 klasörü modül3A.py modülünden fonk32a() fonksiyonuyum....
paketim.paketim3 klasörü modül3B.py modülünden fonk31b() fonksiyonuyum....
paketim.paketim3 klasörü modül3B.py modülünden fonk32b() fonksiyonuyum....
"""