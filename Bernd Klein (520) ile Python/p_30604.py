# coding:iso-8859-9 T�rk�e

from random import SystemRandom
# p_30604.py: SystemRandom() ile istenilen uzunlukta verili tesad�fi karakter se�imli �ifre �retme �rne�i.

kripto = SystemRandom() # SystemRandom s�n�f�n�n bir tipleme nesnesini yarat�r...

def �ifre�retici (�ifreUzunlu�u, kullan�labilirKarakterler=None):
    if kullan�labilirKarakterler==None:
        kullan�labilirKarakterler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        kullan�labilirKarakterler += kullan�labilirKarakterler.lower() + "0123456789"
    uz = len (kullan�labilirKarakterler)-1
    �ifrem = ""
    saya� = 0
    while saya� < �ifreUzunlu�u:
        #tesad�fi0_255Say� = kripto.randint (0, 256)
        #krk = chr (tesad�fi0_255Say�)
        #if krk in kullan�labilirKarakterler: �ifrem += chr (tesad�fi0_255Say�)
        �ifrem += kullan�labilirKarakterler [kripto.randint (0, uz)]
        saya� += 1
    return �ifrem

print ("Python taraf�ndan otomatik �retilen g�venli �ifre: " + �ifre�retici (15, "ABC�DEFG�HI�JKLMNO�PQRS�TU�VWXYZbc�defg�h�ijklmno�pqrs�tu�vwxyz0123456789") )


"""��kt�:
>python p_30604.py
Python taraf�ndan otomatik �retilen g�venli �ifre: oq1�W�kptcP�Y9p

>python p_30604.py  ** TEKRAR **
Python taraf�ndan otomatik �retilen g�venli �ifre: 4X�TpME�1JBfCj2

>python p_30604.py  ** TEKRAR **
Python taraf�ndan otomatik �retilen g�venli �ifre: 9Hv9Qm�HXW�ETQh
"""