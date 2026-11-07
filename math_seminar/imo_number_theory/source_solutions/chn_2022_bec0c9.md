# chn_2022_bec0c9

IMO-TST | China | 2022 | Test 2 Day 1 | 3

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [chn_2022_bec0c9](https://mathnet.mit.edu/data_v2/full/china/chn_2022_bec0c9.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: China
- Title: 2022 China Team Selection Test for IMO
- Year: 2022
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

**Proof:** Consider the set of all positive integers that are coprime to $6$: $B = \{1, 5, 7, 11, 13, \dots\}$, it is obvious that the sum $f(k)$ of the smallest $k$ elements of $B$ satisfies
$$
f(k) = \begin{cases} \frac{3k^2}{2} & \text{if } k \text{ is even} \\ \frac{3k^2-1}{2} & \text{if } k \text{ is odd} \end{cases}, \qquad f(k+1) - f(k) = 3k + 1 \text{ or } 3k + 2.
$$
$$
f(0) = 0,\ f(1) = 1,\ f(2) = 6,\ f(3) = 13,\ f(4) = 24,\ f(5) = 37, \dots
$$
Every positive integer $a$ can be uniquely written as $a = 2^\alpha 3^\beta b$, with $b \in B$ and nonnegative integers $\alpha, \beta$. Denote $h(a) = b$ or say $b$ is the core of $a$. If $a_1, \dots, a_m$ are $m$ positive integers that cannot divide one another, and that all of their cores are $b$, then writing each $a_k = 2^{\alpha_k} 3^{\beta_k} b$ with $k = 1, \dots, m$, we must have that $\alpha_1, \dots, \alpha_m$ are pairwise distinct (otherwise two numbers $2^\alpha 3^\beta b$ and $2^\alpha 3^{\beta'} b$ must have division relations). We may put them in a sequence so that $\alpha_1 < \alpha_2 < \dots < \alpha_m$, then correspondingly we have $\beta_1 > \beta_2 > \dots > \beta_m \ge 0$, this time we get $a_k \ge 2^{k-1} 3^{m-k} b$. Moreover, the sum of these $m$ numbers
$$
a_1 + a_2 + \dots + a_m \ge 2^0 3^{m-1} b + 2^1 3^{m-2} b + \dots + 2^{m-1} 3^0 b = (3^m - 2^m)b.
$$
We consider the map from $A = \{a_1, a_2, \dots, a_n\}$ to $B$ by taking the cores, i.e. every $b \in B$ is the core for several numbers in $A$. Set
$$
B_k = \{b \in B : \#\{a \in A : h(a) = b\} \ge k\}.
$$
i.e. the numbers in $B_k$ are the core for at least $k$ numbers in $\{a_1, \dots, a_n\}$. Thus $B \supseteq B_1 \supseteq B_2 \supseteq \dots$, and the numbers in $B_k \setminus B_{k+1}$ are precisely the core for exactly $k$ numbers in $\{a_1, \dots, a_n\}$. We have
$$
n = \sum_{k=1}^{\infty} k \cdot |B_k \setminus B_{k+1}| = |B_1| + |B_2| + \dots
$$
We use $S(\cdot)$ to denote the sum of the elements in a set. We have:
$$
S(A) = a_1 + \dots + a_n \ge \sum_{k=1}^{\infty} (3^k - 2^k) \times S(B_k \setminus B_{k+1}) = \sum_{k=1}^{\infty} [(3^k - 2^k) - (3^{k-1} - 2^{k-1})] \times S(B_k)
$$
$$
S(A) \geq \sum_{k=1}^{\infty} (2 \times 3^{k-1} - 2^{k-1}) \times f(|B_k|)
$$
Define the sequence $c_k = 2 \times 3^{k-1} - 2^{k-1}$, e.g. $c_1 = 1$, $c_2 = 4$, $c_3 = 14$, $c_4 = 46$, $c_5 = 146$, ...
We turn to consider the optimization problem $\spadesuit$: under the assumption $x_1 + x_2 + \dots = n$ (with each $x_i$ nonnegative), minimize $T = c_1f(x_1) + c_2f(x_2) + \dots$.
Suppose that $X = (x_1, x_2, \dots, x_K, 0, 0, \dots)$ minimizes $T$, where $x_1 \ge x_2 \ge \dots \ge x_K \ge 1$, and $x_{K+1} = x_{K+2} = \dots = 0$.
If $K \le 2$, then
$$
T = c_1f(x_1) + c_2f(x_2) \ge \frac{3x_1^2-1}{2} + 4\frac{3x_2^2-1}{2} \ge \frac{6}{5}(x_1+x_2)^2 - \frac{5}{2} \ge 1.1n^2 - 2n.
$$
If $K \ge 3$, then $X$ being (one of) the minimizing points would mean:
* if we change $X$ to $X' = (x_1+1, x_2, \dots, x_{K-1}, x_K - 1, 0, \dots)$, $T$ does not decrease, i.e.
$$
0 \le \Delta T = c_1(f(x_1+1)-f(x_1)) - c_K(f(x_K)-f(x_K-1)) \le 3x_1+2 - c_K \Rightarrow c_K \le 3x_1+2;
$$
* if we change $X$ to $X'' = (x_1, x_2 + 1, \dots, x_{K-1}, x_K - 1, 0, \dots)$, then $T$ does not decrease, i.e.
$$
0 \le \Delta T = c_2(f(x_2+1)-f(x_2)) - c_K(f(x_K)-f(x_K-1)) \le 4(3x_2+2) - c_K \Rightarrow c_K \le 12x_2+8.
$$
So $n = x_1 + x_2 + \dots + x_K \ge x_1 + x_2 + 1 \ge \frac{c_K-2}{3} + \frac{c_K-8}{12} + 1 = \frac{5c_K-4}{12}$, we get
$$
c_1 + c_2 + \dots + c_K \le c_K \left(1 + \frac{1}{3} + \dots + \frac{1}{3^{K-1}}\right) \le \frac{12n+4}{5} \times \frac{3}{2} \le 4n.
$$
Thus, $T(X) = c_1f(x_1) + \dots + c_Kf(x_K) \ge c_1 \frac{3x_1^2-1}{2} + \dots + c_K \frac{3x_K^2-1}{2}$ and
$$
T(X) \ge \frac{3}{2}[c_1x_1^2 + c_2x_2^2 + \dots + c_Kx_K^2] - \frac{1}{2}[c_1 + c_2 + \dots + c_K] \ge \frac{3}{2} \frac{(x_1 + x_2 + \dots + x_K)^2}{\frac{1}{c_1} + \frac{1}{c_2} + \dots + \frac{1}{c_K}} - 2n.
$$
Since $c_{k+1} \ge 3c_k$ always holds, we have
$$
\frac{1}{c_1} + \frac{1}{c_2} + \dots + \frac{1}{c_K} \le 1 + \frac{1}{4} + \frac{1}{14} + \frac{1}{14 \times 3} + \frac{1}{14 \times 3^2} + \dots = 1 + \frac{1}{4} + \frac{1.5}{14} \le 1.36
$$
So
$$
T \ge \frac{3}{2} \frac{n^2}{1.36} - 2n > 1.1n^2 - 2n
$$
To sum up, the optimization problem $\spadesuit$ has minimum value $T_{\min} \ge 1.1n^2 - 2n$, and for the original question,
$$
S(A) \ge \sum_{k=1}^{\infty} c_k \times f(|B_k|) \ge 1.1n^2 - 2n.
$$
