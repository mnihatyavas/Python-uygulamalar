# coding:iso-8859-9 Türkçe
# p_13412b.py: 0->24 arası 15dk-25sn aralarla tüpleli sonsuz zaman üreteci örneği.

def üreteç (ilk, son, artış):
    aktüel = list (ilk)
    while aktüel < list (son):
        yield tuple (aktüel)
        saniye = artış[2] + aktüel[2]
        dakikayaEkle = 0
        saataEkle = 0
        if saniye < 60: aktüel[2] = saniye
        else:
            aktüel[2] = saniye - 60
            dakikayaEkle = 1
        dakika = aktüel[1] + artış[1] + dakikayaEkle
        if dakika < 60: aktüel[1] = dakika
        else:
            aktüel[1] = dakika - 60
            saataEkle = 1
        saat = aktüel[0] + artış[0] + saataEkle
        if saat < 24:aktüel[0] = saat
        else: aktüel[0] = saat -24

if __name__ == "__main__":
    # yield None olmadığından direkt değer üretimine geçilebilir....
    print ("(saat,dakika,saniye) artan-sonlu zaman tüpleli üreteç çıktısı:", "\n", "-"*62, sep="")
    for zaman in üreteç ((0, 0, 0), (23, 50, 15), (0, 15, 25) ):
        print("{:02d}:{:02d}:{:02d}" .format (zaman[0], zaman[1], zaman[2]) )

"""Çıktı:
>python p_13412b.py
(saat,dakika,saniye) artan-sonlu zaman tüpleli üreteç çıktısı:
--------------------------------------------------------------
00:00:00
00:15:25
00:30:50
00:46:15
01:01:40
01:17:05
01:32:30
01:47:55
02:03:20
02:18:45
02:34:10
02:49:35
03:05:00
03:20:25
03:35:50
03:51:15
04:06:40
04:22:05
04:37:30
04:52:55
05:08:20
05:23:45
05:39:10
05:54:35
06:10:00
06:25:25
06:40:50
06:56:15
07:11:40
07:27:05
07:42:30
07:57:55
08:13:20
08:28:45
08:44:10
08:59:35
09:15:00
09:30:25
09:45:50
10:01:15
10:16:40
10:32:05
10:47:30
11:02:55
11:18:20
11:33:45
11:49:10
12:04:35
12:20:00
12:35:25
12:50:50
13:06:15
13:21:40
13:37:05
13:52:30
14:07:55
14:23:20
14:38:45
14:54:10
15:09:35
15:25:00
15:40:25
15:55:50
16:11:15
16:26:40
16:42:05
16:57:30
17:12:55
17:28:20
17:43:45
17:59:10
18:14:35
18:30:00
18:45:25
19:00:50
19:16:15
19:31:40
19:47:05
20:02:30
20:17:55
20:33:20
20:48:45
21:04:10
21:19:35
21:35:00
21:50:25
22:05:50
22:21:15
22:36:40
22:52:05
23:07:30
23:22:55
23:38:20
"""