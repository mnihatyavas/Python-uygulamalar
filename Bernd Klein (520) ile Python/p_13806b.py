# coding:iso-8859-9
# p_13806b.py: @classmethod'la kopya sınıf nesnelerin değişen tip özelliklerinin aktarılabilmesi örneği.

class Evciller:
    ad = "evcil hayvanlar"
    @classmethod
    def hakkında (sınıf): print ("Bu sınıf {} hakkındadır!" .format (sınıf.ad) )   

class Köpekler (Evciller): ad = "insanların en sadık arkadaşı olan köpekler"
class Kediler (Evciller): ad = "insanın ayakları dibinden ayrılmayan kediler"
class Kuşlar (Evciller): ad = "insanın omuzlarında şakıyan muhabbet kuşları"

e = Evciller()
e.hakkında()

kö = Köpekler()
kö.hakkında()

ke = Kediler()
ke.hakkında()

ku = Kuşlar()
ku.hakkında()



"""Çıktı:
>python p_13806b.py
Bu sınıf evcil hayvanlar hakkındadır!
Bu sınıf insanların en sadık arkadaşı olan köpekler hakkındadır!
Bu sınıf insanın ayakları dibinden ayrılmayan kediler hakkındadır!
Bu sınıf insanın omuzlarında şakıyan muhabbet kuşları hakkındadır!
"""