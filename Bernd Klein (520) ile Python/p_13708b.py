# coding:iso-8859-9
# p_13708b.py: S�n�f nesnesi repr ve str metodlu tiplemelerin eval'le �evrilebilmesi �rne�i.

class Robot:
    def __init__ (self, ad�, y�l�):
        self.ad = ad�
        self.y�l = y�l�
    def __repr__ (self): return "Robot(\"" + self.ad + "\", " +  str (self.y�l) +  ")"
    def __str__ (self): return "Robot(\"" + self.ad + "\", " +  str (self.y�l) +  ")"

if __name__ == "__main__":
    x = Robot ("Muhammed Ali", 19790631)

    print (x, type (x) ) # __str__ metodunu kendi s�n�f tiplemesiyle kullan�r...

    temsiliX = repr (x)
    print (temsiliX, type (temsiliX) ) # __repr__ metodunu str tiplemesiyle kullan�r...

    dizgeX = str (x)
    print (dizgeX, type (dizgeX) ) # __str__ metodunu str tiplemesiyle kullan�r...

    try:
        yeni1 = eval (temsiliX)
        print (yeni1, type (yeni1))
        yeni2 = eval (dizgeX)
        print (yeni2, type (yeni2))
    except Exception as ist: print (ist)

    print ("\n__repr__ ve __str__ eval'le normalen �evrilmiyor, ama s�n�fad�/Robot() ile yan�lt�larak �evriliyor!..")

"""��kt�:
>python p_13708b.py
Robot("Muhammed Ali", 19790631) <class '__main__.Robot'>
Robot("Muhammed Ali",19790631) <class 'str'>
Robot("Muhammed Ali", 19790631) <class 'str'>
Robot("Muhammed Ali", 19790631) <class '__main__.Robot'>
Robot("Muhammed Ali", 19790631) <class '__main__.Robot'>

__repr__ ve __str__ eval'le normalen �evrilmiyor, ama s�n�fad�/Robot() ile yan�lt�larak �evriliyor!..
"""