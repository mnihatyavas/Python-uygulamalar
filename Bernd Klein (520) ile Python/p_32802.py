#coding:iso-8859-9 T�rk�e
# p_32802.py: Pandas date_range tarih_erimi'yle seri de�erlerine tarih endeksi t�retme �rne�i.

import pandas as pd

endeks = pd.date_range ("2019/8/13", "2019/9/2")
print ("�ki tarih aras� endeks:\n", endeks, sep="")

endeks = pd.date_range (start="13-8-2019", periods=21) # Y�l sondaysa, ilk hane >=13'se g�n, <=12'se ay alg�lar...
print ("\n�lk ba�lang�� tarih ve g�n peryotlu endeks:\n", endeks, sep="")

endeks = pd.date_range (end="2019-9-2", periods=21) # Y�l ba�taysa, 2.haneyi daima ay alg�lar...
print ("\nSon biti� tarih ve g�n peryotlu endeks:\n", endeks, sep="")

endeks = pd.date_range ("2015/12/13", "2016/8/13", freq="M") # M:Month, her aysonu g�nleri...
print ("\n�ki tarih aras� her aysonu endeksi:\n", endeks, sep="")

endeks = pd.date_range ("2019-06-13", "2019-08-13", freq="W-Mon") # Her haftan�n pazartesi g�n�...
print ("\n�ki tarih aras� her haftan�n pazartesi g�n� endeksi:\n", endeks, sep="")

"""freq=
B	business day frequency
C	custom business day frequency (experimental)
D	calendar day frequency
W	weekly frequency
M	month end frequency
BM	business month end frequency
MS	month start frequency
BMS	business month start frequency
Q	quarter end frequency
BQ	business quarter endfrequency
QS	quarter start frequency
BQS	business quarter start frequency
A	year end frequency
BA	business year end frequency
AS	year start frequency
BAS	business year start frequency
H	hourly frequency
T	minutely frequency
S	secondly frequency
L	milliseonds
U	microseconds
"""



"""��kt�:
>python p_32802.py
�ki tarih aras� endeks:
DatetimeIndex(['2019-08-13', '2019-08-14', '2019-08-15', '2019-08-16',
               '2019-08-17', '2019-08-18', '2019-08-19', '2019-08-20',
               '2019-08-21', '2019-08-22', '2019-08-23', '2019-08-24',
               '2019-08-25', '2019-08-26', '2019-08-27', '2019-08-28',
               '2019-08-29', '2019-08-30', '2019-08-31', '2019-09-01',
               '2019-09-02'],
              dtype='datetime64[ns]', freq='D')

�lk ba�lang�� tarih ve g�n peryotlu endeks:
DatetimeIndex(['2019-08-13', '2019-08-14', '2019-08-15', '2019-08-16',
               '2019-08-17', '2019-08-18', '2019-08-19', '2019-08-20',
               '2019-08-21', '2019-08-22', '2019-08-23', '2019-08-24',
               '2019-08-25', '2019-08-26', '2019-08-27', '2019-08-28',
               '2019-08-29', '2019-08-30', '2019-08-31', '2019-09-01',
               '2019-09-02'],
              dtype='datetime64[ns]', freq='D')

Son biti� tarih ve g�n peryotlu endeks:
DatetimeIndex(['2019-08-13', '2019-08-14', '2019-08-15', '2019-08-16',
               '2019-08-17', '2019-08-18', '2019-08-19', '2019-08-20',
               '2019-08-21', '2019-08-22', '2019-08-23', '2019-08-24',
               '2019-08-25', '2019-08-26', '2019-08-27', '2019-08-28',
               '2019-08-29', '2019-08-30', '2019-08-31', '2019-09-01',
               '2019-09-02'],
              dtype='datetime64[ns]', freq='D')

�ki tarih aras� her aysonu endeksi:
DatetimeIndex(['2015-12-31', '2016-01-31', '2016-02-29', '2016-03-31',
               '2016-04-30', '2016-05-31', '2016-06-30', '2016-07-31'],
              dtype='datetime64[ns]', freq='M')

�ki tarih aras� her haftan�n pazartesi g�n� endeksi:
DatetimeIndex(['2019-06-17', '2019-06-24', '2019-07-01', '2019-07-08',
               '2019-07-15', '2019-07-22', '2019-07-29', '2019-08-05',
               '2019-08-12'],
              dtype='datetime64[ns]', freq='W-MON')
"""