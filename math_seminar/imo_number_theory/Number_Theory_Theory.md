---
title: "Olympiad Number Theory: Local Obstructions and Descent"
author: "Ayden Bi"
date: "Research edition • 6 November 2026"
lang: en-US
---

# Preface {.unnumbered}

Number theory rewards a precise choice of scale. A congruence sees a residue; a valuation sees the exact power of a prime; an inequality sees the size of an integer quotient; descent sees a direction in which a solution can be made smaller. Difficult problems often require two of these views to cooperate. Neither a long list of moduli nor an unexplained appeal to a famous theorem is a substitute for identifying the obstruction.

This book builds a proof-oriented toolkit around the sixteen checked cases N01–N16 in the companion volume. It includes elementary tools and proves the more advanced results used in the core, including the lifting lemma, quadratic reciprocity in the form needed for Jacobi symbols, and a classification arising from Vieta jumping. The extensions are presented as proved mathematical consequences, without a claim of research novelty.

The accompanying source archive is broader than the checked core and contains IMO, RMM, national contests and selection material. Coverage remains partial, and imported solutions are labeled as source-supplied rather than independently verified. Neither the corpus size nor a problem's shortlist position establishes an objective ranking of difficulty. The historical sources and their contributors retain credit in the ledger and worked volume.

# Begin with the structure of divisibility

## GCD, cancellation, and invertibility

**Theorem 1.1 (Bézout).** For integers $a,b$, not both zero, there are integers $u,v$ such that $ua+vb=\gcd(a,b)$.

**Proof.** The Euclidean algorithm replaces $(a,b)$ by $(b,a-qb)$ without changing the common divisors. The nonnegative remainders strictly decrease until a final nonzero remainder $g$ is reached. It divides both original numbers and every common divisor divides it, so it is their gcd. Substituting backward expresses $g$ as an integer linear combination of $a,b$.

**Corollary.** If $\gcd(a,m)=1$, multiplication by $a$ is invertible modulo $m$. Conversely, an inverse $ab\equiv1\pmod m$ implies that gcd condition. Thus $ac\equiv ad\pmod m$ permits cancellation of $a$ only when $a$ is a unit modulo $m$, or after the modulus has been adjusted by the gcd.

N11 is designed around this issue. The factorial in a binomial coefficient cannot simply be divided away modulo an arbitrary composite modulus. The solution first proves that all primes in that factorial divide a different number, making the factorial coprime to the modulus. Only then is the cancellation legal.

## Chinese remaindering

**Theorem 1.2.** If $m,n$ are coprime, the two congruences $x\equiv a\pmod m$, $x\equiv b\pmod n$ have exactly one solution modulo $mn$.

**Proof.** Write $x=a+mt$. The second congruence becomes $mt\equiv b-a\pmod n$, which has one solution modulo $n$ because $m$ is invertible. This gives existence and uniqueness modulo $mn$. Iteration proves the corresponding result for pairwise coprime moduli.

A useful habit is to distinguish the two jobs of a modulus. It may **obstruct** a proposed solution, or it may **construct** an input with prescribed behavior. In N11, a prime-power modulus constructs an $n$ for which a numerator has too much divisibility. In N03, one modulus simultaneously records all prime factors of the target.

## Positive multiples are inequalities

**Lemma 1.3.** If positive integers $D,N$ satisfy $D\mid N$ and $N<2D$, then $N=D$.

This elementary observation drives N07. The function's value at two is fixed by a short interval containing only one positive multiple of the divisor. More generally, if a positive integer quotient lies in an interval of length less than one, it is determined or impossible. The word positive matters: from $D\mid0$ no lower bound $D\le0$ follows.

# Valuations record exact information

## The valuation laws

For prime $p$ and nonzero integer $n$, $v_p(n)$ is the unique nonnegative exponent with $p^{v_p(n)}\mid n$ but $p^{v_p(n)+1}\nmid n$. Extend to nonzero rational numbers by $v_p(a/b)=v_p(a)-v_p(b)$.

