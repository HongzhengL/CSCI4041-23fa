# Heapsort

```pseudocode
# P128
PARENT(i)
    return i/2

LEFT(i)
    return 2i

RIGHT(i)
    return 2i+1

# P130
MAX-HEAPIFY(A, i)
    l = LEFT(i)
    r = RIGHT(i)
    if l <= A.heap-size and A[l] > A[i]
        largest = l
    else
        largest = i
    if r <= A.heap-size and A[r] > A[largest]
        largest = r
    if largest != i
        exchange A[i] with A[largest]
        MAX-HEAPIFY(A, largest)

# P133
BUILD-MAX-HEAP(A)
    A.heap-size = A.length
    for i = A.length/2 downto 1
        MAX-HEAPIFY(A, i)

# P136
HEAPSORT(A)
    BUILD-MAX-HEAP(A)
    for i = A.length downto 2
        exchange A[1] with A[i]
        A.heap-size = A.heap-size - 1
        MAX-HEAPIFY(A, 1)

# P139
HEAP-MAXIMUM(A)
    return A[1]

# P139
HEAP-EXTRACT-MAX(A)
    if A.heap-size < 1
        error "heap underflow"
    max = A[1]
    A[1] = A[A.heap-size]
    A.heap-size = A.heap-size - 1
    MAX-HEAPIFY(A, 1)
    return max

# P140
HEAP-INCREASE-KEY(A, i, key)
    if key < A[i]
        error "new key is smaller than current key"
    A[i] = key
    while i > 1 and A[PARENT(i)] < A[i]
        exchange A[i] with A[PARENT(i)]
        i = PARENT(i)

# P140
MAX-HEAP-INSERT(A, key)
    A.heap-size = A.heap-size + 1
    A[A.heap-size] = -∞
    HEAP-INCREASE-KEY(A, A.heap-size, key)

HEAP-DELETE(A, i)
    A[i] = A[A.heap-size]
    A.heap-size = A.heap-size - 1
    MAX-HEAPIFY(A, i)

```


# Quicksort

```pseudocode
# P146
QUICKSORT(A, p, r)
    if p < r
        q = PARTITION(A, p, r)
        QUICKSORT(A, p, q-1)
        QUICKSORT(A, q+1, r)
    
# P146
PARTITION(A, p, r)
    x = A[r]
    i = p - 1
    for j = p to r - 1
        if A[j] <= x
            i = i + 1
            exchange A[i] with A[j]
    exchange A[i+1] with A[r]
    return i + 1

# P154
RANDOMIZED-PARTITION(A, p, r)
    i = RANDOM(p, r)
    exchange A[r] with A[i]
    return PARTITION(A, p, r)

# P154
RANDOMIZED-QUICKSORT(A, p, r)
    if p < r
        q = RANDOMIZED-PARTITION(A, p, r)
        RANDOMIZED-QUICKSORT(A, p, q-1)
        RANDOMIZED-QUICKSORT(A, q+1, r)
```

Worst-case partitioning(P150):
$$T(n) = T(n-1) + \Theta(n) = \Theta(n^2)$$

Best-case partitioning(P150):
$$T(n) \leq 2T(n/2) + \Theta(n) = O(n \lg n)$$


# Merge sort

```pseudocode
# P29
MERGE(A, p, q, r)
    n1 = q - p + 1
    n2 = r - q
    let L[1..n1+1] and R[1..n2+1] be new arrays
    for i = 1 to n1
        L[i] = A[p+i-1]
    for j = 1 to n2
        R[j] = A[q+j]
    L[n1+1] = ∞
    R[n2+1] = ∞
    i = 1
    j = 1
    for k = p to r
        if L[i] <= R[j]
            A[k] = L[i]
            i = i + 1
        else
            A[k] = R[j]
            j = j + 1

# P32
MERGE-SORT(A, p, r)
    if p < r
        q = ⌊(p+r)/2⌋
        MERGE-SORT(A, p, q)
        MERGE-SORT(A, q+1, r)
        MERGE(A, p, q, r)
```

# MEDIANS AND ORDER STATISTICS

```pseudocode
# P184
MINIMUM(A)
    min = A[1]
    for i = 2 to A.length
        if A[i] < min
            min = A[i]
    return min

# P186
RANDOMIZED-SELECT(A, p, r, i)
    if p == r
        return A[p]
    q = RANDOMIZED-PARTITION(A, p, r)
    k = q - p + 1
    if i == k
        return A[q]
    else if i < k
        return RANDOMIZED-SELECT(A, p, q-1, i)
    else
        return RANDOMIZED-SELECT(A, q+1, r, i-k)
```



