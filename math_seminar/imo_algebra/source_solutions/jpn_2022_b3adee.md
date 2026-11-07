# jpn_2022_b3adee

JMO | Japan | 2022 | FIRST ROUND | 11

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2022_b3adee](https://mathnet.mit.edu/data_v2/full/japan/jpn_2022_b3adee.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

In the following, we denote $d = 100$ and let $f(0) = 0$. Note that $S = f(0) + f(1) + \dots + f(10^d - 1)$. For any integer $n$ such that $0 \le n \le 10^d$, there exists unique $(a_0, a_1, \dots, a_{d-1})$ with $0 \le a_i \le 9$ ($i = 0, 1, \dots, d-1$) such that
$$
n = a_0 + a_1 \cdot 10 + \dots + a_{d-1} \cdot 10^{d-1}.
$$
If $n > 0$,
$$
f(n) = (-1)^{a_0+a_1+\dots+a_{d-1}} (a_0 + a_1 \cdot 10 + \dots + a_{d-1} \cdot 10^{d-1})^d \quad (*)
$$

(and it is obvious to check it also holds for $n = 0$). Hence, $S$ equals to the sum of $(*)$ for all $(a_0, a_1, \dots, a_{d-1})$ with $0 \le a_i \le 9$ ($i = 0, 1, \dots, d-1$).
By multinomial theorem,
$$
(a_0 + a_1 \cdot 10 + \dots + a_{d-1} \cdot 10^{d-1})^d = \sum_d \sum_{b_0+\dots+d_{d-1}=d, b_i \ge 0} \frac{d!}{b_0!b_1!\dots b_{d-1}!} \prod_{b_i \ne 0} (a_i \cdot 10^i)^{b_i} \\
= \sum_d \sum_{b_0+\dots+d_{d-1}=d, b_i \ge 0} \frac{d!}{b_0!b_1!\dots b_{d-1}!} \left(\prod_{b_i \ne 0} 10^{ib_i}\right) \left(\prod_{b_i \ne 0} a_i^{b_i}\right).
$$
Since $\frac{d!}{b_0!b_1!\dots b_{d-1}!} \prod_{b_i \ne 0} 10^{ib_i}$ is independent of $(a_0, a_1, \dots, a_{d-1})$, it suffices to compute, for each $(b_0, b_1, \dots, b_{d-1})$,
$$
\sum_{a_0=0}^{9} \dots \sum_{a_{d-1}=0}^{9} (-1)^{a_0+a_1+\dots+a_{d-1}} \prod_{b_i \ne 0} a_i^{b_i}.
$$

In the case where $b_k \ne 0$ for some $0 \le k \le d-1$, it equals zero since
$$
\begin{aligned}
\sum_{a_k=0}^{9} \left( (-1)^{a_0+a_1+\dots+a_k+\dots+a_{d-1}} \prod_{b_i \ne 0} a_i^{b_i} \right)
&= \left( \sum_{a_k=0}^{9} (-1)^{a_0+a_1+\dots+a_k+\dots+a_{d-1}} \right) \prod_{b_i \ne 0} a_i^{b_i} \\
&= (1 \cdot 5 + (-1) \cdot 5) \prod_{b_i \ne 0} a_i^{b_i} \\
&= 0.
\end{aligned}
$$

In the case where $b_k \ne 0$ for all $k$, i.e. $b_0 = b_1 = \dots = b_{d-1} = 1$,
$$
(-1)^{a_0+a_1+\dots+a_{d-1}} \prod_{b_i \ne 0} a_i^{b_i} = (-1)^{a_0+a_1+\dots+a_{d-1}} \prod_{i=0}^{d-1} a_i = \prod_{i=0}^{d-1} ((-1)^{a_i} \cdot a_i).
$$

$$
\prod_{i=0}^{d-1} \left( \sum_{a_i=0}^{9} ((-1)^{a_i} \cdot a_i) \right) = (-5)^d.
$$

$b_0 = b_1 = \dots = b_{d-1} = 1$ implies
$$
\frac{d!}{b_0!b_1!\dots b_{d-1}!} \prod_{b_i \ne 0} 10^{ib_i} = d! \prod_{i=0}^{d-1} 10^i = d! \cdot 10^{\frac{d(d-1)}{2}},
$$
and hence
$$
S = d! \cdot 10^{\frac{d(d-1)}{2}} \cdot (-5)^d = 100! \cdot 2^{4950} \cdot 5^{5050}.
$$
This concludes that the answer is $\left\lfloor \frac{100}{5^1} \right\rfloor + \left\lfloor \frac{100}{5^2} \right\rfloor + 5050 = 5074$.
