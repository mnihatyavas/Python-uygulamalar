# coding:iso-8859-9
# p_13708b.py: Sınıf nesnesi repr ve str metodlu tiplemelerin eval'le çevrilebilmesi örneği.

class Robot:
    def __init__ (self, adı, yılı):
        self.ad = adı
        self.yıl = yılı
    def __repr__ (self): return "Robot(\"" + self.ad + "\", " +  str (self.yıl) +  ")"
    def __str__ (self): return "Robot(\"" + self.ad + "\", " +  str (self.yıl) +  ")"

if __name__ == "__main__":
    x = Robot ("Muhammed Ali", 19790631)

    print (x, type (x) ) # __str__ metodunu kendi sınıf tiplemesiyle kullanır...

    temsiliX = repr (x)
    print (temsiliX, type (temsiliX) ) # __repr__ metodunu str tiplemesiyle kullanır...

    dizgeX = str (x)
    print (dizgeX, type (dizgeX) ) # __str__ metodunu str tiplemesiyle kullanır...

    try:
        yeni1 = eval (temsiliX)
        print (yeni1, type (yeni1))
        yeni2 = eval (dizgeX)
        print (yeni2, type (yeni2))
    except Exception as ist: print (ist)

    print ("\n__repr__ ve __str__ eval'le normalen çevrilmiyor, ama sınıfadı/Robot() ile yanıltılarak çevriliyor!..")

"""Çıktı:
>python p_13708b.py
Robot("Muhammed Ali", 19790631) <class '__main__.Robot'>
Robot("Muhammed Ali",19790631) <class 'str'>
Robot("Muhammed Ali", 19790631) <class 'str'>
Robot("Muhammed Ali", 19790631) <class '__main__.Robot'>
Robot("Muhammed Ali", 19790631) <class '__main__.Robot'>

__repr__ ve __str__ eval'le normalen çevrilmiyor, ama sınıfadı/Robot() ile yanıltılarak çevriliyor!..
"""