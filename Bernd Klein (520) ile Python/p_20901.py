# coding:iso-8859-9 Türkçe
# p_20901.py: Networkx grafik modülüne yumru ve bağlantı ekleme, mathplotlib'le grafik çıktısı örneği.

# Online "pip install networkx" ve "matplotlib, numpy" modüllerini indir, kur...

import networkx as nwx # Boş grafik yaratır, yumru ve bağlantılar ekleyebilirsiniz...

grafik =nwx.Graph()

print ("Boş bir grafiğin yumru listesi:", grafik.nodes() )
print ("Boş grafiğin bağlantı listesi:", grafik.edges() )

print ("\nGrafik yumru tipi:", type (grafik.nodes()) )
print ("Grafik bağlantı tipi:", type (grafik.edges()) )
print ("-"*75)
#---------------------------------------------------------------------------------------------------

grafik.add_node ("a") # Grafiğe tek yumru ekleme...
grafik.add_nodes_from (["b", "c"]) # Grafiğe çoklu yumru ekleme...

grafik.add_edge (1, 2) # Grafiğe yeni "(1,2)" bağlantılı 2 yumru ekler...
bağlantılar = ("d", "e")
grafik.add_edge (*bağlantılar) # Grafiğe yeni "('d', 'e')" bağlantılı 2 yumru ekler...
bağ = ("a", "b")
grafik.add_edge (*bağ) # Grafikte mevcut "('a', 'b')" yumrular arası bağlantı kurar...
grafik.add_edge (1, "a")
grafik.add_edge ("b", 2)
grafik.add_edge ("a", "e")
grafik.add_edge ("d", "c")
grafik.add_edge ("c", 2)
grafik.add_edge (1, "d")

print ("\nGrafiğin yumru listesi:", grafik.nodes() )
print ("Grafiğin bağlantı listesi:", grafik.edges() )
print ("-"*75)
#---------------------------------------------------------------------------------------------------

import matplotlib.pyplot as pp # Grafiklerin yumru-bağlantı çizimlerini yapabilirsiniz...

nwx.draw (grafik)
#pp.savefig ("p_20901.png") # Grafiği "p_20901.png" resim dosyası olarak sakla...
pp.show() # Grafiği ekrana yansıt...



"""Çıktı:
>python p_20901.py
Boş bir grafiğin yumru listesi: []
Boş grafiğin bağlantı listesi: []

Grafik yumru tipi: <class 'networkx.classes.reportviews.NodeView'>
Grafik bağlantı tipi: <class 'networkx.classes.reportviews.EdgeView'>
---------------------------------------------------------------------------

Grafiğin yumru listesi: ['a', 'b', 'c', 1, 2, 'd', 'e']
Grafiğin bağlantı listesi: [('a', 'b'), ('a', 1), ('a', 'e'), ('b', 2), ('c', 'd'), ('c', 2), (1, 2), (1, 'd'), ('d', 'e')]
---------------------------------------------------------------------------
nx_pylab.py:579: MatplotlibDeprecationWarning:
The iterable function was deprecated in Matplotlib 3.1 and will be removed in 3.3.
Use np.iterable instead. if not cb.iterable(width):
"""