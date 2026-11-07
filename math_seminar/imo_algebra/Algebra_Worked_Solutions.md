---
title: "Olympiad Algebra: Worked Solutions"
author: "Ayden Bi"
date: "Research edition • 6 November 2026"
lang: en-US
---

# Reading this volume {.unnumbered}

These sixteen complete expositions form the checked core of the accompanying research archive. They are a progression through mechanisms, not a numerical ranking of the sixteen hardest problems. Most are IMO shortlist problems; a shortlist label is not an assertion that a problem appeared on the six-problem IMO paper. The original contest and problem number are identified individually. Statements are restated, and proofs are rewritten with intermediate steps, equality cases, and source defects repaired. The source booklets and their contributors retain credit; this volume makes no claim that the underlying problems or classical methods are new.

For each problem, first read the problem and discovery cue. Attempt a proof before reading the solution. Then reconstruct the final argument from the certificate alone. The companion theory book proves the reusable mechanisms. Source-supplied proofs elsewhere in the archive have a different, explicitly unreviewed status.

# A01. Remove the composition

**Source:** IMO 2019, Problem 1; shortlist A1. **Record:** `imo_2019_abb25c`.

**Problem.** Classify the integer-valued functions on the integers for which
$$f(2x)+2f(y)=f(f(x+y))\qquad(x,y\in\mathbb Z).$$

**Discovery cue.** Keep the sum of the two inputs fixed and move one unit from one input to the other.

**Solution.** Put $c=f(0)$. The substitutions $(0,n+1)$ and $(1,n)$ have the same right side. Therefore
$$2(f(n+1)-f(n))=f(2)-c.$$
The first difference is a constant integer $t=f(1)-c$, for every integer $n$, including negative $n$. Telescoping in both directions gives $f(n)=tn+c$. Substitution in the original equation yields
$$t(t-2)(x+y)+(t-2)c=0.$$
Consequently either $t=2$, with any integer $c$, or $t=c=0$. Both possibilities work. The answer is $f\equiv0$ and $f(n)=2n+c$ for arbitrary $c\in\mathbb Z$.

**Certificate.** Equal composite arguments force equal first differences. The passage from constant first difference to affine form uses the integer domain; it is not an unrestricted theorem about functions on the reals.

# A02. The exact cost of monotonicity

**Source:** IMO shortlist 2007, A1. **Record:** `imo_2007_524a29`.

**Problem.** Given real $a_1,\ldots,a_n$, set $M_i=\max_{j\le i}a_j$, $m_i=\min_{j\ge i}a_j$, and $d=\max_i(M_i-m_i)$. Prove that the least possible value of $\max_i|x_i-a_i|$, over nondecreasing real sequences $(x_i)$, is $d/2$.

**Discovery cue.** A downward jump in the data must be paid for at its two endpoints.

**Solution.** Notice that $d=\max_{j\le k}(a_j-a_k)\ge0$. If the error is at most $e$, then, for $j\le k$,
$$a_j-a_k=(a_j-x_j)+(x_j-x_k)+(x_k-a_k)\le2e.$$
Thus $e\ge d/2$. Conversely, take $x_i=(M_i+m_i)/2$. Both $M_i$ and $m_i$ are nondecreasing, so $(x_i)$ is nondecreasing. Since $m_i\le a_i\le M_i$, its error at index $i$ is at most $(M_i-m_i)/2\le d/2$. The lower bound and the construction coincide.

**Certificate.** An obstructing pair gives the lower bound; monotone envelopes give an explicit optimizer. No search over all sequences is needed.

# A03. A floor map eventually repeats

**Source:** IMO shortlist 2006, A1. **Record:** `imo_2006_e3e5ce`.

**Problem.** Starting from an arbitrary real $a_0$, iterate $a_{r+1}=\lfloor a_r\rfloor\{a_r\}$, where $\{x\}=x-\lfloor x\rfloor$. Prove that eventually $a_{r+2}=a_r$.

**Solution.** If a term is nonnegative, all later terms are nonnegative. While its floor is positive, the next term is strictly smaller than that floor. Thus the nonnegative integer floor decreases until the sequence enters $[0,1)$, after which the next term and all later terms are zero.

