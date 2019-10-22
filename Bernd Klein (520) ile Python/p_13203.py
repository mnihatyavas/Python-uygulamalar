# coding:iso-8859-9 T�rk�e
# p_13203.py: list(map(lambda fonk, arg�man))'la arg�manlar� fonksiyonda haritaland�r�p listeleme �rne�i.

a = [1, 2, 3, 4, 5]
b = [17, 12, 11, 10, -7]
c = [-1, -4, 5, 9] # ��lemlerdeki s�zkonusu listelerin k�sas� esas al�n�r...
d = [4.13, -3.94, 8, 0, -7, 6.9]

print ("'x+y' denklemiyle haritalanan liste:", list (map (lambda x, y : x+y, a,b)) )
print ("'x+y+z' denklemiyle haritalanan liste:", list (map (lambda x, y, z : x+y+z, a, b, c)) )
print ("'2.5*x + 2*y - z' denklemiyle haritalanan liste:", list (map (lambda x, y, z : 2.5*x + 2*y - z, a, b, c)) )
print ("'2.5*a**4 + 2*b**3 - 7*c**2 + 1.5*d - 8' denklemiyle haritalanan liste:", list (map (lambda a, b, c, d : 2.5*a**4 + 2*b**3 - 7*c**2 + 1.5*d - 8, a,b,c,d)) )

"""��kt�:
>python p_13203.py
'x+y' denklemiyle haritalanan liste: [18, 14, 14, 14, -2]
'x+y+z' denklemiyle haritalanan liste: [17, 10, 19, 23]
'2.5*x + 2*y - z' denklemiyle haritalanan liste: [37.5, 33.0, 24.5, 21.0]
'2.5*a**4 + 2*b**3 - 7*c**2 + 1.5*d - 8' denklemiyle haritalanan liste: [9819.695, 3370.09, 2693.5, 2065.0]
"""