# coding:iso-8859-9 "T�rk�e"

s�zl���m = dict (elma="ye�il", muz="sar�", kiraz="k�rm�z�")
print ("S�zl���mdeki element say�s�:", len (s�zl���m))
print ("S�zl���mdeki elementler:", s�zl���m)

s�zl���m["elma"] = "pembe"
print ("De�i�en s�zl���m i�eri�i:", s�zl���m)

s�zl���m["m�rm�reri�i"] = "mor"
print ("�laveli s�zl���m i�eri�i:", s�zl���m)

del (s�zl���m["muz"])
print ("Eksiltilen s�zl���m i�eri�i:", s�zl���m)
