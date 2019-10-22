# coding:iso-8859-9 Türkçe
# p_30701.py: random.choise(..) ile dizge, liste ve tüpleden tesadüfi eleman seçme örneği.

from random import choice as seç

alfabe = "abcçdefgğhıijklmnoöprstuüvyz"
meslekler = ["alim", "filozof", "mühendis", "ulema", "öğretmen", "polis"]
seviye = ("başlangıç", "orta", "ileri", "uzman")

print ("Alfabeden gelişigüzel bir harf seçelim:", seç (alfabe) )
print ("Hangi mesleği tercih edersin?", seç (meslekler) )
print ("Hangi seviyedeki eğitimi almayı istiyorsun?", seç (seviye) )



"""Çıktı:
>python p_30701.py
Alfabeden gelişigüzel bir harf seçelim: g
Hangi mesleği tercih edersin? polis
Hangi seviyeli eğitimi almayı istiyorsun? uzman

>python p_30701.py  ** TEKRAR **
Alfabeden gelişigüzel bir harf seçelim: ç
Hangi mesleği tercih edersin? ulema
Hangi seviyedeki eğitimi almayı istiyorsun? orta
"""