# usa_2008_cbf07d

IMO-TST | United States | 2008 | TST 2008 Problems | 5

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [usa_2008_cbf07d](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_cbf07d.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: United States
- Title: USA and International Mathematical Olympiads 2007-2008
- Editors: Feng, Zuming; Sun, Yi
- Organization: University of Nebraska-Lincoln

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Define $d(i, j) = (a_i - a_j)^2 + (b_i - b_j)^2$. Notice that
$$
(a_n - a_{n-1})^2 + (a_n - a_{n-2})^2 - (a_{n-1} - a_{n-2})^2 = 2(a_n - a_{n-1})(a_n - a_{n-2})
$$
and
$$
(b_n - b_{n-1})^2 + (b_n - b_{n-2})^2 - (b_{n-1} - b_{n-2})^2 = 2(b_n - b_{n-1})(b_n - b_{n-2}).
$$
Adding these two equations and using the given implies that
$$
d(n, n-1) + d(n, n-2) - d(n-1, n-2) = 0,
$$
hence
$$
d(n, n-1) = d(n-1, n-2) - d(n, n-2) \le d(n-1, n-2),
$$
where equality holds if and only if $a_n = a_{n-2}$ and $b_n = b_{n-2}$. Therefore, the sequence
$$
\{d(n, n-1)\}_{n=2}^{\infty} = (d(2, 1), d(3, 2), d(4, 3), \dots)
$$
is nonincreasing. Since all the terms of this sequence are nonnegative integers, the sequence must eventually become constant: $d(n, n-1) = d(n-1, n-2)$ for all sufficiently large $n$, which in particular implies $a_n = a_{n-2}$ for all sufficiently large $n$. So whenever $n$ is large enough, we have
$$
a_{n+2008} = a_{n+2006} = a_{n+2004} = \dots = a_n.
$$

## Supplied solution 2

(Based on work by Palmer Mebane) Let $x_n = a_n - a_{n-1}$ and $y_n = b_n - b_{n-1}$. Then the given equation reads
$$
x_n(x_n + x_{n-1}) + y_n(y_n + y_{n-1}) = 0.
$$
To see this, note that $0 \le (x_{n-1} + x_n)^2 + (y_{n-1} + y_n)^2$, with equality if and only if $x_n = -x_{n-1}$ and $y_n = -y_{n-1}$. Expanding and using the given equation we obtain
$$
0 = 2x_n(x_n + x_{n-1}) + 2y_n(y_n + y_{n-1}) \le (x_{n-1} + x_n)^2 + (y_{n-1} + y_n)^2
$$
or
$$
x_n^2 + y_n^2 \le x_{n-1}^2 + y_{n-1}^2,
$$
with equality if and only if $x_n = -x_{n-1}$ and $y_n = -y_{n-1}$. Thus we have the claim.

Therefore, because $x_n^2 + y_n^2 \ge 0$ is an integer, by the well-ordering principle, $x_n^2 + y_n^2 < x_{n-1}^2 + y_{n-1}^2$ can only hold finitely many times. Thus there is a $k$ such that for all $n > k$, $x_n = -x_{n-1}$ and $y_n = -y_{n-1}$. This gives us the desired $k$ such that $a_k = a_{k+2008}$.