**Proposition 2.1.** For nonzero $a,b$,
$$v_p(ab)=v_p(a)+v_p(b),\qquad
v_p(a+b)\ge\min(v_p(a),v_p(b)),$$
when the sum is nonzero. If the two valuations are unequal, equality holds in the second formula.

**Proof.** Factor out the powers of $p$. For the sum, suppose $a=p^ru$, $b=p^sv$ with $r\le s$ and $p\nmid uv$. Then $a+b=p^r(u+p^{s-r}v)$. If $r<s$, the bracket is nonzero modulo $p$; if $r=s$, it may have additional powers of $p$. This proves both statements.

**Corollary 2.2 (precision lemma).** If $A\equiv B\pmod {p^k}$ and $v_p(B)<k$, then $v_p(A)=v_p(B)$.

**Proof.** Write $A=B+p^kt$ and apply the unequal-valuation rule. This is the entire local mechanism in N03. Knowing a congruence modulo $p^{v_p(B)}$ would not suffice; one more level of precision is essential.

## A finite modulus certifies a perfect power

**Theorem 2.3.** For integers $b>1,n>1$, if $b$ is an $n$th-power residue modulo $b^2$, then $b$ is an integer $n$th power.

**Proof.** If $a^n\equiv b\pmod {b^2}$ and $p^\alpha\Vert b$, then the precision lemma gives $nv_p(a)=\alpha$. Every prime exponent in $b$ is therefore divisible by $n$, so its prime factorization is an $n$th power.

This is stronger than the statement of N03 because it uses only one of its infinitely many congruences. It is not a general theorem that every polynomial equation solvable modulo all integers is solvable over the integers; such a claim would be false in other settings. Here the target's own factorization supplies the decisive modulus.

# Lifting exponents, proved rather than invoked

## Odd-prime lifting

**Theorem 3.1.** Let $p$ be an odd prime, $p\mid a-b$, and $p\nmid ab$. For positive integer $n$,
$$v_p(a^n-b^n)=v_p(a-b)+v_p(n).$$

**Proof.** First, if $p\nmid u$, factor $a^u-b^u=(a-b)(a^{u-1}+\cdots+b^{u-1})$. The second factor is $ub^{u-1}$ modulo $p$, hence is not divisible by $p$. Thus an exponent coprime to $p$ does not change the valuation.

Next let $x=y+p^tc$ with $t\ge1$ and $p\nmid cy$. The binomial expansion of $x^p-y^p$ has first term $p^{t+1}cy^{p-1}$, of valuation $t+1$. For $2\le j\le p-1$, the $j$th term has valuation at least $1+jt\ge t+2$; the last term has valuation $pt\ge t+2$, since $p\ge3$. Thus no cancellation can remove the unique lowest-valuation term, and $v_p(x^p-y^p)=t+1$.

Write $n=p^ru$ with $p\nmid u$. Apply the first step to exponent $u$, then the second step $r$ times. The valuation increases exactly by $r$, proving the theorem.

**Recognition cue.** Before applying the theorem, check all three hypotheses: odd $p$, divisibility of the difference, and coprimality of the bases. In N08, $p=3$, $a=4$, $b=1$, so the formula becomes $v_3(4^k-1)=1+v_3(k)$.

## The two-adic version

**Proposition 3.2.** For odd integers $a,b$ and even positive $n$,
$$v_2(a^n-b^n)=v_2(a-b)+v_2(a+b)+v_2(n)-1,$$
provided the difference is nonzero. For odd $n$, its valuation is $v_2(a-b)$.

**Proof.** An odd exponent contributes an odd cofactor in the difference-of-powers factorization. For powers of two, factor successively into $a-b$, $a+b$, $a^2+b^2$, and so on. Every factor $a^{2^j}+b^{2^j}$ for $j\ge1$ is two modulo eight, so has valuation one. Counting these factors gives the formula. This explains why blindly applying the odd-prime version at $p=2$ fails.

# Factorials, digit sums, and finite states

## Legendre's formula

