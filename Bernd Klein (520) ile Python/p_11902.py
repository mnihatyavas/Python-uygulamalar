#coding:iso-8859-9 Türkçe
# p_11902.py: Dizge.format() şablonlu biçimli yazdırma örneği.
from random import random, randint

a = randint (0, 10000)
b= random()

print ("Python 'dizge.format()' biçimli print:")

# Konumsal endeksli argümanlar:
şablon = "\na={1:}, b={0:}, a*b={4:}, a/b={3:}, a^b={2:}, a**b={2:.5f}, a-üst-b={2:,.1f}"
dizge = şablon.format (b, a, a**b, a/b, a*b)
print (şablon)
print (dizge)

print ("\na={:,d}  b={:,.2f}  a*b={:,.2f}  a/b={:,.2f}  a^b={:,.2f}" .format (a, b, a*b, a/b, a**b) )

# Anahtar kelimeli argümanlar:
print ("a={a:,d}  b={b:,.2f}  a*b={c:,.2f}  a/b={ç:,.2f}  a^b={d:,.2f}" .format (a=a, ç=a/b, d=a**b, c=a*b, b=b) )

# Sola< veya sağa> hizalamalı biçimleme:
print ("\n{0:>25s}={5:<10,d}\n{1:>25s}={6:<13,.2f}\n{2:^25s}={7:^13,.2f}\n{3:25s}={8:+13,.2f}\n{4:25s}={9:013,.2f}"
    .format ("İlk değer", "İkinci değer", "İki değerin çarpımı", "İki değerin bölümü", "İki değerin negatif üssü", a, b, a*b, a/b, -a**b) )


"""Çıktı:
>python p_11902.py
Python 'dizge.format()' biçimli print:

a={1:}, b={0:}, a*b={4:}, a/b={3:}, a^b={2:}, a**b={2:.5f}, a-üst-b={2:,.1f}

a=7845, b=0.5158575526075859, a*b=4046.9025002065114, a/b=15207.686618805232, a^
b=102.10692244198951, a**b=102.10692, a-üst-b=102.1

a=7,845  b=0.52  a*b=4,046.90  a/b=15,207.69  a^b=102.11
a=7,845  b=0.52  a*b=4,046.90  a/b=15,207.69  a^b=102.11

                İlk değer=7,845
             İkinci değer=0.52
   İki değerin çarpımı   =  4,046.90
İki değerin bölümü       =   +15,207.69
İki değerin negatif üssü =-0,000,102.11
"""