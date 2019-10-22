# coding:iso-8859-9 Türkçe
# p_14301.py: Önceki saat ve takvim çoklu kalıtsal modüllerle bir yıl ve bir gün sonrası örneği.

from p_14101x1 import Saat
from p_14101x2 import Takvim

class TakvimSaat (Saat, Takvim):
   def __init__ (self, gün, ay, yıl, saat=0, dakika=0, saniye=0):
        Takvim.__init__ (self, gün, ay, yıl)
        Saat.__init__ (self, saat, dakika, saniye)
   def __str__ (self): return Takvim.__str__ (self) + ", " + Saat.__str__ (self)


if __name__  == "__main__":
    x = TakvimSaat (4, 5, 2019)
    print ("Bugünün başı:", x)
    for i in range (86399): x.tikTak() # 1 gün=24*60**60-1 sn...
    for i in range (365): x.ilerlet()
    print ("1 yıl günsonu:", x)



"""Çıktı:
>python p_14301.py
Bugünün başı: 4/5/2019, 00:00:00
1 yıl günsonu: 3/5/2020, 23:59:59
"""