---
title: "Olympiad Algebra: Structure Before Calculation"
author: "Ayden Bi"
date: "Research edition • 6 November 2026"
lang: en-US
---

# Preface {.unnumbered}

A hard algebra problem often becomes short only after the right object has been chosen. The object might be a first difference, a quadratic with a known sign, a list of marginal costs, or a polynomial whose roots are the endpoints of intervals. The algebra that follows is usually elementary. The challenge is to recognize what should be preserved and what should be eliminated.

This book develops that recognition through definitions, proved tools, complete examples, and transfer exercises. The companion *Worked Solutions* contains sixteen selected problems, labeled A01–A16. The wider archive includes IMO, RMM, national contests, shortlists and team-selection records, subject to documented coverage gaps. The book synthesizes the checked cases and classical mathematics; it does not assert that every imported proof was read or verified, that the collection covers a century completely, or that these are objectively the hardest problems. The generalizations are proved here without a claim of research novelty.

The intended reader knows elementary algebra, basic inequalities, induction and polynomial division. Derivatives are used in a few explicitly marked tools; their role is to certify monotonicity or convexity, never to conceal a missing equality case. A seminar can follow the eight-week program near the end. A contest reader can begin with the recognition table and return to the proofs as needed.

# Certificates and the anatomy of a short proof

## Definitions

A **certificate** is a finite identity, inequality, or construction from which the requested conclusion follows directly. A sum of squares certifies nonnegativity. An explicit feasible configuration certifies attainability. A strictly decreasing positive integer certifies that a process cannot continue forever. These are descriptions of proof mechanisms, not a new branch of algebra.

A **normalization** uses a symmetry of the problem to fix a parameter. If both sides of an inequality are homogeneous of the same degree, one may often set a positive sum to one. A **translation** such as $x=a-1$ is different: it changes the formulas and must be justified by substitution. A **relaxation** discards a constraint to prove a bound on a larger feasible set. Its equality cases must then be checked against the discarded constraint.

In A05, translating four variables removes the cubic term. The upper and lower bounds use only the sum of their squares. The remaining sum condition is still needed to confirm that the two extremal patterns are actually feasible. This distinction prevents a common error: proving a sharp bound for a relaxed problem and announcing it sharp for the original problem without an example.

## A proof-development routine

1. Write the domain and all sign restrictions. A denominator or square root is a hypothesis, not decoration.
2. List symmetries: scaling, translation, permutation, reversal, and exchanging inputs.
3. Predict equality or the answer from simple configurations. Treat the prediction as a conjecture.
4. Search for one certificate aligned with that prediction.
5. Audit every cancellation, strict inequality, and endpoint; then verify the proposed solutions in the original statement.

For an inequality, the equality pattern is a design constraint. If equality should occur when all variables agree, look for factors $a-b$ or for a convexity statement with equal inputs. If an infimum occurs only at a boundary, do not announce a minimum. If the variables are integers, a continuous optimizer may be a useful lower bound but may fail to be attainable.

## Recognition table

| Visible structure | First object to try | Checked case |
|:--|:--|:--|
| A composite $f(f(x+y))$ | Two inputs with the same sum | A01 |
| Uniform approximation by an ordered sequence | Prefix maximum and suffix minimum | A02 |
| A floor inside an iteration | The integer floor as a separate state | A03 |
| Convolution with one exceptional initial sign | Weighted difference of adjacent recurrences | A04 |
| Cubic and quartic terms under moment constraints | Translate to remove the cubic | A05 |
| Reversal of recurrence coefficients | Weighted subsets or a matrix product | A06 |
| Neighboring average inequalities | One sign-changing defect | A07 |
| Mean and variance with endpoint information | $(x-a)(x-b)\le0$ | A08 |
| Cyclic ratios and a product constraint | Pair terms whose products match it | A09 |
| Integral averages of floors | Compare discrete and analytic growth rates | A10 |
| Integer quadratic minimization | Marginal costs | A11 |
| Reciprocal constraint | Normalize, then choose reciprocal weights | A12 |
| Product polynomial with integer parameters | AM–GM with repeated ones | A13 |
| Best quadratic majorant | Local expansion plus global remainder | A14 |
| Radicals containing $bc,ca,ab$ | Two Cauchy inequalities and a cubic bound | A15 |
| Lengths of rational-inequality intervals | Monotonicity and Vieta | A16 |

