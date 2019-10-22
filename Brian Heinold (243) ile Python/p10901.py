#coding:iso-8859-9 Türkçe

from random import randint
ısı=tip=0
while tip != 9:
    try: tip = eval (input ('[1:F; 2:C; 3:K] Derece tipi girin {9:Çık}: '))
    except Exception: tip = randint (1,3)
    if tip == 9: print ("Hoşçakalın, programı sonlandırıyorum!")
    if not (tip == 1 or tip == 2 or tip == 3 or tip == 9): tip = randint (1,3)
    if tip != 9:
        try: ısı = eval (input (str(tip)+' için ısı değeri girin: '))
        except Exception:
            if tip == 1: ısı = randint (-459, 5000)
            elif tip == 2: ısı = randint (-273, 5000)
            else: ısı = randint (0, 5000)
    if tip == 1 and ısı >= - 459.66999: print ("Girdiğiniz", ısı, "F=",  5/9*(ısı-32), "C ve", 5/9*(ısı-32)+273.15, "K derecedir.")
    elif tip == 2 and ısı >= -273.15: print ("Girdiğiniz", ısı, "C=",  1.8*ısı+32, "F ve", 273.15+ısı, "K derecedir.")
    elif tip == 3 and ısı >= 0: print ("Girdiğiniz", ısı, "K=",  ısı-273.15, "C ve", (ısı-273.15)*1.8+32, "F derecedir.")

