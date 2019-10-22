#coding:iso-8859-9 Türkçe
# p_11903.py: **sözlük formatıyla sözlük anahtar ve değerlerinin yazdırılması örneği.

print ("{1:s}'nin başkenti {0:s}'dır." .format ("Ankara", "Türkiye") )
print ("{ülke:s}'nin başkenti {şehir:s}'dır." .format (şehir="Ankara", ülke="Türkiye") )

sözlük = dict (şehir="Ankara", ülke="Türkiye")
print ("\nSözlük =", sözlük)
print ("{ülke:s}'nin başkenti {şehir:s}'dır." .format (**sözlük) )
#-----------------------------------------------------------------------------------------------------------

sözlük = {"Türkiye": "Ankara",
    "Gürcistan": "Tiflis",
    "Ermenistan": "Erivan",
    "Nağcivan": "Nağcivan",
    "İran": "Tahran",
    "Irak": "Bağdat",
    "Suriye": "Şam",
    "KKTC": "Lefkoşe",
    "Yunanistan": "Atina",
    "Bulgaristan": "Sofya",
    "Ukrayna": "Kiev"}

print ("\nTürkiye'nin ve komşularının başşehirleri sözlük dökümü:")
for ülke in sözlük.keys():
    print ("{ülke:s}'nin başkenti {şehir:s}'dır." .format (şehir=sözlük[ülke], ülke=ülke) )

print ("\nAynı sözlük dökümünün farklı yorumu:")
for ülke in sözlük.keys():
    dizge = ülke + ": {" + ülke + "}"
    print (dizge .format (**sözlük) )


"""Çıktı:
>python p_11903.py
Türkiye'nin başkenti Ankara'dır.
Türkiye'nin başkenti Ankara'dır.

Sözlük = {'şehir': 'Ankara', 'ülke': 'Türkiye'}
Türkiye'nin başkenti Ankara'dır.

Türkiye'nin ve komşularının başşehirleri sözlük dökümü:
Türkiye'nin başkenti Ankara'dır.
Gürcistan'nin başkenti Tiflis'dır.
Ermenistan'nin başkenti Erivan'dır.
Nağcivan'nin başkenti Nağcivan'dır.
İran'nin başkenti Tahran'dır.
Irak'nin başkenti Bağdat'dır.
Suriye'nin başkenti Şam'dır.
KKTC'nin başkenti Lefkoşe'dır.
Yunanistan'nin başkenti Atina'dır.
Bulgaristan'nin başkenti Sofya'dır.
Ukrayna'nin başkenti Kiev'dır.

Aynı sözlük dökümünün farklı yorumu:
Türkiye: Ankara
Gürcistan: Tiflis
Ermenistan: Erivan
Nağcivan: Nağcivan
İran: Tahran
Irak: Bağdat
Suriye: Şam
KKTC: Lefkoşe
Yunanistan: Atina
Bulgaristan: Sofya
Ukrayna: Kiev
"""