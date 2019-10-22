# coding:iso-8859-9 Türkçe
# Komut iletisinden girilen tüm Selsiyüs dereceyi Fahrenhayt dereceye çevirir...

import sys

def çevir (dizge):
    """(dizge): float
    Komut iletisinden argüman olarak girilen Selsiyüs float dizgesini
    aşağıdaki formülle bir Fahranhayt derecesine çevirir. Argüman girilmez
    ya da yanlış girilirse kullanıcıya bildirilir...
    """
    selsiyüs = float (dizge)
    fahrenhayt = 9 / 5 * selsiyüs +  32
    return fahrenhayt

def anaProgram():
    # Şayet S argv unutulmuşsa hatırlatılmalıdır...
    if len (sys.argv) == 1:
        print ("{} ..[Unutulan argümanlar: S1 S2 ...]" .format (sys.argv[0]))
        sys.exit (0)

    # Argüman sayısı kadar döngü tekrarı...
    for argüman in sys.argv[1:]:
        try: fahrenhayt = çevir (argüman)
        except ValueError: print ("'{}' bir sayısal veri değildir!" .format (argüman), file=sys.stderr)
        else: print ("{} \N{DEGREE SIGN}C = {} \N{DEGREE SIGN}F" .format (argüman, round (fahrenhayt, 2)))

if __name__ == '__main__':
    anaProgram()