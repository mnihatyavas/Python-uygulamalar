# coding:iso-8859-9 T�rk�e
# p_13407.py: Dekorat�rl� sonsuz d�ng�l� �rete�le mesaj ve karakter ��kt�lar� �rne�i.

from functools import wraps

def haz�rla (�ret):
    # Dekorat�r: �lk yield<None> bir ilerletilip esas mesaj� iletmeye haz�rlar...
    @wraps (�ret)
    def �rete� (*args,**kwargs):   
        g = �ret (*args,**kwargs)   
        next (g)   
        return g   
    return �rete�

@haz�rla
def sonsuz_d�ng� (msj):
    saya� = 0
    mesaj = yield None # �lk None dekorat�rle atlat�l�r...
    while True:
        if saya� >= len (msj):
            saya� = 0
            print()
        mesaj = yield msj [saya�]
        if mesaj != None: saya� = 0 if mesaj < 0 else mesaj
        else: saya� += 1

mesaj = "Dekorat�rle haz�rlanan sonsuz �rete� fonksiyonu!.."
x = sonsuz_d�ng� (mesaj) 

print ("Mesaj�n 5 kez tekrar�:", "\n", "-"*22, sep="")
say = 0
while True:
    say +=1
    print (next (x), end="" )
    if say >= len (mesaj) * 5: break

print ("\n\nMesaj�n tek karakterli kontrolu:\n", "-"*32, sep="", end="")
print (next (x))
print (x.send (4))
print (next (x))
print (next (x))
print (x.send (5))
print (next (x))
print (next (x))
print (x.send (int (len(mesaj)/2)) )
print (x.send (len (mesaj) - 3))

"""��kt�:
>python p_13407.py
Mesaj�n 5 kez tekrar�:
----------------------
Dekorat�rle haz�rlanan sonsuz �rete� fonksiyonu!..
Dekorat�rle haz�rlanan sonsuz �rete� fonksiyonu!..
Dekorat�rle haz�rlanan sonsuz �rete� fonksiyonu!..
Dekorat�rle haz�rlanan sonsuz �rete� fonksiyonu!..
Dekorat�rle haz�rlanan sonsuz �rete� fonksiyonu!..

Mesaj�n tek karakterli kontrolu:
--------------------------------
D
r
a
t
a
t
�
n
!
"""