# coding:iso-8859-9 T�rk�e
# p_30701.py: random.choise(..) ile dizge, liste ve t�pleden tesad�fi eleman se�me �rne�i.

from random import choice as se�

alfabe = "abc�defg�h�ijklmno�prstu�vyz"
meslekler = ["alim", "filozof", "m�hendis", "ulema", "��retmen", "polis"]
seviye = ("ba�lang��", "orta", "ileri", "uzman")

print ("Alfabeden geli�ig�zel bir harf se�elim:", se� (alfabe) )
print ("Hangi mesle�i tercih edersin?", se� (meslekler) )
print ("Hangi seviyedeki e�itimi almay� istiyorsun?", se� (seviye) )



"""��kt�:
>python p_30701.py
Alfabeden geli�ig�zel bir harf se�elim: g
Hangi mesle�i tercih edersin? polis
Hangi seviyeli e�itimi almay� istiyorsun? uzman

>python p_30701.py  ** TEKRAR **
Alfabeden geli�ig�zel bir harf se�elim: �
Hangi mesle�i tercih edersin? ulema
Hangi seviyedeki e�itimi almay� istiyorsun? orta
"""