# Last Year Midterm

## 1. HeapChangeKey method for a max-heap

The `HeapChangeKey` method for a max-heap is defined as follows, in the notation used in the book. `HeapChangeKey(A, i, key)` should change the key in position `i` to the value key and then make suitable adjustments to `A`, so that `A` once again satisfies the heap property. Write pseudocode for `HeapChangeKey` in the style of the book, explain briefly how it works, and informally analyze its worst-case runtime. Your pseudocode may call any other of the other heap methods supplied in the book.

**Hint**: note that the new key could violate the heap property by either being too big or being too small.

```pseudocode
HeapChangeKey(A, i, key)
    if key > A[i]
        HEAP-INCREASE-KEY(A, i, key)
    else if key = A[i]
        return
    else
        A[i] = key
        MAX-HEAPIFY(A, i)
```

When the new key is bigger than the old key, we can use `HEAP-INCREASE-KEY` to fix the heap property. The worst-case runtime of `HEAP-INCREASE-KEY` is `O(lg n)`. 

When the new key is equal to the old key, we don't need to do anything.

When the new key is smaller than the old key, we can use `MAX-HEAPIFY` to fix the heap property. The worst-case runtime of `MAX-HEAPIFY` is `O(lg n)`. So the worst-case runtime of `HeapChangeKey` is `O(lg n)`.

---

## 2. Divide-and-conquer algorithm to find minimum and maximum values

Consider the following divide-and-conquer algorithm to simultaneously compute the minimum and maximum values in the slice of the array `A` between indexes `p` and `r` inclusive. Describe informally what this algorithm does and why it solves the problem. Write down a recurrence relation for the worst-case runtime of this algorithm. Either find a solution to this recurrence or use the master theorem from the book to solve this recurrence. Show your working for full credit. You may make similar assumptions to those made when recurrences were solved in class. You are only required to solve the recurrence in asymptotic notation (i.e., `O` notation).

```pseudocode
//return (s, b), the smallest and biggest values from A[p : r]
minmax(A, p, r) {
    if r == p then return (A[p], A[p])
    q = (p + r) / 2
    (s1, b1) = minmax(A, p, q)
    (s2, b2) = minmax(A, q+1, r)
    s = s1
    if s2 < s then s = s2
    b = b1
    if b2 > b then b = b2
    return (s, b)
}
```

The algorithm recursively divides the array into two halves, and then finds the minimum and maximum values in each half. Then it compares the minimum and maximum values of the two halves, and returns the minimum and maximum values of the whole array.

The recurrence relation is:
$$
T(n) = 2T(\frac{n}{2}) + 2
$$

The master theorem can be applied to this recurrence relation. $a = 2$, $b = 2$, $f(n) = 2$. $c_{crit} = \log_b a = 1$. 
$f(n) = \Theta(n^c)$ where $c = 0 < c_{crit}$. 
So the solution to the recurrence relation is $T(n) = \Theta(n^{c_{crit}}) = \Theta(n)$.

# Homework 1

1. 
    Suppose a binary heap $B_h$ is of height $h$ and is as small as possible for this to be so. Sketch an informal diagram indicating the shape of $B_h$, and briefly justify it. Let $n$ be the number of nodes in $B_h$. What is $n$ as a function of $h$? Prove that your expression for $n$ is correct.

2. 
    Use your answer to the previous question and denote the size of a binary heap by $n$. Suppose we restrict our attention to binary heaps of height $h$, what range of binary heap sizes $n$ is possible? Briefly justify your answer.

3. 
    Starting with your answer to the previous question on this homework, show that the height $h$ of a binary heap of size $n$ is 
    $$
    h = \lfloor \lg n \rfloor
    $$.

4. 
    What is the index of the last internal node (non-leaf) in a binary heap of size $n$? Briefly justify your answer. Using this, state what range of indexes the leaves of a binary heap of size $n$ has, and briefly state why.

5. 
    Prove that for all natural numbers 
    $$
    n = \left\lfloor \frac{n}{2} \right\rfloor + \left\lceil \frac{n}{2} \right\rceil
    $$.

6. 
    Using your answers to the previous two questions, give very simple expressions for the number of internal nodes and the number of leaves in a binary heap of size $n$.


# Homework 2

1. 
    Give an exact expression for the number of nodes of height 1 in a binary heap of size $n$. You may use a correct answer to the last exercise on Homework 1 without proof. Argue that your solution is correct. 
    **Hint**: If the leaves are first removed, reducing the size of the binary heap in a known way, the nodes previously at height 1 are now the leaves, and you know how to find the number of those from the reduced size.

