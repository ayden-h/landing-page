# apm_1989_7c3bdc

APMO | Asia Pacific Mathematics Olympiad (APMO) | 1989 |  | 2

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [apm_1989_7c3bdc](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1989_7c3bdc.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Asia Pacific Mathematics Olympiad (APMO)
- Title: Problems and Solutions
- Year: 1989
- Series: APMO
- Volume: 1989
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We can suppose without loss of generality that $a, b, c, n \geq 0$. Let $(a, b, c, n)$ be a solution with minimum sum $a+b+c+n$. Suppose, for the sake of contradiction, that $a+b+c+n>0$. Since $6$ divides $5 n^{2}$, $n$ is a multiple of $6$. Let $n=6 n_{0}$. Then the equation reduces to
$$
6 a^{2}+3 b^{2}+c^{2}=30 n_{0}^{2}.
$$
The number $c$ is a multiple of $3$, so let $c=3 c_{0}$. The equation now reduces to
$$
2 a^{2}+b^{2}+3 c_{0}^{2}=10 n_{0}^{2}.
$$
Now look at the equation modulo $8$:
$$
b^{2}+3 c_{0}^{2} \equiv 2\left(n_{0}^{2}-a^{2}\right) \quad(\bmod 8).
$$
Integers $b$ and $c_{0}$ have the same parity. Either way, since $x^{2}$ is congruent to $0$ or $1$ modulo $4$, $b^{2}+3 c_{0}^{2}$ is a multiple of $4$, so $n_{0}^{2}-a^{2}=(n_{0}-a)(n_{0}+a)$ is even, and therefore also a multiple of $4$, since $n_{0}-a$ and $n_{0}+a$ have the same parity. Hence $2(n_{0}^{2}-a^{2})$ is a multiple of $8$, and
$$
b^{2}+3 c_{0}^{2} \equiv 0 \quad(\bmod 8).
$$
If $b$ and $c_{0}$ are both odd, $b^{2}+3 c_{0}^{2} \equiv 4\ (\bmod 8)$, which is impossible. Then $b$ and $c_{0}$ are both even. Let $b=2 b_{0}$ and $c_{0}=2 c_{1}$, and we find
$$
a^{2}+2 b_{0}^{2}+6 c_{1}^{2}=5 n_{0}^{2}.
$$
Look at the last equation modulo $8$:
$$
a^{2}+3 n_{0}^{2} \equiv 2\left(c_{1}^{2}-b_{0}^{2}\right) \quad(\bmod 8).
$$
A similar argument shows that $a$ and $n_{0}$ are both even.
We have proven that $a, b, c, n$ are all even. Then, dividing the original equation by $4$ we find
$$
6\left(6(a / 2)^{2}+3(b / 2)^{2}+(c / 2)^{2}\right)=5(n / 2)^{2},
$$
and we find that $(a / 2, b / 2, c / 2, n / 2)$ is a new solution with smaller sum. This is a contradiction, and the only solution is $(a, b, c, n)=(0,0,0,0)$.
