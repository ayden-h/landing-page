# chn_2021_0faf8c

China-TST | China | 2021 | Test II, Second Day | 4

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [chn_2021_0faf8c](https://mathnet.mit.edu/data_v2/full/china/chn_2021_0faf8c.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: China

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

The desired functions have the form
$$
f(n) = \begin{cases} c, & n = 1, \\ dn, & n \ge 2, \end{cases}
$$
where $c, d$ are positive integers. It is straightforward to check that the problem conditions are met.
In the governing equation, taking $n = 2$ leads to $f(4m) = 4f(m)$ for $m \ge 2$. By iterations, it follows that
$$
f(4^k m) = 4^k f(m) \qquad \textcircled{1}
$$
for all $m \ge 2$.
**Claim** For positive integers $m, p$ with $m \ge 2$, $f(pm) = p f(m)$.
**Proof of claim** Induct on $p$: when $p = 1$, the conclusion is trivial; assume $p \ge 2$ and the conclusion is valid for all positive integers less than $p$. Now, if $p$ is composite, the conclusion is validated by the induction hypothesis. In the following, assume $p$ is a prime. Taking $n = p$ in the governing equation, we obtain
$$
f(p^2(p-1)m) = p^2(p-1)f(m)
$$
for all $m \ge p$. By the induction hypothesis,
$$
\begin{aligned}
p^2(p-1)f(m) &= f(p^2(p-1)m) \\
&= (p-1)f(p^2m), \end{aligned}
$$
and thus
$$
f(p^2m) = p^2f(m) \qquad \textcircled{2}
$$
for all $m \ge p$.

Next, take $n = p^2$ in the governing equation to get
$$
f(p^5(p-1)m) = p^5(p-1)f(m)
$$
for $m \ge p^2$. In a similar manner, it follows by induction that
$$
f(p^5(p-1)m) = (p-1)f(p^5m).
$$
Hence,
$$
f(p^5m) = p^5f(m) \qquad \textcircled{3}
$$
for $m \ge p^2$.
Based on the above argument, we take $k$ with $4^k \ge p^2$: for any $m \ge 2$,
$$
4^k p^4 f(p m) \stackrel{\textcircled{2}}{=} 4^k f(p^5 m) \stackrel{\textcircled{1}}{=} f(4^k p^5 m) \stackrel{\textcircled{3}}{=} p^5 f(4^k m) \stackrel{\textcircled{1}}{=} p^5 4^k f(m).
$$
Therefore, $f(p m) = p f(m)$, and the induction is completed.
According to the claim, particularly for $m \ge 2$,
$$
2f(m) = f(2m) = m f(2).
$$
Taking $m = 3$, we infer that $f(2)$ is even. So for $m \ge 2$, $f(m) = d m$, where $d = \frac{f(2)}{2}$ is an integer. $\square$