Suppose instead that every term is negative. Write $c_r=\lfloor a_r\rfloor\le-1$. Since $0\le\{a_r\}<1$, we have $a_{r+1}>c_r$, unless the sequence has reached zero. Hence $c_{r+1}\ge c_r$. This nondecreasing sequence of negative integers stabilizes, say at $c$. Thereafter
$$a_{r+1}=ca_r-c^2.$$
Its fixed point is $L=c^2/(c-1)$, and $a_{r+1}-L=c(a_r-L)$. The terms remain in $[c,c+1)$, so they are bounded. If $c\le-2$, this is possible only when $a_r=L$ for all sufficiently large $r$. If $c=-1$, the map is $a_{r+1}=-a_r-1$, whose square is the identity. In both cases eventual period divides two.

**Audit note.** The recovered source prints $1-a_r$ at one point in the negative two-cycle. The correct partner is $-1-a_r$.

**Certificate.** Stabilize an integer parameter before analyzing the real recurrence.

# A04. Cancel the exceptional coefficient

**Source:** IMO shortlist 2006, A2. **Record:** `imo_2006_e18476`.

**Problem.** Let $a_0=-1$ and, for $n\ge1$, let $\sum_{k=0}^n a_k/(n-k+1)=0$. Show that every $a_n$ with $n\ge1$ is positive.

**Solution.** The equation at $n=1$ gives $a_1=1/2$. Multiply the equations at $n+1$ and $n$ by $n+2$ and $n+1$, respectively, and subtract. The coefficient of $a_0$ cancels exactly, leaving
$$a_{n+1}=\frac1{n+2}\sum_{k=1}^{n}\frac{k\,a_k}{(n-k+1)(n-k+2)}.$$
All displayed weights are positive. Induction beginning at $a_1>0$ now proves the result.

**Certificate.** A subtraction that removes the sole negative initial term turns an opaque convolution into a positive recurrence.

# A05. Translate a quartic into a norm

**Source:** IMO shortlist 2010, A2. **Record:** `imo_2010_66cdab`.

**Problem.** Real $a,b,c,d$ have sum $6$ and sum of squares $12$. Prove
$$36\le4\sum a^3-\sum a^4\le48,$$
where both sums run over the four variables.

**Solution.** Put $x=a-1$, and similarly define $y,z,t$. Then $x^2+y^2+z^2+t^2=4$, $x+y+z+t=2$, and direct expansion gives
$$4\sum a^3-\sum a^4=52-(x^4+y^4+z^4+t^4).$$
For nonnegative $u_i=x_i^2$ with sum $4$, Cauchy's inequality and expansion of a square give
$$4\le\sum u_i^2\le16.$$
This proves the bounds. The lower original bound occurs at a permutation of $(a,b,c,d)=(3,1,1,1)$. The upper bound occurs at a permutation of $(2,2,2,0)$. These satisfy both original constraints, so both constants are sharp.

**Certificate.** A translation kills the cubic term and converts the problem into the elementary range of a squared norm.

# A06. Reverse the coefficients, keep the answer

**Source:** IMO shortlist 2013, A1. **Record:** `imo_2013_d960d1`.

**Problem.** For real $a_1,\ldots,a_{n-1}$, define $u_0=u_1=1$ and $u_{k+1}=u_k+a_ku_{k-1}$. Define $v_0=v_1=1$ by the same recurrence with $a_1,\ldots,a_{n-1}$ reversed. Prove $u_n=v_n$.

**Solution.** Let $\mathcal I_k$ be the subsets of $\{1,\ldots,k-1\}$ containing no two consecutive indices. We claim
$$u_k=\sum_{S\in\mathcal I_k}\prod_{i\in S}a_i,$$
with empty product $1$. For $k=0,1$ this means $u_k=1$. Split the subsets for $u_{k+1}$ according as they omit or contain $k$. The first class contributes $u_k$; the second cannot contain $k-1$ and contributes $a_ku_{k-1}$. Thus the formula follows by induction. Reflection $i\mapsto n-i$ is a bijection on $\mathcal I_n$. It converts the expression for $u_n$ into the expression for $v_n$.

**Certificate.** Expand the recurrence as a weighted family of independent choices. Reversal becomes an actual bijection rather than a mysterious algebraic symmetry.

# A07. A unique crossing

**Source:** IMO shortlist 2014, A1. **Record:** `imo_2014_6534d6`.

