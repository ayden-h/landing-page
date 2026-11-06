# egm_2020_d0be5e

EGMO | European Girls' Mathematical Olympiad (EGMO) | 2020 |  | Problem 4

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [egm_2020_d0be5e](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2020_d0be5e.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: European Girls' Mathematical Olympiad (EGMO)

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $\sigma = (\sigma_{1}, \ldots, \sigma_{n-1})$ be a fresh permutation of the integers $1,2, \ldots, n-1$. We claim that for any $1 \leq i \leq n-1$ the permutation
$$
\sigma^{(i)} = (\sigma_{1}, \ldots, \sigma_{i-1}, n, \sigma_{i}, \ldots, \sigma_{n-1})
$$
is a fresh permutation of the integers $1,2, \ldots, n$. Indeed, let $1 \leq k \leq n-1$. If $k \geq i$ then we have $n \in \{\sigma_{1}^{(i)}, \ldots, \sigma_{k}^{(i)}\}$, but $n \notin \{1,2, \ldots, k\}$. And if $k < i$ we have $k < n-1$, and $\{\sigma_{1}^{(i)}, \ldots, \sigma_{k}^{(i)}\} = \{\sigma_{1}, \ldots, \sigma_{k}\} \neq \{1,2, \ldots, k\}$, since $\sigma$ is fresh. Moreover, it is easy to see that when we apply this construction to all fresh permutations of $1,2, \ldots, n-1$, we obtain $(n-1) \cdot f_{n-1}$ distinct fresh permutations of $1,2, \ldots, n$.

Note that a fresh permutation of $1,2, \ldots, n-1$ cannot end in $n-1$, and hence none of the previously constructed fresh permutations of $1,2, \ldots, n$ will end in $n-1$ either. Therefore, we will complete the proof by finding $f_{n-1}$ fresh permutations of $1,2, \ldots, n$ that end in $n-1$. To do this, let $\sigma = (\sigma_{1}, \ldots, \sigma_{n-1})$ be a fresh permutation of $1,2, \ldots, n-1$ and let $j$ be such that $\sigma_{j} = n-1$. Define
$$
\sigma' = (\sigma_{1}, \ldots, \sigma_{j-1}, n, \sigma_{j+1}, \ldots, \sigma_{n-1}, n-1)
$$
then clearly $\sigma'$ is a permutation of $1,2, \ldots, n$ that ends in $n-1$. We show that $\sigma'$ is fresh, so let $1 \leq k \leq n-1$. If $k \geq j$ then $n \in \{\sigma_{1}', \ldots, \sigma_{k}'\}$ but $n \notin \{1,2, \ldots, k\}$; if $k < j$, then $k < n-1$ and $\{\sigma_{1}', \ldots, \sigma_{k}'\} = \{\sigma_{1}, \ldots, \sigma_{k}\} \neq \{1,2, \ldots, k\}$, since $\sigma$ is fresh. So we have constructed $f_{n-1}$ additional fresh permutations of $1,2, \ldots, n$ (which again are all different), and the total number $f_{n}$ of fresh permutations of $1,2, \ldots, n$ must at least be $(n-1) f_{n-1} + f_{n-1} = n f_{n-1}$, as required.

Comment. A similar way to construct $n$ fresh permutations of $1,2, \ldots, n$ for each fresh permutation $\sigma$ of $1,2, \ldots, n-1$ is as follows: increase all entries of $\sigma$ by 1, and then add the number 1 anywhere; all these permutations are fresh, except the ones where 1 is added at the front, which can be made fresh by swapping the 1 and the 2. It is again straightforward to check that we obtain $n f_{n-1}$ permutations that are fresh and distinct, although a little extra care is needed to account for the fact that we increased the entries of our original permutation.

## Supplied solution 2

Assuming $n \geq 3$, we construct $f_{n-1} \cdot n$ different fresh permutations.

Consider a fresh permutation of the $n-1$ numbers $1,3,4, \ldots, n$ (the number 2 has been removed), by which we mean a permutation $(x_{1}, \ldots, x_{n-1})$ such that $x_{1} \neq 1$ and $\{x_{1}, \ldots, x_{k}\} \neq \{1,3, \ldots, k+1\}$ for all $k$ with $2 \leq k \leq n-2$. There are exactly $f_{n-1}$ such permutations.

By inserting 2 anywhere in such a permutation, i.e. before or after all entries, or between two entries $x_{i}, x_{i+1}$, we generate the following list of $n$ distinct permutations of $1,2, \ldots, n$, which we claim are all fresh:
$$
(2, x_{1}, \ldots, x_{n-1}), \quad \ldots, \quad (x_{1}, \ldots, x_{i-1}, 2, x_{i}, \ldots, x_{n-1}), \quad \ldots, \quad (x_{1}, \ldots, x_{n-1}, 2)
$$
In order to verify freshness, suppose that some permutation above is not fresh, that is, for some $1 \leq k \leq n-1$, the first $k$ elements are $1, \ldots, k$. If $k=1$ then the first element is 1; but the first element is either 2 or $x_{1}$ and $x_{1} \neq 2$, so this is not possible. If $k \geq 2$ then the first $k$ elements must contain 2 and $x_{1}, \ldots, x_{k-1}$, so $\{x_{1}, \ldots, x_{k-1}\} = \{1,3, \ldots, k\}$, in contradiction to the fact that $(x_{1}, \ldots, x_{n-1})$ is fresh.

We have thus constructed $f_{n-1} \cdot n$ different fresh permutations, so $f_{n} \geq f_{n-1} \cdot n$.

Comment. Note that the construction from solution B can also be performed by placing $n-1$ instead of 2, or indeed any $k$ between 2 and $n-1$ (in which case it will work for $n \geq k+1$).

Moreover, similar arguments can be made while choosing to work with non-fresh permutations rather than fresh permutations. Indeed, in order to show that $n! - f_{n} \leq n((n-1)! - f_{n-1})$ for all $n \geq 3$, which is equivalent to the problem statement, one can argue as follows. Given a non-fresh permutation $(\sigma_{1}, \ldots, \sigma_{n})$ of $1,2, \ldots, n$, erasing $n-1$ from it and changing $n$ to $n-1$ yields a permutation which cannot be fresh. Moreover, each non-fresh permutation of $1,2, \ldots, n-1$ can be obtained in this way from at most $n$ different non-fresh permutations of $1,2, \ldots, n$. This type of argument would essentially mirror the one carried out in Solution B.

## Supplied solution 3

By considering all permutations of $1,2, \ldots, n$ and considering the smallest $k$ for which the first $k$ numbers are $1,2, \ldots, k$ in some order, one can deduce the recursion
$$
\sum_{k=1}^{n} (n-k)! \cdot f_{k} = n!
$$
which holds for any $n \geq 1$.

Therefore, if $n \geq 3$ we have
$$
\begin{aligned}
0 &= n! - (n+1)(n-1)! + (n-1)(n-2)! \\
&= \sum_{k=1}^{n} (n-k)! \cdot f_{k} - (n+1) \sum_{k=1}^{n-1} (n-1-k)! \cdot f_{k} + (n-1) \sum_{k=1}^{n-2} (n-2-k)! \cdot f_{k} \\
&= f_{n} - n f_{n-1} + \sum_{k=1}^{n-2} (n-2-k)! \cdot ((n-k)(n-k-1) - (n+1)(n-k-1) + (n-1)) \cdot f_{k} \\
&= f_{n} - n f_{n-1} + \sum_{k=1}^{n-2} (n-2-k)! \cdot k(k+2-n) \cdot f_{k} \leq f_{n} - n f_{n-1}
\end{aligned}
$$
which rewrites as $f_{n} \geq n f_{n-1}$.

## Supplied solution 4

We first show that for any $n \geq 2$ we have
$$
f_{n} = \sum_{k=1}^{n-1} k (n-1-k)! \cdot f_{k}
$$
To deduce this relation, we imagine obtaining permutations of $1,2, \ldots, n$ by inserting $n$ into a permutation of the numbers $1,2, \ldots, n-1$. Specifically, let $(\sigma_{1}, \ldots, \sigma_{n-1})$ be any permutation of $1,2, \ldots, n-1$, and let $1 \leq k \leq n-1$ be minimal with $\{\sigma_{1}, \ldots, \sigma_{k}\} = \{1,2, \ldots, k\}$. Note that there are $(n-1-k)! \cdot f_{k}$ such permutations. Furthermore, inserting $n$ in this permutation will give a fresh permutation if and only if $n$ is inserted before $\sigma_{k}$, so there are $k$ options to do so. Consequently, if $n \geq 3$,
$$
\begin{aligned}
f_{n} &= \sum_{k=1}^{n-1} k (n-1-k)! \cdot f_{k} \\
&= (n-1) \cdot f_{n-1} + \sum_{k=1}^{n-2} k (n-1-k)! \cdot f_{k} \\
&\geq (n-1) \cdot f_{n-1} + \sum_{k=1}^{n-2} k (n-2-k)! \cdot f_{k} \\
&= (n-1) \cdot f_{n-1} + f_{n-1} = n \cdot f_{n-1}
\end{aligned}
$$
completing the proof.

