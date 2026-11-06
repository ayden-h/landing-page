# imo_2009_7c4eea

IMO-SL | IMO | 2009 | Combinatorics | C2

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2009_7c4eea](https://mathnet.mit.edu/data_v2/full/imo/imo_2009_7c4eea.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Problem Shortlist with solutions
- Year: 2009
- Editors: Engel, Konrad; Fegert, Karl; Felgenhauer, Andreas; Gronau, Hans-Dietrich; Labahn, Roger; Mulansky, Bernd; Prestin, Jürgen; Reiher, Christian; Scholze, Peter; Specht, Eckard; Strich, Robert; Welk, Martin
- Organization: Federal Ministry of Education and Research; Die Senatorin für Bildung und Wissenschaft; Freie Hansestadt Bremen; Bildung Begabung; JACOBS UNIVERSITY
- Place: Bremen, Germany
- Series: International Mathematical Olympiad
- Volume: 50th
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $n \geq 2$ be an integer and let $\{T_{1}, \ldots, T_{N}\}$ be any set of triples of nonnegative integers satisfying the conditions (1) and (2). Since the $a$-coordinates are pairwise distinct we have
$$
\sum_{i=1}^{N} a_{i} \geq \sum_{i=1}^{N}(i-1)=\frac{N(N-1)}{2}
$$
Analogously,
$$
\sum_{i=1}^{N} b_{i} \geq \frac{N(N-1)}{2} \quad \text{ and } \quad \sum_{i=1}^{N} c_{i} \geq \frac{N(N-1)}{2} .
$$
Summing these three inequalities and applying (1) yields
$$
3 \frac{N(N-1)}{2} \leq \sum_{i=1}^{N} a_{i}+\sum_{i=1}^{N} b_{i}+\sum_{i=1}^{N} c_{i}=\sum_{i=1}^{N}\left(a_{i}+b_{i}+c_{i}\right)=n N,
$$
hence $3 \frac{N-1}{2} \leq n$ and, consequently,
$$
N \leq\left\lfloor\frac{2 n}{3}\right\rfloor+1
$$
By constructing examples, we show that this upper bound can be attained, so $N(n)=\left\lfloor\frac{2 n}{3}\right\rfloor+1$.
We distinguish the cases $n=3 k-1, n=3 k$ and $n=3 k+1$ for $k \geq 1$ and present the extremal examples in form of a table.

| $n=3 k-1$ |   |   |
| :---: | :---: | :---: |
| $\left\lfloor\frac{2 n}{3}\right\rfloor+1=2 k$ |   |   |
| $a_{i}$ | $b_{i}$ | $c_{i}$ |
| 0 | $k+1$ | $2 k-2$ |
| 1 | $k+2$ | $2 k-4$ |
| $\vdots$ | $\vdots$ | $\vdots$ |
| $k-1$ | $2 k$ | 0 |
| $k$ | 0 | $2 k-1$ |
| $k+1$ | 1 | $2 k-3$ |
| $\vdots$ | $\vdots$ | $\vdots$ |
| $2 k-1$ | $k-1$ | 1 |

| $n=3 k$ |   |   |
| :---: | :---: | :---: |
| $\left\lfloor\frac{2 n}{3}\right\rfloor+1=2 k+1$ |   |   |
| $a_{i}$ | $b_{i}$ | $c_{i}$ |
| 0 | $k$ | $2 k$ |
| 1 | $k+1$ | $2 k-2$ |
| $\vdots$ | $\vdots$ | $\vdots$ |
| $k$ | $2 k$ | 0 |
| $k+1$ | 0 | $2 k-1$ |
| $k+2$ | 1 | $2 k-3$ |
| $\vdots$ | $\vdots$ | $\vdots$ |
| $2 k$ | $k-1$ | 1 |

| $n=3 k+1$ |   |   |
| :---: | :---: | :---: |
| $\left\lfloor\frac{2 n}{3}\right\rfloor+1=2 k+1$ |   |   |
| $a_{i}$ | $b_{i}$ | $c_{i}$ |
| 0 | $k$ | $2 k+1$ |
| 1 | $k+1$ | $2 k-1$ |
| $\vdots$ | $\vdots$ | $\vdots$ |
| $k$ | $2 k$ | 1 |
| $k+1$ | 0 | $2 k$ |
| $k+2$ | 1 | $2 k-2$ |
| $\vdots$ | $\vdots$ | $\vdots$ |
| $2 k$ | $k-1$ | 2 |

It can be easily seen that the conditions (1) and (2) are satisfied and that we indeed have $\left\lfloor\frac{2 n}{3}\right\rfloor+1$ triples in each case.

