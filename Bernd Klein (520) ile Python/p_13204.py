# coding:iso-8859-9 Türkçe
# p_13204.py: Kapsamlı listemeli def fonksiyonla pi radyan derecelerin sin, cos, tan, cotan sonuçları örneği.

from math import sin, cos, tan, pi

def fonksiyonlarHaritası (x, fonksiyonlar):
    # Tek tek x argümanlı fonkiyonu hesaplayıp listeye ekler...
    """Kapsamlı listeleme kullanılacaksa bu satırlar yedekte kalsın...
    sonuç = []
    for fonk in fonksiyonlar: sonuç.append (fonk (x))
    return sonuç
    """
    return [fonk (x) for fonk in fonksiyonlar] # Kapsamlı listeleme yöntemi...

def kotan (x): return cos (x) / sin (x)

fonksiyonlarım = (sin, cos, tan, kotan)

print ("180 derece için sinüs, kosinüs, tanjant ve kotanjant listesi:", fonksiyonlarHaritası (pi, fonksiyonlarım) )
print ("\n90 derece için sinüs, kosinüs, tanjant ve kotanjant listesi:", fonksiyonlarHaritası (pi/2, fonksiyonlarım) )
print ("\n60 derece için sinüs, kosinüs, tanjant ve kotanjant listesi:", fonksiyonlarHaritası (pi/3, fonksiyonlarım) )
print ("\n45 derece için sinüs, kosinüs, tanjant ve kotanjant listesi:", fonksiyonlarHaritası (pi/4, fonksiyonlarım) )
print ("\n30 derece için sinüs, kosinüs, tanjant ve kotanjant listesi:", fonksiyonlarHaritası (pi/6, fonksiyonlarım) )

"""Çıktı:
>python p_13204.py
180 derece için sinüs, kosinüs, tanjant ve kotanjant listesi: [1.2246467991473532e-16, -1.0, -1.2246467991473532e-16, -8165619676597685.0]

90 derece için sinüs, kosinüs, tanjant ve kotanjant listesi: [1.0, 6.123233995736766e-17, 1.633123935319537e+16, 6.123233995736766e-17]

60 derece için sinüs, kosinüs, tanjant ve kotanjant listesi: [0.8660254037844386, 0.5000000000000001, 1.7320508075688767, 0.577350269189626]

45 derece için sinüs, kosinüs, tanjant ve kotanjant listesi: [0.7071067811865475, 0.7071067811865476, 0.9999999999999999, 1.0000000000000002]

30 derece için sinüs, kosinüs, tanjant ve kotanjant listesi: [0.49999999999999994, 0.8660254037844387, 0.5773502691896257, 1.7320508075688776]
"""