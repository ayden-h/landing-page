# chn_2025_2bb7dd

IMO-TST | China | 2025 | Test 3 · Day 1 | Problem 1.

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [chn_2025_2bb7dd](https://mathnet.mit.edu/data_v2/full/china/chn_2025_2bb7dd.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: China
- Title: 2025 International Mathematical Olympiad China National Team Selection Test
- Year: 2025
- Organization: International Mathematical Olympiad China
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

**Proof:** We first prove a lemma.
**Lemma:** For integers $m \ge 2$, $s \ge 1$, and a sequence $1 = x_1 < \dots < x_s$ where every sum $\sum_{1 \le j \le m} x_{i_j}$ ($1 \le i_1 \le \dots \le i_m \le s$) is square-free, there exists an integer $x > x_s$ such that:
* $x$ is coprime with each $x_i$ ($1 \le i \le s$)
* Every sum $(m-t)x + \sum_{1 \le j \le t} x_{i_j}$ ($0 \le t \le m-1$, $1 \le i_1 \le \dots \le i_t \le s$) is square-free
**Proof of Lemma:** Take $B > 1$ such that:
$$
c_B := \prod_{p < B} \left(1 - \frac{1}{p}\right)^{-1} > m \cdot 2^{m+s}.
$$
Let
$$
d_B = \prod_{p \le B} p, \quad M_0 = \prod_{1 \le k \le 2^{m+s} x_s} k, \quad M = d_B M_0.
$$
Consider $x = yM^2 + x_1$ ($1 \le y \le M^2$). Clearly, $x$ is coprime with each $x_i$ ($1 \le i \le s$).
Note that
$$
(m-t)x + \sum_{1 \le j \le t} x_{i_j} \le mx \le m(M^4 + 1) < (mM^2)^2.
$$
If $q^2 \mid (m-t)x + \sum_{1 \le j \le t} x_{i_j}$, then $q < mM^2$.
If $q \nmid M$, clearly $(m-t)x + \sum_{1 \le j \le t} x_{i_j}$ is not divisible by $q^2$. For primes $q < mM^2$ with $q \nmid M$ (so $q > 2^{m+s}x_s$), let $X_q$ be the set of integers $1 \le y \le M^2$ where some sum $(m-t)x + \sum_{1 \le j \le t} x_{i_j}$ is divisible by $q^2$.
The number of possible index sets is at most $2^{s+m-2}$, so
$$
|X_q| \le 2^{m+s-2} \left( \frac{M^2}{q^2} + 1 \right).
$$
For $2^{m+s}x_s < q \le M$:
$$
|X_q| \le 2^{m+s-1} \frac{M^2}{q^2};
$$
---

For $M < q \le mM^2$:
$$
|X_q| \le 2^{m+s-1}.
$$
Thus,
$$
\begin{aligned} |\bigcup X_q| &\le 2^{m+s-1} M^2 \sum_{q>2^{m+s}x_s} \frac{1}{q^2} + 2^{m+s-1}(\pi(mM^2) - \pi(M)) \\ &\le \frac{2^{m+s-1}}{2^{m+s}x_s} M^2 + \frac{m \cdot 2^{m+s-1}}{c_B} M^2 < M^2. \end{aligned}
$$
Since we have used $d_B \mid M$, it follows that
$$
\pi(mM^2) - \pi(M) \le (mM^2 - M) \prod_{p \le B} \left(1 - \frac{1}{p}\right) < c_B^{-1} mM^2.
$$
Now choose an integer $y$ such that $1 \le y \le M$ and
$$
y \notin \bigcup_{\substack{q<mM^2 \\ q \nmid M}} X_q,
$$
then $x = yM^2 + x_1$ will satisfy the requirements.
Now the main proof. If $m$ has a square factor $p^2$, by pigeonhole principle there exist $m$ elements $a_{i_1}, \dots, a_{i_m}$ with $a_{i_1} \equiv \dots \equiv a_{i_m} \pmod{p^2}$, making their sum divisible by $p^2$.
If $m$ is square-free, construct $A = \{a_i\}$ inductively starting with $a_1 = 1$. By the lemma, we can find pairwise coprime integers $1 = a_1 < a_2 < \dots$ where all $m$-term sums are square-free. Then all $m$-term products are also square-free since the $a_i$ are pairwise coprime. $\square$

