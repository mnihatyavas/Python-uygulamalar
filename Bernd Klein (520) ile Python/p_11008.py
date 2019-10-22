# coding:iso-8859-9 Türkçe
# p_11008.py: Sözlüklerde update/güncelle, zip/tüplede-birleştir ve tüple-liste-sözlük çevrimleri örneği.

sözlük1 = {"Sevim":{"JS"}, "Hatice":{"Java", "Python", "CSS"}, "Zeliha":{"ACCESS"} }
sözlük2 = {"Songül":{"HTML"}, "Hatice":{"WORD"}, "Nedim":{"MASM", "HTML", "JS", "CSS"}, "Sevim":{"HTML", "CSS"} }

sözlük1.update (sözlük2)
# Güncellemede 2.de de olan esas alınıyor ve ilki atılıyor, 2.yoksa ilki esas alınıyor; karma ekleme yapmıyor (sakat!)...

print ("Güncellenen sözlük:", sözlük1)
#----------------------------------------------------------------------------------------------------

print ("\nSadece anahtarların dökümü:")
for anahtar in sözlük1: print (anahtar, end=" ")
print()
for anahtar in sözlük1.keys(): print (anahtar, end=" ") # Aynı sonuç...
#----------------------------------------------------------------------------------------------------

print ("\n\nSadece değerlerin dökümü:")
for değer in sözlük1.values(): print (değer, end=" ")
print()
for anahtar in sözlük1.keys(): print (sözlük1[anahtar], end=" ") # Aynı sonuç, ancak ilki daha hızlıdır...
#----------------------------------------------------------------------------------------------------

print ("\n\nAnahtar-değer çiftinin birlikte dökümü:")
for çift in sözlük1.items(): print (çift, end=" ")
#----------------------------------------------------------------------------------------------------

print ("\n\nSözlükten listeye çevrim:")
L = list (sözlük1.items() )
print (L)
#----------------------------------------------------------------------------------------------------

print ("\nSözlük anahtar-değer çiftini 2 ayrı listeye ayırıp, " +
    "sonra zip'le birleşik tüple liste yapıp, " +
    "onu da dict'le tekrar sözlüğe çevirelim:\n", "-"*79, sep="")
L1 = list (sözlük1.keys() )
L2 = list (sözlük1.values() )
L3 = list (zip (L1, L2) )
S = dict (L3)
print ("Anahtarlar listesi:\n", L1, "\n\nDeğerler listesi:\n", L2,
    "\n\nBirleşik tüple listesi:\n", L3, "\n\nSözlük:\n", S, sep="")

print ("\nL1 ve L2 listeleriyle direk zip'ten sözlüğe çevrim:\n", dict (zip (L1, L2)), sep="")
# Zip'te listelerden kısası esas alınıp, artık kırpılır...

print ("\nListesiz direk zip'ten sözlüğe çevrim:\n", dict (zip (['Sevim', 'Hatice',
     'Zeliha', 'Songül', 'Nedim'], [{'CSS', 'HTML'}, {'WORD'}, {'ACCESS'},
    {'HTML'}, {'CSS', 'MASM', 'HTML', 'JS'}])), sep="")


"""Çıktı:
>python p_11008.py
Güncellenen sözlük: {'Sevim': {'CSS', 'HTML'}, 'Hatice': {'WORD'},
'Zeliha': {'ACCESS'}, 'Songül': {'HTML'}, 'Nedim': {'JS', 'CSS', 'HTML', 'MASM'}}

Sadece anahtarların dökümü:
Sevim Hatice Zeliha Songül Nedim
Sevim Hatice Zeliha Songül Nedim

Sadece değerlerin dökümü:
{'CSS', 'HTML'} {'WORD'} {'ACCESS'} {'HTML'} {'JS', 'CSS', 'HTML', 'MASM'}
{'CSS', 'HTML'} {'WORD'} {'ACCESS'} {'HTML'} {'JS', 'CSS', 'HTML', 'MASM'}

Anahtar-değer çiftinin birlikte dökümü:
('Sevim', {'CSS', 'HTML'}) ('Hatice', {'WORD'}) ('Zeliha', {'ACCESS'})
('Songül', {'HTML'}) ('Nedim', {'JS', 'CSS', 'HTML', 'MASM'})

Sözlükten listeye çevrim:
[('Sevim', {'CSS', 'HTML'}), ('Hatice', {'WORD'}), ('Zeliha', {'ACCESS'}),
('Songül', {'HTML'}), ('Nedim', {'JS', 'CSS', 'HTML', 'MASM'})]

Sözlük anahtar-değer çiftini 2 ayrı listeye ayırıp, sonra zip'le birleşik tüple
liste yapıp, onu da dict'le tekrar sözlüğe çevirelim:
-------------------------------------------------------------------------------
Anahtarlar listesi:
['Sevim', 'Hatice', 'Zeliha', 'Songül', 'Nedim']

Değerler listesi:
[{'CSS', 'HTML'}, {'WORD'}, {'ACCESS'}, {'HTML'}, {'JS', 'CSS', 'HTML', 'MASM'}]


Birleşik tüple listesi:
[('Sevim', {'CSS', 'HTML'}), ('Hatice', {'WORD'}), ('Zeliha', {'ACCESS'}),
('Songül', {'HTML'}), ('Nedim', {'JS', 'CSS', 'HTML', 'MASM'})]

Sözlük:
{'Sevim': {'CSS', 'HTML'}, 'Hatice': {'WORD'}, 'Zeliha': {'ACCESS'},
'Songül': {'HTML'}, 'Nedim': {'JS', 'CSS', 'HTML', 'MASM'}}

L1 ve L2 listeleriyle direk zip'ten sözlüğe çevrim:
{'Sevim': {'CSS', 'HTML'}, 'Hatice': {'WORD'}, 'Zeliha': {'ACCESS'},
'Songül': {'HTML'}, 'Nedim': {'JS', 'CSS', 'HTML', 'MASM'}}

Listesiz direk zip'ten sözlüğe çevrim:
{'Sevim': {'CSS', 'HTML'}, 'Hatice': {'WORD'}, 'Zeliha': {'ACCESS'},
'Songül': {'HTML'}, 'Nedim': {'JS', 'CSS', 'HTML', 'MASM'}}
"""