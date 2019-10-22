# coding:iso-8859-9 Türkçe

def şehir_üreteci():
    yield ("Londra")
    yield ("Hamburg")
    yield ("Konstanz")
    yield ("Amsterdam")
    yield ("Berlin")
    yield ("Zürih")
    yield ("Şafhoyzen")
    yield ("Ştutgart")
    yield ("İstanbul")
    yield ("İzmir")

def fibonaki (n):
    """ n adet fibonaki serisini yaratan bir üreteç """
    a, b, sayaç = 0, 1, 0
    while True:
        if (sayaç > n): return
        yield a
        a, b = b, a + b
        sayaç += 1

def fib2():
    """ İstenirse sonsuz adet Fibonaki serisi üreteçi """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
