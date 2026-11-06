# jpn_2006_ef0ba3

JMO | Japan | 2006 |  | 3

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2006_ef0ba3](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_ef0ba3.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: The 16th Japanese Mathematical Olympiad
- Year: 2006
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Denote by $a_{ij}$ the entry that lies in the $i$-th column and the $j$-th row. The given conditions yields that each $1$, $2$, $3$ and $4$ appear exactly once in each column.
We may assume without loss of generality that $a_{1j} = j$ for $j = 1, 2, 3, 4$. We would multiply the answer by $4!$ afterwards. We may also assume that $a_{22} = a_{33} = 1$. We would multiply the answer by $3 \times 2$ afterwards.
If $a_{21}, a_{31} \neq 4$, then $a_{23} = a_{32} = 4$. We can choose which of $a_{24}$ and $a_{34}$ to be $2$, and the rest entries would be determined uniquely. So we have two ways.
Otherwise, if $a_{21} = 4$, there are only one way to fill the other squares. The case $a_{31} = 4$ is similar. So we have two ways.
Therefore, the answer is $4! \times 3 \times 2 \times (2+2) = 576$.

