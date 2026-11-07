# jpn_2007_da6e7a

JMO | Japan | 2007 | The First Round | 4

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2007_da6e7a](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_da6e7a.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: The 17 Japanese Mathematical Olympiad
- Subtitle: The First Round, The Final Round And The 5 Japanese Junior Mathematical Olympiad
- Year: 2007
- Organization: The Mathematical Olympiad Foundation of Japan
- Series: Japan Mathematical Olympiad

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $A$ and $B$ be the first and the last 2 digits of $n$ respectively. We have to determine all $(A, B)$ such that $AB$ divides $100A + B$.

Since $A$ divides $100A + B$, $A$ divides $B$. Let $k = \frac{B}{A}$. Since $A$ and $B$ are 2-digit numbers, $10 \leq A < \frac{100}{k}$.

The condition is equivalent to $kA^2 \mid 100A + kA$ and this is equivalent to $kA \mid 100 + k$. $k$ divides $100 + k$ iff $k$ divides $100$, and with $k < 10$ we get $k = 1, 2, 4, 5$.

From $A \mid \frac{100 + k}{k}$ and $10 \leq A < \frac{100}{k}$ we get $(k, A) = (2, 17), (4, 13)$ and we get $n = 1734, 1352$.
