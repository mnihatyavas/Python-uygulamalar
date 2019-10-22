# coding:iso-8859-9 Türkçe
# p_21501.py: Büyüyen 10 diski çivi1'den çivi2 aracılığıyla çivi3'e aktarma hamle sayısı örneği.

# Küçülen diskler çivi1'den çivi3'e teker teker ve üstte daima daha küçülen
# bulunmak şartıyla optimum 2^n-1 kerede ç1<->ç2<->ç3'e aktarılabilir.

def H (n, çivi1, çivi2, çivi3): # Hanoi kuleleri...
    global sayaç
    if n > 0:
        H (n - 1, çivi1, çivi3, çivi2)
        if çivi1: çivi3.append (çivi1.pop())
        H (n - 1, çivi2, çivi1, çivi3)
        sayaç +=1

sayaç = 0
çivi1 = [10,9,8,7,6,5,4,3,2,1]
çivi3 = []
çivi2 = []
print ("İlk:", çivi1, çivi2, çivi3)
H (len (çivi1), çivi1, çivi2, çivi3)
print ("Son: ", çivi1, " ", çivi2, " ", çivi3, " Hamle:2^", len (çivi3), "-1=", sayaç, sep="")



"""Çıktı:
>python p_21501.py
İlk: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] [] []
Son: [] [] [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] Hamle:2^10-1=1023
"""