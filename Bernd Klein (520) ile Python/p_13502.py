# coding:iso-8859-9 T�rk�e
# p_13502.py: try-raise ile haz�r veya �zel istisna f�rlat�p except Exception'la yakalama �rne�i.

try: raise SyntaxError ("Afedersiniz, kendi hatam!..")
except Exception as ist: print (ist)

print ("Program devam ediyor...")
print ("-"*75, "\n", sep="")
#-----------------------------------------------------------------------------------------------------

class �stisnam (Exception): pass

try: raise �stisnam ("Haz�r ar�iv istisnalar� d���nda kendi istisnan�z� da yarat�p f�rlatabilirsiniz!")
except Exception as ist: print (ist)

print ("Program devam ediyor...")

"""��kt�:
>python p_13502.py
Afedersiniz, kendi hatam!..
Program devam ediyor...
---------------------------------------------------------------------------

Haz�r ar�iv istisnalar� d���nda kendi istisnan�z� da yarat�p f�rlatabilirsiniz!
Program devam ediyor...
"""