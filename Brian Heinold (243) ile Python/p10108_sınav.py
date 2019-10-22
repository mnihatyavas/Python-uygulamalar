# p10108_sınav.py
# coding:iso-8859-9 Türkçe

print ("**********")
print ("**********")
print ("**********")
print ("**********")

print ("\n**********")
print ("*        *")
print ("*        *")
print ("**********")

print ("\n*")
print ("***")
print ("*****")
print ("*******")

sayı = eval (input ("\nBir sayı girin: "))
print ("\nKompleks bir hesap işlemi kalanı [0->99]:", (sayı + (512 - 282) / (47 * 48 + 5) * 10000) % 100)
print (sayı, "'in karesi ", sayı*sayı, "'dır.", sep="")
print (sayı, "'in 5 ardışık katları: ", sep="", end="")
print (2*sayı, 3*sayı, 4*sayı, 5*sayı, 6*sayı, sep="--->")

#sayı = eval (input ("\nBir kilogram değeri girin: ")
print (sayı, "kg =", sayı*2.2, "pound'dur.")

print (sayı, "'in 5 ardışık katlarının toplamı: ",
        2*sayı + 3*sayı + 4*sayı + 5*sayı + 6*sayı, "; ve ortalaması: ",
        (2*sayı + 3*sayı + 4*sayı + 5*sayı + 6*sayı) / 5, "'dir.", sep="")

print (sayı, "'in %15'i: ", sayı*0.15, "; ve ikisinin toplamı: ", sayı*1.15, "'dir.", sep="")
