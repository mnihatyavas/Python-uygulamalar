# coding:iso-8859-9 Türkçe

class Sayaç:
    __gizliTipDeğişkeni = 0 # Dışardan erişilemez gizli sınıf tip değişkeni...

    def sayacıArtır (self):
        self.__gizliTipDeğişkeni += 1
        print ("Sayaç değeri:", self.__gizliTipDeğişkeni)

sayaç = Sayaç()
for i in range (10): sayaç.sayacıArtır()
# print ("Sayacımızın son değeri:", sayaç__gizliTipDeğişkeni)==> Hata verir...
print ("\nSayacımızın son değeri:", sayaç._Sayaç__gizliTipDeğişkeni)
