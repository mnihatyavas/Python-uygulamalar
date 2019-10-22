# coding:iso-8859-9 T�rk�e
# p_14101x1.py: Saat s�n�f� metoduyla saniyenin bir art�e�lmas� ana/alt-�rne�i.

class Saat (object): # Saat s�n�f� SS:dd:ss zaman� sim�le eder...
    def __init__ (self, saat, dakika, saniye):
        self.saat�Kur (saat, dakika, saniye) # public/genel...
    def saat�Kur (self, saat, dakika, saniye):
        """
        Saat, dakika ve saniye parametreleri tamsay� olmal� ve
        �u de�erlerle s�n�rlanmal�d�r:
        0 <= s < 24
        0 <= d < 60
        0 <= sn < 60
        """
        if type (saat) == int and 0 <= saat and saat < 24: self._saat = saat # protected/korumal�...
        else: raise TypeError ("Saat [0->23] aras�nda ve tamsay� olmal�d�r!")
        if type (dakika) == int and 0 <= dakika and dakika < 60: self.__dakika = dakika # private/�zel...
        else: raise TypeError ("Dakika [0->59] aras�nda ve tamsay� olmal�d�r!")
        if type (saniye) == int and 0 <= saniye and saniye < 60: self.__saniye = saniye # private/�zel...
        else: raise TypeError ("Saniye [0->59] aras�nda ve tamsay� olmal�d�r!")
    def __str__ (self):
        return "{0:02d}:{1:02d}:{2:02d}" .format (self._saat, self.__dakika, self.__saniye)
    def tikTak (self): # Zaman�/saniyeyi bir art�r�r...
        """
        �rne�in:
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



"""��kt�:
>python p_14101x1.py
23:59:59
00:00:00
<class 'str'>
"""