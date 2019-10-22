# coding:iso-8859-9 Türkçe
# p_12402.py: Fonksiyonlardaki global ve nonlocal'in genel değişkeni aşması örneği.

def fonk1():
    x = 42
    def fonk11():
        global x # Ana program için global, fonk1() için değil...
        x = 43
    print ("fonk11() çağrılmadan önce:", x)
    print ("Şimdi fonk11() çağrılıyor...")
    fonk11()
    print ("fonk11() çağrıldıktan sonra:", x)

x = 3 # Global bunu aşar...
fonk1()
print ("Ana programda x:", x)
#-------------------------------------------------------------------------------------------------------

def fonk2():
    x = 42
    def fonk22():
        nonlocal x # Sadece buraya lokal değil, tam kapsamlı...
        x = 43
    print  ("fonk22() çağrılmadan önce:", x)
    print ("Şimdi fonk22() çağrılıyor...")
    fonk22()
    print ("fonk22() çağrıldıktan sonra:", x)

print()
x = 3 # nonlocal bunu aşmaz, bu yoksa nonlocal geçerlidir...
fonk2()
print ("Ana programda x:", x)


"""Çıktı:
>python p_12402.py
fonk11() çağrılmadan önce: 42
Şimdi fonk11() çağrılıyor...
fonk11() çağrıldıktan sonra: 42
Ana programda x: 43

fonk22() çağrılmadan önce: 42
Şimdi fonk22() çağrılıyor...
fonk22() çağrıldıktan sonra: 43
Ana programda x: 3
"""