**Theorem 4.1.** For prime $p$ and nonnegative integer $n$,
$$v_p(n!)=\sum_{j\ge1}\left\lfloor\frac n{p^j}\right\rfloor
=\frac{n-s_p(n)}{p-1},$$
where $s_p(n)$ is the sum of the base-$p$ digits of $n$.

**Proof.** Each multiple of $p$ contributes one prime factor, each multiple of $p^2$ one additional factor, and so forth. This proves the floor sum. If $n=\sum_i d_ip^i$, summing its truncated base expansions gives $\sum_i d_i(1+p+\cdots+p^{i-1})=(n-\sum_i d_i)/(p-1)$.

Useful consequences are $v_p(n!)<n/(p-1)$ for $n>0$, and strict increases at multiples of $p$. N08 uses both. The equality $v_3(m!)=v_3((3t)!)$ forces $3t\le m\le3t+2$, not merely an approximate relation between $m$ and $t$.

## A block-additivity lemma

**Lemma 4.2.** If $p^g\mid M$ and $0\le r<p^g$, then
$$v_p((M+r)!)=v_p(M!)+v_p(r!).$$

**Proof.** For $1\le j\le r$, the valuation of $j$ is below $g$, so the precision lemma gives $v_p(M+j)=v_p(j)$. Sum over $j$. The strict condition $r<p^g$ matters: crossing the block boundary can introduce a new carry and an extra prime power.

## Finite-image translation

**Theorem 4.3.** Given finitely many primes $p_i$ and a positive integer $d$, there exist integers $P>N\ge0$ such that every interval $[mP,mP+N]$, $m\ge1$, contains an $n$ for which all $v_{p_i}(n!)$ are divisible by $d$.

**Proof.** Let $f(n)$ be the vector of these valuations modulo $d$, and let $S$ be its finite image, including $f(0)=0$. Choose one representative $n_s$ per image state and let $N=\max n_s$. Choose $g$ so all $p_i^g>N$, and put $P=(\prod p_i)^g$. Lemma 4.2 gives $f(mP+n_s)=f(mP)+s$. Translation is injective in the finite group, so these $|S|$ values exhaust $S$; one is zero. Increasing $g$ if necessary ensures $P>N$.

This is the general mechanism behind N05. It gives solutions in infinitely many separated blocks, stronger than a bare infinitude statement. It does not provide a small numerical bound for $P$: the chosen representatives may be large. A proof of existence should not be advertised as an efficient algorithm without analyzing those representatives.

# Orders, periodicity, and sampling

## Fermat and Euler from permutation

**Theorem 5.1.** If $\gcd(a,m)=1$, then $a^{\varphi(m)}\equiv1\pmod m$.

**Proof.** Multiplication by $a$ permutes the invertible residue classes modulo $m$. Multiply all these congruences. The product of the classes is itself invertible, so cancellation leaves $a^{\varphi(m)}\equiv1$. For prime $p$, this is Fermat's theorem $a^{p-1}\equiv1\pmod p$.

The **multiplicative order** of $a$ modulo $m$ is the least positive $r$ with $a^r\equiv1$, when $a$ is invertible. It divides every exponent $s$ with $a^s\equiv1$: divide $s$ by $r$ and use minimality on the remainder. In particular it divides $\varphi(m)$.

If $a$ is not invertible, its powers are still eventually periodic modulo $m$, because multiplication by $a$ is a deterministic map on a finite set. This elementary observation is sufficient for N02; invoking a multiplicative order without checking coprimality would be unnecessary and potentially wrong.

## A general digit-sampling theorem

**Theorem 5.2.** Let $(d_j)$ be an eventually periodic digit sequence. Let positive indices $k_n$ tend to infinity and be eventually periodic modulo every positive integer. Then the sampled sequence $(d_{k_n})$ is eventually periodic.

**Proof.** Let the original sequence have period $t$ after index $J$. For large $n$, $k_n\ge J$. By the hypothesis modulo $t$, there is a positive shift $r$ such that $k_{n+r}\equiv k_n\pmod t$ for all sufficiently large $n$. Both indices are in the periodic tail, so their digits agree.

