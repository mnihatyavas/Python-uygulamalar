# coding:iso-8859-9 Türkçe
# p_12902.py: İçiçe klasörlerdeki modül-içi fonksiyonları __init__.py vasıtasıyla doğrudan çağırma örneği.

from paketim import *

print ("\n ==>paketim.paketim1.modül1A fonksiyonları çağrılıyor:")
fonk11a()
fonk12a()
print (" ==>paketim.paketim1.modül1B fonksiyonları çağrılıyor:")
fonk11b()
fonk12b()

print ("\n ==>paketim.paketim2.modül2A fonksiyonları çağrılıyor:")
fonk21a()
fonk22a()
print (" ==>paketim.paketim2.modül2B fonksiyonları çağrılıyor:")
fonk21b()
fonk22b()

print ("\n ==>paketim.paketim3.modül3A fonksiyonları çağrılıyor:")
fonk31a()
fonk32a()
print (" ==>paketim.paketim3.modül3 fonksiyonları çağrılıyor:")
fonk31b()
fonk32b()

"""Çıktı:
>python p_12902.py
paketim klasöründen modülA.py çağrılıyor...
paketim klasöründen modülB.py çağrılıyor...

 ==>paketim.paketim1.modül1A fonksiyonları çağrılıyor:
paketim.paketim1 klasörü modül1A.py modülünden fonk11a() fonksiyonuyum....
paketim.paketim1 klasörü modül1A.py modülünden fonk12a() fonksiyonuyum....
 ==>paketim.paketim1.modül1B fonksiyonları çağrılıyor:
paketim.paketim1 klasörü modül1B.py modülünden fonk11b() fonksiyonuyum....
paketim.paketim1 klasörü modül1B.py modülünden fonk12b() fonksiyonuyum....

 ==>paketim.paketim2.modül2A fonksiyonları çağrılıyor:
paketim.paketim2 klasörü modül2A.py modülünden fonk21a() fonksiyonuyum....
paketim.paketim2 klasörü modül2A.py modülünden fonk22a() fonksiyonuyum....
 ==>paketim.paketim2.modül2B fonksiyonları çağrılıyor:
paketim.paketim2 klasörü modül2B.py modülünden fonk21b() fonksiyonuyum....
paketim.paketim2 klasörü modül2B.py modülünden fonk22b() fonksiyonuyum....

 ==>paketim.paketim3.modül3A fonksiyonları çağrılıyor:
paketim.paketim3 klasörü modül3A.py modülünden fonk31a() fonksiyonuyum....
paketim.paketim3 klasörü modül3A.py modülünden fonk32a() fonksiyonuyum....
 ==>paketim.paketim3.modül3 fonksiyonları çağrılıyor:
paketim.paketim3 klasörü modül3B.py modülünden fonk31b() fonksiyonuyum....
paketim.paketim3 klasörü modül3B.py modülünden fonk32b() fonksiyonuyum....
"""

"""Not: paketim __init__.py içeriğine son eklenenler:
# coding:iso-8859-9 Türkçe

from paketim.paketim1.modül1A import *
from paketim.paketim1.modül1B import *

from paketim.paketim2.modül2A import *
from paketim.paketim2.modül2B import *

from paketim.paketim3.modül3A import *
from paketim.paketim3.modül3B import *
"""

"""Tam paket şeması:
paketim
    __init__.py
    modülA.py
        fonkA1()
        fonkA2()
    modülB.py
        fonkB1()
        fonkB2()
    paketim1
        modül1A.py
            fonk11a()
            fonk12a()
        modül1B.py
            fonk11b()
            fonk12b()
    paketim2
        modül2A.py
            fonk21a()
            fonk22a()
        modül2B.py
            fonk21b()
            fonk22b()
    paketim3
        modül3A.py
            fonk31a()
            fonk32a()
        modül3B.py
            fonk31b()
            fonk32b()
"""