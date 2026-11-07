# jpn_2021_aec1d9

JMO | Japan | 2021 | First Round | 9

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2021_aec1d9](https://mathnet.mit.edu/data_v2/full/japan/jpn_2021_aec1d9.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: Japan Mathematical Olympiad
- Subtitle: The 31st Japanese Mathematical Olympiad
- Year: 2021
- Organization: The Mathematical Olympiad Foundation of Japan
- Publisher: The Mathematical Olympiad Foundation of Japan
- Edition: 31st
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

$\boxed{3}$

For $1 \le i \le 2021$ and $1 \le j \le 2021$, let $(i, j)$ denote the cell in the $i$-th row and the $j$-th column, and let $f(i, j)$ denote the number filled in $(i, j)$. We also define $g(i, j)$ as
$$
g(i, j) = \begin{cases} f(i, j) & (i + j \text{ is even}), \\ 4 - f(i, j) & (i + j \text{ is odd}). \end{cases}
$$

It is easy to check that $g(i, j) \in \{1, 2, 3\}$ and $g$ satisfies, for $1 \le i \le 2020$ and $1 \le j \le 2020$,
$$
g(i+1, j) - g(i, j) = g(i+1, j+1) - g(i, j+1). \quad (*)
$$
Indeed, since $f(i, j) + f(i, j + 1) + f(i + 1, j) + f(i + 1, j + 1) = 8$, if $i + j$ is even,
$$
\begin{aligned}
g(i+1, j) - g(i, j) &= (4 - f(i+1, j)) - f(i, j) \\
&= f(i+1, j+1) - (4 - f(i, j+1)) \\
&= g(i+1, j+1) - g(i, j+1)
\end{aligned}
$$
and if $i + j$ is odd,
$$
\begin{aligned}
g(i+1, j) - g(i, j) &= f(i+1, j) - (4 - f(i, j)) \\
&= (4 - f(i+1, j+1)) - f(i, j+1) \\
&= g(i+1, j+1) - g(i, j+1).
\end{aligned}
$$
On the other hand, if we assign $g(i, j)$ for $1 \le i \le 2021$ and $1 \le j \le 2021$ in such a way that $g(i, j) \in \{1, 2, 3\}$ and $g$ satisfies (*),
$$
\tilde{f}(i, j) = \begin{cases} g(i, j) & (i + j \text{ is even}), \\ 4 - g(i, j) & (i + j \text{ is odd}). \end{cases}
$$
satisfies the restriction of the original problem. Hence, $A$ equals to the number of cases of defining $g(i, j)$ under the above condition.

Let $M$ and $m$ denote the maximum and the minimum of $\{g(1, 1), \dots, g(1, 2021)\}$, respectively. Having (*) for every $1 \le i \le 2020$ and $1 \le j \le 2020$ is equivalent to the condition that $g(k+1, \ell) - g(1, \ell)$ is constant for $1 \le \ell \le 2021$ for each $1 \le k \le 2020$. We denote this constant value by $d_k$. Since $1 \le g(i, j) \le 3$ for every $(i, j)$ is equivalent to $1 \le m + d_k$ and $M + d_k \le 3$, or $1 - m \le d_k \le 3 - M$, for every $1 \le k \le 2020$, there are $(3 + m - M)^{2020}$ possibilities for assigning $g(i, j)$ when $g(1, 1), \dots, g(1, 2021)$ are given.

* $M - m = 0$.

In this case we have $g(1, 1) = \dots = g(1, 2021)$ and there are only $3$ possibilities for $(g(1, 1), \dots, g(1, 2021))$. For each possibility, we have $3^{2020}$ ways of assigning the rest of $g(i, j)$, thus the number of cases is $3 \cdot 3^{2020} = 3^{2021}$.

* $M - m = 1$.

In this case we have $m = 1$ or $2$. For each $m$, we have $2^{2021} - 2$ possibilities for $(g(1, 1), \dots, g(1, 2021))$. Thus, the number of cases is $2 \cdot ((2^{2021} - 2) \cdot 2^{2020}) = 2^{4042} - 2^{2022}$.

* $M - m = 2$.

In this case we have $3^{2021} - 2 \cdot (2^{2021} - 2) - 3$ possibilities for $(g(1, 1), \dots, g(1, 2021))$. Thus, the number of cases is $(3^{2021} - 2 \cdot (2^{2021} - 2) - 3) \cdot 1^{2020} = 3^{2021} - 2 \cdot (2^{2021} - 2) - 3$.

$$
A = 3^{2021} + (2^{4042} - 2^{2022}) + (3^{2021} - 2 \cdot (2^{2021} - 2) - 3) = 2 \cdot 3^{2021} + 2^{4042} - 2^{2023} + 1.
$$

To obtain the remainder after dividing $A$ by $100$, we compute $A \pmod{4}$ and $A \pmod{25}$. Since $3^{2021} \equiv 3 \pmod{4}$, we have $A \equiv 2 \cdot 3 + 0 - 0 + 1 \equiv 3 \pmod{4}$. And since $2^{20} \equiv 3^{20} \equiv 1 \pmod{25}$ from Euler's totient theorem,
$$
A \equiv 2 \cdot 3 \cdot (3^{20})^{101} + 2^2 \cdot (2^{20})^{202} - 2^3 \cdot (2^{20})^{101} + 1 \equiv 6 + 4 - 8 + 1 \equiv 3 \pmod{25}.
$$
This concludes that $A \equiv 3 \pmod{100}$.
