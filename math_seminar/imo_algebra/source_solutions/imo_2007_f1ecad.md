# imo_2007_f1ecad

IMO-SL | IMO | 2007 | Number Theory | N4

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2007_f1ecad](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_f1ecad.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: 48th International Mathematical Olympiad
- Subtitle: Shortlisted Problems with Solutions
- Year: 2007
- Editors: Khoai, Ha Huy; Bogdanov, Ilya; Dung, Tran Nam; Hoa, Le Tuan; Kós, Géza
- Organization: International Mathematical Olympiad
- Place: Hanoi, Vietnam
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We use the notation $(2n-1)!! = 1 \cdot 3 \cdots (2n-1)$ and $(2n)!! = 2 \cdot 4 \cdots (2n) = 2^{n} n!$ for any positive integer $n$. Observe that $(2n)! = (2n)!! (2n-1)!! = 2^{n} n! (2n-1)!!$.

For any positive integer $n$ we have
$$
\begin{aligned}
& \binom{4n}{2n} = \frac{(4n)!}{(2n)!^{2}} = \frac{2^{2n}(2n)!(4n-1)!!}{(2n)!^{2}} = \frac{2^{2n}}{(2n)!}(4n-1)!! \\
& \binom{2n}{n} = \frac{1}{(2n)!} \left(\frac{(2n)!}{n!}\right)^{2} = \frac{1}{(2n)!} \left(2^{n}(2n-1)!!\right)^{2} = \frac{2^{2n}}{(2n)!}(2n-1)!!^{2}
\end{aligned}
$$

Then expression (1) can be rewritten as follows:
$$
\begin{aligned}
\binom{2^{k+1}}{2^{k}} - \binom{2^{k}}{2^{k-1}} &= \frac{2^{2^{k}}}{(2^{k})!} (2^{k+1}-1)!! - \frac{2^{2^{k}}}{(2^{k})!} (2^{k}-1)!!^{2} \\
&= \frac{2^{2^{k}} (2^{k}-1)!!}{(2^{k})!} \cdot \left( (2^{k}+1)(2^{k}+3) \ldots (2^{k}+2^{k}-1) - (2^{k}-1)(2^{k}-3) \ldots (2^{k}-2^{k}+1) \right)
\end{aligned}
$$

We compute the exponent of $2$ in the prime decomposition of each factor (the first one is a rational number but not necessarily an integer; it is not important).

First, we show by induction on $n$ that the exponent of $2$ in $(2^{n})!$ is $2^{n}-1$. The base case $n=1$ is trivial. Suppose that $(2^{n})! = 2^{2^{n}-1}(2d+1)$ for some integer $d$. Then we have
$$
(2^{n+1})! = 2^{2^{n}} (2^{n})! (2^{n+1}-1)!! = 2^{2^{n}} 2^{2^{n}-1} \cdot (2d+1) (2^{n+1}-1)!! = 2^{2^{n+1}-1} \cdot (2q+1)
$$
for some integer $q$. This finishes the induction step.

Hence, the exponent of $2$ in the first factor in (2) is $2^{k} - (2^{k}-1) = 1$.

The second factor in (2) can be considered as the value of the polynomial
$$
P(x) = (x+1)(x+3) \ldots (x+2^{k}-1) - (x-1)(x-3) \ldots (x-2^{k}+1)
$$
at $x = 2^{k}$. Now we collect some information about $P(x)$.

Observe that $P(-x) = -P(x)$, since $k \geq 2$. So $P(x)$ is an odd function, and it has nonzero coefficients only at odd powers of $x$. Hence $P(x) = x^{3} Q(x) + c x$, where $Q(x)$ is a polynomial with integer coefficients.

Compute the exponent of $2$ in $c$. We have
$$
\begin{aligned}
c &= 2 (2^{k}-1)!! \sum_{i=1}^{2^{k-1}} \frac{1}{2i-1} = (2^{k}-1)!! \sum_{i=1}^{2^{k-1}} \left( \frac{1}{2i-1} + \frac{1}{2^{k}-2i+1} \right) \\
&= (2^{k}-1)!! \sum_{i=1}^{2^{k-1}} \frac{2^{k}}{(2i-1)(2^{k}-2i+1)} = 2^{k} \sum_{i=1}^{2^{k-1}} \frac{(2^{k}-1)!!}{(2i-1)(2^{k}-2i+1)} = 2^{k} S
\end{aligned}
$$

For any integer $i = 1, \ldots, 2^{k-1}$, denote by $a_{2i-1}$ the residue inverse to $2i-1$ modulo $2^{k}$. Clearly, when $2i-1$ runs through all odd residues, so does $a_{2i-1}$, hence
$$
\begin{aligned}
S &= \sum_{i=1}^{2^{k-1}} \frac{(2^{k}-1)!!}{(2i-1)(2^{k}-2i+1)} \equiv -\sum_{i=1}^{2^{k-1}} \frac{(2^{k}-1)!!}{(2i-1)^{2}} \equiv -\sum_{i=1}^{2^{k-1}} (2^{k}-1)!! a_{2i-1}^{2} \\
&= - (2^{k}-1)!! \sum_{i=1}^{2^{k-1}} (2i-1)^{2} = - (2^{k}-1)!! \frac{2^{k-1}(2^{2k}-1)}{3} \quad (\bmod 2^{k})
\end{aligned}
$$

Therefore, the exponent of $2$ in $S$ is $k-1$, so $c = 2^{k} S = 2^{2k-1}(2t+1)$ for some integer $t$.

Finally we obtain that
$$
P(2^{k}) = 2^{3k} Q(2^{k}) + 2^{k} c = 2^{3k} Q(2^{k}) + 2^{3k-1}(2t+1)
$$
which is divisible exactly by $2^{3k-1}$. Thus, the exponent of $2$ in (2) is $1 + (3k-1) = 3k$.
