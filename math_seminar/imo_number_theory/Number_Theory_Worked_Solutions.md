---
title: "Olympiad Number Theory: Worked Solutions"
author: "Ayden Bi"
date: "Research edition • 6 November 2026"
lang: en-US
---

# Reading this volume {.unnumbered}

These sixteen checked, rewritten expositions are the core of a larger research archive. They are selected for depth and transfer value, not offered as a verified ranking of the hardest problems. Thirteen are shortlist-only cases; N08, N15 and N16 are actual IMO problems, and N12 is a particularly short advanced solution to a difficult shortlist problem. Original contest attribution is stated in every case. The supplied solutions elsewhere in the archive remain explicitly unreviewed.

Write $v_p(m)$ for the exponent of the prime $p$ in a nonzero integer $m$; the valuation of $m!$ is written $v_p(m!)$, avoiding a source convention that used the same symbol for a different function. The companion theory volume proves the tools used here, including the lifting lemma and the quadratic-character identities. No computed search is used to justify an infinite assertion.

# N01. A valuation makes the square small

**Source:** IMO shortlist 2006, N1. **Record:** `imo_2006_bc0ae3`.

**Problem.** Determine all integer solutions of $1+2^x+2^{2x+1}=y^2$.

**Solution.** If $x<0$, the left side lies in $(1,2]$, which contains no integer square. If $x=0$, $y=\pm2$. Assume $x>0$ and, by symmetry, $y>0$. Then $y$ is odd and
$$2^x(1+2^{x+1})=(y-1)(y+1).$$
Exactly one of $y-1,y+1$ has valuation one at $2$, while the other has valuation at least two. Therefore $x\ge3$, and $y=2^{x-1}m+\varepsilon$ for a positive odd $m$ and $\varepsilon\in\{-1,1\}$. Substitution gives
$$1-\varepsilon m=2^{x-2}(m^2-8).$$
If $\varepsilon=1$, the right side is nonpositive, so the only possible positive odd $m$ is $1$, which fails the equation. If $\varepsilon=-1$, positivity gives $m\ge3$, while $1+m\ge2(m^2-8)$ implies $m\le3$. Hence $m=3$, $2^{x-2}=4$, and $(x,y)=(4,23)$. Restoring the sign of $y$, the complete answer is $(0,\pm2),(4,\pm23)$.

**Certificate.** The factorization fixes the large power of two in a neighboring pair; the remaining odd quotient is trapped by a quadratic inequality.

# N02. Sample digits at exponentially growing places

**Source:** IMO shortlist 2006, N2. **Record:** `imo_2006_472d44`.

**Problem.** A decimal expansion represents a rational number in $(0,1)$. Form a new decimal by taking its digits in positions $2,4,8,16,\ldots$. Prove that the new number is rational (possibly an endpoint such as zero).

**Solution.** A rational decimal is eventually periodic. Let its period length be $d$, after an initial segment. The sequence $2^n\bmod d$ is eventually periodic: multiplication by two is a deterministic map on the finite set of residues modulo $d$, so two equal states force all subsequent states to agree after the same shift. For large $n$, the index $2^n$ is beyond the initial segment. Equal residues modulo $d$ then select equal digits of the original decimal. Therefore the sampled digits are eventually periodic, and their decimal is rational.

**Certificate.** Only eventual periodicity of the sampling indices modulo the original period matters. The argument works in any base and also for terminating expansions. The source's assertion that the sampled number necessarily lies in $(0,1)$ is unnecessary and need not hold.

# N03. One modulus replaces all moduli

**Source:** IMO shortlist 2007, N2. **Record:** `imo_2007_886291`.

**Problem.** Integers $b,n>1$ satisfy: for every integer $k>1$, some integer $a$ has $a^n\equiv b\pmod k$. Prove that $b$ is an integer $n$th power.

**Solution.** Use only $k=b^2$. If $p^\alpha\Vert b$, then $a^n\equiv b\pmod {p^{2\alpha}}$, so $v_p(a^n)=\alpha$: congruent numbers have the same valuation when the congruence modulus has strictly larger valuation. Thus $n\mid\alpha$ for each prime factor of $b$. Writing $b=\prod p^{\alpha_p}$ gives $b=(\prod p^{\alpha_p/n})^n$.

