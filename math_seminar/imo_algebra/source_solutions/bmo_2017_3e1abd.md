# bmo_2017_3e1abd

BMO-SL | Balkan Mathematical Olympiad | 2017 | ALGEBRA | A5

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2017_3e1abd](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2017_3e1abd.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: PROBLEM SHORTLIST
- Subtitle: (with solutions)
- Year: 2017
- Authors: Malcheski, Risto; Petrushevski, Mirko; Dimovski, Pavel; Velinov, Daniel; Dimovski, Tomi
- Organization: Union of Mathematicians of Macedonia
- Publisher: Union of Mathematicians of Macedonia
- Place: Ohrid, Macedonia
- Series: Balkan Mathematical Olympiad
- Issue: 34
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $a_0, a_1, \dots, a_n$ be integers to be chosen later, and consider the polynomial $P(x) = \frac{1}{n!} Q(x)$ where
$$
Q(x) = \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} a_k \prod_{\substack{0 \le i \le n \\ i \ne k}} (x-i).
$$
Observe that for $l \in \{0, 1, \dots, n\}$ we have
$$
\begin{aligned}
P(l) &= \frac{1}{n!} (-1)^n \binom{n}{l} a_l \prod_{\substack{0 \le i \le n \\ i \ne l}} (l-i) \\
&= \frac{1}{n!} (-1)^{n-l} \binom{n}{l} a_l l! (-1)^{n-l} (n-l)! \\
&= a_l
\end{aligned}
$$
So $P(x)$ is the unique polynomial of degree at most $n$ such that $P(l) = a_l$. (Any two polynomials of degree at most $n$ agreeing on $n+1$ distinct values are equal.) Note in particular that
$$
\sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} \prod_{\substack{0 \le i \le n \\ i \ne k}} (x-i) = n! \quad (*)
$$
If $p$ is a prime dividing $n!$, we let $r_p$ be maximal such that $p^{r_p}$ divides $n!$. If $p$ divides $m$, then there is an integer $d_p$ such that $m^{d_p} \equiv 0 \pmod{p^{r_p}}$, for example $d_p = r_p$ will do. If $p$ does not divide $m$, then there is an integer $d_p$ such that $m^{d_p} \equiv 1 \pmod{p^{r_p}}$, for example, by Euler's theorem, $d_p = \varphi(p^{r_p})$ will do. Let $d = d_1 d_2 \dots d_p$ and observe that for every positive integer $t$ we have $m^{td} \equiv 0 \pmod{p^{r_p}}$ if $p \mid m$ and $m^{td} \equiv 1 \pmod{p^{r_p}}$ if $p \nmid m$.

Now let $t_0, \dots, t_n$ be positive integers to be chosen later and define $a_k = m^{t_k d}$. We will show that the polynomial $P(x)$ has integer coefficients. We will also show that there is an appropriate choice of $t_0, \dots, t_n$ such that $P(x)$ has degree exactly equal to $n$.

To show that $P(x)$ has integer coefficients it is enough to show that for every $p$ dividing $n!$, all coefficients of $Q(x)$ are multiples of $p^{r_p}$. This is immediate if $p$ divides $m$ as all $a_k$'s are multiples of $p^{r_p}$. If $p$ does not divide $m$ then we have $a_k \equiv 1 \pmod{p^{r_p}}$ for every $0 \le k \le n$ and so by (*)
$$
Q(x) = \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} \prod_{\substack{0 \le i \le n \\ i \ne k}} (x-i) \equiv n! \pmod{p^{r_p}}.
$$
This shows that all coefficients of $Q(x)$ are indeed multiples of $p^{r_p}$. It remains to show that there is a choice of $t_0, \dots, t_n$ guaranteeing that the degree of $P(x)$ is exactly equal to $n$. One such choice is $t_0 = 2$ and $t_1 = \dots = t_n = 1$. This works because if $P(x)$ had degree less than $n$, then looking at the values $P(1), \dots, P(n)$ we would get that $P(x)$ is constant. But this is impossible as $P(0) \ne P(1)$.
