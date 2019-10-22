#coding: iso-8859-9 T�rk�e
# p_32103b.py: T�retilen veri �er�evelerinin yeniden-endekslenmesi �rne�i.

import pandas as pd
import numpy as np

N=366

v�1 = pd.DataFrame ( {
    'Tarih': pd.date_range (start='2019-07-23', periods=N, freq='D'),
    'x': np.linspace (0, stop=N-1, num=N),
    'y': np.random.rand (N),
    'Eczane-A': np.random.choice (['Sabah', 'Ak�am', 'Gece'], N).tolist(),
    'D': np.random.normal (100, 10, size=(N)).tolist() })
print ((N-1), " adet veri �er�evesi tablosu:\n", v�1, sep="")

v�2 = v�1.reindex (index=[0, 2, 5, 9, 16, 25, 35, 365], columns=['Tarih', 'Eczane-A', 'Eczane-B'])
print ("\nVerili tarihlerde Eczane-A ve B'deki 8'er saatl�k vardiya n�beti t�r�:\n", v�2, sep="")
print ("-"*70)
#------------------------------------------------------------------------------------------------------


v�3 = pd.DataFrame (np.random.randn (10, 3), columns=['kolon1','kolon2','kolon3'])
v�4 = pd.DataFrame (np.random.randn (7, 3), columns=['kolon1','kolon2','kolon3'])

print ("\n(10x3) geli�ig�zel say�l� veri �er�evesi:\n", v�3, sep="")
print ("\n(7x3) geli�ig�zel say�l� veri �er�evesi:\n", v�4, sep="")

v�3 = v�3.reindex_like (v�4)
print ("\n(10x3) v�'nin (7x3) ebatl�s�:\n", v�3, sep="")



