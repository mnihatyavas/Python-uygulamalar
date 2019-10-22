#coding:iso-8859-9 Türkçe
# p_32205b.py: Başkanlar excel yaygın-sayfa örneği.

import pandas as pd

ys = pd.read_excel ("p_32205bx.xls") #, header=0, names=["Başkanın ismi", "Başkanlık süresi", "Katılım %", "Kazanan %"]
print ("Başkanlar yaygın sayfası dökümü:\n", ys,
    "\n\nKolon adları:\n", ys.columns, sep="")
print ("-"*79)
#-------------------------------------------------------------------------------------------------------

print ("\nBaşkanlar seçili kolonlar dökümü:\n", ys [["President", "Year first inaugurated", "Years in office", "% popular"]], sep="")
print ("-"*79)
#-------------------------------------------------------------------------------------------------------

ys2 = ys [ys ['Years in office'] > 0] # Eksik bilgili NaN satırlar elensin
print ("\nBaşkanlar (eksiksiz verili) seçili kolonlar dökümü:\n", ys2 [["President", "Year first inaugurated", "Years in office", "% popular"]], sep="")
print ("-"*79)
#-------------------------------------------------------------------------------------------------------

print ('\nEn kısa görev süresi:', ys ['Years in office'].min() )
print ('En uzun görev süresi:', ys ['Years in office'].max() )
print ('Bugüne kadarki toplam görev süresi:', ys ['Years in office'].sum() )



