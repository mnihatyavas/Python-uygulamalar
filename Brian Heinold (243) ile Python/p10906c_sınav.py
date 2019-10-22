# coding:iso-8859-9 Türkçe

sonuç = 0
sayı = fark = a = 1
while sayı:
    try: sayı = abs (eval (input ("Karekökü bulunacak sayıyı girin [0:Çık]: ")))
    except Exception: sayı = 5
    while fark > 1e-10:
        sonuç = (a + sayı / a) / 2
        fark = abs (sonuç - a)
        a = sonuç
    break
if sayı: print (sayı, "sayısının karekökü:", sonuç)
