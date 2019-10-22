# coding:iso-8859-9 Türkçe
# p_30706.py: Farklı sayıda özne, sıfat, nesne ne fiillerden çeşitli tesadüfi cümle kurma örneği.

from random import choice as tercih

def kartezyenSeçim (*taranabilenler):
    sonuç = []
    for listem in taranabilenler: sonuç.append (tercih (listem))
    return sonuç+["."]

özne = ["Bu", "Şu", "O", "Diğer", "Öteki", "Beriki", "Bir"]
sıfat = ["kırmızı", "yeşil", "mavi", "sarı", "gri"]
nesne = ["araba", "ev", "balık", "ışık", "koç"]
fiil = ["kokuyor", "uyuyor", "gözkırpıyor", "yürüyor"]

cümle = kartezyenSeçim (özne, sıfat, nesne, fiil)
print ("Tesadüfi bir cümle:",  cümle)

print ("Tesadüfi (biçimli) bir cümle: ", end="")
for kelime in cümle: print (kelime, end=" ")



"""Çıktı:
>python p_30706.py
Tesadüfi bir cümle: ['Öteki', 'yeşil', 'balık', 'yürüyor', '.']
Tesadüfi (biçimli) bir cümle: Öteki yeşil balık yürüyor .

>python p_30706.py  ** TEKRAR **
Tesadüfi bir cümle: ['Şu', 'mavi', 'balık', 'uyuyor', '.']
Tesadüfi (biçimli) bir cümle: Şu mavi balık uyuyor .

>python p_30706.py  ** TEKRAR **
Tesadüfi bir cümle: ['Beriki', 'kırmızı', 'koç', 'kokuyor', '.']
Tesadüfi (biçimli) bir cümle: Beriki kırmızı koç kokuyor .
"""