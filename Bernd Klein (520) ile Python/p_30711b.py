# coding:iso-8859-9 T�rk�e
# p_30711b.py: Firman�n 12 �ehirdeki farkl� b�y�meoranl� 19 y�ll�k sat�� rakamlar� �rne�i.

import numpy as np

sat��lar = np.array ([1245.89, 2220.00, 1635.77, 1936.25, 1002.03, 2099.13,  723.99, 990.37, 541.44, 1765.00, 1802.84, 1999.00])

dosya = open ("p_30711bx.csv", "w")
sat�r = "Y�l, Frankfurt, M�nih, Berlin, Z�rih, Hamburg, Londra, Toronto, Strasburg, L�ksemburg, Amsterdam, Rotterdam, Heyg"
dosya.write (sat�r + "\n"); print (sat�r, "\n", "-"*113, sep="")

asgariY�zde = 0.98  #  (1-0.98)/0.98=% -2.041
azamiY�zde = 1.06   # (1.06-1)/1=% 6
b�y�meOran� = (azamiY�zde - asgariY�zde) * np.random.random_sample (12) + asgariY�zde
# 12 �ehrin herbiri i�in farkl� b�y�meoran�

for y�l in range (1997, 2016):
    sat�r = str (y�l) + ", " + ", ".join (map (str, sat��lar) )
    dosya.write (sat�r + "\n"); print (sat�r, "==>12 farkl� b�y�me oran�:", b�y�meOran�)
    if y�l % 4 == 0: b�y�meOran� = (azamiY�zde - asgariY�zde) * np.random.random_sample (12) + asgariY�zde
    sat��lar = np.around (sat��lar * b�y�meOran�, 2) # K�s�rat� 2 haneye yuvarlar...

dosya.close()



