# imo_2020_43ccfa

IMO-SL | IMO | 2020 | Algebra | A4

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2020_43ccfa](https://mathnet.mit.edu/data_v2/full/imo/imo_2020_43ccfa.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

The weighted AM-GM inequality with weights $a$, $b$, $c$, $d$ gives
$$
a^{a} b^{b} c^{c} d^{d} \leqslant a \cdot a + b \cdot b + c \cdot c + d \cdot d = a^{2} + b^{2} + c^{2} + d^{2}
$$
so it suffices to prove that $(a + 2b + 3c + 4d)(a^{2} + b^{2} + c^{2} + d^{2}) < 1 = (a + b + c + d)^{3}$. This can be done in various ways, for example:
$$
\begin{aligned}
(a + b + c + d)^{3} > & a^{2}(a + 3b + 3c + 3d) + b^{2}(3a + b + 3c + 3d) \\
& + c^{2}(3a + 3b + c + 3d) + d^{2}(3a + 3b + 3c + d) \\
\geqslant & (a^{2} + b^{2} + c^{2} + d^{2}) \cdot (a + 2b + 3c + 4d)
\end{aligned}
$$

## Supplied solution 2

From $b \geqslant d$ we get
$$
a + 2b + 3c + 4d \leqslant a + 3b + 3c + 3d = 3 - 2a .
$$
If $a < \frac{1}{2}$, then the statement can be proved by
$$
(a + 2b + 3c + 4d) a^{a} b^{b} c^{c} d^{d} \leqslant (3 - 2a) a^{a} a^{b} a^{c} a^{d} = (3 - 2a) a = 1 - (1 - a)(1 - 2a) < 1
$$
From now on we assume $\frac{1}{2} \leqslant a < 1$.
By $b, c, d < 1 - a$ we have
$$
b^{b} c^{c} d^{d} < (1 - a)^{b} \cdot (1 - a)^{c} \cdot (1 - a)^{d} = (1 - a)^{1 - a}
$$
Therefore,
$$
(a + 2b + 3c + 4d) a^{a} b^{b} c^{c} d^{d} < (3 - 2a) a^{a} (1 - a)^{1 - a}
$$
For $0 < x < 1$, consider the functions
$f(x) = (3 - 2x) x^{x} (1 - x)^{1 - x}$ and $g(x) = \log f(x) = \log (3 - 2x) + x \log x + (1 - x) \log (1 - x)$; hereafter, log denotes the natural logarithm. It is easy to verify that
$$
g''(x) = -\frac{4}{(3 - 2x)^{2}} + \frac{1}{x} + \frac{1}{1 - x} = \frac{1 + 8(1 - x)^{2}}{x(1 - x)(3 - 2x)^{2}} > 0
$$
so $g$ is strictly convex on $(0, 1)$.
By $g\left(\frac{1}{2}\right) = \log 2 + 2 \cdot \frac{1}{2} \log \frac{1}{2} = 0$ and $\lim_{x \rightarrow 1-} g(x) = 0$, we have $g(x) \leqslant 0$ (and hence $f(x) \leqslant 1$) for all $x \in \left[\frac{1}{2}, 1\right)$, and therefore
$$
(a + 2b + 3c + 4d) a^{a} b^{b} c^{c} d^{d} < f(a) \leqslant 1
$$
