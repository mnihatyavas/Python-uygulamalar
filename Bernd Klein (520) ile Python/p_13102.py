# coding:iso-8859-9 Türkçe
# p_13102.py: re.compile(kalıp).findall(dizge) ile İngiliz doğru PK'ları bulma örneği.

import re

kalıp = r"[A-z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}"
adresler = "SW1A 0AA: Avam Kamarası, SW1A 1AA: Buckingham Sarayı, SW1A 2AA: Downing Caddesi, BX3 2BB: Barclays Bankası, DH98 1BT: Britanya Telekomünikasyonu, N1 9GU: Guardian Gazatesi, E98 1TT: The Times Meydanı, TIM E22: Sahte postakodu, A B1 A22: Sahte postakodu, EC2N 2DB: Alman Deutsche Bank, SE9 2UG: Greenwhich Üniversitesi, N1 0UY: Islington - London, EC1V 8DS: Clerkenwell - Londra, WC1X 9DT, B42 1LG: Birmingham, B28 9AD: Birmingham, W12 7RJ: Londra BBC Haber Merkezi, BBC 007: Sahte postakodu"
derlenenKalıp = re.compile (kalıp)
sonuç = derlenenKalıp.findall (adresler)
print ("Derlenen kalıpla uyumlu arama sonucu listesi:", sonuç)

"""Çıktı:
>python p_13102.py
Derlenen kalıpla uyumlu arama sonucu listesi: ['SW1A 0AA', 'SW1A 1AA', 'SW1A 2AA',
'BX3 2BB', 'DH98 1BT', 'N1 9GU', 'E98 1TT', 'EC2N 2DB', 'SE9 2UG', 'N1 0UY',
'EC1V 8DS', 'WC1X 9DT', 'B42 1LG', 'B28 9AD', 'W12 7RJ']

"""