# Inequalities as sign certificates

## Cauchy's inequality in the form you need

**Theorem 2.1 (weighted Cauchy).** For real $u_i$ and positive $v_i$,
$$\sum\frac{u_i^2}{v_i}\ge\frac{(\sum u_i)^2}{\sum v_i}.$$
Equality holds exactly when $u_i/v_i$ is constant.

**Proof.** Put $t=(\sum u_i)/(\sum v_i)$ and expand $\sum (u_i-tv_i)^2/v_i\ge0$. The expansion is precisely the claimed difference. Vanishing requires every square to vanish. This proof is also a recipe for discovering the correct weights: identify the linear expression whose square is wanted in the numerator.

The usual form $(\sum x_iy_i)^2\le(\sum x_i^2)(\sum y_i^2)$ follows by applying nonnegativity to $\sum(x_i-ty_i)^2$. Equality means the vectors are proportional, including the zero-vector cases. In a chain of inequalities, every equality condition must hold simultaneously.

## Endpoint polynomials and variance

**Theorem 2.2 (bounded-support variance).** Let positive weights $w_i$ sum to one, let $x_i\in[a,b]$, and let $\mu=\sum w_ix_i$. Then
$$\sum w_i(x_i-\mu)^2\le(b-\mu)(\mu-a).$$
Equality holds exactly when every $x_i$ is an endpoint, apart from the trivial case $a=b$.

**Proof.** Sum $w_i(x_i-a)(x_i-b)\le0$ to obtain $\sum w_ix_i^2\le(a+b)\mu-ab$. Subtract $\mu^2$. Each summand in the original sign certificate is nonpositive, so equality requires each to be zero.

**Corollary.** For $n$ numbers of mean zero and squared sum $Q$, the endpoint product satisfies $ab\le-Q/n$. This makes A08 a one-line application and explains its equality patterns. The general statement is stronger than merely bounding the range $b-a$: since $(b-\mu)(\mu-a)\le(b-a)^2/4$, it also gives the familiar variance bound $(b-a)^2/4$.

## Norm comparison with complete equality information

**Proposition 2.3.** If $u_i\ge0$ and $\sum_{i=1}^n u_i=S$, then
$$S^2/n\le\sum u_i^2\le S^2.$$
The lower equality means all $u_i=S/n$; the upper equality means at most one $u_i$ is nonzero.

**Proof.** The lower bound is Cauchy. The upper bound follows from $S^2-\sum u_i^2=2\sum_{i<j}u_iu_j\ge0$, with the stated equality condition. Applied to $u_i=x_i^2$, this turns a quartic into a norm comparison. It is often more useful to complete a square and translate first than to expand the original quartic in symmetric sums.

# A sharp radical theorem

## The two-stage Cauchy reduction

**Lemma 3.1.** For positive $a_i,D_i$ and $s=\sum a_i$,
$$\sum\frac{a_i}{D_i}\ge\frac{s^{3/2}}{\sqrt{\sum a_iD_i^2}}.$$

**Proof.** Weighted Cauchy gives $(\sum a_i/D_i)(\sum a_iD_i)\ge s^2$. Ordinary Cauchy gives $(\sum a_iD_i)^2\le s\sum a_iD_i^2$. Combine them. Equality in both requires all $D_i$ equal. This is a precise substitute for a vague instruction to “use Cauchy twice.”

![The sharp value changes regime at lambda = 8.](figures/radical_threshold.pdf){width=90%}

