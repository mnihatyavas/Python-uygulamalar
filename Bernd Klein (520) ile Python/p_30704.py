# coding:iso-8859-9 T�rk�e
# p_30704.py: Verili a��rl�kl� meslek tercihlerinin uygulamal�yla k�yas� �rne�i.

from numpy.random import choice as tercih

meslekler = ["filozof", "alim", "ruhani", "m�hendis", "programc�"]
a��rl�klar� = [0.05, 0.2, 0.15, 0.3, 0.3]

print ("Kendine geli�ig�zel bir meslek se�:", tercih (meslekler, p=a��rl�klar�) )
#---------------------------------------------------------------------------------------------------------

from collections import Counter

say = Counter()

try: kere = abs (int (input ("\nKa� kere tercih yapacaks�n [10 000]? ")))
except: kere = 10000

for _ in range (kere):
    meslek = tercih (meslekler, p=a��rl�klar�)
    say [meslek] += 1

print ("\nToplam ", kere, " kerelik tercih say�s�n�n mesleklere da��l�m�:\n", say, sep="")

#toplam = sum (say.values()) # Zaten kere=toplam...
for meslek in say: say[meslek] /= kere

print ("\nHerbir meslek ve tercihlerinin deneysel sonu� y�zdeleri:\n", say, sep="")

print ("\nVerili bi�imli ��kt�lar:\n", "-"*52, sep="")
for _ in range (len (meslekler)): print ("Verili meslek: {:9s} ve olas�l�k y�zdesi: %{:5.2f}" .format (meslekler[_].upper(), a��rl�klar�[_]*100))

print ("\nUygulamal� bi�imli ��kt�lar:\n", "-"*52, sep="")
for meslek in say: print ("Verili meslek: {:9s} ve olas�l�k y�zdesi: %{:5.2f}" .format (meslek.upper(), say[meslek]*100))



"""��kt�:
>python p_30704.py
>python p_30704.py
Kendine geli�ig�zel bir meslek se�: alim

Ka� kere tercih yapacaks�n [10 000]? 1957

Toplam 1957 kerelik tercih say�s�n�n mesleklere da��l�m�:
Counter({'programc�': 615, 'm�hendis': 563, 'alim': 393, 'ruhani': 283, 'filozof': 103})

Herbir meslek ve tercihlerinin deneysel sonu� y�zdeleri:
Counter({'programc�': 0.314256515074093, 'm�hendis': 0.2876852324987225, 'alim': 0.200817577925396, 'ruhani': 0.14460909555442003, 'filozof': 0.05263157894736842})

Verili bi�imli ��kt�lar:
----------------------------------------------------
Verili meslek: FILOZOF   ve olas�l�k y�zdesi: % 5.00
Verili meslek: ALIM      ve olas�l�k y�zdesi: %20.00
Verili meslek: RUHANI    ve olas�l�k y�zdesi: %15.00
Verili meslek: M�HENDIS  ve olas�l�k y�zdesi: %30.00
Verili meslek: PROGRAMCI ve olas�l�k y�zdesi: %30.00

Uygulamal� bi�imli ��kt�lar:
----------------------------------------------------
Verili meslek: PROGRAMCI ve olas�l�k y�zdesi: %31.43
Verili meslek: ALIM      ve olas�l�k y�zdesi: %20.08
Verili meslek: FILOZOF   ve olas�l�k y�zdesi: % 5.26
Verili meslek: M�HENDIS  ve olas�l�k y�zdesi: %28.77
Verili meslek: RUHANI    ve olas�l�k y�zdesi: %14.46

>python p_30704.py  ** TEKRAR **
Kendine geli�ig�zel bir meslek se�: programc�

Ka� kere tercih yapacaks�n [10 000]?

Toplam 10000 kerelik tercih say�s�n�n mesleklere da��l�m�:
Counter({'m�hendis': 3043, 'programc�': 2982, 'alim': 2028, 'ruhani': 1469, 'filozof': 478})

Herbir meslek ve tercihlerinin deneysel sonu� y�zdeleri:
Counter({'m�hendis': 0.3043, 'programc�': 0.2982, 'alim': 0.2028, 'ruhani': 0.1469, 'filozof': 0.0478})

Verili bi�imli ��kt�lar:
----------------------------------------------------
Verili meslek: FILOZOF   ve olas�l�k y�zdesi: % 5.00
Verili meslek: ALIM      ve olas�l�k y�zdesi: %20.00
Verili meslek: RUHANI    ve olas�l�k y�zdesi: %15.00
Verili meslek: M�HENDIS  ve olas�l�k y�zdesi: %30.00
Verili meslek: PROGRAMCI ve olas�l�k y�zdesi: %30.00

Uygulamal� bi�imli ��kt�lar:
----------------------------------------------------
Verili meslek: ALIM      ve olas�l�k y�zdesi: %20.28
Verili meslek: PROGRAMCI ve olas�l�k y�zdesi: %29.82
Verili meslek: M�HENDIS  ve olas�l�k y�zdesi: %30.43
Verili meslek: FILOZOF   ve olas�l�k y�zdesi: % 4.78
Verili meslek: RUHANI    ve olas�l�k y�zdesi: %14.69

>python p_30704.py  ** TEKRAR**
Kendine geli�ig�zel bir meslek se�: programc�

Ka� kere tercih yapacaks�n [10 000]? 20000

Toplam 20000 kerelik tercih say�s�n�n mesleklere da��l�m�:
Counter({'m�hendis': 6094, 'programc�': 5974, 'alim': 3919, 'ruhani': 2993, 'filozof': 1020})

Herbir meslek ve tercihlerinin deneysel sonu� y�zdeleri:
Counter({'m�hendis': 0.3047, 'programc�': 0.2987, 'alim': 0.19595, 'ruhani': 0.14965, 'filozof': 0.051})

Verili bi�imli ��kt�lar:
----------------------------------------------------
Verili meslek: FILOZOF   ve olas�l�k y�zdesi: % 5.00
Verili meslek: ALIM      ve olas�l�k y�zdesi: %20.00
Verili meslek: RUHANI    ve olas�l�k y�zdesi: %15.00
Verili meslek: M�HENDIS  ve olas�l�k y�zdesi: %30.00
Verili meslek: PROGRAMCI ve olas�l�k y�zdesi: %30.00

Uygulamal� bi�imli ��kt�lar:
----------------------------------------------------
Verili meslek: PROGRAMCI ve olas�l�k y�zdesi: %29.87
Verili meslek: M�HENDIS  ve olas�l�k y�zdesi: %30.47
Verili meslek: ALIM      ve olas�l�k y�zdesi: %19.60
Verili meslek: RUHANI    ve olas�l�k y�zdesi: %14.96
Verili meslek: FILOZOF   ve olas�l�k y�zdesi: % 5.10
"""