# apm_2008_eadb1c

APMO | Asia Pacific Mathematics Olympiad (APMO) | 2008 |  | Problem 5

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [apm_2008_eadb1c](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2008_eadb1c.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Asia Pacific Mathematics Olympiad (APMO)
- Title: XX Asian Pacific Mathematics Olympiad
- Year: 2008

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Suppose that two sets are equal. Then $\operatorname{gcd}(b, c) = 1$ and the polynomial
$$
f(x) := \left(1 + x^{b} + x^{2b} + \cdots + x^{a b}\right) - \left(1 + x + x^{2} + \cdots + x^{a-1} + x^{a}\right)
$$
is divisible by $x^{c} - 1$. (This is because: $m = n + c q \Longrightarrow x^{m} - x^{n} = x^{n + c q} - x^{n} = x^{n}(x^{c q} - 1)$ and $\left(x^{c q} - 1\right) = \left(x^{c} - 1\right)\left(\left(x^{c}\right)^{q-1} + \left(x^{c}\right)^{q-2} + \cdots + 1\right)$.) From
$$
f(x) = \frac{x^{(a+1) b} - 1}{x^{b} - 1} - \frac{x^{a+1} - 1}{x - 1} = \frac{F(x)}{(x - 1)(x^{b} - 1)},
$$
where $F(x) = x^{a b + b + 1} + x^{b} + x^{a+1} - x^{a b + b} - x^{a + b + 1} - x$, we have
$$
F(x) \equiv 0 \quad (\bmod x^{c} - 1)
$$
Since $x^{c} \equiv 1 \ (\bmod x^{c} - 1)$, we may conclude that
$$
\begin{equation*}
\{a b + b + 1, b, a + 1\} \equiv \{a b + b, a + b + 1, 1\} \quad (\bmod c) \tag{$\dagger$}
\end{equation*}
$$
Thus,
$$
b \equiv a b + b, a + b + 1 \quad \text{or} \quad 1 \quad (\bmod c)
$$
But neither $b \equiv 1 (\bmod c)$ nor $b \equiv a + b + 1 (\bmod c)$ are possible by the given conditions. Therefore, $b \equiv a b + b (\bmod c)$. But this is also impossible because $\operatorname{gcd}(b, c) = 1$.
