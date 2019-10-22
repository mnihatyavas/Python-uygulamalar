# coding:iso-8859-9 T�rk�e
# p_30712a.py: Zar at��lar�nda �ift, ikiden b�y�k ve birle�ik etkili gelme oranlar� �rne�i.

from random import randint

try: kere = abs (int (input ("Zar ka� kere at�ls�n [10 000]? ")))
except: kere = 10000

t�mAt��lar = [randint (1, 6) for _ in range (kere)]
�iftGelenler = [x for x in t�mAt��lar if x % 2 == 0]
ikidenB�y�kGelenler = [x for x in t�mAt��lar if x > 2]
ikidenb�y�kVe�iftGelenler = [x for x in t�mAt��lar if x % 2 == 0 and x > 2]

print ("\n�ift gelen zarlar�n y�zdesi: %{:.2f}" .format (len (�iftGelenler) / len (t�mAt��lar) * 100))
print ("�kiden b�y�k gelen zarlar�n y�zdesi: %{:.2f}" .format (len (ikidenB�y�kGelenler) / len (t�mAt��lar) * 100))
print ("�kiden b�y�k ve �ift gelen zarlar�n y�zdesi: %{:.2f}" .format (len (ikidenb�y�kVe�iftGelenler) / len (t�mAt��lar) * 100))



"""��kt�:
>python p_30712.py
Zar ka� kere at�ls�n [10 000]?

�ift gelen zarlar�n y�zdesi: %49.88
�kiden b�y�k gelen zarlar�n y�zdesi: %66.27
�kiden b�y�k ve �ift gelen zarlar�n y�zdesi: %32.84

>python p_30712.py  ** TEKRAR **
Zar ka� kere at�ls�n [10 000]? 100

�ift gelen zarlar�n y�zdesi: %48.00
�kiden b�y�k gelen zarlar�n y�zdesi: %69.00
�kiden b�y�k ve �ift gelen zarlar�n y�zdesi: %34.00
"""