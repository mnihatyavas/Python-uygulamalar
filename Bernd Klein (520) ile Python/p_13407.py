# coding:iso-8859-9 Türkçe
# p_13407.py: Dekoratörlü sonsuz döngülü üreteçle mesaj ve karakter çıktıları örneği.

from functools import wraps

def hazırla (üret):
    # Dekoratör: İlk yield<None> bir ilerletilip esas mesajı iletmeye hazırlar...
    @wraps (üret)
    def üreteç (*args,**kwargs):   
        g = üret (*args,**kwargs)   
        next (g)   
        return g   
    return üreteç

@hazırla
def sonsuz_döngü (msj):
    sayaç = 0
    mesaj = yield None # İlk None dekoratörle atlatılır...
    while True:
        if sayaç >= len (msj):
            sayaç = 0
            print()
        mesaj = yield msj [sayaç]
        if mesaj != None: sayaç = 0 if mesaj < 0 else mesaj
        else: sayaç += 1

mesaj = "Dekoratörle hazırlanan sonsuz üreteç fonksiyonu!.."
x = sonsuz_döngü (mesaj) 

print ("Mesajın 5 kez tekrarı:", "\n", "-"*22, sep="")
say = 0
while True:
    say +=1
    print (next (x), end="" )
    if say >= len (mesaj) * 5: break

print ("\n\nMesajın tek karakterli kontrolu:\n", "-"*32, sep="", end="")
print (next (x))
print (x.send (4))
print (next (x))
print (next (x))
print (x.send (5))
print (next (x))
print (next (x))
print (x.send (int (len(mesaj)/2)) )
print (x.send (len (mesaj) - 3))

"""Çıktı:
>python p_13407.py
Mesajın 5 kez tekrarı:
----------------------
Dekoratörle hazırlanan sonsuz üreteç fonksiyonu!..
Dekoratörle hazırlanan sonsuz üreteç fonksiyonu!..
Dekoratörle hazırlanan sonsuz üreteç fonksiyonu!..
Dekoratörle hazırlanan sonsuz üreteç fonksiyonu!..
Dekoratörle hazırlanan sonsuz üreteç fonksiyonu!..

Mesajın tek karakterli kontrolu:
--------------------------------
D
r
a
t
a
t
ö
n
!
"""