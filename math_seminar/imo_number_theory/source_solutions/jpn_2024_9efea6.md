# jpn_2024_9efea6

JMO | Japan | 2024 | Final Round | 2

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2024_9efea6](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_9efea6.json.gz)

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

We prove that the function $f(n) = n$ is the unique function satisfying the condition in the problem. It is easy to see that this $f$ satisfies the condition in the problem.

Suppose that $f$ is the function that satisfies the condition in the problem. First, for any positive integer $k$, we prove that $f(k)$ is a multiple of $k$. Let $r$ be the remainder when dividing $f(k)$ by $k$. Substituting $m = k$ and $n = k - r + 1$ into the equation in the problem, we obtain
$$
\operatorname{lcm}(k, f(k + f(k - r + 1))) = \operatorname{lcm}(f(k), f(k) + k - r + 1).
$$
Therefore, $\operatorname{lcm}(f(k), f(k) + k - r + 1)$ is a multiple of $k$. Here, $f(k) + k - r + 1$ leaves a remainder of $1$ when divided by $k$, and hence, $f(k) + k - r + 1$ is coprime to $k$. Therefore, we conclude that $f(k)$ is a multiple of $k$.

Let $m$ be a positive integer. We prove that $f(m) = m$. Substituting $n = f(m)$ into the equation in the problem, we get
$$
\operatorname{lcm}(m, f(m + f(f(m)))) = \operatorname{lcm}(f(m), 2f(m)) = 2f(m).
$$
Therefore, $2f(m)$ is a multiple of $f(m + f(f(m)))$. Since $f(m + f(f(m)))$ is a multiple of $m + f(f(m))$, $2f(m)$ is a multiple of $m + f(f(m))$. Note that we have
$$
2f(m) \le 2f(f(m)) < 2(m + f(f(m))).
$$
Here, the first inequality follows from the fact that $f(f(m))$ is a multiple of $f(m)$. Therefore, we conclude that $2f(m) = m + f(f(m))$. Since
$$
f(f(m)) = 2f(m) - m < 2f(m)
$$
and $f(f(m))$ is a multiple of $f(m)$, we conclude that $f(f(m)) = f(m)$. Hence, we have $2f(m) = m + f(m)$, and hence $f(m) = m$. We complete the proof.
