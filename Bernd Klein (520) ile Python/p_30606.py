# coding:iso-8859-9 T�rk�e
# p_30606.py: Numpy.random.choise(dizi,size(s,k),replace=False) ile �ehirler dizisinden tesad�fi yegane (s,k) �ekilli matris se�imi �rne�i.

from random import choice as tercih

�ehirler = ["Berlin", "Hamburg", "M�nih", "Amsterdam", "Londra", "Paris",
    "Z�rih", "Haydelberg", "Strasburg", "Augsburg", "Milano", "Roma", "Madrid",
    "Barselona", "Atina", "Sofya", "SarayBosna", "Tiran", "�stanbul"]

print ("Listedeki ", len (�ehirler), " Avrupa �ehrinden ziyaret tercihim: ", tercih (�ehirler), sep="")
#----------------------------------------------------------------------------------------------------------

from numpy.random import choice as se�ilen

print ("\nListedeki ", len (�ehirler), " Avrupa �ehrinden g�rmeyi se�ti�im: ", se�ilen (�ehirler), sep="")
print ("Listedeki ", len (�ehirler), " Avrupa �ehrinden g�rmeyi se�ti�im ��l� dizi: ", se�ilen (�ehirler, size=3), sep="")
print ("\nListedeki ", len (�ehirler), " Avrupa �ehrinden g�rmeyi se�ti�im (3,4)=onikili matris:\n", se�ilen (�ehirler, size=(3,4)), sep="")
print ("\nListedeki ", len (�ehirler), " Avrupa �ehrinden g�rmeyi se�ti�im yegane (3,4)=onikili matris:\n", se�ilen (�ehirler, size=(3,4), replace=False), sep="")



"""��kt�:
>python p_30606.py
Listedeki 19 Avrupa �ehrinden ziyaret tercihim: Roma

Listedeki 19 Avrupa �ehrinden g�rmeyi se�ti�im: Sofya
Listedeki 19 Avrupa �ehrinden g�rmeyi se�ti�im ��l� dizi: ['Amsterdam' 'Amsterdam' 'Z�rih']

Listedeki 19 Avrupa �ehrinden g�rmeyi se�ti�im (3,4)=onikili matris:
[['SarayBosna' 'Hamburg' 'Hamburg' 'Hamburg']
 ['Amsterdam' 'SarayBosna' 'Milano' 'Paris']
 ['Madrid' 'Haydelberg' 'Haydelberg' 'Z�rih']]

Listedeki 19 Avrupa �ehrinden g�rmeyi se�ti�im yegane (3,4)=onikili matris:
[['Atina' 'Berlin' 'Amsterdam' 'M�nih']
 ['Sofya' 'Haydelberg' 'Tiran' '�stanbul']
 ['Paris' 'Augsburg' 'Z�rih' 'Barselona']]
"""