# coding:iso-8859-9 Türkçe
# p_21103.py: Aritmetik ortalamanın yalın ve içiçe fonksiyonlu sonuçları örneği.

def aritmetikOrtalama (*argümanlar): return sum (argümanlar) / len (argümanlar)

def içiçeFonksiyon (fonk):
    f_argümanlar = []
    f_kwargümanlar = {}

    def f (*argümanlar, **kwargümanlar):
        nonlocal f_argümanlar, f_kwargümanlar
        if argümanlar or kwargümanlar:
            f_argümanlar += argümanlar
            f_kwargümanlar.update (kwargümanlar)
            return f
        else: return fonk (*f_argümanlar, *f_kwargümanlar)

    return f

print ("aritmetikOrtalama fonksiyonuyla:")
print (aritmetikOrtalama (2, 5, 9, 4, 5, 5, 9) )
print (aritmetikOrtalama (2, 500, 9, 4, 5, 5, 9,) )

print ("\niçiçeFonksiyon (aritmetikOrtalama) fonksiyonuyla:")
s1 = içiçeFonksiyon (aritmetikOrtalama)
s1(2)(5)(9)(4, 5)
s1(5, 9)

s2 = içiçeFonksiyon (aritmetikOrtalama)
s2(2)(500)(9)(4, 5)
s2(5, 9)
s2()

print (s1() )
print (s2() )



"""Çıktı:
>python p_21103.py
aritmetikOrtalama fonksiyonuyla:
5.571428571428571
76.28571428571429

içiçeFonksiyon (aritmetikOrtalama) fonksiyonuyla:
5.571428571428571
76.28571428571429
"""