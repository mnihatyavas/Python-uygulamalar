# coding:iso-8859-9
# p_13803.py: S�n�f tip �zelli�inin init kurucu ve del imhac� haz� metodlarda kullan�m� �rne�i.

class C: 
    saya� = 0 # S�n�f tip de�i�keni...
    def __init__ (self):  type (self).saya� += 1
    def __del__ (self): C.saya� -= 1 # C == type(self)


if __name__ == "__main__":
    x = C()
    print ("Yaratma sonras� toplam tipleme say�s�: : " + str (C.saya�) )

    y = C()
    print ("Yaratma sonras� toplam tipleme say�s�: : " + str (C.saya�) )

    z = C()
    print ("Yaratma sonras� toplam tipleme say�s�: : " + str (C.saya�) )

    del z
    print ("\n�mha sonras� kalan tipleme say�s�: : " + str (C.saya�) )

    del y
    print ("�mha sonras� kalan tipleme say�s�: : " + str (C.saya�) )

    del x
    print ("�mha sonras� kalan tipleme say�s�: : " + str (C.saya�) )

"""��kt�:
>python p_13803.py
Yaratma sonras� toplam tipleme say�s�: : 1
Yaratma sonras� toplam tipleme say�s�: : 2
Yaratma sonras� toplam tipleme say�s�: : 3

�mha sonras� kalan tipleme say�s�: : 2
�mha sonras� kalan tipleme say�s�: : 1
�mha sonras� kalan tipleme say�s�: : 0
"""