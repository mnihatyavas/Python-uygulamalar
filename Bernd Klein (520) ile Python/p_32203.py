#coding:iso-8859-9 Türkçe
# p_32203.py: Marketlerin yıl ve aylık satış birleşik veri çerçevesi örneği.

import pandas as pd

market1 = {
    2017:{"ocak":23, "şubat":25, "mart":24},
    2018:{"ocak":21, "şubat":19, "mart":20},
    2019:{"ocak":27, "şubat":23, "mart":24} }
market2 = {
    2017:{"ocak":56, "şubat":50, "mart":52},
    2018:{"ocak":62, "şubat":59, "mart":60},
    2019:{"ocak":57, "şubat":43, "mart":54} }
market3 = {
    2017:{"ocak":251, "şubat":235, "mart":252},
    2018:{"ocak":262, "şubat":259, "mart":260},
    2019:{"ocak":257, "şubat":243, "mart":254} }

vç1 = pd.DataFrame (market1).reindex (index=["ocak", "şubat", "mart"])
vç2 = pd.DataFrame (market2).reindex (index=("ocak", "şubat", "mart"))
vç3 = pd.DataFrame (market3).reindex (index=("ocak", "şubat", "mart"))

tümMarketler = vç1 + vç2 + vç3

print ("Market-1 satışları:\n", vç1, sep="")

print ("\nHer 3 market satışları:\n", tümMarketler, sep="")
print ("\nYeniden-endeksli her 3 market satışları:\n", tümMarketler.reindex (index=("mart", "şubat", "ocak")), sep="")
print ("\nHer 3 marketin 2 yıl ve 2 aylık satışları:\n", tümMarketler.reindex (columns=(2018, 2019), index=("ocak", "şubat")), sep="")
print ("-"*46)
#--------------------------------------------------------------------------------------------------------

marketler1 = pd.concat ([vç1, vç2, vç3], keys=["Market-1", "Market-2", "Market-3"])
print ("\nMarketlerin birleşik toplam satışları:\n", marketler1, sep="")
print ("-"*46)
#--------------------------------------------------------------------------------------------------------

marketler2 = pd.concat ([vç1.T, vç2.T, vç3.T], keys=["Market-1", "Market-2", "Market-3"])
print ("\nÇevrili marketlerin birleşik toplam satışları:\n", marketler2, sep="")



"""Çıktı:
>python p_32203.py
Market-1 satışları:
       2017  2018  2019
ocak     23    21    27
şubat    25    19    23
mart     24    20    24

Her 3 market satışları:
       2017  2018  2019
ocak    330   345   341
şubat   310   337   309
mart    328   340   332

Yeniden-endeksli her 3 market satışları:
       2017  2018  2019
mart    328   340   332
şubat   310   337   309
ocak    330   345   341

Her 3 marketin 2 yıl ve 2 aylık satışları:
       2018  2019
ocak    345   341
şubat   337   309
----------------------------------------------

Marketlerin birleşik toplam satışları:
                2017  2018  2019
Market-1 ocak     23    21    27
         şubat    25    19    23
         mart     24    20    24
Market-2 ocak     56    62    57
         şubat    50    59    43
         mart     52    60    54
Market-3 ocak    251   262   257
         şubat   235   259   243
         mart    252   260   254
----------------------------------------------

Çevrili marketlerin birleşik toplam satışları:
               ocak  şubat  mart
Market-1 2017    23     25    24
         2018    21     19    20
         2019    27     23    24
Market-2 2017    56     50    52
         2018    62     59    60
         2019    57     43    54
Market-3 2017   251    235   252
         2018   262    259   260
         2019   257    243   254
"""