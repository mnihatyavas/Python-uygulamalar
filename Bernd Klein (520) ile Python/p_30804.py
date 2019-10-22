# coding:iso-8859-9 T�rk�e
# p_30804.py: 4 ibareler listesini bi�imli yegane ve a��rl�ks�z bire�imleme �rne�i.

import p_30801 as p381

def bi�imle (veriler):
    y�klem, zarf, s�fat, ad, s�fat2 = veriler
    bi�im = "Bu �arap %s olup %s %s %s'l�, \nsonras�nda ise a��zda kal�c� bir %s lezzetinde!"
    return bi�im % (y�klem, zarf, s�fat, ad, s�fat2)  

# �rnek: Bu �arap tam-esritici olup tekd�zeli t�t�n�ms� aroma'l�, sonras�nda ise a��zda kal�c� bir kebab�ms� lezzetinde!

y�klemler = ['hafif-esritici', 'orta-esritici', 'tam-esritici']
zarflar = ['m�nasip', 'iddal�', 'zorgulu', 'bask�l�', 'tamamen', 'daimi', 
    'uygun', 'inan�l�r', 'farkedilir', 'heyecanland�r�c�', 'hareketlendirici', 'verimli', 
    'enerjik', 'heveslendirici', 'mantar�ms�', 'genelde', 'kutsalca', 'etkile�imcili', 
    'i�tenci', 'tekd�zeli', 'nesnel', 'parlat�c�', '�nc�lleyici', 'profesyonelce', 
    'artarcas�na', 'h�zla', 's�ratle', 'kesintisizce', 'sinerjik', 'yegane']
adlar = ['aroma', 'koku', 'tat']
s�fatlar = ['sivrimsi', 'parla��ms�', 'kal�c�ms�', 'isko� esans�', 'tereya��',
    '�ikolata', 'karmams�', 'topraks�', 'gevrekce', 'vurgulu',
    'kebab', '�i�e�imsi', 'yemi�en', 'meyve', '�imenimsi',
    'otumsu', 're�el', 'meyvesuyu', 'moka', 'me�emsi',
    'rafinemsi', 'b�nyemsi', 's�k�-s�k�ms�', 'bask�n�ms�', 'bask�l�ms�',
    't�t�n�ms�', 'yapay�ms�', 'me�esizimsi', 'vanilya', 'kadifemsi']

veriler = (y�klemler, zarflar, s�fatlar, adlar, s�fatlar)
bire�im = p381.bire�imci (veriler, a��rl�klar�=None, bi�imlemeFonksiyonu=bi�imle, tekrarlanabilirSe�imMi=False)
�arapTadlar�n�nYorumu = bire�im()

try: say� = abs (int (input ("Ka� adet sa�masapan �arap tad� yorumu yapal�m [12]? ")))
except: say� = 12

print()
for i in range (say�):
    print ("{0:d}.�arap:".format(i+1) )
    print (next (�arapTadlar�n�nYorumu) )
    print()



"""��kt�:
>python p_30804.py
Ka� adet sa�masapan �arap tad� yorumu yapal�m [12]? 1

1.�arap:
Bu �arap tam-esritici olup heveslendirici kal�c�ms� aroma'l�,
sonras�nda ise a��zda kal�c� bir �ikolata lezzetinde!

>python p_30804.py  ** TEKRAR **
Ka� adet sa�masapan �arap tad� yorumu yapal�m [12]?

1.�arap:
Bu �arap tam-esritici olup inan�l�r re�el aroma'l�,
sonras�nda ise a��zda kal�c� bir sivrimsi lezzetinde!

2.�arap:
Bu �arap tam-esritici olup zorgulu isko� esans� tat'l�,
sonras�nda ise a��zda kal�c� bir gevrekce lezzetinde!

3.�arap:
Bu �arap hafif-esritici olup s�ratle isko� esans� koku'l�,
sonras�nda ise a��zda kal�c� bir tereya�� lezzetinde!

4.�arap:
Bu �arap hafif-esritici olup tamamen tereya�� tat'l�,
sonras�nda ise a��zda kal�c� bir vurgulu lezzetinde!

5.�arap:
Bu �arap tam-esritici olup bask�l� tereya�� koku'l�,
sonras�nda ise a��zda kal�c� bir tereya�� lezzetinde!

6.�arap:
Bu �arap orta-esritici olup inan�l�r b�nyemsi koku'l�,
sonras�nda ise a��zda kal�c� bir vanilya lezzetinde!

7.�arap:
Bu �arap tam-esritici olup uygun yemi�en koku'l�,
sonras�nda ise a��zda kal�c� bir vanilya lezzetinde!

8.�arap:
Bu �arap hafif-esritici olup mantar�ms� meyve koku'l�,
sonras�nda ise a��zda kal�c� bir topraks� lezzetinde!

9.�arap:
Bu �arap hafif-esritici olup nesnel �ikolata aroma'l�,
sonras�nda ise a��zda kal�c� bir meyvesuyu lezzetinde!

10.�arap:
Bu �arap tam-esritici olup yegane isko� esans� aroma'l�,
sonras�nda ise a��zda kal�c� bir karmams� lezzetinde!

11.�arap:
Bu �arap orta-esritici olup tekd�zeli t�t�n koku'l�,
sonras�nda ise a��zda kal�c� bir isko� esans� lezzetinde!

12.�arap:
Bu �arap orta-esritici olup nesnel vurgulu koku'l�,
sonras�nda ise a��zda kal�c� bir tereya�� lezzetinde!
"""