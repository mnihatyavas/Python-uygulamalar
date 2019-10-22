# coding:iso-8859-9 Türkçe
# p_12508x3.py: Dekoratör ve ambalajı @wraps'le ana-programa sonralayan içiçe fonksiyon alt-örneği.

from functools import wraps

def selam (fonk):
    @wraps (fonk)
    def ambalaj (x):
        """ Bu, selam dekoratörünün fonksiyon ambalajıdır. """
        print ("Merhaba, " + fonk.__name__ + " mesajınız: ")
        return fonk (x)
    return ambalaj
