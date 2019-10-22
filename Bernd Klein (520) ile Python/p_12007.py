# coding:iso-8859-9 T�rk�e
# p_12007.py: **parametrik veya **arg�mansal s�zl�k aktar�ml� fonksiyonlar �rne�i.

def f (**parametreler):
    # Anahtar kelimeli de�i�ken say�da ve tipte arg�manlar� kabul eder...
    print (parametreler)

f() # Arg�mans�z...
f (en="�ngilizce", fr="Frans�zca", de="Almanca", ar="Arap�a", ru="Rus�a", zh="�ince", ja="Japonca", tr="T�rk�e")
f (y�l=1957, ay=4, g�n=17, do�um_yeri="Ye�ilyurt")
#---------------------------------------------------------------------------------------------------------

def f (e, d, s, h, f, �): print (d, e, h, s, �, f)

# Parametrik isimle istenilen d�zenlemede ve tipte arg�man atanabilir...
d = {'e':'ekle', "s":"sil", 'f':'fermuarla', '�':'��z', 'h':'hay�r', "d": "dosya"}
print()
f (**d)
f (4, 17, "Ye�ilyurt", 1957, "M.Nihat Yava�", "Malatya")


"""��kt�:
>python p_12007.py
{}
{'en': '�ngilizce', 'fr': 'Frans�zca', 'de': 'Almanca', 'ar': 'Arap�a',
'ru': 'Rus�a', 'zh': '�ince', 'ja': 'Japonca', 'tr': 'T�rk�e'}
{'y�l': 1957, 'ay': 4, 'g�n': 17, 'do�um_yeri': 'Ye�ilyurt'}

dosya ekle hay�r sil ��z fermuarla
17 4 1957 Ye�ilyurt Malatya M.Nihat Yava�
"""