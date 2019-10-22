# coding:iso-8859-9 T�rk�e
# p_12402.py: Fonksiyonlardaki global ve nonlocal'in genel de�i�keni a�mas� �rne�i.

def fonk1():
    x = 42
    def fonk11():
        global x # Ana program i�in global, fonk1() i�in de�il...
        x = 43
    print ("fonk11() �a�r�lmadan �nce:", x)
    print ("�imdi fonk11() �a�r�l�yor...")
    fonk11()
    print ("fonk11() �a�r�ld�ktan sonra:", x)

x = 3 # Global bunu a�ar...
fonk1()
print ("Ana programda x:", x)
#-------------------------------------------------------------------------------------------------------

def fonk2():
    x = 42
    def fonk22():
        nonlocal x # Sadece buraya lokal de�il, tam kapsaml�...
        x = 43
    print  ("fonk22() �a�r�lmadan �nce:", x)
    print ("�imdi fonk22() �a�r�l�yor...")
    fonk22()
    print ("fonk22() �a�r�ld�ktan sonra:", x)

print()
x = 3 # nonlocal bunu a�maz, bu yoksa nonlocal ge�erlidir...
fonk2()
print ("Ana programda x:", x)


"""��kt�:
>python p_12402.py
fonk11() �a�r�lmadan �nce: 42
�imdi fonk11() �a�r�l�yor...
fonk11() �a�r�ld�ktan sonra: 42
Ana programda x: 43

fonk22() �a�r�lmadan �nce: 42
�imdi fonk22() �a�r�l�yor...
fonk22() �a�r�ld�ktan sonra: 43
Ana programda x: 3
"""