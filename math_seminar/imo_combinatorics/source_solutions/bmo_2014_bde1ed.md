# bmo_2014_bde1ed

BMO-SL | Balkan Mathematical Olympiad | 2014 | Combinatorics | C1

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2014_bde1ed](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_bde1ed.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: 31st Balkan Mathematical Olympiad
- Subtitle: Problem Shortlist with solutions
- Year: 2014
- Editors: Kolev, Emil; Ivanov, Alexander; Beluhov, Nikolay
- Organization: Balkan Mathematical Olympiad
- Place: Pleven, Bulgaria
- Series: Balkan Mathematical Olympiad
- Volume: 31
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Denote the desired number by $t$. Consider the set $B$ consisting of all integers of the form $10a + b$, for $a = 0, 1, 2, 3, 4, 5$ and $b = 1, 2, 3, 4, 5$, i.e.
$$
B = \{1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 21, 22, 23, 24, 25, \dots, 51, 52, 53, 54, 55\}.
$$
If $(10a_1 + b_1) - (10a_2 + b_2) = 5$ then $10(a_1 - a_2) = b_2 - b_1 + 5$. Therefore, $b_2 - b_1 + 5$ is divisible by $10$. On the other hand, $-4 \leq b_2 - b_1 \leq 4$ applying $1 \leq b_2 - b_1 + 5 \leq 9$, a contradiction. Since $B$ has cardinality $30$, we have $t \geq 30$.

Consider subset $B$ of $A$ having cardinality $t$. A pair $(m, n)$ is called *good* if $|m - n| = 5$, $m \in B$ and $n \notin B$.

For every $m \in \{1, 2, 3, 4, 5, 51, 52, 53, 54, 55\}$ there exists exactly one $n$ for $(m, n)$ to be a good pair. For all remaining values of $m$ there exist two values of $n$ for $(m, n)$ to be a good pair. Therefore, the number of good pairs is at least $10 + 2(t - 10) = 2t - 10$. On the other hand, this number is at most $2(55 - t)$ (since for every $n$ there exist at most two good pairs $(m, n)$). Thus,
$$
2t - 10 \leq 110 - 2t
$$
applying $t \leq 30$. Therefore $t = 30$.

