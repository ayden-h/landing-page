# chn_2024_cc0bb9

IMO-TST | China | 2024 | Test 3 Day 1 | 2

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [chn_2024_cc0bb9](https://mathnet.mit.edu/data_v2/full/china/chn_2024_cc0bb9.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: China
- Title: The 65th IMO China National Team Selection Test
- Year: 2024
- Organization: China National Team
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

*Proof.* We will show that $\alpha = 2 - \sqrt{2}$ satisfies the requirement. We will prove this in two steps.

First, we prove that $r_n \ge \alpha n - 4$. For this, we only need to consider the case where $n > 4$. Let $m = \lfloor \frac{n}{\sqrt{2}} \rfloor < n$, and let $d = n - m$. Consider an $n$-good set $S$ with $m$ elements, and let the complement of $S$ be $S^c = \{1, 2, \dots, n\} \setminus S = \{a_1, a_2, \dots, a_d\}$, where $a_1 < a_2 < \dots < a_d$. For any $1 \le i \le d$, we claim that $a_i \le 2i - 1$. In fact, if $a_i \ge 2i$, then among the pairs $(1, a_i - 1)$, $(2, a_i - 2)$, \dots, $(i, a_i - i)$, at least one pair would have both numbers in $S$, which contradicts the condition for $S$ being an $n$-good set. (If $a_i = 2i$, the last pair has equal numbers, but this does not affect the proof.) Therefore,
$$
\sum_{x \in S} x = \frac{n(n+1)}{2} - \sum_{x \in S^c} x \ge \frac{n(n+1)}{2} - (1 + 3 + \dots + (2d - 1)) = \frac{n(n+1)}{2} - d^2.
$$
Thus,
$$
r_n \ge \frac{\frac{n(n+1)}{2} - d^2}{n-d} = (n+d) - \frac{n(n-1)}{2(n-d)} = 2n - m - \frac{n(n-1)}{2m} \quad (3)
$$
$$
> 2n - \left(m + \frac{n^2}{2m}\right) > 2n - \sqrt{2n} - 1 = \alpha n - 1, \quad (4)
$$
where the last inequality holds because $m + \frac{n^2}{2m}$ is minimized at $m = \frac{n}{\sqrt{2}}$, with rounding causing at most an error of 1.

Next, we prove that $r_n \le \alpha n + 100$. For this, we only need to consider the case where $n > 100$. We discuss several cases.

**Case 1:** If $m = n$, $\{1, 2, \dots, n\}$ is an $n$-good set, with an arithmetic mean of $\frac{n+1}{2} < \alpha n + 4$.

**Case 2:** If $m \le \sqrt{n} - 1$, let $k = \lfloor \frac{n+1}{m+1} \rfloor$, then $(m+1)k \ge n+1 > n$, while
$$
mk \le m \cdot \frac{m+n+1}{m+1} = \frac{mn+m^2+m}{m+1} \le \frac{mn+n}{m+1} = n.
$$
Thus, $\{k, 2k, \dots, mk\}$ is an $n$-good set with $m$ elements, and its arithmetic mean is
$$
\frac{m+1}{2} \cdot k \le \frac{m+1}{2} \cdot \frac{m+n+1}{m+1} = \frac{n+m+1}{2} \le \frac{n+\sqrt{n}}{2} \le \frac{11n}{20} < \alpha n.
$$

**Case 3:** If $\sqrt{n} - 1 < m \le n - 1$, let $\lfloor \frac{n}{k} \rfloor \le m < \lfloor \frac{n}{k-1} \rfloor$, where $k \ge 2$. We first choose all multiples of $k$ from $\{1, 2, \dots, n\}$ (a total of $\lfloor \frac{n}{k} \rfloor$ elements), then choose the remaining $m - \lfloor \frac{n}{k} \rfloor$ elements that have the same remainder $r$ modulo $k$ (where $r \in \{1, 2, \dots, k-1\}$ and $r \equiv n+1 \pmod{k}$) or $r \equiv n+2 \pmod{k}$). When $k=2$, the unchosen numbers are just a few starting odd numbers, and from the inequality (4), it is easy to see that the chosen numbers form an $n$-good set.

When $k \ge 3$, $m \le \lfloor \frac{n}{k} \rfloor + \lfloor \frac{n}{2k} \rfloor$. This is because
$$
\text{For } k \ge 4, \left\lfloor \frac{n}{k} \right\rfloor + \left\lfloor \frac{n}{2k} \right\rfloor > \frac{3n}{2k} - 2 = \frac{n}{k-1} + \frac{(k-3)n}{2k(k-1)} - 2 \ge \frac{n}{k-1} + \frac{n}{24} - 2 > \frac{n}{k-1},
$$
$$
\text{For } k \ge 3, \left\lfloor \frac{n}{k} \right\rfloor + \left\lfloor \frac{n}{2k} \right\rfloor > \frac{n}{2} - 2.
$$
Therefore, the chosen numbers modulo $k$ are greater than $n - \lfloor \frac{n}{2k} \rfloor \cdot k \ge \frac{n}{2}$, so any two chosen numbers sum to more than $n$, indicating that the chosen numbers form an $n$-good set. Let the multiples of $k$ be $a = \lfloor \frac{n}{k} \rfloor$, then the numbers with the same remainder $r$ modulo $k$ have $m - a$ elements, and their mean does not exceed
$$
\begin{aligned}
& \frac{1}{m} \left( \frac{ka(a+1)}{2} + (m-a)(n+2) - \frac{k(m-a)(m-a+1)}{2} \right) \\
&= n + 2 + \left(a - \frac{1}{2}\right)k - \left(\frac{km}{2} + \frac{(n+k+2)a}{m}\right) \\
&\le n + 2 + \left(a - \frac{1}{2}\right)k - \sqrt{2ak(n+k+2)} \\
&< 2n + 2 - \sqrt{2(n-k+1)(n+k-1)} \\
&= 2n + 2 - \sqrt{2(n^2 - (k-1)^2)} \\
&\le 2n + 2 - \sqrt{2(n^2 - n)} < \alpha n + 4.
\end{aligned}
$$
Therefore, the arithmetic mean of the elements in the above $n$-good set does not exceed $\alpha n + 4$.

In conclusion, $\alpha = 2 - \sqrt{2}$ satisfies the requirement, and the proof is complete. $\square$
