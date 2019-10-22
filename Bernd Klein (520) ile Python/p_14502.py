# coding:iso-8859-9 Türkçe
# p_14502.py: Birbiriyle aynı normal ve tipli sınıf karşılaştırması örneği.

class Robot1:
    sayaç = 0
    def __init__ (self, ad): self.ad = ad
    def selamla (self): return "Merhaba, Benim adım " + self.ad + "'dir."

def Robot2_init (self, ad): self.ad = ad
Robot2 = type ("Robot2",
        (),
        {"sayaç":0,
         "__init__": Robot2_init,
         "selamla": lambda self: "Merhaba, Benim adım " + self.ad + "'dir." } )

# Robot1 ile Robot2 aynıdır...

x1 = Robot1 ("Muhammed Ali")
print (x1.ad)
print (x1.selamla() )

print()
x2 = Robot2 ("Mustafa Nedim")
print (x2.ad)
print (x2.selamla() )

print()
print (x1.__dict__)
print (x2.__dict__)



"""Çıktı:
>python p_14502.py
Muhammed Ali
Merhaba, Benim adım Muhammed Ali'dir.

Mustafa Nedim
Merhaba, Benim adım Mustafa Nedim'dir.

{'ad': 'Muhammed Ali'}
{'ad': 'Mustafa Nedim'}
"""