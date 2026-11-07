# usa_2019_f27ccd

IMO-TST | United States | 2019 | Day 1 | TSTST 1

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [usa_2019_f27ccd](https://mathnet.mit.edu/data_v2/full/united-states/usa_2019_f27ccd.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: United States
- Title: USA TSTST 2019 Solutions
- Subtitle: TST Selection Test
- Year: 2019
- Authors: Bhattacharya, Ankan; Chen, Evan

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

**First solution using Cauchy FE** We prove:
**Claim** — We have $a \diamond b = af(b)$ where $f$ is some involutive and totally multiplicative function. (In fact, this classifies all functions satisfying the first condition completely.)
*Proof*. Let $P(a, b, c)$ denote the assertion $a \diamond (b \diamond c) = (a \diamond b) \cdot c$.
* Note that for any $x$, the function $y \mapsto x \diamond y$ is injective, because if $x \diamond y_1 = x \diamond y_2$ then take $P(1, x, y_i)$ to get $y_1 = y_2$.
* Take $P(1, x, 1)$ and injectivity to get $x \diamond 1 = x$.
* Take $P(1, 1, y)$ to get $1 \diamond (1 \diamond y) = y$.
* Take $P(x, 1, 1 \diamond y)$ to get
$$
x \diamond y = x \cdot (1 \diamond y).
$$
Henceforth let us define $f(y) = 1 \diamond y$, so $f(1) = 1$, $f$ is involutive and
$$
x \diamond y = xf(y).
$$
Plugging this into the original condition now gives $f(bf(c)) = f(b)c$, which (since $f$ is an involution) gives $f$ completely multiplicative. $\square$
In particular, $f(1) = 1$. We are now interested only in the second condition, which reads $f(x) \ge 1/x$ for $x \ge 1$.
Define the function
$$
g(t) = \log f(e^t)
$$
so that $g$ is additive, and also $g(t) \ge -t$ for all $t \ge 0$. We appeal to the following theorem:
**Lemma**
If $h: \mathbb{R} \to \mathbb{R}$ is an additive function which is not linear, then it is *dense* in the plane: for any point $(x_0, y_0)$ and $\varepsilon > 0$ there exists $(x, y)$ such that $h(x) = y$ and $\sqrt{(x - x_0)^2 + (y - y_0)^2} < \varepsilon$.
Applying this lemma with the fact that $g(t) \ge -t$ implies readily that $g$ is linear. In other words, $f$ is of the form $f(x) = x^r$ for some fixed real number $r$. It is easy to check $r = \pm 1$ which finishes.


**Second solution manually** As before we arrive at $a \diamond b = af(b)$, with $f$ an involutive and totally multiplicative function.
We prove that:
**Claim** — For any $a > 0$, we have $f(a) \in \{1/a, a\}$.
*Proof.* WLOG $b > 1$, and suppose $f(b) = a \ge 1/b$ hence $f(a) = b$.
Assume that $ab > 1$; we show $a = b$. Note that for integers $m$ and $n$ with $a^m b^n \ge 1$, we must have
$$
a^m b^n = f(b)^m f(a)^n = f(a^m b^n) \ge \frac{1}{a^m b^n} \implies (ab)^{m+n} \ge 1
$$
and thus we have arrived at the proposition
$$
m + n < 0 \implies n \log_b a + m < 0
$$
for all integers $m$ and $n$. Due to the density of $\mathbb{Q}$ in the real numbers, this can only happen if $\log_b a = 1$ or $a = b$. $\square$
**Claim** — The function $f$ is continuous.
*Proof.* Indeed, it's equivalent to show $g(t) = \log f(e^t)$ is continuous, and we have that
$$
|g(t) - g(s)| = |\log f(e^{t-s})| = |t - s|
$$
since $f(e^{t-s}) = e^{\pm|t-s|}$. Therefore $g$ is Lipschitz. Hence $g$ continuous, and $f$ is too. $\square$
Finally, we have from $f$ multiplicative that
$$
f(2^q) = f(2)^q
$$
for every rational number $q$, say. As $f$ is continuous this implies $f(x) \equiv x$ or $f(x) \equiv 1/x$ identically (depending on whether $f(2) = 2$ or $f(2) = 1/2$, respectively).
Therefore, $a \diamond b = ab$ or $a \diamond b = a \div b$, as needed.
