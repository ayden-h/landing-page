---
title: "AIME Number Theory"
subtitle: "Prime exponents, residues, and exact structure"
author: "Ayden Bi"
date: "Research edition · November 2026"
lang: en-US
---

# Replace the integer by its structure

A large integer is often the wrong object to calculate. Its prime exponents, residue classes, digit blocks, or multiplicative order contain exactly the information a problem needs. The first task is to choose that representation and prove that it preserves the requested property.

This book develops the tools in an order that makes those changes of representation natural. Divisibility becomes an inequality between prime exponents. A congruence becomes a residue class with a specified modulus. A repeating decimal becomes a reduced denominator. An extremal integer becomes a sorted exponent pattern. A recurrence can become ordinary counting in another numeral system.

The historical collection supplies the worked AIME instances and a record of which published alternatives were inspected. Results below are classical unless called archive-derived; that description identifies the formulation produced during this audit, not a claim that the mathematics is new.

## A starting decision table

| Information in the statement | Useful representation |
|---|---|
| Divisors, gcd, lcm, perfect powers | Prime-exponent vectors |
| Several remainders | Linear congruences and CRT |
| Exponential divisibility | Multiplicative order, then valuations |
| Factorials or binomial coefficients | Legendre's formula and carries |
| Repeated digits or decimals | A geometric sum and a reduced denominator |
| Positive integer solutions | Factorization plus bounds and congruences |
| Smallest integer with a divisor property | Ordered prime exponents |
| Floor sums | Lattice points or complete residue periods |

Use a modulus because it distinguishes the possibilities in the problem, not because modular arithmetic is the subject's customary first move. A congruence obstruction proves impossibility; it does not prove that every surviving case is attainable.

# 1. Divisibility, gcd, and the Euclidean algorithm

For integers $a,b$, $a\mid b$ means $b=ak$ for an integer $k$. The positive greatest common divisor of integers not both zero is denoted $\gcd(a,b)$. For positive integers the least common multiple is $\operatorname{lcm}(a,b)$.

**Theorem 1.1 (Euclidean invariance).** For any integer $q$,

$$\gcd(a,b)=\gcd(b,a-qb).$$

**Proof.** A number divides $a,b$ exactly when it divides $b,a-qb$. The sets of common divisors are identical. $\square$

**Theorem 1.2 (Bézout).** There are integers $u,v$ with $ua+vb=\gcd(a,b)$.

**Proof.** Repeated Euclidean division ends at the gcd. Substitute each remainder equation backward to express it as an integer linear combination of the original pair. $\square$

**Corollary 1.3 (coprime cancellation).** If $\gcd(a,m)=1$ and $m\mid ab$, then $m\mid b$.

**Proof.** Multiply an identity $ua+vm=1$ by $b$. Both $uab$ and $vmb$ are divisible by $m$. $\square$

This is the legal form of cancellation in divisibility. Without coprimality the conclusion changes: from $6\mid2b$ one obtains $3\mid b$, not necessarily $6\mid b$.

## 1.1 A polynomial gcd collapses to a constant

**Derived proposition 1.4.** For integers $c\ge0,n\ge1$,

$$\gcd(n^2+c,(n+1)^2+c)=\gcd(4c+1,2n+1).$$

**Proof.** Subtract the two quadratic values to obtain $2n+1$. This is odd, so multiplication of the other entry by four does not change the gcd. Now

$$4(n^2+c)=(2n+1)(2n-1)+(4c+1),$$

and another Euclidean step gives the result. $\square$

For $c>0$ the maximum possible gcd is $4c+1$, attained at $n=2c$. For $c=0$ it is always one. This is the structure behind 1985-A-13: a large search over neighboring quadratic values is replaced by one fixed modulus and an explicit equality witness.

# 2. Prime valuations

**Definition.** For a prime $p$ and nonzero integer $N$, $v_p(N)$ is the exponent of $p$ in its prime factorization. Extend to nonzero rationals by $v_p(a/b)=v_p(a)-v_p(b)$. Zero requires a separate convention and is excluded from formulas with finite valuations below.

Unique prime factorization follows from existence by repeated division and uniqueness using Euclid's lemma for primes. It gives the following coordinate rules.

**Theorem 2.1.**

$$v_p(AB)=v_p(A)+v_p(B),\qquad v_p(A^k)=k v_p(A),$$
$$v_p(\gcd(A,B))=\min(v_p(A),v_p(B)),\qquad
v_p(\operatorname{lcm}(A,B))=\max(v_p(A),v_p(B))$$

for positive $A,B$ and nonnegative integer $k$. In particular, $\gcd(A,B)\operatorname{lcm}(A,B)=AB$.

**Lemma 2.2 (valuation of a sum).** For nonzero rational numbers $A,B$ with $A+B\ne0$, we have $v_p(A+B)\ge\min(v_p(A),v_p(B))$, with equality when the two valuations differ.

**Proof.** Factor out the smaller prime power. When the exponents differ, the remaining sum is a nonmultiple of $p$ plus a multiple of $p$, so it is not divisible by $p$. Equal valuations can produce additional cancellation. $\square$

## 2.1 Perfect powers and rational integrality

For a positive integer $k$, a positive integer is a $k$th power exactly when every prime exponent is divisible by $k$. A rational number whose $k$th power is an integer is an integer: for a nonzero rational, negative prime valuations would remain negative after multiplication by $k$; zero is already an integer.

**Proposition 2.3 (coprime exponent matching).** If positive integers $a,b,r,s$ satisfy $a^r=b^s$ and $\gcd(r,s)=1$, then $a=t^s,b=t^r$ for a positive integer $t$.

**Proof.** For each prime, $r v_p(a)=s v_p(b)$. Coprimality forces $s\mid v_p(a)$ and $r\mid v_p(b)$; the quotient exponents agree. Assemble them into $t$. $\square$

