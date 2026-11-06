# imo_2006_a3af5a

IMO-SL | IMO | 2006 | Combinatorics | C4

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2006_a3af5a](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_a3af5a.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems with Solutions
- Year: 2006
- Editors: Bauer, Andrej; Geretschläger, Robert; Kós, Géza; Kuczma, Marcin; Savchev, Svetoslav
- Organization: International Mathematical Olympiad
- Place: Slovenia
- Series: International Mathematical Olympiad
- Volume: 47
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We use capital letters to denote unit squares; $O$ is the top left corner square. For any two squares $X$ and $Y$ let $[X Y]$ be the smallest grid rectangle containing these two squares. Strawberries lie on some squares in arrangement $\mathcal{A}$. Put a plum on each square of the target configuration $\mathcal{B}$. For a square $X$ denote by $a(X)$ and $b(X)$ respectively the number of strawberries and the number of plums in $[O X]$. By hypothesis $a(X) \leq b(X)$ for each $X$, with strict inequality for some $X$ (otherwise the two arrangements coincide and there is nothing to prove).
The idea is to show that by a legitimate switch one can obtain an arrangement $\mathcal{A}'$ such that
$$
\begin{equation*}
a(X) \leq a'(X) \leq b(X) \quad \text{ for each } X ; \quad \sum_{X} a(X)<\sum_{X} a'(X) \tag{1}
\end{equation*}
$$
(with $a'(X)$ defined analogously to $a(X)$; the sums range over all unit squares $X$ ). This will be enough because the same reasoning then applies to $\mathcal{A}'$, giving rise to a new arrangement $\mathcal{A}''$, and so on (induction). Since $\sum a(X)<\sum a'(X)<\sum a''(X)<\ldots$ and all these sums do not exceed $\sum b(X)$, we eventually obtain a sum with all summands equal to the respective $b(X)$s; all strawberries will meet with plums.
Consider the uppermost row in which the plum and the strawberry lie on different squares $P$ and $S$ (respectively); clearly $P$ must be situated left to $S$. In the column passing through $P$, let $T$ be the top square and $B$ the bottom square. The strawberry in that column lies below the plum (because there is no plum in that column above $P$, and the positions of strawberries and plums coincide everywhere above the row of $P$ ). Hence there is at least one strawberry in the region $[B S]$ below $[P S]$. Let $V$ be the position of the uppermost strawberry in that region.

| $O$ |  | $T$ |  |  |  |  | I |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  |  |  |  | I |  |  |  |  |  |
|  |  | $P$ |  |  | $U$ |  | 1 |  |  | $S$ |  |  |
|  |  |  |  |  |  |  | 1 | 1 |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | 1 |  |  |  |  |  |
| - | - | - | - | - | - | - - | $\underline{X}'$ |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | $R$ |  |  |  |
|  |  |  |  |  | $V$ |  |  |  |  | $W$ |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | $B$ |  |  |  |  |  |  |  |  |  |  |

Denote by $W$ the square at the intersection of the row through $V$ with the column through $S$ and let $R$ be the square vertex-adjacent to $W$ up-left. We claim that
$$
\begin{equation*}
a(X)<b(X) \quad \text{ for all } \quad X \in[P R] . \tag{2}
\end{equation*}
$$
This is so because if $X \in[P R]$ then the portion of $[O X]$ left to column $[T B]$ contains at least as many plums as strawberries (the hypothesis of the problem); in the portion above the row through $P$ and $S$ we have perfect balance; and in the remaining portion, i.e. rectangle $[P X]$ we have a plum on square $P$ and no strawberry at all.
Now we are able to perform the required switch. Let $U$ be the square at the intersection of the row through $P$ with the column through $V$ (some of $P, U, R$ can coincide). We move strawberries from squares $S$ and $V$ to squares $U$ and $W$. Then
$$
a'(X)=a(X)+1 \quad \text{ for } \quad X \in[U R] ; \quad a'(X)=a(X) \quad \text{ for other } X .
$$
And since the rectangle $[U R]$ is contained in $[P R]$, we still have $a'(X) \leq b(X)$ for all $S$, in view of (2); conditions (1) are satisfied and the proof is complete.

