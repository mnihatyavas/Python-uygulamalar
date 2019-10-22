# coding:iso-8859-9 T�rk�e
# p_14003.py: Fonksiyon arg�manlar�nda overload/ta�ma �rne�i.

def fonk (n, m = None):
    if m: return n + m + 42
    else: return n + 42

print ("fonk(3):", fonk (3) )
print ("fonk(3,4):", fonk (3, 4) ) # Overloading/arg�manta�mas�...
print ("-"*75, "\n", sep="")
#---------------------------------------------------------------------------------------------

def fonk (*x): # Arg�man say� ve tipi genel...
    #if len (x) == 1: return x[0] + 42
    #elif len (x) == 2: return x[0] + x[1] + 42
    #else:
        toplam = 42
        for i in range (len (x) ): toplam += x [i]
        return toplam

print ("fonk(3):", fonk (3) )
print ("fonk(3,4):", fonk (3, 4) ) # Overloading/arg�manta�mas�...
print ("fonk(3,4,7,9.5,-1,0,8.25):", fonk (3, 4, 7, 9.5, -1, 0, 8.25) )

"""��kt�:
>python p_14003.py
fonk(3): 45
fonk(3,4): 49
---------------------------------------------------------------------------

fonk(3): 45
fonk(3,4): 49
fonk(3,4,7,9.5,-1,0,8.25): 72.75
"""