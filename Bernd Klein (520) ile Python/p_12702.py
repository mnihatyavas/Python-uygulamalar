# coding:iso-8859-9 Türkçe
# p_12702.py: Metin dosyasını seek, tell, read'le kontrollü okuma, yazma ve silme örneği.

dosya = open ("p_12701x.txt", "r")

print ("Dosyanın baştan sona birer aralıklı karakter-karakter okunması:")
i=0
while True:
    i +=1
    k = dosya.read (1)
    if k == "": break
    elif k == "\n":
        i +=1
        print()
    else: print (k, end=" ")
    dosya.seek (i)
print ("\n", "_"*75, "\n", sep="")
#----------------------------------------------------------------------------------------------------------

print ("==>Dosyanın ilk 25 karakteri ve son konumu:", dosya.seek (0), dosya.read (25), dosya.tell() )
print ("==>Dosyanın sonraki 25 karakteri ve son konumu:", dosya.seek (dosya.tell()-1 ), dosya.read (25), dosya.tell() )
# seek ve tell arasındaki 1 farkın telafisi unutulmamalı, yoksa konumunuz çorbaya döner...
print ("==>Dosyanın sondan önceki 10 karakteri ve son konumu:", dosya.seek (dosya.tell()-11), dosya.read (10), dosya.tell() )
dosya.close()
print ("\n", "_"*75, "\n", sep="")
#----------------------------------------------------------------------------------------------------------

dosya = open ('örnek2.txt', 'w+')
dosya.write ('Renk: Kahverengi')

print ("\nYeni bir dosyaya, önce 'Kahverengi', sonra da silip 'Yeşil' yazıyoruz:")
dosya.seek (0)
print (dosya.read() )
dosya.seek (6)
print (dosya.read (10) )
print (dosya.tell() )
dosya.seek (6)
dosya.write ('Limon')
dosya.seek (0)
print (dosya.read() )
dosya.close()

import os
os.remove ("örnek2.txt")


"""Çıktı:
>python p_12702.py
Dosyanın baştan sona birer aralıklı karakter-karakter okunması:
V .   a d   L e s b i a m

V I V A M U S   m e a   L e s b i a ,   a t q u e   a m e m u s ,
r u m o r e s q u e   s e n u m   s e v e r i o r u m
o m n e s   u n i u s   a e s t i m e m u s   a s s i s !
s o l e s   o c c i d e r e   e t   r e d i r e   p o s s u n t :
n o b i s   c u m   s e m e l   o c c i d i t   b r e u i s   l u x ,
n o x   e s t   p e r p e t u a   u n a   d o r m i e n d a .
d a   m i   b a s i a   m i l l e ,   d e i n d e   c e n t u m ,
d e i n   m i l l e   a l t e r a ,   d e i n   s e c u n d a   c e n t u m ,
d e i n d e   u s q u e   a l t e r a   m i l l e ,   d e i n d e   c e n t u m .
d e i n ,   c u m   m i l i a   m u l t a   f e c e r i m u s ,
c o n t u r b a b i m u s   i l l a ,   n e   s c i a m u s ,
a u t   n e   q u i s   m a l u s   i n u i d e r e   p o s s i t ,
c u m   t a n t u m   s c i a t   e s s e   b a s i o r u m .
( G A I U S   V A L E R I U S   C A T U L L U S )
___________________________________________________________________________

==>Dosyanın ilk 25 karakteri ve son konumu: 0 V. ad Lesbiam VIVAMUS me 27
==>Dosyanın sonraki 25 karakteri ve son konumu: 26 ea Lesbia, atque amemus, 52
==>Dosyanın sondan önceki 10 karakteri ve son konumu: 41 e amemus, 52
___________________________________________________________________________

Yeni bir dosyaya, önce 'Kahverengi', sonra da silip 'Limon' yazıyoruz:
Renk: Kahverengi
Kahverengi
16
Renk: Limonrengi
"""