## The parameter threshold

**Theorem 3.2.** For $\lambda>0$,
$$\inf_{a,b,c>0}\left(\frac a{\sqrt{a^2+\lambda bc}}+
\frac b{\sqrt{b^2+\lambda ca}}+
\frac c{\sqrt{c^2+\lambda ab}}\right)
=\min\left(1,\frac3{\sqrt{1+\lambda}}\right).$$
For $0<\lambda<8$ the infimum is not attained. For $\lambda\ge8$ it is attained at $a=b=c$, and equality forces that relation.

**Proof.** Set $s=a+b+c$. The lemma bounds the expression below by
$$\frac{s^{3/2}}{\sqrt{a^3+b^3+c^3+3\lambda abc}}.$$
AM–GM on the six terms $a^2b,a^2c,b^2a,b^2c,c^2a,c^2b$ gives
$$a^3+b^3+c^3+24abc\le s^3.$$
At $\lambda=8$, the lower bound is one, with equality only at $a=b=c$. If $0<\lambda<8$, every denominator in the original expression is strictly smaller than its value at $8$, so the sum is strictly greater than one. Taking $(a,b,c)=(1,\varepsilon,\varepsilon)$ and letting $\varepsilon\downarrow0$ makes the first term approach one and the other two approach zero. Thus the infimum is one but is not attained.

If $\lambda\ge8$, use also $abc\le s^3/27$:
$$\sum a^3+3\lambda abc
\le s^3+3(\lambda-8)abc
\le\frac{\lambda+1}{9}s^3.$$
The lemma now gives $3/\sqrt{1+\lambda}$, attained when the three variables are equal. The cubic equality condition proves uniqueness up to scaling.

**How it shortens A15.** The constant eight is the precise value at which the mixed cubic certificate matches the expansion of $(a+b+c)^3$. The theorem also tells us why boundary testing matters: the optimizing pattern changes at that threshold.

# Functional equations: erase before solving

## Equal-argument subtraction

**Proposition 4.1.** If $f:\mathbb Z\to\mathbb R$ has $f(n+1)-f(n)=t$ for every integer $n$, then $f(n)=tn+f(0)$ for every integer $n$.

**Proof.** Telescope from zero for positive $n$ and from $n$ to zero for negative $n$. Neither continuity nor boundedness is needed. The domain is essential: an additive function on $\mathbb R$ need not be linear without an additional regularity assumption.

**Theorem 4.2.** Fix an integer $k\ge2$. The functions $f:\mathbb Z\to\mathbb Z$ satisfying
$$f(kx)+kf(y)=f(f(x+y))$$
for all integers $x,y$ are exactly $f\equiv0$ and $f(x)=kx+c$ for arbitrary integer $c$.

**Proof.** Let $c=f(0)$. The pairs $(0,x)$ and $(x,0)$ give $f(kx)=kf(x)-(k-1)c$. Comparing the original equation with the case $(0,x+y)$ then yields
$$f(x+y)=f(x)+f(y)-c.$$
Thus $g(x)=f(x)-c$ is additive on $\mathbb Z$, so $g(x)=tx$ for the integer $t=g(1)$. Substitute $f(x)=tx+c$ into the original relation. The coefficients give $t(t-k)=0$ and $(t-k)c=0$, leaving precisely the stated functions. Direct substitution proves sufficiency.

The transferable step is the cancellation of the nested expression by preserving its argument. Solving for $f(f(x))$ in isolation would retain unnecessary complexity. More generally, when $P(x,y)$ contains a complicated term depending only on $x+y$, compare $P(x,y)$ and $P(x+h,y-h)$ before making any injectivity assumption.

## A disciplined substitution ledger

Write down what each substitution accomplishes: an anchor value, a symmetry, a range statement, or a finite difference. Do not list substitutions merely because they are easy. A claim that $f$ is injective must be proved before cancellation of $f(u)=f(v)$. A claim that $f$ is surjective must be proved before choosing an input with a prescribed output. The proof of A01 needs neither property.