2. 
    Give an exact expression for the number of nodes of height $h$ in a binary heap of size $n$ where $0 \leq h \leq \lg n$. You may use a correct answer to the last exercise on Homework 1 without proof. Argue that your solution is correct. 
    **Hint**: proceed as in the previous exercise, only remove the leaves $h$ times instead of once. Show that your solution is less than or equal to $\frac{n}{2^{h+1}}$, the value used in the book to analyze the runtime of BuildHeap.

3. 
    Write a non-recursive version of Heapify in the style of the book. Your solution should use a loop to repeat the body of Heapify instead of making a recursive call at the end (a tail-recursive call). It should nevertheless perform the same sequence of operations on the binary heap that the original version does.

4. 
    Write a Delete operation for a binary heap in the style of the book. Delete($A,i$) should delete the item in node $i$. 
    **Hint**: use existing operations in the book to perform this task rather than writing it from scratch. Explain why your solution works, and analyze its runtime.

5. 
    Write pseudocode for an algorithm MultiMerge($A$) that is passed an array containing $k$ sorted arrays each of the same length $n/k$ for a total of $n$ elements. Assume that $k \geq 2$ and $n/k \geq 1$. Assume all arrays are indexed from 1. Assume these sizes can be obtained from $A$ using $A$.length to get $k$ and $A[1]$.length to get $n/k$. MultiMerge($A$) should merge the sorted arrays in $A$ into a single sorted array, and it should do so in time $\Theta(n \lg k)$. 
    **Hint**: finding the maximum of $k$ items can be done in time $\Theta(\lg k)$ using a binary heap.

6. 
    Show that the solution to the recurrence $T(n) = T(n - 1) + n$ is $\Theta(n^2)$.

7. 
    Solve the following recurrence relation _exactly_ assuming that $T(1) = 1$ and that $n$ is an exact power of 2 i.e. $n = 2^k$ for $k \in \mathbb{N}$. Show all your working.
    $$
    T(n) = 2T\left(\frac{n}{2}\right) + n \lg n
    $$

## Master Theorem

The Master Theorem provides a method to solve recurrences of the form:
$$T(n) = a \cdot T\left(\frac{n}{b}\right) + f(n)$$

Where:
- $a \geq 1$ (number of recursive calls)
- $b > 1$ (factor by which the problem size is divided)
- $f(n)$ is the cost of the work done outside the recursive calls.

### Steps to Apply Master Theorem:

1. **Determine the Form of the Recurrence**:
   Ensure that the recurrence fits the standard form.

2. **Calculate Critical Exponent**:
   Determine $c_{crit} = \log_b a$

3. **Compare $f(n)$ to $n^{c_{crit}}$**:
   There are three main cases:

   - **Case 1**: If $f(n) = O(n^c)$ where $c < c_{crit}$
     - Solution: $T(n) = \Theta(n^{c_{crit}})$

   - **Case 2**: If $f(n) = \Theta(n^{c_{crit}} \cdot \log^k n)$ 
   for some $k \ge 0$
     - Solution: $T(n) = \Theta(n^{c_{crit}} \cdot \log^{k+1} n)$

   - **Case 3**: If $f(n) = \Omega(n^c)$ where $c > c_{crit}$ and $af\left(\frac{n}{b}\right) \leq kf(n)$ 
   for some $k < 1$ and sufficiently large $n$
     - Solution: $T(n) = \Theta(f(n))$

4. **Formulate the Solution**:
   Based on the matching case, write down the solution for $T(n)$.

5. **Note on Irregular Cases**:
   The Master Theorem doesn't cover every possible form of $f(n)$. In such cases, you might need to rely on other methods like the recursion-tree method or substitution method.

# Asymptotic Notation

$\Theta (g(n))$ = { 
$f(n)$: there exist positive constants $c_1$, $c_2$, 
and $n_0$ such that $0 \leq c_1g(n) \leq f(n) \leq c_2g(n)$ 
for all $n \leq n_0$. 
}

$O(g(n))$ = {
$f(n)$: there exist positive constants $c$ and $n_0$
such that $0 \leq f(n) \leq cg(n)$ for all $n \geq n_0$.
}

$\Omega(g(n))$ = {
$f(n)$: there exist positive constants $c$ and $n_0$
such that $0 \leq cg(n) \leq f(n)$ for all $n \geq n_0$.
}

