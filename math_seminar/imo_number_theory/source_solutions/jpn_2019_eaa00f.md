# jpn_2019_eaa00f

JMO | Japan | 2019 | Problems | 1

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2019_eaa00f](https://mathnet.mit.edu/data_v2/full/japan/jpn_2019_eaa00f.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: The 29th Japanese Mathematical Olympiad
- Subtitle: The First Round, The Final Round
- Year: 2019
- Organization: The Mathematical Olympiad Foundation of Japan
- Publisher: The Mathematical Olympiad Foundation of Japan
- Series: Japan Mathematical Olympiad

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $N = |b^2 - c^2|$. Then, from $N^2 = a^2 + b + 3 \ge 1 + 1 + 3 = 5$ it follows that $N \ge 3$. In particular, since $b \ne c$, we get
$$
N = |b + c||b - c| \ge (b + 1) \cdot 1 = b + 1,
$$
so we have $b \le N - 1$. Since from $a^2 < N^2$ we have $a \le N - 1$, we get
$$
(1) \quad 0 = N^2 - (a^2 + b + 3) \ge N^2 - (N - 1)^2 - b - 3 = 2N - b - 4 \ge N - 3,
$$
showing $N \le 3$. As we have seen in the beginning that $N \le 3$, we get $N = 3$. But, then we have = throughout the inequalities (1), and thus, we get $a = N - 1 = 2$, $b = N - 1 = 2$, which, in turn implies $9 = N^2 = |b^2 - c^2|^2 = (c^2 - 4)^2$ holds. Thus, we have $c^2 = 1, 7$. Since $c$ is a positive integer, we get $c = 1$. Therefore, the answer we seek for the problem is $(a, b, c) = (2, 2, 1)$.
