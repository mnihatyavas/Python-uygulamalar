# coding:iso-8859-9 T�rk�e

def �ehir_�reteci():
    yield ("Londra")
    yield ("Hamburg")
    yield ("Konstanz")
    yield ("Amsterdam")
    yield ("Berlin")
    yield ("Z�rih")
    yield ("�afhoyzen")
    yield ("�tutgart")
    yield ("�stanbul")
    yield ("�zmir")

def fibonaki (n):
    """ n adet fibonaki serisini yaratan bir �rete� """
    a, b, saya� = 0, 1, 0
    while True:
        if (saya� > n): return
        yield a
        a, b = b, a + b
        saya� += 1

def fib2():
    """ �stenirse sonsuz adet Fibonaki serisi �rete�i """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
