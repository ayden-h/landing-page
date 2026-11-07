# vnm_2021_a8fb9e

VMO | Vietnam | 2021 | Day 1 | 2

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [vnm_2021_a8fb9e](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2021_a8fb9e.json.gz)

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

By letting $y = 0$ in (1), we have $f(x) \cdot f(0) = f(-1) + x f(0)$.
We distinguish two cases regarding the value of $f(0)$.

**Case 1.** $f(0) \neq 0$ implies $f(x) = x + c$ for all $x \in \mathbb{R}$ with $c$ is constant, which is not a solution.

**Case 2.** $f(0) = 0$ implies $f(-1) = 0$.
By plugging $x = y = 1$ into (1), we get $f(1)^2 = 2 f(1)$, so $f(1) = 0$ or $f(1) = 2$. From (1), the substitution $y = -1$ yields
$$
f(-y - 1) = f(y), \forall y \in \mathbb{R}. \quad (2)
$$
Replacing $y$ by $-y - 1$ in (1), we get
$$
f(x) f(-y - 1) = f(-x(y + 1) - 1) + x f(-y - 1) - (y + 1) f(x).
$$
Thus, it follows from (2)
$$
f(xy - 1) + y f(x) = f(xy + x) - (y + 1) f(x), \forall x, y \in \mathbb{R}. \quad (3)
$$
Let $x \neq -1$, replacing $x$ by $x + 1$ and $y$ by $\frac{1}{x+1}$ in (3), we have
$$
f(x - 1) = \frac{x - 1}{x + 1} f(x), \forall x \neq -1.
$$
On the other hand, we set $y = 1$ in (1) and get
$$
\begin{aligned}
f(x) \cdot f(1) &= f(x - 1) + x \cdot f(1) + f(x) \\
&= \frac{x - 1}{x + 1} \cdot f(x) + x \cdot f(1) + f(x), \forall x \neq -1.
\end{aligned} \quad (4)
$$
* If $f(1) = 0$ then $f = 0$ because (4) and $f(-1) = 0$.
* If $f(1) = 2$ then $f(x) = x(x + 1)$ because (4) and $f(-1) = 0$.

It is easy to see that $f(x) \equiv 0$ and $f(x) = x(x+1)$ satisfied (1). $\square$
