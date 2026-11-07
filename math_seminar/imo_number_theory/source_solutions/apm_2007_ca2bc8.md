# apm_2007_ca2bc8

APMO | Asia Pacific Mathematics Olympiad (APMO) | 2007 |  | Problem 1

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [apm_2007_ca2bc8](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2007_ca2bc8.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Asia Pacific Mathematics Olympiad (APMO)
- Title: XIX Asian Pacific Mathematics Olympiad
- Year: 2007
- Organization: Asian Pacific Mathematics Olympiad
- Series: Asian Pacific Mathematics Olympiad
- Volume: XIX
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Without loss of generality, we may assume that $S$ contains only positive integers. Let
$$
S = \{2^{a_i} 3^{b_i} \mid a_i, b_i \in \mathbb{Z},\ a_i, b_i \geq 0,\ 1 \leq i \leq 9\}.
$$
It suffices to show that there are $1 \leq i_1, i_2, i_3 \leq 9$ such that
$$
\begin{equation*}
a_{i_1} + a_{i_2} + a_{i_3} \equiv b_{i_1} + b_{i_2} + b_{i_3} \equiv 0 \quad (\bmod\ 3). \tag{$\dagger$}
\end{equation*}
$$
For $n = 2^a 3^b \in S$, let's call $(a \bmod 3, b \bmod 3)$ the type of $n$. Then there are 9 possible types:
$$
(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2).
$$
Let $N(i, j)$ be the number of integers in $S$ of type $(i, j)$. We obtain 3 distinct integers whose product is a perfect cube when
(1) $N(i, j) \geq 3$ for some $i, j$, or
(2) $N(i, 0) N(i, 1) N(i, 2) \neq 0$ for some $i = 0, 1, 2$, or
(3) $N(0, j) N(1, j) N(2, j) \neq 0$ for some $j = 0, 1, 2$, or
(4) $N(i_1, j_1) N(i_2, j_2) N(i_3, j_3) \neq 0$, where $\{i_1, i_2, i_3\} = \{j_1, j_2, j_3\} = \{0, 1, 2\}$.
Assume that none of the conditions (1) $\sim$ (3) holds. Since $N(i, j) \leq 2$ for all $(i, j)$, there are at least five $N(i, j)$'s that are nonzero. Furthermore, among those nonzero $N(i, j)$'s, no three have the same $i$ nor the same $j$. Using these facts, one may easily conclude that the condition (4) should hold. (For example, if one places each nonzero $N(i, j)$ in the $(i, j)$-th box of a regular $3 \times 3$ array of boxes whose rows and columns are indexed by 0, 1 and 2, then one can always find three boxes, occupied by at least one nonzero $N(i, j)$, whose rows and columns are all distinct. This implies (4).)

## Supplied solution 2

Up to $(\dagger)$, we do the same as above and get 9 possible types:
$$
(a \bmod 3, b \bmod 3) = (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)
$$
for $n = 2^a 3^b \in S$.
Note that (i) among any 5 integers, there exist 3 whose sum is $0 \pmod{3}$, and that (ii) if $i, j, k \in \{0, 1, 2\}$, then $i + j + k \equiv 0 \pmod{3}$ if and only if $i = j = k$ or $\{i, j, k\} = \{0, 1, 2\}$.
Let's define
$T$: the set of types of the integers in $S$;
$N(i)$: the number of integers in $S$ of the type $(i, \cdot)$;
$M(i)$: the number of integers $j \in \{0, 1, 2\}$ such that $(i, j) \in T$.
If $N(i) \geq 5$ for some $i$, the result follows from (i). Otherwise, for some permutation $(i, j, k)$ of $(0, 1, 2)$,
$$
N(i) \geq 3, \quad N(j) \geq 3, \quad N(k) \geq 1.
$$
If $M(i)$ or $M(j)$ is 1 or 3, the result follows from (ii). Otherwise $M(i) = M(j) = 2$. Then either
$$
(i, x), (i, y), (j, x), (j, y) \in T \quad \text{or} \quad (i, x), (i, y), (j, x), (j, z) \in T
$$
for some permutation $(x, y, z)$ of $(0, 1, 2)$. Since $N(k) \geq 1$, at least one of $(k, x), (k, y)$ and $(k, z)$ is contained in $T$. Therefore, in any case, the result follows from (ii). (For example, if $(k, y) \in T$, then take $(i, y), (j, y), (k, y)$ or $(i, x), (j, z), (k, y)$ from $T$.)