"""��kt�:
>python p_32103b.py
365 adet veri �er�evesi tablosu:
         Tarih      x         y Eczane-A           D
0   2019-07-23    0.0  0.529934    Sabah  107.306558
1   2019-07-24    1.0  0.209846     Gece  125.213925
2   2019-07-25    2.0  0.880275     Gece  108.336269
3   2019-07-26    3.0  0.978690    Ak�am  100.535892
4   2019-07-27    4.0  0.076751    Sabah   97.896957
5   2019-07-28    5.0  0.683322     Gece   87.513117
6   2019-07-29    6.0  0.627166    Ak�am  101.034470
7   2019-07-30    7.0  0.904748    Ak�am   94.747918
8   2019-07-31    8.0  0.341237    Ak�am  100.899460
9   2019-08-01    9.0  0.539848     Gece   93.864572
10  2019-08-02   10.0  0.427837    Ak�am   99.448138
11  2019-08-03   11.0  0.789559     Gece   97.739310
12  2019-08-04   12.0  0.740888    Ak�am  102.002041
13  2019-08-05   13.0  0.959237    Sabah   91.553658
14  2019-08-06   14.0  0.900495     Gece  101.095391
15  2019-08-07   15.0  0.565678     Gece  122.566546
16  2019-08-08   16.0  0.829645     Gece   89.979197
17  2019-08-09   17.0  0.736634    Ak�am  103.708412
18  2019-08-10   18.0  0.800551    Sabah   84.403360
19  2019-08-11   19.0  0.363374    Ak�am   95.805492
20  2019-08-12   20.0  0.177352    Sabah  104.662569
21  2019-08-13   21.0  0.733611    Ak�am   93.021370
22  2019-08-14   22.0  0.570328    Ak�am   78.109025
23  2019-08-15   23.0  0.212047     Gece  102.654213
24  2019-08-16   24.0  0.958666     Gece  108.650509
25  2019-08-17   25.0  0.452465    Ak�am   93.832652
26  2019-08-18   26.0  0.739218    Ak�am   93.726975
27  2019-08-19   27.0  0.209239     Gece  105.402498
28  2019-08-20   28.0  0.821556    Sabah   82.146193
29  2019-08-21   29.0  0.819071     Gece  107.181775
..         ...    ...       ...      ...         ...
336 2020-06-23  336.0  0.476116     Gece   88.557912
337 2020-06-24  337.0  0.744281     Gece  111.134427
338 2020-06-25  338.0  0.717232    Ak�am  110.287723
339 2020-06-26  339.0  0.693245    Sabah   78.207640
340 2020-06-27  340.0  0.726433    Sabah   95.508770
341 2020-06-28  341.0  0.497854     Gece   98.816127
342 2020-06-29  342.0  0.300083    Ak�am  105.232538
343 2020-06-30  343.0  0.556031     Gece   97.837738
344 2020-07-01  344.0  0.497243     Gece  107.541083
345 2020-07-02  345.0  0.429188    Ak�am  111.018675
346 2020-07-03  346.0  0.052359     Gece  112.471617
347 2020-07-04  347.0  0.923500    Sabah  115.195783
348 2020-07-05  348.0  0.996913    Sabah   99.748419
349 2020-07-06  349.0  0.416029    Sabah  107.595459
350 2020-07-07  350.0  0.414207     Gece  107.741557
351 2020-07-08  351.0  0.943611     Gece  103.253724
352 2020-07-09  352.0  0.971576     Gece  104.650510
353 2020-07-10  353.0  0.333666    Sabah   98.691531
354 2020-07-11  354.0  0.821895     Gece  101.319753
355 2020-07-12  355.0  0.428313     Gece  116.937779
356 2020-07-13  356.0  0.295308     Gece   97.984320
357 2020-07-14  357.0  0.794220     Gece   94.529635
358 2020-07-15  358.0  0.091716     Gece   90.143300
359 2020-07-16  359.0  0.282999    Ak�am   98.673773
360 2020-07-17  360.0  0.674269    Ak�am  108.409732
361 2020-07-18  361.0  0.866284    Sabah   84.554329
362 2020-07-19  362.0  0.901485     Gece  104.411675
363 2020-07-20  363.0  0.205514     Gece  109.404402
364 2020-07-21  364.0  0.353864    Sabah  102.296213
365 2020-07-22  365.0  0.118233    Sabah   94.451940

[366 rows x 5 columns]

Verili tarihlerde Eczane-A ve B'deki 8'er saatl�k vardiya n�beti t�r�:
         Tarih Eczane-A  Eczane-B
0   2019-07-23    Sabah       NaN
2   2019-07-25     Gece       NaN
5   2019-07-28     Gece       NaN
9   2019-08-01     Gece       NaN
16  2019-08-08     Gece       NaN
25  2019-08-17    Ak�am       NaN
35  2019-08-27    Ak�am       NaN
365 2020-07-22    Sabah       NaN
----------------------------------------------------------------------

(10x3) geli�ig�zel say�l� veri �er�evesi:
     kolon1    kolon2    kolon3
0 -0.725901  0.843114  0.718201
1  1.415808  0.301653 -0.061147
2  0.697259 -0.767965 -0.998558
3  1.510965 -0.315171  0.126683
4 -1.089056  0.834616  0.114792
5 -0.205034 -0.198145  0.458181
6  0.121649  0.795466  0.304877
7  1.138248  0.115477 -0.797516
8  0.594168  0.224304 -0.163416
9 -0.887489 -0.615705  0.692739

(7x3) geli�ig�zel say�l� veri �er�evesi:
     kolon1    kolon2    kolon3
0  0.496307  0.743909 -1.281656
1 -0.345394  0.012836  0.723810
2 -0.082970  0.745877  0.492888
3  0.882945  0.109888 -0.294475
4  0.618625 -0.817107  0.094973
5  0.072660 -0.764099 -4.021576
6  0.181687  0.878749 -0.813929

(10x3) v�'nin (7x3) ebatl�s�:
     kolon1    kolon2    kolon3
0 -0.725901  0.843114  0.718201
1  1.415808  0.301653 -0.061147
2  0.697259 -0.767965 -0.998558
3  1.510965 -0.315171  0.126683
4 -1.089056  0.834616  0.114792
5 -0.205034 -0.198145  0.458181
6  0.121649  0.795466  0.304877
"""