Taking $k_n=2^n$ proves N02. Taking $k_n=P(n)$ for an integer-coefficient polynomial with positive leading coefficient also works: $P(n+t)\equiv P(n)\pmod t$, and $P(n)\to\infty$. The theorem is about the digits, not the particular base; eventual periodicity is equivalent to rationality in every integer base at least two.

# Quadratic characters as compact obstructions

## Legendre symbols and Euler's criterion

For an odd prime $p$ and $p\nmid a$, the Legendre symbol $(a/p)$ is $1$ if $a$ is a square modulo $p$ and $-1$ otherwise.

**Lemma 6.1 (Euler).** $(a/p)\equiv a^{(p-1)/2}\pmod p$.

**Proof.** Exactly $(p-1)/2$ nonzero residues are squares, since $x^2=y^2$ implies $x=\pm y$ modulo $p$. Every square satisfies $z^{(p-1)/2}=1$ by Fermat. A polynomial of degree $(p-1)/2$ has at most that many roots over the field modulo $p$, so these are all the roots of $z^{(p-1)/2}-1$. Fermat also gives $(a^{(p-1)/2})^2=1$, so a nonsquare has the other value, $-1$. This proves the criterion and immediately proves multiplicativity in the numerator.

## Gauss's lemma and the parity formula

**Lemma 6.2 (Gauss).** Put $h=(p-1)/2$. Reduce $a,2a,\ldots,ha$ to residues in $(-p/2,p/2)$. If $M$ of these residues are negative, then $(a/p)=(-1)^M$.

**Proof.** Their absolute values are exactly $1,\ldots,h$: a repeated absolute value would give $ai\equiv\pm aj$, forcing $i=j$ in the permitted range. Multiplying the residues gives $a^h h!\equiv(-1)^M h!$. Cancel $h!$ and apply Euler's criterion.

**Corollary 6.3.** If $a$ is positive and odd with $p\nmid a$, then
$$\left(\frac ap\right)=(-1)^{\sum_{i=1}^{(p-1)/2}\lfloor ai/p\rfloor}.$$

**Proof.** Write $ai=pq_i+r_i$ with $1\le r_i<p$. Replace each $r_i>p/2$ by $p-r_i$ to obtain the absolute residues of Gauss's lemma. Modulo two, their sum differs from $\sum r_i$ by $M$. Because $a,p$ are odd and the absolute residues permute $1,\ldots,h$, summing $ai=pq_i+r_i$ modulo two gives $M\equiv\sum q_i\pmod2$. Combine with the lemma.

## Quadratic reciprocity by counting a rectangle

**Theorem 6.4.** For distinct odd primes $p,q$,
$$\left(\frac qp\right)\left(\frac pq\right)=(-1)^{(p-1)(q-1)/4}.$$

**Proof.** Consider pairs $(i,j)$ with $1\le i\le(p-1)/2$, $1\le j\le(q-1)/2$. None lies on $qi=pj$. For fixed $i$, the number with $pj<qi$ is $\lfloor qi/p\rfloor$; for fixed $j$, the number with $qi<pj$ is $\lfloor pj/q\rfloor$. These two counts partition the rectangle. Thus the sum of the two floor sums is $(p-1)(q-1)/4$. Corollary 6.3 turns their parities into the two Legendre symbols and proves the result.

This proof is included because N12 gains its shortness from reciprocity. Treating it as unexplained machinery would move, rather than remove, the difficult step.

## Jacobi symbols and composite moduli

For odd positive $m=\prod p_i^{e_i}$ and $\gcd(a,m)=1$, define the Jacobi symbol $(a/m)=\prod(a/p_i)^{e_i}$. It is multiplicative in the numerator, depends only on that numerator modulo $m$, and takes values $\pm1$. A square unit has symbol one. The converse fails: $(2/15)=1$, although two is not a square modulo three and therefore not a square modulo fifteen.

**Corollary 6.5.** For odd $m$ coprime to $15$,
$$\left(\frac5m\right)=\left(\frac m5\right),\qquad
\left(\frac3m\right)=(-1)^{(m-1)/2}\left(\frac m3\right).$$

