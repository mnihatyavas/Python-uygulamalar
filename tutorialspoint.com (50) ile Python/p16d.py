# coding:iso-8859-9 Türkçe

class AnaSınıf:
    anaDeğer = 100

    def __init__ (self):
        print ("Ana sınıf kurucusu çağrılıyor...")

    def anaMetod (self):
        print ('Ana metod çağrılıyor...')

    def metodum (self):
        print ("Bu 'metodum' ana sınıfın bir metodudur...")

    def değerKoy (self, değer):
        AnaSınıf.anaDeğer = değer

    def değerAl (self):
        print ("AnaSınıf değeri:", AnaSınıf.anaDeğer)

class YavruSınıf (AnaSınıf):
    def __init__ (self):
        print ("Yavru sınıf kurucusu çağrılıyor...")

    def yavruMetod (self):
        print ('Yavru metod çağrılıyor')

    def metodum (self):
        print ("Bu 'metodum' yavru sınıfın override/esgeçme metodudur...")


nesne = YavruSınıf() # Yavru sınıfın bir tiplemesi...
nesne.yavruMetod() # Yavru sınıf metodu çağrılıyor...
nesne.anaMetod() # Mirasla ana sınıf metodu da yavru tipleme nesnesiyle çağrılıyor...
nesne.değerKoy (200) # Mirasla ana sınıf tip değişkenine değer konuluyor...
nesne.değerAl() # Mirasla ana sınıf tip değişkeni değeri alınıyor...
print()
print ("Yavru sınıf ana sınıfın bir alt sınıfı mı?", issubclass (YavruSınıf, AnaSınıf))
print ("'nesne' ana sınıfın bir tiplemesi midir?", isinstance (nesne, AnaSınıf))
print ("'nesne' yavru sınıfın bir tiplemesi midir?", isinstance (nesne, YavruSınıf))
print()
nesne.metodum()
