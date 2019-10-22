# coding:iso-8859-9 "Türkçe"

x = lambda a : a + 10 # Lambda hazır fonksiyonu tanımı...
print ("Lambda (5 + 10) =", x (5))

x = lambda a, b : a * b
print ("Lambda (5 * 6) =", x (5, 6))

x = lambda a, b, c : a + b + c
print ("Lambda (5 + 6 + 2) =", x (5, 6, 2))

def fonksiyonum (n): return lambda a : a * n

ikiKat = fonksiyonum (2)
print ("İki katlı lambdalı 11 =", ikiKat (11))

beşKat = fonksiyonum (5)
print ("Beş katlı lambdalı 11 =", beşKat (11))