**Proof.** Apply reciprocity to each prime factor of $m$ and multiply. For five the sign is always positive. For three the accumulated sign is $(-1)^{\sum e_i(p_i-1)/2}=(-1)^{(m-1)/2}$, because the function $u\mapsto(-1)^{(u-1)/2}$ is multiplicative on odd integers.

In N12, the putative modulus has $m\equiv1\pmod {12}$ and is a nonsquare residue modulo five. The two symbols of the supposedly congruent powers are therefore opposite. Notice how little needs to be factored: the Jacobi identities work without a prime factorization of the large number $m$.

# Descent and the geometry of an integer solution

## The well-ordering certificate

**Principle.** If every alleged counterexample produces another counterexample with a strictly smaller positive integer measure, there are no counterexamples.

**Proof.** Choose a counterexample of least measure, whose existence would follow from the well-ordering of the positive integers. Its smaller successor is a contradiction. The measure might be the largest coordinate, the sum of coordinates, or the value observed only at selected events in a recurrence.

Three checks are indispensable: the transformed object is integral, it still satisfies the original hypotheses, and its measure strictly decreases. N15 verifies all three for the other root of a quadratic. N16 uses a different measure: the value just after a square-root step. Intermediate additions increase the sequence, so ordinary term-by-term descent would be false.

## Vieta jumping and a full classification

**Theorem 7.1.** Positive integers satisfying $a^2+b^2=k(ab+1)$ have square $k$. For $k=1$, the only pair is $(1,1)$. For $k=s^2$ with integer $s\ge2$, all positive pairs, up to exchanging coordinates, are
$$ (u_r,u_{r+1})\quad(r\ge1),\qquad
u_0=0,\quad u_1=s,\quad u_{r+1}=s^2u_r-u_{r-1}.$$

**Proof.** Arrange $a\ge b$. The other quadratic root is $a'=kb-a$, with $aa'=b^2-k$. If $a'<0$, then $a\ge kb+1\ge k+1$, while $a(a-kb)=k-b^2$ forces $a<k$, impossible. Thus $a'\ge0$. Moreover
$$a'=kb-a< b^2/a\le b.$$
If $a'=0$, then $k=b^2$. Otherwise $(b,a')$ is another positive solution with smaller coordinates. Repeating reaches a nonnegative solution $(s,0)$ and proves $k=s^2$.

For $k=1$, $(a-b)^2+ab=1$ forces $a=b=1$. For $s\ge2$, reverse the descent from $(0,s)$. The next coordinate is uniquely determined by $u_{r+1}=s^2u_r-u_{r-1}$. These terms strictly increase after $u_0$: if $u_r>u_{r-1}\ge0$, then $u_{r+1}>(s^2-1)u_r\ge3u_r$. Substitution shows that the quadratic equation is preserved by the replacement $(a,b)\mapsto(b,kb-a)$ and its inverse. Every generated pair is therefore a solution, and every solution reaches the same terminal pair under descent, proving completeness.

The classification turns the original perfect-square conclusion into a description of all solutions. It also reveals a limit of brute force: the coordinates grow rapidly, so a modest search sees only the first few members of an infinite orbit.

![For quotient 4 and b = 8, the other root replaces 30 by 2. The solution pair descends from (30,8) to (8,2).](figures/vieta_jump.pdf){width=90%}

## Bounding the smallest variable

N09 uses a different descent-like strategy without an actual transformation. Ordering $a\ge b\ge c$ makes the largest variable control the total sum, while divisibility makes a positive quotient at least one. Their combination bounds $c$ absolutely. Only after that does a finite case analysis become legitimate. A search that begins with a numerical cutoff on all variables has no proof status unless the cutoff has first been justified.

# Closure, digits, and universal conditions

## A root-closure theorem for any base

**Theorem 8.1.** Fix an integer $q\ge2$. Suppose $S\subseteq\mathbb Z$ contains every $q^a-q^b$ for positive $a,b$, and contains every integer root of every nonconstant polynomial with coefficients in $S$. Then $S=\mathbb Z$.

