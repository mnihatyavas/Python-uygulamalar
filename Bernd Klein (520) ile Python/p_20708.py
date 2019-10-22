# coding:iso-8859-9 Türkçe
# p_20708.py: Grafiğin yumruları, bağlantıları, dereceleri, yumru ve bağlantı ekleme, izole yumrular örneği.

# Bu örneğin Türkçeleştirilmesi p_20702.py
# ve p_20703.py, p_20704.py, p_20705.py, p_20706.py, p_20707.py
# örneklerinde mevcuttur...

from p_20708x import Graph

g = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
    }

graph = Graph (g)
print (graph)

for node in graph.vertices(): print (graph.vertex_degree (node))

print ("\nList of isolated vertices:")
print (graph.find_isolated_vertices())

print ('\nA path from "a" to "e":')
print (graph.find_path ("a", "e"))

print ('\nAll pathes from "a" to "e":')
print (graph.find_all_paths ("a", "e"))

print ("\nThe maximum degree of the graph is:")
print (graph.Delta() )

print ("\nThe minimum degree of the graph is:")
print (graph.delta() )

print ("\nEdges:")
print (graph.edges() )

print ("\nDegree Sequence: ")
ds = graph.degree_sequence()
print (ds)

fullfilling = [
    [2, 2, 2, 2, 1, 1],
    [3, 3, 3, 3, 3, 3],
    [3, 3, 2, 1, 1]
]

non_fullfilling = [
    [4, 3, 2, 2, 2, 1, 1],
    [6, 6, 5, 4, 4, 2, 1],
    [3, 3, 3, 1]
]

print ("\nErdös-Galay'ı sağlayan ve sağlamayan liste:")
for sequence in fullfilling + non_fullfilling: print (sequence, Graph.erdoes_gallai (sequence) )

print ("\nAdd vertex 'z':")
graph.add_vertex ("z")
print (graph)

print ("\nAdd edge ('x','y'): ")
graph.add_edge (('x', 'y'))
print (graph)

print ("\nAdd edge ('a','d'): ")
graph.add_edge (('a', 'd'))
print (graph)

"""Çıktı:
>python p_20708.py
vertices: a b c d e f
edges: {'a', 'd'} {'c', 'b'} {'c'} {'c', 'd'} {'e', 'c'}
1
1
5
2
1
0

List of isolated vertices:
[] a
[] b
[] c
[] d
[] e
[] f
['f']

A path from "a" to "e":
['a', 'd', 'c', 'e']

All pathes from "a" to "e":
[['a', 'd', 'c', 'e']]

The maximum degree of the graph is:
5

The minimum degree of the graph is:
0

Edges:
[{'a', 'd'}, {'c', 'b'}, {'c'}, {'c', 'd'}, {'e', 'c'}]

Degree Sequence:
(5, 2, 1, 1, 1, 0)

Erdös-Galay'ı sağlayan ve sağlamayan liste:
[2, 2, 2, 2, 1, 1] True
[3, 3, 3, 3, 3, 3] True
[3, 3, 2, 1, 1] True
[4, 3, 2, 2, 2, 1, 1] False
[6, 6, 5, 4, 4, 2, 1] False
[3, 3, 3, 1] False

Add vertex 'z':
vertices: a b c d e f z
edges: {'a', 'd'} {'c', 'b'} {'c'} {'c', 'd'} {'e', 'c'}

Add edge ('x','y'):
vertices: a b c d e f z y
edges: {'a', 'd'} {'c', 'b'} {'c'} {'c', 'd'} {'e', 'c'} {'y', 'x'}

Add edge ('a','d'):
vertices: a b c d e f z y
edges: {'a', 'd'} {'c', 'b'} {'c'} {'c', 'd'} {'e', 'c'} {'y', 'x'}
"""