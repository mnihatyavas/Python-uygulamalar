# coding:iso-8859-9 türkçe

def sayı (a):
    try: return int (a)
    except Exception as istisna:
       print ("Tamsayı dönüşümünde hata oluştu: ", istisna)

print (sayı ("dizge"))
print (sayı ("1957"))
print (sayı (1957))
print()

def seviye (a):
    if a <1:
        raise Exception (a)
    # Eğer bir istisna kalkmışsa
    # sonraki kodlamalar işletilmeyecektir...
    return a

try:
    sayı = seviye (-10)
    # Fonksiyonda istisna kaldırılmışsa alttaki print atlanacaktır...
    print ("seviye = ", sayı)
except Exception as ist:
    print ("Seviye fonksiyonunda kaldırılan hata:", ist)

print()
# Kullanıcı tanımlı istisnalar...
class Ağhatası (RuntimeError):
    def __init__ (self, arg): self.args = arg

try: raise Ağhatası ("Yanlış sunucu ismi")
except Ağhatası as ist: print ("HATA:", ist.args)