**Certificate.** Select a modulus whose prime-power precision exceeds every valuation of the target. No general local-to-global principle is being assumed.

# N04. Multiply three divided differences

**Source:** IMO shortlist 2008, N1. **Record:** `imo_2008_dbd5d0`.

**Problem.** For positive integer $n$, prime $p$, and arbitrary integers $a,b,c$, suppose $a^n+pb=b^n+pc=c^n+pa$. Prove $a=b=c$.

**Solution.** If two variables coincide, the equations force the third to coincide too. Otherwise they are pairwise distinct. Dividing the three difference equations and multiplying gives
$$\frac{a^n-b^n}{a-b}\frac{b^n-c^n}{b-c}\frac{c^n-a^n}{c-a}=-p^3.$$
If $n$ is odd, each divided difference is positive because $x^n$ is strictly increasing, a contradiction. Thus $n=2k$.

If $p$ is odd, all three integer factors above must be odd. The sum $a^{n-1}+a^{n-2}b+\cdots+b^{n-1}$, with an even number of terms, is odd only when $a,b$ have opposite parity. The same would hold cyclically, which is impossible for three integers.

Hence $p=2$. The original equations imply that $a,b,c$ have the same parity. Factoring each even power and dividing the product by $8$ yields six integer factors with product $-1$:
$$\prod_{(u,v)=(a,b),(b,c),(c,a)}
\left(\frac{u^k+v^k}{2}\right)
\left(\frac{u^k-v^k}{u-v}\right)=-1.$$
All factors equal $\pm1$. If $k$ is even, $a^k+b^k=2$ forces $|a|=|b|=1$, making the other factor zero, impossible. If $k$ is odd, the nonzero even integer $a+b$ divides $a^k+b^k=\pm2$, so $a+b=\pm2$. Similarly $b+c,c+a\in\{-2,2\}$. Two of these three sums are equal, forcing two variables equal, again a contradiction.

**Certificate.** A cyclic system becomes a product with only one prime factor. Signs and parity then exhaust all possibilities.

# N05. Simultaneous factorial valuations

**Source:** IMO shortlist 2007, N7. **Record:** `imo_2007_e1c86b`.

**Problem.** For any positive integer $d$ and finitely many primes $p_1,\ldots,p_k$, show that infinitely many $n>0$ satisfy $d\mid v_{p_i}(n!)$ for every $i$.

**Solution.** Define $f(n)=(v_{p_1}(n!),\ldots,v_{p_k}(n!))\bmod d$ for $n\ge0$, and let $S$ be its finite image. Choose one representative $n_s$ for every $s\in S$, and let $N=\max n_s$. Choose $g$ with every $p_i^g>N$, and put $P=(p_1\cdots p_k)^g$.

For $0\le r\le N$ and positive $m$, we have
$$v_{p_i}((mP+r)!)=v_{p_i}((mP)!)+v_{p_i}(r!).$$
Indeed, for $1\le j\le r<p_i^g$, $v_{p_i}(mP+j)=v_{p_i}(j)$; sum these equalities. It follows that $f(mP+n_s)=f(mP)+s$. Translation by $f(mP)$ is injective on the finite group $(\mathbb Z/d\mathbb Z)^k$, so these $|S|$ states are distinct. They all belong to $S$, hence they exhaust $S$. In particular one is the zero state, which belongs to $S$ because $f(0)=0$.

Every interval $[mP,mP+N]$ therefore contains a suitable $n$. Since $P>N$, these intervals are disjoint, giving infinitely many such integers.

**Certificate.** A finite set that contains an injective translate of itself contains the whole translate. The proof gives bounded gaps between blocks containing solutions.

# N06. Finite agreement versus eternal agreement

**Source:** IMO shortlist 2009, N2. **Record:** `imo_2009_cf1420`.

**Problem.** Call an integer balanced when its number of prime factors, counted with multiplicity, is even; include $1$. (a) Find distinct positive $a,b$ for which $(n+a)(n+b)$ is balanced for all $1\le n\le50$. (b) Prove that if this holds for every positive $n$, then $a=b$.

