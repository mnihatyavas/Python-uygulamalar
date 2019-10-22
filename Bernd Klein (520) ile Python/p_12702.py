# coding:iso-8859-9 T�rk�e
# p_12702.py: Metin dosyas�n� seek, tell, read'le kontroll� okuma, yazma ve silme �rne�i.

dosya = open ("p_12701x.txt", "r")

print ("Dosyan�n ba�tan sona birer aral�kl� karakter-karakter okunmas�:")
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

print ("==>Dosyan�n ilk 25 karakteri ve son konumu:", dosya.seek (0), dosya.read (25), dosya.tell() )
print ("==>Dosyan�n sonraki 25 karakteri ve son konumu:", dosya.seek (dosya.tell()-1 ), dosya.read (25), dosya.tell() )
# seek ve tell aras�ndaki 1 fark�n telafisi unutulmamal�, yoksa konumunuz �orbaya d�ner...
print ("==>Dosyan�n sondan �nceki 10 karakteri ve son konumu:", dosya.seek (dosya.tell()-11), dosya.read (10), dosya.tell() )
dosya.close()
print ("\n", "_"*75, "\n", sep="")
#----------------------------------------------------------------------------------------------------------

dosya = open ('�rnek2.txt', 'w+')
dosya.write ('Renk: Kahverengi')

print ("\nYeni bir dosyaya, �nce 'Kahverengi', sonra da silip 'Ye�il' yaz�yoruz:")
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
os.remove ("�rnek2.txt")


"""��kt�:
>python p_12702.py
Dosyan�n ba�tan sona birer aral�kl� karakter-karakter okunmas�:
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

==>Dosyan�n ilk 25 karakteri ve son konumu: 0 V. ad Lesbiam VIVAMUS me 27
==>Dosyan�n sonraki 25 karakteri ve son konumu: 26 ea Lesbia, atque amemus, 52
==>Dosyan�n sondan �nceki 10 karakteri ve son konumu: 41 e amemus, 52
___________________________________________________________________________

Yeni bir dosyaya, �nce 'Kahverengi', sonra da silip 'Limon' yaz�yoruz:
Renk: Kahverengi
Kahverengi
16
Renk: Limonrengi
"""