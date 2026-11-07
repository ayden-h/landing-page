# jpn_2008_babc4b

JMO | Japan | 2008 | First Stage | 9

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2008_babc4b](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_babc4b.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: Japan Mathematical Olympiad
- Subtitle: The 18 Japanese Mathematical Olympiad: The First Round, The Final Round And The 6 Japanese Junior Mathematical Olympiad
- Year: 2008
- Organization: The Mathematical Olympiad Foundation of Japan
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $S = x_1 + x_2 + \dots + x_{2008}$. Since $x_1^2 = |x_1|^2 = 999^2$, and $x_n^2 = |x_{n-1} + 1|^2 = (x_{n-1} + 1)^2$ for $2 \le n \le 2008$, we have
$$
\begin{aligned}
x_1^2 + x_2^2 + \dots + x_{2008}^2 &= 999^2 + (x_1 + 1)^2 + \dots + (x_{2007} + 1)^2 \\
&= (x_1^2 + \dots + x_{2007}^2) + 2(x_1 + \dots + x_{2007}) + 2007 + 999^2 \\
&= (x_1^2 + \dots + x_{2007}^2) + 2(S - x_{2008}) + 1000008,
\end{aligned}
$$
from which we obtain
$$
2S = x_{2008}^2 + 2x_{2008} - 1000008 = (x_{2008} + 1)^2 - 1000009.
$$
Because $|x_n| = |x_{n-1} + 1|$ is satisfied, the even-odd parity of $x_n$ is different from that of $x_{n-1}$, namely, the even-odd parity of $x_n$ changes as $n$ increases by $1$. As $x_1$ is an odd number, $x_{2008}$ is even, and hence, $(x_{2008} + 1)^2 \ge 1$. Consequently, we have $S \ge \frac{1-1000009}{2} = -500004$.
On the other hand, if we set
$$
x_n = n - 1000 \quad (1 \le n \le 1000); \quad = -1 \quad (1001 \le n \le 2008, \text{ and $n$ is odd}); \\
= 0 \quad (1001 \le n \le 2008, \text{ and $n$ is even.})
$$
then this choice of $x_1, \dots, x_{2008}$ satisfies the conditions of the problem, and since $x_{2008} = 0$ for this choice, we get $S = -500004$. Therefore, the minimum value that $S = x_1 + \dots + x_{2008}$ can take is $-500004$.
