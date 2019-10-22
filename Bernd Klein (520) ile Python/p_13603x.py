# coding:iso-8859-9 T�rk�e
# p_13603x.py: Test ama�l� 3 adet fib say�s� d�nd�ren fonksiyon alt-�rne�i.

def fib1 (n):
    """ n.nci fibonaki say�s�n� d�nd�r�r """
    a, b = 0, 1
    for i in range(n): a, b = b, a + b
    return a

def fib2 (n):
    """ n.nci fibonaki say�s�n� d�nd�r�r """
    a, b = 0, 1 # �nce a,b=0,1 dene, sonra da a,b=1,1 dene...
    for i in range(n): a, b = b, a + b
    return a

def fib3 (n):
    """ n.nci fibonaki say�s�n� d�nd�r�r """
    a, b = 0, 1
    for i in range(n): a, b = b, a + b
    # if n == 20: a = 42 # Bu sat�r� ilave et, dene...
    return a
