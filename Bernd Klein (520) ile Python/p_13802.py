# coding:iso-8859-9
# p_13802.py: Tüpleli sınıf ip özelliği ve init kuruculu tip değişken özellikleri örneği.

class Robot:
    ÜçlüKanun = (
        """Bir robot bir insanı yaralayamaz, veya bir insanın yaralanabilme olayına duyarsız kalamaz.""",
        """Bir robot bir insan tarafından verilen talimatlara, İlk Kanunu ihlal etmiyorsa uymalıdır.""",
        """Bir robot kendi varlığını, İlk ve İkinci Kanunlara ters düşmüyorsa korumalıdır.""" )
    def __init__ (self, adı, yılı):
        self.ad = adı
        self.yıl = yılı
    # Gereken diğer metodlar...

x = Robot ("Robot Nihat", "19570417")

for sıra, metin in enumerate (Robot.ÜçlüKanun):
    print ("Madde." + str (sıra+1) + ":\n" + metin + "\n")

print (str ("-"*79) + "\n" + x.ÜçlüKanun [1] )

print ("\nAdı: " + x.ad + ", İmal tarihi: " + x.yıl)



"""Çıktı:
>python p_13802.py
Madde.1:
Bir robot bir insanı yaralayamaz, veya bir insanın yaralanabilme olayına duyarsız kalamaz.

Madde.2:
Bir robot bir insan tarafından verilen talimatlara, İlk Kanunu ihlal etmiyorsa uymalıdır.

Madde.3:
Bir robot kendi varlığını, İlk ve İkinci Kanunlara ters düşmüyorsa korumalıdır.

-------------------------------------------------------------------------------
Bir robot bir insan tarafından verilen talimatlara, İlk Kanunu ihlal etmiyorsa uymalıdır.

Adı: Robot Nihat, İmal tarihi: 19570417
"""