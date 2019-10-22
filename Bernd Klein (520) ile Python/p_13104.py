# coding:iso-8859-9 Türkçe
# p_13104.py: re.split'le seçici ayrıştırma ve re.sub'la kelimeleri değiştirme örneği.

import re

başkalaşım = "OF bodies chang'd to various forms, I sing: Ye Gods, from whom these miracles did spring, Inspire my numbers with coelestial heat;..."
print ("Ayrışan noktalamasız sadece harfli kelimeler listesi:", re.split ("\W+", başkalaşım) )
print ("-"*75, "\n")
#---------------------------------------------------------------------------------------------------------

satırlar = ["soyadı: Obama, adı: Barack, mesleği: ABD Başkanı",
    "soyadı: Merkel, adı: Angela, mesleği: Alman Şansöylesi",
    "soyadı: Akşener, adı: Meral, mesleği: İYİ Parti Başkanı"]

print ("re.split'le seçici ayrıştırma:")
for satır in satırlar: print (re.split (",* *\w*: ", satır) )

print ("\nre.split[1:]'le ilk elemansız seçici ayrıştırma:")
for satır in satırlar: print (re.split (",* *\w*: ", satır)[1:] )
print ("-"*75, "\n")
#---------------------------------------------------------------------------------------------------------

dizge = "Evet, ben evet dedim ve tekrar Evet diyeceğim."
sonuç = re.sub ("[eE]vet", "hayır", dizge)
print ("Bulunanın başka ibareyle değiştirilmesi:", sonuç)

"""Çıktı:
>python p_13104.py
Ayrışan noktalamasız sadece harfli kelimeler listesi: ['OF', 'bodies', 'chang',
'd', 'to', 'various', 'forms', 'I', 'sing', 'Ye', 'Gods', 'from', 'whom', 'these',
'miracles', 'did', 'spring', 'Inspire', 'my', 'numbers', 'with', 'coelestial', 'heat', '']
---------------------------------------------------------------------------

re.split'le seçici ayrıştırma:
['', 'Obama', 'Barack', 'ABD Başkanı']
['', 'Merkel', 'Angela', 'Alman Şansöylesi']
['', 'Akşener', 'Meral', 'İYİ Parti Başkanı']

re.split[1:]'le ilk elemansız seçici ayrıştırma:
['Obama', 'Barack', 'ABD Başkanı']
['Merkel', 'Angela', 'Alman Şansöylesi']
['Akşener', 'Meral', 'İYİ Parti Başkanı']
---------------------------------------------------------------------------

Bulunanın başka ibareyle değiştirilmesi: hayır, ben hayır dedim ve tekrar hayır
diyeceğim.
"""