# coding:iso-8859-9 T�rk�e
# p_14202.py: ��lemciler do�rultusunda add, iadd, radd metodlar�yla toplay�p metreye �evirme �rne�i.

from p_14202x import Uzunluk

U = Uzunluk

print ("(2.56m + 3yd + 7.8in + 7.03cm + 0.25m) = ",
    U (2.56, "m") + U (3, "yd") + U (7.8, "in") + U (7.03, "cm") + 0.25, " metre", sep="")
print ("(1mm + 1cm + 1m + 1km + 1in + 1ft + 1yd + 1mi) = ",
    U(1,"mm")+U(1,"cm")+U(1,"m")+U(1,"km")+
    U(1,"in")+U(1,"ft")+U(1,"yd")+U(1,"mi"), " metre", sep="")

x = U (1)
x += U (1.75) # __iadd__ metoduyla (�ncekine) eklemeli art�r�r...
x += U (1.25, "yd")
x += U (3.45, "ft")
x += 0.25
print ("\n(1m + 1.75m + 1.25yd + 3.45ft + 0.25m) =", x, "metre")

y = U (3, "yd") + 5
y += 5 + U (3, "yd") # __radd__ metodunu __iadd__ ile kullan�r...
print ("\n(3yd + 5m + 5m + 3yd =", y, "metre")



"""��kt�:
>python p_14202.py
(2.56m + 3yd + 7.8in + 7.03cm + 0.25m) = 5.82162 metre
(1mm + 1cm + 1m + 1km + 1in + 1ft + 1yd + 1mi) = 2611.5996 metre

(1m + 1.75m + 1.25yd + 3.45ft + 0.25m) = 5.19456 metre

(3yd + 5m + 5m + 3yd = 15.4864 metre
"""