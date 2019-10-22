# coding:iso-8859-9 Türkçe
# p_20902.py: Grafik yumruları ve bağlantıları, doğrusal ve dairesel grafik çıktıları örneği.

import networkx as nwx
import matplotlib.pyplot as pp

grafik1 = nwx.path_graph (6) # grafik1 dizilimi: [5<--0], sağdan-sola...
şehirler = {0:"Edirne", 1:"İstanbul", 2:"Ankara", 3:"Malatya", 4:"Sivas", 5:"Kars"}
grafik2 = nwx.relabel_nodes (grafik1, şehirler) # grafik2 dizilimi: [Kars<--Edirne], sağdan-sola
# grafik2 yeniden yaratılır, grafik1 etkilenmez...
# Grafiklerde maalesef isimler görünmüyor, MS Paint ile etiketlenmeli...

print ("Grafik1'in yumruları:", grafik1.nodes() )
print ("Grafik1'in bağlantıları:", grafik1.edges() )

print ("\nGrafik2'in yumruları:", grafik2.nodes() )
print ("Grafik2'in bağlantıları:", grafik2.edges() )

nwx.draw (grafik2)
#pp.savefig ("p_20902a.png")
pp.show()

print ("-"*75)
#--------------------------------------------------------------------------------------------------

haritalama1 = dict (zip (grafik1.nodes(), "abc"))
nwx.relabel_nodes (grafik1, haritalama1, copy=False) # grafik1 yeni kısagelen isimlerle değiştirilir...

print ("Grafik1'in yumruları:", grafik1.nodes() )
print ("Grafik1'in bağlantıları:", grafik1.edges() )
print ("-"*75)
#--------------------------------------------------------------------------------------------------


grafik1 = nwx.path_graph (6)
haritalama2 = dict (zip (grafik1.nodes(), (100,101,102,103,104,105) ))
nwx.relabel_nodes (grafik1, haritalama2, copy=False) # grafik1 haritalama fonksiyonuyla tamamen ismen değişir...
grafik1.add_edge (100, 105) # Sondan başa bağlantı...

print ("Grafik1'in yumruları:", grafik1.nodes() )
print ("Grafik1'in bağlantıları:", grafik1.edges() )

nwx.draw (grafik1)
#pp.savefig ("p_20902b.png")
pp.show()



"""Çıktı:
>python p_20902.py
Grafik1'in yumruları: [0, 1, 2, 3, 4, 5]
Grafik1'in bağlantıları: [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

Grafik2'in yumruları: ['Edirne', 'İstanbul', 'Ankara', 'Malatya', 'Sivas', 'Kars']
Grafik2'in bağlantıları: [('Edirne', 'İstanbul'), ('İstanbul', 'Ankara'), ('Ankara', 'Malatya'), ('Malatya', 'Sivas'), ('Sivas', 'Kars')]

nx_pylab.py:579: MatplotlibDeprecationWarning:
The iterable function was deprecated in Matplotlib 3.1 and will be removed in 3.3. Use np.iterable instead. if not cb.iterable(width):
---------------------------------------------------------------------------

Grafik1'in yumruları: [3, 4, 5, 'a', 'b', 'c']
Grafik1'in bağlantıları: [(3, 4), (3, 'c'), (4, 5), ('a', 'b'), ('b', 'c')]
---------------------------------------------------------------------------

Grafik1'in yumruları: [100, 101, 102, 103, 104, 105]
Grafik1'in bağlantıları: [(100, 101), (100, 105), (101, 102), (102, 103), (103,104), (104, 105)]
"""