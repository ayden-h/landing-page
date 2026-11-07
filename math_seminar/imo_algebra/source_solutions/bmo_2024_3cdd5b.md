# bmo_2024_3cdd5b

BMO-SL | Balkan Mathematical Olympiad | 2024 | Algebra | A3.

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2024_3cdd5b](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_3cdd5b.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: Problem Shortlist
- Subtitle: with solutions
- Year: 2024
- Authors: Harizanov, Stanislav; Kolev, Emil; Cherkashin, Danila; Boev, Stoyan; Gerdjikov, Stefan
- Organization: Balkan Mathematical Olympiad
- Place: Varna, Bulgaria
- Series: Balkan Mathematical Olympiad
- Volume: 41st
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Considering each of the equalities:
$$
\begin{align*}
abc &= 11bc - 36b - 15c \\
abc &= 12ac - 10c - 28a \\
abc &= 13ab - 21a - 6b
\end{align*}
$$
and dividing the first one by $bc > 0$, the second one by $ac$ and third one by $ab$ we obtain:
$$
\begin{align*}
a &= 11 - \frac{36}{c} - \frac{15}{b} \\
b &= 12 - \frac{10}{a} - \frac{28}{c} \\
c &= 13 - \frac{21}{b} - \frac{6}{a}.
\end{align*}
$$
Summing up all three equalities and rearranging, we conclude that:
$$
a + \frac{16}{a} + b + \frac{36}{b} + c + \frac{64}{c} = 36.
$$
Taking into account that $a, b$ and $c$ are positive and applying AM-GM, we get that $a+\frac{16}{a} \ge 8$, $b+\frac{36}{b} \ge 12$ and $c+\frac{64}{c} \ge 16$. Since $8+12+16 = 36$ we conclude that actually all three inequalities are satisfied with equality and this is possible only if:
$a = 4, \quad b = 6, \quad c = 8.$
For $(a, b, c) = (4, 6, 8)$, we have $\frac{36}{c} = \frac{9}{2}$ and $\frac{15}{b} = \frac{5}{2}$. Therefore:
$$
a = 4 = 11 - 7 = 11 - \frac{9}{2} - \frac{5}{2} = 11 - \frac{36}{c} - \frac{15}{b}.
$$
Similarly, $\frac{10}{a} = \frac{5}{2}$ and $\frac{28}{c} = \frac{7}{2}$ and therefore:
$$
b = 6 = 12 - \frac{5}{2} - \frac{7}{2} = 12 - \frac{10}{a} - \frac{28}{c}.
$$

Since two of the equalities are satisfied and the sum of the left hand sides of all three is equal to the sum of the right hand sides of all three equalities, we conclude that the third equality also holds. This shows that $(a, b, c) = (4, 6, 8)$ is indeed a solution of the given system. Hence the unique positive solution of the given system is $(a, b, c) = (4, 6, 8)$. $\square$
