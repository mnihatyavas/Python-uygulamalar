# coding:iso-8859-9 Türkçe
# p_13502.py: try-raise ile hazır veya özel istisna fırlatıp except Exception'la yakalama örneği.

try: raise SyntaxError ("Afedersiniz, kendi hatam!..")
except Exception as ist: print (ist)

print ("Program devam ediyor...")
print ("-"*75, "\n", sep="")
#-----------------------------------------------------------------------------------------------------

class İstisnam (Exception): pass

try: raise İstisnam ("Hazır arşiv istisnaları dışında kendi istisnanızı da yaratıp fırlatabilirsiniz!")
except Exception as ist: print (ist)

print ("Program devam ediyor...")

"""Çıktı:
>python p_13502.py
Afedersiniz, kendi hatam!..
Program devam ediyor...
---------------------------------------------------------------------------

Hazır arşiv istisnaları dışında kendi istisnanızı da yaratıp fırlatabilirsiniz!
Program devam ediyor...
"""