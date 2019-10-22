# coding:iso-8859-9 Türkçe
# p_12007.py: **parametrik veya **argümansal sözlük aktarımlı fonksiyonlar örneği.

def f (**parametreler):
    # Anahtar kelimeli değişken sayıda ve tipte argümanları kabul eder...
    print (parametreler)

f() # Argümansız...
f (en="İngilizce", fr="Fransızca", de="Almanca", ar="Arapça", ru="Rusça", zh="Çince", ja="Japonca", tr="Türkçe")
f (yıl=1957, ay=4, gün=17, doğum_yeri="Yeşilyurt")
#---------------------------------------------------------------------------------------------------------

def f (e, d, s, h, f, ç): print (d, e, h, s, ç, f)

# Parametrik isimle istenilen düzenlemede ve tipte argüman atanabilir...
d = {'e':'ekle', "s":"sil", 'f':'fermuarla', 'ç':'çöz', 'h':'hayır', "d": "dosya"}
print()
f (**d)
f (4, 17, "Yeşilyurt", 1957, "M.Nihat Yavaş", "Malatya")


"""Çıktı:
>python p_12007.py
{}
{'en': 'İngilizce', 'fr': 'Fransızca', 'de': 'Almanca', 'ar': 'Arapça',
'ru': 'Rusça', 'zh': 'Çince', 'ja': 'Japonca', 'tr': 'Türkçe'}
{'yıl': 1957, 'ay': 4, 'gün': 17, 'doğum_yeri': 'Yeşilyurt'}

dosya ekle hayır sil çöz fermuarla
17 4 1957 Yeşilyurt Malatya M.Nihat Yavaş
"""