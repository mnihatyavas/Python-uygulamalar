# coding:iso-8859-9
# p_13803.py: Sınıf tip özelliğinin init kurucu ve del imhacı hazı metodlarda kullanımı örneği.

class C: 
    sayaç = 0 # Sınıf tip değişkeni...
    def __init__ (self):  type (self).sayaç += 1
    def __del__ (self): C.sayaç -= 1 # C == type(self)


if __name__ == "__main__":
    x = C()
    print ("Yaratma sonrası toplam tipleme sayısı: : " + str (C.sayaç) )

    y = C()
    print ("Yaratma sonrası toplam tipleme sayısı: : " + str (C.sayaç) )

    z = C()
    print ("Yaratma sonrası toplam tipleme sayısı: : " + str (C.sayaç) )

    del z
    print ("\nİmha sonrası kalan tipleme sayısı: : " + str (C.sayaç) )

    del y
    print ("İmha sonrası kalan tipleme sayısı: : " + str (C.sayaç) )

    del x
    print ("İmha sonrası kalan tipleme sayısı: : " + str (C.sayaç) )

"""Çıktı:
>python p_13803.py
Yaratma sonrası toplam tipleme sayısı: : 1
Yaratma sonrası toplam tipleme sayısı: : 2
Yaratma sonrası toplam tipleme sayısı: : 3

İmha sonrası kalan tipleme sayısı: : 2
İmha sonrası kalan tipleme sayısı: : 1
İmha sonrası kalan tipleme sayısı: : 0
"""