# coding:iso-8859-9 Türkçe

# Monty Hall problemini simüle eder.

import argparse, random

def simüleEt (kapıSayısı, yarışmacıMı, izahat):
    """bool (int, bool, bool)

    Geçen argümanlardan yarışmacıMı True ise yarışmacı için, False ise
    rakibi için işletilir. Ayrıca izahat varsa (True) herbir etap sonucu
    tek tek gösterilir. Kazanan varsa dönen True, yoksa False'dır...
    """

    # Arkasında hediye bulunan kapı tesadüfi seçilir...
    hediyeliKapı = random.randint (0, kapıSayısı - 1)
    if izahat: print ('Hediyeli kapı numarası: {}' .format (hediyeliKapı + 1))

    # Oyuncu da tesadüfi bir kapı seçer...
    tercih = random.randint (0, kapıSayısı-1)
    if izahat: print ('Oyuncunun seçtiği kapı no: {}' .format (tercih + 1))

    # Ev sahibi 2 kapı hariç diğer tümünü açabilir...
    kapalıKapılar = list (range (kapıSayısı))
    while len (kapalıKapılar) > 2:
        # Açılacak kapı tesadüfi seçilir...
        #silinecekKapı = random.randint (0, len (kapalıKapılar) - 1)
        silinecekKapı = random.choice (kapalıKapılar)

        # Evsahibi hediyeli kapıyı veya oyuncu kapısını silemez...
        if (silinecekKapı == hediyeliKapı or silinecekKapı == tercih): continue

        # Değilse o kapı listeden silinir...
        kapalıKapılar.remove (silinecekKapı)
        if izahat: print ('Ev sahibi {} numaralı kapıyı açtı' .format (silinecekKapı + 1))

    # Geriye daima 2 kapı kalır...
    assert len (kapalıKapılar) == 2

    # Does the contestant want to yarışmacıMı their tercih?
    if yarışmacıMı:
        if izahat: print ('Oyuncu kapı no: {}"den ' .format (tercih+1), end='')

        # Geriye kalan 2 kapıdan, oyuncununkini silelim...
        mevcutKapılar = list (kapalıKapılar) # Bir kopyasını alalım...
        mevcutKapılar.remove (tercih)

        # Geriye kalanı oyuncunun yeni tercihi olacaktır...
        tercih = mevcutKapılar.pop()
        if izahat: print ('{}"e geçti' .format (tercih+1))

    # Oyuncu kazandı mı?
    kazandı = (tercih == hediyeliKapı)
    if izahat:
        if yarışmacıMı:
            if kazandı: print ('Yarışmacı KAZANDI', end='\n\n')
            else: print ('Yarışmacı KAYBETTİ', end='\n\n')
        else:
            if kazandı: print ('Rakip KAZANDI', end='\n\n')
            else: print ('Rakip KAYBETTİ', end='\n\n')

    return kazandı

def anaProgram():
    # Komut-satırı argümanlarını alalım...
    okuyucu = argparse.ArgumentParser (description='Monty Hall problemini simüle eder')
    okuyucu.add_argument ('--kapılar', default=3, type=int, metavar='int', help='Yarışmacıya sunulan kapı sayısı')
    okuyucu.add_argument ('--denemeler', default=10000, type=int, metavar='int', help='İcra edilecek deneme sayısı')
    okuyucu.add_argument ('--izahat', default=False, action='store_true', help='Herbir deneme sonucunun gösterilmesi')
    argümanlar = okuyucu.parse_args()

    print ('Toplam {} deneme simüle ediliyor...' .format (argümanlar.denemeler))

    # Denemeler işletiliyor...
    rakip_puanı = 0
    yarışmacı_puanı = 0
    for i in range (argümanlar.denemeler):
        # Öncelikle yarışmacının denemedikleri simüle edilecek...
        kazandı = simüleEt (argümanlar.kapılar, yarışmacıMı=False, izahat=argümanlar.izahat)
        if kazandı: rakip_puanı += 1

        # Yarışmacının denedikleri simüle ediliyor...
        kazandı = simüleEt (argümanlar.kapılar, yarışmacıMı=True, izahat=argümanlar.izahat)
        if kazandı: yarışmacı_puanı += 1

    print ('==>Yarışmacı kazandı: Toplam {1} denemede {0:5} kere [Yüzdesi: %{2}]' .format (
            yarışmacı_puanı, argümanlar.denemeler, round( (yarışmacı_puanı / argümanlar.denemeler * 100), 2) ))
    print ('==>Rakibi kazandı: Toplam {1} denemede {0:5} kere [Yüzdesi: %{2}]' .format (
            rakip_puanı, argümanlar.denemeler, round( (rakip_puanı / argümanlar.denemeler * 100), 2) ))

if __name__ == '__main__':
    anaProgram()

çıktı1="""
**  >python p03.py -h  **
usage: p03.py [-h] [--kapılar int] [--denemeler int] [--izahat]

Monty Hall problemini simüle eder

optional arguments:
  -h, --help       show this help message and exit
  --kapılar int    Yarışmacıya sunulan kapı sayısı
  --denemeler int  İcra edilecek deneme sayısı
  --izahat         Herbir deneme sonucunun gösterilmesi
"""

çıktı2="""
**  >python p03.py  **
Toplam 10000 deneme simüle ediliyor...
==>Yarışmacı kazandı: Toplam 10000 denemede  6685 kere [Yüzdesi: %66.85]
==>Rakibi kazandı: Toplam 10000 denemede  3333 kere [Yüzdesi: %33.33]
"""

çıktı3="""
**  >python p03.py --kapılar 15 --denemeler 20000  **
Toplam 20000 deneme simüle ediliyor...
==>Yarışmacı kazandı: Toplam 20000 denemede 18686 kere [Yüzdesi: %93.43]
==>Rakibi kazandı: Toplam 20000 denemede  1337 kere [Yüzdesi: %6.69]
"""

çıktı4="""
**  >python p03.py --kapılar 2 --denemeler 1 --izahat  **
Toplam 1 deneme simüle ediliyor...
Hediyeli kapı numarası: 2
Oyuncunun seçtiği kapı no: 1
Rakip KAYBETTİ

Hediyeli kapı numarası: 2
Oyuncunun seçtiği kapı no: 1
Oyuncu kapı no: 1"den 2"e geçti
Yarışmacı KAZANDI

==>Yarışmacı kazandı: Toplam 1 denemede     1 kere [Yüzdesi: %100.0]
==>Rakibi kazandı: Toplam 1 denemede     0 kere [Yüzdesi: %0.0]
"""