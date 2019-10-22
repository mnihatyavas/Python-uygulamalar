# coding:iso-8859-9 T�rk�e
# Komut iletisinden girilen t�m F dereceyi C dereceye �evirir...

import sys

def �evir (S):
    """(dizge): float
    Komut iletisinden arg�man olarak girilen Fahrenhayt float dizgesini
    a�a��daki form�lle bir Selsiy�s derecesine �evirir. Arg�man girilmez
    yada yanl�� girilirse kullan�c�ya bildirilir...
    """
    fahrenhayt = float (S)
    selsiy�s = (fahrenhayt - 32) * 5 / 9
    return selsiy�s

def anaProgram():
    # �ayet F argv unutulmu�sa hat�rlat�lmal�d�r...
    if len (sys.argv) == 1:
        print ("{} ..[Unutulan arg�manlar: F1 F2 ...]" .format (sys.argv[0]))
        sys.exit (0)

    # Arg�man say�s� kadar d�ng� tekrar�...
    for arg�man in sys.argv[1:]:
        try: selsiy�s = �evir (arg�man)
        except ValueError: print ("{!r} bir say�sal veri de�ildir!" .format (arg�man), file=sys.stderr)
        else: print ("{} \N{DEGREE SIGN}F = {} \N{DEGREE SIGN}C" .format (arg�man, round (selsiy�s, 2)))

if __name__ == '__main__':
    anaProgram()