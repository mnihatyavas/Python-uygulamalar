# coding:iso-8859-9 Türkçe
# p_13405.py: next(x) ile birsonraki karakteri, x.send(n) ile n.nci karakteri döndürme örneği.

def biteviye (nesne):
    uz = len (nesne)
    if uz == 0: return
    sayaç = 0
    while True:
        if sayaç >= uz:
            sayaç = 0
            print()
        mesaj = yield nesne [sayaç]
        if mesaj != None: sayaç = 0 if mesaj < 0 else mesaj
        else: sayaç += 1

mesaj = "Her istediğiniz mesaj argümanını gönderebilirsiniz!.."
x = biteviye (mesaj)

print ("Mesajın 5 kez tekrarı:", "\n", "-"*53, sep="")
uz5 = len (mesaj) * 5
sayaç = 0
while True:
    sayaç +=1
    print (next (x), end="" ) # 5 alt-alta satır bitinceye dek her seferinde tek karakter...
    if sayaç >= uz5: break # Bu sınırlama kontrolu olmazsa mesaj sonsuz gösterilir...
#----------------------------------------------------------------------------------------------------

print ("\n\nMesajın tek karakterli kontrolu:\n", "-"*32, sep="", end="")
print (next (x) )
print (x.send (1) )
print (x.send (2) )
print (x.send (14) )
print (x.send (int (len (mesaj) / 2)) )
print (x.send (len (mesaj) - 3) )
print (x.send (len (mesaj) - 1) )

"""Çıktı:
>python p_13405.py
Mesajın 5 kez tekrarı:
-----------------------------------------------------
Her istediğiniz mesaj argümanını gönderebilirsiniz!..
Her istediğiniz mesaj argümanını gönderebilirsiniz!..
Her istediğiniz mesaj argümanını gönderebilirsiniz!..
Her istediğiniz mesaj argümanını gönderebilirsiniz!..
Her istediğiniz mesaj argümanını gönderebilirsiniz!..

Mesajın tek karakterli kontrolu:
--------------------------------
H
e
r
z
m
!
.
"""