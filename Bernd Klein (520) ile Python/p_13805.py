# coding:iso-8859-9
# p_13805.py: @class/static metodlarla ebob'li pay/payda üreten sınıf nesnesi örneği.

class tamsayılıBölüm (object):
    def __init__ (self, bölünen, bölen):
        self.pay, self.payda = tamsayılıBölüm.sonuç (bölünen, bölen)

    @staticmethod
    def ebob (a, b): # ebob: EnBüyükOrtakBölen
        while b != 0: a, b = b, a%b
        return a

    @classmethod
    def sonuç (sınıf, n1, n2):
        g = sınıf.ebob (n1, n2)
        return (n1 // g, n2 // g)

    def __str__ (self):
        return str (self.pay) + '/' + str (self.payda)

if __name__ == "__main__":
    print ("8/24 =", tamsayılıBölüm (8, 24) )
    print ("48/6 =", tamsayılıBölüm (48, 6) )
    print ("5/24 =", tamsayılıBölüm (5, 24) )
    print ("5/240 =", tamsayılıBölüm (5, 240) )



"""Çıktı:
>python p_13805.py
8/24 = 1/3
48/6 = 8/1
5/24 = 5/24
5/240 = 1/48
"""