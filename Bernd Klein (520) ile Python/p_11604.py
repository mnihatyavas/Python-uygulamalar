# coding:iso-8859-9 Türkçe
# p_11604.py: for-in-taranabilir'de değişmeyen taranabilir[:] örneği.

renkler = ["kırmızı", "mavi"]
for i in renkler: # renkler listesi her döngüde artarak değişti...
    if i == "kırmızı": renkler += ["siyah"]
    elif i == "mavi": renkler += ["sarı"]
    elif i == "siyah": renkler += ["beyaz"]
    elif i == "beyaz": renkler += ["yeşil"]
print ("Renkler listesi:", renkler)

renkler = ["kırmızı", "mavi"]
for i in renkler[:]:  # renkler listesi ilk haliyle kaldı, her döngüde değişmedi...
    if i == "kırmızı": renkler += ["siyah"]
    elif i == "mavi": renkler += ["sarı"]
    elif i == "siyah": renkler += ["beyaz"]
    elif i == "beyaz": renkler += ["yeşil"]
print ("Renkler listesi:", renkler)


"""Çıktı:
>python p_11604.py
Renkler listesi: ['kırmızı', 'mavi', 'siyah', 'sarı', 'beyaz', 'yeşil']
Renkler listesi: ['kırmızı', 'mavi', 'siyah', 'sarı']
"""