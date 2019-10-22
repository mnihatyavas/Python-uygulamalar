# coding:iso-8859-9 Türkçe
# p_14204.py: Listeye null, tüple, aritmetik işlem, dizge, liste ve küme ekleme örneği.

class ListeyeEkle (list):
    def __init__ (self, lst): self.lst = list #list.__init__ (self, lst)
    def ekle (self, birim): self.append (birim)


if __name__ == "__main__":
    x = ListeyeEkle ("")
    x.ekle ((170, 57))
    x.ekle (2019-1957)
    x.ekle (57+4)
    x.ekle ("M.Nihat Yavaş")
    x.ekle ([1957, 4, 17])
    x.ekle ({"Yeşilyurt", "Malatya"})

    print ("Standart list'e null, tüple, aritmetik işlem, dizge, liste, küme vb ekleme:\n", x)



"""Çıktı:
>python p_14204.py
Standart list'e null, tüple, aritmetik işlem, dizge, liste, küme vb ekleme:
 [(170, 57), 62, 61, 'M.Nihat Yavaş', [1957, 4, 17], {'Malatya', 'Yeşilyurt'}]
"""