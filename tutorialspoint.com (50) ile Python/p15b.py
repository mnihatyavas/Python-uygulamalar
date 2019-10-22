# coding:iso-8859-9 t�rk�e

def say� (a):
    try: return int (a)
    except Exception as istisna:
       print ("Tamsay� d�n���m�nde hata olu�tu: ", istisna)

print (say� ("dizge"))
print (say� ("1957"))
print (say� (1957))
print()

def seviye (a):
    if a <1:
        raise Exception (a)
    # E�er bir istisna kalkm��sa
    # sonraki kodlamalar i�letilmeyecektir...
    return a

try:
    say� = seviye (-10)
    # Fonksiyonda istisna kald�r�lm��sa alttaki print atlanacakt�r...
    print ("seviye = ", say�)
except Exception as ist:
    print ("Seviye fonksiyonunda kald�r�lan hata:", ist)

print()
# Kullan�c� tan�ml� istisnalar...
class A�hatas� (RuntimeError):
    def __init__ (self, arg): self.args = arg

try: raise A�hatas� ("Yanl�� sunucu ismi")
except A�hatas� as ist: print ("HATA:", ist.args)
