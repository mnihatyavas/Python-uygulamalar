# coding:iso-8859-9 T�rk�e
# p_13207.py: Sipari� kitap adet*fiyat*1.05 < �100 ise faturaya �10 ekle list(map(lambda...)) �rne�i.

sipari�ler = [ ["1903260001", "Python ��renelim, Mark Lutz", 4, 40.95],
    ["1903260028", "Python Programc�l���, Mark Lutz", 5, 56.80],
    ["1903260156", "Python'la �lk Y�zle�me, Paul Barry", 3, 32.96],
    ["1903260654", "Python3'le Tan��al�m, Bernd Klein", 3, 24.99],
    ["1903260802", "Python'la Programlama, Brian Heinhold", 7, 27.68],
    ["1903260997", "Python ��renimi, H.Sohrabpoor", 17, 12.50] ]

faturaTutar� = list (map (lambda x: x if x[2] >= 100 else (x[0], x[1], x[2] + 10), # Fatura tutar� < 100 � ise 10 � ekle...
    map (lambda x: (x[0], x[1], (x[2] * x[3]) * 1.05), sipari�ler) ) ) # Faturaya %5 vergiler ekleniyor...

print ("  Sipari� No    Kitab�n Ad�                    Fatura Tutar�", "\n", "="*64, sep="")
for i in range (len (faturaTutar�)): print (faturaTutar� [i])

"""��kt�:
>python p_13207.py
  Sipari� No    Kitab�n Ad�                    Fatura Tutar�
================================================================
('1903260001', 'Python ��renelim, Mark Lutz', 171.99)
('1903260028', 'Python Programc�l���, Mark Lutz', 298.2)
('1903260156', "Python'la �lk Y�zle�me, Paul Barry", 103.824)
('1903260654', "Python3'le Tan��al�m, Bernd Klein", 88.7185)
('1903260802', "Python'la Programlama, Brian Heinhold", 203.448)
('1903260997', 'Python ��renimi, H.Sohrabpoor', 223.125)
"""