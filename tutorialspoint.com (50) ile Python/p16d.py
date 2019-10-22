# coding:iso-8859-9 T�rk�e

class AnaS�n�f:
    anaDe�er = 100

    def __init__ (self):
        print ("Ana s�n�f kurucusu �a�r�l�yor...")

    def anaMetod (self):
        print ('Ana metod �a�r�l�yor...')

    def metodum (self):
        print ("Bu 'metodum' ana s�n�f�n bir metodudur...")

    def de�erKoy (self, de�er):
        AnaS�n�f.anaDe�er = de�er

    def de�erAl (self):
        print ("AnaS�n�f de�eri:", AnaS�n�f.anaDe�er)

class YavruS�n�f (AnaS�n�f):
    def __init__ (self):
        print ("Yavru s�n�f kurucusu �a�r�l�yor...")

    def yavruMetod (self):
        print ('Yavru metod �a�r�l�yor')

    def metodum (self):
        print ("Bu 'metodum' yavru s�n�f�n override/esge�me metodudur...")


nesne = YavruS�n�f() # Yavru s�n�f�n bir tiplemesi...
nesne.yavruMetod() # Yavru s�n�f metodu �a�r�l�yor...
nesne.anaMetod() # Mirasla ana s�n�f metodu da yavru tipleme nesnesiyle �a�r�l�yor...
nesne.de�erKoy (200) # Mirasla ana s�n�f tip de�i�kenine de�er konuluyor...
nesne.de�erAl() # Mirasla ana s�n�f tip de�i�keni de�eri al�n�yor...
print()
print ("Yavru s�n�f ana s�n�f�n bir alt s�n�f� m�?", issubclass (YavruS�n�f, AnaS�n�f))
print ("'nesne' ana s�n�f�n bir tiplemesi midir?", isinstance (nesne, AnaS�n�f))
print ("'nesne' yavru s�n�f�n bir tiplemesi midir?", isinstance (nesne, YavruS�n�f))
print()
nesne.metodum()
