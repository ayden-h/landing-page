# usa_87d02d

IMO-TST | United States | year unknown | January TST | Problem 2

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [usa_87d02d](https://mathnet.mit.edu/data_v2/full/united-states/usa_87d02d.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: United States
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $f(n)$ be the answer to the problem. We claim that $f(n) = \lceil \log n \rceil$ for all $n \ge 1$. The proof is divided into showing that this quantity is both an upper and a lower bound.

**Lower Bound.** We show that every tournament on $n$ vertices has directed-edge-chromatic number at least $\lceil \log n \rceil$. We prove this by strong induction on $n$. As our base case, if $n = 1$, then clearly $f(1) \ge 0 = \lceil \log 1 \rceil$. Now, for $n \ge 2$, assume by the strong inductive hypothesis that $f(k) \ge \lceil \log k \rceil$ for all $k < n$. Consider any proper directed-edge-coloring of an $n$-vertex directed graph (vertex set $V$) with $f(n) \ge 1$ colors. Pick an arbitrary color, and let $U_1$ be the set of vertices $u$ for which there exists an edge $\vec{uv}$ of that color, and let $U_2$ be the set of vertices $u$ for which there exists an edge of the form $\vec{vu}$. Clearly since the coloring is proper $U_1 \cap U_2 = \emptyset$. Thus, there exists $i \in \{1, 2\}$ such that $U_i$ has size at most $n/2$. Notice that $V \setminus U_i$ has size at least $n/2$ and also has no edges of the originally chosen color. Thus, the graph induced by $V \setminus U_i$ has a proper directed-edge-coloring of $f(n)-1$ colors. By the inductive hypothesis, this implies that
$$
f(n) - 1 \ge f(|V \setminus U_i|) \ge \lceil \log |V \setminus U_i| \rceil \ge \lceil \log(n/2) \rceil = \lceil \log n \rceil - 1.
$$
Therefore, $f(n) \ge \lceil \log n \rceil$.

**Upper Bound.** We exhibit a proper directed-edge-coloring with $\lceil \log n \rceil$ colors of a tournament with $n$ vertices. Consider the tournament with vertices $0, \dots, n-1$ such that there is a directed edge from $i$ to $j$ if and only if $i > j$. Label our colors $0, \dots, \lceil \log n \rceil - 1$. Color the edge $\vec{ij}$ the largest $k$ such that $i$ has a $1$ and $j$ has a $0$ in the $2^k$th place of their binary representations. Such a $k$ always exists and is at most $\lceil \log n \rceil - 1$ because $i > j$ and $n-1$ requires at most $\lceil \log n \rceil$ digits in its binary representation. Assume for sake of contradiction that this is not a proper directed-edge-coloring. Then, there would exist edge $\overrightarrow{ij}$ and $\overrightarrow{jk}$ of color $l$. Thus, $j$ would have both $0$ and $1$ in the $2^l$th place of its binary representation, contradiction. Hence, this exhibited coloring is proper so $f(n) \le \lceil \log n \rceil$.

Thus, the minimal directed-edge-chromatic number among tournaments on $n$ vertices is $\lceil \log n \rceil$.