"""Çıktı:
>python p_32205b.py
Başkanlar yaygın sayfası dökümü:
                 President  Years in office  ...  % electoral  % popular
0        George Washington              8.0  ...   100.000000       NA()
1               John Adams              4.0  ...    94.964029       NA()
2         Thomas Jefferson              8.0  ...    53.284672       NA()
3            James Madison              8.0  ...    69.318182       NA()
4             James Monroe              8.0  ...    82.805430       NA()
5        John Quincy Adams              4.0  ...    32.183908       NA()
6           Andrew Jackson              8.0  ...    68.199234    55.9706
7        Martin Van Buren               4.0  ...    57.823129    50.8253
8   William Henry Harrison              0.8  ...    79.591837    52.8811
9            James K. Polk              4.0  ...    61.818182    49.5437
10          Zachary Taylor              1.0  ...    56.206897     47.284
11         Franklin Pierce              4.0  ...    85.810811    50.8411
12          James Buchanan              4.0  ...    58.783784    45.2832
13         Abraham Lincoln              4.0  ...    59.405941    39.8225
14        Ulysses S. Grant              8.0  ...    72.789116    52.6637
15     Rutherford B. Hayes              4.0  ...    50.135501    47.9527
16       James A. Garfield              0.5  ...    57.994580    48.2731
17        Grover Cleveland              4.0  ...    54.613466    48.5049
18       Benjamin Harrison              4.0  ...    58.104738    47.8234
19        Grover Cleveland              4.0  ...    62.387387    46.0504
20        William McKinley              4.0  ...    60.626398     51.009
21     William Howard Taft              4.0  ...    66.459627    51.5783
22          Woodrow Wilson              8.0  ...    81.920904    41.8401
23       Warren G. Harding              2.0  ...    76.082863    60.3029
24          Herbert Hoover              4.0  ...    83.615819       58.2
25      Franklin Roosevelt             12.0  ...    88.888889    57.4223
26    Dwight D. Eisenhower              8.0  ...    83.239171    55.1349
27         John F. Kennedy              3.0  ...    56.424581    49.7194
28        Richard M. Nixon              5.0  ...    55.947955    43.4203
29            Jimmy Carter              4.0  ...    55.204461    50.0648
30           Ronald Reagan              8.0  ...    90.892193    50.7473
31             George Bush              4.0  ...    79.182156    53.3779
32            Bill Clinton              8.0  ...    68.773234    43.0063
33          George W. Bush              8.0  ...    50.371747     47.867
34            Barack Obama              NaN  ...    67.843866    53.6875

[35 rows x 15 columns]

Kolon adları:
Index(['President', 'Years in office', 'Year first inaugurated',
       'Age at inauguration', 'State elected from', '# of electoral votes',
       '# of popular votes', 'National total votes', 'Total electoral votes',
       'Rating points', 'Political Party', 'Occupation', 'College',
       '% electoral', '% popular'],
      dtype='object')
-------------------------------------------------------------------------------

Başkanlar seçili kolonlar dökümü:
                 President  Year first inaugurated  Years in office % popular
0        George Washington                    1789              8.0      NA()
1               John Adams                    1797              4.0      NA()
2         Thomas Jefferson                    1801              8.0      NA()
3            James Madison                    1809              8.0      NA()
4             James Monroe                    1817              8.0      NA()
5        John Quincy Adams                    1825              4.0      NA()
6           Andrew Jackson                    1829              8.0   55.9706
7        Martin Van Buren                     1837              4.0   50.8253
8   William Henry Harrison                    1841              0.8   52.8811
9            James K. Polk                    1845              4.0   49.5437
10          Zachary Taylor                    1849              1.0    47.284
11         Franklin Pierce                    1853              4.0   50.8411
12          James Buchanan                    1857              4.0   45.2832
13         Abraham Lincoln                    1861              4.0   39.8225
14        Ulysses S. Grant                    1869              8.0   52.6637
15     Rutherford B. Hayes                    1877              4.0   47.9527
16       James A. Garfield                    1881              0.5   48.2731
17        Grover Cleveland                    1885              4.0   48.5049
18       Benjamin Harrison                    1889              4.0   47.8234
19        Grover Cleveland                    1893              4.0   46.0504
20        William McKinley                    1897              4.0    51.009
21     William Howard Taft                    1909              4.0   51.5783
22          Woodrow Wilson                    1913              8.0   41.8401
23       Warren G. Harding                    1921              2.0   60.3029
24          Herbert Hoover                    1929              4.0      58.2
25      Franklin Roosevelt                    1933             12.0   57.4223
26    Dwight D. Eisenhower                    1953              8.0   55.1349
27         John F. Kennedy                    1961              3.0   49.7194
28        Richard M. Nixon                    1969              5.0   43.4203
29            Jimmy Carter                    1977              4.0   50.0648
30           Ronald Reagan                    1981              8.0   50.7473
31             George Bush                    1989              4.0   53.3779
32            Bill Clinton                    1993              8.0   43.0063
33          George W. Bush                    2001              8.0    47.867
34            Barack Obama                    2009              NaN   53.6875
-------------------------------------------------------------------------------

Başkanlar (eksiksiz verili) seçili kolonlar dökümü:
                 President  Year first inaugurated  Years in office % popular
0        George Washington                    1789              8.0      NA()
1               John Adams                    1797              4.0      NA()
2         Thomas Jefferson                    1801              8.0      NA()
3            James Madison                    1809              8.0      NA()
4             James Monroe                    1817              8.0      NA()
5        John Quincy Adams                    1825              4.0      NA()
6           Andrew Jackson                    1829              8.0   55.9706
7        Martin Van Buren                     1837              4.0   50.8253
8   William Henry Harrison                    1841              0.8   52.8811
9            James K. Polk                    1845              4.0   49.5437
10          Zachary Taylor                    1849              1.0    47.284
11         Franklin Pierce                    1853              4.0   50.8411
12          James Buchanan                    1857              4.0   45.2832
13         Abraham Lincoln                    1861              4.0   39.8225
14        Ulysses S. Grant                    1869              8.0   52.6637
15     Rutherford B. Hayes                    1877              4.0   47.9527
16       James A. Garfield                    1881              0.5   48.2731
17        Grover Cleveland                    1885              4.0   48.5049
18       Benjamin Harrison                    1889              4.0   47.8234
19        Grover Cleveland                    1893              4.0   46.0504
20        William McKinley                    1897              4.0    51.009
21     William Howard Taft                    1909              4.0   51.5783
22          Woodrow Wilson                    1913              8.0   41.8401
23       Warren G. Harding                    1921              2.0   60.3029
24          Herbert Hoover                    1929              4.0      58.2
25      Franklin Roosevelt                    1933             12.0   57.4223
26    Dwight D. Eisenhower                    1953              8.0   55.1349
27         John F. Kennedy                    1961              3.0   49.7194
28        Richard M. Nixon                    1969              5.0   43.4203
29            Jimmy Carter                    1977              4.0   50.0648
30           Ronald Reagan                    1981              8.0   50.7473
31             George Bush                    1989              4.0   53.3779
32            Bill Clinton                    1993              8.0   43.0063
33          George W. Bush                    2001              8.0    47.867
-------------------------------------------------------------------------------

En kısa görev süresi: 0.5
En uzun görev süresi: 12.0
Bugüne kadarki toplam görev süresi: 176.3
"""