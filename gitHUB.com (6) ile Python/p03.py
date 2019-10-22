# coding:iso-8859-9 T�rk�e

# Monty Hall problemini sim�le eder.

import argparse, random

def sim�leEt (kap�Say�s�, yar��mac�M�, izahat):
    """bool (int, bool, bool)

    Ge�en arg�manlardan yar��mac�M� True ise yar��mac� i�in, False ise
    rakibi i�in i�letilir. Ayr�ca izahat varsa (True) herbir etap sonucu
    tek tek g�sterilir. Kazanan varsa d�nen True, yoksa False'd�r...
    """

    # Arkas�nda hediye bulunan kap� tesad�fi se�ilir...
    hediyeliKap� = random.randint (0, kap�Say�s� - 1)
    if izahat: print ('Hediyeli kap� numaras�: {}' .format (hediyeliKap� + 1))

    # Oyuncu da tesad�fi bir kap� se�er...
    tercih = random.randint (0, kap�Say�s�-1)
    if izahat: print ('Oyuncunun se�ti�i kap� no: {}' .format (tercih + 1))

    # Ev sahibi 2 kap� hari� di�er t�m�n� a�abilir...
    kapal�Kap�lar = list (range (kap�Say�s�))
    while len (kapal�Kap�lar) > 2:
        # A��lacak kap� tesad�fi se�ilir...
        #silinecekKap� = random.randint (0, len (kapal�Kap�lar) - 1)
        silinecekKap� = random.choice (kapal�Kap�lar)

        # Evsahibi hediyeli kap�y� veya oyuncu kap�s�n� silemez...
        if (silinecekKap� == hediyeliKap� or silinecekKap� == tercih): continue

        # De�ilse o kap� listeden silinir...
        kapal�Kap�lar.remove (silinecekKap�)
        if izahat: print ('Ev sahibi {} numaral� kap�y� a�t�' .format (silinecekKap� + 1))

    # Geriye daima 2 kap� kal�r...
    assert len (kapal�Kap�lar) == 2

    # Does the contestant want to yar��mac�M� their tercih?
    if yar��mac�M�:
        if izahat: print ('Oyuncu kap� no: {}"den ' .format (tercih+1), end='')

        # Geriye kalan 2 kap�dan, oyuncununkini silelim...
        mevcutKap�lar = list (kapal�Kap�lar) # Bir kopyas�n� alal�m...
        mevcutKap�lar.remove (tercih)

        # Geriye kalan� oyuncunun yeni tercihi olacakt�r...
        tercih = mevcutKap�lar.pop()
        if izahat: print ('{}"e ge�ti' .format (tercih+1))

    # Oyuncu kazand� m�?
    kazand� = (tercih == hediyeliKap�)
    if izahat:
        if yar��mac�M�:
            if kazand�: print ('Yar��mac� KAZANDI', end='\n\n')
            else: print ('Yar��mac� KAYBETT�', end='\n\n')
        else:
            if kazand�: print ('Rakip KAZANDI', end='\n\n')
            else: print ('Rakip KAYBETT�', end='\n\n')

    return kazand�

def anaProgram():
    # Komut-sat�r� arg�manlar�n� alal�m...
    okuyucu = argparse.ArgumentParser (description='Monty Hall problemini sim�le eder')
    okuyucu.add_argument ('--kap�lar', default=3, type=int, metavar='int', help='Yar��mac�ya sunulan kap� say�s�')
    okuyucu.add_argument ('--denemeler', default=10000, type=int, metavar='int', help='�cra edilecek deneme say�s�')
    okuyucu.add_argument ('--izahat', default=False, action='store_true', help='Herbir deneme sonucunun g�sterilmesi')
    arg�manlar = okuyucu.parse_args()

    print ('Toplam {} deneme sim�le ediliyor...' .format (arg�manlar.denemeler))

    # Denemeler i�letiliyor...
    rakip_puan� = 0
    yar��mac�_puan� = 0
    for i in range (arg�manlar.denemeler):
        # �ncelikle yar��mac�n�n denemedikleri sim�le edilecek...
        kazand� = sim�leEt (arg�manlar.kap�lar, yar��mac�M�=False, izahat=arg�manlar.izahat)
        if kazand�: rakip_puan� += 1

        # Yar��mac�n�n denedikleri sim�le ediliyor...
        kazand� = sim�leEt (arg�manlar.kap�lar, yar��mac�M�=True, izahat=arg�manlar.izahat)
        if kazand�: yar��mac�_puan� += 1

    print ('==>Yar��mac� kazand�: Toplam {1} denemede {0:5} kere [Y�zdesi: %{2}]' .format (
            yar��mac�_puan�, arg�manlar.denemeler, round( (yar��mac�_puan� / arg�manlar.denemeler * 100), 2) ))
    print ('==>Rakibi kazand�: Toplam {1} denemede {0:5} kere [Y�zdesi: %{2}]' .format (
            rakip_puan�, arg�manlar.denemeler, round( (rakip_puan� / arg�manlar.denemeler * 100), 2) ))

if __name__ == '__main__':
    anaProgram()

��kt�1="""
**  >python p03.py -h  **
usage: p03.py [-h] [--kap�lar int] [--denemeler int] [--izahat]

Monty Hall problemini sim�le eder

optional arguments:
  -h, --help       show this help message and exit
  --kap�lar int    Yar��mac�ya sunulan kap� say�s�
  --denemeler int  �cra edilecek deneme say�s�
  --izahat         Herbir deneme sonucunun g�sterilmesi
"""

��kt�2="""
**  >python p03.py  **
Toplam 10000 deneme sim�le ediliyor...
==>Yar��mac� kazand�: Toplam 10000 denemede  6685 kere [Y�zdesi: %66.85]
==>Rakibi kazand�: Toplam 10000 denemede  3333 kere [Y�zdesi: %33.33]
"""

��kt�3="""
**  >python p03.py --kap�lar 15 --denemeler 20000  **
Toplam 20000 deneme sim�le ediliyor...
==>Yar��mac� kazand�: Toplam 20000 denemede 18686 kere [Y�zdesi: %93.43]
==>Rakibi kazand�: Toplam 20000 denemede  1337 kere [Y�zdesi: %6.69]
"""

��kt�4="""
**  >python p03.py --kap�lar 2 --denemeler 1 --izahat  **
Toplam 1 deneme sim�le ediliyor...
Hediyeli kap� numaras�: 2
Oyuncunun se�ti�i kap� no: 1
Rakip KAYBETT�

Hediyeli kap� numaras�: 2
Oyuncunun se�ti�i kap� no: 1
Oyuncu kap� no: 1"den 2"e ge�ti
Yar��mac� KAZANDI

==>Yar��mac� kazand�: Toplam 1 denemede     1 kere [Y�zdesi: %100.0]
==>Rakibi kazand�: Toplam 1 denemede     0 kere [Y�zdesi: %0.0]
"""