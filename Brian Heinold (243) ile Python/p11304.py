# coding:iso-8859-9 Türkçe

def varsayılı_selam (dizge, n=1): print (dizge * n)

varsayılı_selam ('Merhaba ', 5)
varsayılı_selam ('Merhaba ')

print()
def stilliYaz (metin="Merhaba", renk='siyah', zemin='beyaz', stil='normal', hizala='sol'):
    print (metin, renk, zemin, stil, hizala)

stilliYaz (metin='Hello', renk='yellow', zemin='black', stil='bold', hizala='left')
stilliYaz (metin='Selam', stil='koyu', hizala='sola', zemin='kara', renk='sarı')
stilliYaz ('Hi', stil='yatık-italik')
stilliYaz ('Merhaba', renk='yeşil', zemin='pembe')
stilliYaz ('Selam')
stilliYaz ()