**Solution.** Let $\epsilon(m)=\Omega(m)\bmod2$, where $\Omega$ counts prime factors with multiplicity. Then $\epsilon(uv)=\epsilon(u)+\epsilon(v)\pmod2$. There are only $2^{50}$ possible vectors $(\epsilon(t+1),\ldots,\epsilon(t+50))$. Among $2^{50}+1$ positive choices of $t$, two, called $a,b$, have equal vectors. Their products are balanced for the first fifty inputs, proving (a).

For (b), suppose $a<b$ and put $h=b-a$. For every sufficiently large integer $k$, the input $n=kh-a$ is positive and gives $(n+a)(n+b)=k(k+1)h^2$. Balance forces $\epsilon(k)=\epsilon(k+1)$. Thus $\epsilon$ is eventually constant. This is impossible because arbitrarily large squares have value zero and arbitrarily large primes have value one. Consequently $a=b$, which indeed works.

**Certificate.** Pigeonhole proves any fixed finite agreement; a scaling substitution turns infinite agreement into a false eventual constancy.

# N07. Divisibility squeezes a function

**Source:** IMO shortlist 2013, N1. **Record:** `imo_2013_a67bc4`.

**Problem.** Find all $f:\mathbb Z_{>0}\to\mathbb Z_{>0}$ satisfying $m^2+f(n)\mid mf(m)+n$ for all positive $m,n$.

**Solution.** Set $m=n=2$. The positive multiple $2f(2)+2$ of $4+f(2)$ is smaller than twice that divisor, so it equals the divisor. Thus $f(2)=2$. Now $m=2$ gives $4+f(n)\mid4+n$, hence $f(n)\le n$. On the other hand, setting $m=n$ and comparing a positive dividend with its divisor gives
$$nf(n)+n\ge n^2+f(n),\qquad(n-1)(f(n)-n)\ge0.$$
For $n\ge2$ this gives $f(n)\ge n$; for $n=1$, positivity and the upper bound give $f(1)=1$. Thus $f(n)=n$, and direct substitution verifies it.

**Certificate.** A small anchor forces an exact value, then divisibility supplies matching upper and lower bounds.

# N08. Two primes eliminate a factorial

**Source:** IMO 2019, Problem 4; shortlist N1. **Record:** `imo_2019_8eb868`.

**Problem.** Find positive integers $m,n$ with $m!=\prod_{i=0}^{n-1}(2^n-2^i)$.

**Solution.** Write the product as $L_n=2^{n(n-1)/2}\prod_{j=1}^n(2^j-1)$. For $n=1,2$, we obtain $(m,n)=(1,1),(3,2)$. For $n=3$, $L_n=168$ lies strictly between $5!$ and $6!$; for $n=4$, $L_n=20160$ lies strictly between $7!$ and $8!$.

Assume $n\ge5$ and put $t=\lfloor n/2\rfloor$. Only even $j$ contribute factors of $3$, and the lifting lemma gives $v_3(2^{2k}-1)=1+v_3(k)$. Hence
$$v_3(L_n)=t+v_3(t!)=v_3((3t)!).$$
The valuation of factorials strictly rises at each multiple of three, so $3t\le m\le3t+2$. Meanwhile every fifth factor $2^j-1$ is divisible by $31$, giving
$$\lfloor n/5\rfloor\le v_{31}(m!)=\sum_{r\ge1}\lfloor m/31^r\rfloor<m/30.$$
For $n\ge5$, $\lfloor n/5\rfloor\ge n/10$, so $m>3n$, contrary to $m\le3n/2+2$. No further solutions exist.

**Certificate.** One small prime tightly bounds the factorial index; another prime makes that bound impossible.

# N09. A cubic equation collapses to a short list

**Source:** IMO shortlist 2019, N2. **Record:** `imo_2019_199a44`.

**Problem.** Classify positive integer triples satisfying $a^3+b^3+c^3=(abc)^2$.

