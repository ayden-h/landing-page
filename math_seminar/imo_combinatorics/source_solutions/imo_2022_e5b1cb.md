# imo_2022_e5b1cb

IMO-SL | IMO | 2022 | Combinatorics | C1.

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2022_e5b1cb](https://mathnet.mit.edu/data_v2/full/imo/imo_2022_e5b1cb.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems with Solutions
- Year: 2022
- Editors: Kunszenti-Kovács, Dávid; Betts, Alexander; Borbényi, Márton; Cranch, James; Lorenzo García, Elisa; Holter, Karl Erik; Ivan, Maria-Romina; Kleppe, Johannes; Kós, Géza; Krachun, Dmitry; Leytem, Charles; Lindqvist, Sofia; Maret, Arnaud; Pompe, Waldemar; Vaderlind, Paul
- Organization: International Mathematical Olympiad
- Place: Oslo, Norway
- Series: International Mathematical Olympiad
- Volume: 63
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

First, we prove that this can always be achieved. Without loss of generality, suppose at least $\frac{2022}{2}=1011$ terms of the $\pm 1$-sequence are $+1$. Define a subsequence as follows: starting at $t=0$, if $a_{t}=+1$ we always include $a_{t}$ in the subsequence. Otherwise, we skip $a_{t}$ if we can (i.e. if we included $a_{t-1}$ in the subsequence), otherwise we include it out of necessity, and go to the next $t$. Clearly, this subsequence will include all $+1$s. Also, for each $-1$ included in the sequence, a $-1$ must have been skipped, so at most $\left\lfloor\frac{1011}{2}\right\rfloor=505$ can be included. Hence the sum is at least $1011-505=506$, as desired.

Next, we prove that, for the $\pm 1$-sequence
$$
(\{-1\},\{+1,+1\},\{-1,-1\},\{+1,+1\}, \ldots,\{+1,+1\},\{-1,-1\},\{+1\})
$$
each admissible subsequence $a_{t_{i}}$ has $-506 \leqslant \sum_{i} a_{t_{i}} \leqslant 506$. We say that the terms inside each curly bracket is a block. In total, there are $1012$ blocks - $506$ of them hold $+1$s, and $506$ of them hold $-1$s. (The two blocks at each end hold $1$ number each, each other block holds $2$.)

Suppose an admissible subsequence includes terms from $k$ blocks holding $+1$s. Then, in each $-1$-pair in between the $+1$-pairs, the subsequence must also include at least one $-1$. There can be at most two $+1$s included from each $+1$-block, and at least one $-1$ must be included from each $-1$-block, so the sum is at most $2k-(k-1)=k+1$.

For $k<506$, this is at most $506$. If $k=506$, one of the $+1$-blocks must be the one at the end, meaning it can only include one $+1$, so that the maximum in this case is only $k$, not $k+1$, so in this case the sum is also at most $506$.

Hence we have shown that for any admissible subsequence, $\sum_{i} a_{t_{i}} \leqslant 506$. Analogously we can show that $-506 \leqslant \sum_{i} a_{t_{i}}$, meaning that $C \leqslant 506$ as desired.

