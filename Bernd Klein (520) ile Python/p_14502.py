# coding:iso-8859-9 T�rk�e
# p_14502.py: Birbiriyle ayn� normal ve tipli s�n�f kar��la�t�rmas� �rne�i.

class Robot1:
    saya� = 0
    def __init__ (self, ad): self.ad = ad
    def selamla (self): return "Merhaba, Benim ad�m " + self.ad + "'dir."

def Robot2_init (self, ad): self.ad = ad
Robot2 = type ("Robot2",
        (),
        {"saya�":0,
         "__init__": Robot2_init,
         "selamla": lambda self: "Merhaba, Benim ad�m " + self.ad + "'dir." } )

# Robot1 ile Robot2 ayn�d�r...

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



"""��kt�:
>python p_14502.py
Muhammed Ali
Merhaba, Benim ad�m Muhammed Ali'dir.

Mustafa Nedim
Merhaba, Benim ad�m Mustafa Nedim'dir.

{'ad': 'Muhammed Ali'}
{'ad': 'Mustafa Nedim'}
"""