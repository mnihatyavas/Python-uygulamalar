# coding:iso-8859-9 T�rk�e
# p_21501.py: B�y�yen 10 diski �ivi1'den �ivi2 arac�l���yla �ivi3'e aktarma hamle say�s� �rne�i.

# K���len diskler �ivi1'den �ivi3'e teker teker ve �stte daima daha k���len
# bulunmak �art�yla optimum 2^n-1 kerede �1<->�2<->�3'e aktar�labilir.

def H (n, �ivi1, �ivi2, �ivi3): # Hanoi kuleleri...
    global saya�
    if n > 0:
        H (n - 1, �ivi1, �ivi3, �ivi2)
        if �ivi1: �ivi3.append (�ivi1.pop())
        H (n - 1, �ivi2, �ivi1, �ivi3)
        saya� +=1

saya� = 0
�ivi1 = [10,9,8,7,6,5,4,3,2,1]
�ivi3 = []
�ivi2 = []
print ("�lk:", �ivi1, �ivi2, �ivi3)
H (len (�ivi1), �ivi1, �ivi2, �ivi3)
print ("Son: ", �ivi1, " ", �ivi2, " ", �ivi3, " Hamle:2^", len (�ivi3), "-1=", saya�, sep="")



"""��kt�:
>python p_21501.py
�lk: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] [] []
Son: [] [] [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] Hamle:2^10-1=1023
"""