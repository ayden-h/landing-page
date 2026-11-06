# imo_2021_da9f3d

IMO-SL | IMO | 2021 | Combinatorics | C2

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2021_da9f3d](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_da9f3d.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems
- Subtitle: IMO 2021: 62nd International Mathematical Olympiad Saint-Petersburg Russia
- Year: 2021
- Editors: Kós, Géza; Woeginger, Gerhard; Ustinov, Alexey; Krachun, Dmitry; Mitrofanov, Ivan; Berlov, Sergey; Petrov, Fedor; Frolov, Ivan; Vaderlind, Paul; Golovanov, Alexander; Bogdanov, Ilya I.
- Organization: International Mathematical Olympiad
- Place: Saint-Petersburg — Russia
- Series: International Mathematical Olympiad
- Volume: 62nd

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Answer: $m_{\text{max}} = n^{2} - n - 1$.

First suppose that there are $n(n-1)-1$ marbles. Then for one of the colours, say blue, there are at most $n-2$ marbles, which partition the non-blue marbles into at most $n-2$ groups with at least $(n-1)^{2} > n(n-2)$ marbles in total. Thus one of these groups contains at least $n+1$ marbles and this group does not contain any blue marble.

Now suppose that the total number of marbles is at least $n(n-1)$. Then we may write this total number as $n k + j$ with some $k \geqslant n-1$ and with $0 \leqslant j \leqslant n-1$. We place around a circle $k-j$ copies of the colour sequence $[1,2,3, \ldots, n]$ followed by $j$ copies of the colour sequence $[1,1,2,3, \ldots, n]$.

