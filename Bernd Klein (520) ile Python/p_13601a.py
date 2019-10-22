# coding:iso-8859-9 T�rk�e
# p_13601a.py: Bilinen sonu�larla fib fonksiyonunun do�ruluk testi �rne�i.

""" Fibonaki Mod�l�-1 """

def fib (n):
    """ n.nci fibonaki say�s�n� d�nd�r�r """
    a, b = 0, 1
    for i in range(n): a, b = b, a + b
    return a

def fibliste (n):
    """ n adet s�ral� fibonaki listesi �retir """
    fib = [0,1]
    for i in range (1,n): fib += [fib[-1]+fib[-2]]
    return fib

if fib (0) == 0 and fib (10) == 55 and fib (50) == 12586269025:
    print ("fib fonksiyonu testi ba�ar�l�d�r!")
else: print ("fib fonksiyonu yanl�� de�erler d�nd�r�yor!")



"""��kt�:
>python p_13601a.py
fib fonksiyonu testi ba�ar�l�d�r!
"""