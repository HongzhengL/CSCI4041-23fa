#### Discussion Section 012

<h1 style="text-align: center;">CSCI4041 Homework 3</h1>

<h4 style="text-align: center;">Hongzheng Li</h4>

## Problem 1:

From the textbook, we know that for each slice of $k$ elements, there are $k!$ ways to arrange the elements within that slice.
Since there are $\frac{n}{k}$ such slices, and the arrangements within each slice are independent, the total number of permutations is:
$$(k!)^{\frac{n}{k}}$$

Let $h$ denotes the height of the decision tree, where $h \in N$. 

Since the decision tree is a binary tree and a binary tree of height $h$ has no more than $2^h$ leaves.
We know that the number of reachable leaves equals to the number of permutations of the sequence, we have

$$(k!)^{\frac{n}{k}} \leq 2^h$$

take logarithm on both side, we have
$$h \geq \frac{n}{k}\lg(k!)$$
where
$$h \in N$$

Therefore, the minimum height of a decision tree with this number of leaves is $\lceil\frac{n}{k}\lg(k!)\rceil$

We know that $\lg n! = \Theta(n\lg n)$, so, we can have
$\lg (k!) = \Theta(k\lg k)$,
using the property of Big $\Theta$, we have
$$\lg (k!) \geq c\cdot k\lg k$$
for sufficiently large $k$ and some constant $c$.

Divide both sides by $k$ and multiply both sides by $n$, we have
$$\frac{n}{k}\lg (k!) \geq c\cdot n\lg k$$
for sufficiently large $k$ and some constant $c$.

That gives
$\frac{n}{k}\lg (k!) = \Omega(n\lg k)$.

From the textbook, we know that the length of the longest simple path from the root of a decision tree to any of its reachable leaves represents the worst-case number of comparisons that the corresponding sorting algorithm performs. And in this case, the minimum height of the decision tree is $ h = \lceil\frac{n}{k}\lg(k!)\rceil$. Therefore, the lower bound of the number of comparisons is
$$\Omega(n\lg k)$$

---

## Problem 2:

First, let's be clear with a fact:

- There're $n+1$ ways to put an element in a sequence of $n$ elements

Using the above fact, we know that to put 2 distinct elements, say $p$, $q$, in a sequence of $n$ elements, there're $(n+1)(n+2)$ ways to do so. 

And, there're two kinds of arrangement of $p$, $q$
-- either $p$ is behind $q$ or $q$ is behind $p$. And they are equal likely. Therefore, to put 2 sorted elements in a sequence of n elements, there're $\frac{(n+1)(n+2)}{2}$ ways.

Therefore,

For 1 pair, 
there're $\frac{(0+1)(0+2)}{2}$ permutations

For 2 pairs, 
there're $\frac{(0+1)(0+2)}{2} \times \frac{(2+1)(2+2)}{2}$ permutations

For 3 pairs, 
there're $\frac{(0+1)(0+2)}{2} \times \frac{(2+1)(2+2)}{2} \times \frac{(4+1)(4+2)}{2}$ permutations

...

For $\frac{n}{2}$ pairs, 
there're $\frac{(0+1)(0+2)}{2} \times \frac{(2+1)(2+2)}{2} \times \frac{(4+1)(4+2)}{2}\times ... \times\frac{((n-2)+1)((n-2)+2)}{2}$ permutations

Therefore, the total number of permutations is

$$\begin{align*}
&\frac{(0+1)(0+2)}{2} \times \frac{(2+1)(2+2)}{2} \times \frac{(4+1)(4+2)}{2}\times \dots \times\frac{((n-2)+1)((n-2)+2)}{2} \\
&=\frac{1\times 2}{2}\times\frac{3\times 4}{2}\times\frac{5\times 6}{2}\times \dots \times\frac{(n-1)\times n}{2} \\
&=\frac{1\times 2\times 3\times 4\times 5\times 6\times \dots \times(n-1)\times n}{2\times 2\times 2\times \dots \times 2} \\
&=\frac{n!}{2^{\frac{n}{2}}}
\end{align*}$$

Let $h$ denotes the height of the decision tree, using what we got from Problem 1, we have
$$\frac{n!}{2^{\frac{n}{2}}}\leq 2^h$$

take logarithm on both side, we have
$$h\geq \lg n! - \frac{n}{2}$$
where $$h\in N$$
Therefore, the minimum height of a decision tree with this number of leaves is 
$\lceil\lg n! - \frac{n}{2}\rceil$

Since 
$\lg n! = \Theta(n \lg n)$
and 
$\frac{n}{2} = \Theta(n)$,
$\lg n!$ dominates the equation as $n$ grows bigger.

So, using the same method as Problem 1, we know that the lower bound of the number of comparisons is
$$\Omega(n\lg n)$$

---

## Problem 3:

The critical operation in QuickSort is choosing a pivot such that the array is approximately split in half each time. If we can guarantee that the pivot always divides the array into two nearly equal-sized subarrays, then QuickSort will have a time complexity of $\Theta(n\lg n)$. To achieve this, we can use the selection algorithm to find the median of the array in $\Theta(n)$ time.

