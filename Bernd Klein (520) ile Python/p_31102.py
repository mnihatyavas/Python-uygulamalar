# coding:iso-8859-9 Türkçe
# p_31102.py: Günlük zaman ve sıcaklık verileri dosyasını okuyup görüntüleme örneği.

import numpy as np

def dakikayaÇevir (saatDakikaSaniye):
    if type (saatDakikaSaniye) == bytes: #byte dizgesi...
        saatDakikaSaniye = saatDakikaSaniye.decode()
    liste = saatDakikaSaniye.split (":")
    dakika = float (liste[0]) * 60 + float (liste[1]) + float (liste[2]) / 60
    return dakika

print ("3 adet SS:DD:ss verisiyle dakikayaÇevir fonksiyonunun testi:")
for z in ["06:00:10", "06:27:45", "12:59:59"]:
    print ("Saat: %s ==> %.4f dakika yapar" % (z, dakikayaÇevir (z)) )
print ("-"*50)
#---------------------------------------------------------------------------------------------

y = np.loadtxt ("p_31102x.txt", converters={0: dakikayaÇevir})
# Dosyanın ilk kolonundaki SS:DD:ss verileri dakikaya çevrilir...

print ("\nGün boyu 6.5 dakikada-bir alınan hava sıcaklığı verileri:")
for i in range (len (y)):
    d = y[i][0]
    s = str (int (d / 60)) + ":" + str (int (d % 60)) + ":" + str (int (eval (str (d)[str (d).index ("."):]) * 60))
    print ("Saat: %8s=Dakika: %7.2f ==>Derece: %5.2f" % (s, d, y[i][1]))



