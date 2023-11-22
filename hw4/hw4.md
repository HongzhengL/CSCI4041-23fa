#### Discussion Section 012

<h1 style="text-align: center;">CSCI4041 Homework 4</h1>

<h4 style="text-align: center;">Hongzheng Li</h4>

## Problem 1:

```python
MULTIPLYCHAIN(i, j, s, A)
    if i == j
        return A[i]
    else
        X = MULTIPLYCHAIN(i, s[i, j], s, A)
        Y = MULTIPLYCHAIN(s[i, j] + 1, j, s, A)
        return MatrixMultiply(X, Y)
```


## Problem 2:

> There're (n-1) pairs of parentheses in a full parenthesization of the product of n matrices

Proof are as following:

**Base case:**

If n = 1, no multiplication is needed, so no parentheses are required.


If n = 2, For two matrices $A_1$ and $A_2$, one matrix multiplication is needed, 
and therefore one pair of parentheses is required.

**Induction:**

Assume that for some $k\in N^+$, 
$(k-2)$ pairs of parentheses are needed for a full parenthesization 
for a product of $(k-1)$ matrices $A_1, A_2,...,A_{k-1}$. 

Now consider the product of $k$ matrices $A_1, A_2,...,A_{k-1},A_{k}$. 
We can group the first $(k-1)$ matrices together and multiply them by the $k^{th}$ matrix: $((A_1, A_2,...,A_{k-1})A_{k})$. 

By the inductive hypothesis, the product of $A_1, A_2,...,A_{k-1}$ requires $(k-2)$ pairs of parentheses. 

Thus, the product of $k$ matrices requires $(k-2)+1=k-1$ pairs of parentheses in total, which completes the inductive step.

Therefore, by induction, a full parenthesization of the product of $n$ matrices requires $(n−1)$ pairs of parentheses.

## Problem 3:

|      n       |       P(n)     |     $2^n$     |
|:-------------|:--------------:|--------------:|
|      1       |        1       |       2       |
|      2       |        1       |       4       |
|      3       |        2       |       8       |
|      4       |        5       |      16       |
|      5       |       14       |      32       |
|      6       |       42       |      64       |

Let's begin our proof by proving $P(n)\geq P(n-1)$.

We want to prove that $P(n) \geq P(n-1)$
for positive integers $n\geq2$, 
where $P(n)$ is defined as

$$P(n) = \sum_{k=1}^{n-1} P(k)P(n-k)$$ 
and $P(1) = 1$.

Using the definition of $P(n)$, we can express $P(n)$ and $P(n-1)$ as follows:

$$\begin{aligned}
P(n) 
&= \sum_{k=1}^{n-1} P(k)P(n-k)\\
&=\sum_{k=1}^{n-2} P(k)P(n-k)+P(n-1)P(1)\\
&=\sum_{k=1}^{n-2} P(k)P(n-k)+P(n-1)
\end{aligned}$$

That gives us $$P(n)-P(n-1)=\sum_{k=1}^{n-2} P(k)P(n-k)$$

Since $P(n)$ is the number of possible parenthesizations of a sequence n elements, 
$P(n)$ will be positive. 
And we can easily reason about that by looking at the definition of $P(n)$, 
which is a recursively summing and multiplying $P(1)$ 
and $P(2)$, which is also positive number.

Summation of positive number always gives positive result. Therefore, we can conclude that

$$\sum_{k=1}^{n-2} P(k)P(n-k)\geq 0$$

which will give us

$$P(n)-P(n-1)\geq0$$

that is

$$P(n)\geq P(n-1)$$

This completes the proof.

---

Then, we start to prove $P(n)\geq\frac{1}{4}2^n$.

<!-- Assume that for $i < n$, we have $P(i)\geq \frac{1}{4}2^i$

Then, we have
$$\begin{aligned}
P(n) &= \sum_{k=1}^{n-1}P(k)P(n-k)\\
&\geq\sum_{k=1}^{n-1}\frac{1}{4}2^k\cdot\frac{1}{4}2^{n-k}\\
&=\frac{1}{16}\sum_{k=1}^{n-1}2^n\\
&=\frac{n-1}{16}2^n
\end{aligned}$$ 

--- -->

<!-- Let's first prove $P(n) \geq P(n-1)$.

