# coding:iso-8859-9 T�rk�e
# p_14301.py: �nceki saat ve takvim �oklu kal�tsal mod�llerle bir y�l ve bir g�n sonras� �rne�i.

from p_14101x1 import Saat
from p_14101x2 import Takvim

class TakvimSaat (Saat, Takvim):
   def __init__ (self, g�n, ay, y�l, saat=0, dakika=0, saniye=0):
        Takvim.__init__ (self, g�n, ay, y�l)
        Saat.__init__ (self, saat, dakika, saniye)
   def __str__ (self): return Takvim.__str__ (self) + ", " + Saat.__str__ (self)


if __name__  == "__main__":
    x = TakvimSaat (4, 5, 2019)
    print ("Bug�n�n ba��:", x)
    for i in range (86399): x.tikTak() # 1 g�n=24*60**60-1 sn...
    for i in range (365): x.ilerlet()
    print ("1 y�l g�nsonu:", x)



"""��kt�:
>python p_14301.py
Bug�n�n ba��: 4/5/2019, 00:00:00
1 y�l g�nsonu: 3/5/2020, 23:59:59
"""