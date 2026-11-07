# rmm_2012_d9fcef

RMM | Romanian Master of Mathematics (RMM) | 2012 | Day 2 | Problem 4

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [rmm_2012_d9fcef](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2012_d9fcef.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Romanian Master of Mathematics (RMM)

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Throughout the solution $n$ stands for a positive integer. By Euler's theorem, $(2^{3^{n}}+1)(2^{3^{n}}-1)=2^{2 \cdot 3^{n}}-1 \equiv 0 \pmod{3^{n+1}}$. Since $2^{3^{n}}-1 \equiv 1 \pmod{3}$, it follows that $2^{3^{n}}+1$ is divisible by $3^{n+1}$.

The number $(2^{3^{n+1}}+1)/(2^{3^{n}}+1)=2^{2 \cdot 3^{n}}-2^{3^{n}}+1$ is greater than $3$ and congruent to $3$ modulo $9$, so it has a prime factor $p_{n}>3$ that does not divide $2^{3^{n}}+1$ (otherwise, $2^{3^{n}} \equiv -1 \pmod{p_{n}}$, so $2^{2 \cdot 3^{n}}-2^{3^{n}}+1 \equiv 3 \pmod{p_{n}}$, contradicting the fact that $p_{n}$ is a factor greater than $3$ of $2^{2 \cdot 3^{n}}-2^{3^{n}}+1$).

We now show that $a_{n}=3^{n} p_{n}$ satisfies the conditions in the statement. Since $2^{a_{n}}+1 \equiv 2^{3^{n}}+1 \not\equiv 0 \pmod{p_{n}}$, it follows that $a_{n}$ does not divide $2^{a_{n}}+1$.

On the other hand, $3^{n+1}$ divides $2^{3^{n}}+1$ which in turn divides $2^{a_{n}}+1$, so $2^{3^{n+1}}+1$ divides $2^{2^{a_{n}}+1}+1$. Finally, both $3^{n}$ and $p_{n}$ divide $2^{3^{n+1}}+1$, so $a_{n}$ divides $2^{2^{a_{n}}+1}+1$.

As $n$ runs through the positive integers, the $a_{n}$ are clearly pairwise distinct and the conclusion follows.

## Supplied solution 2

(Géza Kós) We show that the numbers $a_{n}=(2^{3^{n}}+1)/9$, $n \geq 2$, satisfy the conditions in the statement. To this end, recall the following well-known facts:

(1) If $N$ is an odd positive integer, then $\nu_{3}(2^{N}+1)=\nu_{3}(N)+1$, where $\nu_{3}(a)$ is the exponent of $3$ in the decomposition of the integer $a$ into prime factors; and

(2) If $M$ and $N$ are odd positive integers, then $(2^{M}+1,2^{N}+1)=2^{(M, N)}+1$, where $(a, b)$ is the greatest common divisor of the integers $a$ and $b$.

By (1), $a_{n}=3^{n-1} m$, where $m$ is an odd positive integer not divisible by $3$, and by (2),
$$
(m, 2^{a_{n}}+1) \mid (2^{3^{n}}+1,2^{a_{n}}+1)=2^{(3^{n}, a_{n})}+1=2^{3^{n-1}}+1<\frac{2^{3^{n}}+1}{3^{n+1}}=m
$$
so $m$ cannot divide $2^{a_{n}}+1$.

On the other hand, $3^{n-1} \mid 2^{2^{a_{n}}+1}+1$, for $\nu_{3}(2^{2^{a_{n}}+1}+1)>\nu_{3}(2^{a_{n}}+1)>\nu_{3}(a_{n})=n-1$, and $m \mid 2^{2^{a_{n}}+1}+1$, for $3^{n-1} \mid a_{n}$, so $3^{n} \mid 2^{a_{n}}+1$ whence $m\mid 2^{3^{n}}+1\mid 2^{2^{a_{n}}+1}+1$. Since $3^{n-1}$ and $m$ are coprime, the conclusion follows.

## Supplied solution 3

(Dušan Djukić) Assume that $n$ satisfies the conditions of the problem. We claim that the number $N=2^{n}+1>n$ also satisfies these conditions.

Firstly, since $n \nmid N$, the fact (2) from Solution 2 allows to conclude that $2^{n}+1 \nmid 2^{N}+1$, or $N \nmid 2^{N}+1$. Next, since $n \mid 2^{2^{n}+1}+1=2^{N}+1$, we obtain from the same fact that $N=2^{n}+1 \mid 2^{2^{N}+1}+1$, thus confirming our claim.

Hence, it suffices to provide only one example, hence obtaining an infinite series by the claim. For instance, one may easily check that the number $n=57$ fits.
