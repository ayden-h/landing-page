# bmo_2023_bc3f7d

BMO-SL | Balkan Mathematical Olympiad | 2023 | Algebra | A2

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2023_bc3f7d](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_bc3f7d.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: Shortlisted Problems with Solutions
- Year: 2023
- Editors: Üçer, Melih; Bahadır, Selim; Kadan, Fehmi Emre; Yıldız, Mehmet Akif; İleri, Ahmet; Kaymak, Ozan
- Place: Antalya-Türkiye
- Series: BMO
- Volume: 2023

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Assume that $a \ge b \ge c \ge d$. We will show that the sequence $(x_1, x_2, x_3, x_4) = (a, b, d, c)$ satisfies the requirement $x_1x_2 + x_2x_3 + x_3x_4 + x_4x_1 \ge 4$, i.e. $(a+d)(b+c) \ge 4$. Denoting
$$
x = \frac{a+d}{2}, \quad y = \frac{b+c}{2},
$$
we need to show that $xy \ge 1$ using $a \ge y \ge d$ and
$$
\frac{1}{a+3} + \frac{1}{b+3} + \frac{1}{c+3} + \frac{1}{d+3} = 1.
$$
Since
$$
\frac{1}{b+3} + \frac{1}{c+3} \ge \frac{2}{y+3}
$$
(by the AM-HM inequality or Jensen's inequality), the equality constraint gives
$$
\frac{1}{a+3} + \frac{1}{d+3} + \frac{2}{y+3} \le 1, \quad \text{that is,} \quad \frac{2(x+3)}{ad+6x+9} \le \frac{y+1}{y+3}.
$$
From $(y-a)(y-d) \le 0$, we get $ad \le 2xy - y^2$, therefore we have
$$
\frac{2(x+3)}{2xy - y^2 + 6x + 9} \le \frac{y+1}{y+3}, \quad \text{that is,} \quad \frac{2(x+3)}{(2x-y+3)(y+3)} \le \frac{y+1}{y+3}.
$$
Hence
$$
2(x + 3) \le (2x - y + 3)(y + 1) \implies 2xy \ge y^2 - 2y + 3 \implies 2(xy - 1) \ge (y - 1)^2,
$$
thus $xy \ge 1$.

## Supplied solution 2

Performing the calculations, the equality constraint becomes
$$
S_4 + 2S_3 + 3S_2 = 27,
$$
where $S_4 = abcd$, $S_3 = \sum abc$ and $S_2 = \sum ab$. From the known Maclaurin inequalities
$$
S_4 \le \left(\frac{S_2}{6}\right)^2, \quad \frac{S_3}{4} \le \left(\frac{S_2}{6}\right)^{3/2},
$$
we get
$$
\left(\frac{S_2}{6}\right)^2 + 8 \left(\frac{S_2}{6}\right)^{3/2} + 3S_2 \ge 27,
$$
therefore $S_2 \ge 6$. Now consider the permutations $(a, b, c, d)$, $(a, c, d, b)$ and $(a, d, b, c)$ to form the sums
$$
\sigma_1 = ab + bc + cd + da, \quad \sigma_2 = ac + cd + db + ba, \quad \sigma_3 = ad + db + bc + ca.
$$
We have $\sigma_1 + \sigma_2 + \sigma_3 = 2S_2 \ge 12$, therefore at least one of $\sigma_1, \sigma_2, \sigma_3$ should be greater than or equal to 4, and hence we are done.
