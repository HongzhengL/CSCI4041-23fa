#### Discussion Section 012

<h1 style="text-align: center;">CSCI4041 Homework 6</h1>

<h4 style="text-align: center;">Hongzheng Li</h4>

## Problem 1:

Suppose for contradiction that there is no MST of $G$ that contains $e$. 
Since $G$ is connected, we know that it has at least one spanning tree. 
So, it must have at least one MST, say $T$, which does not contain $e$.

By the definition of spanning tree, $T$ must contain a path $P$ in $T$ from $u$ to $v$.

From the textbook, we know that this path must contain at least one edge $(x, y)$ 
that crosses the cut of the graph which divides the set of vertices into two subsets: 
one containing $u$ and the other containing $v$.

Now, let's construct a new spanning tree $T'$ 
by adding $e = (u, v)$
and removing $(x, y)$ 
from $T$.

Since $(u,v)$ is an edge of minimum weight,
the weight of $(x, y)$ must be greater than or equal to that of $(u, v)$.
Therefore, the total weight of $T'$ is less than or equal to that of $T$.

On the other hand, since $T$ is a minimum spanning tree,
the total weight of $T'$ 
must be greater than or equal to that of $T$,
otherwise $T$ is not a minimum spanning tree.

Therefore, we conclude that the total weight of $T'$ 
is equal to that of $T$.
Then, it follows that $T'$ 
is also a minimum spanning tree of $G$.
It's a contradiction since we assume that no MST should contain $e$.

Therefore, there must be at least one MST of $G$ that contains $e$.

---

## Problem 2:

Let $T$ be a minimum spanning tree of $G$.
Let $e$ be an arbitrary edge of $G$ that belongs to $T$.

From the textbook, we know that removing $e=(u, v)$ 
from $T$ will divide $T$ into two subtrees $T_1$ and $T_2$.

