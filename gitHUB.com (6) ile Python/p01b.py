# coding:iso-8859-9 T�rk�e
# Komut iletisinden girilen t�m Selsiy�s dereceyi Fahrenhayt dereceye �evirir...

import sys

def �evir (dizge):
    """(dizge): float
    Komut iletisinden arg�man olarak girilen Selsiy�s float dizgesini
    a�a��daki form�lle bir Fahranhayt derecesine �evirir. Arg�man girilmez
    ya da yanl�� girilirse kullan�c�ya bildirilir...
    """
    selsiy�s = float (dizge)
    fahrenhayt = 9 / 5 * selsiy�s +  32
    return fahrenhayt

def anaProgram():
    # �ayet S argv unutulmu�sa hat�rlat�lmal�d�r...
    if len (sys.argv) == 1:
        print ("{} ..[Unutulan arg�manlar: S1 S2 ...]" .format (sys.argv[0]))
        sys.exit (0)

    # Arg�man say�s� kadar d�ng� tekrar�...
    for arg�man in sys.argv[1:]:
        try: fahrenhayt = �evir (arg�man)
        except ValueError: print ("'{}' bir say�sal veri de�ildir!" .format (arg�man), file=sys.stderr)
        else: print ("{} \N{DEGREE SIGN}C = {} \N{DEGREE SIGN}F" .format (arg�man, round (fahrenhayt, 2)))

if __name__ == '__main__':
    anaProgram()