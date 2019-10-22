# coding:iso-8859-9 Türkçe
# p_12508x2.py: Dekoratör ve ambalajı ana programa sonralayan içiçe fonksiyon alt-örneği.

def selam (fonk):
    def ambalaj (x):
        """ Bu, selam dekoratörünün fonksiyon ambalajıdır. """
        print ("Merhaba, " + fonk.__name__ + " mesajınız: ")
        return fonk (x)
    ambalaj.__name__ = fonk.__name__
    ambalaj.__doc__ = fonk.__doc__
    ambalaj.__module__ = fonk.__module__
    return ambalaj
