# coding:iso-8859-9 Türkçe
# p_14101.py: Saat ve artıkyıl çift miras kontrollü saniyenin bir ilerletilmesi örneği.

from p_14101x1 import Saat
from p_14101x2 import Takvim

class TakvimliSaat (Saat, Takvim): # Çoklu miras...
    def __init__ (self, gün, ay, yıl, saat, dakika, saniye): # public/genel...
        Saat.__init__ (self, saat, dakika, saniye)
        Takvim.__init__ (self, gün, ay, yıl)
    def tikTak (self):
        öncekiSaat = self._saat
        Saat.tikTak (self)
        if (self._saat < öncekiSaat): self.ilerlet()
    def __str__ (self):
        return Takvim.__str__ (self) + ", " + Saat.__str__ (self)


if __name__ == "__main__":
    x = TakvimliSaat (31, 12, 2018, 23, 59, 59)
    print (x, "tarihinden 1 sn sonrası:", end=" ")
    x.tikTak()
    print (x)

    x = TakvimliSaat (28, 2, 1900, 23, 59, 59)
    print (x, "tarihinden 1 sn sonrası:", end=" ")
    x.tikTak()
    print (x)

    x = TakvimliSaat (28, 2, 2016, 23, 59, 59)
    print (x, "tarihinden 1 sn sonrası:", end=" ")
    x.tikTak()
    print (x)

    x = TakvimliSaat (30, 4, 2019, 4, 23, 45)
    print (x, "tarihinden 1 sn sonrası:", end=" ")
    x.tikTak()
    print (x)

"""Çıktı:
>python p_14101.py
31/12/2018, 23:59:59 tarihinden 1 sn sonrası: 01/01/2019, 00:00:00
28/02/1900, 23:59:59 tarihinden 1 sn sonrası: 01/03/1900, 00:00:00
28/02/2016, 23:59:59 tarihinden 1 sn sonrası: 29/02/2016, 00:00:00
30/04/2019, 04:23:45 tarihinden 1 sn sonrası: 30/04/2019, 04:23:46
"""