"""��kt�:
>python p_30711b.py
Y�l, Frankfurt, M�nih, Berlin, Z�rih, Hamburg, Londra, Toronto, Strasburg, L�ksemburg, Amsterdam, Rotterdam, Heyg
-----------------------------------------------------------------------------------------------------------------
1997, 1245.89, 2220.0, 1635.77, 1936.25, 1002.03, 2099.13, 723.99, 990.37, 541.44, 1765.0, 1802.84, 1999.0 ==>12 farkl� b�y�me oran�: [1.05845253 1.0217798  1.03054188 1.0350882  1.00585482 1.01424527 1.02272066 1.00385654 1.05751977 0.99493064 1.03748611 1.03285177]
1998, 1318.72, 2268.35, 1685.73, 2004.19, 1007.9, 2129.03, 740.44, 994.19, 572.58, 1756.05, 1870.42, 2064.67 ==>12 farkl� b�y�me oran�: [1.05845253 1.0217798  1.03054188 1.0350882  1.00585482 1.01424527 1.02272066 1.00385654 1.05751977 0.99493064 1.03748611 1.03285177]
1999, 1395.8, 2317.75, 1737.22, 2074.51, 1013.8, 2159.36, 757.26, 998.02, 605.51, 1747.15, 1940.53, 2132.5 ==>12 farkl� b�y�me oran�: [1.05845253 1.0217798  1.03054188 1.0350882  1.00585482 1.01424527 1.02272066 1.00385654 1.05751977 0.99493064 1.03748611 1.03285177]
2000, 1477.39, 2368.23, 1790.28, 2147.3, 1019.74, 2190.12, 774.47, 1001.87, 640.34, 1738.29, 2013.27, 2202.56 ==>12 farkl� b�y�me oran�: [1.05845253 1.02177981.03054188 1.0350882  1.00585482 1.01424527 1.02272066 1.00385654 1.05751977 0.99493064 1.03748611 1.03285177]
2001, 1556.46, 2324.89, 1885.22, 2223.76, 1064.61, 2220.59, 773.66, 1021.35, 627.61, 1703.72, 2031.43, 2326.55 ==>12 farkl� b�y�me oran�: [1.05351934 0.9816975 1.05302986 1.03560719 1.04399908 1.01391216 0.998953   1.01944315 0.98012333 0.98011083 1.00902096 1.05629461]
2002, 1639.76, 2282.34, 1985.19, 2302.94, 1111.45, 2251.48, 772.85, 1041.21, 615.14, 1669.83, 2049.76, 2457.52 ==>12 farkl� b�y�me oran�: [1.05351934 0.9816975 1.05302986 1.03560719 1.04399908 1.01391216 0.998953   1.01944315 0.98012333 0.98011083 1.00902096 1.05629461]
2003, 1727.52, 2240.57, 2090.46, 2384.94, 1160.35, 2282.8, 772.04, 1061.45, 602.91, 1636.62, 2068.25, 2595.87 ==>12 farkl� b�y�me oran�: [1.05351934 0.98169751.05302986 1.03560719 1.04399908 1.01391216 0.998953   1.01944315 0.98012333 0.98011083 1.00902096 1.05629461]
2004, 1819.98, 2199.56, 2201.32, 2469.86, 1211.4, 2314.56, 771.23, 1082.09, 590.93, 1604.07, 2086.91, 2742.0 ==>12 farkl� b�y�me oran�: [1.05351934 0.9816975  1.05302986 1.03560719 1.04399908 1.01391216 0.998953   1.01944315 0.98012333 0.98011083 1.00902096 1.05629461]
2005, 1917.58, 2170.07, 2235.2, 2520.37, 1213.99, 2351.06, 757.28, 1082.19, 583.75, 1671.04, 2045.98, 2808.32 ==>12 farkl� b�y�me oran�: [1.05362803 0.98659171.01538916 1.02044961 1.00213961 1.01576758 0.98190921 1.00009659 0.98785636 1.04174774 0.9803852  1.02418622]
2006, 2020.42, 2140.97, 2269.6, 2571.91, 1216.59, 2388.13, 743.58, 1082.29, 576.66, 1740.8, 2005.85, 2876.24 ==>12 farkl� b�y�me oran�: [1.05362803 0.9865917  1.01538916 1.02044961 1.00213961 1.01576758 0.98190921 1.00009659 0.98785636 1.04174774 0.9803852  1.02418622]
2007, 2128.77, 2112.26, 2304.53, 2624.5, 1219.19, 2425.79, 730.13, 1082.39, 569.66, 1813.47, 1966.51, 2945.81 ==>12 farkl� b�y�me oran�: [1.05362803 0.98659171.01538916 1.02044961 1.00213961 1.01576758 0.98190921 1.00009659 0.98785636 1.04174774 0.9803852  1.02418622]
2008, 2242.93, 2083.94, 2339.99, 2678.17, 1221.8, 2464.04, 716.92, 1082.49, 562.74, 1889.18, 1927.94, 3017.06 ==>12 farkl� b�y�me oran�: [1.05362803 0.98659171.01538916 1.02044961 1.00213961 1.01576758 0.98190921 1.00009659 0.98785636 1.04174774 0.9803852  1.02418622]
2009, 2329.91, 2055.22, 2392.5, 2740.0, 1265.35, 2427.2, 746.45, 1088.63, 580.43, 1908.1, 2009.26, 3026.59 ==>12 farkl� b�y�me oran�: [1.03878151 0.98622022 1.02244037 1.02308809 1.03564747 0.98505071 1.04119036 1.00566879 1.03143383 1.01001748 1.04217821 1.00315718]
2010, 2420.27, 2026.9, 2446.19, 2803.26, 1310.46, 2390.92, 777.2, 1094.8, 598.68, 1927.21, 2094.01, 3036.15 ==>12 farkl� b�y�me oran�: [1.03878151 0.98622022 1.02244037 1.02308809 1.03564747 0.98505071 1.04119036 1.00566879 1.03143383 1.01001748 1.04217821 1.00315718]
2011, 2514.13, 1998.97, 2501.08, 2867.98, 1357.17, 2355.18, 809.21, 1101.01, 617.5, 1946.52, 2182.33, 3045.74 ==>12 farkl� b�y�me oran�: [1.03878151 0.986220221.02244037 1.02308809 1.03564747 0.98505071 1.04119036 1.00566879 1.03143383 1.01001748 1.04217821 1.00315718]
2012, 2611.63, 1971.42, 2557.21, 2934.2, 1405.55, 2319.97, 842.54, 1107.25, 636.91, 1966.02, 2274.38, 3055.36 ==>12 farkl� b�y�me oran�: [1.03878151 0.986220221.02244037 1.02308809 1.03564747 0.98505071 1.04119036 1.00566879 1.03143383 1.01001748 1.04217821 1.00315718]
2013, 2698.92, 2078.59, 2527.62, 3056.49, 1457.68, 2335.39, 851.04, 1114.84, 670.16, 1928.16, 2403.07, 3008.82 ==>12 farkl� b�y�me oran�: [1.03342385 1.05436077 0.98842893 1.04167838 1.03709145 1.00664658 1.01008488 1.00685532 1.05219757 0.98074447 1.05658264 0.98476619]
2014, 2789.13, 2191.58, 2498.37, 3183.88, 1511.75, 2350.91, 859.62, 1122.48, 705.14, 1891.03, 2539.04, 2962.98 ==>12 farkl� b�y�me oran�: [1.03342385 1.05436077 0.98842893 1.04167838 1.03709145 1.00664658 1.01008488 1.00685532 1.05219757 0.98074447 1.05658264 0.98476619]
2015, 2882.35, 2310.72, 2469.46, 3316.58, 1567.82, 2366.54, 868.29, 1130.17, 741.95, 1854.62, 2682.71, 2917.84 ==>12 farkl� b�y�me oran�: [1.03342385 1.05436077 0.98842893 1.04167838 1.03709145 1.00664658 1.01008488 1.00685532 1.05219757 0.98074447 1.05658264 0.98476619]
"""