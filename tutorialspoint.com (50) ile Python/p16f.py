# coding:iso-8859-9 T�rk�e

class Saya�:
    __gizliTipDe�i�keni = 0 # D��ardan eri�ilemez gizli s�n�f tip de�i�keni...

    def sayac�Art�r (self):
        self.__gizliTipDe�i�keni += 1
        print ("Saya� de�eri:", self.__gizliTipDe�i�keni)

saya� = Saya�()
for i in range (10): saya�.sayac�Art�r()
# print ("Sayac�m�z�n son de�eri:", saya�__gizliTipDe�i�keni)==> Hata verir...
print ("\nSayac�m�z�n son de�eri:", saya�._Saya�__gizliTipDe�i�keni)
