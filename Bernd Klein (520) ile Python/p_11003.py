# coding:iso-8859-9 Türkçe
# p_11003.py: Değiştirilemez sözlük anahtarı olarak hangi veri tiplerinin kullanılabileceği örneği.

try: S = {[1,2,3]:"abc"}
except TypeError: print ("HATA: Mutable/değiştirilebilir liste'den anahtar olmaz!")

S = { (1,2,3):"abc", 3.1415:"pi", 123:123, "pi":3.1415, True:"Doğru"}
print ("\nDeğiştirilemez/immutable tüple'den ve sabit karakterlerden anahtar olur:", S)
print ("\nTüple değişmezi==> S[(1,2,3)]:", S[(1,2,3)], "\nKayannokta sabiti==> S[3.1415]:", S[3.1415],
    "\nTamsayı sabiti==> S[123]:", S[123], "\nDizge sabiti==> S['pi']:", S["pi"],
    "\nBoolean sabiti==> S[True]:", S[True] )


"""Çıktı:
>python p_11003.py
HATA: Mutable/değiştirilebilir liste'den anahtar olmaz!

Değiştirilemez/immutable tüple'den ve sabit karakterlerden anahtar olur:
{(1, 2, 3): 'abc', 3.1415: 'pi', 123: 123, 'pi': 3.1415, True: 'Doğru'}

Tüple değişmezi==> S[(1,2,3)]: abc
Kayannokta sabiti==> S[3.1415]: pi
Tamsayı sabiti==> S[123]: 123
Dizge sabiti==> S['pi']: 3.1415
Boolean sabiti==> S[True]: Doğru
"""