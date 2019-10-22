# coding:iso-8859-9 Türkçe
# Komut iletisinden girilen tüm F dereceyi C dereceye çevirir...

import sys

def çevir (S):
    """(dizge): float
    Komut iletisinden argüman olarak girilen Fahrenhayt float dizgesini
    aşağıdaki formülle bir Selsiyüs derecesine çevirir. Argüman girilmez
    yada yanlış girilirse kullanıcıya bildirilir...
    """
    fahrenhayt = float (S)
    selsiyüs = (fahrenhayt - 32) * 5 / 9
    return selsiyüs

def anaProgram():
    # Şayet F argv unutulmuşsa hatırlatılmalıdır...
    if len (sys.argv) == 1:
        print ("{} ..[Unutulan argümanlar: F1 F2 ...]" .format (sys.argv[0]))
        sys.exit (0)

    # Argüman sayısı kadar döngü tekrarı...
    for argüman in sys.argv[1:]:
        try: selsiyüs = çevir (argüman)
        except ValueError: print ("{!r} bir sayısal veri değildir!" .format (argüman), file=sys.stderr)
        else: print ("{} \N{DEGREE SIGN}F = {} \N{DEGREE SIGN}C" .format (argüman, round (selsiyüs, 2)))

if __name__ == '__main__':
    anaProgram()