**Proof.** Put $u=q^2-q>0$. Since $0,u,-u\in S$, the polynomials $ux-u$ and $ux+u$ put $1,-1$ in $S$. The polynomial $x+c$ then shows that $S$ is closed under negation.

For any positive $n$, split it as $n=wt$, where every prime dividing $w$ divides $q$ and $\gcd(t,q)=1$. Choose $b>0$ so $w\mid q^b$, and choose $r>0$ so $q^r\equiv1\pmod t$; for $t=1$ any positive $r$ works. Then $N=q^{b+r}-q^b$ is a positive element of $S$ divisible by $n$.

Inductively assume the digits $0,\ldots,n-1$ belong to $S$. The base-$n$ expansion of such an $N$ has zero constant digit and expresses $n$ as a root of a nonconstant polynomial whose other coefficients are these digits and whose constant coefficient is $-N$. Thus $n\in S$. Starting at $n=2$ and using negation gives all integers.

The argument explains N10: the important resource is not a large interval already in $S$, but an available positive multiple of each proposed new base. The polynomial turns the base expansion into a closure operation. If the zero polynomial is included in the closure hypothesis, $0\in S$ already makes the conclusion trivial; the theorem states the substantive convention explicitly.

## Universal quantifiers suggest strategic inputs

In N14 the condition applies to every divisor, so begin with the odd part of $n$, the divisor most strongly constrained by parity. In N11 it applies to every sufficiently large $n$, so prescribe one residue modulo a prime power that breaks the condition. In N07 it applies to every pair $(m,n)$, so choose a diagonal pair and a small anchor. These are different uses of “for all,” and each gives more than random small-value testing.

The reciprocal symmetry of a divisor list is another reusable resource: if $1=d_1<\cdots<d_k=n$, then $d_id_{k+1-i}=n$. N13 uses the hypothesis once at the front of the list and once at the mirrored location. The resulting two relations promote a sum divisibility into individual divisibility.

# Transfer workshop

## Exercises

1. Show that $6x\equiv6y\pmod {15}$ implies $x\equiv y\pmod5$, but need not imply congruence modulo fifteen.
2. If $A\equiv72\pmod {3^5}$, find $v_3(A)$.
3. Determine $v_3(4^{2026}-1)$.
4. Find $v_2(100!)$ using the binary digit sum.
5. Explain why $v_3(m!)=v_3(60!)$ forces $m\in\{60,61,62\}$.
6. Prove that sampling a rational decimal at positions $n^2$ produces a rational decimal.
7. Compute $(5/73)$ and $(3/73)$ and explain how they illustrate N12.
8. Show that a Jacobi symbol of one does not prove that a residue is a square modulo a composite number.
9. List the first three positive unordered solutions of $a^2+b^2=4(ab+1)$.
10. Prove that a positive integer whose divisors form a chain under divisibility is a prime power or one.
11. For fixed $a=6$, list all good indices $b$ in the sense of N11.
12. Replace the number fifty in N06(a) by an arbitrary positive integer $L$ and prove the result.
13. Explain why the argument for root closure works with $3^a-3^b$ instead of $2^a-2^b$.
14. Classify the initial values if the recurrence in N16 is allowed to start at $a_0=1$ as well.
15. Prove that if $p^g\mid M$ then the block-additivity formula can fail at $r=p^g$.
16. Show that if a positive integer $N$ divides a fixed nonzero integer $C$, then $N\le|C|$, and explain how this turns a growing divisibility claim into a contradiction.

## Solutions

