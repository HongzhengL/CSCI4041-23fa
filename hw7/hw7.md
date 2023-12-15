#### Discussion Section 012

<h1 style="text-align: center;"> CSCI4041 Homework 7  </h1>

<h4 style="text-align: center;"> Hongzheng Li </h4>

## Problem 1:

```python
GET-INTERMEDIA-PATH(i, j, p)
    Path = []
    for k = 1 to p.length:
        if p[k][i][j] == True:
            Path.append(GET-INTERMEDIA-PATH(i, k, p))
            Path.append(k)
            Path.append(GET-INTERMEDIA-PATH(k, j, p))
            break
    return Path


PRINT-ANY-PATH(i, j, p)
    Path = GET-INTERMEDIA-PATH(i, j, p)
    if there is not a path from i to j:
        error "NO path from i to j"
    else if Path == []:
        print(i, j)
    else:
        print(i, Path, j)
```

**Why the algorithm is correct:**

By the definition of $p^{(k)}_{ij}$,
we know that $p^{(k)}_{ij}$ is true 
if and only if there are at least one intermediate vertex from vertex $i$ to vertex $j$.
And since we want to find the shortest path from vertex $i$ to vertex $j$,
we also need to find the shortest path from vertex $i$ to vertex $k$,
and the shortest path from vertex $k$ to vertex $j$.
Repeat this process until we find the shortest path for all the intermediate vertices.
Therefore, we use a helper function `GET-INTERMEDIA-PATH(i, j, p)`
to find all the intermediate vertices in the shortest path from vertex $i$ to vertex $j$.

**Runtime Analysis:**

Assume we have $n$ vertices in the graph.
In the worst case, the algorithm will have to check every vertex in the graph 
in all of the three dimensions ancillary array $p$. 
And since checking one vertex in the ancillary array takes $O(n)$ time, 
and we have to check $n$ vertices in the worst case,
the total runtime of the algorithm is $O(n^2)$.

**The solution need the whole of array p.**

The reason is that $p^{(k)}_{ij}$ represents if there is a path that
goes through vertex $k$ from vertex $i$ to vertex $j$ in the shortest path.
To find out the shortest path from vertex $i$ to vertex $j$,
we also need to know the shortest path from vertex $i$ to vertex $k$,
and the shortest path from vertex $k$ to vertex $j$.
Therefore, we need to know the whole of array $p$.

---

## Problem 2:

We can do this by modifying BFS as follows:

For vertices with even distances, color them red, 
and for vertices with odd distances, color them green. 
If we encounter a vertex that has already been colored, 
and the color is the same as the current vertex, 
then we know that the graph is not bipartite. 
Otherwise, the graph is bipartite.

Below is the pseudocode for this algorithm:

```python
BFS-Bipartite(G, s)  # G is a graph, s is the source vertex
    for each vertex u in G.V - {s}
        u.color = None
        u.pi = NIL
        u.distance = INF
    
    s.color = RED
    s.pi = NIL
    s.distance = 0
    Q = { }
    ENQUEUE(Q, s)

    while Q != EMPTY
        u = DEQUEUE(Q)
        for each v in G.Adj[u]
            if v.distance == INF
                v.distance = u.distance + 1
                v.color = (RED if u.distance % 2 == 0 else GREEN)
                v.pi = u
                ENQUEUE(Q, v)
            else if v.color == u.color
                return False

    return True
```

**Why the algorithm is correct:**

The algorithm is correct because it explores vertices in layers. 
When it moves from one layer to the next, it increases the distance from the source vertex. 
Since a bipartite graph has the characteristic that vertices on one side of the partition only have edges to vertices on the other side, 
BFS can exploit this by alternating colors between layers. 
Vertices on the same layer will not be adjacent, 
so they can have the same color. 
The alternating colors correspond to even and odd distances from the source vertex.
If it completes without finding an edge violating this condition, the graph is bipartite.
Otherwise, it is not bipartite.

---

## Problem 3:

```python
dfs(v):
    component[v] = component_number
    for each u in adjacency_list[v]:
        if component[u] == -1:
            dfs(u)

initialize component[] array to all -1
component_number = 1
for v = 1 to number_of_vertices:
    if component[v] == -1:
        dfs(v)
        component_number += 1
```

**Why the algorithm is correct:**

This solution is correct 
because DFS is a graph traversal algorithm 
that exhaustively searches through all vertices and edges in a connected component. 
By running DFS from an unvisited vertex (i.e. a vertex with component number -1), 
we can mark all vertices reachable 
from that starting vertex with the same component number. 
Since the DFS will only visit each vertex once, 
and vertices in different connected components 
will not be reached by the same DFS call, 
this correctly identifies the connected components of the graph.

---

## Problem 4:

The algorithm for computing the component graph is as follows:

1. Perform STRONGLY-CONNECTED-COMPONENTS(G) 
    to find the strongly connected components of G.
2. Next, assign an identifier to each node in $G$
    based on the SCC it belongs to. If there are $k$ SCCs, 
    each node gets a value in the range $[1, k]$,
    where all nodes in the $kth$ SCC receive the identifier $k$.
3. Iterate through each node $i$ in $G$, 
    and for each node $j$ in $G.Adj[i]$,
    check if there is already an edge between the $i$ 
    and $j$ 
    in $G'$.
    If not, and if $component[i] \neq component[j]$,
    add an edge between $component[i]$ 
    and $component[j]$ 
    in $G'$.


**Why the algorithm is correct:**

The algorithm is correct because it first finds the strongly connected components of the graph,
then it assigns an identifier to each node in $G$ based on the SCC it belongs to.
This makes sure that all nodes in the same SCC have the same identifier.
Then, it iterates through each node $i$ in $G$, 
if there is an edge from a vertex in the $SCC$ represented by $u'$
to a vertex in the $SCC$ represented by $v'$,
then we add an edge in $G'$. 
This ensures that $G'$ is a DAG 
because there cannot be a back-edge to an SCC; 
within an SCC, all nodes are mutually reachable, 
and between different SCCs, there is only a one-directional reachability.

For the runtime, since the algorithm iterates through each node in $G$,
and for each node, it iterates through all the edges in $G.Adj[i]$,
the runtime of the algorithm is $O(|V| + |E|)$.

Then, we have find an algorithm of runtime $O(|V| + |E|)$
that finds the component graph of a digraph $G$.

---

## Problem 5:

```pseudocode
IS-SEMICONNECTED(G)
    Use the method in Problem #4 to find the component graph G' of graph G
    TOPOLOGICAL-SORT(G')
    for i = 1 to n-1
        if there is no edge from G'.v[i] to G'.v[i+1]
            return False
    return True
```

**Why the algorithm is correct:**

The algorithm is correct because it first finds the component graph of graph $G$,
then it performs topological sort on the component graph $G'$, 
which ensures that $v_i$ comes before $v_{i+1}$.
After that, for consecutive vertices $v_i$ and 
$v_{i+1}$ in $G'$,
If there is no edge from $v_i$ to $v_{i+1}$,
then there is no path from $v_{i+1}$ to 
$v_i$ in $G$ 
since $v_{i}$ finished 
after $v_{i+1}$.
Using the definition of $G'$,
we know that there is no path from any vertices in $G$ for
vertex represented by $v_{i}$ 
to vertex represented by $v_{i+1}$.
Then it's **NOT** semiconnected and we return False.
Otherwise, we return True.
