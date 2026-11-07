# jpn_2024_eb9ad6

JMO | Japan | 2024 | First Round | 5

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2024_eb9ad6](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_eb9ad6.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: The 34th Japanese Mathematical Olympiad
- Subtitle: The First Round · The Final Round
- Year: 2024
- Organization: The Mathematical Olympiad Foundation of Japan
- Publisher: The Mathematical Olympiad Foundation of Japan
- Series: Japan Mathematical Olympiad
- Volume: 34
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

2519
Note that $[x] > x - 1$ for any real number $x$. In particular, for an integer $1 \le k \le 10$ we have $\lfloor \frac{n}{k} \rfloor > \frac{n}{k} - 1$, thus $k \lfloor \frac{n}{k} \rfloor > n - k$. Since both sides are integers, we have $k \lfloor \frac{n}{k} \rfloor \ge n - k + 1$, thus $\lfloor \frac{n}{k} \rfloor \ge \frac{n-k+1}{k}$. Since $0 < k \le n$ implies $\frac{n-k+1}{k} > 0$, multiplying both sides of $\lfloor \frac{n}{k} \rfloor \ge \frac{n-k+1}{k}$ for $k = 1, 2, \dots, 10$ yields
$$
\lfloor \frac{n}{1} \rfloor \lfloor \frac{n}{2} \rfloor \dots \lfloor \frac{n}{10} \rfloor \ge \frac{n}{1} \cdot \frac{n-1}{2} \dots \frac{n-9}{10} = \binom{n}{10}.
$$
Therefore the equation in the problem holds if and only if $\lfloor \frac{n}{k} \rfloor = \frac{n-k+1}{k}$ for all integers $1 \le k \le 10$.
If $\lfloor \frac{n}{k} \rfloor = \frac{n-k+1}{k}$ holds, $k$ divides $n-k+1$ because the right side is an integer. Conversely, if $k$ divides $n-k+1$ then $\lfloor \frac{n}{k} \rfloor = \lfloor \frac{n-k+1}{k} \rfloor + \frac{k-1}{k} = \frac{n-k+1}{k}$ holds. Therefore the equation $\lfloor \frac{n}{k} \rfloor = \frac{n-k+1}{k}$ holds if and only if $k$ divides $n-k+1$, that is, $n+1$ is a multiple of $k$.
Therefore, for an integer $n \ge 10$, the equation in the problem holds if and only if $n+1$ is a multiple of $k$ for any integer $1 \le k \le 10$, that is, $n+1$ is a common multiple of $1, 2, \dots, 10$. Since the least common multiple of $1, 2, \dots, 10$ is 2520, the smallest possible $n$ is $2520 - 1 = 2519$.
