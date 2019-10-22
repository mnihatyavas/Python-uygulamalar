# coding:iso-8859-9
# p_13709.py: Genel, korunaklı ve özel tip değişkenlerinin erişilebilme ve değiştirilebilme farklılığı örneği.

from p_13709x import A

x = A()

x.genel = x.genel + " Yani beni istediğiniz gibi değiştirebilirsiniz."
print (x.genel)

print()
x._korunaklı = x._korunaklı + " Ve beni de değiştirebilirsiniz."
print (x._korunaklı)

print()
try: print (x.__özel)
except Exception as ist: print ("AttributeError/ÖzellikHatası:", ist)

print()
print (x._A__özel) # Gizli özel değişkenin tavsiye edilmeyen kaçak erişimi...

"""Çıktı:
>python p_13709.py
Ben herkese açık genel bir tip değişkeni özelliğiyim. Yani beni istediğiniz gibi
 değiştirebilirsiniz.

Ben sadece altsıflara açık korunaklı bir tip değişkeni özelliğiyim. Ve beni de d
eğiştirebilirsiniz.

AttributeError/ÖzellikHatası: 'A' object has no attribute '__özel'

Ben herkese kapalı sınıfiçi özel bir tip değişkeni özelliğiyim.
"""