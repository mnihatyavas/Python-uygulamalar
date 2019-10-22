# coding:iso-8859-9 "Türkçe"

sözlüğüm = dict (elma="yeşil", muz="sarı", kiraz="kırmızı")
print ("Sözlüğümdeki element sayısı:", len (sözlüğüm))
print ("Sözlüğümdeki elementler:", sözlüğüm)

sözlüğüm["elma"] = "pembe"
print ("Değişen sözlüğüm içeriği:", sözlüğüm)

sözlüğüm["mürmüreriği"] = "mor"
print ("İlaveli sözlüğüm içeriği:", sözlüğüm)

del (sözlüğüm["muz"])
print ("Eksiltilen sözlüğüm içeriği:", sözlüğüm)
