# coding:iso-8859-9 Türkçe
# p_13207.py: Sipariş kitap adet*fiyat*1.05 < €100 ise faturaya €10 ekle list(map(lambda...)) örneği.

siparişler = [ ["1903260001", "Python Öğrenelim, Mark Lutz", 4, 40.95],
    ["1903260028", "Python Programcılığı, Mark Lutz", 5, 56.80],
    ["1903260156", "Python'la İlk Yüzleşme, Paul Barry", 3, 32.96],
    ["1903260654", "Python3'le Tanışalım, Bernd Klein", 3, 24.99],
    ["1903260802", "Python'la Programlama, Brian Heinhold", 7, 27.68],
    ["1903260997", "Python Öğrenimi, H.Sohrabpoor", 17, 12.50] ]

faturaTutarı = list (map (lambda x: x if x[2] >= 100 else (x[0], x[1], x[2] + 10), # Fatura tutarı < 100 € ise 10 € ekle...
    map (lambda x: (x[0], x[1], (x[2] * x[3]) * 1.05), siparişler) ) ) # Faturaya %5 vergiler ekleniyor...

print ("  Sipariş No    Kitabın Adı                    Fatura Tutarı", "\n", "="*64, sep="")
for i in range (len (faturaTutarı)): print (faturaTutarı [i])

"""Çıktı:
>python p_13207.py
  Sipariş No    Kitabın Adı                    Fatura Tutarı
================================================================
('1903260001', 'Python Öğrenelim, Mark Lutz', 171.99)
('1903260028', 'Python Programcılığı, Mark Lutz', 298.2)
('1903260156', "Python'la İlk Yüzleşme, Paul Barry", 103.824)
('1903260654', "Python3'le Tanışalım, Bernd Klein", 88.7185)
('1903260802', "Python'la Programlama, Brian Heinhold", 203.448)
('1903260997', 'Python Öğrenimi, H.Sohrabpoor', 223.125)
"""