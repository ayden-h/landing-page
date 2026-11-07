# chn_2023_b3eef6

CMO-China | China | 2023 | Day One | 1

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [chn_2023_b3eef6](https://mathnet.mit.edu/data_v2/full/china/chn_2023_b3eef6.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: China
- Title: The 39th Chinese Mathematical Olympiad
- Year: 2023
- Organization: Chinese Mathematical Olympiad
- Place: Wuhan, Hubei
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

The number $\lambda$ is $\frac{1}{1012}$.
The minimal such $\lambda$ is $\frac{1}{1012}$.
To see that $\lambda < \frac{1}{1012}$ does not work, we take $n = p^{2024}$ for some prime number $p$. Then when writing $n$ as the product of $2023$ integers, at least one of the integers is $p^\alpha$ for some $\alpha \ge 2$ (which is not a prime number); then $p^\alpha \ge p^2 = n^{\frac{1}{1012}} > n^\lambda$.
Now we prove that $\lambda = \frac{1}{1012}$ satisfies the condition of the problem. To start, we write $n$ as the product of its prime factors $n = p_1p_2\cdots p_r$ (allowing some $p_i$'s to be equal), where we order the primes so that $p_1 \ge p_2 \ge \cdots$.
Now starting from $p_1$, let $r_1 \ge 1$ be the smallest integer such that $x_1 = p_1p_2\cdots p_{r_1} > n^{1/2024}$. Note that this $x_1$ satisfies the condition of the problem, namely, if $r_1 = 1$, $x_1$ is a prime number; otherwise $r_1 \ge 2$, then we must have $p_1 \le n^{1/2024}$. This means that $p_r \le n^{1/2024}$; so
$$
x_1 = (p_1p_2\cdots p_{r-1})p_r \le n^{1/2024} \cdot n^{1/2024} = n^{1/1012},
$$
where the first inequality holds by minimality of $r_1$.
Next, let $r_2 \ge r_1 + 1$ be the smallest integer such that $x_2 = p_{r_1+1}\cdots p_{r_2} > n^{1/2024}$. The same argument as above shows that either $x_2$ is a prime number or $x_2 \le n^{1/1012}$.
Continue this process. If we run out of $p_i$'s before reaching $x_{2023}$, then set the rest of $x_j$ to be $1$, and then $n = x_1x_2\cdots x_{2023}$ gives the needed decomposition. Otherwise, we have constructed $x_1, x_2, \dots, x_{2022}$ satisfying the condition of the problem (and that each $x_i > n^{1/2024}$ by construction), then we must have
$$
x_{2023} := \frac{n}{x_1 \cdots x_{2022}} < \frac{n}{(n^{1/2024})^{2022}} = n^{1/1012}.
$$
The decomposition $n = x_1x_2\cdots x_{2023}$ satisfies the conditions of the problem.

## Supplied solution 2

The proof for that $\lambda < \frac{1}{1012}$ does not work is the same as Solution 1. We prove that $\lambda = \frac{1}{1012}$ satisfies the requirement. Let $n = p_1p_2\cdots p_r$ be the prime factorization of $n$ (where $p_1 \ge p_2 \ge \cdots \ge p_r$). For $i = 1, 2, \dots, 1012$, define
$$
y_i = \prod_{\substack{1 \le j \le r \\ j \equiv i \pmod{1012}}} p_j.
$$
Then $y_1 \ge y_2 \ge \cdots \ge y_{1012}$ and $y_1y_2\cdots y_{1012} = n$.
If $y_1 \le n^{1/1012}$, then let $x_1, \dots, x_{2023}$ be $y_1, y_2, \dots, y_{1012}$ plus $1011$ ones.
If $y_1 > n^{1/1012}$, since $y_{1012} \le n^{1/1012}$, suppose $y_k > n^{1/1012} \ge y_{k+1}$, then $1 \le k \le 1011$.
For $1 \le i \le k$, we have
$$
\frac{y_i}{p_i} \le y_{1012} \le n^{1/1012}.
$$
Let $x_1, x_2, \dots, x_{2023}$ be $\frac{y_1}{p_1}, \dots, \frac{y_k}{p_k}, y_{k+1}, \dots, y_{1012}, p_1, \dots, p_k$ and $1011 - k$ ones.

## Supplied solution 3

The proof for that $\lambda < \frac{1}{1012}$ does not work is the same as Solution 1. We prove that $\lambda = \frac{1}{1012}$ satisfies the requirement. Express $n$ as $n = x_1x_2\cdots x_{2023}$ such that

$x_1 + x_2 + \cdots + x_{2023}$ is minimized. (Since there are a finite number of ways to express this, such a representation must exist.) Next, we prove that every $x_i$ greater than $n^{1/1012}$ is a prime number.
We use proof by contradiction. Suppose $x_1 > n^{1/1012}$ and $x_1$ is not a prime number. Let $x_1 = ab$ where $a > 1$ and $b > 1$, and without loss of generality, assume $a \ge b$. Since
$$
x_2 \cdots x_{2023} = \frac{n}{x_1} < \frac{x_1^{1012}}{x_1} = x_1^{1011} = (\sqrt{x_1})^{2022} \le a^{2022},
$$
there exists an $x_i < a$. Assume without loss of generality that $x_2 < a$.
Express $n$ as $n = a \cdot b \cdot x_2 \cdot x_3 \cdots x_{2023}$. Since
$$
(ab + x_2 + x_3 + \cdots + x_{2023}) - (a + bx_2 + x_3 + \cdots + x_{2023}) = (b-1)(a-x_2) > 0,
$$
the expression $n = x_1x_2\cdots x_{2023}$ is not the one that minimizes $x_1+x_2+\cdots+x_{2023}$, which is a contradiction!
Therefore, $\lambda = \frac{1}{1012}$ satisfies the problem's conditions.

## Supplied solution 4

The proof for that $\lambda < \frac{1}{1012}$ does not work is the same as Solution 1. We prove that $\lambda = \frac{1}{1012}$ satisfies the requirement. Let $n = p_1p_2\cdots p_k$, where $p_1 \ge p_2 \ge \cdots \ge p_k$ are all the prime factors of $n$.
If $k \le 2023$, then express $n$ as the product of $p_1, p_2, \cdots, p_k$ and $2023-k$ ones.
If $k > 2023$, first express $n$ as $n = p_1p_2\cdots p_k$. Then, perform the following operation: in each step, select the smallest two factors and combine them into their product, continue this process until only $2023$ factors remain. In each step, as the current number of factors is $\ge 2024$, the product of the smallest two numbers will be $\le n^{2/2024} = n^{1/1012}$. This indicates that every "composite" number formed after each operation is $\le n^{1/1012}$.
Combining this with the fact that the initial numbers are primes, it can be concluded that when the operation ends, the $2023$ factors are either prime or do not exceed $n^{1/1012}$. Hence, $\lambda = \frac{1}{1012}$ satisfies the conditions of the problem.
