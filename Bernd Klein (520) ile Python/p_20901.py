# coding:iso-8859-9 T�rk�e
# p_20901.py: Networkx grafik mod�l�ne yumru ve ba�lant� ekleme, mathplotlib'le grafik ��kt�s� �rne�i.

# Online "pip install networkx" ve "matplotlib, numpy" mod�llerini indir, kur...

import networkx as nwx # Bo� grafik yarat�r, yumru ve ba�lant�lar ekleyebilirsiniz...

grafik =nwx.Graph()

print ("Bo� bir grafi�in yumru listesi:", grafik.nodes() )
print ("Bo� grafi�in ba�lant� listesi:", grafik.edges() )

print ("\nGrafik yumru tipi:", type (grafik.nodes()) )
print ("Grafik ba�lant� tipi:", type (grafik.edges()) )
print ("-"*75)
#---------------------------------------------------------------------------------------------------

grafik.add_node ("a") # Grafi�e tek yumru ekleme...
grafik.add_nodes_from (["b", "c"]) # Grafi�e �oklu yumru ekleme...

grafik.add_edge (1, 2) # Grafi�e yeni "(1,2)" ba�lant�l� 2 yumru ekler...
ba�lant�lar = ("d", "e")
grafik.add_edge (*ba�lant�lar) # Grafi�e yeni "('d', 'e')" ba�lant�l� 2 yumru ekler...
ba� = ("a", "b")
grafik.add_edge (*ba�) # Grafikte mevcut "('a', 'b')" yumrular aras� ba�lant� kurar...
grafik.add_edge (1, "a")
grafik.add_edge ("b", 2)
grafik.add_edge ("a", "e")
grafik.add_edge ("d", "c")
grafik.add_edge ("c", 2)
grafik.add_edge (1, "d")

print ("\nGrafi�in yumru listesi:", grafik.nodes() )
print ("Grafi�in ba�lant� listesi:", grafik.edges() )
print ("-"*75)
#---------------------------------------------------------------------------------------------------

import matplotlib.pyplot as pp # Grafiklerin yumru-ba�lant� �izimlerini yapabilirsiniz...

nwx.draw (grafik)
#pp.savefig ("p_20901.png") # Grafi�i "p_20901.png" resim dosyas� olarak sakla...
pp.show() # Grafi�i ekrana yans�t...



"""��kt�:
>python p_20901.py
Bo� bir grafi�in yumru listesi: []
Bo� grafi�in ba�lant� listesi: []

Grafik yumru tipi: <class 'networkx.classes.reportviews.NodeView'>
Grafik ba�lant� tipi: <class 'networkx.classes.reportviews.EdgeView'>
---------------------------------------------------------------------------

Grafi�in yumru listesi: ['a', 'b', 'c', 1, 2, 'd', 'e']
Grafi�in ba�lant� listesi: [('a', 'b'), ('a', 1), ('a', 'e'), ('b', 2), ('c', 'd'), ('c', 2), (1, 2), (1, 'd'), ('d', 'e')]
---------------------------------------------------------------------------
nx_pylab.py:579: MatplotlibDeprecationWarning:
The iterable function was deprecated in Matplotlib 3.1 and will be removed in 3.3.
Use np.iterable instead. if not cb.iterable(width):
"""