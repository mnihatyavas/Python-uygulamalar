# coding:iso-8859-9 T�rk�e
# p_13406.py: d�ng�.throw(�retecinDurumu) ile son saya� kontroll� yield �reteci �rne�i.

class �rete�inDurumu (Exception):
     def __init__ (self, mesaj=None):
         self.mesaj = mesaj

def sonsuz_d�ng� (nesne):
    uz = len (nesne)
    saya� = 0
    while True:
        if saya� >= uz:
            saya� = 0
            print()
        try: mesaj = yield nesne [saya�]
        except �rete�inDurumu: print ("endeks: " + str (saya�))
        if mesaj != None: saya� = 0 if mesaj < 0 else mesaj
        else: saya� += 1

arg�man = "Python"
d�ng� = sonsuz_d�ng� (arg�man)

print ("Arg�man�n 5 kez tekrar�:", "\n", "-"*24, sep="")
uz5 = len (arg�man) * 5
say = 0
while True:
    say +=1
    print (next (d�ng�), end="" )
    if say >= uz5: break

print ("\n\nArg�man�n�n tek karakterli kontrolu:\n", "-"*36, sep="", end="")
print (next (d�ng�) )
print (next (d�ng�) )
print (next (d�ng�) )
print ("Endeksin son de�erini f�rlat==>", end=" ")
print (d�ng�.throw (�rete�inDurumu) ) # Son endeksi f�rlat�r ve s�radaki arg�man karakterini d�nd�r�r...
print (d�ng�.send (4) )
print (d�ng�.send (len (arg�man) -1) )

"""��kt�:
>python p_13406.py
Arg�man�n 5 kez tekrar�:
------------------------
Python
Python
Python
Python
Python

Arg�man�n�n tek karakterli kontrolu:
------------------------------------
P
y
t
Endeksin son de�erini f�rlat==> endeks: 2
h
o
n
"""