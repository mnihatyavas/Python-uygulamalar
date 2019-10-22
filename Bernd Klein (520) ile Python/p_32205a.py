#coding:iso-8859-9 Türkçe
# p_32205a.py: Filimler excel yaygın-sayfa örneği.

#pip install xlrd
#Successfully installed xlrd-1.2.0

#pip install xlwt
#Successfully installed xlwt-1.3.0

#>python -m pip install --upgrade pip
#Successfully uninstalled pip-19.1.1
#Successfully installed pip-19.2.1

import pandas as pd

egzelDosyası = "p_32205ax1.xls" # 1900s, 2000s ve 2010s filimler...

filimler = pd.read_excel (egzelDosyası)
print ("Filimler egzel dosyasının baştan 5 filmi:\n", filimler.head(), sep="")
print ("-"*75)
#---------------------------------------------------------------------------------------------------------

yaygınSayfalar = pd.ExcelFile (egzelDosyası)

döküman = {}
for yaygınSayfa in yaygınSayfalar.sheet_names: döküman [yaygınSayfa] = yaygınSayfalar.parse (yaygınSayfa)
for ys in döküman: print ("\nYaygın sayfanın adı: " + ys + "==>\n", döküman [ys].head(), sep="")
print ("-"*75)
#---------------------------------------------------------------------------------------------------------

ys1 = pd.read_excel (egzelDosyası, sheet_name="1900s")
ys2 = pd.read_excel (egzelDosyası, sheet_name="2000s")
#ys3 = pd.read_excel (egzelDosyası, sheet_name="2010s")

print ("\n1900s sayfası son-5 filimleri:\n", ys1.tail(), sep="")
print ("\n2000s sayfası son-5 filimleri:\n", ys2.tail(), sep="")
print ("\n2010s sayfası son-5 filimleri:\n", döküman ["2010s"].tail(), sep="")
print ("-"*75)
#---------------------------------------------------------------------------------------------------------

ys1 = pd.read_excel (egzelDosyası, sheet_name=0, index_col=0)
ys2 = pd.read_excel (egzelDosyası, sheet_name=1, index_col=0)
ys3 = pd.read_excel (egzelDosyası, sheet_name=2, index_col=0)
filimler = pd.concat ([ys1, ys2, ys3])
print ("\nFilimler veri çerçevesinin şekli:", filimler.shape)
print ("\nToplam: ", filimler.shape [0], " adet birleşik filmin [4905:4915] listesi:\n", filimler [4905:4915], sep="")
print ("-"*75)
#---------------------------------------------------------------------------------------------------------

ys_lar = pd.ExcelFile (egzelDosyası)
filimSayfaları = []
for sayfa in ys_lar.sheet_names:
    filimSayfaları.append (ys_lar.parse (sayfa))
    filimler = pd.concat (filimSayfaları)
print ("\nİlk ve son filimler:\n", filimler [0:1], "\n", filimler [-2:-1], sep="")
print ("-"*75)
#---------------------------------------------------------------------------------------------------------

hasılatSıralı = filimler.sort_values (['Gross Earnings'], ascending=False)
print ("\nHasılat rekoruyla sıralı ilk 10 filim:\n", hasılatSıralı ["Gross Earnings"].head (10), sep="")
print ("-"*75)
#---------------------------------------------------------------------------------------------------------

print ("\nFilimlerin genel tasviri:\n", filimler.describe(), sep="")
print ("-"*75)
#---------------------------------------------------------------------------------------------------------

filimler["Net Hasılat"] = filimler ["Gross Earnings"] - filimler ["Budget"]
hasılatSıralı = filimler.sort_values (["Net Hasılat"], ascending=False)
print ("Net hasılat rekoruyla sıralı ilk 10 filim:\n", hasılatSıralı.head (10), sep="")
print ("-"*75)
#---------------------------------------------------------------------------------------------------------

print ("\nFilimler yaygın sayfası kolon adları:\n", filimler.columns, sep="")
print ("-"*75)
#---------------------------------------------------------------------------------------------------------

