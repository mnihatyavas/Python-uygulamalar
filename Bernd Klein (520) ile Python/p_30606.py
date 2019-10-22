# coding:iso-8859-9 Türkçe
# p_30606.py: Numpy.random.choise(dizi,size(s,k),replace=False) ile şehirler dizisinden tesadüfi yegane (s,k) şekilli matris seçimi örneği.

from random import choice as tercih

şehirler = ["Berlin", "Hamburg", "Münih", "Amsterdam", "Londra", "Paris",
    "Zürih", "Haydelberg", "Strasburg", "Augsburg", "Milano", "Roma", "Madrid",
    "Barselona", "Atina", "Sofya", "SarayBosna", "Tiran", "İstanbul"]

print ("Listedeki ", len (şehirler), " Avrupa şehrinden ziyaret tercihim: ", tercih (şehirler), sep="")
#----------------------------------------------------------------------------------------------------------

from numpy.random import choice as seçilen

print ("\nListedeki ", len (şehirler), " Avrupa şehrinden görmeyi seçtiğim: ", seçilen (şehirler), sep="")
print ("Listedeki ", len (şehirler), " Avrupa şehrinden görmeyi seçtiğim üçlü dizi: ", seçilen (şehirler, size=3), sep="")
print ("\nListedeki ", len (şehirler), " Avrupa şehrinden görmeyi seçtiğim (3,4)=onikili matris:\n", seçilen (şehirler, size=(3,4)), sep="")
print ("\nListedeki ", len (şehirler), " Avrupa şehrinden görmeyi seçtiğim yegane (3,4)=onikili matris:\n", seçilen (şehirler, size=(3,4), replace=False), sep="")



"""Çıktı:
>python p_30606.py
Listedeki 19 Avrupa şehrinden ziyaret tercihim: Roma

Listedeki 19 Avrupa şehrinden görmeyi seçtiğim: Sofya
Listedeki 19 Avrupa şehrinden görmeyi seçtiğim üçlü dizi: ['Amsterdam' 'Amsterdam' 'Zürih']

Listedeki 19 Avrupa şehrinden görmeyi seçtiğim (3,4)=onikili matris:
[['SarayBosna' 'Hamburg' 'Hamburg' 'Hamburg']
 ['Amsterdam' 'SarayBosna' 'Milano' 'Paris']
 ['Madrid' 'Haydelberg' 'Haydelberg' 'Zürih']]

Listedeki 19 Avrupa şehrinden görmeyi seçtiğim yegane (3,4)=onikili matris:
[['Atina' 'Berlin' 'Amsterdam' 'Münih']
 ['Sofya' 'Haydelberg' 'Tiran' 'İstanbul']
 ['Paris' 'Augsburg' 'Zürih' 'Barselona']]
"""