After the modification, the process of QuickSort is:

- Use the selection algorithm to find the median of the array in $\Theta(n)$ time.
- Use this median as the pivot.
- Partition the array around the pivot in $\Theta(n)$ time.
- Recursively sort the two subarrays.

Therefore, the recurrence for this version of QuickSort is:
$$T(n)=\Theta(n)+\Theta(n)+2T(\frac{n}{2})=2T(\frac{n}{2})+\Theta(n)$$

This is the same recurrence as that of MergeSort, whose worst case sorting time is $\Theta(n\lg n)$. 
Then, we have successfully make QuickSort to run in $\Theta(n\lg n)$ time in the worst case.

---

## Problem 4:

The basic idea is to manipulate the position of the desired 
$k^{th}$ smallest element by adding either big enough value $+ \infty$ or small enough value $- \infty$, so that after the additions, the $k^{th}$ smallest element becomes the median.

```Python
FIND-ELEMENT(k, array, n)
    if k = (n/2)
       return Median(array) #Call library function
                            #to return the median of array
    else if k > (n/2)
        for i = 1 to 2k - n
            array.append(+∞) #+∞ means great enough number
    else
        for i = 1 to 2k - n
            array.append(-∞) #-∞ means small enough number

    return Median(array)
```

---

## Problem 5:

```Python
FIND-SET(x)
    root = x
    while root != p[root]
        root = p[root]

    while x != p[x]
        temp = p[x]
        p[x] = root
        x = temp

    return root
```

First, we begin by using a while loop to check if the representative of a node is itself.
Once the loop is over, we find the representative of the set to which the element $x$ belongs, denotes as $root$.

We begin path compression by using the second loop to update the parent of $x$ to point directly to the $root$.
Then, We move $x$ one level up the tree to its original parent before compression. On the next iteration of the loop, this parent's pointer will also be updated to the root, and so on, until we reach the root.

After the path compression is done, the root of the set containing $x$ is returned.

---

## Problem 6:

- First, we perform $n$ MAKESET operation. 

    Since each of the make-set operation takes $O(1)$ time,
    the whole operation takes $O(n)$ time.

- Next, we perform $(n-1)$ UNION operation.

    Here, we will build a set of rank $\lg n$.

    1. Start with n single-node set, each of rank 0.
    2. Merge sets in pairs. After the first set of unions, we'll have $\frac{n}{2}$ sets of rank 1.
    3. Merge sets in pairs again. This time we'll have $\frac{n}{2}$ sets of rank 2.
    4. Repeat the above process until we get only $1$ set.

    We know that the each of the union operation takes $O(1)$ time. 
    Therefore, the whole process will take
    $(\frac{n}{2} + \frac{n}{4} + ... + 2 + 1)O(1)$ time.
    Let $2^{k}$ be the nearest number around n, then
    $\frac{n}{2} + \frac{n}{4} + ... + 2 + 1\approx 2^{k-1}+2^{k-2}+...+2+1=2^k-1=n-1$

    Since every time $k$ increases by 1, rank increases by 1. Therefore, the set is approximately of rank $k=\lg n$. 

    Then, we get a set of rank $\lg n$ in $O(n)$ time.


- Finally, we perform $(m-2n+1)$ FINDSET operation.

    From the second process we know that the set is of rank $\lg n$. If we go from the deepest node to root without path compression, it takes 
    $\Omega(\lg n)$ time. 
    Therefore, we will perform $(m-2n+1)$ FINDSET operation from the deepest node (since we have perform (2n-1) operations above), 
    which will take $\Omega((m-2n+1)\lg n)$ .

In summary, since the term $n\lg n$ grows faster than 
$n$ as $n$ grows larger, given that $m$ is big enough, 
it follows that the whole process takes $\Omega(m\lg n)$ time, as desired.





<!-- n - makeset\
(n-1) - union\
m-(2n-1) - findset -->
<!-- $$\frac{(0+1)(0+2)}{2} \times \frac{(2+1)(2+2)}{2} \times \frac{(4+1)(4+2)}{2}\times ... \times\frac{((n-2)+1)((n-2)+2)}{2}$$

$$=\frac{1\times 2}{2}\times\frac{3\times 4}{2}\times\frac{5\times 6}{2}\times ...\times\frac{(n-1)\times n}{2}$$

$$=\frac{1\times 2\times 3\times 4\times 5\times 6\times ...\times(n-1)\times n}{2\times 2\times 2\times ...\times 2}$$

$$=\frac{n!}{2^{\frac{n}{2}}}$$ -->
 <!-- a b c d

 a d b
 d a b


6
5+4+3+2+1

1 pair: 1\
2 pair: 1 x (3+2+1)\
3 pair: 1 x (3+2+1) x (5+4+3+2+1)\
...\
n/2 pair: 1 x (3x4/2) x (5x6/2) x ... x (n(n+1)/2) -->