We know that $P(n)=\sum_{k=1}^{n-1}P(k)P(n-k)$ and $P(1)=1$.

Therefore, we can have
$$\begin{aligned}

P(n)&=\sum_{k=1}^{n-2}P(k)P(n-k)+P(n-1)P(1)\\
&=\sum_{k=1}^{n-2}P(k)P(n-k)+P(n-1)

\end{aligned}$$

Since all terms in $\sum_{k=1}^{n-2}P(k)P(n-k)$ 
can be obtained from knowing only the value of $P(1),P(2)$,
which are both larger than 0,
since they're summation of positive value, they are larger than $0$,
then we have
$$P(n)=\sum_{k=1}^{n-2}P(k)P(n-k)+P(n-1)\geq P(n-1)$$

That is to say, for $n\in N^+$, we have 
$$P(n)\geq P(n-1)$$ -->
**Base Case:**

When $n = 1$,
$$P(1)=1\geq\frac{1}{4}\times 2=\frac{1}{2}$$

When $n = 2$, 
$$P(2)=P(1)\cdot P(1)=1\geq \frac{1}{4}2^1=\frac{1}{2}$$

**Induction steps:**

When $n\geq 3$, assume that for some $n-1$ where $n\in N^+$, the equation is true
and that gives us $P(n-1) \geq\frac{1}{4}2^{n-1}$

Then, we will prove $P(n) \geq\frac{1}{4}2^{n}$ 
by using $P(i)\geq P(i-1)$ 
for positive integer $i\geq2$.

$$\begin{aligned}
P(n)&= P(1)P(n-1)+P(2)P(n-2)+...+P(n-2)P(2)+P(n-1)P(1)\\
&\geq[P(1)P((n-1)-1)+P(2)P((n-1)-2)+...+P(n-2)P(2-1)]+P(n-1)P(1)\\
&=[P(1)P(n-2)+P(2)P(n-3)+...+P(n-2)P(1)]+P(n-1)P(1)\\
&=P(n-1)+P(n-1)P(1)\\
&=P(n-1)+P(n-1)\times1\\
&=2P(n-1)\\
&\geq 2\times\frac{1}{4}2^{n-1}\\
&=\frac{1}{4}2^n
\end{aligned}$$

Then, combine the base case and induction steps together, we have proved $P(n)\geq\frac{1}{4}2^n$ for $n\in N^+$ by induction.

---

Notice that in the induction step, we have prove
$$P(n)\geq 2P(n-1)$$
when $n\geq 3$.

However, observed from the table, this is not true when $n=1,2$.

Therefore, when $n\geq3$, we can write it as
$$\frac{P(n)}{P(n-1)}\geq2$$

Then, we can write $P(n)$ as:
$$P(n)=\frac{P(n)}{P(n-1)}\cdot\frac{P(n-1)}{P(n-2)}\cdot\cdot\frac{P(3)}{P(2)}\cdot\frac{P(2)}{P(1)}\cdot P(1)\geq2\cdot2\cdot\cdot2\cdot1\cdot1=2^{n-2}=\frac{1}{4}2^n$$

Therefore, using the table and what we have proved,
we can conclude that 
the $\frac{1}{4}$ factor is essentially introduced 
due to the **base case** where the growth of $P(n)$ 
is slower than the exponential growth of $2^n$, namely, when $n=1,2$.

---

## Problem 4:

We start by creating a copy of S in S'. 

Then, we use merge sort to sort the copied sequence S', 
arranging its elements in non-decreasing order.

By finding the Longest Common Subsequence (LCS) 
between the original sequence S and the sorted sequence S', 
we identify the longest subsequence in S 
that is also in non-decreasing order (since S' is sorted). 
This is the Longest Monotonically Increasing Subsequence of S.

The runtime of merge sort on $n$ elements is $O(n\lg n)$.\
The runtime of LCS(S, S') is $\Theta(n^2)$, 
according to the problem description.\
Therefore, the total runtime of the algorithm is $\Theta(n^2+n\lg n)=\Theta(n^2)$,
which satisfies the requirement.

Pseudocode is as following:

```pseudocode
LMIS(S)
   Let S' be a copy of S
   MergeSort(S')
   return LCS(S, S')
```