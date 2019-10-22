# coding:iso-8859-9 Türkçe

# x+y+z=100
# x*5 + y*3 + z*1/3 = 100

print ("1 Ananas: 5 TL, 1 Mango: 3 TL ve 3 Portakal = 1 TL ise")
print ("3 meyve toplam sayısı 100 adet ve toplam fiyat 100 TL olabilmesi için")
print ("Meyvelerin kaçar adetlik kombinasyonları bu şartları sağlar?\n")
print ("="*50)
print ("{:^50s}" .format ("Ananas-Mango-Portakal"))
print ("-"*50)
print ("{:^20s}{:^28s}" .format ("Adet", "Tutar-TL"))
print ("-"*50)
for x in range (21):
    for y in range (34):
        for z in range (301):
            if (x+y+z == 100) and (5*x + 3*y + z/3 == 100):
                print ("{:3d} +{:3d} +{:3d} = 100" .format (x, y, z), end="     ")
                print ("{:3d} +{:3d} +{:3d} = 100" .format (x*5, y*3, z//3))
print ("="*50)
