# coding:iso-8859-9 T�rk�e
# p_13412a.py: send-yield ile 1->10 ��renci notlar� ortalamas� �reteci �rne�i.

print ("��renci notlar�n�n ortalamas� �reteci:", "\n", "-"*48, sep="")

def ortalama():
    toplam = 0.0
    saya� = 0
    ort = None
    while True:
        terim = yield ort
        toplam += terim
        saya� += 1
        ort = toplam / saya�


y = ortalama()
next (y) # �lk None yield'i i�letir...
i = 1
for j in [77.65, 39.43, 67, 100, 82.6, 93.54, 35.41, 54.9, 71.7, 99.99]:
    sonu� = "{a:2d}.not: {b:6.2f}, toplam {c:2d} notlu ortalama: {d:6.2f}"
    print (sonu� .format (a=i, b=j, c=i, d=y.send (j)) )
    i +=1

"""��kt�:
>python p_13412a.py
��renci notlar�n�n ortalamas� �reteci:
------------------------------------------------
 1.not:  77.65, toplam  1 notlu ortalama:  77.65
 2.not:  39.43, toplam  2 notlu ortalama:  58.54
 3.not:  67.00, toplam  3 notlu ortalama:  61.36
 4.not: 100.00, toplam  4 notlu ortalama:  71.02
 5.not:  82.60, toplam  5 notlu ortalama:  73.34
 6.not:  93.54, toplam  6 notlu ortalama:  76.70
 7.not:  35.41, toplam  7 notlu ortalama:  70.80
 8.not:  54.90, toplam  8 notlu ortalama:  68.82
 9.not:  71.70, toplam  9 notlu ortalama:  69.14
10.not:  99.99, toplam 10 notlu ortalama:  72.22
"""