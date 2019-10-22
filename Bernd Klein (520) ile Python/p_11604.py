# coding:iso-8859-9 T�rk�e
# p_11604.py: for-in-taranabilir'de de�i�meyen taranabilir[:] �rne�i.

renkler = ["k�rm�z�", "mavi"]
for i in renkler: # renkler listesi her d�ng�de artarak de�i�ti...
    if i == "k�rm�z�": renkler += ["siyah"]
    elif i == "mavi": renkler += ["sar�"]
    elif i == "siyah": renkler += ["beyaz"]
    elif i == "beyaz": renkler += ["ye�il"]
print ("Renkler listesi:", renkler)

renkler = ["k�rm�z�", "mavi"]
for i in renkler[:]:  # renkler listesi ilk haliyle kald�, her d�ng�de de�i�medi...
    if i == "k�rm�z�": renkler += ["siyah"]
    elif i == "mavi": renkler += ["sar�"]
    elif i == "siyah": renkler += ["beyaz"]
    elif i == "beyaz": renkler += ["ye�il"]
print ("Renkler listesi:", renkler)


"""��kt�:
>python p_11604.py
Renkler listesi: ['k�rm�z�', 'mavi', 'siyah', 'sar�', 'beyaz', 'ye�il']
Renkler listesi: ['k�rm�z�', 'mavi', 'siyah', 'sar�']
"""