# coding:iso-8859-9
# p_13806b.py: @classmethod'la kopya s�n�f nesnelerin de�i�en tip �zelliklerinin aktar�labilmesi �rne�i.

class Evciller:
    ad = "evcil hayvanlar"
    @classmethod
    def hakk�nda (s�n�f): print ("Bu s�n�f {} hakk�ndad�r!" .format (s�n�f.ad) )   

class K�pekler (Evciller): ad = "insanlar�n en sad�k arkada�� olan k�pekler"
class Kediler (Evciller): ad = "insan�n ayaklar� dibinden ayr�lmayan kediler"
class Ku�lar (Evciller): ad = "insan�n omuzlar�nda �ak�yan muhabbet ku�lar�"

e = Evciller()
e.hakk�nda()

k� = K�pekler()
k�.hakk�nda()

ke = Kediler()
ke.hakk�nda()

ku = Ku�lar()
ku.hakk�nda()



"""��kt�:
>python p_13806b.py
Bu s�n�f evcil hayvanlar hakk�ndad�r!
Bu s�n�f insanlar�n en sad�k arkada�� olan k�pekler hakk�ndad�r!
Bu s�n�f insan�n ayaklar� dibinden ayr�lmayan kediler hakk�ndad�r!
Bu s�n�f insan�n omuzlar�nda �ak�yan muhabbet ku�lar� hakk�ndad�r!
"""