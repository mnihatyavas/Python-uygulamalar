# coding:iso-8859-9 Türkçe

from urllib.request import urlopen

internet_sayfası = urlopen ("https://www.qnbfinansbank.enpara.com/")
htmlMetni = internet_sayfası.read().decode()

open ("mny1.html", "w").write (htmlMetni)
# mny1.htm dosyasını herhangibir tarayıcıyla "Birlikte Aç"