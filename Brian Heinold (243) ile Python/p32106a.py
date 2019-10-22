# coding:iso-8859-9 T�rk�e

import re

S = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90,
        'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4,'I':1}

kal�p = re.compile (r"""(?x)
        (M{0,3}) (CM)? (CD)? (D)?
        (C{0,3}) (XC)? (XL)? (L)?
        (X{0,3}) (IX)? (IV)? (V)?
        (I{0,3}) """)

romaRakam� = input ('Roma rakam�n� girin: ').upper()
if romaRakam� == "": romaRakam� = "MCMLVII"
uyan = kal�p.match (romaRakam�)
toplam = 0
for uy in uyan.groups():
    if uy != None and uy != "":
        if uy in ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']: toplam += S[uy]
        elif uy[0] in 'MDCLXVI': toplam += S[uy[0]] * len (uy)

print ("Girdi�iniz <{:s}> roma rakam�n�n ondal�k kar��l���: <{:d}>'dir."
    .format (romaRakam�, toplam) )
