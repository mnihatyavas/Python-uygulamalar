# coding:iso-8859-9 T�rk�e
# p_30706.py: Farkl� say�da �zne, s�fat, nesne ne fiillerden �e�itli tesad�fi c�mle kurma �rne�i.

from random import choice as tercih

def kartezyenSe�im (*taranabilenler):
    sonu� = []
    for listem in taranabilenler: sonu�.append (tercih (listem))
    return sonu�+["."]

�zne = ["Bu", "�u", "O", "Di�er", "�teki", "Beriki", "Bir"]
s�fat = ["k�rm�z�", "ye�il", "mavi", "sar�", "gri"]
nesne = ["araba", "ev", "bal�k", "���k", "ko�"]
fiil = ["kokuyor", "uyuyor", "g�zk�rp�yor", "y�r�yor"]

c�mle = kartezyenSe�im (�zne, s�fat, nesne, fiil)
print ("Tesad�fi bir c�mle:",  c�mle)

print ("Tesad�fi (bi�imli) bir c�mle: ", end="")
for kelime in c�mle: print (kelime, end=" ")



"""��kt�:
>python p_30706.py
Tesad�fi bir c�mle: ['�teki', 'ye�il', 'bal�k', 'y�r�yor', '.']
Tesad�fi (bi�imli) bir c�mle: �teki ye�il bal�k y�r�yor .

>python p_30706.py  ** TEKRAR **
Tesad�fi bir c�mle: ['�u', 'mavi', 'bal�k', 'uyuyor', '.']
Tesad�fi (bi�imli) bir c�mle: �u mavi bal�k uyuyor .

>python p_30706.py  ** TEKRAR **
Tesad�fi bir c�mle: ['Beriki', 'k�rm�z�', 'ko�', 'kokuyor', '.']
Tesad�fi (bi�imli) bir c�mle: Beriki k�rm�z� ko� kokuyor .
"""