**Problem.** For strictly increasing positive integers $z_0,z_1,\ldots$, prove that exactly one $n\ge1$ satisfies
$$z_n<\frac{z_0+\cdots+z_n}{n}\le z_{n+1}.$$

**Solution.** Define $D_n=\sum_{i=0}^n z_i-nz_n$. The requested pair of inequalities is precisely $D_n>0\ge D_{n+1}$. Now $D_1=z_0>0$, while
$$D_{n+1}-D_n=n(z_n-z_{n+1})\le-n.$$
Therefore $D_n\le z_0-n(n-1)/2$, so it eventually becomes nonpositive. Strict decrease proves that there is exactly one last positive term, establishing both existence and uniqueness.

**Certificate.** Encode the two neighboring inequalities as one sign change. Integrality supplies the quantitative decrease; strict increase of a real sequence alone would not give this bound.

# A08. An endpoint certificate for variance

**Source:** IMO shortlist 2019, A2. **Record:** `imo_2019_cd6d5a`.

**Problem.** Real numbers $u_1,\ldots,u_{2019}$ have sum zero and squared sum one. If $a$ and $b$ are their minimum and maximum, prove $ab\le-1/2019$.

**Solution.** Every $u_i$ lies in $[a,b]$, so $(u_i-a)(u_i-b)\le0$. Summing gives
$$1-(a+b)\sum_i u_i+2019ab\le0.$$
The middle term vanishes, giving the claim. Equality holds exactly when each $u_i$ is an endpoint. It is attainable: use $p$ copies of $a=-\sqrt{(2019-p)/(2019p)}$ and $2019-p$ copies of $b=\sqrt{p/(2019(2019-p))}$, for any $1\le p<2019$.

**Certificate.** The polynomial $(x-a)(x-b)$ has a known sign on the entire feasible interval. Summation eliminates the linear coefficient.

# A09. Pair the cyclic ratios

**Source:** IMO shortlist 2020, A3. **Record:** `imo_2020_db020b`.

**Problem.** Positive $a,b,c,d$ satisfy $(a+c)(b+d)=ac+bd$. Determine the minimum of $a/b+b/c+c/d+d/a$.

**Solution.** Apply AM–GM to opposite terms:
$$S\ge2\sqrt{\frac{ac}{bd}}+2\sqrt{\frac{bd}{ac}}
=\frac{2(ac+bd)}{\sqrt{abcd}}
=\frac{2(a+c)(b+d)}{\sqrt{abcd}}\ge8.$$
Equality in the last inequality requires $a=c$ and $b=d$, which also gives equality in the first two AM–GM applications. The constraint then becomes $a^2+b^2=4ab$, or $a/b=2\pm\sqrt3$. Thus the minimum is $8$, attained, for example, at $(a,b,c,d)=(1,2+\sqrt3,1,2+\sqrt3)$.

**Certificate.** Choose pairs whose products are the two monomials in the constraint. Check simultaneous equality, not just equality in each inequality separately.

# A10. Integer averages cannot rise too slowly

**Source:** IMO 2024, Problem 1; shortlist A1. **Record:** `imo_2024_071598`.

**Problem.** Find real $\alpha$ for which $n$ divides $\sum_{k=1}^n\lfloor k\alpha\rfloor$ for every positive integer $n$.

**Solution.** Adding any even integer to $\alpha$ changes this sum by an integer multiple of $n$, namely $q n(n+1)$. Reduce to $0\le\alpha<2$. The value zero works. Suppose $\alpha>0$, and write
$$b_n=\frac1n\sum_{k=1}^n\lfloor k\alpha\rfloor\in\mathbb Z.$$
For all sufficiently large $n$, the new term $\lfloor(n+1)\alpha\rfloor$ is at least every earlier term and is strictly greater than the first. It is therefore strictly greater than their average. Hence $b_{n+1}>b_n$, so the integer sequence eventually increases by at least one at every step. In particular $b_n\ge n+C$ for some constant $C$. But $b_n\le\alpha(n+1)/2$, whose slope is less than one. This contradiction excludes $0<\alpha<2$. Exactly the even integers satisfy the condition.

**Certificate.** The discrete lower speed of an integer sequence conflicts with the analytic upper speed of its average.

# A11. Pay for one unit at a time

**Source:** IMO shortlist 2024, A2. **Record:** `imo_2024_5877d2`.