**Solution.** Order them $a\ge b\ge c$. We have $a<b^2c^2\le3a$ and $b^3+c^3=a^2(b^2c^2-a)\ge a^2$. Consequently
$$18b^3\ge9(b^3+c^3)\ge9a^2\ge b^4c^4\ge b^3c^5.$$
Thus $c^5\le18$, forcing $c=1$. If $a=b$, the equation becomes $b^3(b-2)=1$, impossible. Hence $a>b$. Then $b^3+1<a^3$, so $a<b^2<2a$. As $b^3+1=a^2(b^2-a)\ge a^2$, we obtain $4(b^3+1)>b^4$, forcing $b\le4$.

The case $b=1$ is impossible. For $b=2$, the equation factors as $(a-3)(a^2-a-3)=0$, giving $a=3$. For $b=3$, an integer root of $a^3-9a^2+28$ must divide $28$ and satisfy $3<a<9$; the only candidates $4,7$ both fail. For $b=4$, a root of $a^3-16a^2+65$ must divide $65$ and satisfy $4<a<16$; the candidates $5,13$ both fail. Therefore all solutions are the permutations of $(1,2,3)$, which satisfy the equation.

**Certificate.** A positive integer quotient is at least one. Combined with ordering, this bounds the smallest variable before any finite check.

# N10. Polynomial-root closure fills the integers

**Source:** IMO shortlist 2019, N3. **Record:** `imo_2019_05dd86`.

**Problem.** A set $S\subseteq\mathbb Z$ contains $2^a-2^b$ for all positive $a,b$ and contains every integer root of every nonconstant polynomial with coefficients in $S$. Prove $S=\mathbb Z$.

**Solution.** We have $0,2,-2\in S$. The polynomials $2x+2$ and $2x-2$ show $-1,1\in S$. For any $u\in S$, the polynomial $x+u$ shows $-u\in S$.

Every positive integer $n$ divides some positive element of $S$. Indeed, write $n=2^\alpha t$ with $t$ odd. Choose a positive $r$ with $2^r\equiv1\pmod t$ (for $t=1$, any $r>0$ works). Then $N=2^{\alpha+1+r}-2^{\alpha+1}$ is a positive multiple of $n$ and belongs to $S$.

Induct on $n\ge2$, assuming $0,1,\ldots,n-1\in S$. Choose such a positive multiple $N\in S$ and write its base-$n$ expansion $N=a_kn^k+\cdots+a_1n$, with $0\le a_i<n$ and $a_k>0$. All coefficients of $a_kx^k+\cdots+a_1x-N$ lie in $S$. Its integer root $n$ therefore lies in $S$. Induction and closure under negation give all integers.

**Audit note.** If the phrase “polynomial” is interpreted to include the zero polynomial in the closure condition, the result is immediate from $0\in S$. The nonconstant, nonzero-leading-coefficient interpretation above is the substantive version; its proof also establishes the literal version.

**Certificate.** Available digits plus one available multiple encode a missing integer as a polynomial root.

# N11. Classify the good binomial indices

**Source:** IMO shortlist 2019, N5. **Record:** `imo_2019_aedde5`.

**Problem.** For fixed positive $a$, call $b>0$ good if $an+1\mid\binom{an}{b}-1$ whenever $an\ge b$. If $b$ is good and $b+2$ is not, prove $b+1$ prime.

**Solution.** We prove a stronger classification: $b$ is good exactly when $b$ is even and every prime at most $b$ divides $a$.

Suppose $p\le b$ is prime and $p\nmid a$. Put $t=v_p(b!)$. Choose an arbitrarily large positive $n$ such that $an\equiv p-1\pmod {p^{t+1}}$, possible because $a$ is invertible modulo $p^{t+1}$. In the numerator $an(an-1)\cdots(an-b+1)$, the factor $an-p+1$ is divisible by $p^{t+1}$. After division by $b!$, the binomial coefficient is still divisible by $p$. But $p\mid an+1$, so it cannot be congruent to one modulo $an+1$. Thus a good $b$ must have every prime up to $b$ dividing $a$.

