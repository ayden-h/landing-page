# jpn_2021_ce7bea

JMO | Japan | 2021 | First Round | 4

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2021_ce7bea](https://mathnet.mit.edu/data_v2/full/japan/jpn_2021_ce7bea.json.gz)

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

$3 \cdot 2^{2021} + 3$

For integers $n = 0, \dots, 2021$, let $a \le b \le c$ be three numbers on the blackboard after the procedure is done $n$ times and let $p_n = c - b$, $q_n = b - a$. Here $n = 0$ means the initial status. When the procedure is done once, three numbers $a \le b \le c$ are replaced with $\frac{a+b}{2} \le \frac{a+c}{2} \le \frac{b+c}{2}$ hence $p_{n+1} = \frac{b-a}{2} = \frac{q_n}{2}$, $q_{n+1} = \frac{c-b}{2} = \frac{p_n}{2}$ holds. Therefore $p_{2021} = \frac{q_0}{2^{2021}}$, $q_{2021} = \frac{p_0}{2^{2021}}$. Initial three numbers are distinct thus neither of $p_0, q_0$ is $0$ and then neither of $p_{2021}, q_{2021}$ is $0$. All three numbers after $2021$ procedures are positive integers hence $p_{2021} \ge 1$, $q_{2021} \ge 1$ and $p_0 \ge 2^{2021}$, $q_0 \ge 2^{2021}$. The minimum number of initial three numbers is greater than or equal to $1$ thus the sum of initial three numbers is greater than or equal to $1 + (1 + 2^{2021}) + (1 + 2 \cdot 2^{2021}) = 3 \cdot 2^{2021} + 3$.

We show $1$, $1 + 2^{2021}$, $1 + 2 \cdot 2^{2021}$ satisfy the condition of initial three numbers. Discussion above shows $p_{2021} = 1$, $q_{2021} = 1$. The sum of three numbers is kept unchanged by the procedure thus the sum is $3 \cdot 2^{2021} + 3$ after $2021$ procedures. Therefore three numbers after $2021$ procedures are $2^{2021}$, $2^{2021} + 1$, $2^{2021} + 2$ and these are all integers. Hence the answer is $3 \cdot 2^{2021} + 3$.