**Historical use.** In 1985-A-07 this substitution reduces the multiplicative constraint before the additive constraint is used. Searching over the original two integers would ignore their shared prime structure.

## 2.2 Gcd and lcm constraints are coordinatewise

If $\gcd(x,y)=g$, write $x=gu,y=gv$ with $\gcd(u,v)=1$. If also $\operatorname{lcm}(x,y)=L$, then $uv=L/g$. Every prime power in $L/g$ must go wholly into one of $u,v$. It cannot be split between them. Thus ordered gcd/lcm pairs are naturally counted by assignments of distinct prime factors, not assignments of individual prime copies.

# 3. Divisor functions and exponent patterns

If $N=\prod_{i=1}^r p_i^{e_i}$, each positive divisor corresponds uniquely to an exponent choice $0\le f_i\le e_i$.

**Theorem 3.1.** The number and sum of positive divisors are

$$\tau(N)=\prod_i(e_i+1),\qquad
\sigma(N)=\prod_i(1+p_i+\cdots+p_i^{e_i}).$$

**Proof.** For the first, choose exponents independently. For the second, expand the product; every divisor occurs exactly once. $\square$

**Corollary 3.2.** $N$ has an odd number of divisors exactly when it is a square. More generally its $k$th-power divisors number $\prod_i(\lfloor e_i/k\rfloor+1)$.

