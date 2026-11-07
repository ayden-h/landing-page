# mkd_2008_acffae

BMO | North Macedonia | 2008 | Regional competition, IV year | 1. (B)

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [mkd_2008_acffae](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_acffae.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: North Macedonia
- Title: Macedonian Mathematical Competitions
- Year: 2008
- Editors: Maneva-Erakovic, Vesna; Malcheski, Risto; Markovski, Gjorgji; Markovski, Jasmina; Prangoski, Bojan; Cvetkovski, Zdravko; Petruschevski, Mirko; Malcheski, Aleksa
- Organization: MACEDONIAN MATHEMATICAL SOCIETY

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

If $p, q, r$ are consecutive terms in the arithmetic progression, then $p + r = 2q$. Because of this, we have
$$
\sqrt{y^2 + 2y + 1} + y - 1 = 2 \frac{y^2 + 3y - 1}{3}
$$
$$
3(\sqrt{(y+1)^2} + y - 1) = 2(y^2 + 3y - 1)
$$

Since $\sqrt{(y+1)^2} = |y+1|$, we have
$$
\begin{aligned}
3(|y+1| + y - 1) &= 2(y^2 + 3y - 1) \\
2y^2 + 3y - 3 &= |y+1| + 1 = 0
\end{aligned}
$$
The last equation is equivalent with
$$
\begin{cases} y + 1 \ge 0 \\ y^2 + 3y - 3(y+1) + 1 = 0 \end{cases}
$$
$$
\begin{cases} y + 1 < 0 \\ y^2 + 3y + 3(y+1) + 1 = 0 \end{cases}
$$
$$
\begin{cases} y \ge -1 \\ y^2 - 1 = 0 \end{cases} \text{ or } 
\begin{cases} y < -1 \\ y^2 + 3y + 2 = 0 \end{cases}
$$
The solution of the first system is $y = 1$ or $y = -1$, and for the second one is $y = -2$. Finally $y \in \{-2, -1, 1\}$.
