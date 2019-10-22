#coding:iso-8859-9 T�rk�e
# p_32203.py: Marketlerin y�l ve ayl�k sat�� birle�ik veri �er�evesi �rne�i.

import pandas as pd

market1 = {
    2017:{"ocak":23, "�ubat":25, "mart":24},
    2018:{"ocak":21, "�ubat":19, "mart":20},
    2019:{"ocak":27, "�ubat":23, "mart":24} }
market2 = {
    2017:{"ocak":56, "�ubat":50, "mart":52},
    2018:{"ocak":62, "�ubat":59, "mart":60},
    2019:{"ocak":57, "�ubat":43, "mart":54} }
market3 = {
    2017:{"ocak":251, "�ubat":235, "mart":252},
    2018:{"ocak":262, "�ubat":259, "mart":260},
    2019:{"ocak":257, "�ubat":243, "mart":254} }

v�1 = pd.DataFrame (market1).reindex (index=["ocak", "�ubat", "mart"])
v�2 = pd.DataFrame (market2).reindex (index=("ocak", "�ubat", "mart"))
v�3 = pd.DataFrame (market3).reindex (index=("ocak", "�ubat", "mart"))

t�mMarketler = v�1 + v�2 + v�3

print ("Market-1 sat��lar�:\n", v�1, sep="")

print ("\nHer 3 market sat��lar�:\n", t�mMarketler, sep="")
print ("\nYeniden-endeksli her 3 market sat��lar�:\n", t�mMarketler.reindex (index=("mart", "�ubat", "ocak")), sep="")
print ("\nHer 3 marketin 2 y�l ve 2 ayl�k sat��lar�:\n", t�mMarketler.reindex (columns=(2018, 2019), index=("ocak", "�ubat")), sep="")
print ("-"*46)
#--------------------------------------------------------------------------------------------------------

marketler1 = pd.concat ([v�1, v�2, v�3], keys=["Market-1", "Market-2", "Market-3"])
print ("\nMarketlerin birle�ik toplam sat��lar�:\n", marketler1, sep="")
print ("-"*46)
#--------------------------------------------------------------------------------------------------------

marketler2 = pd.concat ([v�1.T, v�2.T, v�3.T], keys=["Market-1", "Market-2", "Market-3"])
print ("\n�evrili marketlerin birle�ik toplam sat��lar�:\n", marketler2, sep="")



"""��kt�:
>python p_32203.py
Market-1 sat��lar�:
       2017  2018  2019
ocak     23    21    27
�ubat    25    19    23
mart     24    20    24

Her 3 market sat��lar�:
       2017  2018  2019
ocak    330   345   341
�ubat   310   337   309
mart    328   340   332

Yeniden-endeksli her 3 market sat��lar�:
       2017  2018  2019
mart    328   340   332
�ubat   310   337   309
ocak    330   345   341

Her 3 marketin 2 y�l ve 2 ayl�k sat��lar�:
       2018  2019
ocak    345   341
�ubat   337   309
----------------------------------------------

Marketlerin birle�ik toplam sat��lar�:
                2017  2018  2019
Market-1 ocak     23    21    27
         �ubat    25    19    23
         mart     24    20    24
Market-2 ocak     56    62    57
         �ubat    50    59    43
         mart     52    60    54
Market-3 ocak    251   262   257
         �ubat   235   259   243
         mart    252   260   254
----------------------------------------------

�evrili marketlerin birle�ik toplam sat��lar�:
               ocak  �ubat  mart
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