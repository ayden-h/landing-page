# chn_2014_c8fce5

China-TST | China | 2014 | Day 2 | 4

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [chn_2014_c8fce5](https://mathnet.mit.edu/data_v2/full/china/chn_2014_c8fce5.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: China
- Title: 2014 China Team Selection Test
- Year: 2014
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

$$
((k-2)^2 + 1)xy = (x + y - k)^2 + 1, \qquad \textcircled{1}
$$
we prove ① has infinitely many positive odd solutions $(x, y)$.
Obviously $(1,1)$ is one positive odd solution, let $(x_1, y_1) = (1,1)$. Assume $(x_i, y_i)$ is one positive odd solution of ①, and $x_i \le y_i$, let $x_{i+1} = y_i$, $y_{i+1} = (k-1)(k-3)y_i + 2k - x_i$. Since ① can be written as
$$
x^2 - ((k-1)(k-3)y + 2k)x + (y-k)^2 + 1 = 0,
$$
by Vieta's theorem $(x_{i+1}, y_{i+1})$ is also one integer solution of ①. Since $x_i, y_i$ and $k$ are all positive odd integers, and $k \ge 5$, so $x_{i+1}$ is a positive odd integer, and
$$
y_{i+1} = (k-1)(k-3)y_i + 2k - x_i \equiv -x_i \equiv 1 \pmod{2},
$$
$y_{i+1} \ge 8y_i + 2k - x_i > y_i > 0$. Thus $(x_{i+1}, y_{i+1})$ is one positive odd solution of ①, and $x_i + y_i < x_{i+1} + y_{i+1}$. By $(x_1, y_1)$ and the construction above, we get a series of positive odd solutions of ①: $(x_i, y_i)$, $i=1,2,\dots$, such that $x_1 + y_1 < x_2 + y_2 < \dots$.
For any integer $i$ greater than $k$, $x_i + y_i > k$. Let $n = x_i + y_i - k$, $d_1 = x_i$, $d_2 = y_i$, then $n$ is a positive odd integer, and $d_1 + d_2 = n + k$. Since $(k-2)^2 + 1$ is even, we can show that $d_1, d_2$ are both divisors of $\frac{n^2+1}{2}$, and $d_1 + d_2 = n + k$. Thus such $n$ satisfies all the conditions, therefore there exist infinitely many positive odd integers $n$ satisfying the conditions.
