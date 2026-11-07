# vnm_2016_afd01e

VMO | Vietnam | 2016 | Day 1 | 2

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [vnm_2016_afd01e](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2016_afd01e.json.gz)

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

a.
It is obvious that $1 \le \frac{2n^2 + 1}{n^2 - n + 1} \le 2$ for all $n \in \mathbb{Z}^+$. Hence, $0 \le a_n \le \ln 2 < 1$ and $\lfloor a_n \rfloor = 0$. It follows that $\{a_n\} = a_n$ and
$$
\lim_{n \to \infty} \{a_n\} = \lim_{n \to \infty} a_n = \lim_{n \to \infty} \ln \frac{2n^2 + 1}{n^2 + n + 1} = \ln 2.
$$
Therefore, there exists a positive integer $n_0$ such that
$$
\{a_n\} > \ln 2 - \frac{1}{2016}, \forall n \ge n_0.
$$
Then by direct calculation, it deduces that for $n > n_0$,
$$
\{a_n\} = a_n > \ln 2 - \frac{1}{2016} > \frac{1}{2}.
$$

b.
$$
\lim_{n \to \infty} (b_n - b_{n-1}) = \lim_{n \to \infty} \ln \frac{(2n^2 + 1)(n^2 + n + 1)}{(2n^2 - 4n + 3)(n^2 - n + 1)} = 0.
$$
Back to our problem, assume that there exists finite values of $n$ that $\{b_n\} < \frac{1}{2016}$. It follows that there exists a positive integer $n_0$ that $\{b_n\} \ge \frac{1}{2016}$ for all $n$. Because $\lim_{n \to \infty} (b_n - b_{n-1}) = 0$, it implies that there exists a positive integer $n_1$ that
$$
b_n - b_{n-1} < \frac{1}{2016}
$$
for all $n \ge n_1$. Because $(b_n)$ is an increasing sequence and $\lim_{n \to \infty} b_n = +\infty$, it follows that there exists infinite values of $n > \max\{n_0, n_1\}$ which $[b_n] - [b_{n-1}] = 1$. Consider such values of $n$, by the above inequality, we obtain
$$
[b_n] - [b_{n-1}] + \{b_n\} - \{b_{n-1}\} < \frac{1}{2016}
$$
or
$$
\{b_{n-1}\} > \{b_n\} + \frac{2015}{2016}
$$
Notice that $\{b_n\} \ge \frac{1}{2016}$, thus $\{b_{n-1}\} > 1$. This contradiction finishes the given problem. $\square$
