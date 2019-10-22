# coding:iso-8859-9 Türkçe
# p_12508x1.py: Dekoratör ve ambalajı ana-programa öncelleyen içiçe fonksiyon alt-örneği.

def selam (fonk):
    def ambalaj (x):
        """ Bu, selam dekoratörünün fonksiyon ambalajıdır. """
        print ("Merhaba, " + fonk.__name__ + " mesajınız: ")
        return fonk (x)
    return ambalaj