**Problem.** Minimize $\sum_{i=0}^n2^i x_i^2$ over nonnegative integers with $\sum_{i=0}^n x_i=n$.

**Solution.** The marginal costs for row $i$ are $2^i,3\cdot2^i,5\cdot2^i,\ldots$, since $x^2$ is the sum of the first $x$ odd integers. Each positive integer occurs exactly once among all rows, by its unique power-of-two factorization. Any feasible vector chooses $n$ distinct marginal costs, so its total is at least $1+\cdots+n=n(n+1)/2$.

Conversely choose precisely the costs $1,\ldots,n$. In every row these form an initial segment, so the choice corresponds to a feasible vector. No row beyond $n$ is needed, since $2^{n+1}>n$. Explicitly,
$$x_i=\left\lfloor\frac n{2^i}\right\rfloor-\left\lfloor\frac n{2^{i+1}}\right\rfloor.$$
Thus the minimum is $n(n+1)/2$. The uniqueness of the $n$ smallest costs also proves uniqueness of the minimizing vector.

**Certificate.** Replace a discrete quadratic by its increasing increments. The cost table is exactly the positive integers, not an approximation by a continuous optimization.

# A12. Choose the Jensen weights

**Source:** IMO shortlist 2009, A2. **Record:** `imo_2009_c42bed`.

**Problem.** Positive $a,b,c$ satisfy $1/a+1/b+1/c=a+b+c$. Prove $\sum_{\mathrm{cyc}}(2a+b+c)^{-2}\le3/16$.

**Solution.** Let $s=a+b+c$ and $x=a/s$, $y=b/s$, $z=c/s$. Then $x+y+z=1$ and $H=1/x+1/y+1/z=s^2$. It suffices to prove
$$\sum\frac1{(1+x)^2}\le\frac{3H}{16}.$$
The function $g(t)=t/(1+t)^2$ has $g''(t)=2(t-2)/(1+t)^4\le0$ on $[0,1]$, and $g'(t)=(1-t)/(1+t)^3\ge0$ there. Use Jensen with weights $(1/x)/H,(1/y)/H,(1/z)/H$. Their weighted mean of $x,y,z$ is $3/H\le1/3$, since $H\ge9$. Hence
$$\frac1H\sum\frac1{(1+x)^2}\le g(3/H)\le g(1/3)=\frac3{16}.$$
Equality requires $x=y=z$, and the original constraint then gives $a=b=c=1$.

**Certificate.** Choose weights that cancel the numerator inside the summand. The constraint then determines the total weight exactly.

# A13. A polynomial has a definite sign

**Source:** IMO shortlist 2017, A1. **Record:** `imo_2017_5b8561`.

**Problem.** Positive integers $a_i$ satisfy $\sum 1/a_i=k\in\mathbb Z_{>0}$ and $\prod a_i=M>1$. Show that $M(x+1)^k-\prod(x+a_i)$ has no positive real root.

**Solution.** For $x>0$ and a positive integer $a$, AM–GM on $x+1$ and $a-1$ copies of $1$ gives
$$a(x+1)^{1/a}\le x+a.$$
The inequality is strict when $a>1$. Multiply over $i$. Since $M>1$, at least one $a_i>1$, so
$$M(x+1)^{\sum1/a_i}<\prod(x+a_i).$$
The polynomial is strictly negative for every positive $x$, proving the claim.

**Certificate.** A root-exclusion question can be a product inequality. Integer parameters tell us how many copies to put into AM–GM.

# A14. A sharp quadratic majorant

**Source:** IMO shortlist 2020, A1, Version 1. **Record:** `imo_2020_48d762`.

**Problem.** For $N=2^n$ with $n\ge1$, find the least $c$ such that $((1+x^{2N})/2)^{1/N}\le x+c(x-1)^2$ for every real $x$.

**Solution.** The answer is $c=N/2$. To prove necessity, put $x=1+t$ and raise to the $N$th power for sufficiently small $t$, where the right side is positive. The difference between the right power and $(1+(1+t)^{2N})/2$ has quadratic coefficient $Nc-N^2/2$. A negative coefficient violates the inequality for small nonzero $t$, so $c\ge N/2$.

