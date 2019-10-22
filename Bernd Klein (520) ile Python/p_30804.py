# coding:iso-8859-9 Türkçe
# p_30804.py: 4 ibareler listesini biçimli yegane ve ağırlıksız bireşimleme örneği.

import p_30801 as p381

def biçimle (veriler):
    yüklem, zarf, sıfat, ad, sıfat2 = veriler
    biçim = "Bu şarap %s olup %s %s %s'lı, \nsonrasında ise ağızda kalıcı bir %s lezzetinde!"
    return biçim % (yüklem, zarf, sıfat, ad, sıfat2)  

# Örnek: Bu şarap tam-esritici olup tekdüzeli tütünümsü aroma'lı, sonrasında ise ağızda kalıcı bir kebabımsı lezzetinde!

yüklemler = ['hafif-esritici', 'orta-esritici', 'tam-esritici']
zarflar = ['münasip', 'iddalı', 'zorgulu', 'baskılı', 'tamamen', 'daimi', 
    'uygun', 'inanılır', 'farkedilir', 'heyecanlandırıcı', 'hareketlendirici', 'verimli', 
    'enerjik', 'heveslendirici', 'mantarımsı', 'genelde', 'kutsalca', 'etkileşimcili', 
    'içtenci', 'tekdüzeli', 'nesnel', 'parlatıcı', 'öncülleyici', 'profesyonelce', 
    'artarcasına', 'hızla', 'süratle', 'kesintisizce', 'sinerjik', 'yegane']
adlar = ['aroma', 'koku', 'tat']
sıfatlar = ['sivrimsi', 'parlağımsı', 'kalıcımsı', 'iskoç esansı', 'tereyağı',
    'çikolata', 'karmamsı', 'topraksı', 'gevrekce', 'vurgulu',
    'kebab', 'çiçeğimsi', 'yemişen', 'meyve', 'çimenimsi',
    'otumsu', 'reçel', 'meyvesuyu', 'moka', 'meşemsi',
    'rafinemsi', 'bünyemsi', 'sıkı-sıkımsı', 'baskınımsı', 'baskılımsı',
    'tütünümsü', 'yapayımsı', 'meşesizimsi', 'vanilya', 'kadifemsi']

veriler = (yüklemler, zarflar, sıfatlar, adlar, sıfatlar)
bireşim = p381.bireşimci (veriler, ağırlıkları=None, biçimlemeFonksiyonu=biçimle, tekrarlanabilirSeçimMi=False)
şarapTadlarınınYorumu = bireşim()

try: sayı = abs (int (input ("Kaç adet saçmasapan şarap tadı yorumu yapalım [12]? ")))
except: sayı = 12

print()
for i in range (sayı):
    print ("{0:d}.şarap:".format(i+1) )
    print (next (şarapTadlarınınYorumu) )
    print()



"""Çıktı:
>python p_30804.py
Kaç adet saçmasapan şarap tadı yorumu yapalım [12]? 1

1.şarap:
Bu şarap tam-esritici olup heveslendirici kalıcımsı aroma'lı,
sonrasında ise ağızda kalıcı bir çikolata lezzetinde!

>python p_30804.py  ** TEKRAR **
Kaç adet saçmasapan şarap tadı yorumu yapalım [12]?

1.şarap:
Bu şarap tam-esritici olup inanılır reçel aroma'lı,
sonrasında ise ağızda kalıcı bir sivrimsi lezzetinde!

2.şarap:
Bu şarap tam-esritici olup zorgulu iskoç esansı tat'lı,
sonrasında ise ağızda kalıcı bir gevrekce lezzetinde!

3.şarap:
Bu şarap hafif-esritici olup süratle iskoç esansı koku'lı,
sonrasında ise ağızda kalıcı bir tereyağı lezzetinde!

4.şarap:
Bu şarap hafif-esritici olup tamamen tereyağı tat'lı,
sonrasında ise ağızda kalıcı bir vurgulu lezzetinde!

5.şarap:
Bu şarap tam-esritici olup baskılı tereyağı koku'lı,
sonrasında ise ağızda kalıcı bir tereyağı lezzetinde!

6.şarap:
Bu şarap orta-esritici olup inanılır bünyemsi koku'lı,
sonrasında ise ağızda kalıcı bir vanilya lezzetinde!

7.şarap:
Bu şarap tam-esritici olup uygun yemişen koku'lı,
sonrasında ise ağızda kalıcı bir vanilya lezzetinde!

8.şarap:
Bu şarap hafif-esritici olup mantarımsı meyve koku'lı,
sonrasında ise ağızda kalıcı bir topraksı lezzetinde!

9.şarap:
Bu şarap hafif-esritici olup nesnel çikolata aroma'lı,
sonrasında ise ağızda kalıcı bir meyvesuyu lezzetinde!

10.şarap:
Bu şarap tam-esritici olup yegane iskoç esansı aroma'lı,
sonrasında ise ağızda kalıcı bir karmamsı lezzetinde!

11.şarap:
Bu şarap orta-esritici olup tekdüzeli tütün koku'lı,
sonrasında ise ağızda kalıcı bir iskoç esansı lezzetinde!

12.şarap:
Bu şarap orta-esritici olup nesnel vurgulu koku'lı,
sonrasında ise ağızda kalıcı bir tereyağı lezzetinde!
"""