# Discrete convexity and optimal allocation

## Marginal costs

**Definition.** For a function $C_i:\mathbb Z_{\ge0}\to\mathbb R$ with $C_i(0)=0$, define its marginal costs $\Delta_i(j)=C_i(j+1)-C_i(j)$. It is discretely convex when these costs are nondecreasing in $j$.

**Theorem 5.1 (allocation by increments).** Given finitely many discretely convex costs, the minimum of $\sum_i C_i(x_i)$ subject to nonnegative integers $x_i$ and $\sum_i x_i=N$ is obtained by taking $N$ smallest available marginal costs, resolving equal-cost ties so that each row is an initial segment.

**Proof.** A feasible vector selects the first $x_i$ increments in row $i$ and therefore exactly $N$ increments in total. Its cost is their sum, at least the sum of the $N$ smallest increments of the entire table. Since each row is nondecreasing, that smallest collection can be chosen prefix-closed in each row; with ties, replace a chosen later equal entry by an earlier one. The collection therefore comes from a feasible vector and attains the bound.

Only the first $N$ entries of each row need to be considered. This avoids an irrelevant question about whether an infinite table has a smallest entry. An equivalent exchange condition is
$$\Delta_i(x_i-1)\le\Delta_j(x_j)$$
for every occupied row $i$ and every row $j$. If it fails, moving one unit from $i$ to $j$ lowers the cost. If it holds, every chosen cost is no greater than every unchosen cost, so the vector is optimal.

For $C_i(x)=2^ix^2$, the increments are $2^i(2j+1)$. Unique factorization says their union is exactly the positive integers. A11 follows immediately, including the optimizer and its uniqueness. The theorem is broader: any separable discrete convex objective has the same sorting certificate, even when the resulting sorted list has no closed formula.

![For twelve units, the optimal prefixes select precisely the costs 1 through 12.](figures/marginal_costs.pdf){width=95%}

## Uniform monotone approximation

**Theorem 5.2.** The exact distance in maximum norm from a real sequence $a_1,\ldots,a_n$ to the nondecreasing sequences is
$$\frac12\max_{j\le k}(a_j-a_k).$$
One optimizer is $x_i=(\max_{j\le i}a_j+\min_{j\ge i}a_j)/2$.

The proof in A02 consists of two independent certificates: every inverted pair requires that much error, and the envelope midpoint attains it. A useful weighted version is the feasibility test for prescribed error radii $r_i\ge0$: a nondecreasing sequence with $|x_i-a_i|\le r_i$ exists exactly when
$$a_j-r_j\le a_k+r_k\quad\text{for all }j\le k.$$
Necessity is immediate. For sufficiency, set $x_i=\max_{j\le i}(a_j-r_j)$. This is nondecreasing, is at least $a_i-r_i$, and the displayed inequalities put it below $a_i+r_i$. Thus a global ordered approximation problem reduces to pairwise inequalities.

# Recurrences: state, weights, and symmetry

## A bounded affine tail

**Proposition 6.1.** Suppose a bounded real sequence eventually satisfies $x_{n+1}=cx_n+d$. If $|c|>1$, the tail is the fixed point $d/(1-c)$. If $c=-1$, the tail has period dividing two. If $c=1$, boundedness forces $d=0$.

**Proof.** For $c\ne1$, subtract the fixed point to get $x_n-L=c^{n-n_0}(x_{n_0}-L)$. Boundedness proves the first assertion, and $c=-1$ proves the second. For $c=1$, $x_n=x_{n_0}+(n-n_0)d$, giving the third. A03 first stabilizes the integer floor; only then does this proposition apply.

## Positive recurrence by cancellation

