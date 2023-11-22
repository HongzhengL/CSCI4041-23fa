#### Discussion Section 012

<h1 style="text-align: center;">CSCI4041 Homework 2</h1>

<h4 style="text-align: center;">Hongzheng Li</h4>

## Problem 1:

By definition, we know that the number of nodes at height 0 is the number of leaves in a binary heap, from Problem #6 in Homework 1, we know that is
$$\lceil \frac{n}{2} \rceil$$

Removing the leaves and we get a binary heap of size $n - \lceil \frac{n}{2} \rceil = \lfloor \frac{n}{2} \rfloor$

By definition of the height of the node, the number of nodes at height 1 in a binary heap of size n is the number of nodes at height 0 in the previously removed binary heap of size $\lfloor \frac{n}{2} \rfloor$, using what we get from above(let $n=\lfloor \frac{n}{2} \rfloor$ in $\lceil \frac{n}{2} \rceil$), it's given by
$$\lceil \frac{\lfloor \frac{n}{2} \rfloor}{2} \rceil$$

Therefore, the number of nodes at height 1 is given by
$$\lceil \frac{\lfloor \frac{n}{2} \rfloor}{2} \rceil$$

---

## Problem 2:

First, we prove the following equation holds:
$$\lfloor \frac{\lfloor \frac{n}{2^a} \rfloor}{2} \rfloor = \lfloor \frac{n}{2^{a+1}} \rfloor$$

Use the definition of floor function, we have
$$\lfloor \frac{n}{2^a} \rfloor = \frac{n}{2^a} - r$$
where $0 \leq r < 1$, $r$ is the fractional part of $n/2^h$

Now, divide it by 2:
$$\frac {\lfloor \frac{n}{2^a} \rfloor}{2} = \frac {\frac{n}{2^a} - r}{2} = \frac{n}{2^{a+1}} - \frac{r}{2}$$

Taking floor of the above expression:
$$\lfloor \frac{\lfloor \frac{n}{2^a} \rfloor}{2} \rfloor = \lfloor \frac{n}{2^{a+1}} - \frac{r}{2} \rfloor$$

Since $0 \leq r < 1$, then $0 \leq \frac{r}{2} < 0.5$

Therefore, we have
$$\lfloor \frac{n}{2^{a+1}} - \frac{r}{2} \rfloor= \lfloor \frac{n}{2^{a+1}} \rfloor$$

Putting it together,
$$\lfloor \frac{\lfloor \frac{n}{2^a} \rfloor}{2} \rfloor = \lfloor \frac{n}{2^{a+1}}  \rfloor$$

From Problem #1, we know that the number of nodes at height 1 of size n is the number of nodes at height 0 of size $\lfloor \frac{n}{2^{1}} \rfloor$

for the number of nodes at height 2 of size n, it's equal to the number of nodes at height 0 of size $ \lfloor \frac{\lfloor \frac{n}{2} \rfloor}{2} \rfloor = \lfloor \frac{n}{2^{2}} \rfloor$

for the number of nodes at height 3 of size n, it's equal to the number of nodes at height 0 of size $ \lfloor \frac{\lfloor \frac{n}{2^2} \rfloor}{2} \rfloor = \lfloor \frac{n}{2^{3}} \rfloor$

<div style="text-align: center;">......</div>

for the number of nodes at height h of size n is the number of nodes at height 0 of size $\lfloor \frac{n}{2^{h}} \rfloor$, and by Problem #1, that is
$$\lceil \frac{\lfloor \frac{n}{2^h} \rfloor}{2} \rceil$$

Therefore, the expression for the number of nodes of height $h$ in a binary heap of size $n$ is

$$\lceil \frac{\lfloor \frac{n}{2^h} \rfloor}{2} \rceil$$

---

Using the definition of floor, we know that
$$\lfloor \frac{n}{2^h} \rfloor \leq \frac{n}{2^h}$$

Dividing them by 2, we have
$$\frac{\lfloor \frac{n}{2^h} \rfloor}{2} \leq \frac{n}{2^{h+1}}$$

By the definition of ceil function, we have
$$\lceil \frac{\lfloor \frac{n}{2^h} \rfloor}{2}\rceil \leq \lceil \frac{n}{2^{h+1}} \rceil$$

---

## Problem 3:

```python
MAX-HEAPIFY(A, i)
    while True
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
            i = largest
        else
            break

```

---

