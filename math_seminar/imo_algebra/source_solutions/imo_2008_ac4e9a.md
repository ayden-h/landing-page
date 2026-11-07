# imo_2008_ac4e9a

IMO-SL | IMO | 2008 | Algebra | A3

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2008_ac4e9a](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_ac4e9a.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: 49th International Mathematical Olympiad
- Subtitle: Shortlisted Problems with Solutions
- Year: 2008
- Editors: Velázquez, Vicente Muñoz; Calero, Juan Manuel Conde; Kós, Géza; Kuczma, Marcin; Medarde, Daniel Lasaosa; Riera, Ignasi Mundet i; Savchev, Svetoslav
- Place: Madrid, Spain
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We show that the answer is NO for part (a), and YES for part (b).

a.
Throughout the solution, we will use the notation $g_{k}(x) = \overbrace{g(g(\ldots g}^{k}(x) \ldots))$, including $g_{0}(x) = x$ as well.
Suppose that there exists a Spanish Couple $(f, g)$ on the set $\mathbb{N}$. From property (i) we have $f(x) \geq x$ and $g(x) \geq x$ for all $x \in \mathbb{N}$.

We claim that $g_{k}(x) \leq f(x)$ for all $k \geq 0$ and all positive integers $x$. The proof is done by induction on $k$. We already have the base case $k = 0$ since $x \leq f(x)$. For the induction step from $k$ to $k+1$, apply the induction hypothesis on $g_{2}(x)$ instead of $x$, then apply (ii):
$$
g\left(g_{k+1}(x)\right) = g_{k}\left(g_{2}(x)\right) \leq f\left(g_{2}(x)\right) < g(f(x))
$$
Since $g$ is increasing, it follows that $g_{k+1}(x) < f(x)$. The claim is proven.

If $g(x) = x$ for all $x \in \mathbb{N}$ then $f(g(g(x))) = f(x) = g(f(x))$, and we have a contradiction with (ii). Therefore one can choose an $x_{0} \in S$ for which $x_{0} < g\left(x_{0}\right)$. Now consider the sequence $x_{0}, x_{1}, \ldots$ where $x_{k} = g_{k}\left(x_{0}\right)$. The sequence is increasing. Indeed, we have $x_{0} < g\left(x_{0}\right) = x_{1}$, and $x_{k} < x_{k+1}$ implies $x_{k+1} = g\left(x_{k}\right) < g\left(x_{k+1}\right) = x_{k+2}$.

Hence, we obtain a strictly increasing sequence $x_{0} < x_{1} < \ldots$ of positive integers which on the other hand has an upper bound, namely $f\left(x_{0}\right)$. This cannot happen in the set $\mathbb{N}$ of positive integers, thus no Spanish Couple exists on $\mathbb{N}$.

b.
We present a Spanish Couple on the set $S = \{ a - 1 / b : a, b \in \mathbb{N} \}$.
Let
$$
\begin{aligned}
& f(a - 1 / b) = a + 1 - 1 / b \\
& g(a - 1 / b) = a - 1 / (b + 3^{a})
\end{aligned}
$$
These functions are clearly increasing. Condition (ii) holds, since
$$
f(g(g(a - 1 / b))) = (a + 1) - 1 / (b + 2 \cdot 3^{a}) < (a + 1) - 1 / (b + 3^{a+1}) = g(f(a - 1 / b))
$$
