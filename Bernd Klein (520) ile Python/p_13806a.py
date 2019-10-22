# coding:iso-8859-9
# p_13806a.py: @staticmethod'la kopya sınıf nesnelerin değişen tip özelliklerinin aktarılamaması örneği.

class Evciller:
    ad = "evcil hayvanlar"
    @staticmethod
    def hakkında(): print ("Bu sınıf {} hakkındadır!" .format (Evciller.ad) )   

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
>python p_13806a.py
Bu sınıf evcil hayvanlar hakkındadır!
Bu sınıf evcil hayvanlar hakkındadır!
Bu sınıf evcil hayvanlar hakkındadır!
Bu sınıf evcil hayvanlar hakkındadır!
"""