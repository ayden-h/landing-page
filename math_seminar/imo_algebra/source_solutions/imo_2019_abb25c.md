# imo_2019_abb25c

IMO-SL | IMO | 2019 | Algebra | A1

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2019_abb25c](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_abb25c.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems
- Subtitle: with solutions
- Year: 2019
- Editors: Gardiner, Tony; Crane, Edward; Betts, Alexander; Cranch, James; Myers, Joseph; Aaronson, James; Carlotti, Andrew; Kós, Géza; Bogdanov, Ilya I.; Shotton, Jack
- Organization: 60th International Mathematical Olympiad
- Place: Bath, United Kingdom
- Series: International Mathematical Olympiad
- Volume: 60th
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

Checked rewritten solution: [A01](../reviewed_solutions/A01.md).

## Supplied solution 1

Substituting $a=0$, $b=n+1$ gives $f(f(n+1)) = f(0) + 2f(n+1)$. Substituting $a=1$, $b=n$ gives $f(f(n+1)) = f(2) + 2f(n)$.
In particular, $f(0) + 2f(n+1) = f(2) + 2f(n)$, and so $f(n+1) - f(n) = \frac{1}{2}(f(2) - f(0))$. Thus $f(n+1) - f(n)$ must be constant. Since $f$ is defined only on $\mathbb{Z}$, this tells us that $f$ must be a linear function; write $f(n) = M n + K$ for arbitrary constants $M$ and $K$, and we need only determine which choices of $M$ and $K$ work.

Now, (1) becomes
$$
2M a + K + 2(M b + K) = M(M(a+b) + K) + K
$$
which we may rearrange to form
$$
(M-2)(M(a+b) + K) = 0
$$
Thus, either $M = 2$, or $M(a+b) + K = 0$ for all values of $a+b$. In particular, the only possible solutions are $f(n) = 0$ and $f(n) = 2n + K$ for any constant $K \in \mathbb{Z}$, and these are easily seen to work.

## Supplied solution 2

Let $K = f(0)$.
First, put $a = 0$ in (1); this gives
$$
\begin{equation*}
f(f(b)) = 2f(b) + K \tag{2}
\end{equation*}
$$
for all $b \in \mathbb{Z}$.
Now put $b = 0$ in (1); this gives
$$
f(2a) + 2K = f(f(a)) = 2f(a) + K,
$$
where the second equality follows from (2). Consequently,
$$
\begin{equation*}
f(2a) = 2f(a) - K \tag{3}
\end{equation*}
$$
for all $a \in \mathbb{Z}$.
Substituting (2) and (3) into (1), we obtain
$$
\begin{aligned}
f(2a) + 2f(b) & = f(f(a+b)) \\
2f(a) - K + 2f(b) & = 2f(a+b) + K \\
f(a) + f(b) & = f(a+b) + K .
\end{aligned}
$$
Thus, if we set $g(n) = f(n) - K$ we see that $g$ satisfies the Cauchy equation $g(a+b) = g(a) + g(b)$. The solution to the Cauchy equation over $\mathbb{Z}$ is well-known; indeed, it may be proven by an easy induction that $g(n) = M n$ for each $n \in \mathbb{Z}$, where $M = g(1)$ is a constant.
Therefore, $f(n) = M n + K$, and we may proceed as in Solution 1.
