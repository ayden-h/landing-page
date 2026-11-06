# imo_2013_f9ba1b

IMO-SL | IMO | 2013 | Combinatorics | C4

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2013_f9ba1b](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_f9ba1b.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems with Solutions
- Year: 2013
- Editors: Ardila, Federico; Bogdanov, Ilya I.; Kós, Géza; Moreira, Carlos Gustavo Tamm de Araújo; Reiher, Christian
- Organization: International Mathematical Olympiad
- Place: Santa Marta, Colombia
- Series: International Mathematical Olympiad
- Volume: 54th
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 2

Assume, to the contrary, that the statement is false, and choose the minimum number $n$ for which it fails. So there exists a set $A \subseteq\{1, \ldots, n\}$ together with an optimal $A$ partition $n=a_{1}+\cdots+a_{k_{\text{min}}}$ of $n$ refuting our statement, where, of course, $k_{\text{min}}$ is the minimum number of parts in an $A$-partition of $n$. Again, we define $S=\left\{a_{1}, \ldots, a_{k_{\text{min}}}\right\}=\left\{b_{1}, \ldots, b_{s}\right\}$ with $b_{1}<\cdots<b_{s}$; by our assumption we have $s>\sqrt[3]{6 n}>1$. Without loss of generality we assume that $a_{k_{\min}}=b_{s}$. Let us distinguish two cases.

Case 1. $b_{s} \geqslant \frac{s(s-1)}{2}+1$.
Consider the partition $n-b_{s}=a_{1}+\cdots+a_{k_{\text{min}}-1}$, which is clearly a minimum $A$-partition of $n-b_{s}$ with at least $s-1 \geqslant 1$ different parts. Now, from $n<\frac{s^{3}}{6}$ we obtain
$$
n-b_{s} \leqslant n-\frac{s(s-1)}{2}-1<\frac{s^{3}}{6}-\frac{s(s-1)}{2}-1<\frac{(s-1)^{3}}{6}
$$
so $s-1>\sqrt[3]{6\left(n-b_{s}\right)}$, which contradicts the choice of $n$.

Case 2. $b_{s} \leqslant \frac{s(s-1)}{2}$.
Set $b_{0}=0, \Sigma_{0,0}=0$, and $\Sigma_{i, j}=b_{1}+\cdots+b_{i-1}+b_{j}$ for $1 \leqslant i \leqslant j<s$. There are $\frac{s(s-1)}{2}+1>b_{s}$ such sums; so at least two of them, say $\Sigma_{i, j}$ and $\Sigma_{i^{\prime}, j^{\prime}}$, are congruent modulo $b_{s}$ (where $(i, j) \neq\left(i^{\prime}, j^{\prime}\right)$ ). This means that $\Sigma_{i, j}-\Sigma_{i^{\prime}, j^{\prime}}=r b_{s}$ for some integer $r$. Notice that for $i \leqslant j<k<s$ we have
$$
0<\Sigma_{i, k}-\Sigma_{i, j}=b_{k}-b_{j}<b_{s},
$$
so the indices $i$ and $i^{\prime}$ are distinct, and we may assume that $i>i^{\prime}$. Next, we observe that $\Sigma_{i, j}-\Sigma_{i^{\prime}, j^{\prime}}=\left(b_{i^{\prime}}-b_{j^{\prime}}\right)+b_{j}+b_{i^{\prime}+1}+\cdots+b_{i-1}$ and $b_{i^{\prime}} \leqslant b_{j^{\prime}}$ imply
$$
-b_{s}<-b_{j^{\prime}}<\Sigma_{i, j}-\Sigma_{i^{\prime}, j^{\prime}}<\left(i-i^{\prime}\right) b_{s}
$$
so $0 \leqslant r \leqslant i-i^{\prime}-1$.
Thus, we may remove the $i$ terms of $\Sigma_{i, j}$ in our $A$-partition, and replace them by the $i^{\prime}$ terms of $\Sigma_{i^{\prime}, j^{\prime}}$ and $r$ terms equal to $b_{s}$, for a total of $r+i^{\prime}<i$ terms. The result is an $A$-partition of $n$ into a smaller number of parts, a contradiction.

1 additional supplied solution(s) require external figures; use the source link.