Then, $(T_1, T_2)$ is the cut 
that respects $T_1$ and $T_2$.
Since $T$ is a minimum spanning tree, $e$ crosses this cut and it must be a light edge for this cut.
That is, for any edge $e'$ crossing this cut, 
$w(e) \leq w(e')$.

Otherwise, we could take a lighter weight edge $e'$ 
crossing this cut and use it to replace $e$.
Then, we would get a spanning tree with a smaller total weight than $T$.
This contradicts the fact that $T$ is a minimum spanning tree.

Therefore, $e$ is a light edge crossing the some cut of $G$.

---

## Problem 3:

At each step of the algorithm we will add an edge from a vertex in the tree
created so far to a vertex not in the tree, such that this edge has minimum
weight. Thus, it will be useful to know, for each vertex not in the tree, the edge
from that vertex to some vertex in the tree of minimal weight.

Instead of using priority queue, we will use a 2-D array to maintein this information,
where A[i][1] is some vertex in the tree, 
and A[i][2] is the weight of the edge from vertex i to A[i][1]. 

The pseudocode is as follows:

```pseudocode
MST-PRIM-NAIVE(G, w, r)
    Initialize a 2-D array A[n][2]
    for each vertex i in G:
        A[i][1] = None 
        A[i][2] = Infinity 

    A[r][1] = r
    A[r][2] = 0

    MST = {  }

    while MST has fewer than n vertices:

        u = vertex not in MST with minimum A[u][2]  # use a for loop to find u
                                                    # linear time search

        add u to MST

        for each vertex v not in MST:
            if edge u-v exists in G and w(u, v) < A[v][2]:
                A[v][1] = u
                A[v][2] = w(u, v)

    return MST
```

**Runtime Analysis:**

According to the pseudocode, 

- The initialization of the array A will traverse $n$ vertices, 
which takes $\Theta(n)$ time.
- The while loop will add one vertex to the MST in each iteration, and we have $n-1$ vertices in the MST. So, it will run $\Theta(n)$ times.
- The process of finding the vertex $u$ not in the MST with the minimum edge weight 
will traverse all the vertices in the graph, which will run $\Theta(n)$ times.
- And the for loop inside the while loop traverses all the vertices in the graph, 
which also will run $\Theta(n)$ times.

The total runtime inside the while loop is $\Theta(n)+\Theta(n)=\Theta(n)$.
Therefore, the total runtime of the algorithm is $\Theta(n)+\Theta(n^2)=\Theta(n^2)$.

---

## Problem 4:

The matrix plays a role corresponding to the $L^{(0)}$ matrix, which is the initial matrix that
represents direct distances between vertices.

The diagonal elements are $0$, 
indicating that the distance from a vertex to itself is $0$.

The non-diagonal elements are $\infty$, 
indicating the absence of direct edges between vertices.

From the textbook, we have
$$L^{(1)} = L^{(0)}\cdot W = W^1$$
$$l_{ij}^{(r)} = min\{l_{ij}^{(r)}, l_{ik}^{(r-1)}+w_{kj}\}$$
Observe from the two equations above, we can see that
taking a minimum of any number with positive infinity 
will get the same number back.
That is, $W=W^1$.
Therefore,
this matrix also plays a role of the identity matrix in normal matrix multiplication.

---

## Problem 5:

Let matrix $A$, $B$ and $C$ be well-defined matrix.
 
To verify the associativity, we need to prove that
$$(A\cdot B)\cdot C = A\cdot (B\cdot C)$$

By the definition of (min, +) matrix multiplication, 

for the left-hand side, we have
$$\begin{aligned}
((A\cdot B) \cdot C)_{ij}
&= min_l((A\cdot B)_{il}+C_{lj}) \\
&= min_l (min_k((A_{ik}+B_{kl})+C_{lj})) \\
&= min_l min_k(A_{ik}+B_{kl}+C_{lj})
\end{aligned}$$

for the right-hand side, we have
$$\begin{aligned}
(A\cdot (B \cdot C ))_{ij}
&= min_k(A_{ik}+ (B\cdot C)_{kj}) \\
&= min_k (A_{ik}+min_l(B_{kl}+C_{lj})) \\
&= min_k min_l(A_{ik}+B_{kl}+C_{lj})
\end{aligned}$$

Since the min operation and plus operation is commutative and associative,
the order of taking minimum does not affect the outcome.
Thus, we have
$$min_l min_k(A_{ik}+B_{kl}+C_{lj}) = min_k min_l(A_{ik}+B_{kl}+C_{lj})$$

Therefore, LHS equal RHS.
And we have proven that (min, +) matrix multiplication is associative.

---

## Problem 6:

First, initialize the predecessor matrix $\Pi$ such that
$\Pi_{ij}$ is set to $i$ if there is a direct edge from $i$ to $j$,
and NIL if either $i=j$ or there is no direct edge from $i$ to $j$.

Then, for each pair of vertices $(i, j)$, compute the shortest path using
an intermediate vertex $k$.

For $k$ from $1$ to $n$,
for $i$ from $1$ to $n$,
for $j$ from $1$ to $n$,
do the following:

> If $L_{ik}+W_{kj}<L_{ij}$, 
then update $L_{ij}$ 
to $L_{ik}+W_{kj}$ 
and set $\Pi_{ij}$ to $\Pi_{kj}$,
which indicates that the predecessor of $j$ on the shortest path from $i$ 
is the predecessor of $j$ on the shortest path from $k$ to $j$.

After the above process,
$\Pi_{ij}$ will contain the predecessor for the shortest paths.

**Runtime Analysis:**
We use $3$ nested for loops to iterate through all the vertices in the graph,
therefore, the runtime is $\Theta(n^3)$,
which satisfies the requirement.

---

## Problem 7:

Let's denote $d_{ij}^{(k)}$ 
as the shortest path from vertex $i$ 
to vertex $j$ that only uses vertices from the set $\{1, 2, ..., k\}$ 
as intermediate vertices.
We want to show that after the completion of the algorithm, $d_{ij}$
in matrix $D$ equals $d_{ij}^{(n)}$ for all $i$ and $j$.

**Base case:**

After the initialization of matrix $D$,
$d_{ij}$ represents the weight of the edge $(i, j)$ if it exists,
or infinity if it does not.
This satisfies the condition for $k=0$, as there are no intermediate vertices.
Thus, $d_{ij} = d_{ij}^{(0)}$.

**Induction Hypothesis:**

Assume that before the $kth$ iteration,
$d_{ij} = d_{ij}^{(k-1)}$ for all $i$ and $j$. 
That is, it works correctly before the $kth$ iteration.

**Inductive step:**

Consider the $kth$ iteration. We need to show that after this iteration,
$d_{ij}$ will be updated to $d_{ij}^{(k)}$ if and only if the shortest path 
from $i$ to $j$ using vertices {1, 2, ..., k} is shorter than $d_{ij}^{(k-1)}$.

We update $d_{ij}$ using the following formula:
$$d_{ij} = min(d_{ij}, d_{ik}+d_{kj})$$

By induction hypothesis, 
$d_{ik}$ and $d_{kj}$ are the shortest paths 
from $i$ to $k$ 
and from $k$ to $j$, respectively,
using vertices {1, 2, ..., k-1} as intermediate vertices.
Therefore, $d_{ik}+d_{kj}$ is the length of a path 
from $i$ to $j$ that goes through $k$ using any intermediate vertices
from {1, 2, ..., k-1}. If this is shorter than current $d_{ij}$, 
then we update $d_{ij}$ to this value, which is $d_{ij}^{(k)}$.
If not, then we do not update $d_{ij}$, which is still $d_{ij}^{(k-1)}$.

In short, at every iteration $k$, the values in matrix $D$
only depend on the values of the previous matrix $D^{k-1}$.
Thus, it is safe to overwrite the values in matrix $D^{k-1}$.
to matrix $D^k$.

Therefore, we have proven the resulting algorithm is correct.
