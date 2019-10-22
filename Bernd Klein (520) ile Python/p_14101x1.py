# coding:iso-8859-9 Türkçe
# p_14101x1.py: Saat sınıfı metoduyla saniyenin bir artıeılması ana/alt-örneği.

class Saat (object): # Saat sınıfı SS:dd:ss zamanı simüle eder...
    def __init__ (self, saat, dakika, saniye):
        self.saatıKur (saat, dakika, saniye) # public/genel...
    def saatıKur (self, saat, dakika, saniye):
        """
        Saat, dakika ve saniye parametreleri tamsayı olmalı ve
        şu değerlerle sınırlanmalıdır:
        0 <= s < 24
        0 <= d < 60
        0 <= sn < 60
        """
        if type (saat) == int and 0 <= saat and saat < 24: self._saat = saat # protected/korumalı...
        else: raise TypeError ("Saat [0->23] arasında ve tamsayı olmalıdır!")
        if type (dakika) == int and 0 <= dakika and dakika < 60: self.__dakika = dakika # private/özel...
        else: raise TypeError ("Dakika [0->59] arasında ve tamsayı olmalıdır!")
        if type (saniye) == int and 0 <= saniye and saniye < 60: self.__saniye = saniye # private/özel...
        else: raise TypeError ("Saniye [0->59] arasında ve tamsayı olmalıdır!")
    def __str__ (self):
        return "{0:02d}:{1:02d}:{2:02d}" .format (self._saat, self.__dakika, self.__saniye)
    def tikTak (self): # Zamanı/saniyeyi bir artırır...
        """
        Örneğin:
        >>> x = Saat (12, 59, 59)
        >>> print (x)
        12:59:59
        >>> x.tikTak()
        >>> print (x)
        13:00:00
        >>> x.tikTak()
        >>> print (x)
        13:00:01
        """
        if self.__saniye == 59:
            self.__saniye = 0
            if self.__dakika == 59:
                self.__dakika = 0
                if self._saat == 23: self._saat = 0
                else: self._saat += 1
            else: self.__dakika += 1
        else: self.__saniye += 1


if __name__ == "__main__":
    x = Saat (23, 59, 59)
    print (x)
    x.tikTak()
    print (x)
    y = str (x)
    print (type (y) )



"""Çıktı:
>python p_14101x1.py
23:59:59
00:00:00
<class 'str'>
"""