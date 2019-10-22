# coding:iso-8859-9
# p_13708a.py: Sınıf nesnesi repr ve str metod tiplemesi eval yapılamaması örneği.

class Robot:
    def __init__ (self, adı, yılı):
        self.ad = adı
        self.yıl = yılı
    def __repr__ (self):
        return "Robotumuz " + self.ad + ", " +  str (self.yıl) +  " tarihinde imal edildi."
    def __str__ (self):
        return "Robotun adı: " + self.ad + ", İmalat tarihi: " +  str (self.yıl)

if __name__ == "__main__":
    x = Robot ("Muhammed Ali", 19790631)

    print (x, ", Tipi:", type (x) ) # __str__ metodunu kendi sınıf tiplemesiyle kullanır...

    temsiliX = repr (x)
    print (temsiliX, type (temsiliX) ) # __repr__ metodunu str tiplemesiyle kullanır...

    dizgeX = str (x)
    print (dizgeX, ",", type (dizgeX) ) # __str__ metodunu str tiplemesiyle kullanır...

    try:
        yeni1 = eval (temsiliX)
        yeni2 = eval (dizgeX)
    except Exception as ist: print (ist)

    print ("Devam")

"""Çıktı:
>python p_13708a.py
Robotun adı: Muhammed Ali, İmalat tarihi: 19790631 , Tipi: <class '__main__.Robot'>
Robotumuz Muhammed Ali, 19790631 tarihinde imal edildi. <class 'str'>
Robotun adı: Muhammed Ali, İmalat tarihi: 19790631 , <class 'str'>
invalid syntax (<string>, line 1)
Devam
"""