# coding:iso-8859-9 T�rk�e

from urllib.request import urlopen

internet_sayfas� = urlopen ("https://www.qnbfinansbank.enpara.com/")
htmlMetni = internet_sayfas�.read().decode()

open ("mny1.html", "w").write (htmlMetni)
# mny1.htm dosyas�n� herhangibir taray�c�yla "Birlikte A�"