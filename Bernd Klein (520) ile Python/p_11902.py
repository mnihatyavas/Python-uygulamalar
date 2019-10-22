#coding:iso-8859-9 T�rk�e
# p_11902.py: Dizge.format() �ablonlu bi�imli yazd�rma �rne�i.
from random import random, randint

a = randint (0, 10000)
b= random()

print ("Python 'dizge.format()' bi�imli print:")

# Konumsal endeksli arg�manlar:
�ablon = "\na={1:}, b={0:}, a*b={4:}, a/b={3:}, a^b={2:}, a**b={2:.5f}, a-�st-b={2:,.1f}"
dizge = �ablon.format (b, a, a**b, a/b, a*b)
print (�ablon)
print (dizge)

print ("\na={:,d}  b={:,.2f}  a*b={:,.2f}  a/b={:,.2f}  a^b={:,.2f}" .format (a, b, a*b, a/b, a**b) )

# Anahtar kelimeli arg�manlar:
print ("a={a:,d}  b={b:,.2f}  a*b={c:,.2f}  a/b={�:,.2f}  a^b={d:,.2f}" .format (a=a, �=a/b, d=a**b, c=a*b, b=b) )

# Sola< veya sa�a> hizalamal� bi�imleme:
print ("\n{0:>25s}={5:<10,d}\n{1:>25s}={6:<13,.2f}\n{2:^25s}={7:^13,.2f}\n{3:25s}={8:+13,.2f}\n{4:25s}={9:013,.2f}"
    .format ("�lk de�er", "�kinci de�er", "�ki de�erin �arp�m�", "�ki de�erin b�l�m�", "�ki de�erin negatif �ss�", a, b, a*b, a/b, -a**b) )


"""��kt�:
>python p_11902.py
Python 'dizge.format()' bi�imli print:

a={1:}, b={0:}, a*b={4:}, a/b={3:}, a^b={2:}, a**b={2:.5f}, a-�st-b={2:,.1f}

a=7845, b=0.5158575526075859, a*b=4046.9025002065114, a/b=15207.686618805232, a^
b=102.10692244198951, a**b=102.10692, a-�st-b=102.1

a=7,845  b=0.52  a*b=4,046.90  a/b=15,207.69  a^b=102.11
a=7,845  b=0.52  a*b=4,046.90  a/b=15,207.69  a^b=102.11

                �lk de�er=7,845
             �kinci de�er=0.52
   �ki de�erin �arp�m�   =  4,046.90
�ki de�erin b�l�m�       =   +15,207.69
�ki de�erin negatif �ss� =-0,000,102.11
"""