**Theorem 3.3 (Euler's totient).** The number of integers in $\{1,\ldots,N\}$ coprime to $N$ is

$$\varphi(N)=N\prod_{p\mid N}\left(1-\frac1p\right).$$

**Proof.** Exclude multiples of each distinct prime divisor using inclusion-exclusion. Every product of selected distinct primes divides $N$, so each corresponding count is exactly $N$ divided by that product. Factor the alternating sum. $\square$

**Derived proposition 3.4 (fixed-sum reduced fractions).** For an integer $M>2$, positive reduced fractions $a/b<1$ with $a+b=M$ number $\varphi(M)/2$.

**Proof.** $\gcd(a,M-a)=\gcd(a,M)$. Among the $\varphi(M)$ coprime choices $1\le a<M$, pair $a$ with $M-a$. No pair is fixed, since $a=M/2$ would not be coprime for $M>2$. Exactly one member has $a<M-a$. $\square$

This is the counting reduction in 2014-I-03. The restriction $M>2$ matters: for $M=2$ the sole coprime numerator would give equality, not a fraction below one.

# 4. Congruences and legal division

Write $a\equiv b\pmod m$ for $m\mid a-b$, with $m\ge1$. Addition and multiplication preserve congruence. Division requires a condition.

**Theorem 4.1 (linear congruences).** The congruence $ax\equiv b\pmod m$ has a solution exactly when $g=\gcd(a,m)$ divides $b$. When it does, it reduces to

$$\frac ag x\equiv\frac bg\pmod{m/g},$$

which has one solution modulo $m/g$ and therefore $g$ solutions modulo $m$.

**Proof.** Necessity follows because $g$ divides both $ax$ and $m$. After division, $a/g$ is coprime to $m/g$ and has an inverse by Bézout, proving uniqueness modulo the smaller modulus. Its $g$ lifts give all solutions modulo $m$. $\square$

**Example.** $6x\equiv8\pmod{14}$ becomes $3x\equiv4\pmod7$, hence $x\equiv6\pmod7$. The two residues modulo $14$ are $6$ and $13$. Dividing while keeping modulus $14$ would lose a solution.

## 4.1 Chinese remainder theorem

**Theorem 4.2.** If $m,n$ are coprime, every pair of residue conditions $x\equiv a\pmod m$, $x\equiv b\pmod n$ specifies exactly one residue class modulo $mn$.

**Proof.** Write $x=a+mt$. Then $mt\equiv b-a\pmod n$ has one solution modulo $n$ by Theorem 4.1. Uniqueness follows because the difference of two solutions is divisible by both coprime moduli. $\square$

For noncoprime moduli, the two conditions are compatible exactly when $a\equiv b\pmod{\gcd(m,n)}$; when compatible they specify one class modulo $\operatorname{lcm}(m,n)$. This follows by the same substitution and linear-congruence theorem.

**Counting in an interval.** Once $x\equiv r\pmod m$ is known, write $x=r+mk$. The number in $L\le x\le U$ is

$$\max\left(0,\left\lfloor\frac{U-r}{m}\right\rfloor-\left\lceil\frac{L-r}{m}\right\rceil+1\right).$$

Do not round a real interval before checking whether its endpoints are included.

# 5. Polynomial congruences through prime powers

**Theorem 5.1 (idempotents).** If $m=\prod_{i=1}^r p_i^{e_i}$, the congruence $x^2\equiv x\pmod m$ has exactly $2^r$ residue solutions.

**Proof.** Consecutive integers $x,x-1$ are coprime. Thus each prime power $p_i^{e_i}$ dividing their product divides one factor entirely. Choose $x\equiv0$ or $1$ modulo each prime power and combine independently by CRT. $\square$

This is the central reduction in 2014-I-08. Solving modulo the composite modulus directly hides the independent choices.

**Theorem 5.2 (square roots of one).** Modulo an odd prime power $p^e$, $x^2\equiv1$ has exactly the two solutions $\pm1$. Modulo $2^e$, the number of solutions is one for $e=1$, two for $e=2$, and four for $e\ge3$; in the last case they are

$$1,-1,1+2^{e-1},-1+2^{e-1}\pmod{2^e}.$$

**Proof.** Factor $(x-1)(x+1)$. Their gcd divides two. For odd $p$, the entire prime power must divide one factor. For $p=2$, a solution is odd; of its two neighboring even numbers, one has exactly one factor of two. The other must then be divisible by $2^{e-1}$. Hence $x\equiv\pm1\pmod{2^{e-1}}$, giving the four listed lifts, each verified by squaring. The two small exponents are checked directly. $\square$

**Failure test.** A degree-two polynomial modulo a composite number can have more than two roots. The field root bound does not apply to a ring with zero divisors. Prime-power decomposition explains the extra roots.

# 6. Multiplicative order and exponential divisibility

**Definition.** If $\gcd(a,m)=1$ and $m>1$, the order $\operatorname{ord}_m(a)$ is the least positive $d$ with $a^d\equiv1\pmod m$.

**Theorem 6.1 (Euler).** $a^{\varphi(m)}\equiv1\pmod m$ when $a$ is coprime to $m$.

**Proof.** Multiplication by $a$ permutes the reduced residue classes. Multiply all their representatives and cancel their invertible product to obtain the result. $\square$

For prime $p$, this gives Fermat's theorem $a^{p-1}\equiv1\pmod p$ if $p\nmid a$.

**Theorem 6.2.** If $d=\operatorname{ord}_m(a)$, then $a^k\equiv1\pmod m$ exactly when $d\mid k$. In particular $d\mid\varphi(m)$.

**Proof.** Divide $k=qd+r$ with $0\le r<d$. Then $a^k\equiv a^r$. Minimality of $d$ forces $r=0$ when the power is one. The converse is immediate. $\square$

To prove an order equals a divisor $d$ of $\varphi(m)$, check $a^d\equiv1$ and $a^{d/q}\not\equiv1$ for each prime divisor $q$ of $d$. These tests exclude every proper divisor of $d$.

## 6.1 The gcd of two power differences

**Theorem 6.3.** For integers $a\ge2$ and $m,n\ge1$,

$$\gcd(a^m-1,a^n-1)=a^{\gcd(m,n)}-1.$$

**Proof.** For $m\ge n$, subtraction of $a^{m-n}(a^n-1)$ replaces the first entry by $a^{m-n}-1$. The Euclidean algorithm on the exponents reaches their gcd. $\square$

**Derived proposition 6.4.** For positive $m,n$,

$$\gcd(2^m+1,2^n-1)>1\quad\Longleftrightarrow\quad v_2(n)>v_2(m).$$

**Proof.** The consecutive odd integers $2^m-1$ and $2^m+1$ are coprime. Thus their gcds with $2^n-1$ multiply to $\gcd(2^{2m}-1,2^n-1)$. The first gcd is $2^{\gcd(m,n)}-1$, and the product is $2^{\gcd(2m,n)}-1$. The second gcd exceeds one exactly when these exponents differ, which occurs exactly when doubling $m$ increases its common power of two with $n$. $\square$

**Historical use.** This criterion turns the exponential gcd condition of 2021-II-09 into a comparison of valuation classes. The proof establishes sufficiency as well as necessity.

## 6.2 Do not reduce an exponent before checking the base

Euler's theorem applies only to units. To compute a power modulo $10^k$, separate the $2$-power and $5$-power factors of the base first. For a prime power $p^e$, if $a=p^s u$ with $p\nmid u$, then $a^n$ is zero modulo $p^e$ as soon as $sn\ge e$. Below that threshold, calculate the remaining unit part modulo the appropriately reduced power. Combine the prime-power answers by CRT.

# 7. Factorials, binomial coefficients, and carries

**Theorem 7.1 (Legendre).** For prime $p$ and nonnegative integer $n$,

$$v_p(n!)=\sum_{j\ge1}\left\lfloor\frac n{p^j}\right\rfloor.$$

**Proof.** Count one factor of $p$ from each multiple of $p$, a second from each multiple of $p^2$, and so on. Every prime factor occurrence in the factorial is counted once. $\square$

If $s_p(n)$ is the sum of the base-$p$ digits of $n$, this is also

$$v_p(n!)=\frac{n-s_p(n)}{p-1}.$$

To prove it, write $n=\sum_i d_ip^i$ in the floor sum and sum the geometric contributions of each digit.

**Corollary 7.2.** For integers $0\le k\le n$ and prime $p$,

$$v_p\binom nk=\sum_{j\ge1}\left(\left\lfloor\frac n{p^j}\right\rfloor-\left\lfloor\frac k{p^j}\right\rfloor-\left\lfloor\frac{n-k}{p^j}\right\rfloor\right).$$

Each summand is zero or one. It is one exactly when the lower $j$ digits of $k$ and $n-k$ create a carry into position $j$. Thus the valuation equals the number of carries in the base-$p$ addition $k+(n-k)=n$.

**Worked example.** $v_5(100!)=20+4=24$. The number of trailing decimal zeros is $\min(v_2(100!),v_5(100!))=24$, since factors of two are more numerous. For a different base $b=\prod p_i^{e_i}$, the number of trailing base-$b$ zeros is $\min_i\lfloor v_{p_i}(N)/e_i\rfloor$.

## 7.1 Binomial coefficients modulo a prime

**Theorem 7.3 (Lucas).** For a prime $p$ and nonnegative integers $n,k$, write $n=\sum_i n_ip^i$ and $k=\sum_i k_ip^i$ in base $p$. Then

$$\binom nk\equiv\prod_i\binom{n_i}{k_i}\pmod p,$$

where a digit choice $k_i>n_i$ contributes zero.

**Proof.** In characteristic $p$, $(1+x)^p\equiv1+x^p$. Hence

$$ (1+x)^n\equiv\prod_i(1+x^{p^i})^{n_i}\pmod p.$$

Because every chosen exponent digit is at most $n_i<p$, its representation has no carries and is unique. Compare the coefficient of $x^k$. $\square$

In particular, the number of binomial coefficients in row $n$ not divisible by $p$ is $\prod_i(n_i+1)$. This is an exponent-counting problem once the integer is written in the right base.

# 8. Lifting the exponent

Factoring $a^n-b^n$ tells us that $a-b$ divides it. A valuation theorem tells us exactly how many additional copies of a prime appear. That extra precision often turns a large-power divisibility problem into one line.

**Theorem 8.1 (odd-prime lifting).** Let $p$ be an odd prime, let $a,b$ be distinct positive integers with $p\mid a-b$ and $p\nmid ab$, and let $n\ge1$. Then

$$v_p(a^n-b^n)=v_p(a-b)+v_p(n).$$

**Proof.** First suppose $p\nmid m$. The quotient

$$\frac{a^m-b^m}{a-b}=a^{m-1}+a^{m-2}b+\cdots+b^{m-1}$$

is congruent to $mb^{m-1}\not\equiv0\pmod p$. Thus replacing $(a,b)$ by $(a^m,b^m)$ preserves the valuation of their difference.

Next write $A=B+p^s u$, where $s\ge1$ and $p\nmid Bu$. In the binomial expansion of $A^p-B^p$, the first term is $pB^{p-1}p^su$, of valuation $s+1$. The terms indexed $2\le j\le p-1$ have valuation at least $1+js>s+1$; the last term has valuation $ps>s+1$, because $p\ge3$. The smallest valuation is unique, so the whole sum has valuation $s+1$.

Write $n=mp^e$, with $p\nmid m$. Apply the first observation once and the second $e$ times. $\square$

The condition $p\nmid ab$ is essential. If both bases contain $p$, extract their common powers first. For a sum and odd $n$, apply the difference formula to $a$ and $-b$; the same proof works for nonzero integer bases provided the difference being valued is nonzero.

**Theorem 8.2 (the prime two).** For distinct positive odd integers $a,b$ and positive integer $n$,

$$v_2(a^n-b^n)=\begin{cases}v_2(a-b),&n\text{ odd},\\v_2(a-b)+v_2(a+b)+v_2(n)-1,&n\text{ even}.\end{cases}$$

**Proof.** An odd-exponent quotient has an odd number of odd terms, so is odd. For $n=2^e m$ with $m$ odd and $e\ge1$, remove the odd factor $m$ and factor

$$a^{2^e}-b^{2^e}=(a-b)(a+b)\prod_{j=1}^{e-1}(a^{2^j}+b^{2^j}).$$

Odd squares are $1\pmod8$. Every factor in the product is therefore $2\pmod8$ and has valuation one. There are $e-1$ such factors. $\square$

**Worked example.** Find the least positive $n$ for which $10^6\mid3^n-1$. Divisibility by five first requires $4\mid n$, since the order of three modulo five is four. For such $n$,

$$v_5(3^n-1)=v_5(3^4-1)+v_5(n/4)=1+v_5(n),$$

and

$$v_2(3^n-1)=1+2+v_2(n)-1=2+v_2(n).$$

The conditions are $v_5(n)\ge5$ and $v_2(n)\ge4$. They are both necessary and sufficient, so the least exponent is $2^4 5^5=50000$.

# 9. Digits, denominators, and repeating periods

## 9.1 Positional notation is a division algorithm

For an integer base $b\ge2$, every nonnegative integer has a unique base-$b$ expansion (apart from inserting leading zeros)

$$N=d_0+d_1b+\cdots+d_kb^k,\qquad 0\le d_i<b.$$

Existence follows by repeated division by $b$. Uniqueness follows by reducing two proposed expansions modulo $b$, deleting the equal last digits, and repeating. This proof is also an algorithm for digit constraints: eliminate the last digit first whenever divisibility is involved.

**Proposition 9.1.** An integer is congruent to its digit sum modulo $b-1$, and to its alternating digit sum modulo $b+1$.

**Proof.** Substitute $b\equiv1$ and $b\equiv-1$ into its positional expansion. $\square$

A block of $k$ ones is $(b^k-1)/(b-1)$. A repeated block with value $A$ and length $k$ has value $A(1+b^k+\cdots+b^{(r-1)k})$. Keep the block length even when its first digit is zero; it determines the place values.

## 9.2 Rational expansions

**Theorem 9.2.** Use the usual decimal expansion that is not eventually all nines. Let $u/v$ be in lowest terms, with integers $u,v$ and $v>0$, and write

$$v=2^a5^b d,\qquad \gcd(d,10)=1.$$

Its decimal expansion terminates exactly when $d=1$. Otherwise its least preperiod length is $\max(a,b)$ and its least period length is $\operatorname{ord}_d(10)$.

**Proof.** A decimal that repeats after $t$ digits with period $k$ satisfies $v\mid10^t(10^k-1)$ after clearing the reduced denominator. Since $10^k-1$ is coprime to ten, this forces $t\ge\max(a,b)$ and $d\mid10^k-1$. Conversely those two conditions make $10^t(u/v)$ have a purely periodic fractional part of period dividing $k$. Minimality gives the stated lengths. The terminating case is exactly $v\mid10^t$. $\square$

For example, $1/28$ has two nonrepeating digits and period six, because $28=2^2\cdot7$ and $\operatorname{ord}_7(10)=6$.

## 9.3 Count reduced numerators by denominator factors

**Theorem 9.3 (numerator feasibility).** Fix a positive integer $D$ and consider the fractions $N/D$ for integers $1\le N\le D$. For a positive integer $u$, define

$$D_0(u)=\prod_{\substack{p^e\parallel D\\p\nmid u}}p^e.$$

Then $u$ occurs as a reduced numerator if and only if $u\le D_0(u)$.

**Proof.** If $N/D=u/v$ is reduced, then $v\mid D$, $u\le v$, and $\gcd(u,v)=1$. Every prime power of $v$ therefore belongs to $D_0(u)$, so $v\le D_0(u)$. Conversely, if $u\le D_0(u)$, use the reduced fraction $u/D_0(u)$ and multiply numerator and denominator by $D/D_0(u)$. Its original numerator lies between one and $D$. $\square$

This is the structural shortcut behind **2022-I-13**. Partition possible numerators according to which primes dividing $D$ also divide $u$. Within each part, the bound is constant and inclusion–exclusion counts the allowed integers. This counts distinct numerators, whereas summing totients counts reduced fractions and can count the same numerator repeatedly.

\newpage

## 9.4 Extract a digit block only after controlling carries

**Lemma 9.4 (a carry certificate).** Let $b\ge2$ be an integer and let $c_m$ be nonnegative integers such that $X=\sum_{m\ge1}c_mb^{-m}$ converges. For integers $N\ge\ell\ge1$, put

$$T_N=\sum_{j\ge1}c_{N+j}b^{-j}.$$

If $T_N<1$, then

$$\lfloor b^N X\rfloor\equiv
\sum_{m=N-\ell+1}^{N}c_m b^{N-m}\pmod{b^\ell}.$$

One sufficient bound is obtained as follows. If $L$ is a nonnegative integer and $A,B\ge0$ satisfy $c_{N+j}\le A+Bj$ for every integer $j>L$, then

$$T_N\le\sum_{j=1}^{L}c_{N+j}b^{-j}
+b^{-L}\left(\frac{A+BL}{b-1}+\frac{Bb}{(b-1)^2}\right).$$

**Proof.** Split $b^N X$ into the integer $\sum_{m=1}^N c_m b^{N-m}$ and the nonnegative tail $T_N$. A tail below one leaves that integer unchanged under the floor. Terms with $m\le N-\ell$ are divisible by $b^\ell$, giving the congruence. For the bound, keep the first $L$ tail terms and replace each later coefficient by $A+Bj$. Write $j=L+k$ and use

$$\sum_{k\ge1}b^{-k}=\frac1{b-1},\qquad
\sum_{k\ge1}k b^{-k}=\frac b{(b-1)^2}.$$

The second identity follows by counting the coefficient of $b^{-k}$ in $(\sum_{j\ge1}b^{-j})(\sum_{j\ge0}b^{-j})$. $\square$

**Proposition 9.5 (a divisor-generating expansion).** For every integer $b\ge2$,

$$\sum_{k\ge1}\frac1{b^k-1}=\sum_{m\ge1}\tau(m)b^{-m}.$$

**Proof.** Expand each summand as $\sum_{j\ge1}b^{-kj}$. All terms are nonnegative, so regrouping by the product $m=kj$ preserves the sum; that product occurs $\tau(m)$ times. Convergence follows from $\tau(m)\le m$ and the convergent series $\sum m b^{-m}$. $\square$

**Historical use: 2026-II-09.** For $b=10$ and $N=100$, the last three coefficients are $\tau(98)=6$, $\tau(99)=6$, and $\tau(100)=9$. The first tail coefficient is $\tau(101)=2$. Pairing complementary divisors gives $\tau(m)\le2\sqrt m$, and $2\sqrt{100+j}\le20+j$ for $j\ge0$. Lemma 9.4 with $L=1$, $A=20$, $B=1$ therefore gives

$$0<T_{100}\le\frac2{10}+
\frac1{10}\left(\frac{21}{9}+\frac{10}{81}\right)
=\frac{361}{810}<1.$$

Thus the requested remainder is $100\cdot6+10\cdot6+9=669$. The coefficients $\tau(m)$ are not automatically decimal digits: some exceed nine. Knowing only that 101 is prime cannot rule out a carry from the entire later tail; the bound does.

# 10. Linear Diophantine equations and finite intervals

**Theorem 10.1.** Let $a,b>0$ and $g=\gcd(a,b)$. The equation $ax+by=c$ has integer solutions if and only if $g\mid c$. If $(x_0,y_0)$ is one solution, all are

$$x=x_0+\frac bg t,\qquad y=y_0-\frac ag t,\qquad t\in\mathbb Z.$$

**Proof.** Bézout gives a solution when $g\mid c$. Subtract two solutions to obtain $(a/g)(x-x_0)=-(b/g)(y-y_0)$. Coprimality forces $b/g\mid x-x_0$, giving the parameterization. Its substitutions all satisfy the equation. $\square$

Nonnegativity becomes an interval for $t$. Count the integers between the resulting ceiling and floor; do not approximate an interval's length and forget its endpoints.

**Example.** For $7x+11y=200$ with $x,y\ge0$, reduction modulo seven gives $4y\equiv4\pmod7$, so $y=1+7t$. Then $x=27-11t$, and $t=0,1,2$. There are three solutions.

**Theorem 10.2 (two-generator Frobenius theorem).** For coprime integers $a,b>1$, the greatest integer not expressible as $ax+by$ with $x,y\ge0$ is $ab-a-b$.

**Proof.** If $ab-a-b=ax+by$, then $ab=a(x+1)+b(y+1)$. Reduction modulo $a$ forces $a\mid y+1$, so $b(y+1)\ge ab$; the positive term $a(x+1)$ makes equality impossible.

Now let $N>ab-a-b$. There is a unique $y\in\{0,\ldots,a-1\}$ with $by\equiv N\pmod a$. Set $x=(N-by)/a$. Since

$$N-by>ab-a-b-b(a-1)=-a,$$

we have $x>-1$. As $x$ is integral, it is nonnegative. $\square$

The theorem requires coprimality. With three generators there is no direct substitution into this two-generator formula.

# 11. Factorization creates finite searches

## 11.1 Complete a product

**Proposition 11.1.** Positive integer solutions of

$$\frac1x+\frac1y=\frac1n$$

correspond bijectively to ordered positive factor pairs of $n^2$ through

$$(x-n)(y-n)=n^2.$$

Consequently there are $\tau(n^2)$ ordered solutions and $(\tau(n^2)+1)/2$ solutions with $x\le y$.

**Proof.** The original equation forces $x,y>n$. Multiplying and completing the product gives the identity, so both factors are positive. Conversely any positive factor pair gives a valid pair after adding $n$. Swapping the factors pairs all solutions except the unique diagonal pair $(n,n)$ of factors. $\square$

More generally, a term $xy+ax+by$ invites the completion $(x+b)(y+a)$. Record the shifts correctly: the coefficient of $x$ becomes the shift in the other factor.

## 11.2 Primitive Pythagorean triples

**Theorem 11.2.** Every primitive positive integer right triangle has, after exchanging its legs, the form

$$x=m^2-n^2,\qquad y=2mn,\qquad z=m^2+n^2,$$

where $m>n>0$, $\gcd(m,n)=1$, and $m,n$ have opposite parity. Conversely these conditions produce a primitive right triangle.

**Proof.** In a primitive triple, both legs cannot be odd because squares modulo four are zero or one; both cannot be even by primitivity. Let $y$ be even and $x,z$ odd. Then

$$\left(\frac{z+x}{2}\right)\left(\frac{z-x}{2}\right)=\left(\frac y2\right)^2.$$

The factors on the left are coprime: a common divisor divides both $z$ and $x$, whose gcd is one. Each factor must be a square. Write them $m^2,n^2$, with $m>n$, and obtain the formulas. The factors are coprime, and $m,n$ cannot both be odd because $z$ is odd.

Conversely the identity is immediate. A prime dividing both legs would divide $m$ and $n$, except possibly two; opposite parity makes the first leg odd and excludes two. Thus the triple is primitive. $\square$

For a nonprimitive triple multiply all three entries by a common factor. Bounding a hypotenuse bounds $m$ by its square root, making a finite search demonstrably exhaustive.

## 11.3 Consecutive positive sums

**Proposition 11.3.** A representation of $N$ as $k$ consecutive positive integers beginning with $a$ is equivalent to

$$2N=kq,\qquad q=2a+k-1,\qquad q\ge k+1,$$

where $k$ and $q$ have opposite parity.

**Proof.** Sum the arithmetic progression. Solving back gives $a=(q-k+1)/2$; the parity condition makes this integral and the inequality makes it positive. $\square$

This factor-pair test resolves all length and positivity conditions at once. It is the useful form for the extra length restrictions in **1987-A-11**.

# 12. Obstructions and infinite descent

A congruence can disprove a possibility quickly, but satisfying several congruences does not prove existence. Separate the obstruction stage from construction.

**Proposition 12.1.** A square is $0$ or $1$ modulo four; $0$, $1$, or $4$ modulo eight; and $0$ or $1$ modulo three.

**Proof.** Reduce the integer to the finitely many residue classes and square, or split into even and odd cases modulo eight. $\square$

**Theorem 12.2.** If a prime $p\equiv3\pmod4$ divides $x^2+y^2$, then it divides both $x$ and $y$. Consequently its valuation in a nonzero sum of two integer squares is even.

**Proof.** If $p\nmid y$, then $(xy^{-1})^2\equiv-1\pmod p$. Raising to $(p-1)/2$, an odd exponent, gives $(xy^{-1})^{p-1}\equiv-1$, contradicting Fermat's theorem. Thus $p\mid y$ and then $p\mid x$. Extract their common power of $p$ until at least one remaining coordinate is not divisible by $p$. The remaining sum is not divisible by $p$, so the extracted valuation is twice that common exponent. $\square$

This gives a necessary condition. Its converse is a deeper theorem and is not needed for the obstruction arguments here.

**Theorem 12.3 (a descent example).** The equation $x^2+y^2=3z^2$ has no nonzero integer solution.

**Proof.** Modulo three, both squares must be zero; hence $3\mid x,y$. Substituting shows $3\mid z$. Dividing all coordinates by three gives another solution. Choose a nonzero solution with least positive $|z|$; the new solution has smaller positive $|z|$, a contradiction. If $z=0$, both other coordinates are zero. $\square$

The descent proof has three indispensable parts: an integer measure bounded below, a transformation preserving all hypotheses, and strict decrease. An assertion that a process can be repeated is insufficient without those details.

# 13. Floor sums and divisor symmetry

**Theorem 13.1.** For $N\ge1$,

$$\sum_{k=1}^{N}\left\lfloor\frac Nk\right\rfloor=\sum_{m=1}^{N}\tau(m).$$

**Proof.** Both sides count ordered positive pairs $(a,b)$ with $ab\le N$. On the left fix $a$; on the right fix the product. $\square$

**Corollary 13.2 (hyperbola decomposition).** If $r=\lfloor\sqrt N\rfloor$, then

$$\sum_{k=1}^{N}\left\lfloor\frac Nk\right\rfloor=2\sum_{k=1}^{r}\left\lfloor\frac Nk\right\rfloor-r^2.$$

Every pair with product at most $N$ has at least one coordinate at most $r$. Count pairs satisfying each coordinate bound and subtract the $r^2$ pairs counted twice. Thus a sum of $N$ terms needs only about $\sqrt N$ terms.

**Proposition 13.3.** For positive coprime integers $a,b$,

$$\sum_{k=1}^{b-1}\left\lfloor\frac{ak}{b}\right\rfloor=\frac{(a-1)(b-1)}2.$$

**Proof.** None of $ak/b$ is integral. Pair $k$ with $b-k$; their floors add to $a-1$. Summing this identity over all $k$ counts the original sum twice. $\square$

If $a,b$ are not coprime, lattice points lie on the boundary, and the same formula is false. Handle those boundary points explicitly before pairing.

# 14. Extremal integers and encoding states

## 14.1 Put large exponents on small primes

**Theorem 14.1.** Among integers with a fixed multiset of positive prime exponents, the least integer assigns the largest exponent to two, the next largest to three, and so on, using consecutive primes.

**Proof.** Omitting a smaller prime while using a larger one can only increase the product. For $p<q$ and $a<b$,

$$p^a q^b>p^b q^a,$$

because their ratio is $(q/p)^{b-a}>1$. Exchange every inverted exponent pair. $\square$

To minimize an integer with a prescribed divisor count $D$, enumerate the multiplicative partitions $D=\prod(e_i+1)$ with $e_1\ge e_2\ge\cdots\ge1$, and compare the corresponding products of consecutive primes. There are at most $\lfloor\log_2 D\rfloor$ positive exponents. A plausible factorization is not a minimum until the other partitions are excluded or bounded.

**Example.** For $\tau(N)=12$, the exponent patterns are $(11)$, $(5,1)$, $(3,2)$, and $(2,1,1)$. They give $2048$, $96$, $72$, and $60$. The minimum is $60$.

## 14.2 A factorial as a shorter consecutive product

**Derived theorem 14.2.** Fix an integer $a\ge2$. Among integers $n>a$ such that $n!$ is the product of $n-a$ consecutive positive integers, the greatest is $(a+1)!-1$.

**Proof.** Such a block cannot end at or below $n$: it would be a subproduct of $1\cdot2\cdots n$ omitting $a\ge2$ factors, at least one of which exceeds one, and therefore be smaller than $n!$. Its last entry is at least $n+1$, so its first is at least $a+2$. Hence

$$n!\ge(a+2)(a+3)\cdots(n+1)=\frac{(n+1)!}{(a+1)!}.$$

It follows that $n\le(a+1)!-1$. At this endpoint the displayed block has exactly $n-a$ terms and its product equals $n!$, proving attainment. $\square$

This is the shortening mechanism in **1990-A-11**. For $a=1$, the product $2\cdot3\cdots n$ works for every $n\ge2$, so there is no finite maximum. The omitted-factor argument explains exactly why the hypothesis changes the result.

## 14.3 Mixed-radix notation

**Theorem 14.3 (factorial representation).** Every nonnegative integer has a unique finite expansion

$$N=\sum_{k\ge1}a_k k!,\qquad 0\le a_k\le k.$$

**Proof.** Obtain $a_1$ as the remainder on division by two; divide the quotient by three to obtain $a_2$; continue. The quotients eventually vanish. For uniqueness, compare two expansions modulo two, remove their common first digit, divide by two, and repeat modulo three, four, and so on. Equivalently,

$$\sum_{k=1}^{m}k\,k!=(m+1)!-1$$

shows that all lower digits together cannot replace a unit of the next place. The identity telescopes using $k\,k!=(k+1)!-k!$. $\square$

## 14.4 Recognize a counter inside a recurrence

A recurrence may describe a familiar operation in unfamiliar symbols. If a state records a finite set of occupied prime positions and a step deletes the initial occupied positions, then inserts the first unoccupied one, it is binary increment: consecutive terminal ones change to zeros, and the first zero changes to one. Assign weight $2^j$ to position $j$ and prove the weight increases by exactly one:

$$2^r-\sum_{j=0}^{r-1}2^j=1.$$

This encoding is the essential simplification in **2014-II-15**. The proof must establish that each update has precisely this rule; a few matching initial terms only suggest the encoding.

# 15. A short-proof protocol

1. **Factor the modulus or integer.** A statement about divisibility by $M$ is a list of valuation conditions, one for each prime power in $M$.
2. **Separate units from nonunits.** Euler and multiplicative order apply only after checking coprimality.
3. **Extract the gcd.** Coprime factors of a perfect power are individually perfect powers. This is often the decisive step.
4. **Choose the parameter with the smallest range.** A divisor, an exponent, or a reduced residue usually has a shorter range than the original integer.
5. **Prove the converse.** A parameterization must produce every valid object and no invalid ones. A congruence restriction alone rarely completes a count.
6. **Finish with the boundary.** Check zero, one, equality, sign, and whether the stated interval includes its endpoints.

A search is a proof only after its range and its predicate are justified. Exact arithmetic is particularly valuable for checking residue counts and small examples; it should support the structural argument, not replace an unexplained step.

# 16. Training problems

The following exercises are original instances of the methods above. They are deliberately small enough that a structural solution can be checked completely.

1. Find the greatest possible value of $\gcd(n^2+7,(n+1)^2+7)$ for positive integers $n$.
2. Find the least positive $N$ such that $72N$ is a perfect cube.
3. Count ordered pairs of positive integers with gcd $12$ and lcm $360$.
4. Compute $\tau(360)$ and $\sigma(360)$.
5. Count unordered pairs of coprime positive integers whose sum is $100$.
6. Find the least nonnegative solution of $x\equiv2\pmod7$, $x\equiv5\pmod9$.
7. Solve $6x\equiv9\pmod{15}$.
8. Count the solutions of $x^2\equiv x\pmod{840}$ modulo $840$.
9. Count the square roots of one modulo $360$.
10. Find $\gcd(2^{84}-1,2^{30}-1)$.
11. Find $v_3(10^{81}-1)$.
12. Find $v_2(7^{100}-1)$.
13. Find the number of trailing zeros of $100!$ in base twelve.
14. How many binomial coefficients in row $100$ of Pascal's triangle are odd, counting both ends?
15. Find the least decimal preperiod and period lengths of $1/84$.
16. How many distinct reduced numerators occur among $N/12$, $1\le N\le12$?
17. Count nonnegative integer solutions of $7x+11y=200$.
18. Find the largest integer not expressible as $8x+13y$ with $x,y\ge0$ integers.
19. Count positive integer solutions of $1/x+1/y=1/12$ with $x\le y$.
20. Find all primitive positive integer right triangles whose hypotenuse is $25$.
21. List the lengths greater than one of representations of $45$ as a sum of consecutive positive integers.
22. Show that $2025$ cannot be written as $x^2+y^2=3z^2$ with $z$ an integer and $(x,y)\ne(0,0)$.
23. Compute $\sum_{k=1}^{20}\lfloor20/k\rfloor$.
24. Find the least positive integer with exactly eighteen positive divisors.
25. Write $100$ in factorial representation.
26. Prove that no integer square is congruent to $7$ modulo eight.

# 17. Complete exercise solutions

**1.** Proposition 1.4 gives $\gcd(n^2+7,(n+1)^2+7)=\gcd(29,2n+1)$. Thus the maximum is $29$, attained at $n=14$.

**2.** Since $72=2^3 3^2$, the missing exponents modulo three are zero for two and one for three. The minimum is $N=3$, giving $216=6^3$; any other prime factor would increase $N$.

**3.** Divide both entries by twelve. Their gcd is one and lcm is thirty, so each of the prime factors $2,3,5$ must be assigned wholly to one entry. There are $2^3=8$ ordered pairs.

**4.** $360=2^3 3^2 5$. Therefore $\tau(360)=4\cdot3\cdot2=24$ and $\sigma(360)=15\cdot13\cdot6=1170$.

**5.** The ordered pairs are $(a,100-a)$ with $1\le a<100$ and $\gcd(a,100)=1$. There are $\varphi(100)=40$. No pair has equal entries and gcd one, so the unordered count is $20$.

**6.** Put $x=2+7t$. Modulo nine, $7t\equiv3$, giving $t\equiv3\pmod9$. Thus $x\equiv23\pmod{63}$, and the least nonnegative solution is $23$.

**7.** Divide by three and reduce the modulus to five: $2x\equiv3\pmod5$, so $x\equiv4\pmod5$. Modulo fifteen the solutions are $4,9,14$.

**8.** $840=2^3\cdot3\cdot5\cdot7$ has four distinct prime factors. For each prime power an idempotent is zero or one. CRT gives $2^4=16$ solutions.

**9.** $360=8\cdot9\cdot5$. There are four roots modulo eight, two modulo nine, and two modulo five. CRT gives $16$ roots.

**10.** The Euclidean exponent identity gives $2^{\gcd(84,30)}-1=2^6-1=63$.

**11.** Odd-prime lifting gives $v_3(10-1)+v_3(81)=2+4=6$.

**12.** The even-exponent formula gives $v_2(6)+v_2(8)+v_2(100)-1=1+3+2-1=5$.

**13.** $v_2(100!)=50+25+12+6+3+1=97$ and $v_3(100!)=33+11+3+1=48$. Since $12=2^2\cdot3$, the answer is $\min(\lfloor97/2\rfloor,48)=48$.

**14.** $100=64+32+4$ has three ones in binary. Lucas's theorem gives $2^3=8$ odd coefficients.

**15.** $84=2^2\cdot3\cdot7$, so the preperiod is two. Modulo $21$, $10^2\equiv16$, $10^3\equiv13$, and $10^6\equiv1$. Neither exponent one, two, nor three gives one; these are all proper divisors of six. Thus the period is six.

**16.** If $u$ is coprime to six, the bound is twelve, giving $1,5,7,11$. If $u$ is divisible by two but not three, the bound is three, giving only $2$. If divisible by three but not two, the bound is four, giving only $3$. If divisible by both, the bound is one, giving none. The six distinct numerators are $1,2,3,5,7,11$.

**17.** As in Chapter 10, $y=1+7t$ and $x=27-11t$; nonnegativity permits $t=0,1,2$. The answer is three.

**18.** Since eight and thirteen are coprime, the answer is $8\cdot13-8-13=83$.

**19.** The factorization is $(x-12)(y-12)=144=2^4 3^2$. There are $15$ ordered factor pairs and $(15+1)/2=8$ with the first factor at most the second.

**20.** Primitive triples require $m^2+n^2=25$ with $m>n>0$. The only pair is $(4,3)$: testing $m=4$ gives $n=3$, while $m=1,2,3$ cannot exceed $n$ and achieve the sum. The legs are $7$ and $24$. Thus the triangle is $(7,24,25)$, up to exchanging the legs. The familiar $(15,20,25)$ is not primitive.

**21.** Factor $90=kq$ with $q\ge k+1$ and opposite parity. For $k>1$, the allowed lengths are $2,3,5,6,9$, with starting terms $22,14,7,5,1$, respectively. No larger $k$ works because $k(k+1)>90$ for $k\ge10$; among $2$ through $9$, only these divide ninety with the required parity.

**22.** Theorem 12.3 rules out every nonzero integer solution of $x^2+y^2=3z^2$, so it rules out the specified value in particular. Alternatively, $3z^2=2025$ would imply $z^2=675=3^3 5^2$, whose odd three-adic valuation prevents it being a square.

**23.** Here $r=4$. The hyperbola formula gives $2(20+10+6+5)-16=66$.

**24.** The multiplicative partitions of eighteen give exponent patterns $(17)$, $(8,1)$, $(5,2)$, and $(2,2,1)$. Their least integers are $2^{17}$, $2^8\cdot3=768$, $2^5\cdot3^2=288$, and $2^2\cdot3^2\cdot5=180$. Thus the answer is $180$.

**25.** Greedy division gives $100=4\cdot4!+0\cdot3!+2\cdot2!+0\cdot1!$. All digits satisfy $0\le a_k\le k$, so this is the unique factorial representation.

**26.** If an integer is odd, write it $2t+1$; its square is $4t(t+1)+1\equiv1\pmod8$. If it is even, write it $2t$; its square is zero modulo eight when $t$ is even and four when $t$ is odd. None is seven.

# 18. Reading and provenance

This book presents classical number theory with newly written proofs and archive-driven problem-solving connections. The theorem names identify established results; the organizing principles and shortcuts are not claims of discovering new mathematics. The companion problem files cite their historical sources and state where those sources were consulted.

For further training, the [number theory unit index in Evan Chen's OTIS catalogue](https://catalog.evanchen.cc/N/) offers a progression of Olympiad topics. The [MOTP lifting-the-exponent notes](https://jpsaha.github.io/MOTP/assets/pdf/NumberTheory/LTE.pdf) are a focused supplementary reference. Hypotheses are repeated in this book because the exceptional behavior of two, and the distinction between units and nonunits, are frequent sources of incorrect short solutions.
