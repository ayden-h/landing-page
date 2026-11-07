# vnm_2021_dfb9b1

IMO-TST | Vietnam | 2021 | Day 2 | 4

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [vnm_2021_dfb9b1](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2021_dfb9b1.json.gz)

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

Let $p = a + b + c$, $q = ab + bc + ca$ and $r = abc$, we have
$$
2(p^2 - 2q) + 3q = 5p \text{ or } 2p^2 = 5p + q. \quad (1)
$$

We need to prove that $4(p^2 - 2q) + 2q + 7r \le 25$ or $4p^2 + 7r \le 25 + 6q$.
Since $q = p^2 - 5p$, the inequality is equivalent to:
$$
7r + 30p \le 8p^2 + 25.
$$
Notice that $(xy + yz + zx)^2 \ge 3xyz(x + y + z)$ implies $q^2 \ge 3pr$. We distinguish two cases regarding the value of $p$.

* If $p = 0$ then $a = b = c = 0$, so the first inequality is true.

* If $p > 0$ then $r \le \frac{q^2}{3p}$, so we have to prove that
$$
\begin{aligned}
& 7\frac{q^2}{3p} + 30p \le 8p^2 + 25 \\
& 7(2p^2 - 5p)^2 + 90p^2 \le 24p^3 + 75p \\
& p(p-3)(2p-5)(14p-5) \le 0.
\end{aligned} 
\quad (2)
$$
On the other hand, $2p^2 - 5p = q \le \frac{p^2}{3}$ implies $\frac{5}{2} \le p \le 3$, so inequality (2) is true. Therefore, the inequality (1) is true.
