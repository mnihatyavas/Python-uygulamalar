# coding:iso-8859-9 Türkçe
# p_13412c.py: Tüpleli ve formatlı 0->24 sonrası yenibaştanlı zaman üreteci örneği.

print ("Yenibaştanlı (saat,dakika,saniye) artan-adet-kapsamlı zaman tüpleli üreteç çıktısı:", "\n", "-"*79, sep="")

def üreteç (ilk, son, artış):
    zaman = list (ilk)
    while zaman < list (son):
        yenibaştan = yield tuple (zaman)
        if yenibaştan != None:
            zaman = list (yenibaştan)
            continue
        saniye = artış[2] + zaman[2]
        dakikayaEkle = 0
        saataEkle = 0
        if saniye < 60: zaman[2] = saniye
        else:
            zaman[2] = saniye - 60
            dakikayaEkle = 1
        dakika = artış[1] + zaman[1] + dakikayaEkle
        if dakika < 60: zaman[1] = dakika 
        else:
            zaman[1] = dakika - 60
            saataEkle = 1
        saat = artış[0] + zaman[0] + saataEkle
        if saat < 24: zaman[0] = saat 
        else: zaman[0] = saat -24

if __name__ == "__main__":           
    kıstaslar = üreteç ((12, 0, 0), (23, 45, 15), (0, 15, 20) )  
    for i in range (46): print (next (kıstaslar) )

    print ("\nYeniden başlat:", kıstaslar.send ((0, 0, 0)) )
    for _ in range (46):
        a = next (kıstaslar)
        print ("{:02d}:{:02d}:{:02d}" .format (a[0], a[1], a[2]) )

"""Çıktı:
>python p_13412c.py
Yenibaştanlı (saat,dakika,saniye) artan-adet-kapsamlı zaman tüpleli üreteç çıktısı:
-------------------------------------------------------------------------------
(12, 0, 0)
(12, 15, 20)
(12, 30, 40)
(12, 46, 0)
(13, 1, 20)
(13, 16, 40)
(13, 32, 0)
(13, 47, 20)
(14, 2, 40)
(14, 18, 0)
(14, 33, 20)
(14, 48, 40)
(15, 4, 0)
(15, 19, 20)
(15, 34, 40)
(15, 50, 0)
(16, 5, 20)
(16, 20, 40)
(16, 36, 0)
(16, 51, 20)
(17, 6, 40)
(17, 22, 0)
(17, 37, 20)
(17, 52, 40)
(18, 8, 0)
(18, 23, 20)
(18, 38, 40)
(18, 54, 0)
(19, 9, 20)
(19, 24, 40)
(19, 40, 0)
(19, 55, 20)
(20, 10, 40)
(20, 26, 0)
(20, 41, 20)
(20, 56, 40)
(21, 12, 0)
(21, 27, 20)
(21, 42, 40)
(21, 58, 0)
(22, 13, 20)
(22, 28, 40)
(22, 44, 0)
(22, 59, 20)
(23, 14, 40)
(23, 30, 0)

Yeniden başlat: (0, 0, 0)
00:15:20
00:30:40
00:46:00
01:01:20
01:16:40
01:32:00
01:47:20
02:02:40
02:18:00
02:33:20
02:48:40
03:04:00
03:19:20
03:34:40
03:50:00
04:05:20
04:20:40
04:36:00
04:51:20
05:06:40
05:22:00
05:37:20
05:52:40
06:08:00
06:23:20
06:38:40
06:54:00
07:09:20
07:24:40
07:40:00
07:55:20
08:10:40
08:26:00
08:41:20
08:56:40
09:12:00
09:27:20
09:42:40
09:58:00
10:13:20
10:28:40
10:44:00
10:59:20
11:14:40
11:30:00
11:45:20
"""