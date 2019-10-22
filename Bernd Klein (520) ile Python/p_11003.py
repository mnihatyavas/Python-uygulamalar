# coding:iso-8859-9 T�rk�e
# p_11003.py: De�i�tirilemez s�zl�k anahtar� olarak hangi veri tiplerinin kullan�labilece�i �rne�i.

try: S = {[1,2,3]:"abc"}
except TypeError: print ("HATA: Mutable/de�i�tirilebilir liste'den anahtar olmaz!")

S = { (1,2,3):"abc", 3.1415:"pi", 123:123, "pi":3.1415, True:"Do�ru"}
print ("\nDe�i�tirilemez/immutable t�ple'den ve sabit karakterlerden anahtar olur:", S)
print ("\nT�ple de�i�mezi==> S[(1,2,3)]:", S[(1,2,3)], "\nKayannokta sabiti==> S[3.1415]:", S[3.1415],
    "\nTamsay� sabiti==> S[123]:", S[123], "\nDizge sabiti==> S['pi']:", S["pi"],
    "\nBoolean sabiti==> S[True]:", S[True] )


"""��kt�:
>python p_11003.py
HATA: Mutable/de�i�tirilebilir liste'den anahtar olmaz!

De�i�tirilemez/immutable t�ple'den ve sabit karakterlerden anahtar olur:
{(1, 2, 3): 'abc', 3.1415: 'pi', 123: 123, 'pi': 3.1415, True: 'Do�ru'}

T�ple de�i�mezi==> S[(1,2,3)]: abc
Kayannokta sabiti==> S[3.1415]: pi
Tamsay� sabiti==> S[123]: 123
Dizge sabiti==> S['pi']: 3.1415
Boolean sabiti==> S[True]: Do�ru
"""