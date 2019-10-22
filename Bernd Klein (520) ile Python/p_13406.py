# coding:iso-8859-9 Türkçe
# p_13406.py: döngü.throw(ÜretecinDurumu) ile son sayaç kontrollü yield üreteci örneği.

class ÜreteçinDurumu (Exception):
     def __init__ (self, mesaj=None):
         self.mesaj = mesaj

def sonsuz_döngü (nesne):
    uz = len (nesne)
    sayaç = 0
    while True:
        if sayaç >= uz:
            sayaç = 0
            print()
        try: mesaj = yield nesne [sayaç]
        except ÜreteçinDurumu: print ("endeks: " + str (sayaç))
        if mesaj != None: sayaç = 0 if mesaj < 0 else mesaj
        else: sayaç += 1

argüman = "Python"
döngü = sonsuz_döngü (argüman)

print ("Argümanın 5 kez tekrarı:", "\n", "-"*24, sep="")
uz5 = len (argüman) * 5
say = 0
while True:
    say +=1
    print (next (döngü), end="" )
    if say >= uz5: break

print ("\n\nArgümanının tek karakterli kontrolu:\n", "-"*36, sep="", end="")
print (next (döngü) )
print (next (döngü) )
print (next (döngü) )
print ("Endeksin son değerini fırlat==>", end=" ")
print (döngü.throw (ÜreteçinDurumu) ) # Son endeksi fırlatır ve sıradaki argüman karakterini döndürür...
print (döngü.send (4) )
print (döngü.send (len (argüman) -1) )

"""Çıktı:
>python p_13406.py
Argümanın 5 kez tekrarı:
------------------------
Python
Python
Python
Python
Python

Argümanının tek karakterli kontrolu:
------------------------------------
P
y
t
Endeksin son değerini fırlat==> endeks: 2
h
o
n
"""