# usa_2019_afbc19

IMO-TST | United States | 2019 | Day 2 | TSTST 4

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [usa_2019_afbc19](https://mathnet.mit.edu/data_v2/full/united-states/usa_2019_afbc19.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: United States
- Title: USA TSTST 2019 Solutions
- Subtitle: TST Selection Test
- Year: 2019
- Authors: Bhattacharya, Ankan; Chen, Evan

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

The answer is $C = \frac{50}{51}$. The lower bound is obtained if we have $51$ coins of value $\frac{1}{51}$ and $49$ coins of value $1$. We now present two (similar) proofs that this $C = \frac{50}{51}$ suffices.

**First proof (original)** Let $a_1 \le \dots \le a_{100}$ denote the values of the coins in ascending order. Since the $51$ coins $a_{50}, \dots, a_{100}$ are worth at least $51a_{50}$, it follows that $a_{50} \le \frac{50}{51}$; likewise $a_{51} \ge \frac{1}{51}$.
We claim that choosing the stacks with coin values
$$
a_1, a_3, \dots, a_{49}, a_{52}, a_{54}, \dots, a_{100}
$$
and
$$
a_2, a_4, \dots, a_{50}, a_{51}, a_{53}, \dots, a_{99}
$$
works. Let $D$ denote the (possibly negative) difference between the two total values. Then
$$
\begin{aligned}
D &= (a_1 - a_2) + \dots + (a_{49} - a_{50}) - a_{51} + (a_{52} - a_{53}) + \dots + (a_{98} - a_{99}) + a_{100} \\
&\le 25 \cdot 0 - \frac{1}{51} + 24 \cdot 0 + 1 = \frac{50}{51}.
\end{aligned}
$$
Similarly, we have
$$
\begin{aligned}
D &= a_1 + (a_3 - a_2) + \dots + (a_{49} - a_{48}) - a_{50} + (a_{52} - a_{51}) + \dots + (a_{100} - a_{99}) \\
&\ge 0 + 24 \cdot 0 - \frac{50}{51} + 25 \cdot 0 = -\frac{50}{51}.
\end{aligned}
$$
It follows that $|D| \le \frac{50}{51}$, as required.


**Second proof (Evan Chen)** Again we sort the coins in increasing order $0 < a_1 \le a_2 \le \dots \le a_{100} \le 1$. A large gap is an index $i \ge 2$ such that $a_i > a_{i-1} + \frac{50}{51}$; obviously there is at most one such large gap.
**Claim** — If there is a large gap, it must be $a_{51} > a_{50} + \frac{50}{51}$.
*Proof*. If $i < 50$ then we get $a_{50}, \dots, a_{100} > \frac{50}{51}$ and the sum $\sum_{1}^{100} a_i > 50$ is too large. Conversely if $i > 50$ then we get $a_1, \dots, a_{i-1} < \frac{1}{51}$ and the sum $\sum_{1}^{100} a_i < 1/51 \cdot 51 + 49$ is too small. $\square$
Now imagine starting with the coins $a_1, a_3, \dots, a_{99}$, which have total value $S \le 25$. We replace $a_1$ by $a_2$, then $a_3$ by $a_4$, and so on, until we replace $a_{99}$ by $a_{100}$. At the end of the process we have $S \ge 25$. Moreover, since we did not cross a large gap at any point, the quantity $S$ changed by at most $C = \frac{50}{51}$ at each step. So at some point in the process we need to have $25 - C/2 \le S \le 25 + C/2$, which proves $C$ works.

