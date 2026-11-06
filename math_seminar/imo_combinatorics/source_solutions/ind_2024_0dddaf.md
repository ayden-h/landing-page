# ind_2024_0dddaf

IMO-TST | India | 2024 | Day 3 | 2.

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [ind_2024_0dddaf](https://mathnet.mit.edu/data_v2/full/india/ind_2024_0dddaf.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: India
- Title: Indian Mathematical Olympiads
- Subtitle: Problems Booklet
- Year: 2023-24
- Authors: Srivastava, Pranjal; Bhattacharya, Sutanay; Somasundaran, Muralidharan; Mudgal, Anant; Goyal, Rohan; Nene, Shantanu; Nadig, Atul Shatavart; Tejaswi, N.V.; Ghosh, Mainak; Saini, Rijul; Amin, Kazi Aryan; Sudharshan, K.V.

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $n$ be a positive integer. Call a positive integer $a$ *good* for $n$ if $n \mid a^{2n} - a$.
Define $d_n(a) = d$ to be the smallest positive integer such that $n \mid a^{2d} - a$. Then $a^{2d+k} \equiv a^{2k} \pmod{n}$ holds for $k \ge 0 \implies a^{2i} \pmod{n}$ is periodic with period $d$. The minimality of $d$ implies that it is in fact the smallest period. Therefore $d \mid n$. So $d \mid n \mid a^{2d} - a \implies a$ is *good* for $d$ as well.
Assume $n > 1$. If $\gcd(a, n) > 1$, then the sequence $a^{2i} \pmod{n}$ for $i = 1, 2, \dots, n$ does not contain any residues relatively prime to $n$. Else the sequence doesn't contain the residue $0$. In any case the sequence cannot contain all distinct elements, so $d_n(a) < n$.

**Lemma A1.** If $a$ is *good* for $n$, then the numbers $a^{2i} + i$ for $i = 1, \dots, n$ form a complete residue system modulo $n$.
*Proof.* We will prove this by induction on $n$. Base case $n = 1$ is true since there's only one number. Consider $n > 1$ for the induction step. Assume for the sake of contradiction that there exist distinct $i, j \le n$ such that $a^{2i} + i \equiv a^{2j} + j \pmod{n}$. Let $d = d_n(a)$. Then $d \mid n$, $d < n$ and $a$ is *good* for $d$ as well. So $a^{2i} + i \equiv a^{2j} + j \pmod{d}$. Note that, since $a$ is *good* for $d$, reducing $i, j$ modulo $d$ does not change the values of $a^{2i} + i \pmod{d}$ and $a^{2j} + j \pmod{d}$. Therefore, by induction hypothesis, $i \equiv j \pmod{d}$.
But then $a^{2i} \equiv a^{2j} \pmod{n} \implies i \equiv j \pmod{n}$. Contradiction! Hence the numbers are pairwise distinct modulo $n$, and so form a complete residue system. $\square$

**Lemma A2.** If $a$ is *good* for $n$, then so is $a^t$ for every $t \in \mathbb{N}$.
*Proof.* $n \mid a^{2n} - a \mid a^{t \cdot 2n} - a^t$.

We return to the main problem. Clearly we must have $n > 1$. Assume for the sake of contradiction that all the prime factors of $n$ are $\ge 2024$. We will prove using induction on $i$ that
$$
\sum_{k=1}^{n} k^i a^{2k}
$$
is divisible by $n$ for any *good* $a$ and $0 \le i \le 2024$, which will give us the desired contradiction. For the base case, $i = 0$. By Lemma A1,
$$
\sum_{k=1}^{n} (a^{2k} + k) \equiv \sum_{k=1}^{n} k \pmod{n} \implies \sum_{k=1}^{n} a^{2k} \equiv 0 \pmod{n}.
$$
Assume that the hypothesis holds for all $i < m$ for some $m \le 2024$. Then by Lemma A1,
$$
\sum_{k=1}^{n} (a^{2k} + k)^{m+1} \equiv \sum_{k=1}^{n} k^{m+1} \pmod{n} \implies \sum_{i=0}^{m} \binom{m+1}{i} \sum_{k=1}^{n} k^i a^{(m+1-i)2k} \equiv 0 \pmod{n}.
$$
By Lemma A2 and induction hypothesis, all the sums of the form
$$
\sum_{k=1}^{n} k^i a^{(m+1-i)2k}
$$
for $0 \le i \le m-1$ are divisible by $n$. Hence we get
$$
n \mid (m+1) \sum_{k=1}^{n} k^m a^{2^k}
$$
But $m+1 \le 2025$, and $2024, 2025$ are not primes. So all prime factors of $m+1$ are $< 2024$ which implies $\gcd(n, m+1) = 1$. Therefore
$$
n \mid \sum_{k=1}^{n} k^m a^{2^k}
$$
which completes the induction. $\square$

## Supplied solution 2

We begin by observing that proving the following claim is sufficient:
**Claim B1.** Let $p$ be any prime $> 2025$. Now, let $m$ be an integer such that $p \nmid m$. Then for any integer $i \ge 1$, if $p^i \mid a^{2^{m \cdot p^i}} - a$ then for any $\le \alpha \le 2024$,
$$
p^i \mid \sum_{k=1}^{m \cdot p^i} k^\alpha a^{2^k}
$$
Observe that if the above claim follows then, we have that if $n$ does not have any prime factors $\le 2025$ and $n \mid a^{2^n} - a$ then $n \mid \sum_{k=1}^{n} k^{2024} a^{2^n}$ since the divisibility follows for all prime factors of $n$ from Claim 1. Thus, if $n$ satisfies the problem conditions then it must have a prime factor $\le 2025$ i.e. some prime factor $< 2024$ since $2024 = 2 \cdot 1012$ and $2025 = 45^2$ are not primes.
Thus, we just prove Claim B1!
*Proof of Claim B1.*
**Lemma B1.** If $p^i \mid a^{2^{m \cdot p^i}} - a$ then $p^i \mid a^{2^{m \cdot p^{i-1}}} - a$.
**Lemma B2.** If $t \in \mathbb{N}$ and $t < p-1$ then
$$
p \mid 1^t + 2^t + \dots + (p-1)^t
$$
We delay the proof of Lemma B1 and Lemma B2 to the end of the proof. Now, assuming above lemmas, observe that we can prove Claim B1 by induction on $i$: We begin by proving the base case $i=1$:
$$
\sum_{k=1}^{m \cdot p} k^{\alpha} a^{2^k} \equiv \sum_{k=1}^{m} \sum_{j=0}^{p-1} a^{2^{k+mj}} (k+mj)^{\alpha} \pmod{p}
$$
$$
\equiv \sum_{k=1}^{m} a^{2^k} \left( \sum_{j=0}^{p-1} (k+mj)^{\alpha} \right) \pmod{p}
$$
$$
\equiv \sum_{k=1}^{m} a^{2^k} \left( pk^{\alpha} + \sum_{t=1}^{\alpha} \binom{\alpha}{t} k^{\alpha-t} m^t \left( \sum_{j=0}^{p-1} j^t \right) \right) \pmod{p}
$$
$$
\equiv 0 \pmod{p}
$$
The last part follows since when $0 < t \le \alpha \le 2024 < p-1$, by Lemma B2,
$$
p \mid 0^t + 1^t + 2^t + \dots + (p-1)^t
$$
Now, for the induction step $i+1 > 1$:
$$
\begin{align*}
\sum_{k=1}^{m \cdot p^{i+1}} k^{\alpha} a^{2^k} &\equiv \sum_{k=1}^{mp^i} \sum_{j=0}^{p-1} a^{2^{k+p^i m j}} (k+p^i m j)^{\alpha} \quad (\text{mod } p^{i+1}) \\
&\equiv \sum_{k=1}^{mp^i} a^{2^k} \left( \sum_{j=0}^{p-1} (k+p^i m j)^{\alpha} \right) \quad (\text{mod } p^{i+1}) \\
&\equiv \sum_{k=1}^{mp^i} a^{2^k} \left( p k^{\alpha} + \alpha p^i m \left( \sum_{j=1}^{p-1} j \right) \right) \quad (\text{mod } p^{i+1}) \\
&\equiv p \left( \sum_{k=1}^{mp^i} a^{2^k} k^{\alpha} \right) \quad (\text{mod } p^{i+1}) \\
&\equiv 0 \quad (\text{mod } p^{i+1})
\end{align*}
$$
The last step follows since inductively we have $p^i \mid \sum_{k=1}^{mp^i} a^{2^k} k^\alpha$. Thus, we are done with the proof of Claim B1! $\square$

Now, we just prove Lemma B1 and B2.
*Proof of Lemma B2.* Let $c$ be any number from $\{1, \cdots, p-1\}$ such that $c^t - 1 \not\equiv 0 \pmod{p}$. This exists since $x^t - 1$ can only have $t < p-1$ roots (mod $p$).
Then,
$$
\sum_{j=1}^{p-1} j^t \equiv \sum_{j=1}^{p-1} (cj)^t \equiv c^t \sum_{j=1}^{p-1} j^t \implies (c^t - 1) \left( \sum_{j=1}^{p-1} j^t \right) \equiv 0 \pmod{p} \implies \sum_{j=1}^{p-1} j^t \equiv 0 \pmod{p}
$$
Alternately, lemma B2 is often proved by letting $g$ be a primitive root (mod $p$), then
$$
\sum_{j=0}^{t} j^t \equiv \sum_{j=1}^{p-2} g^{jt} \equiv \frac{g^{(p-1)t} - 1}{g^t - 1} \equiv 0 \pmod{p}
$$
This follows since $g^t \neq 0$ and $g^{(p-1)t} \equiv 1 \pmod{p}$ by Fermat's little theorem. (Another alternative is to consider the complete residue systems $\{0, 1, 2, \dots, p-1\}$ and $\{0, g, 2g, \dots, (p-1)g\}$ and compare the sum of $t^{th}$ powers) $\square$

*Proof of Lemma B1.*
**Lemma B3.** If $k|a^b - 1$ then $k|a^c - 1$ then $k|a^{\gcd(b,c)} - 1$.
*Proof.* This follows since, if we let $0 < d$ be the lowest number such that $k|a^d - 1$ then, we if $b = dq + r$ then $k | a^{dq}a^r - 1 \implies k | a^r - 1$ but $r < d$. Thus, $r = 0$ and $d|b$. Similarly, $d|c$. Now, $d|\gcd(b,c)$ so $(a^d)^{\gcd(b,c)/d} - 1 \equiv 1 \pmod{k}$. $\square$

In particular, this means that if $k|a^b - 1$ then $\gcd(a, k) = 1$, so $k|a^{\gcd(b, \phi(k))} - 1$ since $k|a^{\phi(k)} - 1$.
Applying this to our problem, if $p^i \mid a^{2^{mp^i}} - a$ and $p \mid a$ then we have that $p^i \mid a$ so $p \mid a^{2^{mp^i-1}} - a$.
And now if, $\gcd(a, p) = 1$ then we have that
$$
p^i \mid a^{2^{mp^i}-1} - 1 \implies p^i \mid a^{\gcd(2^{mp^i}-1, (p-1)p^{i-1})} - 1
$$
Now, observe that
$$
\gcd(p-1, 2^{mp^i}-1) = \gcd(p-1, 2^{\gcd(mp^i), \phi(p-1)}-1) = \gcd(p-1, 2^{\gcd(m), \phi(p-1)}-1) = \gcd(p-1, 2^{mp^i-1}-1)
$$
Also, if $p|2^{mp^i} - 1$, then $p \mid 2^m - 1$. Thus, $\nu_p(2^{mp^i} - 1) = i + \nu_p(2^m - 1)$. Thus, if $p|2^m - 1$, then $p^i \mid 2^{mp^{i-1}} - 1$. If $p \nmid 2^m - 1$, then $p \nmid 2^{mp^{i-1}} - 1$. Thus, $\gcd(p^{i-1}, 2^{mp^i}) = \gcd(p^{i-1}, 2^{mp^{i-1}})$. Thus,
$$
\gcd(2^{mp^i} - 1, (p-1)p^{i-1}) = \gcd(2^{mp^{i-1}} - 1, (p-1)p^{i-1})
$$
So, we get that $p^i \mid a^{2^{mp^{i-1}} - 1} - 1 \implies p^i \mid a^{2^{mp^{i-1}}} - a$ as desired!

