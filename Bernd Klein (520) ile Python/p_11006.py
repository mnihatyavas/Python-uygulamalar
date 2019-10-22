# coding:iso-8859-9 T�rk�e
# p_11006.py: Anahtarl� pop yerine anahtars�z sondan popitem() ile silme �rne�i.

ba�kentler = {"T�rkiye":"Ankara", "KKTC":"Lefko�e", "Yunanistan":"Atina",
    "Avusturya":"Viyana", "Almanya":"Berlin", "Hollanda":"Amsterdam",
    "�ngiltere":"Londra", "Bulgaristan":"Sofya", "�talya":"Roma"}
ba�kentler["Arnavutluk"] = "Tiran" # Yeni anahtar-de�er �iftini sona ekler...

print (ba�kentler)

# popitem() s�zl���n sonundaki anahtar-de�er (t�ple-)�iftini ��kar�r; hi� kalmam��sa KeyError istisnas� f�rlat�r...

print()
�lke, ba�kent = ba�kentler.popitem()
print (ba�kent, ", ", �lke, "'un ba��ehridir\n", ba�kentler, sep="")

while True:
    print()
    try: print (ba�kentler.popitem(), "\n", ba�kentler, sep="")
    except KeyError:
        print ("S�zl�kte popitem() ��kar�lacak anahtar-de�er �ifti kalmam��!")
        break


"""��kt�:
>python p_11006.py
{'T�rkiye': 'Ankara', 'KKTC': 'Lefko�e', 'Yunanistan': 'Atina', 'Avusturya': 'Viyana',
'Almanya': 'Berlin', 'Hollanda': 'Amsterdam', '�ngiltere': 'Londra', 'Bulgaristan': 'Sofya',
'�talya': 'Roma', 'Arnavutluk': 'Tiran'}

Tiran, Arnavutluk'un ba��ehridir
{'T�rkiye': 'Ankara', 'KKTC': 'Lefko�e', 'Yunanistan': 'Atina', 'Avusturya': 'Viyana',
'Almanya': 'Berlin', 'Hollanda': 'Amsterdam', '�ngiltere': 'Londra', 'Bulgaristan': 'Sofya', '�talya': 'Roma'}

('�talya', 'Roma')
{'T�rkiye': 'Ankara', 'KKTC': 'Lefko�e', 'Yunanistan': 'Atina', 'Avusturya': 'Viyana',
'Almanya': 'Berlin', 'Hollanda': 'Amsterdam', '�ngiltere': 'Londra', 'Bulgaristan': 'Sofya'}

('Bulgaristan', 'Sofya')
{'T�rkiye': 'Ankara', 'KKTC': 'Lefko�e', 'Yunanistan': 'Atina', 'Avusturya': 'Viyana',
'Almanya': 'Berlin', 'Hollanda': 'Amsterdam', '�ngiltere': 'Londra'}

('�ngiltere', 'Londra')
{'T�rkiye': 'Ankara', 'KKTC': 'Lefko�e', 'Yunanistan': 'Atina', 'Avusturya': 'Viyana',
'Almanya': 'Berlin', 'Hollanda': 'Amsterdam'}

('Hollanda', 'Amsterdam')
{'T�rkiye': 'Ankara', 'KKTC': 'Lefko�e', 'Yunanistan': 'Atina', 'Avusturya': 'Viyana',
'Almanya': 'Berlin'}

('Almanya', 'Berlin')
{'T�rkiye': 'Ankara', 'KKTC': 'Lefko�e', 'Yunanistan': 'Atina', 'Avusturya': 'Vi
yana'}

('Avusturya', 'Viyana')
{'T�rkiye': 'Ankara', 'KKTC': 'Lefko�e', 'Yunanistan': 'Atina'}

('Yunanistan', 'Atina')
{'T�rkiye': 'Ankara', 'KKTC': 'Lefko�e'}

('KKTC', 'Lefko�e')
{'T�rkiye': 'Ankara'}

('T�rkiye', 'Ankara')
{}

S�zl�kte popitem() ��kar�lacak anahtar-de�er �ifti kalmam��!
"""