## Problem 4:

``` python
DELETE(A, i)
    A[i] = A[A.heap-size]
    A.heap-size = A.heap-size - 1
    HEAPIFY(A, i)
```

Explanation:

- When removing an element, there'll be a gap left in its place. By taking the last element of the heap and placing it in this gap, we're effectively delete the node i without causing other gap. 

- Then, reduce the size of the heap by 1 since the program removes one node. 

- However, the element we've moved might either too large or too small relative to its neighbors, so we use the HEAPIFY function to restructure the heap and ensure that the heap property is maintained.

Runtime analysis:

- Assigning the last element to position i takes constant time, which is $O(1)$

- Decrementing the heap-size takes constant time, which is $O(1)$

- HEAPIFY takes a runtime of $O(\lg n)$, 
where $n$ is the number of elements in the heap.
In the worst case, the element at index $i$ might need to be moved down the height of the tree to find its correct place.

Therefore, the overall runtime of DELETE operation takes a runtime of $O(\lg n)$


---

## Problem 5:

``` python
#starting index is 1
MULTIMERGE(A)
    H <- MinHeap    #insert a turple and sort its first element
    result <- array #result is an array to store the merged array
    carry <- turple #carry[1]: the smallest unsorted value from the kth array
                    #carry[2]: the index of the kth array
                    #carry[3]: the index of the smallest unsorted value in the kth array
    for i <- 1 to A.length
        H.push((A[i][1], i, 1)) #initialize

    while H.not_empty()
        H.heapify() #heap sort the first element in the turple
        carry = H.top()
        H.pop()
        result.push(carry[1])
        
        if carry[3] < A[carry[2]].length
            H.push(A[carry[2]][carry[3]+1], carry[2],carry[3]+1)

    return result
```

---

## Problem 6:

We know $$T(n)=T(n-1)+n$$
then 
$$\begin{equation}
\tag{1}
T(n) - T(n-1) = n
\end{equation}$$

let $n = n - 1$, then
$$\begin{equation}
\tag{2}
T(n-1) - T(n-2) = n-1
\end{equation}$$

Doing so repeatedly, we have:

$$\begin{equation}
\tag{3}
T(n-2) - T(n-3) = n-2
\end{equation}$$

$$\begin{equation}
\tag{4}
T(n-3) - T(n-4) = n-3
\end{equation}$$

<div style="text-align: center;">......</div>

$$\begin{equation}
\tag{n-1}
T(2) - T(1) = 2
\end{equation}$$

$$\begin{equation}
\tag{n}
T(1) - T(0) = 1
\end{equation}$$

Adding equation (1) to (n) together, we have 
$$T(n)=T(0)+1+2+...+(n-1)+n = T(0)+n^2/2+n/2$$

$T(0)$ is a constant, and $n^2$ dominates the linear term $n$ as $n$ grows larger.
Therefore, the solution to the recurrence $T(n)=T(n-1)+n$ is $\Theta(n^2)$

---

## Problem 7:

Let $n = 2^k$, then $\lg n = k$, then we have $$T(2^k) = 2T(2^{k-1})+k \times 2^k$$

Let $u_k = T(2^k)$ for $k \in N$, then we have $u_{k-1} = T(2^{k-1})$

Plugging in, we have 
$$u_k=2u_{k-1}+k \times 2^k$$

Let $u_k=2^kv_k$, then we have
$$2^kv_k=2^kv_{k-1}+k \times 2^k$$

Divide both side by $2^k$, $$v_k=v_{k-1}+k$$

Subtract $v_{k-1}$ from both sides,
$$v_k-v_{k-1}=k$$

then $$\sum_{i=1}^{k} (v_i - v_{i-1}) = v_k - v_0 = k + (k-1) + ... + 2 + 1$$

that is
$$v_k=v_0+k+(k-1)+...+2+1=v_0+\frac{k(k+1)}{2}$$

we know that 
$$u_0 = 2^0 v_0 =T(2^0) = T(1) = 1$$

Therefore,
$$v_k = 1+\frac{k^2+k}{2}=\frac{k^2+k+2}{2}$$

That is,
$$T(n)=T(2^k)=u_k=2^kv_k=2^{k-1}(k^2+k+2)=\frac{n((\lg n)^2+\lg n+2)}{2}$$

Therefore, the solution to the recurrence $T(n)=T(n-1)+n$ is $\Theta(n\lg^2(n))$