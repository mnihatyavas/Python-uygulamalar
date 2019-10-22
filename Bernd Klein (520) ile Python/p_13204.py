# coding:iso-8859-9 T�rk�e
# p_13204.py: Kapsaml� listemeli def fonksiyonla pi radyan derecelerin sin, cos, tan, cotan sonu�lar� �rne�i.

from math import sin, cos, tan, pi

def fonksiyonlarHaritas� (x, fonksiyonlar):
    # Tek tek x arg�manl� fonkiyonu hesaplay�p listeye ekler...
    """Kapsaml� listeleme kullan�lacaksa bu sat�rlar yedekte kals�n...
    sonu� = []
    for fonk in fonksiyonlar: sonu�.append (fonk (x))
    return sonu�
    """
    return [fonk (x) for fonk in fonksiyonlar] # Kapsaml� listeleme y�ntemi...

def kotan (x): return cos (x) / sin (x)

fonksiyonlar�m = (sin, cos, tan, kotan)

print ("180 derece i�in sin�s, kosin�s, tanjant ve kotanjant listesi:", fonksiyonlarHaritas� (pi, fonksiyonlar�m) )
print ("\n90 derece i�in sin�s, kosin�s, tanjant ve kotanjant listesi:", fonksiyonlarHaritas� (pi/2, fonksiyonlar�m) )
print ("\n60 derece i�in sin�s, kosin�s, tanjant ve kotanjant listesi:", fonksiyonlarHaritas� (pi/3, fonksiyonlar�m) )
print ("\n45 derece i�in sin�s, kosin�s, tanjant ve kotanjant listesi:", fonksiyonlarHaritas� (pi/4, fonksiyonlar�m) )
print ("\n30 derece i�in sin�s, kosin�s, tanjant ve kotanjant listesi:", fonksiyonlarHaritas� (pi/6, fonksiyonlar�m) )

"""��kt�:
>python p_13204.py
180 derece i�in sin�s, kosin�s, tanjant ve kotanjant listesi: [1.2246467991473532e-16, -1.0, -1.2246467991473532e-16, -8165619676597685.0]

90 derece i�in sin�s, kosin�s, tanjant ve kotanjant listesi: [1.0, 6.123233995736766e-17, 1.633123935319537e+16, 6.123233995736766e-17]

60 derece i�in sin�s, kosin�s, tanjant ve kotanjant listesi: [0.8660254037844386, 0.5000000000000001, 1.7320508075688767, 0.577350269189626]

45 derece i�in sin�s, kosin�s, tanjant ve kotanjant listesi: [0.7071067811865475, 0.7071067811865476, 0.9999999999999999, 1.0000000000000002]

30 derece i�in sin�s, kosin�s, tanjant ve kotanjant listesi: [0.49999999999999994, 0.8660254037844387, 0.5773502691896257, 1.7320508075688776]
"""