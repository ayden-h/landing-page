# imo_2019_aedde5

IMO-SL | IMO | 2019 | Number Theory | N5

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2019_aedde5](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_aedde5.json.gz)

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

**Known source issue:** One imported alternate proof reverses a binomial ratio and invokes unnecessary Dirichlet machinery. N11 proves the exact criterion directly.

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

Checked rewritten solution: [N11](../reviewed_solutions/N11.md).

## Supplied solution 1

We first show that $b$ is $a$-good if and only if $b$ is even, and $p \mid a$ for all primes $p \leqslant b$.
To start with, the condition that $a n+1 \left\lvert\,\binom{ a n}{b}-1\right.$ can be rewritten as saying that
$$
\frac{a n(a n-1) \cdots(a n-b+1)}{b!} \equiv 1 \quad(\bmod a n+1) .
$$
Suppose, on the one hand, there is a prime $p \leqslant b$ with $p \nmid a$. Take $t=v_{p}(b!)$. Then there exist positive integers $c$ such that $a c \equiv 1\left(\bmod p^{t+1}\right)$. If we take $c$ big enough, and then take $n=(p-1) c$, then $a n=a(p-1) c \equiv p-1\left(\bmod p^{t+1}\right)$ and $a n \geqslant b$. Since $p \leqslant b$, one of the terms of the numerator $a n(a n-1) \cdots(a n-b+1)$ is $a n-p+1$, which is divisible by $p^{t+1}$. Hence the $p$-adic valuation of the numerator is at least $t+1$, but that of the denominator is exactly $t$. This means that $p \left\lvert\,\binom{ a n}{b}\right.$, so $p \nmid \binom{a n}{b}-1$. As $p \mid a n+1$, we get that $a n+1 \nmid \binom{a n}{b}-1$, so $b$ is not $a$-good.
On the other hand, if for all primes $p \leqslant b$ we have $p \mid a$, then every factor of $b!$ is coprime to $a n+1$, and hence invertible modulo $a n+1$ : hence $b!$ is also invertible modulo $a n+1$. Then equation above reduces to:
$$
a n(a n-1) \cdots(a n-b+1) \equiv b!\quad(\bmod a n+1) .
$$
However, we can rewrite the left-hand side as follows:
$$
a n(a n-1) \cdots(a n-b+1) \equiv(-1)(-2) \cdots(-b) \equiv(-1)^{b} b!\quad(\bmod a n+1) .
$$
Provided that $a n>1$, if $b$ is even we deduce $(-1)^{b} b!\equiv b!$ as needed. On the other hand, if $b$ is odd, and we take $a n+1>2(b!)$, then we will not have $(-1)^{b} b!\equiv b!$, so $b$ is not $a$-good. This completes the claim.
To conclude from here, suppose that $b$ is $a$-good, but $b+2$ is not. Then $b$ is even, and $p \mid a$ for all primes $p \leqslant b$, but there is a prime $q \leqslant b+2$ for which $q \nmid a$ : so $q=b+1$ or $q=b+2$. We cannot have $q=b+2$, as that is even too, so we have $q=b+1$ : in other words, $b+1$ is prime.

## Supplied solution 2

We show only half of the claim of the previous solution: we show that if $b$ is $a$-good, then $p \mid a$ for all primes $p \leqslant b$. We do this with Lucas' theorem.
Suppose that we have $p \leqslant b$ with $p \nmid a$. Then consider the expansion of $b$ in base $p$; there will be some digit (not the final digit) which is nonzero, because $p \leqslant b$. Suppose it is the $p^{t}$ digit for $t \geqslant 1$.
Now, as $n$ varies over the integers, $a n+1$ runs over all residue classes modulo $p^{t+1}$; in particular, there is a choice of $n$ (with $a n>b$ ) such that the $p^{0}$ digit of $a n$ is $p-1$ (so $p \mid a n+1)$ and the $p^{t}$ digit of $a n$ is 0. Consequently, $p \mid a n+1$ but $p \mid \binom{ a n}{b}$ (by Lucas' theorem) so $p \nmid \binom{a n}{b}-1$. Thus $b$ is not $a$-good.
Now we show directly that if $b$ is $a$-good but $b+2$ fails to be so, then there must be a prime dividing $a n+1$ for some $n$, which also divides $(b+1)(b+2)$. Indeed, the ratio between $\binom{a n}{b+2}$ and $\binom{a n}{b}$ is $(b+1)(b+2) /(a n-b)(a n-b-1)$. We know that there must be a choice of $a n+1$ such that the former binomial coefficient is 1 modulo $a n+1$ but the latter is not, which means that the given ratio must not be $1 \bmod a n+1$. If $b+1$ and $b+2$ are both coprime to $a n+1$ then the ratio is 1, so that must not be the case. In particular, as any prime less than $b$ divides $a$, it must be the case that either $b+1$ or $b+2$ is prime.
However, we can observe that $b$ must be even by insisting that $a n+1$ is prime (which is possible by Dirichlet's theorem) and hence $\binom{a n}{b} \equiv(-1)^{b}=1$. Thus $b+2$ cannot be prime, so $b+1$ must be prime.
