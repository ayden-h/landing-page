# egm_2020_2eb0ec

EGMO | European Girls' Mathematical Olympiad (EGMO) | 2020 |  | Problem 6

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [egm_2020_2eb0ec](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2020_2eb0ec.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: European Girls' Mathematical Olympiad (EGMO)

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

The only such $m$ are $m = 2$ and $m = 10$.

Consider an integer $m > 1$ for which the sequence defined in the problem statement contains only perfect squares. We shall first show that $m - 1$ is a power of $3$.

Suppose that $m - 1$ is even. Then $a_{4} = 5m - 1$ should be divisible by $4$ and hence $m \equiv 1 \pmod{4}$. But then $a_{5} = 5m^{2} + 3m - 1 \equiv 3 \pmod{4}$ cannot be a square, a contradiction. Therefore $m - 1$ is odd.

Suppose that an odd prime $p \neq 3$ divides $m - 1$. Note that $a_{n} - a_{n-1} \equiv a_{n-2} - a_{n-3} \pmod{p}$. It follows that modulo $p$ the sequence takes the form $1, 1, 4, 4, 7, 7, 10, 10, \ldots$; indeed, a simple induction shows that $a_{2k} \equiv a_{2k-1} \equiv 3k - 2 \pmod{p}$ for $k \geq 1$. Since $\gcd(p, 3) = 1$ we get that the sequence $a_{n} \pmod{p}$ contains all the residues modulo $p$, a contradiction since only $(p + 1)/2$ residues modulo $p$ are squares. This shows that $m - 1$ is a power of $3$.

Let $h, k$ be integers such that $m = 3^{k} + 1$ and $a_{4} = h^{2}$. We then have $5 \cdot 3^{k} = (h - 2)(h + 2)$. Since $\gcd(h - 2, h + 2) = 1$, it follows that $h - 2$ equals either $1, 3^{k}$ or $5$, and $h + 2$ equals either $5 \cdot 3^{k}, 5$ or $3^{k}$, respectively. In the first two cases we get $k = 0$ and in the last case we get $k = 2$. This implies that either $m = 2$ or $m = 10$.

We now show the converse. Suppose that $m = 2$ or $m = 10$. Let $t = 1$ or $t = 3$ so that $m = t^{2} + 1$. Let $b_{1}, b_{2}, b_{3}, \ldots$ be a sequence of integers defined by $b_{1} = 1, b_{2} = 1, b_{3} = 2$, and
$$
b_{n} = t b_{n-1} + b_{n-2}, \quad \text{for all } n \geq 4
$$
Clearly, $a_{n} = b_{n}^{2}$ for $n = 1, 2, 3$. Note that if $m = 2$ then $a_{4} = 9$ and $b_{4} = 3$, and if $m = 10$ then $a_{4} = 49$ and $b_{4} = 7$. In both the cases we have $a_{4} = b_{4}^{2}$.

If $n \geq 5$ then we have
$$
b_{n}^{2} + b_{n-3}^{2} = \left(t b_{n-1} + b_{n-2}\right)^{2} + \left(b_{n-1} - t b_{n-2}\right)^{2} = \left(t^{2} + 1\right)\left(b_{n-1}^{2} + b_{n-2}^{2}\right) = m\left(b_{n-1}^{2} + b_{n-2}^{2}\right).
$$
Therefore, it follows by induction that $a_{n} = b_{n}^{2}$ for all $n \geq 1$. This completes the solution.

## Supplied solution 2

We present an alternate proof that $m = 2$ and $m = 10$ are the only possible values of $m$ with the required property.

Note that
$$
\begin{aligned}
& a_{4} = 5m - 1 \\
& a_{5} = 5m^{2} + 3m - 1 \\
& a_{6} = 5m^{3} + 8m^{2} - 2m - 4
\end{aligned}
$$
Since $a_{4}$ and $a_{6}$ are squares, so is $a_{4} a_{6}$. We have
$$
4 a_{4} a_{6} = 100 m^{4} + 140 m^{3} - 72 m^{2} - 72 m + 16
$$
Notice that
$$
\begin{aligned}
& \left(10 m^{2} + 7m - 7\right)^{2} = 100 m^{4} + 140 m^{3} - 91 m^{2} - 98 m + 49 < 4 a_{4} a_{6} \\
& \left(10 m^{2} + 7m - 5\right)^{2} = 100 m^{4} + 140 m^{3} - 51 m^{2} - 70 m + 25 > 4 a_{4} a_{6}
\end{aligned}
$$
so we must have
$$
4 a_{4} a_{6} = \left(10 m^{2} + 7m - 6\right)^{2} = 100 m^{4} + 140 m^{3} - 71 m^{2} - 84 m + 36
$$
This implies that $m^{2} - 12m + 20 = 0$, so $m = 2$ or $m = 10$.
