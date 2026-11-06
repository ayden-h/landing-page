# vnm_2013_8efd6e

VMO | Vietnam | 2013 | Day 1 | 4

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [vnm_2013_8efd6e](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2013_8efd6e.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Vietnam
- Title: VIETNAMESE MATHEMATICAL COMPETITIONS
- Subtitle: 2013 - 2022
- Year: 2022
- Authors: Vinh, Le Anh; Lu, Le Phuc; Nghia, Truong Tuan; Toan, Dao Trong
- Publisher: Vietnam National University Press
- Place: Hanoi
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

a) We first observe that one cannot write the number $2013$ between a pair $(a, b)$ with $a + b > 2013$. Using this simple observation, it is easy to check that the number $2013$ is written only twice after $2013$ steps in the $8$th and the $1013$th steps.

b) We add an extra number $1$ after $1000$ on the line. We perform $2013$ such steps on this new line and count how many times the number $2013$ is written. We construct a sequence $A$ of pairs inductively as follows. Initially,
$$
A = \{(1, 2), (2, 3), \dots, (999, 1000), (1000, 1)\}.
$$
In each step of the transformation, whenever we write a number $k = a + b$ between the pair $(a, b)$ (from left to right), we add two pairs $(a, k)$ and $(k, b)$ into the sequence $A$.
We will prove by induction on $a + b$ that an ordered pair $(a, b)$ appears on the sequence $A$ only if $\text{gcd}(a, b) = 1$, and if $\text{gcd}(a, b) = 1$ then the pair $(a, b)$ appears exactly once on the sequence $A$.
Suppose that this statement holds for any $a+b < k$, we show that it also holds when $a+b = k$. Without loss of generality, we can assume that $a < b$ (the case $a > b$ is similar). The pair $(a, b)$ is added to the sequence $A$ whenever we write the number $b$ between the pair $(a, b-a)$. Since $a+(b-a) = b < k$, the pair $(a, b-a)$ appears on the sequence $A$ only if $\text{gcd}(a, b-a) = 1$, and if $\text{gcd}(a, b-a) = 1$ then the pair $(a, b-a)$ appears exactly once on the sequence $A$. Since
$$
\text{gcd}(a, b) = \text{gcd}(a, b-a),
$$
the statement holds for $a+b=k$. By the induction principle, the statement holds for any $(a, b)$. This implies that the number of times that $2013$ is written is the number of pairs $(a, 2013-a)$ with $\text{gcd}(a, 2013-a) = 1$. Therefore, the number $2013$ is written $\phi(2013) = 1200$ times on the new line.

By the part a), the number $2013$ is written twice between $1000$ and $1$. Hence, the number $2013$ is written $1200-2=1198$ times on the given line. $\square$