For sufficiency, induct on powers of two, including $N=1$, where equality is an identity. Suppose the claim holds for $N$ at every real input. Then
$$\begin{aligned}
[x+N(x-1)^2]^2
&=x^2+\frac N2(x^2-1)^2+\left(N^2-\frac N2\right)(x-1)^4\\
&\ge x^2+\frac N2(x^2-1)^2
\ge\left(\frac{1+x^{4N}}2\right)^{1/N}.
\end{aligned}$$
Moreover $x+N(x-1)^2\ge(x^2+1)/2>0$. Taking square roots proves the claim for $2N$.

**Certificate.** The local expansion predicts the optimal coefficient; an exact nonnegative remainder proves the global statement. This proof covers Version 1, not the source's more general Version 2.

# A15. The radical inequality and its sharp parameter

**Source:** IMO 2001, Problem 2. Official paper: [PDF](https://www.imo-official.org/assets/documents/problems/2001/2001_eng.pdf).

**Problem.** For positive $a,b,c$, prove $\sum_{\mathrm{cyc}}a/\sqrt{a^2+8bc}\ge1$.

**Solution.** Put $s=a+b+c$ and $D_a=\sqrt{a^2+8bc}$. Two applications of Cauchy's inequality give
$$\left(\sum\frac a{D_a}\right)\left(\sum aD_a\right)\ge s^2,
\qquad
\left(\sum aD_a\right)^2\le s\sum aD_a^2.$$
But $\sum aD_a^2=\sum a^3+24abc\le s^3$, because
$$s^3-\sum a^3-24abc=3\left(\sum_{\mathrm{sym}}a^2b-6abc\right)\ge0$$
by AM–GM on the six mixed terms. Thus $\sum aD_a\le s^2$, and the desired sum is at least one. Equality holds exactly at $a=b=c$.

**Transfer.** The theory volume proves the full parameter result
$$\inf_{a,b,c>0}\sum\frac a{\sqrt{a^2+\lambda bc}}=
\min\left(1,\frac3{\sqrt{1+\lambda}}\right)\quad(\lambda>0).$$
The threshold $8$ emerges from the cubic certificate rather than from guesswork.

# A16. Measure a union of rational-inequality intervals

**Source:** IMO 1988, Problem 4. Official paper: [PDF](https://www.imo-official.org/assets/documents/problems/1988/1988_eng.pdf).

**Problem.** Show that the real solution set of $\sum_{k=1}^{70} k/(x-k)\ge5/4$ is a disjoint union of intervals whose total length is $1988$; the poles are excluded from the domain.

**Solution.** Let $F(x)=\sum_{k=1}^{70}k/(x-k)$. On each interval without a pole, $F'(x)=-\sum k/(x-k)^2<0$. On $(i,i+1)$ it decreases from $+\infty$ to $-\infty$, so there is a unique root $r_i$ of $F(x)=5/4$. On $(70,\infty)$ it decreases from $+\infty$ to zero, giving one root $r_{70}$. On $(-\infty,1)$ it is negative. Thus the solution intervals are $(i,r_i]$ for $1\le i\le70$.

Let $Q(x)=\prod_{k=1}^{70}(x-k)$. The $r_i$ are the seventy roots of
$$\sum_{k=1}^{70}k\frac{Q(x)}{x-k}-\frac54Q(x)=0.$$
None of the poles is a root of this polynomial. Its leading coefficient is $-5/4$, and its next coefficient is $(1+5/4)\sum k$. Vieta's formula therefore gives $\sum r_i=(9/5)\sum k$. The total interval length is
$$\sum_{i=1}^{70}(r_i-i)=\frac45\frac{70\cdot71}{2}=1988.$$

**Certificate.** Monotonicity locates all roots; Vieta computes their sum without finding any root individually.

# Source and verification notes {.unnumbered}

The MathNet records above are available at `https://mathnet.mit.edu/data_v2/full/imo/RECORD.json.gz`, with RECORD replaced by the printed identifier. The package ledger preserves each record's booklet contributors and source metadata. MathNet is an extraction and retrieval source, so its text is checked rather than treated as infallible. In particular A03 corrects a sign, A06 supplies the omitted $v_1=1$ initialization in one transcription, A11 uses rows $0$ through $n$, and A14 restricts its claim to the version actually proved here. Finite checks in the audit directory support selected identities and extremal examples; they do not replace the proofs.
