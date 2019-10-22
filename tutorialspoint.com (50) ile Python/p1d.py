# coding:iso-8859-9 Türkçe

kelime = 'kelime'
cümle = "Bu, büyükharfle başlayıp noktayla biten tek satırlık bir cümledir."
paragraf = """Bu ise bir paragraftır.
Bir cümle 2 tırnak arasındaki tek satırlık metinken,
bir paragraf birden çok satırlık metinden oluşabilir.
Paragraf başlangıcı 3 tırnakla başlar ve
bitişi de yine 3 tırnakla olmalıdır."""

# Tek satırlık yorumumuz...
print (kelime, "\n") # Bu da bir yorumdur...
print (cümle, "\n")
print (paragraf)

# Python'da çoklu yorum satırı sembolü yoktur.
# Çoklu yorum satırı gireceksek,
# herbir yorum satırını teker teker yazmalıyız.

input ("\n\nDevam için Ent tuşuna basın: ")

import sys; x = 'çoklu ifade satırı'; sys.stdout.write (x + '\n') # print(..) ile aynıdır...
