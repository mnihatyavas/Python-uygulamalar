# coding:iso-8859-9 Türkçe
# p_11006.py: Anahtarlı pop yerine anahtarsız sondan popitem() ile silme örneği.

başkentler = {"Türkiye":"Ankara", "KKTC":"Lefkoşe", "Yunanistan":"Atina",
    "Avusturya":"Viyana", "Almanya":"Berlin", "Hollanda":"Amsterdam",
    "İngiltere":"Londra", "Bulgaristan":"Sofya", "İtalya":"Roma"}
başkentler["Arnavutluk"] = "Tiran" # Yeni anahtar-değer çiftini sona ekler...

print (başkentler)

# popitem() sözlüğün sonundaki anahtar-değer (tüple-)çiftini çıkarır; hiç kalmamışsa KeyError istisnası fırlatır...

print()
ülke, başkent = başkentler.popitem()
print (başkent, ", ", ülke, "'un başşehridir\n", başkentler, sep="")

while True:
    print()
    try: print (başkentler.popitem(), "\n", başkentler, sep="")
    except KeyError:
        print ("Sözlükte popitem() çıkarılacak anahtar-değer çifti kalmamış!")
        break


"""Çıktı:
>python p_11006.py
{'Türkiye': 'Ankara', 'KKTC': 'Lefkoşe', 'Yunanistan': 'Atina', 'Avusturya': 'Viyana',
'Almanya': 'Berlin', 'Hollanda': 'Amsterdam', 'İngiltere': 'Londra', 'Bulgaristan': 'Sofya',
'İtalya': 'Roma', 'Arnavutluk': 'Tiran'}

Tiran, Arnavutluk'un başşehridir
{'Türkiye': 'Ankara', 'KKTC': 'Lefkoşe', 'Yunanistan': 'Atina', 'Avusturya': 'Viyana',
'Almanya': 'Berlin', 'Hollanda': 'Amsterdam', 'İngiltere': 'Londra', 'Bulgaristan': 'Sofya', 'İtalya': 'Roma'}

('İtalya', 'Roma')
{'Türkiye': 'Ankara', 'KKTC': 'Lefkoşe', 'Yunanistan': 'Atina', 'Avusturya': 'Viyana',
'Almanya': 'Berlin', 'Hollanda': 'Amsterdam', 'İngiltere': 'Londra', 'Bulgaristan': 'Sofya'}

('Bulgaristan', 'Sofya')
{'Türkiye': 'Ankara', 'KKTC': 'Lefkoşe', 'Yunanistan': 'Atina', 'Avusturya': 'Viyana',
'Almanya': 'Berlin', 'Hollanda': 'Amsterdam', 'İngiltere': 'Londra'}

('İngiltere', 'Londra')
{'Türkiye': 'Ankara', 'KKTC': 'Lefkoşe', 'Yunanistan': 'Atina', 'Avusturya': 'Viyana',
'Almanya': 'Berlin', 'Hollanda': 'Amsterdam'}

('Hollanda', 'Amsterdam')
{'Türkiye': 'Ankara', 'KKTC': 'Lefkoşe', 'Yunanistan': 'Atina', 'Avusturya': 'Viyana',
'Almanya': 'Berlin'}

('Almanya', 'Berlin')
{'Türkiye': 'Ankara', 'KKTC': 'Lefkoşe', 'Yunanistan': 'Atina', 'Avusturya': 'Vi
yana'}

('Avusturya', 'Viyana')
{'Türkiye': 'Ankara', 'KKTC': 'Lefkoşe', 'Yunanistan': 'Atina'}

('Yunanistan', 'Atina')
{'Türkiye': 'Ankara', 'KKTC': 'Lefkoşe'}

('KKTC', 'Lefkoşe')
{'Türkiye': 'Ankara'}

('Türkiye', 'Ankara')
{}

Sözlükte popitem() çıkarılacak anahtar-değer çifti kalmamış!
"""