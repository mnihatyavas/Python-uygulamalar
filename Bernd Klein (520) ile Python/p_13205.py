# coding:iso-8859-9 Türkçe
# p_13205.py: Fibonaki serisinin lambda fonksiyonla tek ve çift olarak ayrıştırılması örneği.

fibonaki = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597]

tekSayılar = list (filter (lambda x: x % 2, fibonaki)) # x%2 kalanı 1=tekse True, 0=çiftse False üretir...
çiftSayılar = list (filter (lambda x: x % 2 == 0, fibonaki)) # Eşitlik çift sayılarda sağlandığında True üretir...
# Veya: çiftSayılar = list (filter (lambda x: x % 2 -1, fibonaki))

print ("Filitrelenen fibonaki çifli sayıları listesi:", çiftSayılar)
print ("Filitrelenen fibonaki tekli sayıları listesi:", tekSayılar)

"""Çıktı
>python p_13205.py
Filitrelenen fibonaki çifli sayıları listesi: [0, 2, 8, 34, 144, 610]
Filitrelenen fibonaki tekli sayıları listesi: [1, 1, 3, 5, 13, 21, 55, 89, 233,377, 987, 1597]
"""