The calculation in A04 suggests a general rule. Suppose two consecutive identities involve one coefficient of the wrong sign. Multiply them so that this exceptional coefficient cancels; inspect the signs of the remaining coefficient differences. This is a method, not a universal positivity theorem: the signs have to be checked for the actual kernel. In A04 the kernel $1/(n-k+1)$ yields the positive difference
$$\frac{n+1}{n-k+1}-\frac{n+2}{n-k+2}
=\frac{k}{(n-k+1)(n-k+2)}.$$
That explicit expression is the entire induction engine.

## Independent-set polynomials

**Definition.** For weights $a_1,\ldots,a_m$ on a path, define
$$I(a_1,\ldots,a_m)=\sum_{S}\prod_{i\in S}a_i,$$
where $S\subseteq\{1,\ldots,m\}$ contains no adjacent indices and the empty product is one.

Partitioning by whether $m$ is selected gives $I_m=I_{m-1}+a_mI_{m-2}$. Reflection of the path gives $I(a_1,\ldots,a_m)=I(a_m,\ldots,a_1)$. These statements hold for arbitrary real weights, even negative ones, because they are polynomial identities; no counting interpretation with positive probabilities is required. This is the clean explanation of A06.

The same technique handles other recurrences: specify the weighted objects, partition them by the final choice, and identify a symmetry of the objects. Guessing a closed form is often unnecessary.

# Polynomials, roots, and interval length

## The root-count principle

**Theorem 7.1.** A nonzero polynomial over a field of degree at most $d$ has at most $d$ distinct roots.

**Proof.** If $r$ is a root, polynomial division gives $P(x)=(x-r)Q(x)$ with $\deg Q=\deg P-1$. Induct on degree. Therefore two degree-at-most-$d$ polynomials agreeing at $d+1$ distinct points are identical. This justifies interpolation arguments and exact symbolic checks; agreement at many random numerical points does not provide the same theorem unless a degree bound and exact arithmetic are supplied.

**Corollary (Lagrange interpolation).** For distinct $t_0,\ldots,t_d$ and $\deg P\le d$,
$$P(x)=\sum_{i=0}^d P(t_i)\prod_{j\ne i}\frac{x-t_j}{t_i-t_j}.$$
The right side has degree at most $d$ and agrees at each $t_i$, so the root-count theorem proves the formula. Comparing leading coefficients often extracts a sum identity without expanding the entire polynomial.

## A general rational-interval theorem

**Theorem 7.2.** Let $t_1<\cdots<t_n$, positive residues $r_i>0$, and $c>0$. The set
$$\left\{x\notin\{t_i\}:\sum_{i=1}^n\frac{r_i}{x-t_i}\ge c\right\}$$
is a union of $n$ disjoint intervals $(t_i,s_i]$, with $s_i\in(t_i,t_{i+1})$ for $i<n$ and $s_n>t_n$. Their total length is $\sum r_i/c$.

**Proof.** The rational function is strictly decreasing between consecutive poles, with limits $+\infty,-\infty$ on each bounded gap; on the last gap it decreases from $+\infty$ to zero. It is negative before the first pole. This gives precisely the stated roots and intervals. Multiply the equation at height $c$ by $Q(x)=\prod(x-t_i)$. The resulting polynomial has leading coefficient $-c$ and next coefficient $c\sum t_i+\sum r_i$. Its $n$ roots are exactly the $s_i$, so Vieta gives $\sum s_i=\sum t_i+\sum r_i/c$. Subtract the left endpoints.

This theorem turns A16 into a substitution. Its positivity assumptions are structural: negative residues can destroy monotonicity and interlacing, while $c=0$ changes the unbounded tail. Do not extrapolate the interval formula beyond its hypotheses.

# Convexity and sharp local information

## Jensen with a proof

**Theorem 8.1.** If $g$ is differentiable and concave on an interval, then for positive weights $w_i$ summing to one,
$$\sum w_ig(x_i)\le g\left(\sum w_ix_i\right).$$

