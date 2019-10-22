# coding:iso-8859-9 T�rk�e
# p_21103.py: Aritmetik ortalaman�n yal�n ve i�i�e fonksiyonlu sonu�lar� �rne�i.

def aritmetikOrtalama (*arg�manlar): return sum (arg�manlar) / len (arg�manlar)

def i�i�eFonksiyon (fonk):
    f_arg�manlar = []
    f_kwarg�manlar = {}

    def f (*arg�manlar, **kwarg�manlar):
        nonlocal f_arg�manlar, f_kwarg�manlar
        if arg�manlar or kwarg�manlar:
            f_arg�manlar += arg�manlar
            f_kwarg�manlar.update (kwarg�manlar)
            return f
        else: return fonk (*f_arg�manlar, *f_kwarg�manlar)

    return f

print ("aritmetikOrtalama fonksiyonuyla:")
print (aritmetikOrtalama (2, 5, 9, 4, 5, 5, 9) )
print (aritmetikOrtalama (2, 500, 9, 4, 5, 5, 9,) )

print ("\ni�i�eFonksiyon (aritmetikOrtalama) fonksiyonuyla:")
s1 = i�i�eFonksiyon (aritmetikOrtalama)
s1(2)(5)(9)(4, 5)
s1(5, 9)

s2 = i�i�eFonksiyon (aritmetikOrtalama)
s2(2)(500)(9)(4, 5)
s2(5, 9)
s2()

print (s1() )
print (s2() )



"""��kt�:
>python p_21103.py
aritmetikOrtalama fonksiyonuyla:
5.571428571428571
76.28571428571429

i�i�eFonksiyon (aritmetikOrtalama) fonksiyonuyla:
5.571428571428571
76.28571428571429
"""