"""Çıktı:
>python p_31102.py
3 adet SS:DD:ss verisiyle dakikayaÇevir fonksiyonunun testi:
Saat: 06:00:10 ==> 360.1667 dakika yapar
Saat: 06:27:45 ==> 387.7500 dakika yapar
Saat: 12:59:59 ==> 779.9833 dakika yapar
--------------------------------------------------

Gün boyu 6.5 dakikada-bir alınan hava sıcaklığı verileri:
Saat:    0:0:0=Dakika:    0.00 ==>Derece: 31.90
Saat:   0:6:30=Dakika:    6.50 ==>Derece:  5.40
Saat:   0:13:0=Dakika:   13.00 ==>Derece: 13.70
Saat:  0:19:30=Dakika:   19.50 ==>Derece:  8.65
Saat:   0:26:0=Dakika:   26.00 ==>Derece:  2.78
Saat:  0:32:30=Dakika:   32.50 ==>Derece: 39.87
Saat:   0:39:0=Dakika:   39.00 ==>Derece: 33.36
Saat:  0:45:30=Dakika:   45.50 ==>Derece:  5.29
Saat:   0:52:0=Dakika:   52.00 ==>Derece: 23.87
Saat:  0:58:30=Dakika:   58.50 ==>Derece: 18.66
Saat:    1:5:0=Dakika:   65.00 ==>Derece: 15.25
Saat:  1:11:30=Dakika:   71.50 ==>Derece: 23.21
Saat:   1:18:0=Dakika:   78.00 ==>Derece: 37.12
Saat:  1:24:30=Dakika:   84.50 ==>Derece: 27.16
Saat:   1:31:0=Dakika:   91.00 ==>Derece: 39.14
Saat:  1:37:30=Dakika:   97.50 ==>Derece: 24.10
Saat:   1:44:0=Dakika:  104.00 ==>Derece: 26.65
Saat:  1:50:30=Dakika:  110.50 ==>Derece: 30.70
Saat:   1:57:0=Dakika:  117.00 ==>Derece: 16.60
Saat:   2:3:30=Dakika:  123.50 ==>Derece: 36.67
Saat:   2:10:0=Dakika:  130.00 ==>Derece: 24.03
Saat:  2:16:30=Dakika:  136.50 ==>Derece: 20.93
Saat:   2:23:0=Dakika:  143.00 ==>Derece: 18.54
Saat:  2:29:30=Dakika:  149.50 ==>Derece: 24.64
Saat:   2:36:0=Dakika:  156.00 ==>Derece: 20.02
Saat:  2:42:30=Dakika:  162.50 ==>Derece: 38.52
Saat:   2:49:0=Dakika:  169.00 ==>Derece: 34.47
Saat:  2:55:30=Dakika:  175.50 ==>Derece: 29.91
Saat:    3:2:0=Dakika:  182.00 ==>Derece:  7.85
Saat:   3:8:30=Dakika:  188.50 ==>Derece:  4.97
Saat:   3:15:0=Dakika:  195.00 ==>Derece: 27.42
Saat:  3:21:30=Dakika:  201.50 ==>Derece:  4.19
Saat:   3:28:0=Dakika:  208.00 ==>Derece:  2.74
Saat:  3:34:30=Dakika:  214.50 ==>Derece: 12.67
Saat:   3:41:0=Dakika:  221.00 ==>Derece: 13.58
Saat:  3:47:30=Dakika:  227.50 ==>Derece:  2.20
Saat:   3:54:0=Dakika:  234.00 ==>Derece:  3.23
Saat:   4:0:30=Dakika:  240.50 ==>Derece:  1.22
Saat:    4:7:0=Dakika:  247.00 ==>Derece:  8.14
Saat:  4:13:30=Dakika:  253.50 ==>Derece: 24.52
Saat:   4:20:0=Dakika:  260.00 ==>Derece: 39.49
Saat:  4:26:30=Dakika:  266.50 ==>Derece: 32.25
Saat:   4:33:0=Dakika:  273.00 ==>Derece:  3.72
Saat:  4:39:30=Dakika:  279.50 ==>Derece: 23.95
Saat:   4:46:0=Dakika:  286.00 ==>Derece: 18.53
Saat:  4:52:30=Dakika:  292.50 ==>Derece: 27.99
Saat:   4:59:0=Dakika:  299.00 ==>Derece: 28.97
Saat:   5:5:30=Dakika:  305.50 ==>Derece: 21.90
Saat:   5:12:0=Dakika:  312.00 ==>Derece: 28.50
Saat:  5:18:30=Dakika:  318.50 ==>Derece: 18.85
Saat:   5:25:0=Dakika:  325.00 ==>Derece: 31.09
Saat:  5:31:30=Dakika:  331.50 ==>Derece: 38.75
Saat:   5:38:0=Dakika:  338.00 ==>Derece:  7.26
Saat:  5:44:30=Dakika:  344.50 ==>Derece: 32.49
Saat:   5:51:0=Dakika:  351.00 ==>Derece: 27.28
Saat:  5:57:30=Dakika:  357.50 ==>Derece: 30.99
Saat:    6:4:0=Dakika:  364.00 ==>Derece: 39.63
Saat:  6:10:30=Dakika:  370.50 ==>Derece: 24.65
Saat:   6:17:0=Dakika:  377.00 ==>Derece: 21.55
Saat:  6:23:30=Dakika:  383.50 ==>Derece: 16.30
Saat:   6:30:0=Dakika:  390.00 ==>Derece: 20.36
Saat:  6:36:30=Dakika:  396.50 ==>Derece: 18.19
Saat:   6:43:0=Dakika:  403.00 ==>Derece:  0.58
Saat:  6:49:30=Dakika:  409.50 ==>Derece: 19.61
Saat:   6:56:0=Dakika:  416.00 ==>Derece:  8.77
Saat:   7:2:30=Dakika:  422.50 ==>Derece: 29.29
Saat:    7:9:0=Dakika:  429.00 ==>Derece: 32.17
Saat:  7:15:30=Dakika:  435.50 ==>Derece: 35.87
Saat:   7:22:0=Dakika:  442.00 ==>Derece: 14.68
Saat:  7:28:30=Dakika:  448.50 ==>Derece:  3.91
Saat:   7:35:0=Dakika:  455.00 ==>Derece: 10.39
Saat:  7:41:30=Dakika:  461.50 ==>Derece: 38.67
Saat:   7:48:0=Dakika:  468.00 ==>Derece: 21.32
Saat:  7:54:30=Dakika:  474.50 ==>Derece:  8.78
Saat:    8:1:0=Dakika:  481.00 ==>Derece:  8.32
Saat:   8:7:30=Dakika:  487.50 ==>Derece: 11.47
Saat:   8:14:0=Dakika:  494.00 ==>Derece: 30.03
Saat:  8:20:30=Dakika:  500.50 ==>Derece: 11.10
Saat:   8:27:0=Dakika:  507.00 ==>Derece: 30.10
Saat:  8:33:30=Dakika:  513.50 ==>Derece:  2.23
Saat:   8:40:0=Dakika:  520.00 ==>Derece:  7.87
Saat:  8:46:30=Dakika:  526.50 ==>Derece:  5.93
Saat:   8:53:0=Dakika:  533.00 ==>Derece: 36.73
Saat:  8:59:30=Dakika:  539.50 ==>Derece: 36.25
Saat:    9:6:0=Dakika:  546.00 ==>Derece: 24.24
Saat:  9:12:30=Dakika:  552.50 ==>Derece: 25.42
Saat:   9:19:0=Dakika:  559.00 ==>Derece: 26.41
Saat:  9:25:30=Dakika:  565.50 ==>Derece:  7.18
Saat:   9:32:0=Dakika:  572.00 ==>Derece: 13.77
Saat:  9:38:30=Dakika:  578.50 ==>Derece: 27.68
Saat:   9:45:0=Dakika:  585.00 ==>Derece:  0.71
Saat:  9:51:30=Dakika:  591.50 ==>Derece:  8.22
Saat:   9:58:0=Dakika:  598.00 ==>Derece: 19.23
Saat:  10:4:30=Dakika:  604.50 ==>Derece: 39.98
Saat:  10:11:0=Dakika:  611.00 ==>Derece: 19.10
Saat: 10:17:30=Dakika:  617.50 ==>Derece: 16.62
Saat:  10:24:0=Dakika:  624.00 ==>Derece: 27.17
Saat: 10:30:30=Dakika:  630.50 ==>Derece: 29.55
Saat:  10:37:0=Dakika:  637.00 ==>Derece: 37.18
Saat: 10:43:30=Dakika:  643.50 ==>Derece:  8.27
Saat:  10:50:0=Dakika:  650.00 ==>Derece:  5.36
Saat: 10:56:30=Dakika:  656.50 ==>Derece: 11.79
Saat:   11:3:0=Dakika:  663.00 ==>Derece: 22.66
Saat:  11:9:30=Dakika:  669.50 ==>Derece:  8.67
Saat:  11:16:0=Dakika:  676.00 ==>Derece: 16.43
Saat: 11:22:30=Dakika:  682.50 ==>Derece:  3.57
Saat:  11:29:0=Dakika:  689.00 ==>Derece: 29.57
Saat: 11:35:30=Dakika:  695.50 ==>Derece: 35.72
Saat:  11:42:0=Dakika:  702.00 ==>Derece:  2.11
Saat: 11:48:30=Dakika:  708.50 ==>Derece: 22.03
Saat:  11:55:0=Dakika:  715.00 ==>Derece: 25.89
Saat:  12:1:30=Dakika:  721.50 ==>Derece:  3.56
Saat:   12:8:0=Dakika:  728.00 ==>Derece:  6.73
Saat: 12:14:30=Dakika:  734.50 ==>Derece: 22.53
Saat:  12:21:0=Dakika:  741.00 ==>Derece:  8.94
Saat: 12:27:30=Dakika:  747.50 ==>Derece: 24.59
Saat:  12:34:0=Dakika:  754.00 ==>Derece:  6.13
Saat: 12:40:30=Dakika:  760.50 ==>Derece: 37.68
Saat:  12:47:0=Dakika:  767.00 ==>Derece: 38.87
Saat: 12:53:30=Dakika:  773.50 ==>Derece: 20.05
Saat:   13:0:0=Dakika:  780.00 ==>Derece: 22.50
Saat:  13:6:30=Dakika:  786.50 ==>Derece:  5.36
Saat:  13:13:0=Dakika:  793.00 ==>Derece: 28.55
Saat: 13:19:30=Dakika:  799.50 ==>Derece: 23.17
Saat:  13:26:0=Dakika:  806.00 ==>Derece: 32.03
Saat: 13:32:30=Dakika:  812.50 ==>Derece: 11.14
Saat:  13:39:0=Dakika:  819.00 ==>Derece: 12.75
Saat: 13:45:30=Dakika:  825.50 ==>Derece: 12.87
Saat:  13:52:0=Dakika:  832.00 ==>Derece:  3.92
Saat: 13:58:30=Dakika:  838.50 ==>Derece: 20.91
Saat:   14:5:0=Dakika:  845.00 ==>Derece:  0.31
Saat: 14:11:30=Dakika:  851.50 ==>Derece: 21.09
Saat:  14:18:0=Dakika:  858.00 ==>Derece: 39.46
Saat: 14:24:30=Dakika:  864.50 ==>Derece:  5.32
Saat:  14:31:0=Dakika:  871.00 ==>Derece: 28.45
Saat: 14:37:30=Dakika:  877.50 ==>Derece: 16.13
Saat:  14:44:0=Dakika:  884.00 ==>Derece: 21.22
Saat: 14:50:30=Dakika:  890.50 ==>Derece: 11.38
Saat:  14:57:0=Dakika:  897.00 ==>Derece: 24.17
Saat:  15:3:30=Dakika:  903.50 ==>Derece:  7.02
Saat:  15:10:0=Dakika:  910.00 ==>Derece: 10.27
Saat: 15:16:30=Dakika:  916.50 ==>Derece:  1.50
Saat:  15:23:0=Dakika:  923.00 ==>Derece: 35.72
Saat: 15:29:30=Dakika:  929.50 ==>Derece: 36.78
Saat:  15:36:0=Dakika:  936.00 ==>Derece: 12.08
Saat: 15:42:30=Dakika:  942.50 ==>Derece: 18.96
Saat:  15:49:0=Dakika:  949.00 ==>Derece:  9.05
Saat: 15:55:30=Dakika:  955.50 ==>Derece: 29.87
Saat:   16:2:0=Dakika:  962.00 ==>Derece: 16.94
Saat:  16:8:30=Dakika:  968.50 ==>Derece: 24.86
Saat:  16:15:0=Dakika:  975.00 ==>Derece: 17.76
Saat: 16:21:30=Dakika:  981.50 ==>Derece:  4.47
Saat:  16:28:0=Dakika:  988.00 ==>Derece: 17.78
Saat: 16:34:30=Dakika:  994.50 ==>Derece: 31.13
Saat:  16:41:0=Dakika: 1001.00 ==>Derece: 29.46
Saat: 16:47:30=Dakika: 1007.50 ==>Derece:  9.01
Saat:  16:54:0=Dakika: 1014.00 ==>Derece:  3.76
Saat:  17:0:30=Dakika: 1020.50 ==>Derece: 28.95
Saat:   17:7:0=Dakika: 1027.00 ==>Derece: 14.84
Saat: 17:13:30=Dakika: 1033.50 ==>Derece:  8.00
Saat:  17:20:0=Dakika: 1040.00 ==>Derece: 38.25
Saat: 17:26:30=Dakika: 1046.50 ==>Derece: 33.99
Saat:  17:33:0=Dakika: 1053.00 ==>Derece: 14.88
Saat: 17:39:30=Dakika: 1059.50 ==>Derece: 35.20
Saat:  17:46:0=Dakika: 1066.00 ==>Derece: 12.97
Saat: 17:52:30=Dakika: 1072.50 ==>Derece: 39.08
Saat:  17:59:0=Dakika: 1079.00 ==>Derece: 20.35
Saat:  18:5:30=Dakika: 1085.50 ==>Derece: 29.65
Saat:  18:12:0=Dakika: 1092.00 ==>Derece: 37.52
Saat: 18:18:30=Dakika: 1098.50 ==>Derece: 28.90
Saat:  18:25:0=Dakika: 1105.00 ==>Derece:  5.26
Saat: 18:31:30=Dakika: 1111.50 ==>Derece:  5.22
Saat:  18:38:0=Dakika: 1118.00 ==>Derece: 18.46
Saat: 18:44:30=Dakika: 1124.50 ==>Derece: 12.68
Saat:  18:51:0=Dakika: 1131.00 ==>Derece: 29.46
Saat: 18:57:30=Dakika: 1137.50 ==>Derece: 37.73
Saat:   19:4:0=Dakika: 1144.00 ==>Derece: 18.56
Saat: 19:10:30=Dakika: 1150.50 ==>Derece: 31.09
Saat:  19:17:0=Dakika: 1157.00 ==>Derece: 21.16
Saat: 19:23:30=Dakika: 1163.50 ==>Derece:  6.75
Saat:  19:30:0=Dakika: 1170.00 ==>Derece:  0.28
Saat: 19:36:30=Dakika: 1176.50 ==>Derece: 36.43
Saat:  19:43:0=Dakika: 1183.00 ==>Derece:  5.38
Saat: 19:49:30=Dakika: 1189.50 ==>Derece:  7.09
Saat:  19:56:0=Dakika: 1196.00 ==>Derece: 37.70
Saat:  20:2:30=Dakika: 1202.50 ==>Derece: 36.40
Saat:   20:9:0=Dakika: 1209.00 ==>Derece: 20.55
Saat: 20:15:30=Dakika: 1215.50 ==>Derece: 21.64
Saat:  20:22:0=Dakika: 1222.00 ==>Derece: 24.55
Saat: 20:28:30=Dakika: 1228.50 ==>Derece: 19.00
Saat:  20:35:0=Dakika: 1235.00 ==>Derece: 17.42
Saat: 20:41:30=Dakika: 1241.50 ==>Derece: 38.34
Saat:  20:48:0=Dakika: 1248.00 ==>Derece: 17.53
Saat: 20:54:30=Dakika: 1254.50 ==>Derece: 23.78
Saat:   21:1:0=Dakika: 1261.00 ==>Derece: 11.71
Saat:  21:7:30=Dakika: 1267.50 ==>Derece:  8.19
Saat:  21:14:0=Dakika: 1274.00 ==>Derece:  0.28
Saat: 21:20:30=Dakika: 1280.50 ==>Derece: 11.79
Saat:  21:27:0=Dakika: 1287.00 ==>Derece: 36.37
Saat: 21:33:30=Dakika: 1293.50 ==>Derece: 32.46
Saat:  21:40:0=Dakika: 1300.00 ==>Derece:  3.18
Saat: 21:46:30=Dakika: 1306.50 ==>Derece:  5.45
Saat:  21:53:0=Dakika: 1313.00 ==>Derece: 39.32
Saat: 21:59:30=Dakika: 1319.50 ==>Derece: 37.62
Saat:   22:6:0=Dakika: 1326.00 ==>Derece: 29.54
Saat: 22:12:30=Dakika: 1332.50 ==>Derece: 13.51
Saat:  22:19:0=Dakika: 1339.00 ==>Derece: 10.39
Saat: 22:25:30=Dakika: 1345.50 ==>Derece: 34.23
Saat:  22:32:0=Dakika: 1352.00 ==>Derece: 12.54
Saat: 22:38:30=Dakika: 1358.50 ==>Derece: 19.85
Saat:  22:45:0=Dakika: 1365.00 ==>Derece:  7.89
Saat: 22:51:30=Dakika: 1371.50 ==>Derece: 36.39
Saat:  22:58:0=Dakika: 1378.00 ==>Derece:  2.46
Saat:  23:4:30=Dakika: 1384.50 ==>Derece: 13.15
Saat:  23:11:0=Dakika: 1391.00 ==>Derece: 15.80
Saat: 23:17:30=Dakika: 1397.50 ==>Derece: 39.18
Saat:  23:24:0=Dakika: 1404.00 ==>Derece:  4.34
Saat: 23:30:30=Dakika: 1410.50 ==>Derece: 26.47
Saat:  23:37:0=Dakika: 1417.00 ==>Derece:  8.84
Saat: 23:43:30=Dakika: 1423.50 ==>Derece:  5.08
Saat:  23:50:0=Dakika: 1430.00 ==>Derece:  9.51
"""