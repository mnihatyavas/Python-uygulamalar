# coding:iso-8859-9 Türkçe

from random import randint
def rgb():
    L = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    i = randint (0,14)
    return str (L[i])

def renk():
    dizge = ""
    for i in range (6): dizge = dizge + rgb()
    return "#" + dizge
renk = [renk() for i in range (1000)]
