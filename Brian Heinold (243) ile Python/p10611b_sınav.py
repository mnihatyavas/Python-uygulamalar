# coding:iso-8859-9 T�rk�e

teklif1 = "Say�n "
teklif2 = "\n\nSize yeni Platin Art� �kramiyeli kart�m�z� %47.99 gibi\n�ok �zel bir tan�t�m indirimiyle sunmaktan gurur duyuyorum.\n"
teklif3 = ", b�yle bir teklif kimseye her g�n pek s�k yap�lmaz;\nbu y�zden +90-800-314-1592 �cretsiz numaram�z� hemen\naraman�z� �iddetle tavsiye ediyorum.\nB�ylesi indirimli tan�t�m kampanya indirimini �ok uzun s�re devam\nettiremeyiz, "
teklif4 = ", bu y�zden hi� vakit yitirmeden\nhemen bizi aramal�s�n�z!.."

giri� = input ("A��k ad soyad�n�z� giriniz: ")
if len(giri�) > 0:
    try: ad = giri�[:giri�.index(' ')]
    except ValueError: ad = giri�
    print (teklif1, giri�, teklif2, ad, teklif3, ad, teklif4, sep="")