if (input ("\nExcel dosyası saklansın mı? ") == "e"):
    filimler.to_excel ("p_32205ax2.xls")
    #filimler.to_excel ("p_32205ax2.xls", index=False)

filimler2 = pd.read_excel ("p_32205ax2.xls")
print ("\nİlk 10 filim:\n", filimler2 [["Year", "Title", "IMDB Score"]].head (10), sep="")



"""Çıktı:
>python p_32205a.py
Filimler egzel dosyasının baştan 5 filmi:
                                               Title  ...  IMDB Score
0  Intolerance: Love's Struggle Throughout the Ages   ...         8.0
1                    Over the Hill to the Poorhouse   ...         4.8
2                                    The Big Parade   ...         8.3
3                                        Metropolis   ...         8.3
4                                     Pandora's Box   ...         8.0

[5 rows x 25 columns]
---------------------------------------------------------------------------

Yaygın sayfanın adı: 1900s==>
                                               Title  ...  IMDB Score
0  Intolerance: Love's Struggle Throughout the Ages   ...         8.0
1                    Over the Hill to the Poorhouse   ...         4.8
2                                    The Big Parade   ...         8.3
3                                        Metropolis   ...         8.3
4                                     Pandora's Box   ...         8.0

[5 rows x 25 columns]

Yaygın sayfanın adı: 2000s==>
                    Title  Year  ... Reviews by Crtiics IMDB Score
0         102 Dalmatians   2000  ...               84.0        4.8
1                28 Days   2000  ...              116.0        6.0
2              3 Strikes   2000  ...               22.0        4.0
3               Aberdeen   2000  ...               28.0        7.3
4  All the Pretty Horses   2000  ...               85.0        5.8

[5 rows x 25 columns]

Yaygın sayfanın adı: 2010s==>
                                  Title    Year  ... Reviews by Crtiics IMDB Score
0                            127 Hours   2010.0  ...              450.0        7.6
1                          3 Backyards   2010.0  ...               20.0        5.2
2                                    3   2010.0  ...               76.0        6.8
3            8: The Mormon Proposition   2010.0  ...               28.0        7.1
4  A Turtle's Tale: Sammy's Adventures   2010.0  ...               56.0        6.1

[5 rows x 25 columns]
---------------------------------------------------------------------------

1900s sayfası son-5 filimleri:
                               Title  Year  ... Reviews by Crtiics IMDB Score
1333               Twin Falls Idaho   1999  ...               54.0        7.3
1334  Universal Soldier: The Return   1999  ...               75.0        4.1
1335                  Varsity Blues   1999  ...               67.0        6.4
1336                 Wild Wild West   1999  ...               85.0        4.8
1337                 Wing Commander   1999  ...               85.0        4.1

[5 rows x 25 columns]

2000s sayfası son-5 filimleri:
                                  Title  Year  ... Reviews by Crtiics IMDB Score
2095          X-Men Origins: Wolverine   2009  ...              350.0        6.7
2096                          Year One   2009  ...              170.0        4.9
2097                   Youth in Revolt   2009  ...              192.0        6.5
2098  ZMD: Zombies of Mass Destruction   2009  ...               64.0        5.1
2099                        Zombieland   2009  ...              445.0        7.7

[5 rows x 25 columns]

2010s sayfası son-5 filimleri:
                                     Title  ...  IMDB Score
1599              War & Peace               ...         8.2
1600                    Wings               ...         7.3
1601               Wolf Creek               ...         7.1
1602        Wuthering Heights               ...         7.7
1603  Yu-Gi-Oh! Duel Monsters               ...         7.0

[5 rows x 25 columns]
---------------------------------------------------------------------------

Filimler veri çerçevesinin şekli: (5042, 24)

Toplam: 5042 adet birleşik filmin [4905:4915] listesi:
                               Year  ... IMDB Score
Title                                ...
The Birth of a Nation        2016.0  ...        5.4
The Boss                     2016.0  ...        5.3
The Boy                      2016.0  ...        6.0
The Conjuring 2              2016.0  ...        7.8
The Dog Lover                2016.0  ...        4.8
The Finest Hours             2016.0  ...        6.8
The Forest                   2016.0  ...        4.8
The Huntsman: Winter's War   2016.0  ...        6.1
The Infiltrator              2016.0  ...        7.3
The Jungle Book              2016.0  ...        7.8

[10 rows x 24 columns]
---------------------------------------------------------------------------

İlk ve son filimler:
                                               Title  ...  IMDB Score
0  Intolerance: Love's Struggle Throughout the Ages   ...         8.0
[1 rows x 25 columns]

                               Title  Year  ... Reviews by Crtiics IMDB Score
1602  Wuthering Heights                NaN  ...                9.0        7.7
[1 rows x 25 columns]
---------------------------------------------------------------------------

Hasılat rekoruyla sıralı ilk 10 filim:
1867    760505847.0
1027    658672302.0
1263    652177271.0
610     623279547.0
611     623279547.0
1774    533316061.0
1281    474544677.0
226     460935665.0
1183    458991599.0
618     448130642.0
Name: Gross Earnings, dtype: float64
---------------------------------------------------------------------------

Filimlerin genel tasviri:
              Year     Duration  ...  Reviews by Crtiics   IMDB Score
count  4935.000000  5028.000000  ...         4993.000000  5042.000000
mean   2002.470517   107.201074  ...          140.194272     6.442007
std      12.474599    25.197441  ...          121.601675     1.125189
min    1916.000000     7.000000  ...            1.000000     1.600000
25%    1999.000000    93.000000  ...           50.000000     5.800000
50%    2005.000000   103.000000  ...          110.000000     6.600000
75%    2011.000000   118.000000  ...          195.000000     7.200000
max    2016.000000   511.000000  ...          813.000000     9.500000

[8 rows x 16 columns]
---------------------------------------------------------------------------
Net hasılat rekoruyla sıralı ilk 10 filim:
                                           Title  ...  Net Hasılat
1867                                     Avatar   ...  523505847.0
1263                             Jurassic World   ...  502177271.0
1027                                    Titanic   ...  458672302.0
226          Star Wars: Episode IV - A New Hope   ...  449935665.0
328                  E.T. the Extra-Terrestrial   ...  424449459.0
610                                The Avengers   ...  403279547.0
611                                The Avengers   ...  403279547.0
737                               The Lion King   ...  377783777.0
1281  Star Wars: Episode I - The Phantom Menace   ...  359544677.0
1774                            The Dark Knight   ...  348316061.0

[10 rows x 26 columns]
---------------------------------------------------------------------------

Filimler yaygın sayfası kolon adları:
Index(['Title', 'Year', 'Genres', 'Language', 'Country', 'Content Rating',
       'Duration', 'Aspect Ratio', 'Budget', 'Gross Earnings', 'Director',
       'Actor 1', 'Actor 2', 'Actor 3', 'Facebook Likes - Director',
       'Facebook Likes - Actor 1', 'Facebook Likes - Actor 2',
       'Facebook Likes - Actor 3', 'Facebook Likes - cast Total',
       'Facebook likes - Movie', 'Facenumber in posters', 'User Votes',
       'Reviews by Users', 'Reviews by Crtiics', 'IMDB Score', 'Net Hasılat'],
      dtype='object')
---------------------------------------------------------------------------

Excel dosyası saklansın mı?

İlk 10 filim:
     Year                                              Title  IMDB Score
0  1916.0  Intolerance: Love's Struggle Throughout the Ages          8.0
1  1920.0                    Over the Hill to the Poorhouse          4.8
2  1925.0                                    The Big Parade          8.3
3  1927.0                                        Metropolis          8.3
4  1929.0                                     Pandora's Box          8.0
5  1929.0                               The Broadway Melody          6.3
6  1930.0                                     Hell's Angels          7.8
7  1932.0                                A Farewell to Arms          6.6
8  1933.0                                       42nd Street          7.7
9  1933.0                                She Done Him Wrong          6.5
"""