Under that condition, $b!$ is invertible modulo $an+1$. Reducing the numerator term by term gives
$$\binom{an}{b}\equiv(-1)^b\pmod {an+1}.$$
This is one for all eligible $n$ exactly when $b$ is even; for odd $b$, take $an+1>2$. The classification follows.

Now $b$ and $b+2$ are even. Since only the second fails, some prime $q\le b+2$ does not divide $a$, while every prime $\le b$ does. Hence $q=b+1$ or $b+2$. The latter is an even integer at least four, so $q=b+1$ is prime.

**Certificate.** First prove the exact criterion. A carefully chosen prime-power residue prevents illegal cancellation of a nonunit factorial.

# N12. A Jacobi-symbol obstruction

**Source:** IMO shortlist 2022, N8. **Record:** `imo_2022_264ed6`.

**Problem.** Show $2^n+65$ never divides $5^n-3^n$ for positive integer $n$.

**Solution.** Suppose it does, and set $m=2^n+65$. If $n$ is even, $3\mid m$ but $3\nmid5^n-3^n$, impossible. The case $n=1$ is immediate, so assume $n\ge3$ odd. Then $m$ is odd, coprime to $15$, and $m\equiv1\pmod4$, $m\equiv1\pmod3$, $m\equiv2$ or $3\pmod5$.

For the Jacobi symbol, multiplicativity, oddness of $n$, and quadratic reciprocity give
$$\left(\frac{5^n}{m}\right)=\left(\frac5m\right)=\left(\frac m5\right)=-1,
\qquad
\left(\frac{3^n}{m}\right)=\left(\frac3m\right)=\left(\frac m3\right)=1.$$
These contradict $5^n\equiv3^n\pmod m$. Notice that $m$ need not be prime; using Legendre symbols with denominator $m$ would be invalid. The Jacobi identities used here are proved in the theory volume.

**Certificate.** Apply a multiplicative character to a purported congruence. A hard divisibility test becomes two small residue calculations.

# N13. Reverse the ordered divisor list

**Source:** IMO shortlist 2023, N1. **Record:** `imo_2023_2e005b`.

**Problem.** Let $1=d_1<\cdots<d_k=n$ be all positive divisors of a composite $n$. Classify $n$ for which $d_i\mid d_{i+1}+d_{i+2}$ for $1\le i\le k-2$.

**Solution.** We prove $d_i\mid d_{i+1}$ for every $i$. The base case $i=1$ is immediate. Suppose $2\le i\le k-1$ and $d_{i-1}\mid d_i$. The hypothesis at index $i-1$ then gives $d_{i-1}\mid d_{i+1}$. The reciprocal identity $d_jd_{k+1-j}=n$ and the hypothesis at index $k-i$ give
$$\frac{d_{i+1}}{d_i}+\frac{d_{i+1}}{d_{i-1}}\in\mathbb Z.$$
The second summand is an integer, so the first is too. This proves the induction.

Thus all divisors form a divisibility chain. Two distinct prime divisors could not both lie in such a chain, so $n=p^r$ for a prime $p$ and $r\ge2$. Conversely its divisors are $1,p,\ldots,p^r$, and each divides the sum of the next two. These are exactly the solutions.

**Certificate.** The reversal $d\mapsto n/d$ supplies a second divisibility relation that upgrades a sum condition to a chain condition.

# N14. The odd part controls all divisors

**Source:** IMO shortlist 2024, N1. **Record:** `imo_2024_268bb8`.

**Problem.** Find positive $n$ such that every divisor $d$ of $n$ has either $d+1\mid n$ or $d+1$ prime.

**Solution.** Write $n=2^km$ with $m$ odd. If $m=1$, then $k\le2$: otherwise $8\mid n$ but $9\nmid n$ and $9$ is composite. This gives $n=1,2,4$.

If $m>1$, then $m+1$ is even and composite, so $m+1\mid n$. Since it is coprime to $m$, it must be $2^j$ with $2\le j\le k$. Thus $n=2^k(2^j-1)$. If $k\ge3$, neither $2^k+1$ nor $2^{k-1}+1$ divides $n$: both are odd, the first exceeds $m$, and the second exceeds $m$ unless $j=k$. In that last case, a divisor $2^{k-1}+1$ of $2^k-1=2(2^{k-1}+1)-3$ would divide $3$, which is impossible since it is at least five.

