# chn_2022_aece1e

CMO-China | China | 2022 | Day One | 3

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [chn_2022_aece1e](https://mathnet.mit.edu/data_v2/full/china/chn_2022_aece1e.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: China
- Title: The 38th Chinese Mathematical Olympiad
- Year: 2022
- Place: Shenzhen, Guangdong
- Language: English

## Problem

Fix two positive integers $m$ and $n$. Fix a way to color the vertices of a regular $(2m+2n)$-gon so that $2m$ of them are black and the other $2n$ are white. Define the coloring distance $d(B, C)$ between two black points $B$ and $C$ to be the lesser of the numbers of white points on either side of the line $BC$; similarly, define the coloring distance $d(W, X)$ between two white points $W$ and $X$ to be the lesser of the numbers of black points on either side of the line $WX$.
A black pairing scheme $\mathcal{B}$ means to label the $2m$ black points as $B_1, \dots, B_m, C_1, \dots, C_m$, such that no two segments from $B_1C_1, \dots, B_mC_m$ intersect each other. For each such $\mathcal{B}$, put
$$
P(\mathcal{B}) = \sum_{i=1}^{m} d(B_i, C_i).
$$
A white pairing scheme $\mathcal{W}$ means to label the $2n$ white points as $W_1, \dots, W_n, X_1, \dots, X_n$, such that no two segments from $W_1X_1, \dots, W_nX_n$ intersect each other. For each such $\mathcal{W}$, put
$$
P(\mathcal{W}) = \sum_{i=1}^{n} d(W_i, X_i).
$$
Prove that, regardless of how the $2m+2n$ vertices are colored, we always have
$$
\max_{\mathcal{B}} P(\mathcal{B}) = \max_{\mathcal{W}} P(\mathcal{W}),
$$
where the maxima are taken over all possible black pairing schemes and all possible white pairing schemes, respectively.
