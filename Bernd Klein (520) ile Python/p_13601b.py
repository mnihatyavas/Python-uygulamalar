# coding:iso-8859-9 T�rk�e
# p_13601b.py: name-main import kontroll� fonksiyon tan�mlar� mod�l� �rne�i.

""" Fibonaki Mod�l�-2 """

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

if __name__ == "__main__": # Mod�l import'unda alttakileri esge�er...
    if fib (0) == 0 and fib (10) == 55 and fib (50) == 12586269025:
        print ("fib fonksiyonu testi ba�ar�l�d�r!")
    else: print ("fib fonksiyonu yanl�� de�erler d�nd�r�yor!")
