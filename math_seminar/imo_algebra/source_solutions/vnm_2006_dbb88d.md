# vnm_2006_dbb88d

VMO | Vietnam | 2006 | First day | Problem 1

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [vnm_2006_dbb88d](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2006_dbb88d.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Vietnam
- Title: 2006 VIETNAMESE MATHEMATICAL OLYMPIAD
- Year: 2006

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Conditions for $x$, $y$, $z$ of the definition of the expressions in the equation are: $x, y, z < 6$.
The given system of equations is equivalent to the system:
$$
\left\{
\begin{aligned}
\log_3(6-y) &= \frac{x}{\sqrt{x^2-2x+6}} && (1) \\
\log_3(6-z) &= \frac{y}{\sqrt{y^2-2y+6}} && (2) \\
\log_3(6-x) &= \frac{z}{\sqrt{z^2-2z+6}} && (3)
\end{aligned}
\right.
$$
The function $f(x) = \frac{x}{\sqrt{x^2-2x+6}}$ is increasing since
$$
f'(x) = \frac{6-x}{(x^2 - 2x + 6)\sqrt{x^2 - 2x + 6}} > 0
$$
for $x < 6$.
The function $g(x) = \log_3(6-x)$ is decreasing for $x < 6$.
We now prove that if $(x, y, z)$ is a solution to the given system of equations then $x = y = z = 3$.
Without loss of generality, suppose that $\max(x, y, z) = x$. We must consider two cases:

i) $x \geq y \geq z$

As $f(x) = \frac{x}{\sqrt{x^2-2x+6}}$ is increasing, (1), (2), (3) show that
$$
\log_3(6-y) \geq \log_3(6-z) \geq \log_3(6-x),
$$
so $x \ge z \ge y$. But $y \ge z$, so $z = y$. Then (1) and (2) imply that $x = y = z$.

ii) $x \geq z \geq y$

Analogously, we have $\log_3(6-y) \ge \log_3(6-x) \ge \log_3(6-z)$ and so $z \ge x \ge y$. But $x \ge z$, so $x = z$. Then (1) and (3) imply that $x = y = z$.

The equation $f(x) = g(x)$ has a unique root $x = 3$. Consequently, the given system of equations has a unique solution $x = y = z = 3$.