**Proof.** Let $\mu=\sum w_ix_i$. Concavity gives the tangent-line inequality $g(x)\le g(\mu)+g'(\mu)(x-\mu)$; for twice differentiable $g$, it follows by integrating the nonincreasing derivative on either side of $\mu$. Multiply by $w_i$ and sum. The linear terms cancel. Strict concavity forces equality only when all $x_i$ coincide.

The function in A12 is $g(t)=t/(1+t)^2$, which is concave on $[0,1]$. The remarkable choice is the weights, proportional to $1/x_i$: they turn $w_ig(x_i)$ into the target reciprocal squares. Always specify the interval on which the second derivative has the required sign.

## Local necessity is not global sufficiency

If $F(1)=1$, $F'(1)=1$, and $F(x)\le x+c(x-1)^2$ near one, then Taylor expansion forces $c\ge F''(1)/2$. This is a necessary condition. It is sufficient only after a separate global argument. A14 provides exactly that argument: an induction and an explicit nonnegative fourth-power remainder. A local computation alone would not solve the problem for all real $x$.

When squaring an inequality, record the signs first. A14 checks that its proposed majorant is at least $(x^2+1)/2>0$ even for negative $x$. This small line prevents an otherwise plausible induction from proving only an inequality between squares.

# Transfer workshop

Attempt each exercise before reading the solutions. They are original practice formulations around classical tools and the checked cases, not additional historical contest claims.

## Exercises

1. For $x_i\in[2,7]$ with average $4$, prove that their average squared deviation from $4$ is at most $6$. Describe equality.
2. Find the infimum of $\sum a/\sqrt{a^2+3bc}$ over positive $a,b,c$, and decide whether it is attained.
3. Classify integer-valued $f$ on $\mathbb Z$ satisfying $f(3x)+3f(y)=f(f(x+y))$.
4. Find a closest nondecreasing sequence in maximum norm to $(4,1,3,2)$, and give the exact error.
5. Minimize $x^2+3y^2$ over nonnegative integers with $x+y=10$.
6. Prove $I(a,b,c)=1+a+b+c+ac$ and explain its reversal symmetry without algebraic expansion.
7. If $z_0=5$ and $z_n=5+2n$, determine the crossing index in A07.
8. Find the total length of the set where $2/(x+1)+5/(x-2)\ge7$.
9. For distinct $t_0,\ldots,t_d$, show $\sum_i t_i^d/\prod_{j\ne i}(t_i-t_j)=1$.
10. Suppose a bounded tail satisfies $x_{n+1}=-3x_n+2$. Determine the tail.
11. For real $x_1,\ldots,x_5$ with squared sum $10$, find the full range of their fourth-power sum.
12. Prove that prescribed intervals $[\ell_i,u_i]$ admit a nondecreasing selection exactly when $\ell_j\le u_k$ for all $j\le k$.
13. Let $x_i>0$ sum to one and put $H=\sum 1/x_i$ for three indices. Prove $\sum(1+x_i)^{-2}\le3H/16$ without changing the Jensen weights midway.
14. Show that $\sum_{i=0}^{n}2^ix_i^2=n(n+1)/2$ with $\sum x_i=n$ forces the unique vector in A11.
15. Give a counterexample to the assertion that every strictly increasing real sequence of positive terms has the crossing in A07.
16. Explain why two polynomials of degree at most four agreeing at five distinct real points are equal, while two arbitrary functions need not be equal.

## Solutions

