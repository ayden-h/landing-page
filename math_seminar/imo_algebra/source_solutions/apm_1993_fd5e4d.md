# apm_1993_fd5e4d

APMO | Asia Pacific Mathematics Olympiad (APMO) | 1993 |  | 3

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [apm_1993_fd5e4d](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1993_fd5e4d.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Asia Pacific Mathematics Olympiad (APMO)
- Title: APMO 1993 – Problems and Solutions
- Year: 1993

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Expanding $(x + r) f(x)$, we find that $c_{n+1} = a_{n}$, $c_{k} = a_{k-1} + r a_{k}$ for $k = 1, 2, \ldots, n$, and $c_{0} = r a_{0}$. Consider three cases:
- $r = 0$. Then $c_{0} = 0$ and $c_{k} = a_{k-1}$ for $k = 1, 2, \ldots, n$, and $a = c \Longrightarrow \frac{a}{c} = 1 \leq n+1$.

- $|r| \geq 1$. Then
$$
\begin{gathered}
\left|a_{0}\right| = \left|\frac{c_{0}}{r}\right| \leq c, \\
\left|a_{1}\right| = \left|\frac{c_{1} - a_{0}}{r}\right| \leq \left|c_{1}\right| + \left|a_{0}\right| \leq 2c,
\end{gathered}
$$
and inductively if $\left|a_{k}\right| \leq (k+1)c$
$$
\left|a_{k+1}\right| = \left|\frac{c_{k+1} - a_{k}}{r}\right| \leq \left|c_{k+1}\right| + \left|a_{k}\right| \leq c + (k+1)c = (k+2)c.
$$
Therefore, $\left|a_{k}\right| \leq (k+1)c \leq (n+1)c$ for all $k$, and $a \leq (n+1)c \Longleftrightarrow \frac{a}{c} \leq n+1$.

- $0 < |r| < 1$. Now work backwards: $\left|a_{n}\right| = \left|c_{n+1}\right| \leq c$,
$$
\left|a_{n-1}\right| = \left|c_{n} - r a_{n}\right| \leq \left|c_{n}\right| + \left|r a_{n}\right| < c + c = 2c,
$$
and inductively if $\left|a_{n-k}\right| \leq (k+1)c$
$$
\left|a_{n-k-1}\right| = \left|c_{n-k} - r a_{n-k}\right| \leq \left|c_{n-k}\right| + \left|r a_{n-k}\right| < c + (k+1)c = (k+2)c.
$$
Therefore, $\left|a_{n-k}\right| \leq (k+1)c \leq (n+1)c$ for all $k$, and $a \leq (n+1)c$ again.