1. Divide $15\mid6(x-y)$ by three to get $5\mid2(x-y)$, then cancel the unit two modulo five. Taking $x-y=5$ shows the stronger claim fails.
2. Since $v_3(72)=2<5$, the precision lemma gives $v_3(A)=2$.
3. The lifting lemma gives $1+v_3(2026)=1$.
4. The binary expansion of $100$ is $1100100$, with digit sum three. Thus $v_2(100!)=100-3=97$.
5. The valuation rises at $60$ and again at $63$, with no rise in between. Monotonicity therefore gives exactly that plateau.
6. The index sequence tends to infinity and $(n+d)^2\equiv n^2\pmod d$. Apply Theorem 5.2 to the original period.
7. Reciprocity gives $(5/73)=(73/5)=(3/5)=-1$. Since $73\equiv1\pmod {12}$, $(3/73)=1$. Here $73=2^3+65$, the first nontrivial odd-exponent modulus in N12.
8. Take $m=15,a=2$. Both $(2/3)$ and $(2/5)$ are $-1$, so their product is one. But a square modulo fifteen would be a square modulo three, and two is not.
9. With $s=2$, the recurrence is $u_{r+1}=4u_r-u_{r-1}$ and begins $0,2,8,30,112$. The pairs are $(2,8),(8,30),(30,112)$. Theorem 7.1 proves that these are the first three and describes every later pair.
10. If two distinct primes divided the number, they would be incomparable divisors. Conversely the divisors of $p^r$ are its successive powers, which form a chain; the divisor set of one is trivial.
11. The classification requires even $b$ and all primes $\le b$ to divide six. Thus $b=2,4$ work, while every even $b\ge6$ includes the missing prime five. No odd index works.
12. There are $2^L$ binary prime-factor-parity vectors of length $L$. Two of $2^L+1$ starting points have the same vector, giving the desired distinct shifts.
13. Apply Theorem 8.1 with $q=3$. The essential step is still constructing a positive multiple of every integer using a sufficiently high power of three times $3^r-1$.
14. The value one is a fixed point. Together with the previous classification, the recurrent initial values are one and all positive multiples of three.
15. Take $M=p^g$, $r=p^g$. The product $(M+1)\cdots(M+r)$ has the same valuations as $r!$ except at the last factor when $p=2$: $v_2(2^{g+1})=g+1$ rather than $g$. This supplies a counterexample to an unrestricted extension of the lemma. For odd $p$, choose $M=(p-1)p^g$, so the last factor is $p^{g+1}$ and again has one extra valuation.
16. Write $C=kN$ with nonzero integer $k$, so $|C|=|k|N\ge N$. Therefore a sequence of positive divisors of the same nonzero constant cannot tend to infinity. Always separate the case $C=0$, when every positive integer divides it.

# A seminar plan built around proof decisions

| Week | Decision to practice | Cases | Exit task |
|:--|:--|:--|:--|
| 1 | Which cancellation is legal? | N07, N11 | Prove the exact binomial criterion |
| 2 | Which prime precision matters? | N01, N03 | Explain why one modulus suffices |
| 3 | Which primes constrain a factorial? | N05, N08 | Reconstruct the two-prime contradiction |
| 4 | Which states repeat? | N02, N06 | Separate finite from infinite agreement |
| 5 | Which character distinguishes the sides? | N12 | Prove the Jacobi identities used |
| 6 | Which integer measure decreases? | N15, N16 | Check every descent hypothesis |
| 7 | Which variable or divisor should be chosen first? | N09, N13, N14 | Justify the finite case bound |
| 8 | Which closure operation creates a missing integer? | N10, N04 | Present a mixed problem with a full audit |

After each session, write the shortest valid proof you can, then annotate every place where positivity, integrality, coprimality, or a strict inequality is used. Those annotations reveal which hypotheses are essential and suggest legitimate generalizations. A shorter proof is valuable only when its hidden assumptions have been made visible.

# Attribution and scope {.unnumbered}

Historical problems are identified individually in the companion worked volume. Primary IMO archive: https://www.imo-official.org/problems/ . Retrieval dataset: https://mathnet.mit.edu/ and https://huggingface.co/datasets/ShadenA/MathNet . The source ledger preserves original booklet credits, classification repairs, missing text and rights metadata. Bézout, Euler, Gauss, Legendre, Vieta and the other classical tools retain their established attribution. Consult `Coverage_Report.md` for exact counts and the distinction between checked proofs and imported source solutions.
