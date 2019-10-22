# coding:iso-8859-9 T�rk�e
# p_13205.py: Fibonaki serisinin lambda fonksiyonla tek ve �ift olarak ayr��t�r�lmas� �rne�i.

fibonaki = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597]

tekSay�lar = list (filter (lambda x: x % 2, fibonaki)) # x%2 kalan� 1=tekse True, 0=�iftse False �retir...
�iftSay�lar = list (filter (lambda x: x % 2 == 0, fibonaki)) # E�itlik �ift say�larda sa�land���nda True �retir...
# Veya: �iftSay�lar = list (filter (lambda x: x % 2 -1, fibonaki))

print ("Filitrelenen fibonaki �ifli say�lar� listesi:", �iftSay�lar)
print ("Filitrelenen fibonaki tekli say�lar� listesi:", tekSay�lar)

"""��kt�
>python p_13205.py
Filitrelenen fibonaki �ifli say�lar� listesi: [0, 2, 8, 34, 144, 610]
Filitrelenen fibonaki tekli say�lar� listesi: [1, 1, 3, 5, 13, 21, 55, 89, 233,377, 987, 1597]
"""