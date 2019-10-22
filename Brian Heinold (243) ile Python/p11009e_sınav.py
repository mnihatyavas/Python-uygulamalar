# coding:iso-8859-9 Türkçe

try: sayı = abs (eval (input ("Küsüratlı bir feet değeri girin: ")))
except Exception: sayı = 4.75
küsürat = sayı - int (sayı)
inç = küsürat * 30.48 / 2.54
print ("Girdiğiniz sayı:", int (sayı), "feet ve", inç, "inç'tir.")

L = []
büyükSayı1=büyükSayı2=0
küçükSayı1=küçükSayı2=999
while True:
    dizge = input ("\n(5'7\") biçimli değer girin [Çıkış: son]: ")
    if dizge.lower() == "son": break

    try: sayı1 = int (dizge[:dizge.index ("'")])
    except Exception: sayı1 = 5; print (sayı1, "'")
    try: sayı2 = int (dizge[dizge.index ("'")+1:dizge.index ("\"")])
    except Exception: sayı2 = 7; print (sayı2, "\"")

    if sayı1 > büyükSayı1: büyükSayı1 = sayı1
    if sayı1 < küçükSayı1: küçükSayı1 = sayı1
    if sayı2 > büyükSayı2: büyükSayı2 = sayı2
    if sayı2 < küçükSayı2: küçükSayı2 = sayı2

    sayı = sayı1 + (sayı2 * 2.54 / 30.48)
    L = L + [sayı]
print ("\nGirdiğiniz feet'inç\" değerlerinin feet karşılıkları listesi==>")
for k in L: print ("{:.2f}" .format (k), end=" ")
print ("\n\nGirilen enbüyük ve enküçük feet değerleri:", büyükSayı1, küçükSayı1)
print ("Girilen enbüyük ve enküçük inç değerleri:", büyükSayı2, küçükSayı2)
