# apm_2003_7dec2d

APMO | Asia Pacific Mathematics Olympiad (APMO) | 2003 |  | 4

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [apm_2003_7dec2d](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2003_7dec2d.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Asia Pacific Mathematics Olympiad (APMO)
- Title: XV APMO: Solutions and Marking Schemes

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Without loss of generality, assume $a \leq b \leq c$. As $a + b > c$, we have
$$
\frac{\sqrt[n]{2}}{2} = \frac{\sqrt[n]{2}}{2}(a + b + c) > \frac{\sqrt[n]{2}}{2}(c + c) = \sqrt[n]{2 c^{n}} \geq \sqrt[n]{b^{n} + c^{n}}. \quad [2 \text{ marks}] \tag{1}
$$
As $a \leq c$ and $n \geq 2$, we have
$$
\begin{aligned}
\left(c^{n} + a^{n}\right) - \left(c + \frac{a}{2}\right)^{n} & = a^{n} - \sum_{k=1}^{n} \binom{n}{k} c^{n-k} \left(\frac{a}{2}\right)^{k} \\
& \leq \left[1 - \sum_{k=1}^{n} \binom{n}{k} \left(\frac{1}{2}\right)^{k}\right] a^{n} \quad (\text{since } c^{n-k} \geq a^{n-k}) \\
& = \left[\left(1 - \frac{n}{2}\right) - \sum_{k=2}^{n} \binom{n}{k} \left(\frac{1}{2}\right)^{k}\right] a^{n} < 0.
\end{aligned}
$$
Thus
$$
\sqrt[n]{c^{n} + a^{n}} < c + \frac{a}{2}. \quad [3 \text{ marks}] \tag{2}
$$
Likewise
$$
\sqrt[n]{b^{n} + a^{n}} < b + \frac{a}{2}. \quad [1 \text{ mark}] \tag{3}
$$
Adding (1), (2) and (3), we get
$$
\sqrt[n]{a^{n} + b^{n}} + \sqrt[n]{b^{n} + c^{n}} + \sqrt[n]{c^{n} + a^{n}} < \frac{\sqrt[n]{2}}{2} + c + \frac{a}{2} + b + \frac{a}{2} = 1 + \frac{\sqrt[n]{2}}{2}. \quad [1 \text{ mark}]
$$
