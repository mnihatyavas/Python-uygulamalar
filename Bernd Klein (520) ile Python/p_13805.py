# coding:iso-8859-9
# p_13805.py: @class/static metodlarla ebob'li pay/payda �reten s�n�f nesnesi �rne�i.

class tamsay�l�B�l�m (object):
    def __init__ (self, b�l�nen, b�len):
        self.pay, self.payda = tamsay�l�B�l�m.sonu� (b�l�nen, b�len)

    @staticmethod
    def ebob (a, b): # ebob: EnB�y�kOrtakB�len
        while b != 0: a, b = b, a%b
        return a

    @classmethod
    def sonu� (s�n�f, n1, n2):
        g = s�n�f.ebob (n1, n2)
        return (n1 // g, n2 // g)

    def __str__ (self):
        return str (self.pay) + '/' + str (self.payda)

if __name__ == "__main__":
    print ("8/24 =", tamsay�l�B�l�m (8, 24) )
    print ("48/6 =", tamsay�l�B�l�m (48, 6) )
    print ("5/24 =", tamsay�l�B�l�m (5, 24) )
    print ("5/240 =", tamsay�l�B�l�m (5, 240) )



"""��kt�:
>python p_13805.py
8/24 = 1/3
48/6 = 8/1
5/24 = 5/24
5/240 = 1/48
"""