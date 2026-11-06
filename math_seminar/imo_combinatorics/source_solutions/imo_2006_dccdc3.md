# imo_2006_dccdc3

IMO-SL | IMO | 2006 | Combinatorics | C1

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2006_dccdc3](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_dccdc3.json.gz)

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

a.
Experiments with small $n$ lead to the guess that every $n$ of the form $2^{k}$ should be good. This is indeed the case, and more precisely: let $A_{k}$ be the $2^{k} \times 2^{k}$ matrix whose rows represent the evolution of the system, with entries $0,1$ (for off and on respectively). The top row shows the initial state $[1,0,0, \ldots, 0]$; the bottom row shows the state after $2^{k}-1$ steps. The claim is that:
$$
\text{The bottom row of } A_{k} \text{ is } [1,1,1, \ldots, 1] \text{.}
$$
This will of course suffice because one more move then produces $[0,0,0, \ldots, 0]$, as required.

The proof is by induction on $k$. The base $k=1$ is obvious. Assume the claim to be true for a $k \geq 1$ and write the matrix $A_{k+1}$ in the block form $\left(\begin{array}{cc}A_{k} & O_{k} \\ B_{k} & C_{k}\end{array}\right)$ with four $2^{k} \times 2^{k}$ matrices. After $m$ steps, the last $1$ in a row is at position $m+1$. Therefore $O_{k}$ is the zero matrix. According to the induction hypothesis, the bottom row of $[A_{k} \ O_{k}]$ is $[1, \ldots, 1,0, \ldots, 0]$, with $2^{k}$ ones and $2^{k}$ zeros. The next row is thus
$$
[\underbrace{0, \ldots, 0}_{2^{k}-1}, 1,1, \underbrace{0, \ldots, 0}_{2^{k}-1}]
$$
It is symmetric about its midpoint, and this symmetry is preserved in all subsequent rows because the procedure described in the problem statement is left/right symmetric. Thus $B_{k}$ is the mirror image of $C_{k}$. In particular, the rightmost column of $B_{k}$ is identical with the leftmost column of $C_{k}$.

Imagine the matrix $C_{k}$ in isolation from the rest of $A_{k+1}$. Suppose it is subject to evolution as defined in the problem: the first (leftmost) term in a row depends only on the two first terms in the preceding row, according as they are equal or not. Now embed $C_{k}$ again in $A_{k}$. The 'leftmost' terms in the rows of $C_{k}$ now have neighbours on their left side - but these neighbours are their exact copies. Consequently the actual evolution within $C_{k}$ is the same, whether or not $C_{k}$ is considered as a piece of $A_{k+1}$ or in isolation. And since the top row of $C_{k}$ is $[1,0, \ldots, 0]$, it follows that $C_{k}$ is identical with $A_{k}$.

The bottom row of $A_{k}$ is $[1,1, \ldots, 1]$; the same is the bottom row of $C_{k}$, hence also of $B_{k}$, which mirrors $C_{k}$. So the bottom row of $A_{k+1}$ consists of ones only and the induction is complete.

b.
There are many ways to produce an infinite sequence of those $n$ for which the state $[0,0, \ldots, 0]$ will never be achieved. As an example, consider $n=2^{k}+1$ (for $k \geq 1$). The evolution of the system can be represented by a matrix $\mathcal{A}$ of width $2^{k}+1$ with infinitely many rows. The top $2^{k}$ rows form the matrix $A_{k}$ discussed above, with one column of zeros attached at its right.

In the next row we then have the vector $[0,0, \ldots, 0,1,1]$. But this is just the second row of $\mathcal{A}$ reversed. Subsequent rows will be mirror copies of the foregoing ones, starting from the second one. So the configuration $[1,1,0, \ldots, 0,0]$, i.e. the second row of $\mathcal{A}$, will reappear. Further rows will periodically repeat this pattern and there will be no row of zeros.

