# coding:iso-8859-9 T�rk�e
# p_20902.py: Grafik yumrular� ve ba�lant�lar�, do�rusal ve dairesel grafik ��kt�lar� �rne�i.

import networkx as nwx
import matplotlib.pyplot as pp

grafik1 = nwx.path_graph (6) # grafik1 dizilimi: [5<--0], sa�dan-sola...
�ehirler = {0:"Edirne", 1:"�stanbul", 2:"Ankara", 3:"Malatya", 4:"Sivas", 5:"Kars"}
grafik2 = nwx.relabel_nodes (grafik1, �ehirler) # grafik2 dizilimi: [Kars<--Edirne], sa�dan-sola
# grafik2 yeniden yarat�l�r, grafik1 etkilenmez...
# Grafiklerde maalesef isimler g�r�nm�yor, MS Paint ile etiketlenmeli...

print ("Grafik1'in yumrular�:", grafik1.nodes() )
print ("Grafik1'in ba�lant�lar�:", grafik1.edges() )

print ("\nGrafik2'in yumrular�:", grafik2.nodes() )
print ("Grafik2'in ba�lant�lar�:", grafik2.edges() )

nwx.draw (grafik2)
#pp.savefig ("p_20902a.png")
pp.show()

print ("-"*75)
#--------------------------------------------------------------------------------------------------

haritalama1 = dict (zip (grafik1.nodes(), "abc"))
nwx.relabel_nodes (grafik1, haritalama1, copy=False) # grafik1 yeni k�sagelen isimlerle de�i�tirilir...

print ("Grafik1'in yumrular�:", grafik1.nodes() )
print ("Grafik1'in ba�lant�lar�:", grafik1.edges() )
print ("-"*75)
#--------------------------------------------------------------------------------------------------


grafik1 = nwx.path_graph (6)
haritalama2 = dict (zip (grafik1.nodes(), (100,101,102,103,104,105) ))
nwx.relabel_nodes (grafik1, haritalama2, copy=False) # grafik1 haritalama fonksiyonuyla tamamen ismen de�i�ir...
grafik1.add_edge (100, 105) # Sondan ba�a ba�lant�...

print ("Grafik1'in yumrular�:", grafik1.nodes() )
print ("Grafik1'in ba�lant�lar�:", grafik1.edges() )

nwx.draw (grafik1)
#pp.savefig ("p_20902b.png")
pp.show()



"""��kt�:
>python p_20902.py
Grafik1'in yumrular�: [0, 1, 2, 3, 4, 5]
Grafik1'in ba�lant�lar�: [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

Grafik2'in yumrular�: ['Edirne', '�stanbul', 'Ankara', 'Malatya', 'Sivas', 'Kars']
Grafik2'in ba�lant�lar�: [('Edirne', '�stanbul'), ('�stanbul', 'Ankara'), ('Ankara', 'Malatya'), ('Malatya', 'Sivas'), ('Sivas', 'Kars')]

nx_pylab.py:579: MatplotlibDeprecationWarning:
The iterable function was deprecated in Matplotlib 3.1 and will be removed in 3.3. Use np.iterable instead. if not cb.iterable(width):
---------------------------------------------------------------------------

Grafik1'in yumrular�: [3, 4, 5, 'a', 'b', 'c']
Grafik1'in ba�lant�lar�: [(3, 4), (3, 'c'), (4, 5), ('a', 'b'), ('b', 'c')]
---------------------------------------------------------------------------

Grafik1'in yumrular�: [100, 101, 102, 103, 104, 105]
Grafik1'in ba�lant�lar�: [(100, 101), (100, 105), (101, 102), (102, 103), (103,104), (104, 105)]
"""