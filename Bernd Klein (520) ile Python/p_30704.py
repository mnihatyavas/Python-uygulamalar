# coding:iso-8859-9 Türkçe
# p_30704.py: Verili ağırlıklı meslek tercihlerinin uygulamalıyla kıyası örneği.

from numpy.random import choice as tercih

meslekler = ["filozof", "alim", "ruhani", "mühendis", "programcı"]
ağırlıkları = [0.05, 0.2, 0.15, 0.3, 0.3]

print ("Kendine gelişigüzel bir meslek seç:", tercih (meslekler, p=ağırlıkları) )
#---------------------------------------------------------------------------------------------------------

from collections import Counter

say = Counter()

try: kere = abs (int (input ("\nKaç kere tercih yapacaksın [10 000]? ")))
except: kere = 10000

for _ in range (kere):
    meslek = tercih (meslekler, p=ağırlıkları)
    say [meslek] += 1

print ("\nToplam ", kere, " kerelik tercih sayısının mesleklere dağılımı:\n", say, sep="")

#toplam = sum (say.values()) # Zaten kere=toplam...
for meslek in say: say[meslek] /= kere

print ("\nHerbir meslek ve tercihlerinin deneysel sonuç yüzdeleri:\n", say, sep="")

print ("\nVerili biçimli çıktılar:\n", "-"*52, sep="")
for _ in range (len (meslekler)): print ("Verili meslek: {:9s} ve olasılık yüzdesi: %{:5.2f}" .format (meslekler[_].upper(), ağırlıkları[_]*100))

print ("\nUygulamalı biçimli çıktılar:\n", "-"*52, sep="")
for meslek in say: print ("Verili meslek: {:9s} ve olasılık yüzdesi: %{:5.2f}" .format (meslek.upper(), say[meslek]*100))



"""Çıktı:
>python p_30704.py
>python p_30704.py
Kendine gelişigüzel bir meslek seç: alim

Kaç kere tercih yapacaksın [10 000]? 1957

Toplam 1957 kerelik tercih sayısının mesleklere dağılımı:
Counter({'programcı': 615, 'mühendis': 563, 'alim': 393, 'ruhani': 283, 'filozof': 103})

Herbir meslek ve tercihlerinin deneysel sonuç yüzdeleri:
Counter({'programcı': 0.314256515074093, 'mühendis': 0.2876852324987225, 'alim': 0.200817577925396, 'ruhani': 0.14460909555442003, 'filozof': 0.05263157894736842})

Verili biçimli çıktılar:
----------------------------------------------------
Verili meslek: FILOZOF   ve olasılık yüzdesi: % 5.00
Verili meslek: ALIM      ve olasılık yüzdesi: %20.00
Verili meslek: RUHANI    ve olasılık yüzdesi: %15.00
Verili meslek: MÜHENDIS  ve olasılık yüzdesi: %30.00
Verili meslek: PROGRAMCI ve olasılık yüzdesi: %30.00

Uygulamalı biçimli çıktılar:
----------------------------------------------------
Verili meslek: PROGRAMCI ve olasılık yüzdesi: %31.43
Verili meslek: ALIM      ve olasılık yüzdesi: %20.08
Verili meslek: FILOZOF   ve olasılık yüzdesi: % 5.26
Verili meslek: MÜHENDIS  ve olasılık yüzdesi: %28.77
Verili meslek: RUHANI    ve olasılık yüzdesi: %14.46

>python p_30704.py  ** TEKRAR **
Kendine gelişigüzel bir meslek seç: programcı

Kaç kere tercih yapacaksın [10 000]?

Toplam 10000 kerelik tercih sayısının mesleklere dağılımı:
Counter({'mühendis': 3043, 'programcı': 2982, 'alim': 2028, 'ruhani': 1469, 'filozof': 478})

Herbir meslek ve tercihlerinin deneysel sonuç yüzdeleri:
Counter({'mühendis': 0.3043, 'programcı': 0.2982, 'alim': 0.2028, 'ruhani': 0.1469, 'filozof': 0.0478})

Verili biçimli çıktılar:
----------------------------------------------------
Verili meslek: FILOZOF   ve olasılık yüzdesi: % 5.00
Verili meslek: ALIM      ve olasılık yüzdesi: %20.00
Verili meslek: RUHANI    ve olasılık yüzdesi: %15.00
Verili meslek: MÜHENDIS  ve olasılık yüzdesi: %30.00
Verili meslek: PROGRAMCI ve olasılık yüzdesi: %30.00

Uygulamalı biçimli çıktılar:
----------------------------------------------------
Verili meslek: ALIM      ve olasılık yüzdesi: %20.28
Verili meslek: PROGRAMCI ve olasılık yüzdesi: %29.82
Verili meslek: MÜHENDIS  ve olasılık yüzdesi: %30.43
Verili meslek: FILOZOF   ve olasılık yüzdesi: % 4.78
Verili meslek: RUHANI    ve olasılık yüzdesi: %14.69

>python p_30704.py  ** TEKRAR**
Kendine gelişigüzel bir meslek seç: programcı

Kaç kere tercih yapacaksın [10 000]? 20000

Toplam 20000 kerelik tercih sayısının mesleklere dağılımı:
Counter({'mühendis': 6094, 'programcı': 5974, 'alim': 3919, 'ruhani': 2993, 'filozof': 1020})

Herbir meslek ve tercihlerinin deneysel sonuç yüzdeleri:
Counter({'mühendis': 0.3047, 'programcı': 0.2987, 'alim': 0.19595, 'ruhani': 0.14965, 'filozof': 0.051})

Verili biçimli çıktılar:
----------------------------------------------------
Verili meslek: FILOZOF   ve olasılık yüzdesi: % 5.00
Verili meslek: ALIM      ve olasılık yüzdesi: %20.00
Verili meslek: RUHANI    ve olasılık yüzdesi: %15.00
Verili meslek: MÜHENDIS  ve olasılık yüzdesi: %30.00
Verili meslek: PROGRAMCI ve olasılık yüzdesi: %30.00

Uygulamalı biçimli çıktılar:
----------------------------------------------------
Verili meslek: PROGRAMCI ve olasılık yüzdesi: %29.87
Verili meslek: MÜHENDIS  ve olasılık yüzdesi: %30.47
Verili meslek: ALIM      ve olasılık yüzdesi: %19.60
Verili meslek: RUHANI    ve olasılık yüzdesi: %14.96
Verili meslek: FILOZOF   ve olasılık yüzdesi: % 5.10
"""