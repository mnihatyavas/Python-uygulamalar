# coding:iso-8859-9 Türkçe
# p_13601b.py: name-main import kontrollü fonksiyon tanımları modülü örneği.

""" Fibonaki Modülü-2 """

def fib (n):
    """ n.nci fibonaki sayısını döndürür """
    a, b = 0, 1
    for i in range(n): a, b = b, a + b
    return a

def fibliste (n):
    """ n adet sıralı fibonaki listesi üretir """
    fib = [0,1]
    for i in range (1,n): fib += [fib[-1]+fib[-2]]
    return fib

if __name__ == "__main__": # Modül import'unda alttakileri esgeçer...
    if fib (0) == 0 and fib (10) == 55 and fib (50) == 12586269025:
        print ("fib fonksiyonu testi başarılıdır!")
    else: print ("fib fonksiyonu yanlış değerler döndürüyor!")
