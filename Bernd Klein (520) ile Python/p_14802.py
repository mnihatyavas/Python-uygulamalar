# coding:iso-8859-9 T�rk�e
# p_14802.py: @Dekorat�rl� ve atamal� fonksiyonla �a�r� say�s� tesbiti �rne�i.

def saya�Metodu (fonk):
    def yard�mc� (*arg�manlar, **kwarg�manlar):
        yard�mc�.�a�r� += 1
        return fonk (*arg�manlar, **kwarg�manlar)
    yard�mc�.�a�r� = 0
    yard�mc�.__name__= fonk.__name__
    return yard�mc�

@saya�Metodu # Dekorat�rl�...
def f(): pass

print ("Dekorat�rl�:")
print (f.�a�r�)

for _ in range (10): f()
print (f.�a�r�)
#------------------------------------------------------------------------------------------------------

def fnk(): pass # Dekorat�rs�z...
f = saya�Metodu (fnk)

print ("\nDekorat�rs�z:")
print (f.�a�r�)

for i in range (10): f()
print (f.�a�r�)



"""��kt�:
>python p_14802.py
Dekorat�rl�:
0
10

Dekorat�rs�z:
0
10
"""