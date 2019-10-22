# coding:iso-8859-9 Türkçe
# p_12510.py: Dekoratörlü @ fonksiyon ve sınıfının karşılaştırılması örneği.

def dekoratör1 (f):
    def yardımcı (x):
        print (f.__name__ + " adlı fonksiyonu dekore ediyorum")
        f (x)
    return yardımcı

@dekoratör1
def fonk (a): print (a, "mutlak sayısının karekökü:", abs (a**(1/2)) )

print ("Karekök işlemini olağan dekoratör fonksiyonuyla yapıyorum==>")
tüple = (-1.25, 2, -45.89, 9, 0)
for (i, j) in enumerate (tüple):
    print ("\n", i+1, ": ", sep="", end="")
    fonk (j)
print ("-"*75, "\n")
#---------------------------------------------------------------------------------------------------------

class dekoratör2:
    def __init__ (self, f): self.f1 = f
    def __call__ (self, b):
        print (self.f1.__name__ + " adlı fonksiyonu dekore ediyorum")
        self.f1 (b)

@dekoratör2
def fonk1 (a): print (a, "mutlak sayısının karekökü:", abs (a**(1/2)) )

print ("Şimdi de aynı işlemi dekoratör sınıfıyla gerçekleştiriyorum==>")
for (i, j) in enumerate (tüple):
    print ("\n", i+1, ": ", sep="", end="")
    fonk1 (j)



"""Çıktı:
>python p_12510.py
Karekök işlemini olağan dekoratör fonksiyonuyla yapıyorum==>

1:fonk adlı fonksiyonu dekore ediyorum
-1.25 mutlak sayısının karekökü: 1.118033988749895

2:fonk adlı fonksiyonu dekore ediyorum
2 mutlak sayısının karekökü: 1.4142135623730951

3:fonk adlı fonksiyonu dekore ediyorum
-45.89 mutlak sayısının karekökü: 6.774215821775979

4:fonk adlı fonksiyonu dekore ediyorum
9 mutlak sayısının karekökü: 3.0

5:fonk adlı fonksiyonu dekore ediyorum
0 mutlak sayısının karekökü: 0.0
---------------------------------------------------------------------------

Şimdi de aynı işlemi dekoratör sınıfıyla gerçekleştiriyorum==>

1:fonk1 adlı fonksiyonu dekore ediyorum
-1.25 mutlak sayısının karekökü: 1.118033988749895

2:fonk1 adlı fonksiyonu dekore ediyorum
2 mutlak sayısının karekökü: 1.4142135623730951

3:fonk1 adlı fonksiyonu dekore ediyorum
-45.89 mutlak sayısının karekökü: 6.774215821775979

4:fonk1 adlı fonksiyonu dekore ediyorum
9 mutlak sayısının karekökü: 3.0

5:fonk1 adlı fonksiyonu dekore ediyorum
0 mutlak sayısının karekökü: 0.0
"""