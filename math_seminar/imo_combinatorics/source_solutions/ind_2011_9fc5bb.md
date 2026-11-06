# ind_2011_9fc5bb

IMO-TST | India | 2011 |  | 4

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [ind_2011_9fc5bb](https://mathnet.mit.edu/data_v2/full/india/ind_2011_9fc5bb.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: India
- Title: Some problems used in Indian team selection for IMO-2011
- Year: 2011
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Consider points $P_j = (a_j, b_j)$ in the plane. The slope of the lines $P_nP_{n-1}$ and $P_nP_{n-2}$ are
$$
r = \frac{b_n - b_{n-1}}{a_n - a_{n-1}}, \quad s = \frac{b_n - b_{n-2}}{a_n - a_{n-2}},
$$
respectively. The given condition implies that $rs = -1$. Hence it follows that the lines $P_nP_{n-1}$ and $P_nP_{n-2}$ are perpendicular to each other. This implies that $P_n$ lies on the circle $C_n$ with diameter $P_{n-1}P_{n-2}$. Let $f(n) = |P_{n-1} - P_{n-2}|^2$. Then $f(n)$ is an integer. The observation that $P_n$ lies on the circle $C_n$ shows that $f(n) \le f(n-1)$. Thus we get a non-increasing sequence of positive integers. This must be constant after certain stage. Thus $f(n)$ is constant for $n \ge N$, for some positive integer $N$. This implies that the diameter of $C_n$ is constant for all $n \ge N$. Hence $C_n$ are all equal circles for $n \ge N$. This implies that $P_n = P_{n+2}$ for all $n \ge N$. But then $a_n = a_{n+2}$ for all $n \ge N$. Hence
$$
a_{N+2011} = a_{N+(2011)^{2011}}.
$$