1. Theorem 2.2 gives $(7-4)(4-2)=6$. Equality uses only the endpoints; the proportion at $7$ is $2/5$. For a finite unweighted list this requires its length to be divisible by five.
2. Theorem 3.2 gives infimum one, not attained. The family $(1,\varepsilon,\varepsilon)$ supplies the limiting values.
3. Theorem 4.2 gives $f\equiv0$ or $f(n)=3n+c$ with $c\in\mathbb Z$.
4. The largest downward pair difference is three. Prefix maxima are $(4,4,4,4)$ and suffix minima are $(1,1,2,2)$, so $(5/2,5/2,3,3)$ is an optimizer with error $3/2$.
5. Substituting $x=10-y$ gives $4(y-5/2)^2+75$. The nearest integers are $y=2,3$, giving minimum $76$ at $(8,2)$ and $(7,3)$.
6. The allowed subsets of a three-vertex path are the empty set, the three singletons and $\{1,3\}$. Reflection exchanges the endpoints and preserves this family.
7. Here $D_n=5-n(n-1)$. The last positive term is $D_2=3$, followed by $D_3=-1$, so $n=2$.
8. Theorem 7.2 gives $(2+5)/7=1$. No individual endpoint needs to be found.
9. Apply Lagrange interpolation to $P(x)=x^d$ and compare the coefficient of $x^d$.
10. Proposition 6.1 gives the fixed tail $x_n=1/2$.
11. Set $u_i=x_i^2$. The range is $[20,100]$. Both endpoints are attained; all intermediate values occur continuously along a path on the sphere between an equal-magnitude vector and a one-coordinate vector.
12. Necessity follows from $\ell_j\le x_j\le x_k\le u_k$. For sufficiency set $x_i=\max_{j\le i}\ell_j$.
13. Use weights $1/(Hx_i)$, weighted mean $3/H\le1/3$, concavity and monotonicity of $t/(1+t)^2$ on $[0,1]$, exactly as in A12.
14. All marginal costs are distinct positive integers. A selection of $n$ costs has the minimum possible sum only if it is precisely $\{1,\ldots,n\}$. Count the integers of each exact power-of-two valuation to obtain the formula.
15. Take $z_n=2-2^{-n}$, so $z_0=1$. Its defect satisfies $D_n=\sum_{i=0}^nz_i-nz_n=(n+1)2^{-n}>0$ for every $n\ge1$. Thus it never crosses. This demonstrates why a discrete gap hypothesis matters.
16. The polynomial difference has five roots and degree at most four, hence is zero. For arbitrary functions, one may change a value at any sixth point while preserving the five specified values.

# Seminar program and final proof checklist

| Week | Core tools | Worked cases | Deliverable |
|:--|:--|:--|:--|
| 1 | Domain, equality, sign polynomials | A05, A08 | Two exact certificates |
| 2 | Weighted Cauchy and the radical threshold | A09, A15 | Prove Theorem 3.2 from memory |
| 3 | Equal-argument subtraction | A01, A10 | Explain the role of the integer domain |
| 4 | Ordered envelopes and marginal costs | A02, A11 | Construct both optimizers |
| 5 | Stabilized states and positive recurrences | A03, A04 | Repair the sign error independently |
| 6 | Weighted objects and sign changes | A06, A07 | Give a bijection and a descent bound |
| 7 | Polynomial signs and root sums | A13, A16 | Generalize the interval-length result |
| 8 | Jensen weights and sharp majorants | A12, A14 | A timed mixed proof followed by an audit |

Before submitting a proof, check: are all denominators nonzero; are squared expressions known to have the needed sign; is an integer quotient positive before it is bounded below by one; are all proposed functions checked in the original equation; are all equality conditions compatible; and is a limiting construction being called an infimum rather than a minimum? These are mathematical checks, not stylistic polish. A short proof earns its brevity by making its decisive certificate exact.

# Sources and scope {.unnumbered}

Historical problem attribution and source URLs appear in the companion worked volume and in `audit/source_ledger.jsonl`. Primary contest archive: https://www.imo-official.org/problems/ . Retrieval corpus: https://mathnet.mit.edu/ and https://huggingface.co/datasets/ShadenA/MathNet . The ledger retains source-booklet contributors and rights fields. Classical names such as Cauchy, Jensen, Vieta and Lagrange are retained; the organizing terminology and proved extensions here make no novelty claim. Consult `Coverage_Report.md` for precise recovered counts, missing records, scope distinctions and the limits of independent verification.
