# coding:iso-8859-9 Türkçe
# p_13603x.py: Test amaçlı 3 adet fib sayısı döndüren fonksiyon alt-örneği.

def fib1 (n):
    """ n.nci fibonaki sayısını döndürür """
    a, b = 0, 1
    for i in range(n): a, b = b, a + b
    return a

def fib2 (n):
    """ n.nci fibonaki sayısını döndürür """
    a, b = 0, 1 # Önce a,b=0,1 dene, sonra da a,b=1,1 dene...
    for i in range(n): a, b = b, a + b
    return a

def fib3 (n):
    """ n.nci fibonaki sayısını döndürür """
    a, b = 0, 1
    for i in range(n): a, b = b, a + b
    # if n == 20: a = 42 # Bu satırı ilave et, dene...
    return a
