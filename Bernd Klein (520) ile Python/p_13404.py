# coding:iso-8859-9 T�rk�e
# p_13404.py: Arg�mans�z send-yield de�er ge�irme, print �rete� ve istisnas� �rne�i.

def arg�mans�z_ileti�im():
    print ("Arg�mans�z ileti�im fonksiyonu ba�lat�ld�!")
    x = yield # send(..) ile yield'e arg�man aktar�labilir...
    print ("send->yield ile al�nan de�er:", x)

fonk1 = arg�mans�z_ileti�im()

try:
    next (fonk1) # �lk next ile ilk print �al��t�r�l�r...
    next (fonk1) # �kinci next ile yield-x'li ikinci print �al��t�r�l�r...
    next (fonk1) # except i�letilir...
except StopIteration: print ("HATA1")
#--------------------------------------------------------------------------------------------------

fonk2 = arg�mans�z_ileti�im()

print()
try:
    next (fonk2) # ilk print...
    print (fonk2.send ("Merhaba!") ) # yield'e g�nderilen mesajl� x print'i...
    next (fonk2) # except...
except StopIteration: print ("HATA2")

"""��kt�:
>python p_13404.py
Arg�mans�z ileti�im fonksiyonu ba�lat�ld�!
send->yield ile al�nan de�er: None
HATA1

Arg�mans�z ileti�im fonksiyonu ba�lat�ld�!
send->yield ile al�nan de�er: Merhaba!
HATA2
"""