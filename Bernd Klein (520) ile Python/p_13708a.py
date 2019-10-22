# coding:iso-8859-9
# p_13708a.py: S�n�f nesnesi repr ve str metod tiplemesi eval yap�lamamas� �rne�i.

class Robot:
    def __init__ (self, ad�, y�l�):
        self.ad = ad�
        self.y�l = y�l�
    def __repr__ (self):
        return "Robotumuz " + self.ad + ", " +  str (self.y�l) +  " tarihinde imal edildi."
    def __str__ (self):
        return "Robotun ad�: " + self.ad + ", �malat tarihi: " +  str (self.y�l)

if __name__ == "__main__":
    x = Robot ("Muhammed Ali", 19790631)

    print (x, ", Tipi:", type (x) ) # __str__ metodunu kendi s�n�f tiplemesiyle kullan�r...

    temsiliX = repr (x)
    print (temsiliX, type (temsiliX) ) # __repr__ metodunu str tiplemesiyle kullan�r...

    dizgeX = str (x)
    print (dizgeX, ",", type (dizgeX) ) # __str__ metodunu str tiplemesiyle kullan�r...

    try:
        yeni1 = eval (temsiliX)
        yeni2 = eval (dizgeX)
    except Exception as ist: print (ist)

    print ("Devam")

"""��kt�:
>python p_13708a.py
Robotun ad�: Muhammed Ali, �malat tarihi: 19790631 , Tipi: <class '__main__.Robot'>
Robotumuz Muhammed Ali, 19790631 tarihinde imal edildi. <class 'str'>
Robotun ad�: Muhammed Ali, �malat tarihi: 19790631 , <class 'str'>
invalid syntax (<string>, line 1)
Devam
"""