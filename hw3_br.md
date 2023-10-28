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