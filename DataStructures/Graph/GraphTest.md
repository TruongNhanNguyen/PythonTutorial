# Testing graph

## Creating Graph

Firstly, we create a simple graph by using the command below:

```Python
G = Graph(directed=True)            # I demo a directed graph firstly. If you wanna create a undirected graph, set optional parameter directed=False
```

Next, use `insert_vertex(element=None)` method to create vertices for the graph.

Because `insert_vertex(element=None)` method return a `Vertex` object, we will use ***alphabet characters*** to denote vertices.

```Python
u = G.insert_vertex('SFO')
v = G.insert_vertex('JFK')
w = G.insert_vertex('BOS')
x = G.insert_vertex('ORD')
y = G.insert_vertex('LAX')
z = G.insert_vertex('DFW')
t = G.insert_vertex('MIA')
```

Then, the graph must have to edges connecting the vertices of the graph. To create Edges, **Graph** class provides a method for this task `insert_edge(origin, destination, element=None)`. This method return an `Edge` object. Sample code below:

```Python
vu = G.insert_edge(v, u, 'SW 45')
wv = G.insert_edge(w, v, 'NW 35')
wt = G.insert_edge(w, t, 'DL 247')
vt = G.insert_edge(v, t, 'AA 903')
vz = G.insert_edge(v, z, 'AA 1387')
yx = G.insert_edge(y, x, 'UA 120')
xz = G.insert_edge(x, z, 'UA 877')
zx = G.insert_edge(z, x, 'DL 335')
zy = G.insert_edge(z, y, 'AA 49')
ty = G.insert_edge(t, y, 'AA 411')
tz = G.insert_edge(t, z, 'AA 523')
```

## Use of Graph's methods

### Check if the graph is directed or undirected

Use this command:

```Python
G.is_directed()
```

### Counting vertices and edges of the graph

The **Graph** class supports two methods for this task:

- [x] `vertex_count()`
- [x] `edge_count()`

```Python
print(G.vertex_count())
print(G.edge_count())
```

## Print element stored in graph's edges or vertices

**Graph** class supports two methods `edges()` and `vertices()`. Each of them return a generator of **Objects** and to retrive the element we have two use the `for loop` and the `element()` method in each class (`Edge` and `Vertex` classes).

```Python
for e in G.edges():
    print(e.element())

for v in G.edges():
    print(v.element())
```

## Find the incident edges or vertices of a specify vertex `v`

Two methods `incident_edges(v, outgoing=True)` and `incident_vertices(v, outgoing=True)` return **generators**, so we use the `for loop` statement to print elements of them. The optional parameter `outgoing` is set default to `True` to produce outgoing vertices or edges. You can set it to `True` for incoming.

```Python
for v in G.incident_vertices(z):
    print(v.element(z))

for v in G.incident_vertices(z, outgoing=False):
    print(v.element())

for e in G.incident_edges(z):
    print(e.element())

for e in G.incident_edges(z, outgoing=False):
    print(e.element())
```

## Remove edge or vertex

Use these methods `remove_edge(edge)` and `remove_vertex(vertex)`

Example:

```Python
# I want to remove the edge vu
G.remove_edge(vu)
# Or you wanna remove the vertex z and all of its incident edges
G.remove_vertex(z)
```

## Traversal Algorithms