Because $2^k,2^{k-1}$ divide $n$, both successors would therefore have to be prime. But one of the consecutive exponents $k,k-1$ is odd and at least three; its successor $2^{\text{odd}}+1$ is a composite multiple of three. Hence $k=2$, forcing $j=2$ and $n=12$. Direct checking of the divisors of $1,2,4,12$ verifies all four answers.

**Certificate.** Apply a universal divisor condition first to the odd part, then to two neighboring powers of two.

# N15. Vieta jumping with every inequality checked

**Source:** IMO 1988, Problem 6. Official paper: [PDF](https://www.imo-official.org/assets/documents/problems/1988/1988_eng.pdf).

**Problem.** For positive integers $a,b$ with $ab+1\mid a^2+b^2$, prove that $(a^2+b^2)/(ab+1)$ is a perfect square.

**Solution.** Put the quotient equal to the positive integer $k$. If a nonsquare $k$ occurs, choose a corresponding pair with minimal $a+b$ and arrange $a\ge b$. Regarding the equation as a quadratic in $a$, its other root is the integer
$$a'=kb-a,\qquad aa'=b^2-k.$$
If $a'<0$, then $a\ge kb+1\ge k+1$, while $a(a-kb)=k-b^2$ implies $a\le k-b^2<k$, a contradiction. If $a'=0$, then $k=b^2$, contrary to the choice of $k$. Thus $a'>0$.

Finally,
$$k=\frac{a^2+b^2}{ab+1}<\frac ab+\frac ba,$$
so $a'=kb-a<b^2/a\le b$. The pair $(b,a')$ is positive, satisfies the same equation with quotient $k$, and has smaller sum. This contradicts minimality. Therefore every possible $k$ is a square.

**Certificate.** The other quadratic root must be integral, nonnegative, and strictly smaller. All three facts are essential; naming “Vieta jumping” does not replace them.

# N16. Arithmetic descent in a nonlinear recurrence

**Source:** IMO 2017, Problem 1. Official paper: [PDF](https://www.imo-official.org/assets/documents/problems/2017/2017_eng.pdf).

**Problem.** Start at an integer $a_0>1$. Replace a square by its positive square root and replace a nonsquare by that number plus three. Determine which initial values cause some integer to occur infinitely often.

**Solution.** Exactly the multiples of three work. A value congruent to two modulo three can never be square, so its subsequent terms increase by three forever.

For a value $a\equiv0\pmod3$, repeated additions reach the next square of a multiple of three. Its square root is at most $\sqrt a+3<a$ for $a\ge6$. Thus, when we observe the process only just after square-root steps, the positive multiples of three decrease until reaching $3$. The cycle is $3,6,9,3$.

For a value $a\equiv1\pmod3$, additions reach the next square whose root is not divisible by three. The least such root is less than $\sqrt a+2<a$ for $a\ge7$. The exceptional square $a=4$ maps to $2$. After each square-root step the residue is either one or two modulo three. The decreasing sequence of observed values cannot stay in residue one forever: it cannot reach $1$ from a value greater than one, because neither legal predecessor of $1$ is greater than one. It therefore reaches residue two, after which the process diverges. This excludes every initial value not divisible by three.

**Certificate.** A recurrence need not decrease at every step. Prove descent between selected events, and separately analyze the finite terminal dynamics.

# Source and verification notes {.unnumbered}

Each record identifier resolves at `https://mathnet.mit.edu/data_v2/full/imo/RECORD.json.gz`; the source ledger retains booklet credits. N08 also matches the official IMO 2019 paper. N10's leading-coefficient convention is made explicit, N11 avoids a reversed ratio and an unnecessary appeal to Dirichlet's theorem in one imported solution, and N09 uses the correct bounds rather than a malformed square-root expression in another source exposition. A 2024 N2 record whose attached solution discusses an unrelated finite set is excluded from the checked core and flagged in the archive. The proofs above are mathematical arguments; the audit's finite checks only test selected computations and edge cases.
