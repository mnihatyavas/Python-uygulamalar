# coding:iso-8859-9 T�rk�e
# p_315.py Tesad�fi renk yaratma �rne�i.

from random import randint
class Renk:
    def rgb():
        L = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        i = randint (0,15)
        return str (L [i])

    def renk():
        dizge = ""
        for i in range (6): dizge +=Renk.rgb()
        return "#" + dizge

#print (Renk.renk() )