# coding:iso-8859-9 T�rk�e
# p_13102.py: re.compile(kal�p).findall(dizge) ile �ngiliz do�ru PK'lar� bulma �rne�i.

import re

kal�p = r"[A-z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}"
adresler = "SW1A 0AA: Avam Kamaras�, SW1A 1AA: Buckingham Saray�, SW1A 2AA: Downing Caddesi, BX3 2BB: Barclays Bankas�, DH98 1BT: Britanya Telekom�nikasyonu, N1 9GU: Guardian Gazatesi, E98 1TT: The Times Meydan�, TIM E22: Sahte postakodu, A B1 A22: Sahte postakodu, EC2N 2DB: Alman Deutsche Bank, SE9 2UG: Greenwhich �niversitesi, N1 0UY: Islington - London, EC1V 8DS: Clerkenwell - Londra, WC1X 9DT, B42 1LG: Birmingham, B28 9AD: Birmingham, W12 7RJ: Londra BBC Haber Merkezi, BBC 007: Sahte postakodu"
derlenenKal�p = re.compile (kal�p)
sonu� = derlenenKal�p.findall (adresler)
print ("Derlenen kal�pla uyumlu arama sonucu listesi:", sonu�)

"""��kt�:
>python p_13102.py
Derlenen kal�pla uyumlu arama sonucu listesi: ['SW1A 0AA', 'SW1A 1AA', 'SW1A 2AA',
'BX3 2BB', 'DH98 1BT', 'N1 9GU', 'E98 1TT', 'EC2N 2DB', 'SE9 2UG', 'N1 0UY',
'EC1V 8DS', 'WC1X 9DT', 'B42 1LG', 'B28 9AD', 'W12 7RJ']

"""