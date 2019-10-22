# coding:iso-8859-9 Türkçe
# p_14205.py: Eklemeli çarpmalı işlemlerle farklı paraları baştaki birime çevirme örneği.

from p_14205x import ParaBirimleri
"""
url = "https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote"
çevrimiçinden "from exchange_rates(.py) import get_currency_rates" güncel kurlar
alınıp ParaBirimleri sınıf nesnesi içinde aktüel kullanılabilir.
"""

x1 = ParaBirimleri (10.00, "EUR")
x2 = ParaBirimleri (10.00, "GBP")
print (x1 + x2)

x3 = ParaBirimleri (10, "JPY")
x4 = ParaBirimleri (10, "USD")
x5 = ParaBirimleri (10, "CAD")
print (x4 + x1 + x3 + x2 + x5)

lira = ParaBirimleri (10, "TL")
print (lira + 2*x1 + x2*0.92 + 1.5*x3 + 0.25*x4 + 0.85*x5)
print (1.5*x3 + lira + 2*x1 + x2*0.92 + 0.25*x4 + 0.85*x5)
print (10*ParaBirimleri (0, "GBP") + 1.5*x3 + lira + 2*x1 + x2*0.92 + 0.25*x4 + 0.85*x5)



"""Çıktı:
>python p_14205.py
21.22 EUR
41.14 USD
263.97 TL
4566.51 JPY
35.60 GBP
"""