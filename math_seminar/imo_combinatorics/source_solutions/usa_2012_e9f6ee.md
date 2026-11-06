# usa_2012_e9f6ee

IMO-TST | United States | 2012 | TST 2012 Problems | 3.

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [usa_2012_e9f6ee](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_e9f6ee.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: United States
- Title: USA and International Mathematical Olympiads 2012-2013
- Editors: Feng, Zuming; Sun, Yi

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We claim there do exist such integers $a, b, c$.

Note that $(a_1, b_1, c_1) = (1, 1, 1)$ satisfy the given equation. For $n > 1$, define $(a_{n+1}, b_{n+1}, c_{n+1})$ by
$$
(a_{n+1}, b_{n+1}, c_{n+1}) = (a_n + 2c_n + 2b_n, b_n + a_n + 2c_n, c_n + b_n + a_n).
$$
It is not hard to verify algebraically that
$$
a_{n+1}^3 + 2b_{n+1}^3 + 4c_{n+1}^3 - 6a_{n+1}b_{n+1}c_{n+1} = a_n^3 + 2b_n^3 + 4c_n^3 - 6a_n b_n c_n,
$$
which shows that $(a_n, b_n, c_n)$ satisfy the given equation for all $n \ge 1$. Moreover, notice that $a_{n+1} > a_n$, $b_{n+1} > b_n$, and $c_{n+1} > c_n$ for all $n \ge 1$; this implies that for sufficiently large $n$ we will have $a_n, b_n, c_n > 2010$, yielding the desired result.

