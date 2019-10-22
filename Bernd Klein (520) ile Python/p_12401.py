# coding:iso-8859-9 T�rk�e
# p_12401.py: Fonksiyonda ve ana programda lokal ve global de�i�kenler �rne�i.

def fonk1(): print (dizge) 

dizge = "Ben Paris'in yaz�n� severim!.."
fonk1()
#----------------------------------------------------------------------------------------------------------

def fonk2():
    try: print (dizge)
    except Exception as ist: print ("HATA:", ist)
    dizge = "Hay�r, ben esas Londra'n�n yaz�n� severim!"
    print (dizge)

print()
fonk2()
print (dizge)
#----------------------------------------------------------------------------------------------------------

def fonk3():
    global dizge
    print (dizge)
    dizge = "Ama Londra'da Thames nehri boyunca trekking yapabilirim!.."
    print (dizge)

print()
dizge = "Ben Paris'te uzun bir trekking/y�r�y�� yolu bulamad�m!.." 
fonk3()
print (dizge)
#----------------------------------------------------------------------------------------------------------

def fonk4():
    dizge2 = "Ben global olarak tan�nm�yorum, sadece bu fonksiyon i�in lokal'im."
    print (dizge2) 

print()
fonk4()
try: print (dizge2)
except Exception as ist: print ("HATA:", ist)
#----------------------------------------------------------------------------------------------------------

def fonk5 (x, y):
    global a
    a = 42
    x, y = y, x
    b = 33
    c = 100
    print (a, b, x, y)

print ("\na  b  x y\n", "-"*10, sep="")
a, b, x, y = 1, 15, 3, 4
fonk5 (17, 4)
print (a, b, x, y)


"""��kt�:
>python p_12401.py
Ben Paris'in yaz�n� severim!..

HATA: local variable 'dizge' referenced before assignment
Hay�r, ben esas Londra'n�n yaz�n� severim!
Ben Paris'in yaz�n� severim!..

Ben Paris'te uzun bir trekking/y�r�y�� yolu bulamad�m!..
Ama Londra'da Thames nehri boyunca trekking yapabilirim!..
Ama Londra'da Thames nehri boyunca trekking yapabilirim!..

Ben global olarak tan�nm�yorum, sadece bu fonksiyon i�in lokal'im.
HATA: name 'dizge2' is not defined

a  b  x y
----------
42 33 4 17
42 15 3 4
"""