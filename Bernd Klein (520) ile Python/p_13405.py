# coding:iso-8859-9 T�rk�e
# p_13405.py: next(x) ile birsonraki karakteri, x.send(n) ile n.nci karakteri d�nd�rme �rne�i.

def biteviye (nesne):
    uz = len (nesne)
    if uz == 0: return
    saya� = 0
    while True:
        if saya� >= uz:
            saya� = 0
            print()
        mesaj = yield nesne [saya�]
        if mesaj != None: saya� = 0 if mesaj < 0 else mesaj
        else: saya� += 1

mesaj = "Her istedi�iniz mesaj arg�man�n� g�nderebilirsiniz!.."
x = biteviye (mesaj)

print ("Mesaj�n 5 kez tekrar�:", "\n", "-"*53, sep="")
uz5 = len (mesaj) * 5
saya� = 0
while True:
    saya� +=1
    print (next (x), end="" ) # 5 alt-alta sat�r bitinceye dek her seferinde tek karakter...
    if saya� >= uz5: break # Bu s�n�rlama kontrolu olmazsa mesaj sonsuz g�sterilir...
#----------------------------------------------------------------------------------------------------

print ("\n\nMesaj�n tek karakterli kontrolu:\n", "-"*32, sep="", end="")
print (next (x) )
print (x.send (1) )
print (x.send (2) )
print (x.send (14) )
print (x.send (int (len (mesaj) / 2)) )
print (x.send (len (mesaj) - 3) )
print (x.send (len (mesaj) - 1) )

"""��kt�:
>python p_13405.py
Mesaj�n 5 kez tekrar�:
-----------------------------------------------------
Her istedi�iniz mesaj arg�man�n� g�nderebilirsiniz!..
Her istedi�iniz mesaj arg�man�n� g�nderebilirsiniz!..
Her istedi�iniz mesaj arg�man�n� g�nderebilirsiniz!..
Her istedi�iniz mesaj arg�man�n� g�nderebilirsiniz!..
Her istedi�iniz mesaj arg�man�n� g�nderebilirsiniz!..

Mesaj�n tek karakterli kontrolu:
--------------------------------
H
e
r
z
m
!
.
"""