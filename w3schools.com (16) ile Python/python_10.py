# coding:iso-8859-9 "Türkçe"

import camelcase # Cümledeki tüm kelimelerin ilk harflerini büyükharf yapar

deve = camelcase.CamelCase()

cümle = "import camelcase modülü cümledeki tüm kelimelerin ilk harflerini büyükharf yapar."
print ("Orijinal cümle: [" + cümle + "]\n")
print ("CamelCase() cümlesi: [" + deve.hump (cümle))
