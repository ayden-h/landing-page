# vnm_2009_d06acd

VMO | Vietnam | 2009 |  | Problem 4

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [vnm_2009_d06acd](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2009_d06acd.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Vietnam
- Title: VIETNAMESE MATHEMATICAL OLYMPIAD IN 2009
- Year: 2009

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

For each positive integer $n$, let $T_n = a^n + b^n + c^n$. By assumption, $T_n \in \mathbb{Z}$ for all $n \ge 1$.
We will show that the numbers $p = -(a + b + c)$, $q = ab + bc + ca$ and $r = -abc$ satisfy the requirement for the problem.
Indeed, according to the theorem of Viet, $a$, $b$, $c$ are 3 solutions of the equation
$$
x^3 + px^2 + qx + r = 0.
$$
Moreover, since $p = -T_1$, $p \in \mathbb{Z}$. Next, we will show $q, r \in \mathbb{Z}$.
We have the following presentations of $T_n$ in terms of $p$, $q$, $r$:
$$
\begin{align*}
T_1 &= -p \\
T_2 &= p^2 - 2q \tag{4.1}
\end{align*}
$$
$$
T_3 = -p^3 + 3pq - 3r \quad (4.2)
$$
$$
T_{n+3} = -pT_{n+2} - qT_{n+1} - rT_n \quad \forall n \ge 1. \quad (4.3)
$$
Since $T_2$, $p \in \mathbb{Z}$, it follows from (4.1) that $2q \in \mathbb{Z}$. \qquad (4.4)
$$
\begin{align*}
& \text{It follows from (4.2) that} \\
& \quad 2pT_3 = -2p^4 + 6p^2q - 6pr. \tag*{(4.5)}
\end{align*}
$$
Let $n=1$ in (4.3), we have: $T_4 = -pT_3 - qT_2 - rT_1 = p^4 - 4p^2q + 4pr + 2q^2$.
$$
\text{Consequently} \qquad 3T_4 = 3p^4 - 12p^2q + 12pr + 6q^2.
$$
Hence, according to (4.4) and (4.5), we have $6q^2 \in \mathbb{Z}$. By means of (4.4), we get $q \in \mathbb{Z}$.

Hence, according to (4.2), $3r \in \mathbb{Z}$. That is $r$ has the form: $r = \frac{m}{3}$, $m \in \mathbb{Z}$. (4.6)
On the other hand, it follows from (4.3) that: $rT_n \in \mathbb{Z} \quad \forall n \ge 1$.
By means of (4.6), we conclude $mT_n \equiv 0 \pmod{3} \quad \forall n \ge 1$. (4.7)
- If there exists $n$ such that $(T_n, 3) = 1$ then according to (4.7) $m \equiv 0 \pmod{3}$. Whence $r \in \mathbb{Z}$.
- Consider the case $T_n \equiv 0 \pmod{3} \quad \forall n \ge 1$. Then, since $p \equiv T_1 \equiv 0 \pmod{3}$ and $T_3 \equiv 0 \pmod{3}$ we conclude by means of (4.2) that $r \in \mathbb{Z}$. The proof is complete.
