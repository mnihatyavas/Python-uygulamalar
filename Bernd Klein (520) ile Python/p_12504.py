# coding:iso-8859-9 T�rk�e
# p_12504.py: Parametrik i�i�e fonksiyonlarda @ direktifi �rne�i.

def dekorat�r�m (fonksiyon):
    def sarmalay�c�m (x):
        print (fonksiyon.__name__ + " adl� fonksiyon �a�r�lmadan �nce")
        fonksiyon (x)
        print (fonksiyon.__name__ + " adl� fonksiyon �a�r�ld�ktan sonra")
    return sarmalay�c�m

def fonk (x): print ("Merhaba, fonk('" + str (x) + "') �a�r�ld�!")

print ("fonk('Selam') dekorat�rs�z �a�r�l�yor:")
fonk ("Selam")

print ("\n�imdi fonk(x) dekorlan�yor...")
f = dekorat�r�m (fonk)
print ("Ve dekorlu fonk(1957) �a�r�l�yor:")
f (1957)
print ("-"*75, "\n")
#------------------------------------------------------------------------------------------------------

# f, son dekar�t�rl� isim i�in, arg�man olan fonk fonksiyon ad� kullan�labilir...
fonk = dekorat�r�m (fonk)
print ("Dekorlu fonk('17/04/1957') yeniden �a�r�l�yor:")
fonk ("17/04/1957")
print ("-"*75, "\n")
#------------------------------------------------------------------------------------------------------

# Hatta def fonk �n�ne @dekorat�r�m tan�t�m�yla fonk=dekorat�r�m(fonk) gereksizle�ir...
@dekorat�r�m
def fonk (x): print ("Merhaba, fonk('" + str (x) + "') �a�r�ld�!")
print ("@ dekorlu fonk('17 Nisan 1957') yeniden �a�r�l�yor:")
fonk ("17 Nisan 1957")



"""��kt�:
>python p_12504.py
fonk('Selam') dekorat�rs�z �a�r�l�yor:
Merhaba, fonk('Selam') �a�r�ld�!

�imdi fonk(x) dekorlan�yor...
Ve dekorlu fonk(1957) �a�r�l�yor:
fonk adl� fonksiyon �a�r�lmadan �nce
Merhaba, fonk('1957') �a�r�ld�!
fonk adl� fonksiyon �a�r�ld�ktan sonra
---------------------------------------------------------------------------

Dekorlu fonk('17/04/1957') yeniden �a�r�l�yor:
fonk adl� fonksiyon �a�r�lmadan �nce
Merhaba, fonk('17/04/1957') �a�r�ld�!
fonk adl� fonksiyon �a�r�ld�ktan sonra
---------------------------------------------------------------------------

@ dekorlu fonk('17 Nisan 1957') yeniden �a�r�l�yor:
fonk adl� fonksiyon �a�r�lmadan �nce
Merhaba, fonk('17 Nisan 1957') �a�r�ld�!
fonk adl� fonksiyon �a�r�ld�ktan sonra
"""