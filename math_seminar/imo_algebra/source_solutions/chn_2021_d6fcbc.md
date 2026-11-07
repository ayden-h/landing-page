# chn_2021_d6fcbc

China-TST | China | 2021 | Test IV, Second Day | 4

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [chn_2021_d6fcbc](https://mathnet.mit.edu/data_v2/full/china/chn_2021_d6fcbc.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: China

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

The maximum is $40$. First, notice that
$$
\begin{align*}
\sum_{i=1}^{60} x_i^2 (x_{i+1} - x_{i-1}) &= \sum_{i=1}^{60} x_i^2 x_{i+1} - \sum_{i=1}^{60} x_i^2 x_{i-1} \\
&= \sum_{i=1}^{60} x_i^2 x_{i+1} - \sum_{i=1}^{60} x_{i+1}^2 x_i \\
&= \sum_{i=1}^{60} x_i x_{i+1} (x_i - x_{i+1}).
\end{align*}
$$
Since $3xy(x-y) = x^3 - y^3 - (x-y)^3$ for any real numbers $x, y$, we have
$$
\begin{align*}
\sum_{i=1}^{60} x_i^2 (x_{i+1} - x_{i-1}) &= \frac{1}{3} \sum_{i=1}^{60} (x_i^3 - x_{i+1}^3 - (x_i - x_{i+1})^3) \\
&= \frac{1}{3} \sum_{i=1}^{60} (x_{i+1} - x_i)^3.
\end{align*}
$$
On one hand, if $x_{3k+1} = 1$, $x_{3k+2} = 0$, $x_{3k+3} = -1$ ($k = 0, 1, \dots, 19$),
$$
\sum_{i=1}^{60} (x_{i+1} - x_i)^3 = 40 \cdot (-1)^3 + 20 \cdot 2^3 = 120;
$$
On the other hand, for $a \in [-2, 2]$, $(a+1)^2(a-2) \le 0$, or $a^3 \le 3a + 2$, and hence
$$
\sum_{i=1}^{60} (x_{i+1} - x_i)^3 \le \sum_{i=1}^{60} (3(x_{i+1} - x_i) + 2) = 120.
$$
In conclusion, the maximum of $\sum_{i=1}^{60} (x_{i+1} - x_i)^3$ is $120$, and the maximum of $\sum_{i=1}^{60} x_i^2(x_{i+1} - x_{i-1})$ is $40$ (when $\{x_n\} = \{1, 0, -1, 1, 0, -1, \dots, 1, 0, -1\}$). $\square$
