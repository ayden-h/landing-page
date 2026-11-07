# imo_2012_2dedb8

IMO-SL | IMO | 2012 | Combinatorics | C2

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2012_2dedb8](https://mathnet.mit.edu/data_v2/full/imo/imo_2012_2dedb8.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems with Solutions
- Subtitle: 53rd International Mathematical Olympiad
- Year: 2012
- Editors: Avendaño, Martín; di Fiore, Carlos; Kós, Géza; Savchev, Svetoslav
- Organization: International Mathematical Olympiad
- Place: Mar del Plata, Argentina

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Consider $x$ such pairs in $\{1,2, \ldots, n\}$. The sum $S$ of the $2x$ numbers in them is at least $1+2+\cdots+2x$ since the pairs are disjoint. On the other hand $S \leq n+(n-1)+\cdots+(n-x+1)$ because the sums of the pairs are different and do not exceed $n$. This gives the inequality
$$
\frac{2x(2x+1)}{2} \leq nx-\frac{x(x-1)}{2}
$$
which leads to $x \leq \frac{2n-1}{5}$. Hence there are at most $\left\lfloor\frac{2n-1}{5}\right\rfloor$ pairs with the given properties.

We show a construction with exactly $\left\lfloor\frac{2n-1}{5}\right\rfloor$ pairs. First consider the case $n=5k+3$ with $k \geq 0$, where $\left\lfloor\frac{2n-1}{5}\right\rfloor=2k+1$. The pairs are displayed in the following table.

| Pairs | $3k+1$ | $3k$ | $\cdots$ | $2k+2$ | $4k+2$ | $4k+1$ | $\cdots$ | $3k+3$ | $3k+2$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|       | 2     | 4     | $\cdots$ | $2k$   | 1     | 3     | $\cdots$ | $2k-1$ | $2k+1$ |
| Sums  | $3k+3$ | $3k+4$ | $\cdots$ | $4k+2$ | $4k+3$ | $4k+4$ | $\cdots$ | $5k+2$ | $5k+3$ |

The $2k+1$ pairs involve all numbers from $1$ to $4k+2$; their sums are all numbers from $3k+3$ to $5k+3$. The same construction works for $n=5k+4$ and $n=5k+5$ with $k \geq 0$. In these cases the required number $\left\lfloor\frac{2n-1}{5}\right\rfloor$ of pairs equals $2k+1$ again, and the numbers in the table do not exceed $5k+3$. In the case $n=5k+2$ with $k \geq 0$ one needs only $2k$ pairs. They can be obtained by ignoring the last column of the table (thus removing $5k+3$). Finally, $2k$ pairs are also needed for the case $n=5k+1$ with $k \geq 0$. Now it suffices to ignore the last column of the table and then subtract $1$ from each number in the first row.
