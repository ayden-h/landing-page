# AIME Algebra Worked Solutions

New exposition after source consultation. Each entry records its source review and verification; see the coverage and provenance reports for their precise scope.

## 1983 AIME Problem 1: Reciprocal logarithms

For x,y,z>1 and w>0, suppose log_x(w)=24, log_y(w)=40, and log_(xyz)(w)=12. Find log_z(w).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1983_AIME_Problems/Problem_1) · MAA AMC.

### Solution

Since w=x^{24}>1, logarithms to base w are defined. The product rule gives log_w z=log_w(xyz)-log_w x-log_w y=1/12-1/24-1/40=1/60. Taking the reciprocal yields log_z w=60.

**Answer:** 060.

**Methods:** logarithms, change of base.

**Verification:** Exact rational subtraction gives 1/60; substituting x=w^(1/24), y=w^(1/40), z=w^(1/60) verifies the product-base condition.

**Source comparison:** All six alternatives use change of base or exponent elimination and give 60. The reciprocal-logarithm method is shortest; w>1 follows from the hypotheses.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Taking reciprocal logarithms converts the three bases into an additive relation.

## 1983 AIME Problem 2: Absolute values on a fixed interval

Let 0<p<15 and f(x)=|x-p|+|x-15|+|x-p-15|. Find the minimum of f on p≤x≤15.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1983_AIME_Problems/Problem_2) · MAA AMC.

### Solution

On this interval the three terms are x-p, 15-x, and p+15-x. Thus f(x)=30-x, a decreasing function. Its minimum is f(15)=15.

**Answer:** 015.

**Methods:** absolute values, piecewise linear functions.

**Verification:** The sign conditions hold throughout the closed interval, and x=15 attains the lower bound.

**Source comparison:** Index 0 correctly resolves the signs. Index 1 chooses p near 15 and treats the interval as a point; this does not prove the claim for arbitrary p.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The prescribed interval fixes the signs of all three absolute values.

## 1983 AIME Problem 3: A radical equation with a repeated quadratic

Find the product of all real roots of x²+18x+30=2√(x²+18x+45).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1983_AIME_Problems/Problem_3) · MAA AMC.

### Solution

Put t=√(x²+18x+45)≥0. Then t²-15=2t, so (t-5)(t+3)=0 and t=5. Hence x²+18x+20=0. Its discriminant is 244>0, and each root gives t=5 in the original equation. Vieta therefore gives product 20.

**Answer:** 020.

**Methods:** substitution, radicals, Vieta.

**Verification:** The reduced discriminant is positive and both roots satisfy the unsquared equation.

**Source comparison:** All four alternatives reduce to the same quadratic after excluding the extraneous radical branch. Index 3 has a sign typo saying the right side is negative when it is nonnegative.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A repeated quadratic expression reduces the radical equation to a quadratic, followed by Vieta.

## 1983 AIME Problem 5: Recovering a sum from power sums

Complex numbers x,y satisfy x²+y²=7 and x³+y³=10. Find the largest real value of x+y.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1983_AIME_Problems/Problem_5) · MAA AMC.

### Solution

Set s=x+y and p=xy. Then s²-2p=7 and s³-3 ps=10. Eliminating p gives s³-21s+20=(s-4)(s-1)(s+5)=0. The largest real candidate is 4. It is attainable: the roots of t²-4t+9/2=0 are complex numbers with sum 4 and product 9/2, so their second and third power sums are 7 and 10. Thus the answer is 4.

**Answer:** 004.

**Methods:** symmetric polynomials, power sums, complex roots.

**Verification:** For s=4,p=9/2 the power sums are 16-9=7 and 64-54=10; all three possible sums are listed.

**Source comparison:** Indices 0,2,3 correctly use the sum/product cubic. Index 1 wrongly infers conjugacy without considering zero imaginary parts and assumes an integer requested sum; the cubic proof avoids both assumptions.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The power sums determine a cubic for the sum of the two complex numbers.

## 1983 AIME Problem 9: An attainable inequality bound

Find the minimum of (9x²sin²x+4)/(x sin x) for 0<x<π.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1983_AIME_Problems/Problem_9) · MAA AMC.

### Solution

Let t=x sin x>0. The expression is 12+(3t-2)²/t, hence at least 12. The continuous function x sin x takes values 0 and π/2 at 0 and π/2, so it equals 2/3 at some interior point. The square then vanishes, proving that the minimum 12 is attained.

**Answer:** 012.

**Methods:** inequalities, equality cases, continuity.

**Verification:** The squared-error representation gives a global bound, and the intermediate value theorem supplies an allowed equality case.

**Source comparison:** All five alternatives were read. The AM-GM and completed-square methods correctly require attainability. Index 2 mistakenly calls the negative critical point a minimum; index 3 differentiates with respect to y while labeling the derivative by x; index 4 unjustifiably assumes the value is an integer.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A positive substitution reduces the trigonometric expression to an equality-case inequality.

## 1983 AIME Problem 13: Sum of alternating subset sums

For every nonempty subset of 1 through 7, list its elements decreasingly and alternately add and subtract them, starting with plus. Sum these values over all subsets.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1983_AIME_Problems/Problem_13) · MAA AMC.

### Solution

Give the empty set value 0. Pair each subset $U\subseteq\{1,\ldots,6\}$ with $U\cup\{7\}$. Adding 7 at the front reverses every old sign, so the two values sum to 7. There are $2^6$ pairs, hence the required total is $7\cdot2^6=448$. Removing the empty set changes nothing.

**Answer:** 448.

**Methods:** involution, weighted subsets.

**Verification:** Independent exact check passed: Directly summed the 127 nonempty subset values. Result 448. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 5 archived solution entries. Alternatives use maximum-element pairing, a recurrence and cancellation of individual coefficients.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. A sum over all subsets is simplified by cancellation of signed element contributions.

## 1984 AIME Problem 1: The even-indexed half of a progression

An arithmetic progression has common difference 1 and a₁+⋯+a₉₈=137. Find a₂+a₄+⋯+a₉₈.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1984_AIME_Problems/Problem_1) · MAA AMC.

### Solution

Let E and O be the sums of the 49 even-indexed and 49 odd-indexed terms. Pairing consecutive terms gives E-O=49, while E+O=137. Thus E=(137+49)/2=93.

**Answer:** 093.

**Methods:** arithmetic progressions, pairing.

**Verification:** The resulting odd-indexed sum 44 differs from 93 by 49 and their total is 137.

**Source comparison:** All five alternatives correctly obtain 93. Pairing adjacent terms extracts the requested sum directly, while solving for the first term adds unnecessary arithmetic.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Adjacent terms of an arithmetic progression determine the difference between its even and odd partial sums.

## 1984 AIME Problem 4: Recovering a list from two means

A list of positive integers contains 68 and has mean 56. Removing one occurrence of 68 leaves mean 55. Find the largest possible entry in the original list.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1984_AIME_Problems/Problem_4) · MAA AMC.

### Solution

If N entries remain, then 55N+68=56(N+1), so N=12 and their sum is 660. Every one of those entries is at most 660-11=649 because the other eleven are positive integers. The list consisting of 68,649,and eleven 1s attains both means, so 649 is the required maximum.

**Answer:** 649.

**Methods:** averages, integer optimization, attainment.

**Verification:** The original total is 728 across 13 entries, giving 56; removing 68 leaves 660/12=55.

**Source comparison:** Both alternatives correctly determine twelve remaining entries and use eleven 1s to attain the bound; repeated values are allowed.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Removing one value determines the list length, after which positivity bounds its maximum.

## 1984 AIME Problem 5: A product from symmetric logarithms

Positive a,b satisfy log₈a+log₄(b²)=5 and log₈b+log₄(a²)=7. Find ab.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1984_AIME_Problems/Problem_5) · MAA AMC.

### Solution

Write u=log₂a and v=log₂b. The equations become u/3+v=5 and v/3+u=7. Adding gives 4(u+v)/3=12, so log₂(ab)=u+v=9 and ab=512.

**Answer:** 512.

**Methods:** logarithms, symmetric elimination.

**Verification:** Solving also givesu=6,v=3, so a=64,b=8 satisfy both equations.

**Source comparison:** All nine alternatives reviewed; they agree on 512. Index 4 has missing logarithm bases and an erroneous intermediate exponent display, although its intended sum-and-change-of-base method is valid.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A symmetric pair of logarithm equations determines the logarithm of the product directly.

## 1984 AIME Problem 7: A nested recurrence determined by parity

For every integer n, let f(n)=n-3 when n≥1000 and f(n)=f(f(n+5)) when n<1000. Find f(84).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1984_AIME_Problems/Problem_7) · MAA AMC.

### Solution

Directly descending from 999 gives f(999)=998, f(998)=997, f(997)=998, f(996)=997, and f(995)=998. We claim for all n<1000 that f(n)=997 when n is even and 998 when n is odd. The five values establish the initial block. For n≤994, descending induction already knows f(n+5), which equals 998 if n is even and 997 if n is odd. Applying the known values f(998)=997 and f(997)=998 proves the claim at n. Since 84 is even, f(84)=997.

**Answer:** 997.

**Methods:** functional recurrence, descending induction, parity.

**Verification:** The displayed parity formula satisfies both branches for every integer, and descending induction makes the values uniquely determined. Independent exact check passed: Evaluate the nested definition directly with memoization.

**Source comparison:** All four entries read. Index 1 states the correct parity pattern but leaves induction implicit. Index 0 uses iterates with a valid repeated reduction. Index 2 manipulates iteration counts without a rigorous justification; index 3 is a computational recursion rather than a general proof.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A nested functional recurrence is solved by a descending parity induction.

## 1984 AIME Problem 8: A restricted ninth root of unity

A root z of z⁶+z³+1=0 has argument θ strictly between 90° and 180°. Find θ in degrees.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1984_AIME_Problems/Problem_8) · MAA AMC.

### Solution

Multiplication by z³-1 gives z⁹=1. The roots of the original polynomial are exactly the ninth roots of unity that are not cube roots of unity, since a cube root gives value 3. Their arguments are 40°,80°,160°,200°,280°,320°. Only 160° is in the required interval.

**Answer:** 160.

**Methods:** roots of unity, polynomial factorization.

**Verification:** Forθ=160°,9θ is a multiple of 360° but 3θ is not, so the original polynomial vanishes.

**Source comparison:** Both alternatives correctly use ninth roots with cube roots excluded, or solve first forz³ and take all three cube roots.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The polynomial factors a roots-of-unity equation and excludes cube roots of1.

## 1984 AIME Problem 10: A score that determines the number correct

A 30-question test scores 30+4c−w, with c correct, w wrong and the rest blank. Find the smallest score above 80 that uniquely determines c.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1984_AIME_Problems/Problem_10) · MAA AMC.

### Solution

If $w\ge4$, replacing $(c,w)$ by $(c-1,w-4)$ preserves the score and is feasible (a score above 80 ensures $c>0$). If at least five questions are blank, $(c+1,w+4)$ is another feasible pair. Uniqueness therefore requires $w\le3$ and $c+w\ge26$. Hence $c\ge23$ and $s\ge30+4(23)-3=119$. For $s=119$, $w=4c-89$ and $0\le w\le30-c$ force $23\le c\le23$, so 119 is achievable and uniquely identifies $c=23$.

**Answer:** 119.

**Methods:** integer feasibility, extremal.

**Verification:** Independent exact check passed: Enumerated all feasible correct/wrong counts. Result 119. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 4 archived solution entries. Alternatives use score intervals and equivalent feasible-answer transformations.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Feasible correct/wrong/blank score configurations determine the first uniquely informative score.

## 1984 AIME Problem 12: Root orbits under two reflections

A real function is unchanged by reflection about 2 and about 7, and vanishes at 0. Find the fewest roots it can have in [−1000,1000].

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1984_AIME_Problems/Problem_12) · MAA AMC.

### Solution

The symmetries are $x\mapsto4-x$ and $x\mapsto14-x$; their compositions translate by 10. Thus every $10k$ and $4+10k$ is forced to be a root. There are respectively 201 and 200 such points in the interval. This lower bound is attained: define $f(x)=0$ on those two residue classes and $f(x)=1$ elsewhere. Both reflections preserve their union and its complement. Hence exactly $401$ roots are possible.

**Answer:** 401.

**Methods:** group orbit, hybrid algebra.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 4 archived solution entries. Valid approaches use the orbit generated by two reflections; attaining the lower bound must also be justified.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Two reflection identities generate a periodic orbit of forced roots, which must be counted and realized.

## 1984 AIME Problem 13: A telescoping inverse-trigonometric sum

Evaluate 10 cot(arccot 3+arccot 7+arccot 13+arccot 21), taking each inverse cotangent in(0,π/2).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1984_AIME_Problems/Problem_13) · MAA AMC.

### Solution

For k=1,2,3,4, the tangent subtraction formula gives tan(arctan(k+1)-arctan k)=1/(k²+k+1). Both angles are acute, so arccot(k²+k+1)=arctan(k+1)-arctan k. The four angles therefore telescope to arctan 5-arctan 1, whose tangent is (5-1)/(1+5)=2/3. Its cotangent is 3/2, and the requested value is 15.

**Answer:** 015.

**Methods:** arctangent telescoping, trigonometric identities.

**Verification:** The denominators k²+k+1 are exactly 3,7,13,21; the telescoped angle lies in(0,π/2), so no branch ambiguity occurs.

**Source comparison:** All four alternatives inspected. Pairwise addition gives the correct value. Index 2 confuses cotangent with inverse-cotangent notation, and index 3 switches between two complex products and suppresses positive scale factors as if they were equalities. The consecutive arctangent telescope supplies a shorter exact derivation.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Repeated tangent addition or an arctangent telescope evaluates the angle sum.

## 1984 AIME Problem 15: Extracting a coefficient from a rational system

Real x,y,z,w satisfy x²/(t-1)+y²/(t-9)+z²/(t-25)+w²/(t-49)=1 at t=4,16,36,64. Find x²+y²+z²+w².

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1984_AIME_Problems/Problem_15) · MAA AMC.

### Solution

Let F(t)=(t-1)(t-9)(t-25)(t-49) and S=x²+y²+z²+w². Subtracting the four numerator terms fromF gives a monic quartic H(t) with roots 4,16,36,64. Thus H(t)=(t-4)(t-16)(t-36)(t-64). Its cubic coefficient is-(1+9+25+49)-S=-84-S, while the factored form gives-(4+16+36+64)=-120. Hence S=36.

**Answer:** 036.

**Methods:** polynomial interpolation, Vieta, rational functions.

**Verification:** The four evaluation points are distinct and avoid all poles, so clearing denominators and identifying the monic quartic is valid;120-84=36. Independent exact check passed: Exact rational Gaussian elimination, independent of coefficient extraction.

**Source comparison:** All four entries inspected. Indices 0 and 1 give valid interpolation and coefficient arguments. Index 2 only proposes unperformed elimination. Index 3 misprints two denominator factors in one numerator but uses the correct intended leading-coefficient comparison.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A rational-function interpolation identity extracts the sum of four unknown squares without solving separately.

## 1985 AIME Problem 1: Pairing a reciprocal recurrence

Let x₁=97 and xₙ=n/xₙ₋₁ for n>1. Find x₁x₂⋯x₈.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1985_AIME_Problems/Problem_1) · MAA AMC.

### Solution

All terms are nonzero. The recurrence gives xₙ₋₁xₙ=n. Pairing consecutive factors therefore yields x₁x₂⋯x₈=(x₁x₂)(x₃x₄)(x₅x₆)(x₇x₈)=2·4·6·8=384.

**Answer:** 384.

**Methods:** recurrences, pairing, products.

**Verification:** Each of the four pair identities follows directly at indices 2,4,6,8.

**Source comparison:** Both alternatives use the same cancellation; the long nested-fraction expansion is unnecessary. The initial value matters only by being nonzero.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Adjacent recurrence terms multiply to their index, so the eight-term product pairs off.

## 1985 AIME Problem 3: An integer complex cube

Positive integers a,b,c satisfy c=(a+bi)³-107i, where i²=-1. Find c.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1985_AIME_Problems/Problem_3) · MAA AMC.

### Solution

Comparing imaginary parts gives b(3a²-b²)=107. Since 107 is prime and b>0, b is 1 or 107. The second choice would give 3a²=107²+1≡2(mod 3), impossible. Thus b=1 and 3a²=108, so a=6. The real part is c=a³-3ab²=216-18=198.

**Answer:** 198.

**Methods:** complex expansion, prime divisors, congruences.

**Verification:** (6+i)³=198+107i, so the candidate satisfies the full complex equation. Independent exact check passed: Enumerate the prime-divisor cases and all possible positive a in their bounds.

**Source comparison:** The sole alternative correctly combines real/imaginary parts with the primality of 107 and a modulo 3 exclusion.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. The imaginary part of a complex cube yields a prime-divisor restriction on a positive integer.

## 1985 AIME Problem 5: A six-period recurrence

Integers aₙ satisfy aₙ=aₙ₋₁-aₙ₋₂ for n≥3. The first 1492 terms sum to 1985 and the first 1985 terms sum to 1492. Find the sum of the first 2001 terms.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1985_AIME_Problems/Problem_5) · MAA AMC.

### Solution

If a₁=u,a₂=v, the first six terms are u,v,v-u,-u,-v,u-v. Their sum is 0, and the next two terms are u,v again, proving period 6. Since 1492≡4,1985≡5,2001≡3(mod 6), the given sums are 2v-u=1985 and v-u=1492. Subtraction gives v=493. The requested sum is u+v+(v-u)=2v=986.

**Answer:** 986.

**Methods:** periodic recurrences, partial sums.

**Verification:** The equations give u=-999,v=493; the relevant block-prefix sums are 1985,1492,986. Independent exact check passed: Generate all2001 recurrence terms directly and sum three prefixes.

**Source comparison:** The single archived proof correctly establishes repetition of the state pair and zero total per six-term block.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A second-order linear recurrence has a six-term cycle whose sum is zero.

## 1985 AIME Problem 10: Values of a floor sum

How many integers from 1 through 1000 occur as floor(2x)+floor(4x)+floor(6x)+floor(8x) for real x?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1985_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Put $t=2x$ and $F(t)=\lfloor t\rfloor+\lfloor2t\rfloor+\lfloor3t\rfloor+\lfloor4t\rfloor$. Then $F(t+1)=F(t)+10$. On $0\le t<1$, the breakpoints are $0,1/4,1/3,1/2,2/3,3/4$ and the values are respectively $0,1,2,4,5,6$. Thus exactly six residue classes modulo 10 are attainable, and each occurs 100 times among 1 through 1000. The answer is $600$.

**Answer:** 600.

**Methods:** floor partition, periodic counting.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 9 archived solution entries. Alternatives enumerate breakpoints, use half-period shifts or express the floor sum through Hermite’s identity.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. A floor-sum range is counted by its jump pattern and periodic translates.

## 1986 AIME Problem 1: A fourth-root quadratic

Find the sum of all real solutions of x^(1/4)=12/(7-x^(1/4)), with the principal fourth root.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1986_AIME_Problems/Problem_1) · MAA AMC.

### Solution

Let t=x^(1/4)≥0, with t≠7. Then t(7-t)=12, so(t-3)(t-4)=0. Both possibilities satisfy the domain and the original equation. Thus the x-values are 81 and 256, with sum 337.

**Answer:** 337.

**Methods:** radical substitution, domain restrictions.

**Verification:** 3=12/(7-3) and 4=12/(7-4);81+256=337.

**Source comparison:** The sole alternative correctly substitutes the fourth root and raises both allowed positive roots to the fourth power.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The principal fourth root is a nonnegative substitution reducing the equation to a quadratic.

## 1986 AIME Problem 2: A product of four radical conjugates

Evaluate(√5+√6+√7)(√5+√6-√7)(√5-√6+√7)(-√5+√6+√7).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1986_AIME_Problems/Problem_2) · MAA AMC.

### Solution

The first two factors multiply to (√5+√6)²-7=4+2√30. The last two multiply to 7-(√5-√6)²=-4+2√30. Their product is (2√30)²-4²=120-16=104.

**Answer:** 104.

**Methods:** conjugates, difference of squares.

**Verification:** The general symmetric product is 2(5·6+6·7+7·5)-(5²+6²+7²)=104.

**Source comparison:** All three alternatives correctly evaluate 104. Two use conjugates; the third interprets the product through Heron’s formula and the cosine rule.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Pairing conjugate radical factors twice evaluates the symmetric product.

## 1986 AIME Problem 3: Tangent from a sum and a reciprocal sum

Given tanx+tany=25 and cotx+coty=30, find tan(x+y).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1986_AIME_Problems/Problem_3) · MAA AMC.

### Solution

Put u=tanx,v=tany. The defined cotangents ensure u,v≠0. Since(u+v)/(uv)=30, we obtain uv=25/30=5/6. The tangent addition formula then gives tan(x+y)=25/(1-5/6)=150; the nonzero denominator also shows the requested tangent is defined.

**Answer:** 150.

**Methods:** trigonometric addition, symmetric sums.

**Verification:** The product 5/6 and sum 25 produce denominator 1/6 and tangent 150.

**Source comparison:** All three alternatives agree. The quadratic-formula alternative solves individual tangents unnecessarily; their product already follows from the reciprocal sum.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The sums of tangents and reciprocals determine their product and the tangent of the sum.

## 1986 AIME Problem 4: A common-sum linear system

For i=1,2,3,4,5, let x₁+⋯+x₅+xᵢ equal 6,12,24,48,96 respectively. Find 3x₄+2x₅.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1986_AIME_Problems/Problem_4) · MAA AMC.

### Solution

Let S=x₁+⋯+x₅. Adding the five equations gives 6S=6+12+24+48+96=186, so S=31. Hence x₄=48-31=17 and x₅=96-31=65. The requested combination is 3·17+2·65=181.

**Answer:** 181.

**Methods:** linear systems, symmetric elimination.

**Verification:** The full vector(-25,-19,-7,17,65) sums to 31 and satisfies all five equations.

**Source comparison:** Both alternatives correctly solve the system. Summing the rows extracts the common offset with less work than eliminating each variable.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The common sum of all variables diagonalizes a symmetric linear system.

## 1986 AIME Problem 8: Logarithms of proper divisors

Let S be the sum of the base 10 logarithms of all positive proper divisors of 1,000,000. Find the integer nearest to S.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1986_AIME_Problems/Problem_8) · MAA AMC.

### Solution

The number 10⁶=2⁶5⁶ has 49 positive divisors. The involution d↦10⁶/d pairs logarithms with sum 6; equivalently, summing the identity logd+log(10⁶/d)=6 over all 49 divisors gives twice the full sum as 294. Thus the full sum is 147. Excluding 10⁶ subtracts 6, giving S=141 exactly.

**Answer:** 141.

**Methods:** divisor pairing, logarithms.

**Verification:** Direct exponent summation over 0≤a,b≤6 gives 147 for each prime’s exponent; deleting(6,6) leaves 141 and product 10^141.

**Source comparison:** All three entries reviewed. The divisor-product or involution proof handles the self-paired divisor 1000 automatically. Index 2 has a sign slip in an intermediate sentence but uses the correct final 144+3-6.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Pairing complementary divisors evaluates their logarithmic sum.

## 1986 AIME Problem 10: Recovering a permuted numeral

The five digit permutations of a three-digit numeral other than its original ordering have sum 3194. Recover the original numeral, allowing leading zeros in rearrangements.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1986_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Across all six position permutations, each digit appears twice in every place, so their sum is $222(a+b+c)$. If the original numeral is $N$, then $N+3194=222(a+b+c)$, hence $N\equiv136\pmod{222}$. The three-digit candidates are 136,358,580,802. Substitution of their digit sums into the identity leaves only $358$: $358+3194=222(3+5+8)$.

**Answer:** 358.

**Methods:** digit incidence, hybrid algebra.

**Verification:** Independent exact check passed: Checked every three-digit original numeral, retaining multiplicities of all six position permutations. Result [358]. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 4 archived solution entries. Alternatives supplement digit incidence with congruences modulo 9 and 222.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Digit-position multiplicities determine the omitted original permutation.

## 1986 AIME Problem 11: A translated coefficient of a geometric polynomial

Write 1-x+x²-⋯-x¹⁷ as a polynomial a₀+a₁y+⋯+a₁₇y¹⁷ in y=x+1. Find a₂.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1986_AIME_Problems/Problem_11) · MAA AMC.

### Solution

The polynomial identity(1+x)(1-x+x²-⋯-x¹⁷)=1-x¹⁸ becomes yP(y)=1-(y-1)¹⁸. Thus a₂ is the coefficient of y³ in the right side, namely- C(18,3)(-1)¹⁵=C(18,3)=816. This is a polynomial identity, so division by y does not introduce an exception at y=0.

**Answer:** 816.

**Methods:** coefficient extraction, geometric sums, binomial theorem.

**Verification:** The independent coefficient sumΣ_{k=2}^{17}C(k,2)=C(18,3)=816 agrees.

**Source comparison:** All five alternatives reviewed. Geometric-series compression, hockey-stick summation, second derivatives, and basis matrices give 816. The matrix proof leaves its inverse identity as an exercise; the direct polynomial identity needs no such additional lemma.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A geometric polynomial identity extracts a coefficient after translating the variable.

## 1986 AIME Problem 14: A box from distances to a body diagonal

For a rectangular box, the distances from a body diagonal to the six edges it does not meet take the three values 2√5,30/√13,15/√10. Find the box volume.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1986_AIME_Problems/Problem_14) · MAA AMC.

### Solution

For edges parallel to a side of lengtha, project perpendicular to that direction. The body diagonal projects to a diagonal of a b-by-c rectangle, and the relevant edge projects to a different corner. Its distance is bc/√(b²+c²); the perpendicular feet lie within both segments. Thus the reciprocals of the three squared distances are the pairwise sums of 1/a²,1/b²,1/c². They are 45/900,13/900,40/900. Half the appropriate sums minus the remaining value give the three individual reciprocals 36/900,9/900,4/900. Hence the side lengths are 5,10,15 in some order, and volume 750.

**Answer:** 750.

**Methods:** skew-line distances, orthogonal projection, reciprocal substitution.

**Verification:** For sides $5,10,15$, the face-diagonal altitudes are $50/\sqrt{125}=2\sqrt5$, $150/\sqrt{325}=30/\sqrt{13}$, and $75/\sqrt{250}=15/\sqrt{10}$.

**Source comparison:** The sole archived solution correctly projects to face diagonals and solves a reciprocal-square linear system. Guessing a1:2:3 ratio from the radicals is not needed.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Projecting skew lines gives reciprocal-square equations for a box’s edge lengths.

## 1987 AIME Problem 4: A region bounded by absolute values

Find the area enclosed by|x-60|+|y|=|x|/4.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1987_AIME_Problems/Problem_4) · MAA AMC.

### Solution

A point on the graph must satisfy|x-60|≤|x|/4. Negative x is impossible, and for x≥0 the inequality gives 48≤x≤80. The upper boundary is y=5x/4-60 for 48≤x≤60 and y=60-3x/4 for 60≤x≤80; the lower boundary is its reflection across the x-axis. Thus the vertices are (48,0),(60,15),(80,0),(60,-15), giving area(80-48)·30/2=480.

**Answer:** 480.

**Methods:** absolute values, coordinate area.

**Verification:** All four vertices satisfy the equation and the two triangular halves each have area 240.

**Source comparison:** Both alternatives correctly identify the quadrilateral. Index 0 calls the symmetry a y-axis symmetry instead of x-axis symmetry; index 1 drops an x from one intermediate equation.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. Absolute-value branches form a quadrilateral whose area is determined by its intercepts.

## 1987 AIME Problem 5: A factored equation in two integer squares

Integers x,y satisfy y²+3x²y²=30x²+517. Find 3x²y².

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1987_AIME_Problems/Problem_5) · MAA AMC.

### Solution

Rearrange to (3x²+1)(y²-10)=507=3·13². The first factor is a positive divisor congruent to 1 modulo 3, so it is 1,13,or 169. These give x²=0,4,or 56. The last is not a square; the first would force y²=517, also not a square. Therefore x²=4, and the second factor is 39, giving y²=49. The requested product is 3·4·49=588.

**Answer:** 588.

**Methods:** factorization, integer squares, divisor cases.

**Verification:** For x²=4,y²=49, the original sides equal 49+588=637 and 120+517=637. Independent exact check passed: Enumerate all integer pairs within the bounds supplied by the positive factorization.

**Source comparison:** The sole alternative gives the correct factorization but omits the factor 1 case corresponding to x=0. The new proof explicitly excludes it.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Completing a product converts an integer equation in two squares to finitely many divisor cases.

## 1987 AIME Problem 10: Walking against an escalator

Al walks down an upward-moving escalator, taking 150 walking steps. Bob walks up it, taking 75 walking steps. Al’s walking rate is three times Bob’s. How many steps are visible on the escalator?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1987_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Measure time so Bob walks 1 step per unit and Al walks 3. Their travel times are 75 and 50. If the escalator moves upward at e steps per unit and has visible lengthL, then L=75(1+e)=50(3-e). Therefore 125e=75, so e=3/5 and L=75·8/5=120.

**Answer:** 120.

**Methods:** relative speed, rates, linear equations.

**Verification:** At e=3/5, Bob’s speed 8/5 for 75 units and Al’s downward speed 12/5 for 50 units both cover 120.

**Source comparison:** All five alternatives inspected. Indices 0,3,4 correctly use walking-step counts to determine times. Index 1 divides the walking counts by escalator speed, and index 2 multiplies step counts directly by net speeds; their displayed equations are invalid despite the announced answer 120.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Walking times and relative speeds give two expressions for a fixed escalator length.

## 1987 AIME Problem 12: An integer just above a cube

Let m be the smallest integer with cube root n+r, where n is a positive integer and 0<r<1/1000. Find n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1987_AIME_Problems/Problem_12) · MAA AMC.

### Solution

For fixed n, the least possible integer is n³+1. It works exactly when(n+1/1000)³-n³>1. This difference increases with n. At n=18 it is 972054001/10⁹<1; at n=19 it is 1083057001/10⁹>1. Therefore the first possible n is 19, realized by m=19³+1. Every larger n gives a larger m, so this also minimizes m globally.

**Answer:** 019.

**Methods:** integer bounds, binomial expansion, monotonicity.

**Verification:** The exact cubic increments at 18 and 19 straddle 1, and their monotonicity settles every smaller n.

**Source comparison:** All four alternatives read. Index 1 uses the exact interval width. Index 0 has an insufficiently justified preliminary bound; index 2 simply discards positive small terms, which cannot prove minimality. Index 3 gives derivative bounds but leaves the endpoint comparison implicit.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. An integer immediately above a cube must lie in a short interval whose width increases with the cube root.

## 1987 AIME Problem 14: A telescoping Sophie Germain product

Evaluate the product over j=0,1,2,3,4 of[((10+12j)⁴+324)/((4+12j)⁴+324)].

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1987_AIME_Problems/Problem_14) · MAA AMC.

### Solution

Let F(t)=t²+9. Completing a square gives x⁴+324=F(x-3)F(x+3). The numerator therefore contains F(7),F(13),…,F(61), while the denominator contains F(1),F(7),…,F(55), each with step 6. All common factors cancel. The quotient isF(61)/F(1)=(61²+9)/(1²+9)=373.

**Answer:** 373.

**Methods:** Sophie Germain identity, telescoping products.

**Verification:** The ten factors in each factored list overlap in exactly nine positions;3730/10=373. Independent exact check passed: Form the exact large numerator and denominator, then reduce.

**Source comparison:** All six entries read. The direct quadratic factorization proves telescoping. Index 2 is only an introduction to the complex-root subsolutions at indices 3 and 4; index 5 calls the cancellation a hypothesis instead of writing the general indexed factorization.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Sophie Germain factorization exposes a telescoping quotient of quartics.

## 1987 AIME Problem 15: Two orientations of an inscribed square

Triangle ABC is right-angled at C. One inscribed square has a vertex at C, sides along CA and CB, and its opposite vertex on AB; its area is 441. A second has one side on AB and its other two vertices on CA and CB; its area is 440. Find AC+CB.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1987_AIME_Problems/Problem_15) · MAA AMC.

### Solution

Let the legs be a,b, their sum s, product p, and hypotenuse c. The first square has side ab/(a+b), so p=21s. For the second square, similarity at heightq above the hypotenuse gives q=c(1-q/h), where h=p/c; hence q=pc/(c²+p). Using q²=440 and c²=s²-2p gives 440=441(s²-42s)/(s-21)². Rearrangement yields(s-21)²=441². Since s>0 and p=21s implies s>42, we take s-21=441, so s=462.

**Answer:** 462.

**Methods:** inscribed squares, similarity, symmetric variables.

**Verification:** At s=462,p=9702,c²=194040, the first side is 21 and the second squared side p²c²/(c²+p)² is 440; the leg quadratic has positive roots. Independent exact check passed: Verify both square-area equations with exact rational symmetric data.

**Source comparison:** All four alternatives reviewed. The ratio and symmetric-sum approaches give 462. The source figures were replaced by the two explicit square orientations; these are essential because different inscribed-square placements need not have the same area.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Two differently oriented inscribed squares determine symmetric functions of a right triangle’s legs.

## 1988 AIME Problem 3: Nested logarithms with different bases

A real x satisfies log₂(log₈x)=log₈(log₂x). Find(log₂x)².

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_3) · MAA AMC.

### Solution

Put u=log₂x. The logarithm arguments require u>0. Since log₈x=u/3, the equation is log₂(u/3)=(1/3)log₂u. Multiplication by 3 and the logarithm power rule give(u/3)³=u. Dividing by the positive u yields u²=27, the requested value.

**Answer:** 027.

**Methods:** nested logarithms, domain restrictions, change of base.

**Verification:** The domain selects u=3√3, and (u/3)³=u verifies the transformed equation.

**Source comparison:** All four alternatives obtain 27. Indices 2 and 3 divide by log(log₂x), which requires excluding log₂x=1 first; that value indeed fails the original equation, but the direct positive substitution avoids the extra division.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A nested logarithm equation reduces to a positive cubic relation after changing bases.

## 1988 AIME Problem 4: An absolute-value defect of nineteen

Real numbers x₁,…,xₙ satisfy|xᵢ|<1 and Σ|xᵢ|=19+|Σxᵢ|. Find the least possible n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_4) · MAA AMC.

### Solution

The equation implies Σ|xᵢ|≥19, while the strict individual bounds give Σ|xᵢ|<n. Thus n>19 and n≥20. Choose ten terms equal to 19/20 and ten equal to-19/20. Their sum is 0 and their absolute-value sum is 19, so n=20 is attained.

**Answer:** 020.

**Methods:** absolute values, inequalities, extremal construction.

**Verification:** The 20-term construction has every absolute value 0.95<1, total absolute value 19, and signed sum 0.

**Source comparison:** All three alternatives read. Index 0 proves both the lower bound and construction. Index 1 gives an informal cancellation discussion; index 2 establishes only the lower bound and omits attainability.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The triangle-inequality defect is bounded by the number of terms, with an explicit equality construction.

## 1988 AIME Problem 6: A grid arithmetic in both directions

Index a5×5 grid by coordinates(i,j),0≤i,j≤4, increasing rightward and upward. Every row and column is arithmetic. Given T(0,0)=0,T(1,3)=74,T(4,2)=186,T(2,1)=103, and positive integers in all other cells, find T(3,4).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_6) · MAA AMC.

### Solution

A row is affine in i, and its values at i=0 and 1 are each affine in j. Therefore T(i,j)=αi+βj+γij. The data give α+3β+3γ=74,4α+2β+8γ=186, and 2α+β+2γ=103. Subtracting twice the third equation from the second gives 4γ=-20, so γ=-5. The remaining equations yield β=13 and α=50. Hence T(3,4)=150+52-60=142. This grid is positive away from (0,0), since T(i,j)=i(50-5j)+13j.

**Answer:** 142.

**Methods:** bilinear interpolation, arithmetic progressions, linear systems.

**Verification:** The formula 50i+13j-5 ij reproduces all four given cells;50-5j≥30 ensures positivity of every other cell. Independent exact check passed: Construct all25 cells and verify every row and column difference.

**Source comparison:** All three alternatives read. The general bilinear table in index 1 explains why only three parameters are needed. Index 0 mislabels one target coordinate in prose but computes the intended(3,4). The givens and target were recovered explicitly from the archived tables.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Row-wise and column-wise arithmetic progressions force a bilinear grid formula.

## 1988 AIME Problem 8: A functional equation hiding the least common multiple

On positive integer pairs, f satisfies f(x,x)=x, f(x,y)=f(y,x), and (x+y)f(x,y)=y f(x,x+y). Find f(14,52).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_8) · MAA AMC.

### Solution

Normalize by setting g(x,y)=f(x,y)/(xy). The third identity becomes g(x,x+y)=g(x,y), and symmetry permits interchange of the arguments. Applying the subtractive Euclidean algorithm therefore reduces g(x,y) to g(d,d), where d=gcd(x,y). At that pair, g(d,d)=d/d²=1/d. Hence f(x,y)=xy/gcd(x,y), uniquely. Since gcd(14,52)=2, f(14,52)=14·52/2=364.

**Answer:** 364.

**Methods:** functional equations, Euclidean algorithm, normalization.

**Verification:** The derived formula satisfies all three identities. Subtractive Euclidean reduction of $(14,52)$ passes through $(14,38),(14,24),(10,14),(4,10)$, then through $(4,6),(2,4),(2,2)$, reaching $d=2$.

**Source comparison:** All three alternatives read. The first two perform the recurrence directly. Index 2 verifies that lcm is a solution but appeals to AIME answer uniqueness rather than proving functional uniqueness. The invariant plus descending Euclidean algorithm supplies that proof.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. A two-variable functional equation becomes an invariant under the Euclidean algorithm.

## 1988 AIME Problem 11: Mean lines pass through a centroid

A line is a mean line for complex points w₁,…,w₅ if it contains z₁,…,z₅ with Σ(zₖ-wₖ)=0. For w=(32+170i,-7+64i,-9+200i,1+27i,-14+43i), find the slope of the mean line whose y-intercept is 3.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_11) · MAA AMC.

### Solution

A mean line must contain the average of its points zₖ, which equals the average of the wₖ. Conversely any line through that average works by choosing all zₖ equal to it. Here the average is (3/5,504/5). The line through this point and (0,3) has slope(504/5-3)/(3/5)=163.

**Answer:** 163.

**Methods:** centroids, affine geometry, complex coordinates.

**Verification:** At x=3/5, the line y=163x+3 has y=504/5, and choosing five identical centroid points satisfies the sum condition.

**Source comparison:** All three alternatives give 163. The centroid characterization in index 2 is shortest; the new proof includes its converse, ensuring existence as well as the necessary slope. Index 1 calls Cartesian components polar coordinates.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The affine closure of a line identifies every mean line as a line through the centroid.

## 1988 AIME Problem 12: Three equal terminal pieces of cevians

Cevians AD,BE,CF of triangle ABC meet at an interior point P. Suppose PD=PE=PF=3, while AP=a,BP=b,CP=c and a+b+c=43. Find abc.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Triangles PBC and ABC share their base, and their altitude ratio is PD/AD=3/(a+3). The analogous ratios for the other two sides sum to 1 because PBC,PCA,PAB partition ABC. Therefore 3/(a+3)+3/(b+3)+3/(c+3)=1. Clear denominators and cancel the common 3(ab+bc+ca) terms. The result is abc=9(a+b+c)+54=9·43+54=441.

**Answer:** 441.

**Methods:** concurrent cevians, area ratios, symmetric identities.

**Verification:** The general identity for equal terminal length d is abc=d²(a+b+c)+2d³; d=3 and sum 43 give 441.

**Source comparison:** All four alternatives read. Area ratios, mass points, and a Gergonne/Ceva identity yield the same cubic relation. The proof only needs the sum of the three barycentric area ratios, not a separate theorem citation. Missing figure labels were reconstructed from the explicit ratios.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Concurrent-cevian area ratios give a symmetric cubic identity for three segment lengths.

## 1988 AIME Problem 13: Fibonacci remainders modulo a quadratic

Integers a,b satisfy x²-x-1 | ax¹⁷+bx¹⁶+1 as polynomials. Find a.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_13) · MAA AMC.

### Solution

Modulo x²-x-1, the relation x²=x+1 implies by induction xⁿ≡Fₙx+Fₙ₋₁, where F₀=0,F₁=1 and Fₙ₊₁=Fₙ+Fₙ₋₁. In particular F₁₅=610,F₁₆=987,F₁₇=1597. The remainder vanishes exactly when 1597a+987b=0 and 987a+610b=-1. Multiply the first equation by 610 and the second by 987 and subtract: (1597·610-987²)a=987. The coefficient is 1, so a=987.

**Answer:** 987.

**Methods:** polynomial remainders, Fibonacci recurrence, linear systems.

**Verification:** a=987,b=-1597 make both remainder coefficients zero:1597·987-987·1597=0 and 987²-610·1597+1=0. Independent exact check passed: Perform exact polynomial long division instead of using the Fibonacci formula.

**Source comparison:** All eight alternatives inspected. Remainder recurrence and repeated squaring give rigorous proofs. Indices 0,2,7 have indexing or sign mistakes in generalized pattern statements; index 7 substitutes pattern recognition for induction. Index 4 relies on the contest answer range to fix a parameter, omitting the second coefficient equation. The exact determinant resolves uniqueness without that assumption.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Remainders modulo a quadratic follow the Fibonacci recurrence and determine two coefficients.

## 1988 AIME Problem 14: Reflecting a rectangular hyperbola

Reflect the curve xy=1 in the line y=2x. Write its equation as 12x²+bxy+cy²+d=0. Find bc.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_14) · MAA AMC.

### Solution

A unit vector along the reflecting line is u=(1,2)/√5. Reflection is v↦2(v·u)u-v, with matrix(1/5)[[-3,4],[4,3]]. Since reflection is its own inverse, a point(x,y) on the reflected curve corresponds to ((-3x+4y)/5,(4x+3y)/5) on the original. Their product is 1, so-12x²+7 xy+12y²=25. In the requested normalization, b=-7,c=-12, and bc=84.

**Answer:** 084.

**Methods:** reflection matrices, conics, coordinate transformations.

**Verification:** The reflection matrix squares to the identity and fixes(1,2). Expanding the transformed coordinate product gives the stated normalized coefficients.

**Source comparison:** All four alternatives read. The coordinate reflection method is complete. Index 2 writes an incorrect principal-arctangent equality for the doubled angle and misprints 3/5 as 5/5 once; its intended matrix and final equation are correct. Index 3 proposes a point-fitting calculation without carrying it out.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A reflection matrix transforms a rectangular hyperbola’s quadratic equation.

## 1989 AIME Problem 1: A square hidden among four consecutive factors

Evaluate √(31·30·29·28+1).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1989_AIME_Problems/Problem_1) · MAA AMC.

### Solution

Pair the factors as 31·28=868 and 30·29=870. Then the radicand is (869−1)(869+1)+1=869², so its positive square root is 869.

**Answer:** 869.

**Methods:** difference of squares, consecutive integers.

**Verification:** 869²=755161 and 868·870+1=755161.

**Source comparison:** All six alternatives read. The central-product identity is decisive. Index 5 uses last digits and an informal approximation without proving the necessary bounds or integrality.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Four consecutive factors become the difference of two adjacent squares.

## 1989 AIME Problem 3: A repeated decimal digit forced by divisibility

For a positive integer n and a decimal digit d, n/810=0.d25d25d25…. Find n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1989_AIME_Problems/Problem_3) · MAA AMC.

### Solution

The repeating decimal equals (100d+25)/999. Therefore n=750(4d+1)/37. Since 750 is relatively prime to 37, integrality requires 37 to divide 4d+1. For 0≤d≤9, this expression lies between 1 and 37, so it must equal 37. Thus d=9 and n=750.

**Answer:** 750.

**Methods:** repeating decimals, divisibility, digit constraints.

**Verification:** 750/810=25/27=925/999=0.925925…. Independent exact check passed: Exhaust the digit and numerator ranges with exact fractions.

**Source comparison:** All four alternatives read. The denominator-divisibility argument supplies uniqueness. Index 3 incorrectly states that n divides 25 and 30; its conclusion is not supported by that sentence.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. A repeated three-digit decimal is converted to a fraction and constrained by divisibility.

## 1989 AIME Problem 6: The first possible moving rendezvous

A and B are 100 units apart. Allie leaves A at speed 8 along a ray making a 60° angle with AB. Billie leaves B simultaneously at speed 7 along a chosen straight ray. What distance has Allie traveled at their earliest possible meeting?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1989_AIME_Problems/Problem_6) · MAA AMC.

### Solution

Set $A=(0,0)$ and $B=(100,0)$. After time $t>0$, Allie is at $(4t,4\sqrt3t)$. Billie can reach this point in the same time precisely when its distance from $B$ is $7t$. Squaring gives $(100-4t)^2+48t^2=49t^2$, or $3t^2-160t+2000=0$. Its roots are $20$ and $100/3$, and each determines a valid ray from $B$. The earlier meeting occurs at $t=20$, when Allie has traveled $8\cdot20=160$.

**Answer:** 160.

**Methods:** relative motion, law of cosines, quadratic equations.

**Verification:** At $t=20$ the displacement from $B$ is $(-20,80\sqrt3)$, whose squared length is $19600=(7\cdot20)^2$.

**Source comparison:** All four alternatives read. The coordinate quadratic retains both possible meeting times. Several geometric alternatives choose an orientation that yields the earlier branch without discussing the second; index 0 also writes two proportional quadratic expressions as literally equal.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. An earliest meeting of two constant-speed travelers is a quadratic distance equation.

## 1989 AIME Problem 7: Squares of an arithmetic progression

An integer k is added to 36, 300, and 596. The three resulting numbers, in that order, are squares of three consecutive terms of an arithmetic progression. Find k.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1989_AIME_Problems/Problem_7) · MAA AMC.

### Solution

Write those terms as $u-d,u,u+d$. Taking the second difference of their squares gives $2d^2=596-2\cdot300+36=32$, hence $d^2=16$. Taking the first difference gives $2ud-d^2=300-36=264$, so $ud=140$. Therefore $u^2=(ud)^2/d^2=1225$ and $k=u^2-300=925$. The signs of $u$ and $d$ do not affect this conclusion.

**Answer:** 925.

**Methods:** arithmetic progressions, finite differences, squares.

**Verification:** 36+925=31², 300+925=35², and 596+925=39².

**Source comparison:** All three alternatives read. Index 2 misprints the second-difference equation as 4d²=32 while proceeding to d=4. The sign-free calculation avoids assumptions about positive square roots.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The second difference of three squared arithmetic-progression terms fixes the common difference.

## 1989 AIME Problem 8: A quadratic sequence of linear forms

Real numbers x₁,…,x₇ satisfy Σi²xᵢ=1, Σ(i+1)²xᵢ=12, and Σ(i+2)²xᵢ=123, with every sum over i=1,…,7. Find Σ(i+3)²xᵢ.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1989_AIME_Problems/Problem_8) · MAA AMC.

### Solution

Define F(t)=Σ(i+t)²xᵢ. It is a polynomial of degree at most two, so its third finite difference vanishes: F(3)−3F(2)+3F(1)−F(0)=0. Thus the requested value is 3·123−3·12+1=334.

**Answer:** 334.

**Methods:** finite differences, polynomial interpolation, linear forms.

**Verification:** The unique quadratic through F(0)=1,F(1)=12,F(2)=123 is 50t²−39t+1, which gives F(3)=334.

**Source comparison:** All seven archived entries read, including mathematical text accompanying a video link; no video was viewed. Index 5 arbitrarily sets four variables to zero without first proving that the requested expression is invariant. The polynomial identity proves that invariance directly.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Shifted square coefficient vectors have zero third finite difference.

## 1989 AIME Problem 14: Real integers written in a complex base

Let β=−3+i. Consider four-digit expressions a₃β³+a₂β²+a₁β+a₀ with decimal digits 0≤aⱼ≤9 and a₃≠0. Find the sum of all distinct real integers represented.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1989_AIME_Problems/Problem_14) · MAA AMC.

### Solution

Since β²=8−6i and β³=−18+26i, vanishing imaginary part requires a₁−6a₂+26a₃=0. As 6a₂−a₁≤54, we have a₃=1 or 2. For a₃=1, the digit bounds on a₁=6a₂−26 force (a₂,a₁)=(5,4). For a₃=2 they force (a₂,a₁)=(9,2). The real parts are respectively 10+a₀ and 30+a₀. Thus the represented integers are exactly 10,…,19 and 30,…,39, with sum 145+345=490.

**Answer:** 490.

**Methods:** complex bases, digit constraints, bounded linear equations.

**Verification:** The complete digit analysis yields precisely twenty integers in two disjoint ten-term intervals. Independent exact check passed: Enumerate every four-digit complex-base numeral using integer real/imaginary components.

**Source comparison:** The single archived alternative correctly reduces the imaginary part to two digit cases. The two resulting integer intervals are disjoint, so summing numerals does not introduce duplicate values.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. The imaginary part of a complex-base numeral imposes a bounded linear equation on its digits.

## 1990 AIME Problem 2: A difference of conjugate radical cubes

Evaluate (52+6√43)^(3/2)−(52−6√43)^(3/2).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1990_AIME_Problems/Problem_2) · MAA AMC.

### Solution

The positive square roots of the two bases are √43+3 and √43−3, because √43>3. Their cubed difference is (√43+3)³−(√43−3)³=6(3·43+9)=828.

**Answer:** 828.

**Methods:** denesting radicals, difference of cubes.

**Verification:** (√43±3)²=52±6√43, and the odd powers of √43 cancel in the cubed difference.

**Source comparison:** All six alternatives read. Index 3 changes the required difference into a sum and contains several incorrect expansions. Index 4 misprints a²+b² as 102 before using the correct 104. Index 5 repeats the plus sign in the original expression once. The positive-root denesting avoids these issues.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Conjugate radicals become a difference of cubes of positive square roots.

## 1990 AIME Problem 4: Three denominators with a common quadratic part

Find the positive real solution of 1/(x²−10x−29)+1/(x²−10x−45)−2/(x²−10x−69)=0.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1990_AIME_Problems/Problem_4) · MAA AMC.

### Solution

Set t=x²−10x−29, with t≠0,16,40. Multiplying the transformed equation 1/t+1/(t−16)−2/(t−40)=0 by its nonzero denominator gives −64t+640=0, so t=10. Therefore x²−10x−39=(x−13)(x+3)=0. The positive solution is 13, and t=10 violates none of the denominator restrictions.

**Answer:** 013.

**Methods:** substitution, rational equations, domain restrictions.

**Verification:** For x=13 the three denominators are 10,−6,−30, and 1/10−1/6+1/15=0.

**Source comparison:** The sole alternative correctly uses a common-expression substitution. The new proof explicitly tracks excluded denominator values.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A shared quadratic denominator expression reduces a rational equation to a linear one.

## 1990 AIME Problem 10: Products of two root-of-unity groups

Let $A=\{z:z^{18}=1\}$ and $B=\{w:w^{48}=1\}$. How many distinct complex numbers occur as $zw$ with $z\in A$ and $w\in B$?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1990_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Let $\zeta=e^{2\pi i/144}$. Every product has the form $\zeta^{8a+3b}$, so it is among the $144$ powers of $\zeta$. Conversely, fix any integer $k$. Choose $a\in\{0,1,2\}$ with $8a\equiv k\pmod3$, and set $b=(k-8a)/3$. Then $\zeta^{8a}$ is an eighteenth root and $\zeta^{3b}$ is a forty-eighth root, and their product is $\zeta^k$. Thus all $144$ distinct powers occur.

**Answer:** 144.

**Methods:** roots of unity, finite cyclic groups, image counting, least common multiple.

**Verification:** The multiplication map has 18·48 inputs and kernel {(u,u⁻¹):u⁶=1} of size 6, independently giving 864/6=144 products. Independent exact check passed: Enumerate all864 root-product exponents, independently checking the image size.

**Source comparison:** All three alternatives read. The first uses a Frobenius-number argument that needs explicit reduction of exponent ranges. The second comment incorrectly claims every integer 0 through 143 is literally representable with nonnegative bounded exponents; modular representability is sufficient. The third uses synchronized exponents, which does generate all 144 values but needs an order calculation.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra, number_theory. The number of distinct products of roots of unity is the size of a finite cyclic-group image.

## 1990 AIME Problem 15: A recurrence for weighted power sums

Real a,b,x,y satisfy ax+by=3, ax²+by²=7, ax³+by³=16, and ax⁴+by⁴=42. Find ax⁵+by⁵.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1990_AIME_Problems/Problem_15) · MAA AMC.

### Solution

Put Tₙ=axⁿ+byⁿ, S=x+y, and P=xy. Since each of x,y satisfies t²−St+P=0, we have Tₙ₊₂=STₙ₊₁−PTₙ. The given values imply 7S−3P=16 and 16S−7P=42. Solving yields S=−14,P=−38. Hence T₅=−14·42+38·16=20.

**Answer:** 020.

**Methods:** power sums, linear recurrences, characteristic polynomials.

**Verification:** The coefficient system has determinant −1 and thus uniquely determines the recurrence; its characteristic roots −7±√87 are real.

**Source comparison:** All four alternatives read. The recurrence arguments are valid. Index 2 gives an incorrect sum of the first three equations and ends with an unperformed elimination, so it is incomplete. The direct elimination in index 3 works but requires unnecessary radical roots.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Two weighted exponential sequences satisfy the same second-order linear recurrence.

## 1991 AIME Problem 1: Symmetric sums with an integer restriction

Positive integers x,y satisfy xy+x+y=71 and x²y+xy²=880. Find x²+y².

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_1) · MAA AMC.

### Solution

Let s=x+y and p=xy. Then s+p=71 and sp=880, so {s,p}={16,55}. Positive integers satisfy xy≥x+y−1, because (x−1)(y−1)≥0. Thus s=55,p=16 is impossible. Therefore s=16,p=55 and x²+y²=s²−2p=146. The values x,y=5,11 verify existence.

**Answer:** 146.

**Methods:** symmetric sums, Vieta formulas, integer inequalities.

**Verification:** 5·11+5+11=71 and 5·11·16=880. Independent exact check passed: Exhaust positive integer pairs within the first-equation bound.

**Source comparison:** All five alternatives read. Indices 2 and 4 discard the wrong branch only because it would exceed the contest answer range; index 3 leaves that exclusion implicit. The positive-integer inequality eliminates it mathematically.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Symmetric sums reduce the equations to two cases, and positive integrality eliminates one.

## 1991 AIME Problem 2: Parallel slices of a rectangle

In a 4 by 3 rectangle ABCD, divide AB and CB into 168 equal parts starting at A and C, and join corresponding interior division points. Repeat on AD and CD, then include diagonal AC. Find the total length of the resulting 335 parallel segments.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_2) · MAA AMC.

### Solution

The diagonal has length 5. By similarity, the 167 interior segments on either side have lengths 5j/168 for j=1,…,167. Hence their total, including the diagonal once, is 5+(10/168)(167·168/2)=5+835=840.

**Answer:** 840.

**Methods:** similar triangles, arithmetic sums, parallel segments.

**Verification:** There are 2·167+1=335 segments, and each pair of complementary slice lengths sums to 5.

**Source comparison:** All three alternatives read. Index 0 mixes the summation endpoints and subtraction of the diagonal, obtaining the right total through inconsistent displayed arithmetic. The other two give valid direct summation or pairing arguments.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Similar right triangles produce an arithmetic sequence of parallel segment lengths.

## 1991 AIME Problem 3: The peak of a weighted binomial row

For $0\le k\le1000$, let $A_k=\binom{1000}{k}(0.2)^k$. Find the index $k$ for which $A_k$ is largest.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_3) · MAA AMC.

### Solution

For $0\le k<1000$, $A_{k+1}/A_k=(1000-k)/(5(k+1))$. This ratio exceeds 1 exactly when $k<995/6$, and is less than 1 exactly when $k>995/6$. Thus the sequence strictly increases through $A_{166}$ and strictly decreases afterward. Its unique maximum is at $k=166$.

**Answer:** 166.

**Methods:** binomial coefficients, successive ratios, unimodality.

**Verification:** A₁₆₆/A₁₆₅=835/830>1, while A₁₆₇/A₁₆₆=834/835<1. Independent exact check passed: Compare all1001 weighted binomial terms after multiplying by the common denominator5^1000.

**Source comparison:** All five alternatives read. Index 0 contains a false factorial simplification and its general maximum formula needs a two-mode caveat when the threshold is integral. Indices 1 and 4 confuse the threshold index in prose. The exact neighboring ratio establishes both monotonicity and uniqueness.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Ratios of neighboring weighted binomial coefficients determine their unique maximum.

## 1991 AIME Problem 4: Counting logarithm-sine intersections rigorously

How many real x satisfy (log₂x)/5=sin(5πx)?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_4) · MAA AMC.

### Solution

The sine bound restricts x to [1/32,32]. Put f(x)=sin(5πx)−ln(x)/(5ln2). Below 1, roots can occur only in the negative sine lobes (1/5,2/5) and (3/5,4/5), or at x=1. On either negative lobe f is strictly convex, since f″=−25π²sin(5πx)+1/(5ln2·x²)>0. It is positive at both endpoints and negative at the midpoint, so each lobe gives exactly two roots. Also x=1 is a root. Above 1, only the positive lobes (2j/5,(2j+1)/5), j=3,…,79, can contribute. On each, f is negative at the endpoints and positive at its midpoint. It has exactly one maximum: on the first half, x²sin(5πx) strictly increases, so f″ changes sign at most once, from positive to negative; f′ starts positive and is negative at the midpoint, hence has exactly one zero. On the second half f′<0. Therefore each of the 77 positive lobes has exactly two roots. The total is 4+1+2·77=159.

**Answer:** 159.

**Methods:** root counting, periodic functions, monotonicity, convexity.

**Verification:** The two negative lobes contribute four roots, 77 complete positive lobes contribute 154, and the sole common zero is x=1; neither domain endpoint solves the equation.

**Source comparison:** Both alternatives read. They assume without proof that every relevant lobe contributes exactly two intersections. Index 0 incorrectly locates the common zero at x=1/5 instead of x=1. The derivative argument supplies a rigorous count and checks the end lobes.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The number of logarithm-sine intersections is controlled on each positive or negative lobe.

## 1991 AIME Problem 6: Recovering a number from a floor sum

A real r satisfies Σₖ₌₁₉⁹¹ floor(r+k/100)=546. Find floor(100r).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_6) · MAA AMC.

### Solution

The 73 floor values are nondecreasing and differ by at most 1. Since 546=73·7+35, they consist of 38 sevens followed by 35 eights. The last seven occurs at k=56 and the first eight at k=57. Thus r+56/100<8≤r+57/100, giving 7.43≤r<7.44. Therefore floor(100r)=743.

**Answer:** 743.

**Methods:** floor functions, threshold counting, interval recovery.

**Verification:** Throughout [7.43,7.44), offsets 19 through 56 give 7 and offsets 57 through 91 give 8, totaling 546.

**Source comparison:** All three entries read. Index 0 is only a warning that a removed solution was incorrect. Index 1 gives the valid jump argument. Index 2 uses Hermite’s identity but reverses a displayed monotonic inequality and ambiguously includes the endpoint r+1; the identity requires exactly the hundred offsets 0 through 99.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. A run of equally spaced floor terms has a single jump, fixing the fractional interval.

## 1991 AIME Problem 7: A finite continued fraction and its fixed points

Let f(t)=√19+91/t. Find the square of the sum of the absolute values of all real solutions of x=f(f(f(f(f(x))))), with every intermediate expression defined.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_7) · MAA AMC.

### Solution

Represent f by M=[[s,91],[1,0]], where s=√19; multiplying such matrices composes the corresponding fractional linear maps. Since M²=sM+91I, induction gives M⁵=uM+vI with u>0 and v≥0. Consequently the fixed-point equation for f⁵, wherever defined, is ((us+v)x+91u)/(ux+v)=x, which reduces to x²−sx−91=0. Its two roots are (√19±√383)/2. Each is nonzero and fixed by f itself, so both satisfy the original equation with all iterates defined. They have opposite signs; their absolute values sum to √383, whose square is 383.

**Answer:** 383.

**Methods:** fractional linear transformations, iteration, matrix polynomials.

**Verification:** The fixed-point polynomial has product of roots −91, and substitution into f(t)=t ensures that no intermediate denominator vanishes.

**Source comparison:** Both alternatives read. Index 0 replaces an inner finite fraction by x without justification. Index 1 appeals to a quadratic degree bound but does not rule out an identity iterate or verify all denominators. The positive matrix-polynomial coefficient proves that the iterate is not the identity and verifies both roots.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. An odd iterate of a fractional linear transformation has the same fixed points as the transformation.

## 1991 AIME Problem 8: Integer roots via a shifted factorization

For how many real values a does x²+ax+6a=0 have two integer roots, counted with multiplicity?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_8) · MAA AMC.

### Solution

If the roots are r,s, then r+s=−a and rs=6a. Eliminating a gives (r+6)(s+6)=36. Unordered positive factor pairs of 36 are (1,36),(2,18),(3,12),(4,9),(6,6), and there are five corresponding negative pairs. Each gives integer r,s and a=12−((r+6)+(s+6)). The positive pair sums 37,20,15,13,12 are distinct, and the negative pair sums are their negatives; hence all ten values of a are distinct. The answer is 10.

**Answer:** 010.

**Methods:** integer roots, Vieta formulas, factor pairs.

**Verification:** The ten parameter values are −25,−8,−3,−1,0,24,25,27,32,49. Independent exact check passed: Enumerate all shifted-factor-bounded integer root pairs and distinct parameters.

**Source comparison:** Both alternatives read. The shifted-root factorization is shorter than the discriminant approach. Counting pairs alone requires checking that different pairs do not yield the same parameter; their explicit sums establish injectivity.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Integer quadratic roots correspond to signed factor pairs of 36 after a Vieta shift.

## 1991 AIME Problem 9: A rational transformation of trigonometric sums

Suppose sec x+tan x=22/7. Write csc x+cot x=m/n in lowest terms with n>0. Find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_9) · MAA AMC.

### Solution

The identity (sec x+tan x)(sec x−tan x)=1 gives sec x−tan x=7/22. Adding and subtracting yields sec x=533/308 and tan x=435/308. Thus cos x=308/533 and sin x=435/533, both positive. Therefore csc x+cot x=(533+308)/435=29/15, and m+n=44.

**Answer:** 044.

**Methods:** trigonometric identities, reciprocal pairs, rational parametrization.

**Verification:** 533²−435²=308², and (533+435)/308=22/7.

**Source comparison:** All nine alternatives read. Reciprocal secant-tangent pairs determine the signs directly. Several alternatives assume an acute representative or take a positive square root without first proving the signs; index 8 explicitly checks the extraneous sine value introduced by squaring.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Reciprocal trigonometric identities determine a rational half-angle expression.

## 1991 AIME Problem 15: An attainable vector minimum that is integral

For each positive integer n, let Sₙ be the minimum of Σₖ₌₁ⁿ√((2k−1)²+aₖ²) over positive real aₖ with Σaₖ=17. Find the unique n for which Sₙ is an integer.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_15) · MAA AMC.

### Solution

The triangle inequality for vectors (2k−1,aₖ) gives Sₙ≥√((Σ(2k−1))²+17²)=√(n⁴+289). Equality is attained by aₖ=17(2k−1)/n², which is positive and sums to 17; hence this bound is the actual minimum. If Sₙ=m is integral, then (m−n²)(m+n²)=289. The positive factor pairs are (1,289) and (17,17). The latter gives n=0 and is excluded. The former gives n²=144, so n=12, and indeed S₁₂=145.

**Answer:** 012.

**Methods:** triangle inequality, equality cases, perfect squares, factorization.

**Verification:** At n=12, the chosen aₖ sum to 17 and all vectors are parallel; 144²+17²=145².

**Source comparison:** All four alternatives read. Indices 0 and 1 state a lower bound but do not explicitly construct equality. Index 3 has sign errors in its difference-of-squares factorization. The proportional positive coordinates prove attainment, and factor pairs establish uniqueness.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. The vector triangle inequality gives an attainable minimum, whose integrality becomes a difference of squares.

## 1992 AIME Problem 3: A small improvement in a win ratio

Before a weekend a tennis player has won exactly half her matches. She then wins three of four matches, raising her win ratio above 0.503. What is the largest possible number of wins she had beforehand?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_3) · MAA AMC.

### Solution

If she initially had $w$ wins, she had played $2w$ matches. The new ratio satisfies $(w+3)/(2w+4)>503/1000$. The denominator is positive, so cross-multiplication gives $1000w+3000>1006w+2012$, or $w<494/3=164\tfrac23$. Thus the greatest possible integer is $164$, which satisfies the strict inequality.

**Answer:** 164.

**Methods:** rational inequalities, integer bounds, ratios.

**Verification:** For w=164, the ratio is 167/332>503/1000 because 167000>166996; w=165 fails.

**Source comparison:** Both alternatives correctly translate and solve the strict inequality. The integer endpoint must be checked against a strict rather than weak bound.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The change in a win ratio gives a strict rational inequality for the initial win count.

## 1992 AIME Problem 4: Three consecutive binomial coefficients in a ratio

Rows of Pascal's triangle are numbered from row $0$, containing only $1$. In which row do three consecutive entries occur in the ratio $3:4:5$?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_4) · MAA AMC.

### Solution

Write the entries as $\binom n{k-1},\binom nk,\binom n{k+1}$. Neighboring ratios give $k/(n-k+1)=3/4$ and $(n-k)/(k+1)=5/4$. Hence $4k=3(n-k+1)$ and $4(n-k)=5(k+1)$. Solving gives $k=27,n=62$. These indices lie inside row $62$, and the two ratios verify the required triple.

**Answer:** 062.

**Methods:** Pascal triangle, binomial ratios, linear systems.

**Verification:** At n=62,k=27, k/(n−k+1)=27/36=3/4 and (n−k)/(k+1)=35/28=5/4. Independent exact check passed: Compare exact adjacent binomial integers in the first101 rows.

**Source comparison:** Both alternatives correctly reduce adjacent-binomial ratios to linear equations. No large binomial coefficients need to be evaluated.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Ratios of adjacent Pascal-triangle entries yield two linear equations for their indices.

## 1992 AIME Problem 8: A quadratic sequence from second differences

A real sequence satisfies aₙ₊₂−2aₙ₊₁+aₙ=1 for every positive n, with a₁₉=a₉₂=0. Find a₁.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_8) · MAA AMC.

### Solution

The sequence qₙ=(n−19)(n−92)/2 has second difference 1 and vanishes at n=19 and 92. Thus bₙ=aₙ−qₙ has zero second difference, so its first differences are constant and bₙ is affine in n. Its two distinct zeros force bₙ=0 for every n. Hence a₁=(1−19)(1−92)/2=819.

**Answer:** 819.

**Methods:** finite differences, quadratic sequences, uniqueness.

**Verification:** The polynomial (n−19)(n−92)/2 has leading coefficient 1/2, hence constant second difference 1, and a₁=819.

**Source comparison:** All six alternatives read. Index 0 uses a differential-equation analogy as a guess without proving uniqueness. Index 1 contains an incorrect general Newton expansion and a dropped −1 in a coefficient. Index 5 has arithmetic transcription errors near its last elimination. The difference of two candidate sequences proves uniqueness cleanly.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Constant second differences force a quadratic sequence with two prescribed zeros.

## 1992 AIME Problem 10: A square outside two semicircles

Let A consist of nonzero complex z such that the real and imaginary parts of both z/40 and 40/conj(z) lie in [0,1]. Find the integer nearest the area of A.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Write z=x+iy. The first condition gives 0≤x,y≤40. The second gives x²+y²≥40x and x²+y²≥40y, so the region is the square outside the circles centered at (20,0) and (0,20), both of radius 20. Within the square these are two semicircles, each of area 200π. Their overlap consists of two 90° circular segments, with total area 2(100π−200)=200π−400. Their union therefore has area 200π+400. The required area is 1600−(200π+400)=1200−200π≈571.681, whose nearest integer is 572.

**Answer:** 572.

**Methods:** complex inequalities, circle intersections, area inclusion-exclusion.

**Verification:** Using 3.14159<π<3.14160 puts the exact area between 571.680 and 571.682, safely rounding to 572.

**Source comparison:** The sole alternative obtains the correct final area but calls 200π+400 the overlap; it is actually the union area. The true overlap is 200π−400. Distinguishing those regions fixes the exposition.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Complex-coordinate inequalities describe a square with two semicircular regions removed.

## 1992 AIME Problem 13: Maximum area on an Apollonius circle

Triangle ABC has AB=9 and BC:AC=40:41. Find its largest possible area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_13) · MAA AMC.

### Solution

Place B=(0,0), A=(9,0), and C=(x,y). The side ratio gives 1681(x²+y²)=1600((x−9)²+y²). Completing the square yields (x+1600/9)²+y²=(1640/9)². Thus C lies on a circle of radius 1640/9, and its greatest possible distance from line AB is that radius, attained directly above or below the circle’s center. The maximum area is (9/2)(1640/9)=820.

**Answer:** 820.

**Methods:** Apollonius circles, maximum triangle area, completing the square.

**Verification:** The highest locus point has nonzero altitude and satisfies the exact squared-distance ratio 1600:1681.

**Source comparison:** All five alternatives read. Coordinate and Heron/AM-GM methods are valid when attainment is checked. Index 0 contains a 1600-versus-1600/81 simplification typo; index 4 duplicates a prefactor in its final line. The locus circle both bounds and attains the altitude.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A fixed side ratio gives an Apollonius circle whose radius maximizes the altitude.

## 1992 AIME Problem 14: A universal product identity for cevian ratios

Cevians AA′,BB′,CC′ of triangle ABC meet at an interior point O, with A′,B′,C′ on the opposite sides. If AO/OA′+BO/OB′+CO/OC′=92, find the product of these three ratios.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_14) · MAA AMC.

### Solution

Set x=AO/OA′, y=BO/OB′, z=CO/OC′. The area fraction [OBC]/[ABC] equals OA′/AA′=1/(1+x), and the analogous fractions sum to 1. Thus 1/(1+x)+1/(1+y)+1/(1+z)=1. Clearing denominators gives xy+xz+yz+2(x+y+z)+3=xyz+xy+xz+yz+x+y+z+1. Therefore xyz=x+y+z+2=94.

**Answer:** 094.

**Methods:** barycentric areas, concurrent cevians, symmetric identities.

**Verification:** The denominator factors are positive because O is interior, and the exact identity xyz=x+y+z+2 follows without assumptions about triangle shape.

**Source comparison:** All four alternatives read. The area-coordinate and mass-point proofs are complete. Index 2 arbitrarily sets two barycentric coordinates equal without proving invariance, so that specialization alone is insufficient. Clearing the universal area identity supplies the needed invariant.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Barycentric area fractions imply a symmetric identity among concurrent-cevian ratios.

## 1993 AIME Problem 2: A forty-day spiral of square distances

A traveler goes east, north, west, south in a repeating four-day cycle. On day n he travels n²/2 miles. How far is he from his starting point after 40 days?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_2) · MAA AMC.

### Solution

Group the days into ten blocks indexed by $j=0,\ldots,9$. The east-minus-west displacement in block $j$ is $((4j+1)^2-(4j+3)^2)/2=-8j-4$. The north-minus-south displacement is $((4j+2)^2-(4j+4)^2)/2=-8j-6$. Summing with $\sum_{j=0}^9j=45$ gives total displacement $(-400,-420)$. Its length is $\sqrt{400^2+420^2}=20\sqrt{20^2+21^2}=580$.

**Answer:** 580.

**Methods:** vector displacement, difference of squares, arithmetic sums.

**Verification:** The component magnitudes 400 and 420 form the scaled 20–21–29 right triangle.

**Source comparison:** The sole alternative correctly groups days into four-day blocks. Its initial prose calls an entire block the first day and briefly drops a factor 1/2, but the displayed block sums and final result are correct.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Alternating directional square distances sum to two perpendicular displacement components.

## 1993 AIME Problem 3: Recovering a total from overlapping averages

In a fishing contest the winner catches 15 fish. Exactly 9,5,7 contestants catch 0,1,2 fish respectively, and 5,2,1 catch 13,14,15 respectively. Those catching at least 3 average 6 fish; those catching at most 12 average 5. Find the total fish caught.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_3) · MAA AMC.

### Solution

Let N be the number of contestants and F the fish total. Removing the 21 contestants with fewer than 3 fish removes 19 fish, so F−19=6(N−21). Removing the eight contestants with more than 12 fish removes 108 fish, so F−108=5(N−8). Thus F=6N−107=5N+68, giving N=175 and F=943.

**Answer:** 943.

**Methods:** weighted averages, linear systems, subtracting complementary groups.

**Verification:** (943−19)/(175−21)=6 and (943−108)/(175−8)=5.

**Source comparison:** Both alternatives correctly set up overlapping population totals. The original table also lists 23 contestants catching three fish, but that datum is unnecessary for determining the requested total and is omitted from the concise restatement.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Two conditional averages determine the total numbers of contestants and fish.

## 1993 AIME Problem 5: Twenty translations of a polynomial

Let P₀(x)=x³+313x²−77x−8, and define Pₙ(x)=Pₙ₋₁(x−n) for n≥1. Find the coefficient of x in P₂₀(x).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_5) · MAA AMC.

### Solution

Composing the translations gives P₂₀(x)=P₀(x−(1+⋯+20))=P₀(x−210). Its linear coefficient is 3·210²−626·210−77=210(630−626)−77=763.

**Answer:** 763.

**Methods:** polynomial translation, coefficient extraction.

**Verification:** The same coefficient equals P₀′(−210)=3·210²−626·210−77=763.

**Source comparison:** Both alternatives correctly combine the shifts. The root-translation/Vieta method is valid but adds variables that direct coefficient extraction avoids.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Repeated polynomial translations combine into one shift, after which only the linear coefficient is needed.

## 1993 AIME Problem 13: When a moving line of sight clears a building

Jenny and Kenny walk in the same direction at 1 and 3 feet per second on parallel paths 200 feet apart. A circular building of diameter 100 is centered midway between the paths. When it first blocks their view they are 200 feet apart. If visibility returns after t seconds, find numerator plus denominator of t in lowest terms.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_13) · MAA AMC.

### Solution

At first blockage they are abreast, since their separation equals the distance between the paths. Put the building center at the origin and their positions at (−50,100) and (−50,−100). At time t they are J=(−50+t,100), K=(−50+3t,−100), and their joining line is 100x+ty=200t−5000. Its distance from the origin is |200t−5000|/√(10000+t²). Tangency occurs when this equals 50; squaring and simplifying gives t(15t−800)=0. For 0<t<160/3 the line’s distance is less than 50, and the intersected circle lies between the paths, so the segment is blocked. Visibility returns at t=160/3; the requested sum is 163.

**Answer:** 163.

**Methods:** distance to a line, moving geometry, tangency, visibility interval.

**Verification:** The squared distance minus 2500 has numerator 2500t(15t−800), establishing the sign throughout the blockage interval.

**Source comparison:** All four alternatives read. Coordinate, angle-bisector, similarity, and area methods agree. The new proof checks the interval between the two tangencies and confirms that line intersection corresponds to segment blockage, not merely an intersection outside the walkers.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The line of sight becomes tangent to a circle at the endpoints of a visibility interval.

## 1993 AIME Problem 14: The least perimeter of an unstuck inscribed rectangle

A rectangle inscribed in a 6 by 8 rectangle has one vertex on each side. Call it unstuck if a nonzero sufficiently small rotation about its center keeps it inside the larger rectangle. The least possible perimeter is √N. Find N.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_14) · MAA AMC.

### Solution

Center the outer rectangle at the origin with sides x=±4,y=±3. The inscribed rectangle has the same center, so write adjacent vertices A=(4,u), B=(v,3), with opposites −A,−B. Equal diagonals give v²−u²=7. A small positive rotation changes A’s x-coordinate initially by −u times the angle and B’s y-coordinate by v times the angle. Thus an allowed rotation in either direction requires uv≤0. Reflecting if necessary, write u=y≥0,v=−x≤0, where x²=y²+7. If p,q are its side lengths, then p²+q²=4|A|²=64+4y² and pq=2 det(A,B)=24+2 xy. Its perimeter squared is 4(p+q)²=448+16y²+16 xy≥448. Equality occurs at y=0,x=√7. This rectangle is unstuck: a small positive rotation moves its right-hand vertex inward to x=4cosθ<4 and its upper vertex downward, while the other coordinates remain strictly inside their bounds. Hence N=448.

**Answer:** 448.

**Methods:** inscribed rectangles, rotation feasibility, perimeter optimization, coordinate geometry.

**Verification:** At equality p²+q²=64 and pq=24, so the perimeter squared is 4(64+48)=448; an explicit small rotation preserves containment.

**Source comparison:** Both alternatives read. The first gives a geometric deformation argument; the second asserts a minimum-diagonal principle without proving it. The coordinate sign condition and exact squared-perimeter identity establish a global bound and verify that equality is genuinely unstuck.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The unstuck rotation condition restricts contact-point signs, yielding a sharp perimeter bound.

## 1994 AIME Problem 2: A square between internally tangent circles

A circle of diameter PQ=10 is internally tangent at P to a circle of radius 20. A square ABCD has A,B on the larger circle, while CD is tangent to the smaller circle at Q and the smaller circle lies outside the square. If AB=m+√n, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_2) · MAA AMC.

### Solution

Put the large-circle center at (0,0), P=(0,20), and Q=(0,10). The line CD is y=10, and the square extends away from the small circle, downward. If its side is s, then AB is a horizontal chord at height 10−s, with endpoints (±s/2,10−s). The circle equation gives s²/4+(10−s)²=400, or s²−16s−240=0. Its only positive root is s=8+√304, so m+n=312.

**Answer:** 312.

**Methods:** circle chords, tangent square, quadratic equations.

**Verification:** The negative quadratic root is impossible for a side length, and the positive root places both chord endpoints exactly on the radius-20 circle.

**Source comparison:** The sole alternative correctly uses the half-chord and center offset. The coordinate restatement of the configuration explains the orientation imposed by the smaller circle being outside the square.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A centered square chord and the circle radius give a quadratic for the square side.

## 1994 AIME Problem 3: A triangular particular solution

A real function satisfies f(x)+f(x−1)=x² for every real x, and f(19)=94. Find the remainder when f(94) is divided by 1000.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_3) · MAA AMC.

### Solution

For integer n let g(n)=f(n)−n(n+1)/2. Since n(n+1)/2+(n−1)n/2=n², the functional equation gives g(n)=−g(n−1). Now g(19)=94−190=−96. The difference 94−19=75 is odd, so g(94)=96. Thus f(94)=94·95/2+96=4561, with remainder 561.

**Answer:** 561.

**Methods:** particular solutions, alternating recurrences, triangular numbers.

**Verification:** Successive normalized values alternate sign, and 4465+96=4561.

**Source comparison:** Both alternatives correctly evaluate the recurrence. The triangular-number normalization replaces a long alternating square sum and applies only on the integer orbit needed by the problem.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Subtracting a triangular-number particular solution leaves an alternating recurrence.

## 1994 AIME Problem 4: A sum of binary logarithm floors

Find the positive integer n satisfying Σₖ₌₁ⁿ floor(log₂k)=1994.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_4) · MAA AMC.

### Solution

For 2ʲ≤k<2ʲ⁺¹ the summand is j. Thus the sum through 255 is Σʲ₌₀⁷j2ʲ=1538, and through 511 it is 1538+8·256=3586. Hence 256≤n≤511. Every new term in that range equals 8, so 1538+8(n−255)=1994, giving n=312. The sum strictly increases for n≥2, proving uniqueness.

**Answer:** 312.

**Methods:** floor sums, dyadic intervals, arithmetico-geometric sums.

**Verification:** 1538+8·57=1994, with n=255+57=312. Independent exact check passed: Compute each logarithm floor independently by integer bit length.

**Source comparison:** The single alternative correctly groups integers between successive powers of two. Its endpoint counts and resulting linear equation are valid.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Binary magnitude intervals give a piecewise linear formula for a logarithm-floor sum.

## 1994 AIME Problem 8: An equilateral triangle from two heights

The points (0,0),(a,11),(b,37) form an equilateral triangle. Find ab.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_8) · MAA AMC.

### Solution

One vector from the origin is obtained from the other by a rotation of ±60°. For the +60° orientation, b=a/2−11√3/2 and 37=√3a/2+11/2. Thus a=21√3 and b=5√3, giving ab=315. The −60° orientation is the reflection of this configuration across the y-axis, changing both signs and preserving the product.

**Answer:** 315.

**Methods:** equilateral triangles, rotation matrices, orientation.

**Verification:** For a=21√3,b=5√3, all three squared side lengths equal 1444; changing both signs preserves them.

**Source comparison:** All four alternatives read. Index 1 switches perpendicular-vector signs inconsistently; index 2 misprints the final value of a; index 3 has a malformed initial equality and chooses positive roots without discussing reflection. The two rotation orientations exhaust the possibilities.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A 60-degree rotation relates the coordinates of an equilateral triangle.

## 1994 AIME Problem 13: Reciprocal roots on a translated unit circle

The ten roots of x¹⁰+(13x−1)¹⁰=0 form five conjugate pairs rⱼ,conj(rⱼ). Find Σⱼ₌₁⁵1/(rⱼconj(rⱼ)).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_13) · MAA AMC.

### Solution

No root is zero. Set t=1/x; then (13−t)¹⁰=−1, so t=13−ω as ω runs through the ten roots of ω¹⁰+1=0. Each has |ω|=1, hence |t|²=170−13(ω+conj(ω)). Their sum is zero by Vieta, as is the conjugate sum, so the sum of |t|² over all ten roots is 1700. Conjugate roots have equal squared modulus and there are no real roots; the requested sum takes one from each pair and equals 850.

**Answer:** 850.

**Methods:** reciprocal polynomials, roots of unity, conjugate pairs, Vieta sums.

**Verification:** For real x, the two tenth powers cannot both vanish, so no real roots disrupt the five-pair count.

**Source comparison:** Both alternatives correctly transform reciprocal roots to a translated unit circle. Summing all ten squared moduli and halving makes the conjugate-pair accounting explicit.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Reciprocal roots lie on a translated unit circle, and their squared moduli sum by Vieta.

## 1995 AIME Problem 1: Five shrinking squares with quarter overlaps

Start with a unit square. Each successive square has half the previous side length and is centered at its outward corner, with parallel sides; at every stage use the corner away from the earlier squares. For the first five squares, write their union area as m/n in lowest terms. Find m−n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_1) · MAA AMC.

### Solution

Each new square overlaps the preceding one in a quarter of its own area. It does not overlap an earlier square: along either coordinate direction, the nearest edge of the square two stages later already lies beyond the earlier square’s outer edge. Thus the union area is 1+(3/4)(1/4+1/16+1/64+1/256)=1+255/1024=1279/1024. The numerator is odd and the denominator a power of two, so the fraction is reduced and m−n=255.

**Answer:** 255.

**Methods:** geometric series, overlapping squares, union area.

**Verification:** The successive added areas are 3/16,3/64,3/256,3/1024, totaling 255/1024.

**Source comparison:** The single alternative correctly subtracts adjacent overlaps but leaves the absence of nonadjacent overlaps implicit. The outward-corner construction in the restatement expresses the original perpendicular-bisector conditions without a figure.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Successively halved squares overlap in quarter-squares, giving a telescoping area sum.

## 1995 AIME Problem 2: A product of roots without solving them

Find the last three decimal digits of the product of all positive roots of √1995·x^(log₁₉₉₅x)=x².

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_2) · MAA AMC.

### Solution

Set u=log₁₉₉₅x, a bijection from positive x to real u. The equation becomes u²+1/2=2u. Its two distinct real roots have sum 2, so the corresponding x-values have product 1995^(u₁+u₂)=1995². Modulo 1000 this is (−5)²=25, giving final digits 025.

**Answer:** 025.

**Methods:** logarithmic substitution, Vieta formulas, root products, modular arithmetic.

**Verification:** The transformed discriminant is positive, and the logarithmic substitution preserves exactly all positive solutions.

**Source comparison:** All three alternatives read. Index 1 takes logarithms to base x without first excluding x=1, which indeed is not a solution. Index 2 makes an arithmetic error when simplifying the quadratic roots; their sum remains correct. Vieta avoids unnecessary radicals.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. A logarithmic substitution makes the positive roots exponential images of a quadratic’s roots.

## 1995 AIME Problem 5: A quartic coefficient from conjugate data

A monic quartic with real coefficients has four nonreal roots. The product of two roots is 13+i, and the sum of the other two is 3+4i. Find the coefficient of x².

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_5) · MAA AMC.

### Solution

Let the first pair be u,v. Their product is nonreal, so they are not a conjugate pair; the remaining roots must be conj(u),conj(v). Thus u+v=3−4i and conj(u)conj(v)=13−i. The sum of all six pairwise products, which is the x² coefficient, equals uv+conj(u)conj(v)+(u+v)(conj(u)+conj(v))=26+|3−4i|²=51.

**Answer:** 051.

**Methods:** conjugate roots, Vieta formulas, symmetric products.

**Verification:** The grouped products are 13+i,13−i, and 25, summing to 51.

**Source comparison:** Both alternatives read. Index 0 initially refers to an unestablished nonreal sum when the given nonreal product is the reason the pair cannot be conjugate. The grouped Vieta expression avoids introducing four real components.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Conjugate root pairs and Vieta’s formulas determine a quartic coefficient.

## 1995 AIME Problem 7: A symmetric sine-cosine expression

Given (1+sin t)(1+cos t)=5/4 and (1−sin t)(1−cos t)=m/n−√k, where k,m,n are positive integers and m/n is reduced, find k+m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_7) · MAA AMC.

### Solution

Put s=sin t+cos t. Then sin t cos t=(s²−1)/2, so the given equation becomes (s+1)²/2=5/4. Since |s|≤√2, the root s=−1−√(5/2) is impossible, leaving s=−1+√(5/2). The requested expression differs from the given one by −2s, hence equals 5/4−2s=13/4−√10. Therefore k+m+n=10+13+4=27.

**Answer:** 027.

**Methods:** symmetric trigonometric expressions, branch selection, quadratic substitution.

**Verification:** The retained sum lies in [−√2,√2], and 13/4−√10 is positive as the product of two nonnegative factors requires.

**Source comparison:** All three alternatives read. Index 1 incorrectly takes sin t cos t as a positive square root; the actual product is negative, and its later squaring hides the sign mistake. Index 2 omits the justification for rejecting the other quadratic branch.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The symmetric sine-cosine sum satisfies a quadratic whose admissible branch fixes the target.

## 1995 AIME Problem 9: An isosceles triangle with a tripled angle

In isosceles triangle ABC, AB=AC and altitude AM=11. A point D on AM satisfies AD=10 and ∠BDC=3∠BAC. If the triangle’s perimeter is a+√b, find a+b.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_9) · MAA AMC.

### Solution

Let θ=∠CAM. Symmetry gives ∠CDM=3θ, and DM=1. Thus tan 3θ/tanθ=(CM/1)/(CM/11)=11. Since 0<3θ<90°, all tangents and denominators are valid. Writing u=tanθ>0, the triple-angle identity gives (3−u²)/(1−3u²)=11, so u²=1/4. Therefore CM=11/2 and AC=11√5/2. The perimeter is 2 CM+2 AC=11+√605, yielding a+b=616.

**Answer:** 616.

**Methods:** angle multiplication, isosceles symmetry, tangent triple angle.

**Verification:** For u=1/2, tan 3θ=(3u−u³)/(1−3u²)=11/2, exactly the required CM/DM.

**Source comparison:** All five alternatives read. The tangent identity is shortest, while complex arguments require quadrant verification. The geometric angle bound 3θ<90° prevents spurious branches introduced by tangent periodicity. The longer synthetic construction reaches the same lengths.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. An altitude and a tripled apex angle lead to a tangent triple-angle equation.

## 1995 AIME Problem 13: Grouping a sum by rounded fourth roots

Let f(n) be the integer nearest to the positive fourth root of n. Find Σₖ₌₁¹⁹⁹⁵1/f(k).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_13) · MAA AMC.

### Solution

For a positive integer j, f(n)=j exactly when (j−1/2)⁴<n<(j+1/2)⁴. The endpoints are never integers; both have fractional part 1/16, so the number of integer n in a complete interval is their difference, 4j³+j. For j=1,…,6 these intervals contain 4(1³+⋯+6³)+(1+⋯+6)=4·441+21=1785 integers and contribute Σ(4j²+1)=4·91+6=370. The remaining 210 integers through 1995 have f(n)=7, contributing 210/7=30. The total is 400.

**Answer:** 400.

**Methods:** rounding intervals, floor endpoints, power sums.

**Verification:** 6.5⁴=1785+1/16 and 7.5⁴=3164+1/16, so exactly the integers 1786 through 1995 form the final partial group. Independent exact check passed: Find each nearest fourth root by exact integer midpoint comparisons, then sum individually.

**Source comparison:** Both alternatives read. Index 0 counts integers by flooring an interval length, which is not valid in general; it works here because both endpoints have the same fractional part 1/16. That endpoint fact is made explicit. Index 1 gives only an abbreviated numerical grouping.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Rounding fourth roots groups a reciprocal sum into polynomially sized intervals.

## 1996 AIME Problem 1: The center of a three-by-three magic square

A 3×3 magic square has first row (x,19,96) and second-row first entry 1. Every row, column, and main diagonal has the same sum. Find x.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_1) · MAA AMC.

### Solution

Let the common sum be S and the center be c. Adding the four lines through the center counts every outer entry once and the center four times, so 4S=3S+3c and S=3c. Equality of the first row and first column makes the bottom-left entry 19+96−1=114. The diagonal through 96 and 114 then gives 96+c+114=3c, so c=105 and S=315. Hence x=315−19−96=200.

**Answer:** 200.

**Methods:** magic squares, linear invariants, double counting identities.

**Verification:** A completed square is [[200,19,96],[1,105,209],[114,191,10]], with every required line summing to 315.

**Source comparison:** All three alternatives read. The first gives valid elimination; the third cites unexplained averaging formulas. The center identity proves the useful invariant directly and reconstructs the missing figure’s given entries from the archived tables.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Equal row, column, and diagonal sums determine the missing magic-square entry by linear relations.

## 1996 AIME Problem 3: Counting monomials after expansion

Find the least positive n for which (xy−3x+7y−21)^n has at least 1996 nonzero monomials after collecting terms.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_3) · MAA AMC.

### Solution

Factor the expression as $(x+7)^n(y-3)^n$. For each pair $0\le i,j\le n$, the monomial $x^iy^j$ has coefficient $\binom ni7^{n-i}\binom nj(-3)^{n-j}\ne0$. Different exponent pairs are distinct monomials, so exactly $(n+1)^2$ terms survive. Since $44^2=1936<1996\le45^2=2025$, the minimum is $n=44$.

**Answer:** 044.

**Methods:** Cartesian product, polynomial support.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 2 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Factoring the bivariate polynomial reveals an independent rectangular array of nonzero monomials.

## 1996 AIME Problem 5: A polynomial evaluated at its root sum

The roots of x³+3x²+4x−11 are a,b,c. A monic cubic with roots a+b,b+c,c+a has constant term t. Find t.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_5) · MAA AMC.

### Solution

Let $P(x)=x^3+3x^2+4x-11$. Vieta gives $a+b+c=-3$, so

$$(a+b)(b+c)(c+a)=(-3-c)(-3-a)(-3-b)=P(-3).$$

The new cubic's constant term is the negative of this product. Thus $t=-P(-3)=-(-27+27-12-11)=23$.

**Answer:** 023.

**Methods:** Vieta formulas, root transformations, polynomial evaluation.

**Verification:** Equivalently, t=abc−(a+b+c)(ab+bc+ca)=11−(−3)·4=23.

**Source comparison:** All three alternatives read. Direct evaluation at the total root sum is shortest; the symmetric identity and translated-polynomial approaches provide valid checks.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Pairwise root sums are complements of the total root sum, allowing direct polynomial evaluation.

## 1996 AIME Problem 10: An integer angle from a tangent identity

Find the smallest positive integer x satisfying tan(19x°)=(cos 96°+sin 96°)/(cos 96°−sin 96°).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Dividing numerator and denominator by cos 96° and using tangent addition transforms the right side into tan(96°+45°)=tan 141°. Therefore 19x≡141 modulo 180. Since 19²=361≡1 modulo 180, multiplication by 19 gives x≡2679≡159 modulo 180. The least positive solution is 159.

**Answer:** 159.

**Methods:** tangent addition, modular inverses, integer angles.

**Verification:** 19·159=3021=141+16·180, and none of these angles is a tangent pole.

**Source comparison:** All three alternatives read. The first two correctly reduce to a congruence. Index 2 changes subtraction to addition in a cosine-addition line; the intended identity is clear but the displayed signs are wrong.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. A tangent addition identity becomes a linear congruence in an integer angle.

## 1996 AIME Problem 11: Upper-half-plane roots of a reciprocal polynomial

Let P be the product of the roots of z⁶+z⁴+z³+z²+1=0 with positive imaginary part. Write P=r(cosθ°+i sinθ°), r>0 and 0≤θ<360. Find θ.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_11) · MAA AMC.

### Solution

The polynomial factors as (z²−z+1)(z⁴+z³+z²+z+1). The second factor has the nontrivial fifth roots of unity, while the first has roots e^(±iπ/3). The roots with positive imaginary part therefore have arguments 60°,72°,144°. Each has modulus 1, so their product has argument 60°+72°+144°=276°.

**Answer:** 276.

**Methods:** cyclotomic factorization, complex arguments, reciprocal polynomials.

**Verification:** Multiplying the two displayed factors reproduces the polynomial, and the six listed unit roots are distinct.

**Source comparison:** All six alternatives read. Index 2 misprints 288° as 292°. Index 3 forms an incorrect geometric sum and treats a product equal to 1 as a union of zero sets, so that argument is invalid. Index 5 clears denominators and must separately check excluded roots; the direct factorization avoids these complications.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A reciprocal polynomial factors into cyclotomic pieces whose upper-half-plane arguments add.

## 1996 AIME Problem 15: A parallelogram determined by doubled angles

Diagonals of parallelogram ABCD meet at O. Both ∠CAB and ∠DBC equal twice ∠DBA. If ∠ACB=r∠AOB, find floor(1000r).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_15) · MAA AMC.

### Solution

Let θ=∠DBA. Then ∠CAB=∠DBC=2θ, ∠ACB=180°−5θ, and ∠AOB=180°−3θ, with 0<θ<36°. Since AO=CO, the sine law in ABO and CBO gives sin²2θ=sinθ sin 5θ. Put u=cos 2θ. Product-to-sum and the double/triple-angle formulas transform this equation into (u−1)(4u²−3)=0. The angle bound gives 0<u<1, so u=√3/2 and θ=15°. Therefore r=105/135=7/9 and floor(1000r)=777.

**Answer:** 777.

**Methods:** parallelogram diagonals, sine law, trigonometric factorization, angle bounds.

**Verification:** At θ=15°, sin²30°=sin 15°sin 75°=1/4, and the two requested angles are 105° and 135°.

**Source comparison:** All three alternatives read. Index 0 gives a valid factorization with a geometric branch choice. Index 1 miswrites the second quadratic root’s sign, and index 2 contains inconsistent angle labels. The explicit range 0<θ<36° selects the unique admissible root.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Parallelogram midpoint geometry yields a factored trigonometric equation for the angles.

## 1997 AIME Problem 3: Concatenation mistaken for multiplication

A two-digit integer x written immediately before a three-digit integer y forms a five-digit number equal to nine times xy. Find x+y.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_3) · MAA AMC.

### Solution

The concatenation condition is 1000x+y=9 xy, so y=1000/(9−1/x). Because 10≤x≤99, we have 111<1000/9<y≤10000/89<113. Thus the integer y must be 112. Substitution gives 1000x+112=1008x, hence x=14 and x+y=126.

**Answer:** 126.

**Methods:** digit concatenation, rational bounds, integer uniqueness.

**Verification:** The concatenation 14112 equals 9·14·112. Independent exact check passed: Exhaust all two-digit and three-digit factor pairs.

**Source comparison:** All three alternatives read. Index 0 finds a successful divisor but does not exhaust the possible divisors; index 1 says the ratio is “a little” below nine without explicit bounds. The two-digit range forces y uniquely by a narrow interval.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. A concatenation equation and the two-digit bound force the three-digit factor.

## 1997 AIME Problem 7: The midpoint time of a storm crossing

A car moves east at 2/3 mile per minute. A circular storm of radius 51 moves southeast at √2/2 mile per minute, initially centered 110 miles north of the car. If the car enters at t₁ and leaves at t₂, find (t₁+t₂)/2.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_7) · MAA AMC.

### Solution

Relative to the storm center, the car is at (t/6,t/2−110). Its squared distance is (5/18)t²−110t+12100. Entry and exit occur when this equals 51², so the two times are the roots of a quadratic with leading coefficient 5/18 and linear coefficient −110. Their average is 110/(2·5/18)=198.

**Answer:** 198.

**Methods:** relative motion, quadratic symmetry, Vieta formulas.

**Verification:** At t=198 the squared distance is 1210<2601, so two crossings do occur; their positive sum is 396 and positive product ensures both are after time zero.

**Source comparison:** All three alternatives read. Index 0 calls the quadratic vertex a maximum, although it is a minimum. Both the quadratic and relative-velocity projection methods correctly give the midpoint time without solving the individual entry and exit times.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Relative motion makes the average entry and exit time the minimum-distance time.

## 1997 AIME Problem 9: Reducing a golden-ratio power

For positive a, the fractional parts of 1/a and a² are equal, and 2<a²<3. Find a¹²−144/a.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_9) · MAA AMC.

### Solution

The bounds imply 0<1/a<1 and floor(a²)=2, so 1/a=a²−2. Thus a³−2a−1=(a+1)(a²−a−1)=0. Positivity excludes a=−1, leaving a²=a+1 and 1/a=a−1. Squaring a³=2a+1 gives a⁶=8a+5, and squaring again gives a¹²=144a+89. Therefore a¹²−144/a=144a+89−144(a−1)=233.

**Answer:** 233.

**Methods:** fractional parts, polynomial reduction, golden ratio, repeated squaring.

**Verification:** Every power reduction uses only a²=a+1; the positive root (1+√5)/2 satisfies the original interval.

**Source comparison:** All four alternatives read. The Fibonacci reduction and repeated squaring are shorter than radical expansion. Index 0 refers to real radical conjugates as complex conjugates, but its numerical expansion is correct.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Fractional-part restrictions force a quadratic relation that reduces a high power.

## 1997 AIME Problem 11: A reflected index in trigonometric sums

Let x=(Σₙ₌₁⁴⁴cos n°)/(Σₙ₌₁⁴⁴sin n°). Find floor(100x).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_11) · MAA AMC.

### Solution

Write the numerator and denominator as C and S. Replacing n by 45−n permutes the index set, so C=Σcos(45°−n°)=(C+S)/√2. Hence S=(√2−1)C and x=C/S=1+√2. Since 1.41²<2<1.42², we have 241<100x<242, giving floor(100x)=241.

**Answer:** 241.

**Methods:** trigonometric sums, index symmetry, angle addition.

**Verification:** All terms of C and S are positive, so every division is valid; the squared rational bounds prove the floor exactly.

**Source comparison:** All seven alternatives read. Index 3 replaces a finite cotangent by infinity without an error bound and therefore does not justify the exact value or floor. Index 0 has a stray multiplication by √2 in simplification. The index-reflection identity is exact and avoids approximation.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Reflecting the angle index in a trigonometric sum gives a linear relation between the sums.

## 1997 AIME Problem 12: The missing value of a fractional-linear involution

Let f(x)=(ax+b)/(cx+d), where a,b,c,d are nonzero real numbers. Suppose f(19)=19, f(97)=97, and f(f(x))=x on its domain. Find the unique real number outside its range.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Since 0 lies in the domain, f(f(0))=0. Its numerator is b(a+d), so b≠0 forces d=−a. The fixed-point equation is then cx²−2 ax−b=0, with distinct roots 19 and 97. Vieta gives 2a/c=116, hence a/c=58. The determinant ad−bc is nonzero because f takes two distinct values. Solving y=(ax+b)/(cx+d) for x shows that every y≠a/c occurs and y=a/c cannot occur. Therefore the unique omitted value is 58.

**Answer:** 058.

**Methods:** fractional-linear maps, involutions, fixed points, range.

**Verification:** An equivalent function is f(x)=58+1521/(x−58), which fixes 19 and 97, is self-inverse, and omits exactly 58.

**Source comparison:** All ten alternatives read. Several contain incorrect decompositions of the rational function; index 6 misstates its inverse, index 7 is only an unsupported averaging guess, and index 8 has the wrong constant-term sign in the fixed-point polynomial. The f(0) argument and Vieta give a complete proof with the nonconstant condition checked.

**Archived entries inspected:** 10 of 10. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A nonconstant fractional-linear involution has opposite diagonal coefficients and symmetric fixed points.

## 1997 AIME Problem 13: A wire graph made of unit diagonals

Let f(t)=abs(abs(abs(t)−2)−1). The planar set S is defined by f(x)+f(y)=1. Its total length is a√b with b squarefree. Find a+b.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_13) · MAA AMC.

### Solution

The equation forces |x|,|y|≤4. On each of the eight unit intervals between consecutive integers from −4 to 4, f is affine with slope ±1 and maps that interval onto [0,1]. Consequently, in each of the 64 unit squares of [−4,4]², the equation f(x)+f(y)=1 is exactly one diagonal of length √2. Different cell segments meet only at endpoints, so the total wire length is 64√2 and a+b=66.

**Answer:** 066.

**Methods:** absolute-value graphs, piecewise linear functions, grid decomposition.

**Verification:** The values of f at integers −4,…,4 alternate 1,0,1,0,1,0,1,0,1, so every unit cell contains one full diagonal.

**Source comparison:** All four alternatives read. Index 1 uses incorrect piecewise formulas outside their valid intervals. Indices 2 and 3 assert that each absolute value always multiplies total length by a fixed factor, which is false without domain and overlap checks. The unit-cell argument verifies exactly where every segment lies.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A piecewise-linear absolute-value function makes one diagonal segment in every unit grid cell.

## 1997 AIME Problem 14: A short arc probability

Two distinct 1997th roots of unity are chosen uniformly. Find numerator plus denominator for the chance that $|v+w|\ge\sqrt{2+\sqrt3}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_14) · MAA AMC.

### Solution

If $\theta$ is their shorter angular separation, then $|v+w|^2=2+2\cos\theta$. The condition is $\cos\theta\ge\sqrt3/2$, or $\theta\le30^\circ$. Fixing $v$, the circular step distance can be any of $1,\ldots,\lfloor1997/12\rfloor=166$ in either direction. Thus 332 of the 1996 possible values of $w$ qualify. The probability is $83/499$, giving $582$.

**Answer:** 582.

**Methods:** cyclic symmetry, geometric probability.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 4 archived solution entries. Valid sources use rotation invariance and the cosine of the angular separation; one geometric derivation has incorrect equations.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry, algebra. Angular differences between roots of unity count pairs satisfying a vector-sum bound.

## 1997 AIME Problem 15: A rigorous maximum equilateral triangle in a rectangle

An equilateral triangle lies entirely inside a 10 by 11 rectangle. Its largest possible area is p√q−r, where q is squarefree. Find p+q+r.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_15) · MAA AMC.

### Solution

Any triangle has a vertex attaining two adjacent extrema of its axis-aligned bounding box, because four extrema are attained by three vertices. Reflect the picture so this vertex is both leftmost and lowest. For an equilateral triangle of side s, its two outgoing sides then make angles θ and θ+60° with the horizontal, with 0≤θ≤30°. Its bounding-box width and height are s cosθ and s sin(θ+60°). Thus s≤min(11/cosθ,10/sin(θ+60°)). The first bound increases and the second decreases on this interval, so their minimum is maximized at their unique intersection. There s cosθ=11 and s sin(θ+60°)=10, giving s sinθ=20−11√3. Hence s²=11²+(20−11√3)²=884−440√3. This bounding box fits exactly, so the bound is attained. The area is s²√3/4=221√3−330, yielding p+q+r=554.

**Answer:** 554.

**Methods:** bounding boxes, orientation optimization, equilateral triangles, attainment.

**Verification:** The intersection satisfies tanθ=(20−11√3)/11, which lies between 0 and tan 30°, so the maximizing orientation is admissible.

**Source comparison:** All three alternatives assume, without proof, that an optimal triangle has a vertex at a rectangle corner and its other vertices on the opposite sides. Their subsequent computations are correct. The bounding-box argument proves the global optimization over all translations and orientations.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Orientation-dependent bounding-box widths give a rigorous maximum for an inscribed equilateral triangle.

## 1998 AIME Problem 3: Factoring a graph into four half-lines

The graph y²+2 xy+40|x|=400 encloses one bounded region. Find its area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_3) · MAA AMC.

### Solution

For x≥0 the equation factors as (y+20)(y+2x−20)=0. For x≤0 it factors as (y−20)(y+2x+20)=0. The bounded region therefore has vertices (0,20),(20,−20),(0,−20),(−20,20). Its horizontal top and bottom edges each have length 20 and are 40 apart. Thus its area is 20·40=800.

**Answer:** 800.

**Methods:** absolute values, factored curves, parallelogram area.

**Verification:** Each stated vertex satisfies the original equation, and the bounded edges lie in the appropriate half-planes.

**Source comparison:** Both alternatives correctly factor the graph. The half-plane restrictions must be retained; treating all four factors as full lines would describe extra regions.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Factoring the absolute-value equation on two half-planes reveals a bounded parallelogram.

## 1998 AIME Problem 5: A four-term cycle of signed triangular numbers

For positive k let Aₖ=k(k−1)cos(k(k−1)π/2)/2. Find |A₁₉+A₂₀+⋯+A₉₈|.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_5) · MAA AMC.

### Solution

The cosine is (−1)^(k(k−1)/2), so its signs repeat +,+,−,− for k≡0,1,2,3 modulo 4. In each block beginning at k=4j+3, the four signed triangular numbers are −Tₖ₋₁,+Tₖ,+Tₖ₊₁,−Tₖ₊₂, where Tᵣ=r(r+1)/2. Their sum is k−(k+2)=−2. The eighty terms from 19 through 98 form twenty such blocks, giving sum −40 and absolute value 40.

**Answer:** 040.

**Methods:** triangular-number parity, periodic signs, telescoping.

**Verification:** The first block is −171+190+210−231=−2, and the same difference identity applies to all twenty blocks.

**Source comparison:** The sole alternative correctly pairs consecutive triangular differences and then pairs those results. Its displayed absolute-value expression temporarily omits outer bars, but the final sign treatment is correct.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Triangular-number parity gives a four-term sign cycle and telescoping cancellation.

## 1998 AIME Problem 8: The longest subtractive recurrence

A sequence begins 1000,x and each later term is the term two places earlier minus the preceding term. Stop when the first negative term appears, including it. Which positive integer x makes the sequence longest?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_8) · MAA AMC.

### Solution

Repeated substitution gives the tenth and eleventh terms as 34x−21000 and 34000−55x. Any sequence reaching a twelfth term must have both nonnegative, so 21000/34≤x≤34000/55. The only integer in this interval is 618. For x=618 the sequence is 1000,618,382,236,146,90,56,34,22,12,10,2,8,−6, of length 14. Every other positive integer stops by its eleventh term, so 618 is the unique maximizer.

**Answer:** 618.

**Methods:** subtractive recurrences, Fibonacci coefficients, integer intervals, maximal length.

**Verification:** Direct recurrence evaluation gives fourteen terms for 618; the necessary interval for surviving eleven nonnegative terms contains no other integer. Independent exact check passed: Generate every subtractive sequence for1≤x≤1000; x>1000 stops immediately at term3.

**Source comparison:** All three entries read. Entry 0 is an introductory fragment with an incorrect general formula. Entry 1 uses strict inequalities although zero is allowed and misquotes one Fibonacci ratio. Entry 2 relies only on a limiting ratio, which does not prove the finite optimum. Two exact term inequalities plus the full candidate sequence settle maximality.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Consecutive nonnegativity constraints in a Fibonacci-coefficient recurrence isolate the maximizing integer.

## 1998 AIME Problem 12: A golden-ratio configuration in a medial triangle

In equilateral triangle ABC, D,E,F are the midpoints of BC,CA,AB. Points P∈DE,Q∈EF,R∈FD satisfy P∈CQ, Q∈AR, and R∈BP. If [ABC]/[PQR]=a+b√c with c squarefree, find a²+b²+c².

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Affine maps preserve collinearity and area ratios, so use A=(0,0),B=(2,0),C=(0,2), giving D=(1,1),E=(0,1),F=(1,0). Write P=(p,1),Q=(q,1−q),R=(1,r). The three collinearities respectively give p=q/(1+q), q=1/(1+r), and r=1/(2−p). Eliminating p,q yields r²+r−1=0. Since 0≤r≤1, r=(√5−1)/2, q=r, and p=1−r. These values lie in the required segments and satisfy all three equations, proving existence and uniqueness. Triangle DEF has area 1/2; each of the three corner triangles cut off by PQR has area r(1−r)/2. Thus [PQR]=(1−3r(1−r))/2=(7−3√5)/2. Since [ABC]=2, their ratio is 4/(7−3√5)=7+3√5. The answer is 7²+3²+5²=83.

**Answer:** 083.

**Methods:** affine normalization, cyclic collinearity, golden ratio, area ratios.

**Verification:** With r²=1−r, the parameters satisfy all three collinearities and lie strictly between 0 and 1; the reciprocal area ratio rationalizes exactly to 7+3√5.

**Source comparison:** Both alternatives read. Both assume equal cyclic segment ratios without proving them. Index 0 uses a similarity involving the wrong vertex and obtains the complementary segment value; the symmetric area expression hides this error. Index 1 contains multiple sign errors in its polynomial substitutions. The three affine collinearity equations prove the unique configuration and show the area ratio holds for every nondegenerate triangle.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Cyclic collinearity constraints determine a unique medial-triangle configuration and its affine area ratio.

## 1998 AIME Problem 13: Complex weights over subsets

For each nonempty subset of {1,…,n}, list its elements increasingly and weight the jth by i^j. Let S_n sum these weighted subset sums. Given S_8=−176−64i and S_9=p+qi, find |p|+|q|.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_13) · MAA AMC.

### Solution

Pair each subset $U$ of $\{1,\ldots,8\}$, including the empty set, with $U\cup\{9\}$. Old terms contribute twice $S_8$. If $U$ has $k$ elements, the new term is $9i^{k+1}$, so the total extra contribution is $9i\sum_{k=0}^8\binom8k i^k=9i(1+i)^8=144i$. Consequently $S_9=2(-176-64i)+144i=-352+16i$, giving $368$.

**Answer:** 368.

**Methods:** weighted subsets, binomial theorem.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Subset insertion yields a recurrence for ranked complex power sums.

## 1998 AIME Problem 14: A sharp bound for a box volume ratio

Positive integers m≤n≤p satisfy 2 mnp=(m+2)(n+2)(p+2). Find the largest possible p.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_14) · MAA AMC.

### Solution

The equation implies 2=(1+2/m)(1+2/n)(1+2/p)>1+2/m, so m≥3. Put a=m−2,b=n−2, positive integers. Solving for p gives p=2(a+4)(b+4)/(ab−8), with ab−8 a positive integer. Since (a−1)(b−1)≥0, we have a+b≤ab+1. Therefore p=(2 ab+8(a+b)+32)/(ab−8)≤10+120/(ab−8)≤130. Equality is achieved by a=1,b=9, giving (m,n,p)=(3,11,130). Thus the maximum is 130.

**Answer:** 130.

**Methods:** integer optimization, volume ratios, product-sum bound, attainment.

**Verification:** 2·3·11·130=8580=(3+2)(11+2)(130+2), and the dimensions are in the required order. Independent exact check passed: Enumerate ordered integral dimension pairs within the analytic bound and solve exactly for the third.

**Source comparison:** Both alternatives read. Index 0 eventually supplies the necessary global inequality after an exploratory denominator guess. Index 1 fixes m=3 without proving global optimality. The positive integer denominator and sharp product-sum bound establish the maximum uniformly.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. An integer volume ratio is bounded by a factored denominator and a sharp product-sum inequality.

## 1999 AIME Problem 3: A quadratic square condition with four solutions

Find the sum of all positive integers n for which n²−19n+99 is a perfect square.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_3) · MAA AMC.

### Solution

Write n²−19n+99=k² with k≥0. Completing the square gives (2k−(2n−19))(2k+(2n−19))=35. Since 4k²=(2n−19)²+35, both factors are positive. The ordered factor pairs are (1,35),(5,7),(7,5),(35,1), giving n=18,10,9,1 respectively. All four are positive and satisfy the equation, so their sum is 38.

**Answer:** 038.

**Methods:** perfect-square conditions, difference of squares, factor pairs.

**Verification:** The corresponding squares are 81,9,9,81 for n=1,9,10,18. Independent exact check passed: Direct square test through100; factorization proves no later solutions.

**Source comparison:** All three alternatives are valid. The factorization method exhausts the possibilities without checking an interval of individual integers.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Completing the square converts a quadratic perfect-square condition into factor pairs of 35.

## 1999 AIME Problem 6: Square roots turn a quadrilateral into an annular sector

Apply (x,y)↦(√x,√y) to the region enclosed by (900,300),(1800,600),(600,1800),(300,900). If its image has area k, find floor(k).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_6) · MAA AMC.

### Solution

The original region is bounded by y=x/3, y=3x, and x+y=1200,2400. In image coordinates (u,v), these become v=u/√3, v=√3u, and u²+v²=1200,2400. Thus the image is an annular sector between angles 30° and 60°. Its area is (30/360)π(2400−1200)=100π, whose floor is 314.

**Answer:** 314.

**Methods:** nonlinear coordinate maps, annular sectors, region transformations.

**Verification:** The square-root map is a bijection on the positive quadrant, and 314<100π<315.

**Source comparison:** The sole alternative correctly transforms the entire boundary rather than treating the image as the straight-edged quadrilateral joining the transformed vertices.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Coordinate square roots map the quadrilateral into an annular sector.

## 1999 AIME Problem 9: An equidistant complex multiplier

For positive real a,b, the map f(z)=(a+bi)z sends every complex z to a point equidistant from z and 0. Given |a+bi|=8 and b²=m/n in lowest terms, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_9) · MAA AMC.

### Solution

Apply the condition to z=1. It gives |a+bi−1|=|a+bi|, so (a−1)²+b²=a²+b² and a=1/2. The modulus condition then yields b²=64−1/4=255/4. Therefore m+n=259. Conversely, |a+bi−1|=|a+bi| implies the required equality for every z after multiplying both sides by |z|.

**Answer:** 259.

**Methods:** complex similarity, perpendicular bisectors, modulus identities.

**Verification:** The two multiplier moduli |1/2+bi| and |−1/2+bi| are equal for every real b, verifying the global condition.

**Source comparison:** All six alternatives read. Index 3 mislabels a hypotenuse factor and attributes the first-quadrant condition to z rather than the multiplier. Index 4 misexpands the imaginary coordinate. Testing z=1 is sufficient and avoids divisions by arbitrary coordinates or by z=0.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equidistance under complex multiplication forces the multiplier’s real part to be one half.

## 1999 AIME Problem 11: A telescoping arithmetic-angle sine sum

Angles are in degrees. Given Σₖ₌₁³⁵sin(5k°)=tan((m/n)°), where m,n are coprime positive integers and m/n<90, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_11) · MAA AMC.

### Solution

Let S be the sum. The product-to-sum identity gives 2sin5°·S=Σₖ₌₁³⁵(cos(5k−5)°−cos(5k+5)°). Cancellation leaves cos 0°+cos 5°−cos 175°−cos 180°=2(1+cos 5°). Therefore S=(1+cos 5°)/sin 5°=cot 2.5°=tan 87.5°. Tangent is injective on (0°,90°), so m/n=175/2 and m+n=177.

**Answer:** 177.

**Methods:** telescoping trigonometric sums, product-to-sum, half-angle identities.

**Verification:** Only the first two and last two cosine terms survive the telescoping sum; 175/2 lies in the required interval and is reduced.

**Source comparison:** All three alternatives read. Index 1 uses degree angles in exponential notation without conversion and an off-by-one geometric-series expression; its imaginary part happens to remain correct. Index 2 uses radians consistently. The product-to-sum proof is exact and short.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A product-to-sum identity telescopes an arithmetic-angle sine sum.

## 1999 AIME Problem 12: A triangle from inradius and two tangent lengths

The incircle of triangle ABC has radius 21 and touches AB at P, with AP=23 and PB=27. Find the triangle’s perimeter.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Equal tangent segments from each vertex let the three tangent lengths be 23,27,x, so the semiperimeter is s=50+x. The area is 21s, while Heron gives area squared s·23·27·x. Equating yields 441s²=621 sx. Since s>0, cancel s to get 441(50+x)=621x, hence x=245/2. The perimeter is 2s=100+245=345.

**Answer:** 345.

**Methods:** incircle tangent lengths, Heron formula, area equals inradius times semiperimeter.

**Verification:** The resulting sides are 50,291/2,299/2, satisfying all triangle inequalities; Heron divided by s² gives inradius squared 441.

**Source comparison:** All four entries read, including a diagram-only first entry. The Heron and half-angle approaches are valid. The last entry calls x an unknown side although its equations use the third tangent length; the new notation removes that ambiguity.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Tangent-length variables combine the inradius area formula with Heron’s formula.

## 2000 AIME I Problem 3: Adjacent binomial coefficients

For coprime positive integers $a,b$, the coefficients of $x^2$ and $x^3$ in $(ax+b)^{2000}$ agree. Determine $a+b$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

The ratio of the $x^3$ coefficient to the $x^2$ coefficient is $\frac{1998a}{3b}=\frac{666a}{b}$. Equality forces $b=666a$. Coprimality gives $(a,b)=(1,666)$, hence $667$.

**Answer:** 667.

**Methods:** binomial coefficients.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Equality of adjacent binomial coefficients gives a ratio of the two linear-form coefficients.

## 2000 AIME I Problem 4: Nine-square dissection as a linear system

A rectangle is tiled by nine squares with side lengths $a_1<\cdots<a_9$. Their edge relations are $a_3=a_1+a_2$, $a_4=a_1+a_3$, $a_5=a_3+a_4$, $a_6=a_4+a_5$, $a_7=a_2+a_3+a_5$, $a_8=a_2+a_7$, $a_9=a_1+a_4+a_6$, and $a_6+a_9=a_7+a_8$. Its width is $a_8+a_9$ and height is $a_6+a_9$. If these dimensions are coprime integers, find its perimeter.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Put $a_1=a,a_2=b$. Successive substitution gives $a_3=a+b$, $a_4=2a+b$, $a_5=3a+2b$, $a_6=5a+3b$, $a_7=4a+4b$, $a_8=4a+5b$, $a_9=8a+4b$. The final edge relation is $13a+7b=8a+9b$, so $5a=2b$. Thus the square sides are $t(2,5,7,9,16,25,28,33,36)$, and the rectangle dimensions are $69t,61t$. Because $61$ and $69$ are coprime, integer dimensions force $t$ to be an integer by Bezout; their coprimality then forces $t=1$. The perimeter is $2(69+61)=260$.

**Answer:** 260.

**Methods:** dissections, linear systems, primitive scaling.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three source entries were reviewed. The first two encode equivalent edge systems. The third normalizes a smallest square to 1 and glosses over the subsequent rescaling; the proof here makes primitive scaling explicit. The textual edge relations replace the source diagram.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Shared edges of a square dissection form a homogeneous linear system, followed by primitive integer scaling.

## 2000 AIME I Problem 6: A gap between means

How many integer pairs $(x,y)$ satisfy $0<x<y<10^6$ and $\frac{x+y}{2}-\sqrt{xy}=2$?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

The equation is $(\sqrt y-\sqrt x)^2=4$, hence $\sqrt y=\sqrt x+2$. Squaring gives $4\sqrt x=y-x-4$, so $\sqrt x$ is rational. A rational square root of an integer is an integer: in a reduced fraction its denominator must divide its numerator after squaring. Write $x=a^2,y=(a+2)^2$. The bounds are precisely $1\le a\le997$, giving $997$ pairs.

**Answer:** 997.

**Methods:** radicals, integer squares.

**Verification:** Exhaustive check over the full x range of the derived square condition; exhaustion relies on the analytic reduction.

**Source comparison:** All five entries were reviewed. Several omit the rational-square-root justification. Entry 3 contains a mistaken derived square, and entry 4 has inconsistent factors in its squaring steps. The integer-square parametrization above supplies the missing implication.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. The mean equation forces two integer square roots differing by 2.

## 2000 AIME I Problem 7: A reciprocal cyclic system

Positive reals satisfy $xyz=1$, $x+1/z=5$, and $y+1/x=29$. Express $z+1/y=m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Since $1/z=xy$, the first equation is $x+xy=5$. Multiplying the second by $x$ gives $xy+1=29x$. Subtraction yields $30x=6$, so $x=1/5$, $y=24$, and $z=5/24$. Therefore $z+1/y=1/4$, and the answer is $5$.

**Answer:** 005.

**Methods:** reciprocal systems, substitution.

**Verification:** Exact substitution of all three variables into the original system and target.

**Source comparison:** All six entries were reviewed, including the cyclic-product shortcut. Entry 4 misprints x as 5 instead of 1/5; entry 5 initially writes a wrong sign for the denominator defining z. The stated substitution avoids these slips.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Using the product constraint removes the reciprocal terms and makes two equations linear in x and xy.

## 2000 AIME I Problem 9: Shifted logarithms factor a system

Positive reals satisfy $\log(2000xy)-\log x\log y=4$, $\log(2yz)-\log y\log z=1$, and $\log(zx)-\log z\log x=0$, with base-10 logarithms. Find the sum of all possible values of $y$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Let $a=\log x-1$, $b=\log y-1$, and $c=\log z-1$. The three equations become $ab=\log2$, $bc=\log2$, and $ac=1$. Because $b\ne0$, we have $a=c$; hence $a=c=1$ or $a=c=-1$. Correspondingly $b=\log2$ or $b=-\log2$, so $y=20$ or $y=5$. Both sign choices give positive solutions of the original system. Their sum is $25$.

**Answer:** 025.

**Methods:** logarithmic systems, factorization.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. Entry 1 makes an invalid logarithmic conversion and gives an incorrect intermediate x. Entry 2 needs justification before cancelling 1-log y; the shifted formulation provides it.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Subtracting 1 from each logarithm factors the three nonlinear equations.

## 2000 AIME I Problem 10: A hundred variables and one sum

Reals $x_1,\ldots,x_{100}$ satisfy $x_k=\sum_{j\ne k}x_j-k$ for each $k$. If $x_{50}=m/n$ in lowest terms with $n>0$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

Write $S=\sum_{k=1}^{100}x_k$. Each equation says $2x_k=S-k$. Summing gives $2S=100S-5050$, so $S=2525/49$. Consequently $x_{50}=(S-50)/2=75/98$, and $m+n=173$.

**Answer:** 173.

**Methods:** linear systems, symmetric sums.

**Verification:** Exact substitution of all 100 entries into the original linear system.

**Source comparison:** Both source entries were reviewed. One uses the total sum, the other the arithmetic progression forced by pairwise subtraction; both are valid.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A common total collapses the symmetric linear system to one equation.

## 2000 AIME I Problem 12: Reflection orbits

A real function satisfies $f(x)=f(398-x)=f(2158-x)=f(3214-x)$ for every real $x$. What is the largest number of different values among $f(0),\ldots,f(999)$?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Composing reflections gives periods $1760$ and $1056$, hence period $352$. On residues modulo $352$, the remaining identification is $r\sim46-r$. There are two fixed residues, $23$ and $199$; all other $350$ residues occur in pairs. Thus there are $2+350/2=177$ orbits. Assign a separate value to each orbit (and extend using the same reflection action on the reals); all $177$ values occur in $0,\ldots,999$.

**Answer:** 177.

**Methods:** orbits, invariants.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Functional symmetries identify argument orbits and reduce the independent function values to a finite count.

## 2000 AIME I Problem 13: Fast highways and a slower prairie

Two perpendicular highways cross at the fire station. A truck travels at $50$ miles per hour on either highway and $14$ miles per hour elsewhere. The area it can reach in six minutes is $m/n$ square miles in lowest terms. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

An off-road segment joining highways can be replaced by highway travel through their intersection without increasing time: $(|a|+|b|)/50\le\sqrt{a^2+b^2}/14$. Segments returning to the same highway can likewise be replaced. Thus an optimal route uses one highway and then a straight off-road segment. In the sector $x\ge y\ge0$, for an exit $(s,0)$ the inequality $7(x-s)+24y\le25\sqrt{(x-s)^2+y^2}$ gives travel time at least $(7x+24y)/350$ (also using $|s|\ge s$). Equality occurs at $s=x-7y/24\ge0$. Negative exits are no better than the origin. For a nonnegative exit distance $s$, the squared distance from $(0,s)$ to $(x,y)$ exceeds that from $(s,0)$ by $2s(x-y)\ge0$. Thus the x-axis route is at least as good as any y-axis route. Hence the six-minute boundary is $7x+24y=35$ in this sector, with its reflection in $y=x$ in the other half-quadrant. The first-quadrant region has vertices $(0,0),(5,0),(35/31,35/31),(0,5)$ and area $175/31$. Multiplying by four gives $700/31$, so the answer is $731$.

**Answer:** 731.

**Methods:** geometric optimization, reachable regions, Cauchy inequality.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The single downloaded solution constructs an envelope of circles and its tangent line. Its geometric result is correct. The present proof explicitly reduces routes and explains the minimizing highway exit.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The reachable set is determined by a sharp weighted travel-time inequality, producing a polygonal envelope.

## 2000 AIME II Problem 1: Reciprocal logarithms share a base

Write $\frac2{\log_4(2000^6)}+\frac3{\log_5(2000^6)}=m/n$ in lowest terms. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

Using $1/\log_a b=\log_b a$, the expression is $\log_{2000^6}(4^2 5^3)=\log_{2000^6}2000=1/6$. Thus $m+n=7$.

**Answer:** 007.

**Methods:** change of base, logarithm laws.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries were reviewed. They are valid common-base manipulations, although the fourth needlessly expands a linear equation in logarithms.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Changing the logarithms to a common base turns their weighted sum into the logarithm of 2000.

## 2000 AIME II Problem 7: Half a binomial row

Define $N$ by $\sum_{k=2}^{9}1/(k!(19-k)!)=N/18!$. Find the greatest integer strictly smaller than $N/100$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Multiply by $19!$. Complementation pairs the subsets of sizes $0,\ldots,9$ with those of sizes $19,\ldots,10$, so their binomial sum is $2^{18}$. Consequently $19N=2^{18}-1-19=262124$, hence $N=13796$ and the requested integer is $137$.

**Answer:** 137.

**Methods:** binomial identities, complement.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 2: The common denominator is described as 19 factorial although the displayed reduced numerators correspond to 18 factorial.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. A factorial-denominator sum becomes half a binomial row after pairing symmetric coefficients.

## 2000 AIME II Problem 9: Reciprocal complex powers

If $z\in\mathbb C$ satisfies $z+1/z=2\cos3^\circ$, find the least integer strictly larger than $z^{2000}+z^{-2000}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

The quadratic $z^2-2\cos3^\circ z+1=0$ has roots $z=\cos3^\circ\pm i\sin3^\circ$. Thus $z^{2000}+z^{-2000}=2\cos6000^\circ=2\cos240^\circ=-1$. The least integer strictly greater than this is $0$.

**Answer:** 000.

**Methods:** complex roots, De Moivre theorem.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries were reviewed. Entry 1 does not justify its modulus assertion and misprints an exponent. Entry 2 is invalid: it assumes a different exponent gives the same rounding and asserts false monotonicity under repeated squaring. Entry 3 misprints the imaginary part as a cosine. The quadratic proof avoids these issues.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A reciprocal quadratic places its roots at conjugate unit-circle angles.

## 2000 AIME II Problem 10: Radius from four tangent lengths

A circle inscribed in convex quadrilateral $ABCD$ touches $AB$ at $P$ and $CD$ at $Q$. If $AP=19$, $PB=26$, $CQ=37$, and $QD=23$, find the square of its radius.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Let the four tangent lengths from the vertices be $a,b,c,d=19,26,37,23$, and let the radius be $r$. If $\theta_i$ is the angle at the center between a vertex ray and either adjacent tangency radius, then $\tan\theta_i=a_i/r$ and $\sum\theta_i=\pi$. Consequently the product $(r+ia)(r+ib)(r+ic)(r+id)$ is real. Its imaginary part is $r^3(a+b+c+d)-r(abc+abd+acd+bcd)=0$. Hence $r^2=(abc+abd+acd+bcd)/(a+b+c+d)=67935/105=647$.

**Answer:** 647.

**Methods:** tangential quadrilaterals, half angles, symmetric polynomials.

**Verification:** Independent numerical half-angle closure check for the claimed inradius.

**Source comparison:** All three entries were reviewed. The tangent-addition method and the stated tangential-area formula agree. The proof here derives the needed symmetric identity and avoids divisions by potentially vanishing tangent-addition denominators.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The four half-angle tangent parameters satisfy a symmetric cubic-to-linear radius identity.

## 2000 AIME II Problem 13: A hidden geometric-series factor

The polynomial $2000x^6+100x^5+10x^3+x-2$ has a real root $(m+\sqrt n)/r$, where $m,n,r$ are integers, $r>0$, and $\gcd(m,r)=1$. Find $m+n+r$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Put $t=10x^2$. The polynomial is $2(t^3-1)+x(t^2+t+1)=(2t+x-2)(t^2+t+1)$. For real $x$, the second factor is positive. Thus the real roots satisfy $20x^2+x-2=0$, giving $x=(-1\pm\sqrt{161})/40$. The root with the required plus sign has $(m,n,r)=(-1,161,40)$, and the sum is $200$.

**Answer:** 200.

**Methods:** polynomial factorization, geometric series, positivity.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries were reviewed, including the extended substitutions within entry 0. The direct factorization is sound. Entry 1 has a sign inconsistency in its complex factorization, and its claim that imaginary terms must cancel separately is unjustified for complex z. Entry 2 divides by a potentially zero factor and should check that excluded case separately.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A difference of cubes shares its cofactor with the odd-power terms.

## 2000 AIME II Problem 14: Borrowing in factorial base

For $N=16!-32!+48!-\cdots-1984!+2000!$, let $N=\sum_{i=1}^j f_i i!$ be its factorial-base expansion, where $0\le f_i\le i$ and $f_j>0$. Find $\sum_{i=1}^j(-1)^{i+1}f_i$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

The identity $k\,k!=(k+1)!-k!$ implies $(b+1)!-a!=\sum_{k=a}^b k\,k!$. Group the original expression as $16!+\sum_{m=1}^{62}((32m+16)!-(32m)!)$. Its factorial digits are therefore $f_{16}=1$, $f_k=k$ on each interval $32m\le k\le32m+15$, and zero elsewhere. These intervals are disjoint and all digits are allowed, so no carrying occurs. Each interval contributes eight pairs $-2q+(2q+1)=1$, while $f_{16}$ contributes $-1$. The result is $62\cdot8-1=495$.

**Answer:** 495.

**Methods:** mixed radix, telescoping, factorial digits.

**Verification:** Direct mixed-radix division of the full exact factorial integer, with reconstruction check.

**Source comparison:** All three entries were reviewed. The first two give correct telescoping and borrowing arguments. Entry 2 repeatedly misprints factorial indices and later writes a 32-term block where the nonzero block has 16 terms; its final digit pattern is correct.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. The telescoping identity k k!=(k+1)!-k! explicitly describes factorial-base borrowing.

## 2000 AIME II Problem 15: Reflection completes a trigonometric telescope

Find the least positive integer $n$ such that $\sum_{k=0}^{44}\frac1{\sin(45+2k)^\circ\sin(46+2k)^\circ}=1/\sin n^\circ$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Write the sum as $S$. The identity $\sin1^\circ/(\sin t^\circ\sin(t+1)^\circ)=\cot t^\circ-\cot(t+1)^\circ$ converts it into alternating cotangents. Reflection $t\mapsto180-t$ shows that the sum with pairs $(46,47),(48,49),\ldots,(134,135)$ also equals $S$. Adding the two cotangent expressions gives $2S\sin1^\circ=\cot45^\circ-\cot135^\circ=2$. Thus $S=1/\sin1^\circ$, and the least positive integer is $n=1$.

**Answer:** 001.

**Methods:** trigonometric telescoping, reflection symmetry.

**Verification:** Numerically evaluated all 45 original trigonometric terms.

**Source comparison:** All three source entries were reviewed. Entry 0 gives a valid cancellation argument. Entry 1 is merely an approximation-based guess, not a proof. Entry 2 has the correct reflected telescope but misprints its final equality as S=sin(1) rather than its reciprocal.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Adding the reflected sum fills the missing alternating terms in a cotangent telescope.

## 2001 AIME I Problem 2: Two changes to a mean

A finite set of distinct reals has mean $M$. Adjoining $1$ lowers its mean by $13$, while adjoining $2001$ raises it by $27$. Find $M$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

Neither 1 nor 2001 is already in the set, since adjoining an existing element would leave the mean unchanged. If the set has $n$ elements, then $(nM+1)/(n+1)=M-13$ and $(nM+2001)/(n+1)=M+27$. Subtraction gives $2000/(n+1)=40$, so $n+1=50$. The first equation now gives $M=1+13\cdot50=651$.

**Answer:** 651.

**Methods:** means, linear equations.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both source entries were reviewed. The weighted-average shortcut is valid; the proof here also explicitly justifies the increase in set size.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The same sample size makes the two changes in mean proportional to the new values distances from the original mean.

## 2001 AIME I Problem 3: A polynomial symmetric about one quarter

Find the sum of all complex roots of $x^{2001}+(1/2-x)^{2001}=0$, assuming all roots are simple.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

The degree-2001 terms cancel, while the coefficient of $x^{2000}$ is $2001/2\ne0$, so there are 2000 roots. The polynomial is unchanged by $x\mapsto1/2-x$, and the sole fixed point $x=1/4$ is not a root. Thus the roots split into 1000 pairs, each summing to $1/2$. Their total is $500$.

**Answer:** 500.

**Methods:** root symmetry, degree cancellation.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. The Vieta and root-pairing arguments are sound. Entry 2 writes an incorrect outer factor in its final sum notation; its intended centered-root argument is correct.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Reflection of roots pairs their sum, after cancellation lowers the polynomial degree by one.

## 2001 AIME I Problem 5: Equilateral triangle in an ellipse

An equilateral triangle inscribed in $x^2+4y^2=4$ has vertex $(0,1)$ and an altitude on the $y$-axis. If its squared side length is reduced $m/n$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

The other vertices have coordinates $(\pm u,v)$ with $u>0$. The equilateral altitude condition is $v=1-\sqrt3u$. Substitution into the ellipse gives $u^2+4(1-\sqrt3u)^2=4$, or $u(13u-8\sqrt3)=0$. Nondegeneracy gives $u=8\sqrt3/13$. The side length is $2u$, so its square is $768/169$ and the answer is $937$.

**Answer:** 937.

**Methods:** conics, equilateral triangles, coordinate substitution.

**Verification:** Substituted the two lower vertices into the ellipse and independently compared squared side lengths.

**Source comparison:** All seven entries were inspected, including the diagram-only entry 0. Entries 2 and 4 incorrectly impose the positive square-root branch for a vertex below the x-axis; entry 4 also uses an incorrect equilateral altitude formula. Entries 1, 3, and 5 are sound. Entry 6 has a reused point label but a valid affine-circle argument.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The horizontal base and equilateral altitude impose a line equation that intersects the ellipse in a quadratic.

## 2001 AIME I Problem 9: Area from symmetric side fractions

In triangle $ABC$ with sides $13,15,17$, points $D\in AB,E\in BC,F\in CA$ satisfy $AD/AB=p$, $BE/BC=q$, $CF/CA=r$, where $p,q,r>0$, $p+q+r=2/3$, and $p^2+q^2+r^2=2/5$. If $[DEF]/[ABC]=m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

The corner-triangle area fractions are $p(1-r)$, $q(1-p)$, and $r(1-q)$. Therefore $[DEF]/[ABC]=1-(p+q+r)+(pq+qr+rp)$. Squaring the first given sum shows $pq+qr+rp=((2/3)^2-2/5)/2=1/45$. The desired fraction is $1-2/3+1/45=16/45$, yielding $61$.

**Answer:** 061.

**Methods:** area ratios, symmetric polynomials.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. The corner-area and determinant methods are valid. Entry 2 sets p=0 despite strict positivity and assumes the area is invariant before proving it; that shortcut alone is incomplete. The numerical side lengths are unnecessary.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Subtracting the three corner triangles expresses the area ratio through the first two symmetric sums of the side fractions.

## 2001 AIME II Problem 3: A fourth-order recurrence hides a sign flip

Let $x_1=211,x_2=375,x_3=420,x_4=523$ and $x_n=x_{n-1}-x_{n-2}+x_{n-3}-x_{n-4}$ for $n\ge5$. Find $x_{531}+x_{753}+x_{975}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

For $n\ge6$, adding the recurrence equations for $x_n$ and $x_{n-1}$ and cancelling gives $x_n=-x_{n-5}$. Hence the sequence has period 10. The required sum is $x_1+x_3+x_5=x_1+x_3+(x_4-x_3+x_2-x_1)=x_2+x_4=898$.

**Answer:** 898.

**Methods:** linear recurrences, periodicity, telescoping.

**Verification:** Directly generated every recurrence term through index 975 without using periodicity.

**Source comparison:** All three entries were reviewed. The first two prove the antiperiod; the third observes a pattern and refers back to that proof.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Adding adjacent recurrence equations gives antiperiod 5 and period 10.

## 2001 AIME II Problem 4: A prescribed midpoint between two lines

Points $P,Q$ lie on $8y=15x$ and $10y=3x$, respectively, and have midpoint $(8,6)$. If $PQ=m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Write $P=(a,15a/8)$ and $Q=(b,3b/10)$. The midpoint equations are $a+b=16$ and $15a/8+3b/10=12$. They give $a=32/7,b=80/7$. Thus $Q-P=(48/7,-36/7)$, whose length is $60/7$. The answer is $67$.

**Answer:** 067.

**Methods:** midpoints, coordinates.

**Verification:** Exact endpoint substitution, midpoint check, and squared-distance calculation.

**Source comparison:** The sole source was reviewed; its midpoint system and distance calculation are correct.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The midpoint condition gives a two-by-two linear system for the endpoints.

## 2001 AIME II Problem 8: The first crossing of a self-similar tent function

For positive $x$, a function satisfies $f(3x)=3f(x)$ and $f(x)=1-|x-2|$ on $1\le x\le3$. Find the smallest positive $x$ with $f(x)=f(2001)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

On every interval $[3^k,3^{k+1}]$, including negative integers $k$, scaling gives $f(x)=3^k-|x-2\cdot3^k|$. Since $729\le2001\le2187$, $f(2001)=2187-2001=186$. Every interval below $[243,729]$ has peak at most 81, so cannot reach 186. On $[243,486]$, the first rising branch is $f(x)=x-243$, which reaches 186 at $x=429$. All later intervals begin beyond this point, so this is the minimum.

**Answer:** 429.

**Methods:** functional equations, self-similarity, piecewise linear functions.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries were reviewed. The first gives a valid scaling argument. The second mislabels the exponent of the peak at (1458,729); its geometric crossing calculation is correct.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Scaling extends a triangular graph to disjoint power-of-three intervals; the first sufficient peak determines the minimum argument.

## 2001 AIME II Problem 14: Unit roots of a sparse polynomial

List the unit-modulus roots of $z^{28}-z^8-1=0$ by arguments $0\le\theta_1<\cdots<\theta_{2n}<360^\circ$. Find $\theta_2+\theta_4+\cdots+\theta_{2n}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Put $w=z^8$. Since $|w|=|w+1|=1$, subtracting squared moduli gives $\Re w=-1/2$. Thus either $(z^8,z^{28})=(e^{120^\circ i},e^{60^\circ i})$ or its conjugate. In the first case $\theta=15^\circ+45^\circ k$ for $0\le k\le7$; the second power condition becomes $60^\circ+180^\circ k\equiv60^\circ\pmod{360^\circ}$, so $k$ is even. These arguments are $15,105,195,285$ degrees; conjugation adds $75,165,255,345$ degrees. In increasing order the even-indexed arguments are the latter four, summing to $840$.

**Answer:** 840.

**Methods:** unit complex roots, angle congruences.

**Verification:** Checked every 15-degree candidate in the original complex equation; the analytic congruence proof establishes exhaustiveness.

**Source comparison:** The sole source was reviewed. Its unit-circle geometry is correct; the explicit congruence calculation here proves completeness of the listed roots.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Equal unit moduli constrain two powers to equilateral-triangle vertices, followed by simultaneous angle congruences.

## 2002 AIME I Problem 4: A telescope followed by a prime-square factorization

For $a_k=1/(k^2+k)$, positive integers $m<n$ satisfy $\sum_{k=m}^{n-1}a_k=1/29$. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Since $1/(k(k+1))=1/k-1/(k+1)$, the condition is $1/m-1/n=1/29$. In particular $m<29$. Rearranging gives $(29-m)(29+n)=29^2$. The positive factor $29-m$ lies between 1 and 28, so the only possibility is $29-m=1$. Thus $m=28,n=812$, and the sum is $840$.

**Answer:** 840.

**Methods:** telescoping, Diophantine factorization.

**Verification:** Summed all 784 original rational terms exactly for the claimed endpoints.

**Source comparison:** Both entries were reviewed. The first needs an explicit coprimality step when inferring a divisor of 29; the shifted-product proof makes the uniqueness immediate.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. The reciprocal quadratic terms telescope; a shifted product then uses the primality of 29.

## 2002 AIME I Problem 6: Products of exponential solutions without solving them

The system $\log_{225}x+\log_{64}y=4$, $\log_x225-\log_y64=1$ has solutions $(x_1,y_1),(x_2,y_2)$. Find $\log_{30}(x_1y_1x_2y_2)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

Put $u=\log_{225}x$, $v=\log_{64}y$. Then $u+v=4$ and $1/u-1/v=1$, so $u^2-6u+4=0$. Its two roots are nonzero and different from 4, so both yield valid solutions. Their sum is 6, while the corresponding v values sum to $8-6=2$. Therefore $x_1x_2=225^6=15^{12}$ and $y_1y_2=64^2=2^{12}$. Their product is $30^{12}$, giving $12$.

**Answer:** 012.

**Methods:** logarithmic substitution, Vieta formulas.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source and its Vieta remark were reviewed. Its signs for the paired v values should be opposite those of u, but the two-root sums are correct.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Vieta gives the sum of logarithmic variables, which is exactly what the product of solutions needs.

## 2002 AIME I Problem 7: Three fractional digits of an enormous power

Find the first three digits after the decimal point of $(10^{2002}+1)^{10/7}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Write the number as $10^{2860}(1+10^{-2002})^{10/7}$. Taylor expansion with second derivative bounded above by $30/49$ on positive arguments gives $10^{2860}+10^{859}/7+R$, where $0<R<(15/49)10^{-1144}$. Since $10^6\equiv1\pmod7$ and $859\equiv1\pmod6$, the fractional part of the middle term is $3/7$. The positive remainder is smaller than $429/1000-3/7=3/7000$, so the number has fractional part strictly between $428/1000$ and $429/1000$. The requested digits are $428$.

**Answer:** 428.

**Methods:** binomial approximation, remainder bounds, modular arithmetic.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source was reviewed, including its modular alternative. It correctly identifies the decisive term but only informally bounds the tail. The explicit remainder bound here proves that no carry changes the third digit.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. A rigorously bounded binomial tail reduces the fractional digits to a modular power divided by 7.

## 2002 AIME I Problem 8: The first repeated Fibonacci-type endpoint

Consider nondecreasing positive integer sequences satisfying $a_n=a_{n-1}+a_{n-2}$ for $n>2$. Find the smallest value of $a_9$ attained by at least two such sequences.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

Writing $a_1=u,a_2=v$ with $1\le u\le v$, recurrence expansion gives $a_9=13u+21v$. If two initial pairs give the same value and the first has smaller u, their difference must be $(21t,-13t)$ for an integer $t\ge1$. Nondecreasing initial terms for the second pair require $v-13t\ge u+21t$, hence $v\ge u+34t\ge35$. Thus every collision has value at least $13+21\cdot35=748$. Equality is attained by initial pairs $(1,35)$ and $(22,22)$, so the answer is $748$.

**Answer:** 748.

**Methods:** linear recurrences, Diophantine representations, minimal collision.

**Verification:** Enumerated all positive ordered initial pairs with ninth term at most 748; found the unique first collision.

**Source comparison:** The sole source was reviewed. Its primitive step and initial-term inequality are correct; including a general positive multiple t makes the lower bound cover all possible collisions.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. The endpoint is a linear form in the initial terms, and two representations differ by a primitive lattice vector.

## 2002 AIME I Problem 12: A Möbius transformation of order three

Let $F(z)=(z+i)/(z-i)$ and $z_{n+1}=F(z_n)$, starting from $z_0=1/137+i$. If $z_{2002}=a+bi$, find $a+b$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Composition gives $F^2(z)=i(z+1)/(z-1)$ and $F^3(z)=z$ wherever the successive values are defined. The given $z_0$ is neither i nor 1; $F(z)=i$ would require $z=1$, and $F^2(z)-i=2i/(z-1)\ne0$, so this orbit avoids the pole. Since $2002\equiv1\pmod3$, $z_{2002}=F(z_0)=(1/137+2i)/(1/137)=1+274i$. Hence $a+b=275$.

**Answer:** 275.

**Methods:** Möbius transformations, composition, periodicity.

**Verification:** Numerically iterated the original complex map 2002 times, independently of the period-three reduction.

**Source comparison:** The sole source was reviewed. Its composition calculation is correct; the proof here adds the domain check needed before concluding perpetual periodicity.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Direct composition reveals a short orbit instead of requiring thousands of iterates.

## 2002 AIME II Problem 3: An integral geometric progression with a square gap

Positive integers $a<b<c$ form a geometric progression and satisfy $\log_6a+\log_6b+\log_6c=6$. If $b-a$ is a perfect square, find $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

The logarithms give $abc=6^6$. A geometric progression has $ac=b^2$, hence $b^3=6^6$ and $b=36$. Since $0<a<36$ and $36-a$ is a positive square, $a$ is one of $35,32,27,20,11$. We also need $c=1296/a$ integral. Only 27 divides 1296, giving $c=48$. Thus the sum is $27+36+48=111$.

**Answer:** 111.

**Methods:** geometric progressions, integer divisibility.

**Verification:** Exhaustively checked every smaller integer first term against the square-gap and integral geometric-mean constraints.

**Source comparison:** Both entries were reviewed. Their square-gap enumeration and middle-term reduction are correct.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. The product fixes the middle term, leaving a short list of square gaps compatible with divisibility.

## 2002 AIME II Problem 6: A reciprocal-square telescope with a rounding bound

Find the integer nearest to $1000\sum_{n=3}^{10000}1/(n^2-4)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Use $1/(n^2-4)=\tfrac14(1/(n-2)-1/(n+2))$. The expression equals $250(1+1/2+1/3+1/4)-250\sum_{j=9999}^{10002}1/j=3125/6-T$, where $0<T<1000/9999<1/9$. Consequently it lies strictly between $520.5$ and $521.5$, and the nearest integer is $521$.

**Answer:** 521.

**Methods:** partial fractions, telescoping, error bounds.

**Verification:** Numerically summed all 9998 original terms directly; the proof supplies the rigorous rounding margin.

**Source comparison:** Both entries were reviewed. Entry 0 reverses its initially named partial-fraction coefficients before writing the correct decomposition. Entry 1 says to ignore the tail; the bound here justifies the rounding.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Partial fractions cancel all but four terms at each end, and an explicit tail bound certifies the nearest integer.

## 2002 AIME II Problem 8: The first missing integer quotient

Find the least positive integer $k$ never equal to $\lfloor2002/n\rfloor$ for an integer $n\ne0$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

A positive quotient requires $n>0$, and $\lfloor2002/n\rfloor=k$ is equivalent to $2002/(k+1)<n\le2002/k$. For $1\le k\le44$ this interval has length $2002/(k(k+1))\ge2002/1980>1$, so it contains an integer. Values $k=45,46,47,48$ are attained at $n=44,43,42,41$, respectively. For $k=49$, the interval is $(2002/50,2002/49]=(40.04,40+42/49]$, containing no integer. The answer is $49$.

**Answer:** 049.

**Methods:** floor quotients, interval lengths.

**Verification:** Enumerated every possible positive nonzero floor quotient and found the first missing value.

**Source comparison:** All four entries were reviewed. Entry 0 gives a sound no-skipping argument. Entry 1 checks only the preceding value after experimentation and does not prove minimality. Entry 2 mishandles the strict lower endpoint using a ceiling; entry 3 provides only an estimate before referring to entry 0. The interval-length proof covers every smaller k.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. A floor quotient equals k exactly when a reciprocal interval contains an integer, giving a guaranteed initial range and a short boundary check.

## 2002 AIME II Problem 10: Equal sine values in degrees and radians

The two smallest positive real numbers for which $\sin(x^\circ)=\sin x$ are $m\pi/(n-\pi)$ and $p\pi/(q+\pi)$, with positive integer parameters. Find $m+n+p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

The degree argument is $\pi x/180$ radians. Equality of sines gives either $x-\pi x/180=2k\pi$ or $x+\pi x/180=(2k+1)\pi$. The least positive values in these two families are $360\pi/(180-\pi)$ and $180\pi/(180+\pi)$. The latter is smaller, and the next member of its family, $540\pi/(180+\pi)$, exceeds $360\pi/(180-\pi)$ because $\pi<36$. Thus these are exactly the two smallest solutions. The parameter sum is $360+180+180+180=900$.

**Answer:** 900.

**Methods:** trigonometric equations, ordering solutions.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries were reviewed. Their two solution families are correct. The explicit comparison with the next member proves the claimed ordering.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The two standard families of equal sine arguments produce interlaced positive solution sequences.

## 2002 AIME II Problem 11: Two geometric series with a shared second term

Two distinct convergent real geometric series each sum to $1$ and have the same second term. One has third term $1/8$. Write the common second term as $(\sqrt m-n)/p$, with square-free $m$, and find $100m+10n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

If their ratios are r and s, their first terms are $1-r$ and $1-s$. Equality of second terms gives $r(1-r)=s(1-s)$. Distinctness forces $s=1-r$ and $r\ne1/2$. Convergence of both series then requires $0<r<1$. For the series with third term $1/8$, $(1-r)r^2=1/8$, or $(2r-1)(4r^2-2r-1)=0$. The admissible root is $r=(1+\sqrt5)/4$: the other quadratic root is negative, and $1/2$ would make the series identical. Therefore the common second term is $r(1-r)=(\sqrt5-1)/8$, giving $518$.

**Answer:** 518.

**Methods:** geometric series, convergence, factorization.

**Verification:** Checked convergence, the prescribed third term, and the shared second term for the two distinct ratios.

**Source comparison:** All three entries were reviewed. Entry 0 selects a root from the requested answer form without explaining distinctness and convergence. Entry 2 incorrectly identifies the negative quadratic root as the second ratio; its later sidenote corrects this to the complementary ratio. The proof here explicitly filters every root.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Equal sums make the first term and ratio complementary, while distinctness excludes a repeated quadratic root.

## 2002 AIME II Problem 14: A circle centered on a leg of a right triangle

Right triangle $APM$ has right angle at $A$ and perimeter $152$. A circle of radius $19$, centered at $O\in AP$, is tangent to $AM$ and $PM$. Write $OP=m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Let $AM=b$ and $\theta=\angle AMP$. Tangency gives $AO=19$ and makes MO the internal angle bisector, so $t=\tan(\theta/2)=19/b<1$. The double-angle formulas give $AP/b=2t/(1-t^2)$ and $PM/b=(1+t^2)/(1-t^2)$. Therefore the perimeter is $2b/(1-t)=2b^2/(b-19)=152$. This simplifies to $(b-38)^2=0$, so $b=38$ and $t=1/2$. Hence $AP=b\cdot(2t)/(1-t^2)=152/3$, and $OP=AP-19=95/3$. The answer is $98$.

**Answer:** 098.

**Methods:** tangent circles, half-angle substitution, right triangles.

**Verification:** Exact Pythagorean, perimeter, and point-to-hypotenuse tangency checks for the derived right triangle.

**Source comparison:** All three entries were reviewed. Entries 0 and 2 yield valid similarity and half-angle arguments. Entry 1 includes unsupported square-root ratios and an incomplete elimination, so its numerical result is not a self-contained proof.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The center lies on the other vertex angle bisector, turning the perimeter condition into a perfect-square equation.

## 2002 AIME II Problem 15: Two tangent circles through one point

Two circles meet in two points, including $(9,6)$. Both are tangent to the x-axis and to $y=mx$, where $m>0$, and their radii have product $68$. Write $m=a\sqrt b/c$ in lowest radical form and find $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Both circles lie above the x-axis. They also lie on the same side of their other common tangent, since opposite-side disks could share at most a point on that line. Their centers therefore lie on the same angle-bisector ray and can be written $(kr_1,r_1),(kr_2,r_2)$. Passing through $(9,6)$ gives $k^2r^2-(18k+12)r+117=0$. The distinct circles have distinct radii, so Vieta gives $k^2=117/68$. Tangency to $y=mx$ gives $(1-km)^2=1+m^2$, hence $m=2k/(k^2-1)$. Because $m>0$ and $k^2>1$, k is positive. Thus $m=2\sqrt{117/68}/(49/68)=12\sqrt{221}/49$, and the answer is $282$.

**Answer:** 282.

**Methods:** circle tangency, Vieta formulas, angle bisectors.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed, including the parabola reinterpretation and explicit-center sidenote. Their main quadratic reductions agree. The original proofs assume the same angle-bisector branch; the shared-tangent separation argument here justifies that assumption.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The radii are roots of a common point-on-circle quadratic, so their product determines the common angle bisector.

## 2003 AIME I Problem 2: Alternating concentric annuli

Concentric circles have radii $1,2,\ldots,100$. Color the central disk red and alternate red and green on successive annuli. If the green area divided by the radius-100 disk area is reduced $m/n$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

The green annuli have inner and outer radii $(2j-1,2j)$ for $1\le j\le50$. Their total area is $\pi\sum_{j=1}^{50}((2j)^2-(2j-1)^2)=\pi\sum_{j=1}^{50}(4j-1)=5050\pi$. Dividing by $10000\pi$ gives $101/200$, so the answer is $301$.

**Answer:** 301.

**Methods:** annular areas, arithmetic sums.

**Verification:** Direct exact sum of all 50 green annular area coefficients.

**Source comparison:** All three entries were reviewed, including the smaller-case pattern and alternate sum in entry 0. The exact arithmetic-series derivations are sound; the observed pattern alone would need proof.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Each green annulus has area given by a consecutive-square difference, so the total is an arithmetic sum.

## 2003 AIME I Problem 4: A logarithmic trigonometric invariant

Given $\log_{10}\sin x+\log_{10}\cos x=-1$ and $\log_{10}(\sin x+\cos x)=\tfrac12(\log_{10}n-1)$, find n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

The first equation gives $\sin x\cos x=1/10$. Hence $(\sin x+\cos x)^2=1+2/10=6/5$. Doubling the second equation gives $\log_{10}((\sin x+\cos x)^2)=\log_{10}(n/10)$, so $n/10=6/5$ and $n=12$.

**Answer:** 012.

**Methods:** logarithm laws, trigonometric identities.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. Their invariant is correct. Entry 1 introduces an unnecessary division by a logarithm; positivity of the sum squared makes the direct exponentiation simpler.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The product of sine and cosine determines their squared sum without finding the angle.

## 2003 AIME I Problem 8: An arithmetic triple followed by a geometric triple

Four increasing positive integers have their first three in arithmetic progression and their last three in geometric progression. The last exceeds the first by 30. Find their sum.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

Write the first three terms as $a-d,a,a+d$, with integers $a>d>0$. The fourth is $(a+d)^2/a$, so the endpoint condition is $30=3d+d^2/a$. Because $0<d^2/a<d$, this gives $3d<30<4d$, hence $d=8$ or 9. Solving $a=d^2/(30-3d)$ gives the noninteger $32/3$ for $d=8$ and $a=27$ for $d=9$. The sequence is $18,27,36,48$, whose sum is $129$.

**Answer:** 129.

**Methods:** mixed progressions, integer bounds.

**Verification:** Exhaustively checked steps 1 through 9 and middle terms through 10000; the analytic inequality narrows the unbounded problem to the two final steps.

**Source comparison:** All three entries were reviewed. Entries 0 and 2 provide valid bounds. Entry 1 explicitly relies on presumed AIME uniqueness instead of checking all factor cases, so its standalone argument is incomplete.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. The endpoint difference bounds the common arithmetic step between two consecutive integers, leaving one integral solution.

## 2003 AIME I Problem 11: Triangle inequalities as interval probability

Choose $x$ uniformly from $(0,90^\circ)$. The probability that $\sin^2x,\cos^2x,\sin x\cos x$ fail to form a triangle is $d/n$, where $d$ is the degree measure of $\arctan m$ and $m+n<1000$. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Reflection $x\mapsto90^\circ-x$ preserves the event. On $(0,45^\circ)$ the largest length is $\cos^2x$, so failure means $\cos2x\ge\tfrac12\sin2x$, or $x\le\tfrac12\arctan2$. The two symmetric intervals have total length $\arctan2$, hence probability $(\arctan2)/90$. The requested value is $2+90=92$. Endpoints have probability zero.

**Answer:** 092.

**Methods:** continuous probability, symmetry.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry, algebra. A random angle produces a geometric-probability event governed by triangle inequalities and trigonometric thresholds.

## 2003 AIME I Problem 12: Equal opposite angles cancel two cosine laws

Convex quadrilateral $ABCD$ has $\angle A=\angle C$, $AB=CD=180$, $AD\ne BC$, and perimeter $640$. Find $\lfloor1000\cos A\rfloor$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Put $u=AD,v=BC$. The two cosine laws for diagonal BD give $180^2+u^2-360u\cos A=180^2+v^2-360v\cos A$. Thus $(u-v)(u+v-360\cos A)=0$. Since $u\ne v$, and $u+v=640-360=280$, we obtain $\cos A=7/9$. Hence the requested floor is $777$.

**Answer:** 777.

**Methods:** cosine-law subtraction, quadrilaterals.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries were reviewed. The subtraction proof is direct and valid. The alternate ambiguous-SSA construction reaches the same relation but needs careful point ordering; no such auxiliary construction is needed here.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The common diagonal has two cosine-law expressions whose difference factors by the unequal sides.

## 2003 AIME II Problem 8: Products of arithmetic sequences are quadratic

A sequence begins $1440,1716,1848,\ldots$ and is formed by multiplying corresponding terms of two arithmetic sequences. Find its eighth term.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

The nth term is a product of two affine functions of n, hence a polynomial of degree at most two. Its first differences start at $276,132$, so the constant second difference is $-144$. The discrete quadratic formula gives $a_8=a_1+7\Delta a_1+\binom72\Delta^2a_1=1440+7\cdot276-21\cdot144=348$.

**Answer:** 348.

**Methods:** finite differences, quadratic interpolation.

**Verification:** Constructed two explicit arithmetic sequences matching all three supplied products and checked their eighth product; uniqueness follows from quadratic interpolation.

**Source comparison:** All five entries were reviewed. Entries 0–2 are correct. Entry 3 writes the quadratic coefficient as a sum instead of a product and misindexes its displayed first-difference rule, though its later numerical differences are correct. Entry 4 drops a factor b in an expansion but its interpolation combination is correct.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Constant second differences determine every later term from the first three products.

## 2003 AIME II Problem 9: Reduce a polynomial before summing it over roots

Let $P(x)=x^6-x^5-x^3-x^2-x$ and $Q(x)=x^4-x^3-x^2-1$. If $z_1,\ldots,z_4$ are the roots of Q, counted with multiplicity, find $\sum_{j=1}^4P(z_j)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

The identity $P(x)=(x^2+1)Q(x)+x^2-x+1$ gives $P(z_j)=z_j^2-z_j+1$. Vieta gives $\sum z_j=1$ and $\sum_{i<j}z_i z_j=-1$, hence $\sum z_j^2=1^2-2(-1)=3$. The required sum is $3-1+4=6$.

**Answer:** 006.

**Methods:** polynomial remainders, Vieta formulas, root sums.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries were reviewed. The remainder arguments are correct. Entry 1 misindexes one term in its general Newton recurrence; its target numerical result agrees with the shorter division calculation.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Polynomial division lowers the target degree, after which Vieta determines the needed power sums.

## 2003 AIME II Problem 14: An equilateral hexagon with six prescribed heights

A convex equilateral hexagon ABCDEF has $A=(0,0)$, $B=(b,2)$, $\angle FAB=120^\circ$, and opposite sides parallel. Its vertex y-coordinates are exactly $0,2,4,6,8,10$. Write its area as $m\sqrt n$ with square-free n, and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Let the first three directed sides be u,v,w. Convexity and equal opposite parallel sides make the remaining sides $-u,-v,-w$, so the vertices are $0,u,u+v,u+v+w,v+w,w$. Central symmetry makes opposite y-coordinates sum to 10. Thus $D_y=10,E_y=8$, while $(F_y,C_y)$ is either $(4,6)$ or $(6,4)$. Reflect horizontally if needed so $b>0$. Writing $s=F_y$, rotation through $120^\circ$ gives $u=(2(s+1)/\sqrt3,2)$ and $w=(-(s+4)/\sqrt3,s)$. If s=6, then $v_y=2$; equal lengths force either $v=u$, causing collinearity, or $v=(-14/\sqrt3,2)$, for which $u\times v>0$ but $v\times w<0$, contradicting convexity. Thus s=4. We obtain $u=(10/\sqrt3,2)$, $v=(8/\sqrt3,4)$, $w=(-8/\sqrt3,4)$; the other sign for v would make v=w. Shoelace on the six displayed vertices gives area $144/\sqrt3=48\sqrt3$, so the answer is $51$.

**Answer:** 051.

**Methods:** centrally symmetric polygons, convexity, coordinate area.

**Verification:** Exact scaled-coordinate checks of all six equal lengths, positive turns, and area; actual x-coordinates are divided by sqrt(3).

**Source comparison:** All four entries were reviewed. Every source assumes the crucial height order without a full exclusion of the alternative; the proof here supplies that missing convexity argument. Entry 2 includes an erroneous factor 1/2 in its parallelogram area display. Entry 3 misprints the negative root of its auxiliary quadratic.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Opposite parallel equal sides force central symmetry; convexity eliminates the competing height order before coordinates determine area.

## 2003 AIME II Problem 15: Triangular coefficients encode a squared geometric sum

Let $P(x)=24x^{24}+\sum_{j=1}^{23}(24-j)(x^{24-j}+x^{24+j})$. For its distinct roots z, write $\sum_z|\operatorname{Im}(z^2)|=m+n\sqrt p$ with square-free p. Find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

The triangular coefficient pattern gives $P(x)=x(1+x+\cdots+x^{23})^2$. Its distinct roots are 0 and the 24th roots of unity other than 1. The zero root contributes nothing, and including the omitted root 1 would also add zero. Thus the required sum is $\sum_{k=0}^{23}|\sin(30k^\circ)|$. There are four equal positive half-cycles, each summing to $\sin30^\circ+\sin60^\circ+\sin90^\circ+\sin120^\circ+\sin150^\circ=2+\sqrt3$. The result is $8+4\sqrt3$, yielding $15$.

**Answer:** 015.

**Methods:** polynomial convolution, roots of unity, trigonometric sums.

**Verification:** Verified the exact polynomial coefficient convolution and independently summed the 24 trigonometric contributions numerically.

**Source comparison:** All three entries were reviewed. Entries 0 and 2 correctly track distinct roots and repeated squared values. Entry 1 divides away zero and multiplies by x-1 without tracking exclusions; the direct factorization preserves the root set.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Factoring the coefficient convolution identifies roots of unity, whose squared imaginary parts have a short trigonometric cycle.

## 2004 AIME I Problem 2: Consecutive sets from their means

A set A of m consecutive integers sums to $2m$. A set B of $2m$ consecutive integers sums to m. Their greatest elements differ in absolute value by 99. Find m.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

The means of A and B are 2 and $1/2$. The maximum of a consecutive n-term set is its mean plus $(n-1)/2$, so the maxima are $(m+3)/2$ and m. Hence $|m-3|/2=99$. The possibilities are $m=201$ and $m=-195$, and positivity selects $201$. This odd value also makes both starting points integral.

**Answer:** 201.

**Methods:** arithmetic sequences, means.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All five entries were reviewed. Entries 0, 1, and 4 have valid equations. Entry 2 dismisses the absolute-value branch without justification; entry 3 relies on observed growth and includes sign and arithmetic slips. Explicitly solving both branches avoids these issues.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The mean and number of consecutive integers determine each maximum directly.

## 2004 AIME I Problem 5: Strict daily rates with a larger aggregate score

A contestant attempts 500 points over two days and scores a positive integer each day. Its first-day success rate is below $160/300$, its second-day rate below $140/200$, and it does not attempt 300 points on day one. Find m+n for the largest possible aggregate rate m/n in lowest terms.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Let q be the first-day attempted points and let a,b be the two scores. Then $a<(8/15)q$ and $b<(7/10)(500-q)$, so $a+b<350-q/6<350$. Since the scores are integers, their sum is at most 349. This is attainable by attempting 2 points and scoring 1 on day one, then attempting 498 and scoring 348 on day two: both strict rate inequalities hold. The maximal aggregate rate is $349/500$, yielding $849$.

**Answer:** 849.

**Methods:** weighted averages, integer optimization, strict inequalities.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries were reviewed. Entry 0 gives the correct global bound but incorrectly says every q from 2 through 5 attains 349; q=3 or 5 does not. Entry 1 constructs a valid optimum but does not explicitly prove the universal bound. The proof here combines the bound with one verified witness.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. A weighted rate bound caps the integer total, and one allocation attains that cap.

## 2004 AIME I Problem 7: Pair contributions to a coefficient

Find the absolute value of the coefficient of $x^2$ in $\prod_{k=1}^{15}(1+(-1)^k kx)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Put $a_k=(-1)^k k$. The desired coefficient is $\sum_{i<j}a_i a_j=((\sum a_i)^2-\sum a_i^2)/2$. Here $\sum a_i=-8$ and $\sum a_i^2=15\cdot16\cdot31/6=1240$. The coefficient is $(64-1240)/2=-588$, giving $588$.

**Answer:** 588.

**Methods:** contribution counting, generating functions.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: An ordered-pair index is used where an unordered-pair index is required before doubling. Source 3: A positive contribution subtotal is mistyped; the printed arithmetic does not give the claimed result. Source 4: The final coefficient sign is reversed; its absolute value is still correct. Source 6: The displayed product does not retain the original alternating signs, so that expansion cannot justify the requested coefficient.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. The quadratic coefficient is a pairwise-product sum extracted from a signed product.

## 2004 AIME I Problem 11: Equal painted-area and volume ratios

A cone of height 4 and radius 3 is painted on its entire exterior, including its base. A parallel cut separates a smaller cone C and a frustum F. Their painted-area ratio C:F equals their volume ratio C:F, namely reduced m/n. Find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

The original slant height is 5, so its lateral and total painted areas are $15\pi$ and $24\pi$. Let the smaller cone have linear scale t. Its painted-area fraction of the whole is $(15/24)t^2=(5/8)t^2$, while its volume fraction is $t^3$. Equal part-to-remainder ratios force these fractions equal, so $t=5/8$ since $t>0$. Therefore $m/n=t^3/(1-t^3)=125/387$, and $m+n=512$.

**Answer:** 512.

**Methods:** similarity exponents, painted surfaces, ratio conversion.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries were reviewed. Their radius and scale-factor calculations are correct. Passing directly to part-to-whole fractions cancels the common remainder denominators before solving.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equality of part-to-remainder ratios is equivalent to equality of part-to-whole fractions, which exposes the scale exponents.

## 2004 AIME I Problem 12: Area selected by even logarithmic floors

Let S consist of $(x,y)\in(0,1]^2$ for which both $\lfloor\log_2(1/x)\rfloor$ and $\lfloor\log_5(1/y)\rfloor$ are even. If S has area reduced m/n, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

For a base $b>1$, an even logarithmic floor selects intervals $(b^{-(2j+1)},b^{-2j}]$ for $j\ge0$. Their total length is $(1-1/b)\sum_{j\ge0}b^{-2j}=b/(b+1)$. The allowed x and y sets therefore have lengths $2/3$ and $5/6$. Since S is their Cartesian product, its area is $5/9$, giving $14$.

**Answer:** 014.

**Methods:** geometric series, floor functions, product regions.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source was reviewed. Its interval lengths and product calculation are correct; some endpoints are written open instead of closed, which does not affect area.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. The two independent coordinate conditions select geometric sequences of intervals, so their measures multiply.

## 2004 AIME I Problem 13: Two interlaced families of roots of unity

Write the 34 roots of $(1+x+\cdots+x^{17})^2-x^{17}$ as $r_k e^{2\pi ia_k}$, where $r_k>0$ and $0<a_1\le\cdots\le a_{34}<1$. If $a_1+\cdots+a_5=m/n$ in lowest terms, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Multiplication by $(x-1)^2$ gives $(x^{18}-1)^2-x^{17}(x-1)^2=(x^{19}-1)(x^{17}-1)$. Since $P(1)=323\ne0$, its roots are precisely the nontrivial 17th and 19th roots of unity. Their sets do not overlap because 17 and 19 are coprime. The five smallest arguments divided by $2\pi$ are $1/19,1/17,2/19,2/17,3/19$. Their sum is $6/19+3/17=159/323$, giving $482$.

**Answer:** 482.

**Methods:** geometric-sum factorization, roots of unity, argument ordering.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source was reviewed. Its factorization and comparison of the five least arguments are correct; evaluating P at 1 explicitly accounts for the canceled denominator.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A geometric-sum identity factors the polynomial into two cyclotomic root sets whose smallest arguments can be ordered rationally.

## 2004 AIME II Problem 5: Recovering a delayed work schedule

A job was planned for 1000 equally productive workers. Its first quarter used all 1000, its second quarter used 900, and its third used 800. Find the fewest additional workers to hire for the last quarter so the original deadline is met.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Normalize each quarter to 1000 worker-days, so the original deadline is 4 days. The first three quarters take $1+1000/900+1000/800=121/36$ days, leaving $23/36$. The final workforce must therefore be at least $1000/(23/36)=36000/23$. Its least integer value is 1566, so the additional number is $1566-800=766$.

**Answer:** 766.

**Methods:** work rates, reciprocal sums, ceiling.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. The speed analogy and the two worker-time normalizations agree and use the correct upward rounding.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Equal work portions consume times inversely proportional to workforce, and the final requirement is rounded upward.

## 2004 AIME II Problem 6: Integer shares in a three-stage distribution

Three monkeys successively take portions of a banana pile. They keep respectively $3/4,1/4,1/12$ of their portions and split each remainder equally between the other two. Every transfer is integral, the last monkey empties the pile, and final holdings have ratio $3:2:1$. Find the smallest initial pile.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

The three taken portions must be $8x,8y,24z$ for positive integers x,y,z. The final holdings are $6x+3y+11z$, $x+2y+11z$, and $x+3y+2z$. Equating the first two to three and two times the last gives $3x-6y+5z=0$ and $-x-4y+7z=0$. Elimination yields $9x=11z$ and $9y=13z$. Thus $z=9t,x=11t,y=13t$ with positive integer t. The total is $(8\cdot11+8\cdot13+24\cdot9)t=408t$. Taking t=1 gives holdings $204,136,68$, so the minimum is $408$.

**Answer:** 408.

**Methods:** integer linear systems, primitive ratios, divisibility.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries were reviewed. The units-based and normalized-fraction systems are valid. Entry 0 lists 72 as a basic divisibility requirement for the third portion, whereas the split itself requires 24; entry 2 incorrectly says 11 divides that portion. The explicit primitive parameterization removes these bookkeeping errors.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Choosing units that make each split integral turns the final-ratio conditions into a primitive integer null vector.

## 2004 AIME II Problem 9: Alternating arithmetic and geometric triples

A positive integer sequence starts at $a_1=1$. Every triple $a_{2j-1},a_{2j},a_{2j+1}$ is geometric, and every triple $a_{2j},a_{2j+1},a_{2j+2}$ is arithmetic. Given $a_9+a_{10}=646$, let $a_n$ be its greatest term below 1000. Find $n+a_n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Put $q=a_2$ and $f_j=1+j(q-1)$. Induction using the geometric and arithmetic conditions gives $a_{2j+1}=f_j^2$ and $a_{2j}=f_{j-1}f_j$: a geometric step squares the latter product and divides by $f_{j-1}^2$, and the next arithmetic step uses $2f_j-f_{j-1}=f_{j+1}$. Thus $(4q-3)(9q-7)=646$, or $(q-5)(36q+125)=0$, so $q=5$. Now $f_j=4j+1$, making the sequence increasing. We have $a_{16}=29\cdot33=957$ and $a_{17}=33^2=1089$, so the answer is $16+957=973$.

**Answer:** 973.

**Methods:** alternating recurrences, arithmetic-square representation, induction.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. Entry 0 proves the structural formula. Entry 1 merely guesses the initial term and does not prove uniqueness. Entry 2 assumes strict increase without deriving it; the positive initial parameter and formula here justify that property.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The odd terms are squares of an arithmetic progression and the even terms are products of neighboring members.

## 2004 AIME II Problem 12: A circle between four vertex circles

Isosceles trapezoid ABCD has $AB=6,CD=4,AD=BC=5$. Circles centered at A,B have radius 3, and those at C,D have radius 2. A circle contained in the trapezoid is tangent to all four. Write its radius as $(-k+m\sqrt n)/p$ with square-free n and $\gcd(k,p)=1$, and find $k+m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Use $A=(0,0),B=(6,0),D=(1,h),C=(5,h)$, where $h=\sqrt{24}$. Internal tangency to a corner circle would put the desired circle inside that disk; tangency also to the neighboring disk, which touches it on a trapezoid side, would force the desired center onto that boundary side, impossible for a positive-radius contained circle. Thus all four tangencies are external; equal distances to A,B place its center at $(3,y)$. For radius r, the tangencies give $y^2=r^2+6r$ and $(h-y)^2=r^2+4r$. Subtraction yields $y=(12+r)/h$. Substituting back gives $23r^2+120r-144=0$, whose unique positive root is $(-60+48\sqrt3)/23$. It satisfies the original unsquared tangency equations and lies in the interior gap. Hence the answer is $60+48+3+23=134$.

**Answer:** 134.

**Methods:** tangent circles, symmetry axes, quadratic elimination.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source was reviewed. Its radical-sum equation is correct; subtracting squared distances avoids repeated squaring and displays the unique positive root directly.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equal-radius tangencies force the symmetry axis, and subtracting two squared distance equations makes the center height linear in the radius.

## 2005 AIME I Problem 4: A rectangular formation five above a square

A band has five more members than a square formation can hold, and exactly fills a rectangle with seven more rows than columns. Find its greatest possible size.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Let the rectangle have n columns and let the square side count be s. Then $n(n+7)=s^2+5$, so $(2n+7-2s)(2n+7+2s)=69$. Both factors are positive odd integers; their pairs are $(1,69)$ and $(3,23)$. Their sum equals $4n+14$, which is largest for $(1,69)$, giving $n=14,s=17$. The resulting band size is $14\cdot21=294$.

**Answer:** 294.

**Methods:** completing the square, Diophantine factorization.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All seven entries were reviewed. The bounding-squares and factor-pair proofs are sound. Entry 4 contains incorrect signs, a repeated variable, and a factor 68 instead of 69. Entry 6 uses the AIME answer range as an unjustified global bound; the complete factorization avoids that reliance.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Completing the square converts the two formation requirements to factor pairs of 69.

## 2005 AIME I Problem 6: Complete a fourth power before separating roots

Let P be the product of the nonreal roots of $x^4-4x^3+6x^2-4x=2005$. Find $\lfloor P\rfloor$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

Adding 1 gives $(x-1)^4=2006$. If $r=2006^{1/4}>0$, the nonreal roots are $1+ir$ and $1-ir$, with product $1+r^2=1+\sqrt{2006}$. Since $44^2<2006<45^2$, the floor is $45$.

**Answer:** 045.

**Methods:** translated powers, complex conjugates.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries were reviewed. The main fourth-power and quadratic-factor methods agree. Entry 2 calls 0 and 2 roots of the left polynomial, not of the full equation; entry 4 final rationalization note incorrectly replaces square roots by fourth roots. The conjugate product is immediate after translation.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A translation makes the quartic a pure fourth power, separating real and conjugate imaginary branches.

## 2005 AIME I Problem 8: A sum of exponential roots from a cubic product

The equation $2^{333x-2}+2^{111x+2}=2^{222x+1}+1$ has three real roots whose sum is reduced m/n. Find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

Set $y=2^{111x}>0$. Multiplying by 4 gives $y^3-8y^2+16y-4=0$. The three original roots correspond to its three positive roots $y_1,y_2,y_3$. Vieta gives their product 4, hence $2^{111(x_1+x_2+x_3)}=4$. Therefore the sum is $2/111$ and the answer is $113$.

**Answer:** 113.

**Methods:** exponential substitution, Vieta product.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source was reviewed. Its use of the supplied three-real-root hypothesis correctly identifies all three cubic roots as positive.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Exponentiating converts addition of the original roots into multiplication of the substituted roots, which Vieta supplies.

## 2005 AIME I Problem 10: Move along a median to prescribe area

Triangle ABC has area 70, with $B=(12,19)$ and $C=(23,20)$. Its median from $A=(p,q)$ to BC has slope $-5$. Find the largest p+q.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

The midpoint of BC is $M=(35/2,39/2)$, so write $A=M+t(1,-5)$. Since $C-B=(11,1)$, the determinant of $C-B$ and $A-B$ is $-56t$. Thus the area condition gives $28|t|=70$, or $t=\pm5/2$. The coordinate sum is $p+q=37-4t$, maximized at $t=-5/2$, giving $47$.

**Answer:** 047.

**Methods:** median coordinates, determinants, linear parameterization.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries were reviewed. Entry 0 omits the absolute-value branch and assumes the desired ordering; entry 1 initially omits a square root in the point-line denominator before correcting it; entries 2 and 3 give valid two-branch calculations. The parameter proof treats both signs at once.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A line parameter through the midpoint makes oriented area linear in one scalar.

## 2005 AIME I Problem 11: Largest semicircle in a square

A semicircular region lies inside a square of side 8. Its largest possible diameter is $m-\sqrt n$ for positive integers m,n. Find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Let its radius be r. By square symmetries, take the diameter direction as $(\cos\theta,\sin\theta)$ with $0\le\theta\le\pi/2$, and the curved half on the side with normal $(-\sin\theta,\cos\theta)$. Its horizontal width is $r(1+\cos\theta)$ and vertical width is $r(1+\sin\theta)$: in each coordinate one extreme lies on the arc and the other at a diameter endpoint. Fitting inside the square requires $r(1+\max(\cos\theta,\sin\theta))\le8$. Since the maximum is at least $1/\sqrt2$, $r\le8/(1+1/\sqrt2)=16-8\sqrt2$. Equality is attained at $\theta=\pi/4$ by translating the bounding square onto the given square. The diameter is $32-16\sqrt2=32-\sqrt{512}$, so the answer is $544$.

**Answer:** 544.

**Methods:** convex widths, orientation optimization, semicircles.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries were reviewed, including the incomplete introductory entry 0. They calculate the diagonal placement correctly but justify its global optimality only heuristically or by assertion. The two-width bound proves the maximum over all translations and orientations.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Horizontal and vertical widths give a global orientation bound, attained by a diagonal diameter.

## 2005 AIME I Problem 14: Constructing a square by perpendicular normal coordinates

A unique square has the points $A=(0,12)$, $B=(10,9)$, $C=(8,0)$, $D=(-4,7)$ on four different sides. If its area is K, find the remainder of 10K modulo 1000.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Consider the four lines $-x+3y=36$, $-x+3y=-8$, $3x+y=39$, and $3x+y=-5$. Their normals $(-1,3)$ and $(3,1)$ are perpendicular and have equal length $\sqrt{10}$; each strip has width $44/\sqrt{10}$, so their intersection is a square. A,B,C,D lie on the respective four lines, and their values in the other normal coordinate lie within the corresponding strip, so they are on the actual sides. By the supplied uniqueness, this is the required square. Hence $K=44^2/10$ and $10K\equiv936\pmod{1000}$.

**Answer:** 936.

**Methods:** normal coordinates, supporting lines, square reconstruction.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries were reviewed. Their rotated-vector and normal-vector methods agree. The second calls the prescribed side points opposite vertices, a wording error; the explicit strip construction verifies the required side incidences.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Two perpendicular linear forms provide equal-width strips whose boundary lines pass through the four prescribed points.

## 2005 AIME I Problem 15: An incircle trisecting a median

Triangle ABC has $BC=20$. Its incircle meets median AD at the two trisection points. If its area is $m\sqrt n$ with square-free n, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Let $b=CA,c=AB$, and write $AD=L$. The two secant powers are equal: $\operatorname{Pow}(A)=\operatorname{Pow}(D)=2L^2/9$. If the incircle touches BC at T and the semiperimeter is s, the tangent lengths give $\operatorname{Pow}(A)=(s-20)^2$ and $\operatorname{Pow}(D)=DT^2=(b-c)^2/4$. Thus $b+c-20=|b-c|$, so the smaller of b,c is 10. Take $b=10,c>10$. The median formula gives $L^2=(c^2-100)/2$. Equating the power at A yields $9(c-10)^2=4(c^2-100)$, or $(c-10)(c-26)=0$. Nondegeneracy forces $c=26$. Heron gives area $\sqrt{28\cdot8\cdot18\cdot2}=24\sqrt{14}$, so the answer is $38$.

**Answer:** 038.

**Methods:** power of a point, incircle tangents, median formula.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. Their tangent-length and median calculations are valid. Expressing the two equal powers symmetrically avoids assuming the side ordering before deriving which side must equal 10.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equal secant powers at the median endpoints force one side to be half the base, after which the median formula determines the other side.

## 2005 AIME II Problem 1: A binomial ratio determines deck size

A deck with $n\ge6$ distinct cards has six times as many six-card subsets as three-card subsets. Find $n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

Cancel factorials in $\binom n6=6\binom n3$ to obtain $(n-3)(n-4)(n-5)=720$. The left side increases strictly for $n\ge6$. Since $10\cdot9\cdot8=720$, the unique solution is $n=13$.

**Answer:** 013.

**Methods:** binomial coefficients.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. A ratio of binomial coefficients gives a short integer equation for the deck size.

## 2005 AIME II Problem 3: A geometric series and its squared terms

An infinite geometric series sums to 2005. Squaring every term produces a series whose sum is 20050. If the original common ratio is reduced m/n, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

Let the first term be a and ratio r, with $|r|<1$. The sum formulas give $a/(1-r)=2005$ and $a^2/(1-r^2)=20050$. Dividing yields $a/(1+r)=10$, so $2005(1-r)=10(1+r)$. Hence $r=1995/2015=399/403$, which lies in the convergence interval, and the answer is $802$.

**Answer:** 802.

**Methods:** geometric series, ratio elimination.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries were reviewed. Their two-sum reductions agree. The second uses a trial scaling of numerator and denominator; direct reduction gives the primitive ratio immediately.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Dividing the two sum formulas cancels one factor and gives a linear equation for the ratio.

## 2005 AIME II Problem 5: Reciprocal logarithms force powers

Count ordered integer pairs $(a,b)$ with $2\le a,b\le2005$ satisfying $\log_a b+6\log_b a=5$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Let $t=\log_a b>0$. Then $t+6/t=5$, so $(t-2)(t-3)=0$. Thus $b=a^2$ or $b=a^3$. The square family has $a=2,\ldots,44$, giving 43 pairs; the cube family has $a=2,\ldots,12$, giving 11. No ordered pair belongs to both because $a^2=a^3$ would require $a=1$. The total is $54$.

**Answer:** 054.

**Methods:** logarithmic ratios, integer powers.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. Their quadratic substitutions are valid. The explanatory note in entry 0 correctly distinguishes overlap of b values from overlap of ordered pairs.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. A quadratic in the logarithmic ratio reduces the integer pairs to square and cube families.

## 2005 AIME II Problem 7: A dyadic radical product telescopes

Let $x=4/((\sqrt5+1)(\sqrt[4]5+1)(\sqrt[8]5+1)(\sqrt[16]5+1))$. Find $(x+1)^{48}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Put $z=5^{1/16}$. Repeatedly factoring differences of squares gives $(z-1)(z+1)(z^2+1)(z^4+1)(z^8+1)=z^{16}-1=4$. Therefore $x=z-1$, so $(x+1)^{48}=z^{48}=5^3=125$.

**Answer:** 125.

**Methods:** difference of squares, radical products.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. Telescoping conjugates and expanded geometric sums give the same identity.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Repeated difference-of-squares factors turn the entire denominator into one geometric quotient.

## 2005 AIME II Problem 9: A swapped sine-cosine power identity

For how many positive integers $n\le1000$ does $(\sin t+i\cos t)^n=\sin(nt)+i\cos(nt)$ hold for every real t?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Since $\sin t+i\cos t=ie^{-it}$, the identity is $i^n e^{-int}=ie^{-int}$. It holds for every t exactly when $i^n=i$, equivalently $n\equiv1\pmod4$. The values are $1,5,\ldots,997$, totaling $250$.

**Answer:** 250.

**Methods:** complex exponentials, roots of unity, congruences.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All eight entries were reviewed. The exponential and argument calculations are valid. Entry 4 tests only t=0, proving necessity but not sufficiency; entry 5 drops an exponent in an intermediate factorization. The displayed equivalence supplies both directions.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. The expression is i times a unit exponential, so the universal identity becomes a fourth-root-of-unity congruence.

## 2005 AIME II Problem 11: Adjacent products linearize a nonlinear recurrence

A real sequence satisfies $a_0=37,a_1=72,a_m=0$ and $a_{k+1}=a_{k-1}-3/a_k$ for $1\le k<m$. Find the positive integer m.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Multiplying the recurrence by $a_k$ gives $a_ka_{k+1}=a_{k-1}a_k-3$. Hence $a_ka_{k+1}=2664-3k$. At $k=m-1$, the left side is zero, so $2664=3(m-1)$ and $m=889$. This endpoint is attainable: all adjacent products for $k<888$ are positive, so starting from positive $a_0,a_1$, induction keeps every denominator nonzero through $a_{888}$; the next term is zero.

**Answer:** 889.

**Methods:** nonlinear recurrences, adjacent-product invariant, telescoping.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed, including the induction addendum in entry 1. The product recurrence is correct. The addendum runs its induction backward with an awkward base statement; the direct forward formula and nonzero check are cleaner.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Multiplication by the middle term turns the rational recurrence into a constant difference of adjacent products.

## 2005 AIME II Problem 12: A forty-five-degree view of a segment

In square ABCD of side 900 and center O, points E,F lie on AB in that order, with $AE<BF$, $EF=400$, and $\angle EOF=45^\circ$. If $BF=p+q\sqrt r$ with square-free r, find p+q+r.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Put $O=(0,0),A=(-450,450),B=(450,450)$, and write $E=(x,450),F=(x+400,450)$. The cross-product magnitude of OE and OF is 180000, while their dot product is $x(x+400)+202500$. For an angle of $45^\circ$, these are equal, so $x^2+400x+22500=0$. Thus $x=-200\pm50\sqrt7$. Now $AE=x+450$ and $BF=50-x$; the inequality $AE<BF$ requires $x<-200$, selecting the minus sign. Hence $BF=250+50\sqrt7$, and the answer is $307$.

**Answer:** 307.

**Methods:** dot products, cross products, angle constraints.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All ten entries were reviewed. The tangent, rotation, complex, and similarity methods agree. Entry 1 misprints 160000 as 16000; entry 3 has incompatible area and squared-length values; entry 5 swaps endpoint labels; entry 6 mixes a length with its square; entry 8 is only an unfinished recipe; entry 9 mislabels a straight angle and includes a radical typo. The direct vector equation avoids these auxiliary assumptions.

**Archived entries inspected:** 10 of 10. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The cross-product-to-dot-product ratio gives the angle condition without assuming where the side midpoint lies.

## 2005 AIME II Problem 13: Integer polynomial values constrain integer roots

An integer-coefficient polynomial satisfies $P(17)=10$, $P(24)=17$, and $P(n)=n+3$ for two distinct integers $n_1,n_2$. Find $n_1n_2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Neither 17 nor 24 is such a solution. For any integer solution n, the integer-polynomial divisibility rule gives $n-17\mid P(n)-P(17)=n-7$ and $n-24\mid P(n)-P(24)=n-14$. Subtracting the respective divisors shows that both $n-17$ and $n-24$ divide 10. They differ by 7, so among the signed divisors $\pm1,\pm2,\pm5,\pm10$, the only ordered pairs are $(2,-5)$ and $(5,-2)$. Thus the only possible solutions are 19 and 22. Since two distinct solutions are given, their product is $418$.

**Answer:** 418.

**Methods:** integer polynomial congruences, signed divisors.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. Entry 2 gives a valid degree-free argument. Entry 0 writes a quotient A without clarifying it is an integer polynomial rather than a constant; entry 1 assumes P is quadratic without justification. The divisibility proof works for every degree.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Polynomial congruence preservation makes two integer differences divisors of the same small constant.

## 2005 AIME II Problem 15: Tangent-circle centers form an ellipse

Circles $w_1,w_2$ have equations $x^2+y^2+10x-24y-87=0$ and $x^2+y^2-10x-24y+153=0$. Let m be the least positive slope of a line through the origin containing the center of a circle internally tangent to $w_1$ and externally tangent to $w_2$. If $m^2=p/q$ in lowest terms, find p+q.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

The given centers are $F_1=(-5,12),F_2=(5,12)$ with radii 16 and 4. Since the smaller given disk lies strictly inside the larger, the sought circle must itself lie inside the larger; otherwise it could not be externally tangent to the smaller. For center X and radius r, $XF_1=16-r$ and $XF_2=4+r$, so the locus is the ellipse $x^2/100+(y-12)^2/75=1$. Conversely, its focal distances range from 5 to 15, so $r=XF_2-4\in[1,11]$ makes every point a valid center. Substituting $y=ax$ gives $(3+4a^2)x^2-96ax+276=0$. Its discriminant is $48(100a^2-69)$, so a positive-slope line meets the ellipse exactly when $a^2\ge69/100$. Equality is attainable and gives the least slope. Thus $m^2=69/100$, and the answer is $169$.

**Answer:** 169.

**Methods:** ellipse loci, circle tangency, tangent discriminant.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries were reviewed. The discriminant, reflection, calculus, and affine-circle methods agree. The locus equivalence here explicitly checks positive radii and rules out the reversed internal-tangency interpretation; entry 3 has a malformed fraction in its derivative line.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The tangency distances have constant sum, and the least positive slope through the resulting ellipse is determined by a zero discriminant.

## 2006 AIME I Problem 5: Recognizing a squared radical sum

Positive integers $a,b,c$ satisfy $a\sqrt2+b\sqrt3+c\sqrt5=\sqrt{2006+104\sqrt6+468\sqrt{10}+144\sqrt{15}}$. Find $abc$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

The mixed coefficients suggest $ab=52$, $ac=234$, and $bc=72$, giving $a=13$, $b=4$, $c=18$. Direct expansion verifies the identity: the rational term is $2(13)^2+3(4)^2+5(18)^2=2006$, and the mixed terms have the required coefficients. Uniqueness follows from the rational linear independence of $\sqrt2,\sqrt3,\sqrt5$ (apply sign-changing automorphisms in their multiquadratic field). Therefore $abc=936$.

**Answer:** 936.

**Methods:** radical identities.

**Verification:** Exact coefficient expansion of the proposed radical identity.

**Source comparison:** Both entries reviewed. Coefficient matching is valid with radical independence; the second entry has a radicand transcription error in its final identity.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A radical identity is obtained from three pairwise coefficient products.

## 2006 AIME I Problem 6: Uniform digit contributions

Sum all repeating decimals $0.\overline{abc}$ with three distinct decimal digits, allowing $a=0$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

There are $10\cdot9\cdot8=720$ digit strings. In any fixed position each digit occurs $9\cdot8=72$ times. Since $0.\overline{abc}=(100a+10b+c)/999$, the sum is $72(0+\cdots+9)(100+10+1)/999=360$. Distinct triples represent distinct values here.

**Answer:** 360.

**Methods:** contribution counting, digit symmetry.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Digit symmetry counts each contribution to a sum of repeating decimals.

## 2006 AIME I Problem 7: Alternating strips in an angle

An angle has its vertex between parallel lines $L_0,L_1$ in an equally spaced family. Both rays cross $L_1,L_2,\ldots$. Let $A$ be its triangular part before $L_1$ and let $B,C,D$ be its portions between $L_2,L_3$, between $L_4,L_5$, and between $L_6,L_7$, respectively. If $[C]/[B]=11/5$, find $[D]/[A]$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Normalize the line spacing to one and let the vertex be distance $t$ before $L_1$, with $0<t<1$. Similarity makes the area up to a line at distance $u$ from the vertex equal to $cu^2$. Hence $[A]=ct^2$, $[B]=c((t+2)^2-(t+1)^2)=c(2t+3)$, $[C]=c(2t+7)$, and $[D]=c(2t+11)$. The given ratio yields $5(2t+7)=11(2t+3)$, so $t=1/6$. The desired ratio is $(2t+11)/t^2=408$.

**Answer:** 408.

**Methods:** similarity, area differences.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries read. The first two give equivalent similarity arguments. The third has a reversed ratio, mixed-variable typographical errors, and an inconsistent final multiplication.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Similar-triangle area differences form a linear progression.

## 2006 AIME I Problem 9: Integral geometric progressions and logarithms

A geometric progression begins with positive integer $a$ and has positive integer ratio $r$. If $\sum_{k=0}^{11}\log_8(ar^k)=2006$, how many pairs $(a,r)$ exist?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Combining logarithms gives $a^{12}r^{66}=2^{6018}$, or $a^2r^{11}=2^{1003}$. Unique factorization forces $a=2^u$, $r=2^v$ with $u,v\ge0$. Thus $2u+11v=1003$. Exactly the odd values $v=1,3,\ldots,91$ are admissible, and each determines one nonnegative integer $u$. There are $46$ pairs.

**Answer:** 046.

**Methods:** logarithms, prime exponents, linear Diophantine equations.

**Verification:** Exhaustive exponent-pair enumeration within bounds supplied by the exact prime-factor reduction.

**Source comparison:** All three entries reviewed. The exponent argument is correct; the third mistakenly writes the final exponent pair as (541,1) rather than (496,1), and sometimes calls exponents a and r.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. A logarithmic product becomes a two-variable prime-exponent equation.

## 2006 AIME I Problem 12: Factoring a trigonometric cubic

Find the sum of all degree measures $x$ in $(100,200)$ satisfying $\cos^3(3x)+\cos^3(5x)=8\cos^3(4x)\cos^3x$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Put $u=\cos3x$ and $v=\cos5x$. Since $u+v=2\cos4x\cos x$, the equation is $u^3+v^3=(u+v)^3$, equivalent to $uv(u+v)=0$. Therefore at least one of $\cos x,\cos3x,\cos4x,\cos5x$ vanishes. In the prescribed interval their distinct zeros are respectively none; $150$; $112.5,157.5$; and $126,162,198$. Their sum is $906$.

**Answer:** 906.

**Methods:** trigonometric identities, factorization.

**Verification:** Substituted every half-degree candidate into the original trigonometric equation; the analytic factorization establishes exhaustiveness.

**Source comparison:** The sole source uses the same cubic factorization; its listed six roots are complete and distinct.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A product-to-sum identity turns a cubic equation into four cosine factors.

## 2006 AIME I Problem 15: A telescoping potential

Start with $x_0=0$ and choose $x_k$ subject to $|x_k|=|x_{k-1}+3|$. Find the minimum of $|x_1+\cdots+x_{2006}|$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Let $b_k=x_k/3$, so $b_k^2=(b_{k-1}+1)^2$. Summing this identity gives $\sum_{k=1}^{2006}b_k=((b_{2006}+1)^2-2007)/2$. Every $b_k$ is integral. The nearest integer square to $2007$ is $2025$, so the absolute sum is at least $9$. Attain it by alternating $-1,0$ through time $1962$, then taking $44$ successive increments to finish at $b_{2006}=44$. Multiplying by three gives $27$.

**Answer:** 027.

**Methods:** invariants, telescoping, extremal construction.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 2: The proposed attaining sequence alternates two positive values that do not satisfy the recurrence. The telescoping lower bound is valid, but a different construction is necessary. Source 3: The exhibited construction gives the answer but does not prove that a smaller absolute sum is impossible.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. A signed discrete recurrence is optimized through parity and constructive trajectories.

## 2006 AIME II Problem 2: Logarithms as triangle sides

For how many positive integers $n$ do $\log_{10}12$, $\log_{10}75$, and $\log_{10}n$ form the sides of a nondegenerate triangle?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

The triangle criterion for a third side $c$ is $|a-b|<c<a+b$. Here it becomes $\log_{10}(75/12)<\log_{10}n<\log_{10}(12\cdot75)$, or $25/4<n<900$. Thus $n=7,8,\ldots,899$, giving $899-7+1=893$.

**Answer:** 893.

**Methods:** triangle inequality, logarithms.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source has the correct strict bounds. These automatically guarantee positivity of the third side and the remaining triangle inequality.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Strict triangle inequalities become bounds on an integer logarithm argument.

## 2006 AIME II Problem 5: Opposite-face bias

A die assigns probability $1/6+t$ to a face, $1/6-t$ to its opposite, and $1/6$ to the four others; opposite labels sum to seven. Two independent such dice sum to seven with probability $47/288$. Find numerator plus denominator of the larger face probability.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

The sum-seven probability is $4/36+2(1/6+t)(1/6-t)=1/6-2t^2$. Thus $2t^2=1/288$, so $t=1/24$. The larger face probability is $5/24$, giving $29$.

**Answer:** 029.

**Methods:** probability, symmetry.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Independent biased dice yield a probability equation for paired opposite faces.

## 2006 AIME II Problem 6: An axis-parallel square in a right triangle

In unit square $ABCD$, points $E\in BC$ and $F\in CD$ make $AEF$ equilateral. A smaller square lies inside $ABCD$, has vertex $B$, parallel sides, and its opposite vertex on $AE$. Its side is $(a-\sqrt b)/c$ in reduced form with squarefree $b$. Find $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Set $B=(0,0)$, $A=(0,1)$, $C=(1,0)$, $D=(1,1)$ and $E=(t,0)$. From $AE=AF$, the point $F$ is $(1,1-t)$. Then $AE^2=1+t^2$ and $EF^2=2(1-t)^2$, giving $t=2-\sqrt3$ after rejecting the root above one. The line $AE$ is $x/t+y=1$. Its intersection with the diagonal $x=y=s$ gives $s=t/(1+t)=(3-\sqrt3)/6$. Therefore $a+b+c=3+3+6=12$.

**Answer:** 012.

**Methods:** equilateral triangle, line intercepts, inscribed square.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All five entries read. The Pythagorean and similarity methods agree. One trigonometric entry labels original unit sides by the new square side, a notation error avoided here.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. An equilateral condition sets an intercept, then a line intercept equation determines the smaller square.

## 2006 AIME II Problem 9: Intersecting internal common tangents

Circles with centers $(0,0),(12,0),(24,0)$ have radii $1,2,4$. The first two have a common internal tangent of positive slope; the last two have one of negative slope. Their intersection has $x$-coordinate $p-q\sqrt r$ in reduced squarefree form. Find $p+q+r$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

An internal tangent crosses the centers' line in the ratio of the radii. Thus the first tangent crosses at $x=4$ and the second at $x=16$. If their inclinations have absolute values $\alpha,\beta$, then $\sin\alpha=(1+2)/12=1/4$ and $\sin\beta=(2+4)/12=1/2$. Their equations are $y=(x-4)/\sqrt{15}$ and $y=-(x-16)/\sqrt3$. Solving gives $x=(16\sqrt5+4)/(\sqrt5+1)=19-3\sqrt5$. The answer is $19+3+5=27$.

**Answer:** 027.

**Methods:** circle tangency, homothety centers.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source reaches the same tangent equations through several auxiliary right triangles; the inclination formula shortens the computation.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Signed center distances determine the two tangent equations.

## 2006 AIME II Problem 11: A telescoping tribonacci sum

Let $a_1=a_2=a_3=1$ and $a_{n+3}=a_{n+2}+a_{n+1}+a_n$. Given $a_{28}=6090307$, $a_{29}=11201821$, and $a_{30}=20603361$, find $\sum_{k=1}^{28}a_k$ modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Define $b_n=(a_n+a_{n+2})/2$. Then $b_1=1$ and the recurrence gives $b_{n+1}-b_n=(a_{n+1}+a_{n+3}-a_n-a_{n+2})/2=a_{n+1}$. Hence $b_n=\sum_{k=1}^n a_k$ by telescoping. The required sum is $(6090307+20603361)/2=13346834$, so the remainder is $834$.

**Answer:** 834.

**Methods:** linear recurrence, telescoping.

**Verification:** Generated all 30 terms from the original recurrence and directly summed the first 28.

**Source comparison:** All three entries read. The telescoping derivation and direct modular calculation are valid; the coefficient-guessing entry checks only initial cases and needs the invariant proof supplied here.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A fixed linear combination of nearby recurrence terms gives a partial sum.

## 2006 AIME II Problem 15: A radical system encoding triangle altitudes

Real numbers satisfy $x=\sqrt{y^2-1/16}+\sqrt{z^2-1/16}$, $y=\sqrt{z^2-1/25}+\sqrt{x^2-1/25}$, and $z=\sqrt{x^2-1/36}+\sqrt{y^2-1/36}$. If $x+y+z=m/\sqrt n$ with squarefree $n$ and positive integers $m,n$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

The equations imply $x,y,z>0$ and the strict triangle inequalities. In the first equation, the two nonnegative radicals are the projections of sides $y,z$ onto a base of length $x$, giving a triangle of height $1/4$. The other equations construct congruent triangles with heights $1/5$ and $1/6$ over the other sides. If their common area is $K$, then $x=8K$, $y=10K$, $z=12K$. Heron's formula now yields $K^2=(15K)(7K)(5K)(3K)=1575K^4$, so $K=1/(15\sqrt7)$ and $x+y+z=2/\sqrt7$. These sides form an acute $4:5:6$ triangle, so all projection signs agree with the original radicals. The answer is $9$.

**Answer:** 009.

**Methods:** triangle altitudes, Heron formula, radical systems.

**Verification:** Numerically substituted the proposed solution into all three original radical equations, including radical signs.

**Source comparison:** Both entries read. The geometric source proves triangle existence but does not fully justify its initial acute-angle assumption; the projection construction here supplies that missing link. The algebraic elimination offers an independent symmetric-polynomial derivation.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Each radical equation constructs an altitude of the same triangle.

## 2007 AIME I Problem 2: Three moving positions

A length-$100$ walkway moves at $6$ feet per second. Al stands on it from time $0$. Bob enters at time $2$ and walks forward at $4$ feet per second relative to it. Cy starts beside it at time $4$, walking at $8$ feet per second. When one is midway between the others, how far from the start is that person?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

After time $4$, their positions are $A=6t$, $B=10t-20$, and $C=8t-32$. The three possible midpoint equations give: $2A=B+C$ implies $t=26/3$; $2B=A+C$ implies $t=4/3$, outside the domain; and $2C=A+B$ is impossible. At $t=26/3$, all positions remain between $0$ and $100$, and Al is at $6t=52$.

**Answer:** 052.

**Methods:** linear motion, midpoint equations.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The single source checks all three midpoint choices. Its preliminary guess about ordering is unnecessary once the three equations are solved.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Linear position functions determine which traveler can be the midpoint.

## 2007 AIME I Problem 3: Equal imaginary parts

For $z=9+bi$ with $b>0$, the numbers $z^2$ and $z^3$ have equal imaginary parts. Find $b$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

The imaginary parts are $18b$ and $243b-b^3$. Equality and $b>0$ give $b^2=225$, hence $b=15$.

**Answer:** 015.

**Methods:** complex numbers.

**Verification:** Direct complex-power evaluation of the proposed positive imaginary part.

**Source comparison:** The sole source correctly discards the zero and negative roots.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Expansion of two complex powers yields a cubic in the imaginary coordinate.

## 2007 AIME I Problem 4: The next planetary alignment

Three coplanar planets travel uniformly in circular orbits in the same direction, with periods $60,84,140$ years. They and the central star are initially collinear. After how many years will this first recur?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Collinearity permits angular differences that are integral multiples of $\pi$, regardless of which side of the star a planet occupies. Consecutive relative angular speeds are $2\pi(1/60-1/84)=\pi/105$ and $2\pi(1/84-1/140)=\pi/105$. Thus both required differences are integral half-turns exactly when $t/105$ is an integer. The first positive time is $105$.

**Answer:** 105.

**Methods:** relative angular speed, periodicity.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source correctly works modulo a half-turn, rather than requiring every planet to return to its initial location.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Relative angular speeds lead to a common half-turn period.

## 2007 AIME I Problem 7: A floor-ceiling logarithm indicator

Find $\sum_{k=1}^{1000}k(\lceil\log_{\sqrt2}k\rceil-\lfloor\log_{\sqrt2}k\rfloor)$ modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

The parenthesis is zero when the logarithm is integral and one otherwise. If $k=(\sqrt2)^m$ is an integer, then $m$ is even, so these exceptions are exactly $1,2,4,\ldots,512$. The sum is therefore $1000\cdot1001/2-(2^{10}-1)=499477$, with remainder $477$.

**Answer:** 477.

**Methods:** floor and ceiling, indicator functions.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source identifies the same exceptions; the parity of the exponent explicitly justifies why odd powers of the square root cannot occur.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. The floor-ceiling difference deletes precisely the powers of two from an arithmetic sum.

## 2007 AIME I Problem 8: Two quadratic factors of a cubic

For what largest real $k$ can both $x^2+(k-29)x-k$ and $2x^2+(2k-43)x+k$ divide a cubic polynomial?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

The two quadratics must share a root $r$, since otherwise their least common multiple has degree four. Subtracting twice the first equation from the second gives $15r+3k=0$, so $r=-k/5$. Substitution yields $-4k(k-30)/25=0$, giving $k=0$ or $30$. At $k=30$, the factors are $(x+6)(x-5)$ and $(x+6)(2x+5)$; their product with the shared factor counted once is cubic. Thus the maximum is $30$.

**Answer:** 030.

**Methods:** polynomial gcd, elimination.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries reviewed. Common-root elimination is complete. The Vieta and coefficient-comparison alternatives divide by k or a common root and consequently omit k=0, harmless only because the question asks for the maximum.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A degree bound forces a common factor, detected by elimination.

## 2007 AIME I Problem 12: Overlap of two rotated isosceles triangles

Let $A=(0,0)$, $B=(20,0)$, and let $C$ lie in the first quadrant with $AC=BC$ and $\angle BAC=75^\circ$. Rotate the triangle counterclockwise until $C$ reaches the positive vertical axis. If the common area is $p\sqrt2+q\sqrt3+r\sqrt6+s$, find $(p-q+r-s)/2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

The rotation is $15^\circ$; denote the new vertices by $B_1,C_1$. Put $D=AC\cap B_1C_1$, $E=BC\cap B_1C_1$, and $F=BC\cap AB_1$. The overlap is $ADEF$, obtained from triangle $ADB_1$ by removing $EFB_1$. The first triangle has angles $60^\circ,75^\circ,45^\circ$ and side $AB_1=20$, so its area is $20^2\sin60^\circ\sin75^\circ/(2\sin45^\circ)=150+50\sqrt3$. Since $AF\perp BC$, $AF=20\cos15^\circ=5(\sqrt6+\sqrt2)$. Therefore $[EFB_1]=\frac12(20-5\sqrt6-5\sqrt2)^2\tan75^\circ=750+400\sqrt3-500\sqrt2-300\sqrt6$. Subtraction gives the common area $500\sqrt2-350\sqrt3+300\sqrt6-600$, and the requested value is $875$.

**Answer:** 875.

**Methods:** rotation, polygon intersection, trigonometric area.

**Verification:** Independently clipped the original and rotated triangles numerically and compared their polygon area with the radical expression.

**Source comparison:** All five entries reviewed, including the diagram-only entry. The first dissection and coordinate equations support the result. The second has a malformed intermediate denominator; the third duplicates and then loses an area term in its final simplification.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The overlap is a larger triangle with one right triangular corner removed.

## 2007 AIME I Problem 14: Linearizing a nonlinear recurrence

Let $a_0=a_1=3$ and $a_{n+1}a_{n-1}=a_n^2+2007$ for $n\ge1$. Find $\left\lfloor(a_{2006}^2+a_{2007}^2)/(a_{2006}a_{2007})\right\rfloor$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

For positive adjacent terms $u,v$, let $H(u,v)=(u^2+v^2+2007)/(uv)$. Substitution of the next term $w=(v^2+2007)/u$ shows $H(v,w)=H(u,v)$. Thus every adjacent pair has $H=H(3,3)=225$. The sequence is positive and nondecreasing, since $v\ge u>0$ implies $(v^2+2007)/u>v$. Moreover $a_1a_2=3\cdot672=2016>2007$. Therefore for every $n\ge1$, $0<2007/(a_na_{n+1})<1$, and the requested expression is $225-2007/(a_{2006}a_{2007})$, whose floor is $224$.

**Answer:** 224.

**Methods:** invariants, nonlinear recurrence, linearization.

**Verification:** Generated 20 exact nonlinear-recurrence steps and checked the floor and invariant; the proof extends them to index 2006.

**Source comparison:** All six entries reviewed. The invariant and telescoping methods are sound after minor index repairs. The matrix entry has an incorrect final denominator; the generalized proof omits a divisor in one monotonicity line. The final asymptotic argument is not a proof and even misstates the initial values.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A conserved rational expression gives a sharp floor without computing large terms.

## 2007 AIME I Problem 15: An inscribed sixty-degree triangle

In equilateral triangle $ABC$, points $F\in AB$, $D\in BC$, and $E\in CA$ satisfy $AF=5$, $CD=2$, $\angle DEF=60^\circ$, and $[DEF]=14\sqrt3$. The two possible side lengths are $p\pm q\sqrt r$ with rational $p,q$ and squarefree integer $r$. Find $r$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Write $AB=x$ and $AE=y$. Subtracting the three corner triangles from $ABC$ gives $x^2=5y+(x-5)(x-2)+2(x-y)+56$, hence $3y=5x-66$. Angle chasing using $\angle DEF=60^\circ$ gives $\triangle AEF\sim\triangle CDE$, so $5/(x-y)=y/2$, or $y(x-y)=10$. Eliminating $y$ produces $10x^2-462x+4446=0$, whence $x=(231\pm3\sqrt{989})/10$. Both roots have $x>5$ and $0<y<x$; conversely the product relation gives the corner-triangle similarity by SAS and thus the required angle, so both configurations exist. Since $989=23\cdot43$, the answer is $989$.

**Answer:** 989.

**Methods:** area decomposition, similarity, quadratic discriminant.

**Verification:** Constructed both candidate triangles in coordinates and independently checked the 60-degree angle, prescribed area, and segment placements.

**Source comparison:** Both entries reviewed. The first provides the efficient area-and-similarity reduction. The second chooses a radical sign without accounting for both configurations; the present argument verifies both roots geometrically.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Area decomposition and angle-induced similarity yield a quadratic for the outer side.

## 2007 AIME II Problem 4: Worker-hours as an additive resource

Identical workers produce two products at fixed per-item labor costs. In one hour, $100$ workers make $300$ of the first and $200$ of the second. In two hours, $60$ workers make $240$ and $300$. In three hours, $50$ workers make $150$ of the first and $m$ of the second. Find $m$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Let $u,v$ be worker-hours per item. Then $300u+200v=100$ and $240u+300v=120$, giving $u=1/7$, $v=2/7$. The last production run uses $150$ worker-hours, so $150/7+2m/7=150$. Thus $m=450$.

**Answer:** 450.

**Methods:** linear systems, work rates.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The single source correctly treats total worker-hours as the conserved resource.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Two production measurements identify the unit labor costs.

## 2007 AIME II Problem 7: Multiples inside a cube-root interval

Exactly $70$ positive integers $n$ satisfy both $\lfloor\sqrt[3]n\rfloor=k$ and $k\mid n$ for some integer $k$. Find the largest possible value of $n/k$ among them.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Necessarily $k\ge1$. The multiples lie from $k^3$ through $(k+1)^3-1=k(k^2+3k+3)$, inclusive, with step $k$. Their number is $k^2+3k+3-k^2+1=3k+4$. Hence $k=22$, and the largest quotient is $k^2+3k+3=553$.

**Answer:** 553.

**Methods:** floor functions, arithmetic progressions.

**Verification:** Directly enumerated the cube-root intervals through k=39; the analytic count proves no further k works.

**Source comparison:** Both entries reviewed. The direct endpoint count and two-sided inequality yield the same unique value of k.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Exact endpoints count a short arithmetic progression.

## 2007 AIME II Problem 8: Optimizing a rectangular grid

Draw full lines parallel to the sides of a $4\times5$ sheet, with total drawn length $2007$. Basic rectangles must have four drawn sides and no drawn line inside. Find the maximal number modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

With $h$ lines of length $5$ and $v$ of length $4$, we have $5h+4v=2007$ and $(h-1)(v-1)$ basic rectangles. Thus $h\equiv3\pmod4$ and the objective is the concave quadratic $(h-1)(2003-5h)/4$, centered at $h=1004/5$. The two nearest permissible values are $199,203$, giving $49896$ and $49894$. Concavity excludes all others. The answer is $896$.

**Answer:** 896.

**Methods:** grid counting, discrete optimization.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. A product of interval counts is optimized under a linear line-length constraint.

## 2007 AIME II Problem 11: Rolling over a smaller cylinder

A radius-$72$ cylinder rolls along a plane, over a fixed parallel radius-$24$ cylinder, and back onto the plane without slipping. After exactly one complete rotation, its horizontal displacement is $a\pi+b\sqrt c$, with integer coefficients and squarefree $c$. Find $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

At first and last contact with the small cylinder, the center separation is $96$ and the vertical difference is $48$. Thus each horizontal offset is $48\sqrt3$, and the large center traverses an angle $2\pi/3$ around the small center. On this arc its speed is $96\dot\theta$. No slipping makes its spin speed $96\dot\theta/72$, so this portion consumes rolling length $96(2\pi/3)=64\pi$ from the total one-revolution length $144\pi$. The remaining flat travel is $80\pi$, while the obstacle crossing contributes horizontal distance $96\sqrt3$. Hence the answer is $80+96+3=179$.

**Answer:** 179.

**Methods:** rolling without slipping, circular motion.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The source correctly combines the two large-circle angular contributions with the small-circle arc. The instantaneous velocity relation here makes the no-slip accounting explicit.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. No-slip rotation relates center-arc travel to the consumed revolution.

## 2007 AIME II Problem 12: The largest term controls a geometric sum

An increasing geometric sequence consists of integral powers of $3$. It satisfies $\sum_{j=0}^{7}\log_3x_j=308$ and $56\le\log_3(\sum_{j=0}^{7}x_j)\le57$. Find $\log_3x_{14}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Write $x_j=3^{a+jd}$ with integers $a$ and $d\ge1$. The first condition gives $2a+7d=77$. If $M=a+7d$, the sum satisfies $3^M<S<3^M\sum_{j=0}^{\infty}3^{-j}=\frac32\,3^M$. Since $3^{56}\le S\le3^{57}$, an integer $M\le55$ is too small and $M\ge57$ is too large. Thus $M=56$. Solving yields $a=21$, $d=5$, so $a+14d=91$.

**Answer:** 091.

**Methods:** geometric sums, logarithms, dominant term bounds.

**Verification:** Exact large-integer substitution of the proposed progression into both original conditions.

**Source comparison:** All four entries reviewed. The base-three and geometric-tail ideas are sound. The first uses an approximation where a bound is needed; the last repeatedly discards small terms and does not establish uniqueness. The strict tail bound repairs both issues and also permits negative initial exponents.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. A geometric tail bound fixes the leading exponent exactly.

## 2007 AIME II Problem 14: A polynomial identity controlled by its roots

A real polynomial satisfies $f(0)=1$, $f(2)+f(3)=125$, and $f(x)f(2x^2)=f(2x^3+x)$ identically. Find $f(5)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

The polynomial is nonconstant, and comparison of leading coefficients makes it monic. If $z$ is a root, so is $T(z)=2z^3+z$. A root with $|z|>1$ would generate infinitely many roots of increasing modulus, because $|T(z)|\ge2|z|^3-|z|>|z|$. Thus all roots have modulus at most one. Their product has modulus $|f(0)|=1$, so each has modulus one. Its image also has modulus one, giving $1=|2z^2+1|^2=5+4\operatorname{Re}(z^2)$. Hence $z^2=-1$. Real coefficients pair the roots equally, so $f(x)=(x^2+1)^n$. This form satisfies the identity. Since $5^n+10^n=125$ and this sum increases strictly with $n\ge0$, $n=2$. Therefore $f(5)=26^2=676$.

**Answer:** 676.

**Methods:** polynomial functional equations, root dynamics, complex modulus.

**Verification:** Checked the proposed polynomial identity at 41 integer inputs, more than its degree, and both numerical conditions; classification uniqueness remains analytic.

**Source comparison:** All three entries reviewed, including the corrective comment in the second. The first root-product argument is rigorous. The second initial descent assumes f(-2) is not one without proof; its comment offers a repair. The third incorrectly infers a strict upper bound from a lower-bound triangle inequality for roots inside the unit disk.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Root dynamics and the constant coefficient force all roots to be plus or minus i.

## 2008 AIME I Problem 1: Changing a percentage by adding students

Initially a party is $60\%$ girls, and $40\%$ of attendees like dancing. Twenty more boys arrive, all liking dancing, and the party becomes $58\%$ girls. How many attendees now like dancing?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

If there were initially $N$ attendees, the unchanged number of girls gives $0.60N=0.58(N+20)$, so $N=580$. The new number liking dancing is $0.40(580)+20=252$.

**Answer:** 252.

**Methods:** percentages, linear equations.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries reviewed. The first three are equivalent population equations. The fourth introduces an unnecessary special distribution of preferences; only the totals are relevant.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. An unchanged subgroup determines the original population.

## 2008 AIME I Problem 3: Integer speeds from two distance totals

Biking, jogging, and swimming speeds $b,j,s$ are positive integers. A two-hour bike ride, three-hour jog, and four-hour swim cover $74$ km; four hours biking, two jogging, and three swimming cover $91$ km. Find $b^2+j^2+s^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

The equations are $2b+3j+4s=74$ and $4b+2j+3s=91$. Elimination gives $s=125-8b$ and $j=10b-142$. Positivity forces $14.2<b<15.625$, so the integer $b$ must be $15$. Then $j=8$, $s=5$, and the required sum is $225+64+25=314$.

**Answer:** 314.

**Methods:** integer linear systems, positivity bounds.

**Verification:** Exhaustively checked all positive integral rates within bounds from the first distance equation.

**Source comparison:** All four entries reviewed. The first two rigorously isolate the solution. The third contains parity errors and unjustified congruence steps; the fourth appeals to plausible athletic speeds rather than proving uniqueness.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Positivity sharply bounds the single free parameter in an integer linear system.

## 2008 AIME I Problem 4: A shifted difference of squares

Positive integers $x,y$ satisfy $x^2+84x+2008=y^2$. Find $x+y$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Completing the square gives $(y-x-42)(y+x+42)=244$. Both factors are positive and have the same parity. As $244=4\cdot61$, the only same-parity positive factor pair is $(2,122)$. Hence $y=62$, $x=18$, and $x+y=80$.

**Answer:** 080.

**Methods:** difference of squares, factor pairs.

**Verification:** Direct square test through the factorization-derived global bound, finding the unique positive solution.

**Source comparison:** All six entries read. The factorization proof is complete. Several alternatives merely test candidates or invoke the stated uniqueness. The fifth has a sign error in its expansion; the last writes x=12 even though its own relation gives x=18.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Completing the square reduces the equation to same-parity factor pairs.

## 2008 AIME I Problem 8: An arctangent sum through complex multiplication

Find positive integer $n$ for which $\arctan(1/3)+\arctan(1/4)+\arctan(1/5)+\arctan(1/n)=\pi/4$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

The product $(3+i)(4+i)(5+i)=48+46i$ has argument equal to the sum of the first three angles, which is acute. Its tangent is $23/24<1$, so this sum is below $\pi/4$. Multiplying by $n+i$ gives real and imaginary parts $48n-46$ and $46n+48$. Equality of these parts yields $n=47$. Both parts are positive then, so the argument is exactly $\pi/4$, and the positive missing angle ensures uniqueness.

**Answer:** 047.

**Methods:** complex arguments, arctangent identities.

**Verification:** Direct numerical evaluation of the original four arctangents.

**Source comparison:** All four entries reviewed. Sequential tangent addition and Gaussian-integer multiplication are valid. The four-angle entry interchanges the tangent numerator and denominator; equality to one happens to conceal the error. The last entry is an unfinished sketch.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Multiplying Gaussian integers adds their arguments.

## 2008 AIME I Problem 10: A trapezoid forced by equality bounds

An isosceles trapezoid $ABCD$ has longer base $AD\parallel BC$, base angles $60^\circ$, and diagonals $10\sqrt{21}$. A point $E$ satisfies $EA=10\sqrt7$, $ED=30\sqrt7$. If $F$ is the perpendicular projection of $C$ onto $AD$, write $EF=m\sqrt n$ in squarefree form and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

Write $AD=x$, $CD=y$. The two distances from $E$ imply $x\ge ED-EA=20\sqrt7$. The cosine rule in $ADC$ gives $2100=x^2+y^2-xy=(y-x/2)^2+3x^2/4$, so $x\le20\sqrt7$. Equality holds in both bounds: $y=x/2=10\sqrt7$, and $E,A,D$ are collinear in that order. Since $DF=y\cos60^\circ=5\sqrt7$, we get $AF=15\sqrt7$ and $EF=25\sqrt7$. The answer is $32$.

**Answer:** 032.

**Methods:** equality cases, law of cosines, reverse triangle inequality.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries reviewed. The first gives the essential tight bounds. The second assumes the incorrect length AD=40 sqrt(7) and unsupported right-triangle angles, so it does not establish the result.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A reverse triangle inequality meets a quadratic discriminant bound.

## 2008 AIME I Problem 12: Maximum traffic through a fixed point

All cars are $4$ meters long and travel at common speed $v>0$ km/h. The gap behind each car is exactly $4\lceil v/15\rceil$ meters. A roadside detector counts passing cars for one hour. Over all speeds and initial placements, let $M$ be the largest possible whole count. Find the integer quotient $M/10$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Put $n=\lceil v/15\rceil$. Consecutive fronts cross at intervals $\delta=4(n+1)/(1000v)\ge(n+1)/(3750n)>1/3750$ hours. Thus $3751$ crossings would span $3750\delta>1$ hour and are impossible. Conversely choose $v=15n$ with $n=3750$. Then $3749\delta=3749\cdot3751/(3750^2)<1$, so an initial phase places $3750$ consecutive crossings strictly within the hour. Therefore $M=3750$, and the requested quotient is $375$.

**Answer:** 375.

**Methods:** interval packing, ceiling functions, throughput.

**Verification:** Exact crossing-span check for the attaining finite speed; the analytic headway bound excludes 3751 at every speed.

**Source comparison:** All three entries reviewed. The first recognizes the endpoint-count issue, though it phrases it using partial units. The second omits car length from the headway; the third uses floor instead of ceiling for nonmultiple speeds. The exact crossing-span proof resolves these ambiguities.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, combinatorics. A discrete crossing count depends on headway and the initial phase, not just limiting flow rate.

## 2008 AIME I Problem 13: A common zero of a two-dimensional cubic family

Every polynomial $p(x,y)$ of total degree at most three under consideration vanishes at $(0,0),(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(2,2)$. Find the positive nonintegral common zero $(a/c,b/c)$, with positive integers $a,b,c$, $\gcd(a,c)=1$, $c>1$, by reporting $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

The five axis conditions and the two points with $x=1$ reduce the polynomial to $p=\alpha(x-x^3)+\beta(y-y^3)+\gamma xy(1-x)$. The point $(2,2)$ imposes $3\alpha+3\beta+2\gamma=0$. Hence a universal zero must annihilate both coefficients after setting $\gamma=-3(\alpha+\beta)/2$. Since $x>0$ is nonintegral, the first coefficient gives $y=2(x+1)/3$. Since $y>0$, the second gives $y^2-1=3x(x-1)/2$. Substitution yields $(19x-5)(x-2)=0$. Rejecting integral $x=2$ leaves $x=5/19$, $y=16/19$. These values annihilate both coefficients, proving sufficiency. Thus $a+b+c=40$.

**Answer:** 040.

**Methods:** polynomial interpolation, linear algebra, common zeros.

**Verification:** Exact substitution into both independently variable basis coefficients; the analytic elimination proves this basis spans the constrained family.

**Source comparison:** All three entries reviewed. Coefficient elimination gives a complete two-parameter family. The geometric-basis entry has expansion and denominator typos and does not prove its chosen polynomials span the family; the explicit reduction here supplies that requirement.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Linear conditions reduce a bivariate cubic family to two basis polynomials.

## 2008 AIME I Problem 14: Maximizing a tangent projection distance

Circle $\omega$ has diameter $AB=18$. A point $C$ lies beyond $A$ on ray $BA$, and $CT$ is tangent to the circle. Let $P$ be the perpendicular projection of $A$ onto $CT$. If $m$ is the largest possible $BP$, find $m^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Let $O$ be the center and let $\theta$ be the acute angle between $CA$ and the tangent. Write $u=\sin\theta=9/OC$, so $0<u<1$. If $Q$ is the perpendicular projection of $B$ onto the tangent, then $BQ=9(1+u)$ and $PQ=18\cos\theta$. Therefore $BP^2=81(1+u)^2+324(1-u^2)=81(5+2u-3u^2)=432-243(u-1/3)^2$. Equality occurs at $u=1/3$, corresponding to $OC=27$, so $m^2=432$.

**Answer:** 432.

**Methods:** tangent projections, quadratic optimization.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries reviewed; the external forum link in entry four was not opened. The trigonometric quadratic and reciprocal-distance methods are sound. Entry four has a squared-variable typo in AP; the final entry overstates the admissible altitude range, though its optimizer is feasible.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A tangent-line coordinate system makes the squared distance a concave quadratic.

## 2008 AIME II Problem 1: Paired alternating squares

Find the remainder modulo $1000$ of $100^2+99^2-98^2-97^2+96^2+95^2-\cdots+4^2+3^2-2^2-1^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

For each $j=1,\ldots,25$, the four-term block is $(4j)^2+(4j-1)^2-(4j-2)^2-(4j-3)^2=32j-12$. Therefore the sum is $32(25\cdot26/2)-12\cdot25=10100$, whose remainder is $100$.

**Answer:** 100.

**Methods:** finite differences, arithmetic sums.

**Verification:** Directly evaluated all 100 signed square terms.

**Source comparison:** All four entries reviewed. Their regroupings are valid; the third writes a quotient where a remainder is intended in its final display.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Grouping four terms turns quadratic terms into an arithmetic progression.

## 2008 AIME II Problem 2: Equal arrival times with different rest schedules

Two cyclists start together on a $50$-mile trip. The faster rider rests five minutes after each mile, and the slower rider, traveling at three-quarters the faster speed, rests five minutes after each two miles. They reach the finish together. How many minutes elapse?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

No rest after arrival counts. Thus the faster rider rests $49\cdot5=245$ minutes, and the slower rests $24\cdot5=120$. If the faster moving time is $t$, the slower moving time is $4t/3$. Equal arrival gives $t+245=4t/3+120$, so $t=375$ and total elapsed time is $620$.

**Answer:** 620.

**Methods:** rates, linear equations.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries reviewed. Each correctly excludes the break at the finish.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Rest counts convert a speed ratio into an equation for elapsed time.

## 2008 AIME II Problem 3: Ten slices from a rectangular block

A $10\times13\times14$ rectangular solid loses ten slices, each one unit thick and parallel to a face of the remaining block. What is the largest possible remaining volume?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

Every slice reduces one dimension by one. Thus the remaining positive dimensions $a,b,c$ satisfy $a+b+c=10+13+14-10=27$. AM-GM yields $abc\le9^3=729$. Cutting one unit from the first dimension, four from the second, and five from the third produces a $9\times9\times9$ cube, so the bound is attained.

**Answer:** 729.

**Methods:** AM-GM, geometric optimization.

**Verification:** Exhaustively enumerated every nonnegative allocation of the ten unit slices with a positive remaining first dimension.

**Source comparison:** Both entries reviewed. The AM-GM proof is complete; the greedy alternative lists a successful path but leaves its global optimality assertion unstated.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. A fixed sum of remaining dimensions makes AM-GM sharp.

## 2008 AIME II Problem 6: A factorial recurrence in disguise

Sequences satisfy $a_0=a_1=1$, $b_0=1$, $b_1=3$, and both obey $u_n=u_{n-1}+u_{n-1}^2/u_{n-2}$ for $n\ge2$. Find $b_{32}/a_{32}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

All terms are positive. Dividing the recurrence by $u_{n-1}$ gives $u_n/u_{n-1}=1+u_{n-1}/u_{n-2}$. Hence $a_n/a_{n-1}=n$ and $b_n/b_{n-1}=n+2$. Multiplication yields $a_n=n!$ and $b_n=(n+2)!/2$. Thus $b_{32}/a_{32}=34\cdot33/2=561$.

**Answer:** 561.

**Methods:** ratio substitution, factorials.

**Verification:** Generated both original rational recurrences exactly through index 32 without using factorial formulas.

**Source comparison:** The sole source identifies the same arithmetic progression of ratios and resulting factorial forms.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Ratios of adjacent terms form an arithmetic progression.

## 2008 AIME II Problem 7: Cubes of pairwise root sums

Let $r,s,t$ be the roots, with multiplicity, of $8x^3+1001x+2008=0$. Find $(r+s)^3+(s+t)^3+(t+r)^3$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Vieta gives $r+s+t=0$, so the target is $-(r^3+s^3+t^3)$. Summing the defining polynomial equation over the three roots gives $8(r^3+s^3+t^3)+1001(r+s+t)+3\cdot2008=0$. Thus the target is $3\cdot2008/8=753$.

**Answer:** 753.

**Methods:** Vieta formulas, Newton sums.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All ten entries reviewed; the linked Newton-sums article was not opened. Root substitution gives the shortest proof. Several expanded alternatives contain intermediate sign or missing-term errors; in particular the transformed-root product is positive 251, not negative, and the final long expansion is unreliable.

**Archived entries inspected:** 10 of 10. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The missing quadratic coefficient makes each pair sum the negative third root.

## 2008 AIME II Problem 8: A trigonometric telescope and divisibility

Put $a=\pi/2008$. Find the smallest positive integer $n$ for which $2\sum_{k=1}^{n}\cos(k^2a)\sin(ka)$ is an integer.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Product-to-sum gives $2\cos(k^2a)\sin(ka)=\sin(k(k+1)a)-\sin(k(k-1)a)$. The sum therefore equals $\sin(n(n+1)\pi/2008)$. An integer sine must be $-1,0,$ or $1$, so its argument must be a multiple of $\pi/2$. Thus $1004=4\cdot251$ must divide $n(n+1)$. The prime $251$ forces the first candidate to be $n=250$, but $250\cdot251$ is not divisible by four. The next candidate $n=251$ works because $252$ is divisible by four. Hence the answer is $251$.

**Answer:** 251.

**Methods:** telescoping, trigonometric identities, divisibility.

**Verification:** Directly summed the original trigonometric series at every candidate index through 251.

**Source comparison:** Both entries reviewed. The complex-exponential derivation is equivalent to product-to-sum and has a cubic exponent typo in one expanded telescoping line.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Quadratic-angle product-to-sum terms telescope to one sine.

## 2008 AIME II Problem 9: An affine rotation with period eight

Start at $(5,0)$. A move rotates the point counterclockwise by $45^\circ$ about the origin and then translates it ten units right. After $150$ moves the point is $(p,q)$. Find $\lfloor|p|+|q|\rfloor$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Identify the plane with complex numbers and let $\zeta=e^{i\pi/4}$. A move is $z\mapsto\zeta z+10$. Since $\zeta^8=1$ and $\sum_{j=0}^{7}\zeta^j=0$, eight moves are the identity. Thus $150$ moves equal six, giving $z=5\zeta^6+10\sum_{j=0}^{5}\zeta^j=5(-i)-10(\zeta^6+\zeta^7)=-5\sqrt2+(5+5\sqrt2)i$. Therefore $|p|+|q|=5+10\sqrt2$. The inequalities $1.4<\sqrt2<1.5$ give $19<5+10\sqrt2<20$, so the answer is $19$.

**Answer:** 019.

**Methods:** affine rotations, roots of unity.

**Verification:** Numerically applied all 150 original rotation-and-translation moves.

**Source comparison:** All four entries reviewed; the external Desmos link was not opened. The periodicity is correct. The second has a summation-index error, the fixed-center entry calls a positive-angle rotation clockwise, and the matrix entry asserts false pairwise cancellations even though the full eight-term sum is zero.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The sum of eighth roots of unity annihilates the translation over one period.

## 2008 AIME II Problem 11: Two tangent circles along an isosceles base

Triangle $ABC$ has $AB=AC=100$, $BC=56$. A radius-$16$ circle touches $AC$ and $BC$. Another circle lies entirely inside the triangle, touches $AB$ and $BC$, and is externally tangent to the first circle. Its radius is $m-n\sqrt k$ with squarefree $k$. Find $m+nk$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Choose $B=(-28,0)$, $C=(28,0)$, $A=(0,96)$. Half the base angle has tangent $3/4$, so the first center is $(20/3,16)$ and the second is $(-28+4r/3,r)$. External tangency gives $((104-4r)/3)^2+(16-r)^2=(16+r)^2$, or $(26-r)^2=36r$. Thus $r=44\pm6\sqrt{35}$. Every contained circle has radius at most the inradius $2688/128=21$, excluding the plus sign. The smaller root is positive and below 21, and its corner circle consequently lies inside all three side half-planes. The answer is $44+6\cdot35=254$.

**Answer:** 254.

**Methods:** tangent circles, half-angle ratios.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries reviewed. The first and incenter-based third are sound. The second is garbled and dimensionally inconsistent; the fourth contains incorrect numerators in both its similarity ratio and final base-length equation.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Angle-bisector offsets and the external tangency distance produce a quadratic radius equation.

## 2008 AIME II Problem 13: Inverting the exterior of a regular hexagon

A regular hexagon centered at $0$ in the complex plane has opposite sides one unit apart, including a pair parallel to the imaginary axis. Let $S=\{1/z:z\text{ is outside the hexagon}\}$. If its area is $a\pi+\sqrt b$, find $a+b$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

In the angular sector $-\pi/6\le\theta\le\pi/6$, the original boundary is $r\cos\theta=1/2$. Reciprocal inversion reflects the angle and sends the exterior radial interval to $0<\rho\le2\cos\theta$. Thus its boundary arc belongs to the unit circle centered at $(1,0)$. Rotating by multiples of $60^\circ$ gives the six boundary arcs. Their endpoints form a regular hexagon of circumradius $\sqrt3$, with area $9\sqrt3/2$. Each outward circular segment has central angle $120^\circ$, hence area $\pi/3-\sqrt3/4$. Adding six segments gives $2\pi+3\sqrt3=2\pi+\sqrt{27}$. Therefore $a+b=29$.

**Answer:** 029.

**Methods:** complex inversion, circular segments.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries reviewed. The inversion sketch, circular-segment construction, and polar integral agree. The geometric entry misstates the centers as angles k*pi/6; the six centers are spaced by pi/3. Boundary and omitted-origin conventions do not affect area.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Reciprocal inversion turns the six supporting lines into six unit-circle arcs.

## 2008 AIME II Problem 14: An equilateral constraint inside a rectangle

For $a\ge b>0$, suppose $a^2+y^2=b^2+x^2=(a-x)^2+(b-y)^2$ has a solution with $0\le x<a$, $0\le y<b$. Let $\rho$ be the largest possible $a/b$. If $\rho^2=m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Let the common value be $L$. Expanding the last square gives $L=2L-2(ax+by)$, so $L=2ax+2by$. Since $2by\ge y^2$, the equality $a^2+y^2=2ax+2by$ implies $x\le a/2$. Also $b^2+x^2=a^2+y^2\ge a^2$, hence $b^2\ge a^2-x^2\ge3a^2/4$. Thus $\rho^2\le4/3$. Equality is attained by $(a,b,x,y)=(1,\sqrt3/2,1/2,0)$, which satisfies every constraint. The answer is $4+3=7$.

**Answer:** 007.

**Methods:** inequalities, equilateral triangle, equality cases.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries reviewed. The direct inequality proof is complete. The geometric alternatives need care at allowed zero endpoints; one mislabels x as sqrt(1-a^2), and the final entry reverses an angle bound. The present proof checks the boundary equality explicitly.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. Nonnegativity bounds an equal-distance system by a sharp quadratic inequality.

## 2009 AIME I Problem 1: Extremal three-digit geometric progressions

A three-digit integer is called geometric when its three distinct digits, in order, form a geometric progression. Find the largest such integer minus the smallest.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

Write the digits as $a,b,c$. None can be zero, since a zero ratio would repeat zeros, and $b^2=ac$. The smallest possible first digit is one; the smallest distinct middle digit then is two, producing $124$. For the largest numeral take $a=9$, which is feasible. Then $b^2=9c$ forces $3\mid b$; distinctness excludes $b=9$, so the largest possible $b$ is six, giving $c=4$ and numeral $964$. The difference is $964-124=840$.

**Answer:** 840.

**Methods:** digit constraints, geometric progressions.

**Verification:** Exhaustively tested all 900 three-digit numbers for distinct geometric digits.

**Source comparison:** All three entries reviewed. The geometric-mean condition gives a complete extremal argument; the shortest entry leaves its candidate exclusions implicit.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Digit bounds and a geometric-mean identity find the extreme numerals.

## 2009 AIME I Problem 2: A complex quotient with fixed imaginary part

A complex number $z$ has imaginary part $164$ and satisfies $z/(z+n)=4i$ for a positive integer $n$. Find $n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

Rearranging gives $z=4in/(1-4i)=n(-16+4i)/17$. Its imaginary part is $4n/17=164$, so $n=697$. The resulting $z=-656+164i$ has $z+n\ne0$, verifying the equation is defined.

**Answer:** 697.

**Methods:** complex arithmetic.

**Verification:** Exact floating complex division for integer components verifies the original quotient.

**Source comparison:** All four entries reviewed. Coefficient comparison, rationalization, and the right-triangle interpretation give the same value.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Rationalizing a linear fractional equation isolates the integer parameter.

## 2009 AIME I Problem 3: Cancel symmetric binomial coefficients

Eight independent coin flips have head probability $p$. The chance of three heads is one twenty-fifth of the chance of five heads. Find numerator plus denominator of $p$ in lowest terms.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

The equal binomial coefficients cancel, leaving $(1-p)^2/p^2=1/25$. Since $0<p<1$, take the positive square root: $(1-p)/p=1/5$. Thus $p=5/6$ and the answer is $11$.

**Answer:** 011.

**Methods:** binomial probability.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. A ratio of binomial probabilities determines the coin bias.

## 2009 AIME I Problem 4: A diagonal meeting a short intercept segment

In parallelogram $ABCD$, points $M\in AB$ and $N\in AD$ satisfy $AM/AB=17/1000$ and $AN/AD=17/2009$. If $P=AC\cap MN$, find $AC/AP$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Use the independent vectors $AB,AD$ as an affine coordinate basis, so $A=(0,0)$, $C=(1,1)$, $M=(17/1000,0)$, and $N=(0,17/2009)$. The line $MN$ is $1000x+2009y=17$. On $AC$, write $x=y=t$, giving $t=17/3009=1/177$. Therefore $AC/AP=177$.

**Answer:** 177.

**Methods:** affine coordinates, intercept form.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries reviewed. The vector and mass-point methods are rigorous. The first collapses the diagram to a line without justification; the last assumes a rectangle without first invoking affine invariance and also gives N an incorrect sign. Affine coordinates avoid both issues.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Affine coordinates turn the intersection ratio into a sum of reciprocals.

## 2009 AIME I Problem 6: Integer values of a stepped power function

How many positive integers $N<1000$ occur as $x^{\lfloor x\rfloor}$ for some real $x$ where the expression is defined?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

For $x<0$, either $-1<x<0$ gives a negative reciprocal or $x\le-1$ gives magnitude at most one, with no positive integer value at the boundary; thus there are no new values. For $0<x<1$, the value is one. If $k\le x<k+1$ with integer $k\ge1$, the image is $[k^k,(k+1)^k)$. For $k=1,2,3,4$ the integer counts are $1,5,37,369$; these ranges are disjoint. For $k\ge5$ all values exceed $1000$. Hence the total is $1+5+37+369=412$.

**Answer:** 412.

**Methods:** floor functions, piecewise monotonicity.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries reviewed. The positive-domain counts are correct; neither source discusses negative real x, which contributes no additional positive integer values as checked here.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. The floor partitions the domain into disjoint monotone-image intervals.

## 2009 AIME I Problem 7: An exponential recurrence that telescopes

Let $a_1=1$ and $5^{a_{n+1}-a_n}-1=1/(n+2/3)$ for $n\ge1$. Find the least integer $k>1$ such that $a_k$ is integral.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

The recurrence is $5^{a_{n+1}-a_n}=(3n+5)/(3n+2)$. Multiplying from $n=1$ through $k-1$ gives $5^{a_k-1}=(3k+2)/5$, hence $5^{a_k}=3k+2$. For $k>1$, the first candidate powers are $25$ and $125$. The former is one modulo three and cannot equal $3k+2$; the latter gives $k=(125-2)/3=41$. Thus the answer is $41$.

**Answer:** 041.

**Methods:** telescoping products, logarithms, modular arithmetic.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries reviewed. Their telescoping and induction approaches are equivalent and complete.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Multiplication of adjacent exponential ratios produces an arithmetic progression inside a logarithm.

## 2009 AIME I Problem 8: Sum of pairwise differences

Sum all positive differences between pairs from $\{1,2,4,\ldots,2^{10}\}$, and report the remainder modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

The value $2^k$ occurs positively in $k$ differences and negatively in $10-k$, so the sum is $\sum_{k=0}^{10}(2k-10)2^k=16398$. (Use $\sum2^k=2047$ and $\sum k2^k=18434$.) Distinct pairs yield distinct differences because the exact power of two dividing the difference identifies the smaller exponent. The residue is $398$.

**Answer:** 398.

**Methods:** contribution counting, weighted sums.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Counting positive and negative appearances of each power evaluates a pairwise-difference sum.

## 2009 AIME I Problem 13: Infinite integrality forces a two-cycle

Every term of a sequence is a positive integer, and $a_{n+2}=(a_n+2009)/(1+a_{n+1})$ for $n\ge1$. Find the smallest possible $a_1+a_2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Subtract consecutive rearranged recurrence equations to obtain $(a_{n+3}-a_{n+1})(a_{n+2}+1)=a_{n+2}-a_n$. Thus the integer differences $d_n=a_{n+2}-a_n$ satisfy $|d_{n+1}|\le|d_n|/2$. If $d_1$ were nonzero, all subsequent differences would remain nonzero by the same identity, contradicting this bound. Hence $d_1=0$, so $a_3=a_1$ and the original equation gives $a_1a_2=2009=7^2\cdot41$. Conversely any such factor pair repeats periodically and works. The factor pairs are $(1,2009),(7,287),(41,49)$; the minimum sum is $90$.

**Answer:** 090.

**Methods:** integer descent, nonlinear recurrence, periodic sequences.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries reviewed. The first integer-difference descent is rigorous. The interval argument in the second incorrectly claims all intervening integers occur; the third explicitly offers only a periodicity guess. The quantitative contraction makes the necessity precise.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. A contracting integer difference must vanish identically.

## 2009 AIME I Problem 14: Minimizing a second moment with fixed first and fourth moments

A sequence of $350$ entries, each in $\{1,2,3,4\}$, satisfies $\sum a_i=513$ and $\sum a_i^4=4745$. Find the smallest possible $\sum a_i^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Let $w,x,y,z$ count the entries equal to $1,2,3,4$. Subtracting the count equation from the two moment equations gives $x+2y+3z=163$ and $15x+80y+255z=4395$. Eliminating $x$ gives $5y+21z=195$. Thus $z\equiv0\pmod5$ and $0\le z\le9$, so $(y,z)$ is $(39,0)$ or $(18,5)$. These give $(w,x)=(226,85)$ or $(215,112)$ respectively. Their second moments are $917$ and $905$, so the minimum is $905$, attained by the latter frequencies.

**Answer:** 905.

**Methods:** frequency variables, integer optimization, moments.

**Verification:** Enumerated every feasible frequency vector using the count and moment constraints, and minimized the second moment.

**Source comparison:** The sole source correctly reduces the constraints to two feasible frequency vectors. The explicit second moments here certify which is minimal.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory, combinatorics. Frequency variables reduce a finite-valued sequence optimization to two feasible integer points.

## 2009 AIME II Problem 1: Equal paint remainders

Initially there are $130$ ounces of blue paint, $164$ of red, and $188$ of white. Four equal-size stripes use blue, red, white, and a red-white mixture, respectively. Equal amounts of the three original colors remain. Find the total paint left.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

Each pure-color stripe uses the same amount. Therefore the mixed stripe must use the initial red excess $164-130=34$ and white excess $188-130=58$. Its total is $92$ ounces, so every stripe uses $92$. The remainder of each color is $130-92=38$, giving total $114$.

**Answer:** 114.

**Methods:** conservation, linear equations.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All seven entries read. The excess argument and total-volume equations are correct. The sixth solves its stripe-size equation as 38 instead of 92, confusing stripe size with remainder; its final total happens to be correct.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The mixed stripe consumes exactly the initial excesses of its two components.

## 2009 AIME II Problem 2: Squared logarithmic exponents

Positive reals satisfy $a^{\log_3 7}=27$, $b^{\log_7 11}=49$, and $c^{\log_{11}25}=\sqrt{11}$. Find $a^{(\log_3 7)^2}+b^{(\log_7 11)^2}+c^{(\log_{11}25)^2}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

Exponentiation by the same logarithm again gives $a^{(\log_3 7)^2}=27^{\log_3 7}=7^3=343$. Similarly the second term is $49^{\log_7 11}=11^2=121$, and the third is $(\sqrt{11})^{\log_{11}25}=\sqrt{25}=5$. Their sum is $469$.

**Answer:** 469.

**Methods:** logarithm identities, exponent rules.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries reviewed. Each uses the same valid power-logarithm cancellation, with different intermediate variables.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Applying the known exponent a second time eliminates the unknown bases.

## 2009 AIME II Problem 3: Perpendicular lines in a rectangle

Rectangle $ABCD$ has $AB=100$. If $E$ is the midpoint of $AD$ and $AC\perp BE$, find the greatest integer less than $AD$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

Choose $A=(0,0)$, $B=(100,0)$, $D=(0,h)$, so $C=(100,h)$ and $E=(0,h/2)$. The perpendicular vectors $AC=(100,h)$ and $BE=(-100,h/2)$ give $-10000+h^2/2=0$. Thus $h=100\sqrt2$. Since $141^2<20000<142^2$, the answer is $141$.

**Answer:** 141.

**Methods:** dot product, rectangle geometry.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries reviewed. Similarity, slopes, and vectors give the same equation. The auxiliary-parallelogram entry misses a square in one Pythagorean display.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A zero dot product fixes the rectangle aspect ratio.

## 2009 AIME II Problem 4: The smallest winning score

For some number of children, the child ranked $k$ eats exactly $n+2-2k$ grapes, a nonnegative amount. Their total is $2009$. Find the smallest possible winning count $n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

If $n\le88$, the largest possible total occurs at $n=88$ with every positive term included: $88+86+\cdots+2=44\cdot45=1980<2009$. Hence $n\ge89$. For $n=89$, the sum of all positive odd terms through 89 is $45^2=2025$. Deleting the tail $7+5+3+1=16$ leaves $89+87+\cdots+9=2009$. This is a valid contest with 41 children, so the minimum is $89$.

**Answer:** 089.

**Methods:** arithmetic progressions, extremal bounds.

**Verification:** Enumerated all nonnegative arithmetic-score contests with winner count at most 89.

**Source comparison:** All four entries reviewed, including the statement-clarification entry. The maximum-sum construction is rigorous. The final factor-pair discussion notes an invalid reversed participant count, though the valid 41-child solution is correct.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. A maximal arithmetic-progression sum gives a sharp lower bound, attained by deleting a tail.

## 2009 AIME II Problem 5: A circle tangent to three interior circles

An equilateral triangle is inscribed in a radius-$10$ circle. Three internally tangent circles touch the outer circle at the triangle vertices and have radii $3,2,2$. A fourth circle is externally tangent to all three. Its radius is reduced $m/n$. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Place the outer center at the origin and the three inner centers at $(0,7)$ and $(\pm4\sqrt3,-4)$. A fourth center equidistant from the last two lies at $(0,y)$. If its radius is $r>0$, then $|y-7|=r+3$ and $48+(y+4)^2=(r+2)^2$. The branch $y=10+r$ yields $r=-10$, impossible. Thus $y=4-r$, and substitution gives $48+(8-r)^2=(r+2)^2$, so $20r=108$. Hence $r=27/5$ and $m+n=32$.

**Answer:** 032.

**Methods:** tangent circles, symmetry, distance equations.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source uses the same symmetry with a cosine rule, assuming the center lies below the origin. The two-branch calculation here proves that the selected location is the unique positive-radius option.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Symmetry and distance equations make the unknown radius linear after cancellation.

## 2009 AIME II Problem 7: A sum with strictly increasing dyadic denominators

Write $\sum_{i=1}^{2009}(2i-1)!!/(2i)!!$ in lowest terms with denominator $2^ab$, where $b$ is odd. Find $ab/10$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

The ith summand equals $\binom{2i}{i}/2^{2i}$, so its reduced denominator is a power of two. Since $(2i)!=2^ii!(2i-1)!!$, its numerator binomial has valuation $i-\nu_2(i!)$. Thus the reduced denominator exponent is $e_i=i+\nu_2(i!)$, strictly increasing with i. On the common denominator $2^{e_{2009}}$, the last numerator is odd and every earlier numerator is even. No further factor of two cancels, so $b=1$ and $a=2009+\nu_2(2009!)$. Legendre gives $\nu_2(2009!)=1004+502+251+125+62+31+15+7+3+1=2001$. Hence $a=4010$ and $ab/10=401$.

**Answer:** 401.

**Methods:** prime valuation, unique minimum valuation, central binomial coefficients.

**Verification:** Summed all 2009 rational summands exactly and checked the fully reduced denominator.

**Source comparison:** All four entries reviewed, including comments in the first. The strict valuation argument is sound. Several alternatives invoke contest answer bounds to assert b=1, or infer a sum valuation from a non-strict lower bound; those do not suffice. The unique odd numerator here explicitly prevents cancellation.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. A unique largest reduced power-of-two denominator cannot cancel in the sum.

## 2009 AIME II Problem 10: Two equal-angle observations

Points $A,B,C,D$ satisfy $AB=5$, $BC=12$, $AC=13$, $\angle BAD=\angle CAD$, and $\angle ACB=\angle DCB$. Write $AD=p\sqrt q/r$ in reduced squarefree form and find $p+q+r$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Place $B=(0,0)$, $A=(5,0)$, $C=(0,12)$. The second angle equality makes ray $CD$ the reflection of $CA$ across $CB$, so its line is $y=12+12x/5$; the other choice would place the distinct point D at A. The line $AD$ is the internal angle-bisector line at A, whose direction is $(-1,0)+(-5,12)/13$, hence $y=(10-2x)/3$. Intersecting gives $D=(-65/23,120/23)$. Therefore $AD=\sqrt{180^2+120^2}/23=60\sqrt{13}/23$, and the answer is $96$.

**Answer:** 096.

**Methods:** angle bisectors, reflection, coordinates.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries reviewed. The reflection, Stewart, cosine, and sine methods agree. Some source diagrams use vertical leg 13 rather than 12, but their numerical derivations use the correct 5-12-13 triangle.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Reflection and an angle bisector determine a point by two lines.

## 2009 AIME II Problem 11: Exactly fifty logarithmic neighbors

Positive integers $m\ge n$ have exactly fifty positive integers $k$ satisfying $|\log m-\log k|<\log n$. Find the sum of all possible products $mn$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

The inequality is $m/n<k<mn$. Exactly fifty integers occur precisely when $mn-51\le m/n<mn-50$, or $50n/(n^2-1)<m\le51n/(n^2-1)$; $n=1$ gives none. Since $m\ge n$, the upper bound forces $n^2-1\le51$, so $2\le n\le7$. For $n=2$ the interval is $(100/3,34]$, giving $m=34$; for $n=3$ it is $(150/8,153/8]$, giving $m=19$. For $n=4,5,6,7$ the intervals $(200/15,204/15]$, $(250/24,255/24]$, $(300/35,306/35]$, and $(350/48,357/48]$ contain no integer. The sum is $68+57=125$.

**Answer:** 125.

**Methods:** logarithmic inequalities, integer intervals.

**Verification:** Exhaustively counted integer points in every analytically bounded open interval.

**Source comparison:** The sole source gives the same exact endpoint treatment and finite bound on n.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Strict logarithmic bounds translate into a narrow interval for an integer parameter.

## 2009 AIME II Problem 13: A product of semicircle chords

A radius-$2$ semicircle with diameter endpoints $A,B$ is divided into seven equal arcs by $C_1,\ldots,C_6$. Let $N=\prod_{k=1}^{6}AC_k\,BC_k$. Find $N$ modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Each triangle $ABC_k$ is right, and its altitude to diameter $AB=4$ is $2\sin(k\pi/7)$. Comparing its two area formulas gives $AC_k\,BC_k=8\sin(k\pi/7)$. For $\zeta=e^{2\pi i/7}$, evaluation at one of $(x^7-1)/(x-1)=\prod_{k=1}^{6}(x-\zeta^k)$ yields $7=\prod_{k=1}^{6}|1-\zeta^k|=2^6\prod_{k=1}^{6}\sin(k\pi/7)$. Therefore $N=8^6\cdot7/2^6=7\cdot2^{12}=28672$, giving remainder $672$.

**Answer:** 672.

**Methods:** roots of unity, sine products, chord lengths.

**Verification:** Directly multiplied the twelve chord lengths using six paired altitude products.

**Source comparison:** All four entries reviewed. The roots-of-unity proofs are complete. One paired-root index should be 7-k rather than k-7; the final solution misses a factor four when adding the diameter chord, though its final numerical expression restores the correct power.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A roots-of-unity product evaluates a sine product exactly.

## 2009 AIME II Problem 14: A radical recurrence with an eventual two-cycle

Let $a_0=0$ and $a_{n+1}=\frac85a_n+\frac65\sqrt{4^n-a_n^2}$. Find $\lfloor a_{10}\rfloor$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Set $b_n=a_n/2^n$. Then $b_{n+1}=(4b_n+3\sqrt{1-b_n^2})/5$. Exact calculation gives $b_1=3/5$, $b_2=24/25$, $b_3=117/125$, and $b_4=24/25$, using the nonnegative square roots $4/5,7/25,44/125$. Since each next term depends only on the current term, the values $24/25$ and $117/125$ now alternate. Thus $a_{10}=1024\cdot24/25=983+1/25$, and its floor is $983$.

**Answer:** 983.

**Methods:** normalization, radical recurrence, periodicity.

**Verification:** Numerically iterated the original unnormalized radical recurrence through index ten.

**Source comparison:** All three entries reviewed, including the normalization-only first entry. The exact iteration and folded-angle explanation agree; the latter correctly retains the absolute value in sqrt(1-sin^2 s).

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Scaling removes exponential growth and reveals an exact short cycle.

## 2009 AIME II Problem 15: Maximum separation of two chord intercepts

Circle diameter $MN$ has length one. On one semicircle, $A$ is the arc midpoint and $MB=3/5$. A variable point $C$ lies on the other semicircle. The chords $AC,BC$ meet $MN$ at $D,E$. If the largest $DE$ is $r-s\sqrt t$ in reduced squarefree form, find $r+s+t$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Put $MC=x$, $NC=y$, so $x,y>0$ and $x^2+y^2=1$. Since A is an arc midpoint, $CA$ bisects $\angle MCN$, yielding $MD=x/(x+y)$. Also $BN=4/5$, and the sine form of the cevian ratio gives $ME/EN=x\sin\angle MCB/(y\sin\angle BCN)=3x/(4y)$. Hence $ME=3x/(3x+4y)$, so $DE=xy/((x+y)(3x+4y))=1/(7+3x/y+4y/x)$. AM-GM gives $3x/y+4y/x\ge4\sqrt3$. Equality occurs at $x=2/\sqrt7$, $y=\sqrt3/\sqrt7$, which is realized by a point on the semicircle. Thus the maximum is $1/(7+4\sqrt3)=7-4\sqrt3$, and the answer is $14$.

**Answer:** 014.

**Methods:** generalized angle bisector, AM-GM, chord intersections.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All five entries reviewed. The elementary cevian-ratio argument supplies both the bound and explicit equality. The cross-ratio alternatives have notation errors, and one omits the attainment check; the calculus methods agree with the same optimum.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The generalized angle-bisector ratio reduces the chord separation to AM-GM.

## 2010 AIME I Problem 3: Equal cross powers at a fixed ratio

Positive reals satisfy $y=3x/4$ and $x^y=y^x$. If $x+y=r/s$ in lowest terms, find $r+s$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

Logarithms and division by $x>0$ give $(3/4)\log x=\log(3x/4)=\log x+\log(3/4)$. Thus $\log x=4\log(4/3)$, so $x=256/81$ and $y=192/81$. Their sum is $448/81$, already reduced, yielding $448+81=529$.

**Answer:** 529.

**Methods:** exponential equations, logarithms.

**Verification:** Exact positive-rational substitution: x^3=y^4 is equivalent to the original positive-power equation when y=3x/4.

**Source comparison:** All four entries reviewed. The logarithm-base-x alternatives implicitly require x not equal to one; natural logarithms avoid that preliminary exception.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Taking logarithms reduces the power equation to one linear logarithm equation.

## 2010 AIME I Problem 5: Equality in a difference-of-squares bound

Positive integers $a>b>c>d$ satisfy $a+b+c+d=2010$ and $a^2-b^2+c^2-d^2=2010$. How many distinct values can $a$ take?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Since $a-b,c-d\ge1$, we have $(a+b)(a-b)+(c+d)(c-d)\ge a+b+c+d$. Equality forces $a-b=c-d=1$. Hence $a+c=1006$, $b=a-1$, $d=c-1$. The remaining conditions are $c\ge2$ and $a-1>c$, equivalent to $504\le a\le1004$. Every integer in this interval works, so there are $501$.

**Answer:** 501.

**Methods:** equality cases, integer inequalities.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries reviewed. The first explicitly forces both unit gaps. The second bounds the first gap but leaves sufficiency and the second gap implicit.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Integer gaps are at least one, so equality forces both gaps to equal one.

## 2010 AIME I Problem 6: A quadratic trapped between two parabolas

A quadratic polynomial satisfies $x^2-2x+2\le P(x)\le2x^2-4x+3$ for every real $x$, and $P(11)=181$. Find $P(16)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

The bounds are $1+(x-1)^2$ and $1+2(x-1)^2$. Thus $P(1)=1$ and $P(x)\ge1$ everywhere, so the quadratic has its vertex at $(1,1)$. Write $P(x)=1+c(x-1)^2$. The condition at 11 gives $100c=180$, hence $c=9/5$, which lies between one and two and satisfies the bounds. Therefore $P(16)=1+(9/5)225=406$.

**Answer:** 406.

**Methods:** quadratic inequalities, common tangent.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All seven entries reviewed. The vertex argument is complete; the graph in the first entry uses coefficient 8/5 instead of the required 9/5, but its written calculation is correct.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Touching bounds force a common vertex and remove the linear coefficient.

## 2010 AIME I Problem 9: A cubic system reduced to one product

Real triples satisfy $x^3-xyz=2$, $y^3-xyz=6$, $z^3-xyz=20$. If the greatest possible $x^3+y^3+z^3$ is reduced $m/n$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Put $t=xyz$. Then $x^3=t+2$, $y^3=t+6$, $z^3=t+20$, so $t^3=(t+2)(t+6)(t+20)$. Cancellation yields $7t^2+43t+60=(t+4)(7t+15)=0$. Both roots give genuine real triples by taking real cube roots, whose product is t because real cubing is injective. The target is $3t+28$, largest at $t=-15/7$, with value $151/7$. Therefore the answer is $158$.

**Answer:** 158.

**Methods:** product substitution, real cube roots.

**Verification:** Exact substitution of both analytically exhaustive product parameters and comparison of target values.

**Source comparison:** All three entries reviewed. One alternative expansion omits a factor four in its linear coefficient; the main product-variable reductions are correct. The real-cube-root argument verifies that neither quadratic candidate is extraneous.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Multiplying the three equations cancels cubic terms in the product variable.

## 2010 AIME I Problem 11: Revolving a triangular inequality region

The region satisfying $|8-x|+y\le10$ and $3y-x\ge15$ is revolved around $3y-x=15$. Write its volume as $m\pi/(n\sqrt p)$ in reduced squarefree form and find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

The region is the triangle with apex $(8,10)$ and base endpoints $(9/2,13/2)$ and $(39/4,33/4)$ on the axis. The perpendicular apex distance is $r=7/\sqrt{10}$, and the base length is $L=7\sqrt{10}/4$. The foot lies between the endpoints, so rotation gives two cones whose heights sum to L. Their combined volume is $\pi r^2L/3=343\pi/(12\sqrt{10})$, giving $343+12+10=365$.

**Answer:** 365.

**Methods:** solids of revolution, point-line distance, cones.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source correctly identifies the triangular region and adds the two cone volumes.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The rotated triangle becomes two cones with a shared base.

## 2010 AIME I Problem 13: A rectangle and semicircle cut in a fixed area ratio

A rectangle $ABCD$ and a semicircle with diameter $AB$ lie on opposite sides of $AB$. A line meets the semicircle at $N$, $AB$ at $U$, and $CD$ at $T$, dividing their union in area ratio $1:2$. Given $AU=84$, $UB=168$, $AN=126$, write $AD=m\sqrt n$ in squarefree form and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Scale lengths by 42. Use $A=(0,0)$, $B=(6,0)$ and rectangle below the axis with height h. The circle radius is three, and $AN=3$ forces $N=(3/2,3\sqrt3/2)$, since the center $(3,0)$ forms an equilateral triangle with A,N. As $U=(2,0)$, the line meets the bottom at $T=(2+h/(3\sqrt3),-h)$; the condition $T\in CD$ gives $0<h\le12\sqrt3$. The left piece has area $L=2h+h^2/(6\sqrt3)+3\pi/2-3\sqrt3/4$, whereas total area is $S=6h+9\pi/2$. It cannot equal $2S/3$, since $L-2S/3=h^2/(6\sqrt3)-2h-3\pi/2-3\sqrt3/4<0$ on that height range. Hence $L=S/3$, giving $h^2/(6\sqrt3)=3\sqrt3/4$, or $h=3\sqrt6/2$. Restoring the scale yields $AD=63\sqrt6$ and answer $69$.

**Answer:** 069.

**Methods:** area cancellation, circular sectors, branch exclusion.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries reviewed, including the diagram-only entry. The intended smaller-side calculation is correct, but the claim that the same side is always smaller is not valid over the full admissible height range. The explicit alternate-ratio exclusion here repairs that gap. Several entries also confuse NU with its horizontal projection or misprint sqrt(3) as sqrt(2).

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Circular-sector terms cancel against a target area fraction, with the alternate ratio branch excluded.

## 2010 AIME I Problem 14: A monotone sum of decimal digit counts

For positive integers $n$, define $f(n)=\sum_{k=1}^{100}\lfloor\log_{10}(kn)\rfloor$. Find the largest $n$ with $f(n)\le300$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Each summand is nondecreasing in n, so f is nondecreasing. At $n=109$, products for $k=1,\ldots,9$ have three digits, those for $k=10,\ldots,91$ have four, and those for $k=92,\ldots,100$ have five. Thus $f(109)=9\cdot2+82\cdot3+9\cdot4=300$. At $n=110$, the middle block ends at $k=90$, giving $f(110)=9\cdot2+81\cdot3+10\cdot4=301$. Monotonicity excludes every larger n, so the answer is $109$.

**Answer:** 109.

**Methods:** digit counts, monotonicity, floor logarithms.

**Verification:** Evaluated the 100 original floor-log terms exactly using decimal lengths at the boundary integers.

**Source comparison:** All four entries reviewed. The first incorrectly says strictly increasing, although nondecreasing is enough. Approximate averaging and broad claims about unit increments are unnecessary; two exact evaluations establish maximality.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Monotonicity makes two adjacent exact evaluations a complete maximality proof.

## 2010 AIME I Problem 15: Equal inradii determine a cevian length

Triangle $ABC$ has $AB=12$, $BC=13$, $AC=15$. A point $M$ inside $AC$ makes triangles $ABM$ and $BCM$ have equal inradii. Write $AM/CM=p/q$ in lowest terms and find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Let the common inradius be r, the original inradius R, total area K, semiperimeter $s=20$, and $BM=d$. Adding the two area formulas gives $K=r(s+d)$, while $K=Rs$. The tangent lengths from A and C to the smaller incircles sum to $s-d$; they also equal $r(\cot(A/2)+\cot(C/2))$. For the original incircle, $R(\cot(A/2)+\cot(C/2))=AC=15$. Thus $r/R=(20-d)/15=20/(20+d)$, yielding $d^2=100$ and $d=10$. Equal inradii also give $AM/CM=(12+d)/(13+d)=22/23$ after cross-multiplying the area ratio. This cevian exists: coordinates $A=(0,0)$, $C=(15,0)$ give $B=(20/3,\sqrt{896}/3)$, and $M=(22/3,0)$ has $BM=10$ and the required area-perimeter ratio. Hence the answer is $45$.

**Answer:** 045.

**Methods:** incircle tangency, equal inradii, cevian length.

**Verification:** Constructed the proposed point in Cartesian coordinates and independently compared the two area-over-semiperimeter inradii; optimality and uniqueness remain analytic.

**Source comparison:** All eight entries reviewed, including the diagram-only entry and the homothety addendum. The contact-length sum gives the shortest elimination. Quartic/Stewart approaches are valid after sign filtering; several source displays omit factors or misuse a ratio, and the answer-range shortcut via the rational-root theorem is unnecessary.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Adding contact lengths and area formulas eliminates the two smaller inradii.

## 2010 AIME II Problem 5: The norm of three logarithms

Positive numbers satisfy $xyz=10^{81}$ and $(\log_{10}x)(\log_{10}(yz))+(\log_{10}y)(\log_{10}z)=468$. Find $\sqrt{(\log_{10}x)^2+(\log_{10}y)^2+(\log_{10}z)^2}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Put $u=\log_{10}x$, $v=\log_{10}y$, $w=\log_{10}z$. Then $u+v+w=81$ and $uv+uw+vw=468$. Therefore $u^2+v^2+w^2=81^2-2\cdot468=5625$, whose square root is $75$.

**Answer:** 075.

**Methods:** symmetric sums, logarithms.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries read. The first symmetric identity is complete. The second arbitrarily sets the unknown cubic constant term to zero; without first proving the target is independent of that coefficient, this specialization does not justify the answer.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The first two elementary symmetric sums determine the sum of squares.

## 2010 AIME II Problem 6: The first reducible quartic

Find the smallest positive integer $n$ for which $x^4-nx+63$ factors into two nonconstant integer-coefficient polynomials.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Because the polynomial is monic, a factorization can be taken monic. A linear factor gives an integer root $r\mid63$ and $n=r^3+63/r$. For positive n, r must be positive. The choices $r=1,3$ give 64 and 48, and $r\ge7$ gives n above 343. Otherwise two monic quadratics have form $(x^2+ax+b)(x^2-ax+d)$. Coefficients require $bd=63$, $b+d=a^2$, and $n=a(b-d)$. The factors b,d must be positive; their unordered pairs are $(1,63),(3,21),(7,9)$. Only sums 64 and 16 are squares, yielding positive n values 496 and 8. Indeed $x^4-8x+63=(x^2+4x+9)(x^2-4x+7)$. Thus the minimum is $8$.

**Answer:** 008.

**Methods:** integer polynomial factorization, rational root theorem.

**Verification:** Exhausted integral constant-factor pairs and integer roots in all factorization types; the coefficient bound |a|<=12 covers b+d<=126.

**Source comparison:** Both entries reviewed. The first covers both possible degree patterns but abbreviates the linear case. The second omits linear-cubic factorizations entirely. Both are addressed explicitly here.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Both linear-cubic and quadratic-quadratic factorization patterns must be checked.

## 2010 AIME II Problem 7: A cubic constrained by conjugate roots

A monic cubic $P(z)=z^3+az^2+bz+c$ has real coefficients and roots $w+3i,w+9i,2w-4$ for some complex w. Find $|a+b+c|$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Write $w=u+vi$. The sum of roots is real, so $4v+12=0$ and $v=-3$. The roots are then $u,u+6i,2u-4-6i$. The nonreal roots must be conjugate, giving $u=2u-4$ and $u=4$. Thus $P(1)=(1-4)((1-4)^2+36)=-135$. Since $P(1)=1+a+b+c$, the requested absolute value is $136$.

**Answer:** 136.

**Methods:** conjugate roots, evaluation at one.

**Verification:** Direct Vieta coefficient computation for the proposed conjugate root triple.

**Source comparison:** All three entries reviewed. Conjugacy avoids checking the imaginary parts of all coefficients. The casework entry mistypes w+9i as w+6i once, without affecting its surviving case.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Real coefficients fix the imaginary shift and force the remaining roots to be conjugate.

## 2010 AIME II Problem 9: A regular hexagon bounded by rotated chords

In regular hexagon $ABCDEF$, let $G,H,I,J,K,L$ be the midpoints of $AB,BC,CD,DE,EF,FA$. The segments $AH,BI,CJ,DK,EL,FG$ bound a smaller regular hexagon. If its area divided by the original area is reduced $m/n$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Normalize the outer circumradius and side length to one. Take $A=(1,0)$, $B=(1/2,\sqrt3/2)$, $C=(-1/2,\sqrt3/2)$, so $H=(0,\sqrt3/2)$. The line $AH$ is $\sqrt3x+2y=\sqrt3$, at distance $\sqrt{3/7}$ from the center. The six rotated lines give the smaller hexagon this apothem, while the original apothem is $\sqrt3/2$. Similar regular polygons have area ratio equal to the squared apothem ratio, here $4/7$. Thus $m+n=11$.

**Answer:** 011.

**Methods:** regular polygons, apothem, similarity.

**Verification:** Independently clipped the outer hexagon by all six defining lines and computed the area ratio by shoelace.

**Source comparison:** All four entries reviewed, including the diagram/setup entry and brief similarity suggestion. The coordinate-intersection entry misprints the y-coordinate of B in its line equation; the correct computed intersection agrees with the direct apothem method. Its external image link was not separately opened.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Distances from the common center to a side line give the area ratio directly.

## 2010 AIME II Problem 10: Quadratics modulo interchange of roots

Count quadratic polynomials with integer coefficients and integer roots whose constant coefficient is $2010$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Write $f(x)=a(x-r)(x-s)$, so $ars=2010$. Since $2010$ has four distinct prime factors, assigning each prime to $|a|,|r|,|s|$ gives $3^4$ ordered magnitude triples. There are four sign assignments with positive product, hence $324$ ordered signed triples. Swapping $r,s$ leaves the polynomial unchanged and fixes exactly two triples, with $r=s=1$ or $r=s=-1$ and $a=2010$. Burnside gives $(324+2)/2=163$.

**Answer:** 163.

**Methods:** Burnside lemma, prime allocations.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, number_theory, algebra. Integer-root quadratics are counted through signed divisor pairs and leading-coefficient choices.

## 2010 AIME II Problem 12: Two isosceles triangles with equal area and perimeter

Two noncongruent integer-sided isosceles triangles have equal areas and perimeters, and their base lengths are in ratio $8:7$. Find their least possible common perimeter.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Write the bases as $8t,7t$ with positive integer t. Equal perimeters make their difference t twice the difference of equal-side lengths, so t is even; put $t=2u$. With common semiperimeter s, the side triples are $(s-8u,s-8u,16u)$ and $(s-7u,s-7u,14u)$, and s is integral. Heron gives equal squared areas $64u^2s(s-16u)=49u^2s(s-14u)$. Thus $15s=338u$. Since 15 and 338 are coprime, the least positive scale is $u=15$, $s=338$. The resulting triples $(218,218,240)$ and $(233,233,210)$ satisfy the triangle inequalities, so the minimum perimeter is $676$.

**Answer:** 676.

**Methods:** Heron formula, parity, primitive integer scaling.

**Verification:** Exhausted all integer-sided isosceles pairs with base ratio 8:7 and perimeter through 676, comparing exact squared areas.

**Source comparison:** Both entries reviewed, including the parity note. The main scaling calculation is correct, but integrality of the parameter in bases 16u and 14u requires the parity argument supplied here.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory, algebra. Parity and Heron reduce the primitive integral solution to a coprime scaling condition.

## 2010 AIME II Problem 13: Two fixed cards share a rank team

Four people draw distinct uniform cards from $1,\ldots,52$ and the two lowest form one team. Two specified people hold $a,a+9$. Among choices with their same-team probability at least $1/2$, find numerator plus denominator of the smallest probability.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

The other two cards must both lie below $a$ or both above $a+9$. Hence $p(a)=[\binom{a-1}{2}+\binom{43-a}{2}]/\binom{50}{2}$. Writing $a=22+t$ makes the numerator $420+t^2$. Thus $p(a)\ge1/2$ requires $t^2\ge192.5$, whose least allowable value is $196$ at $|t|=14$. The minimum is $616/1225=88/175$, yielding $263$.

**Answer:** 263.

**Methods:** conditional probability, convexity.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Conditional card-order probabilities lead to a discrete optimization over the two fixed cards.

## 2010 AIME II Problem 14: A doubled angle in a right triangle

Right triangle $ABC$ has right angle C, $AB=4$, and $\angle A<45^\circ$. A point $P$ on $AB$ satisfies $CP=1$ and $\angle APC=2\angle ACP$. If $AP/BP=p+q\sqrt r$ in squarefree form, find $p+q+r$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Let $\theta=\angle ACP$ and $\beta=\angle ABC$. In triangle BCP, the sine rule gives $BP=\cos\theta/\sin\beta$. In triangle ACP, using $AC=4\sin\beta$, it gives $AP=AC\sin\theta/\sin2\theta=2\sin\beta/\cos\theta$. Hence $AP\cdot BP=2$ and $AP+BP=4$, so the two lengths are $2\pm\sqrt2$. Also $\angle A=180^\circ-3\theta<45^\circ$ forces $\theta>45^\circ>\angle A$, so $AP>CP=1$. Therefore $AP=2+\sqrt2$, yielding $AP/BP=3+2\sqrt2$ and answer $7$.

**Answer:** 007.

**Methods:** sine rule, angle doubling, branch selection.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries reviewed. The sine-rule and power-of-a-point methods give the correct product. Several entries assert AP greater than BP without using the angle condition; the explicit angle comparison here selects the correct root. The long angle-bisector derivation also contains a denominator typo.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Two sine-rule equations cancel the auxiliary angles and determine a chord product.

## 2010 AIME II Problem 15: A radical axis evaluated by endpoint powers

Triangle $ABC$ has $AC=13$, $BC=14$, $AB=15$. Let M,N be the midpoints of AC,AB, and let the angle bisectors from B,C meet AC,AB at D,E. The circles AMN and ADE meet again at P. Ray AP meets BC at Q. If $BQ/CQ=m/n$ in lowest terms, find $m-n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Let $F(X)=\operatorname{Pow}_{AMN}(X)-\operatorname{Pow}_{ADE}(X)$. The quadratic parts of the two power functions cancel, so F is affine and vanishes on their radical axis AP. At B, secants along BA give $F(B)=BA(BN-BE)=15(15/2-70/9)=-25/6$, because the angle-bisector theorem gives $BE=14\cdot15/27=70/9$. At C, similarly $F(C)=CA(CM-CD)=13(13/2-182/29)=169/58$. These have opposite signs, so the zero on BC lies inside the segment. Affine interpolation yields $BQ/CQ=-F(B)/F(C)=(25/6)/(169/58)=725/507$. Thus $m-n=218$.

**Answer:** 218.

**Methods:** radical axis, power of a point, affine interpolation.

**Verification:** Exact evaluation of the radical-axis affine ratio; the geometric power interpretation is established analytically.

**Source comparison:** All four entries reviewed, including the stated concurrency extension; its cited external reference was not opened. Power interpolation gives the shortest proof. The first general formula cancels an extra factor only because a-b=c-a=1 in this instance; the explicit numeric powers avoid overstating that cancellation.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The difference of circle powers is affine along the opposite side.

## 2011 AIME I Problem 1: Balancing two acid mixtures

Containers hold $4$ liters of $45\%$ acid, $5$ liters of $48\%$ acid, and $1$ liter of $k\%$ acid. Splitting the third container between the first two makes both $50\%$ acid. If the fraction poured into the first is $m/n$ in lowest terms, find $k+m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

The final $10$ liters contain $5$ liters of acid. The third container therefore contains $5-4(0.45)-5(0.48)=0.8$ liters of acid, so $k=80$. If $t$ liters go to the first container, $1.8+0.8t=0.5(4+t)$, giving $t=2/3$. The requested sum is $80+2+3=85$.

**Answer:** 085.

**Methods:** mixtures, linear equations, conservation.

**Verification:** Exact substitution into both final concentration balances.

**Source comparison:** All four entries were reviewed. Total acid conservation shortens the two-equation approach. The second alternative uses an unnecessarily complicated hypothetical transfer and mixed unit language; the invariant is sufficient.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Two linear mixture balances and conservation of acid.

## 2011 AIME I Problem 2: Parallel segments across a rectangle

In rectangle $ABCD$, $AB=12$ and $BC=10$. Interior points $E,F$ satisfy $BE=9$, $DF=8$, $BE\parallel DF$, and $EF\parallel AB$; the line $BE$ meets side $AD$. Write $EF=m\sqrt n-p$ with squarefree $n$ and positive integers $m,n,p$, and find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

Use $D=(0,0)$, $B=(12,10)$ and write $F=8(u,v)$, $E=B-9(u,v)$, where $u^2+v^2=1$ and $u,v>0$. Equal heights give $17v=10$, hence $17u=\sqrt{17^2-10^2}=3\sqrt{21}$. Their horizontal separation is $17u-12$, so $EF=3\sqrt{21}-12$ and the answer is $3+21+12=36$.

**Answer:** 036.

**Methods:** parallel vectors, Pythagorean theorem.

**Verification:** Independent coordinate reconstruction verifies both segment lengths, equal heights, and the requested separation.

**Source comparison:** All three entries were reviewed. Their similar-triangle or extended-segment constructions encode the same length-17 right triangle. One longer algebraic derivation has a squared-expression transcription error; the vector computation avoids it.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Parallel vectors reduce a rectangular configuration to a right triangle.

## 2011 AIME I Problem 3: Coordinates in rotated perpendicular axes

Line $L$ has slope $5/12$ and contains $(24,-1)$. Its perpendicular $M$ contains $(5,6)$. Use $L,M$ as the new coordinate axes, with positive directions toward these respective points. If $(-14,27)$ has coordinates $(\alpha,\beta)$ in this system, find $\alpha+\beta$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

Unit vectors in the positive axis directions are $(12,5)/13$ and $(-5,12)/13$. Since the new first coordinate vanishes on $M$ and the second on $L$, the coordinate functions are $\alpha=(12x+5y-90)/13$ and $\beta=(-5x+12y+132)/13$. Their values at the specified direction points are positive, verifying orientation. At $(-14,27)$ they give $-123/13$ and $526/13$, whose sum is $31$.

**Answer:** 031.

**Methods:** orthogonal projection, signed coordinates.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. Signed distances avoid computing the intersection of the axes. The long coordinate alternative has a mistyped right-hand-side coordinate; the final projection entry is only an outline.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Signed orthogonal projections determine the rotated coordinates.

## 2011 AIME I Problem 6: An integer value of a parabola

The graph of $ax^2+bx+c$, with $a>0$, has vertex $(1/4,-9/8)$, and $a+b+c$ is an integer. The smallest possible $a$ is $p/q$ in lowest terms. Find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

Vertex form gives $P(x)=a(x-1/4)^2-9/8$, so $P(1)=9a/16-9/8$. As $a>0$, this integer exceeds $-9/8$; its least possible value is $-1$. Solving $9a/16-9/8=-1$ gives $a=2/9$, hence the answer is $11$.

**Answer:** 011.

**Methods:** vertex form, integer constraints.

**Verification:** Exact substitution of the minimal coefficient into the vertex-form integer condition; minimality remains analytic.

**Source comparison:** All five entries were reviewed. Evaluation at 1 is the useful invariant. Coefficient comparison, derivative equations, and congruence language all reduce to this same one-dimensional integer condition.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Vertex form converts the coefficient-sum constraint into an integer interval.

## 2011 AIME I Problem 8: Folding triangular legs of equal height

A triangular sheet has side lengths $23,27,30$. Cut off a corner triangle at each vertex by a fold line parallel to the opposite side, with the three corner interiors disjoint. Fold these corners downward through $90^\circ$ so their vertex tips lie on one plane below the central tabletop. What is the greatest height, written $m\sqrt n/p$ in reduced form with squarefree $n$? Find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

The area is $K=\sqrt{40\cdot17\cdot13\cdot10}=20\sqrt{221}$. If the common height is $h$, the corner similarity ratios are $23h/(2K)$, $27h/(2K)$, and $30h/(2K)$, because each corner altitude becomes a vertical leg. Along each original side the two adjacent ratios must sum to at most 1. The strongest of these three conditions is $57h/(2K)\le1$. At equality the other two inequalities are strict, so the configuration exists and the central tabletop has positive area. Thus $h=40\sqrt{221}/57$, giving $40+221+57=318$.

**Answer:** 318.

**Methods:** similarity, folding, linear constraints, Heron formula.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. Each uses corner similarity and the first pair of legs to meet. The proof here explicitly checks all three edge constraints and attainment, allowing the two limiting fold lines to share a point.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Similar corner triangles translate a folding problem into pairwise linear constraints.

## 2011 AIME I Problem 9: A logarithmic trigonometric equation

For $x\in[0,\pi/2]$, suppose $\log_{24\sin x}(24\cos x)=3/2$. Find $24\cot^2x$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

The logarithm requires $0<x<\pi/2$ and $24\sin x\ne1$. With $s=\sin x>0$, squaring $24\cos x=(24s)^{3/2}$ gives $24s^3+s^2-1=0$. Factor this as $(3s-1)(8s^2+3s+1)=0$. The quadratic has negative discriminant, so $s=1/3$. This gives the valid logarithmic base 8 and $\cot^2x=(1-s^2)/s^2=8$. The requested value is $192$.

**Answer:** 192.

**Methods:** logarithms, trigonometry, factorization.

**Verification:** Exact substitution into the cubed trigonometric identity and target; the proof checks logarithm admissibility.

**Source comparison:** Both entries were reviewed. One finds the sine root without proving uniqueness; the other uses a monotone cubic in cotangent squared. The displayed factorization proves uniqueness and checks the logarithm domain.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The logarithm becomes a cubic in sine with only one admissible root.

## 2011 AIME I Problem 11: Summing a power-residue orbit without its order

Let $R$ be the set of distinct residues of $2^n$ modulo $1000$ for integers $n\ge0$. Find the remainder modulo $1000$ of the sum of the elements of $R$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Let $r_j=r_i$ be the first repetition in the sequence $r_n\equiv2^n\pmod{1000}$, with $i<j$. Since $1000\mid2^i(2^{j-i}-1)$ and the second factor is odd, $i\ge3$. Cancellation modulo $125$ gives $2^{j-i}\equiv1\pmod{125}$, hence $2^{j-i+3}\equiv8\pmod{1000}$. If $i>3$, this repeats $r_3$ before index $j$, a contradiction. Thus $i=3$ and $r_j=8$. Every distinct residue occurs exactly once among $r_0,\ldots,r_{j-1}$, since the subsequent sequence repeats its cycle. Their sum is congruent to $1+2+\cdots+2^{j-1}=2^j-1\equiv7\pmod{1000}$.

**Answer:** 007.

**Methods:** modular dynamics, geometric series, eventual periodicity.

**Verification:** Generated the full modular orbit up to its first repetition and summed every distinct residue.

**Source comparison:** All five entries were reviewed. Order computations are unnecessary. Some entries only guess that 8 is the first repeated residue or incompletely exclude smaller orders; the first-repetition argument supplies the missing justification without determining the cycle length.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. The transient and periodic parts of powers modulo 1000 control their distinct-residue sum.

## 2011 AIME I Problem 13: The height of a tilted cube

A cube of edge length $10$ lies above a plane. Its nearest vertex is $A$, and the three vertices adjacent to $A$ are at distances $10,11,12$ from the plane. Express the distance of $A$ as $(r-\sqrt s)/t$ in reduced form and find $r+s+t$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Let $h$ be the height of $A$. The vertical components of its three mutually perpendicular length-10 edges are $10-h,11-h,12-h$. For an orthonormal basis the squared components of the unit vertical vector sum to 1, so $(10-h)^2+(11-h)^2+(12-h)^2=100$. Setting $z=11-h$ yields $3z^2+2=100$. Since $A$ is the nearest vertex, $h<10$ and $z>0$. Therefore $h=11-7\sqrt6/3=(33-\sqrt{294})/3$, giving $330$.

**Answer:** 330.

**Methods:** orthonormal basis, spatial projection, quadratic equation.

**Verification:** Numerically checked the vertical-component identity and nearest-vertex branch.

**Source comparison:** Both entries were reviewed. The normal-vector identity gives a direct proof; the centroid-and-tilt construction reaches the same quadratic with more geometry. The nearest-vertex hypothesis selects the correct root.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Orthogonal edge directions give a sum of squared vertical components.

## 2011 AIME I Problem 14: Projecting the midpoint square of an octagon

In a regular octagon $A_1\cdots A_8$, let $M_i$ be the midpoint of $A_iA_{i+1}$ for odd $i$. Inward rays from $M_1,M_3,M_5,M_7$ are perpendicular to their neighboring rays. Their successive intersections are $B_1,B_3,B_5,B_7$, with $B_1\in R_1\cap R_3$. If $B_1B_3$ equals an octagon side, write $\cos(2\angle A_3M_3B_1)=m-\sqrt n$ and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Scale the octagon side to 2. The odd-side midpoints form a square on a circle of radius $a=1+\sqrt2$, and $M_1M_5$ is parallel to side $A_3A_4$. Because $R_1$ and $R_5$ are perpendicular to $R_3$, the points $B_1,B_3$ are the perpendicular projections of $M_1,M_5$ onto its line. If $\theta=\angle A_3M_3B_1$, the projection length is $2a|\cos\theta|=2$. Consequently $\cos2\theta=2/a^2-1=2(\sqrt2-1)^2-1=5-\sqrt{32}$, so the answer is $37$.

**Answer:** 037.

**Methods:** regular octagon, orthogonal projection, double-angle identity.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All five entries were reviewed. The projection interpretation gives the shortest route and avoids relying on an unproved symmetry of the intersection square. One alternative mistakenly calls the octagon a hexagon; its intended projection calculation is recognizable.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Adjacent perpendicular rays make their intersection gap a projection of a diameter.

## 2011 AIME I Problem 15: Bounding integer roots of a depressed cubic

The polynomial $x^3-2011x+m$ has three integer roots. Find the sum of their absolute values.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

None of the roots is zero, since otherwise the other two would be $\pm\sqrt{2011}$. Their sum is zero, so after reversing all signs if necessary write them as $u,v,-s$, with $u,v>0$ and $s=u+v$. Vieta gives $uv=s^2-2011$. Thus $s^2>2011$, while $uv\le s^2/4$ gives $3s^2\le8044$. Hence $45\le s\le51$. The discriminant of $t^2-st+(s^2-2011)$ must be a square. For these seven values of $s$, it is respectively $1969,1696,1417,1132,841,544,241$. Only $841=29^2$ is square. Thus $s=49$ and $\{u,v\}=\{10,39\}$; these roots do satisfy the required coefficients. Their absolute values sum to $2s=98$.

**Answer:** 098.

**Methods:** Vieta formulas, integer roots, discriminant, finite bounding.

**Verification:** Enumerated every sorted integer-root triple in the analytically proved magnitude bound 51.

**Source comparison:** All six entries were reviewed. The sources find the root triple, but several stop at its discovery without excluding all other cases; one proposed valuation discussion is unrelated and contains a year/constant typo. The explicit bound and all seven discriminants prove the required uniqueness.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Vieta reduces integral roots to seven discriminant checks, proving uniqueness.

## 2011 AIME II Problem 1: Changing the purchased and consumed amounts

A person drinks a reduced fraction $m/n$ of a purchased beverage. If the purchased amount had been halved and the amount drunk doubled, the waste would have been only $2/9$ of the original waste. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

Normalize the original purchase to 1 and put $t=m/n$. The two wasted amounts are $1-t$ and $1/2-2t$, so $1/2-2t=(2/9)(1-t)$. Multiplication by 18 gives $9-36t=4-4t$, hence $t=5/32$. This is admissible since $2t<1/2$, and the answer is $37$.

**Answer:** 037.

**Methods:** linear equations, ratios.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole entry was reviewed. Its correct normalization distinguishes doubling the amount drunk from doubling the consumed fraction of a changed purchase.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A linear equation compares absolute wasted amounts.

## 2011 AIME II Problem 2: Three equal segments spanning a square

In square $ABCD$, points $E$ and $F$ lie in the interiors of $AD$ and $BC$, respectively. If $BE=EF=FD=30$, find the area of the square.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

Set $A=(0,0)$, $B=(s,0)$, $C=(s,s)$, $D=(0,s)$, $E=(0,e)$, and $F=(s,f)$, with $0<e,f<s$. From $BE=FD$ we obtain $e=s-f$. Then $BE=EF$ gives $e^2=(s-2e)^2$, or $(s-e)(s-3e)=0$. The interior condition excludes $e=s$, so $e=s/3$. Finally $900=BE^2=s^2+(s/3)^2=10s^2/9$, and the area is $810$.

**Answer:** 810.

**Methods:** distance equations, square, degenerate cases.

**Verification:** Direct distance check of the nondegenerate trisection configuration.

**Source comparison:** The sole entry was reviewed. It asserts the trisection without deriving it. The coordinate proof derives it and makes explicit the intended distinct-point convention: allowing E=D and F=B would create a different degenerate answer.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Source correction:** The archived wording says points lie on sides without explicitly excluding endpoints. The intended distinct-vertex configuration has interior E,F and area 810; the coincident choice E=D,F=B would instead give area 450. The restatement states the intended nondegeneracy explicitly.

**Subject classification:** geometry, algebra. Equal distances force the two side points to trisect their respective sides.

## 2011 AIME II Problem 3: Integer angles in arithmetic progression

The interior angle measures of a convex $18$-gon, in increasing order, form a strictly increasing arithmetic progression of integers. Find its smallest angle in degrees.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

Write the angles as $a,a+d,\ldots,a+17d$, with positive integer $d$. Their sum is $16\cdot180$, so $2a+17d=320$. Thus $d$ is even. The largest angle equals $160+17d/2<180$, yielding $d<40/17$. The only positive even possibility is $d=2$, and $a=160-17=143$.

**Answer:** 143.

**Methods:** polygon angle sum, arithmetic progression, parity.

**Verification:** Exhaustive integer search over all convex arithmetic-progressive angle lists.

**Source comparison:** All four entries were reviewed. The angle-sum equation supplies the parity condition sometimes left implicit in median arguments. The final entry incorrectly describes every angle as 160 before listing a progression; the intended average is 160.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory, algebra. The polygon angle sum and convexity bound an even integral common difference.

## 2011 AIME II Problem 4: A midpoint on an angle bisector

In triangle $ABC$, $AB=20$ and $AC=11$. The internal bisector from $A$ meets $BC$ at $D$, and $M$ is the midpoint of $AD$. Line $BM$ meets $AC$ at $P$. If $CP/PA=m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Take $A$ as vector origin, with position vectors $b,c$ for $B,C$. The angle-bisector theorem gives $BD:DC=20:11$, so $D=(11b+20c)/31$ and $M=(11b+20c)/62$. A point on $BM$ is $(1-t)b+tM$. Its $b$ coefficient vanishes at $t=62/51$, giving $P=20c/51$. Thus $AP:PC=20:31$, and $m+n=51$.

**Answer:** 051.

**Methods:** angle-bisector theorem, affine coordinates, mass points.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All nine entries were reviewed, including one attribution-only entry. Mass points, Menelaus, and area ratios are valid routes. The barycentric entry reverses its final written fraction; another assumes a right triangle without explaining affine invariance. The vector argument works for every allowed shape.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The angle-bisector ratio and affine coordinates give a second cevian ratio.

## 2011 AIME II Problem 5: Geometric blocks of equal length

A geometric sequence has sum $200$ over its first $2011$ terms and sum $380$ over its first $4022$ terms. Find the sum over its first $6033$ terms.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

If the common ratio is $r$, each block of $2011$ terms is $r^{2011}$ times the preceding block, term by term. The first two block sums are $200$ and $180$, so their ratio is $9/10$. The third block sums to $180(9/10)=162$. The requested total is $380+162=542$.

**Answer:** 542.

**Methods:** geometric series, blocking.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. Comparing blocks avoids solving for the original ratio and avoids any unnecessary division by 1-r.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Equal-length block sums of a geometric sequence form another geometric sequence.

## 2011 AIME II Problem 8: Independent choices among rotated complex roots

Let $z_1,\ldots,z_{12}$ be the roots of $z^{12}=2^{36}$. Independently choose each $w_j$ to equal $z_j$ or $iz_j$. If the maximum of $\operatorname{Re}\sum_jw_j$ is $m+\sqrt n$ for positive integers $m,n$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

The roots are $8e^{ik\pi/6}$ for $0\le k<12$. For a root $z=a+bi$, the best contribution is $\max(a,-b)$. Opposite roots together contribute $\max(a,-b)+\max(-a,b)=|a+b|$. For $k=0,1,2,3,4,5$, these pair contributions are $8$, $4(\sqrt3+1)$, $4(\sqrt3+1)$, $8$, $4(\sqrt3-1)$, $4(\sqrt3-1)$. Their sum is $16+16\sqrt3=16+\sqrt{768}$. Every choice is independent, so this upper bound is attained; the answer is $784$.

**Answer:** 784.

**Methods:** complex roots, independent maximization, absolute-value identity.

**Verification:** Computed all twelve complex roots numerically and maximized each allowed two-choice real contribution directly.

**Source comparison:** All five stored entries were reviewed, and the full statement was recovered from the alternate archive. The first projection method is sound. Later entries contain errors: sin(x)=cos(x+pi/2) has the wrong sign, the root angle is k*pi/6 rather than k*pi/12, and changing a root sign is not an allowed independent choice. Pairing the already-present opposite roots avoids those issues.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Source correction:** The primary statement was truncated after the first choice; the complete alternate statement specifies w_j in {z_j, i z_j} and asks for the maximum real sum.

**Subject classification:** algebra, geometry. Separability of the objective and opposite root pairs reduce a complex maximum to absolute projections.

## 2011 AIME II Problem 9: Completing a cyclic cubic to a product

Nonnegative $x_1,\ldots,x_6$ sum to $1$ and satisfy $x_1x_3x_5+x_2x_4x_6\ge1/540$. Find $p+q$ if the maximum of $\sum_{j=1}^6x_jx_{j+1}x_{j+2}$, with indices taken modulo $6$, is the reduced fraction $p/q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Let $T=x_1x_3x_5+x_2x_4x_6$ and let $S$ be the target sum. Expansion gives $S+T=(x_1+x_4)(x_2+x_5)(x_3+x_6)\le1/27$ by AM-GM. Therefore $S\le1/27-1/540=19/540$. Equality is achieved by $(x_1,\ldots,x_6)=(1/3,19/60,1/3,0,1/60,0)$: each opposite pair sums to $1/3$ and $T=1/540$. Hence the answer is $19+540=559$.

**Answer:** 559.

**Methods:** AM-GM, factor completion, equality cases.

**Verification:** Exact substitution verifies the nonnegative equality witness and both original cubic expressions; the upper bound is analytic.

**Source comparison:** Both entries were reviewed. The principal product-completion method is correct once equality is exhibited. The alternative symmetry guess is invalid: equal odd entries and equal even entries cannot attain the proposed constraint equality, as that entry itself acknowledges.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Add the constrained terms to expose a three-factor AM-GM bound with an explicit boundary equality case.

## 2011 AIME II Problem 10: A diameter through two chord projections

In a circle of radius $25$ centered at $O$, chords of lengths $30$ and $14$ meet at $P$. Their midpoints are $12$ units apart. If $OP^2=m/n$ in lowest terms, find the remainder of $m+n$ modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Let the chord midpoints be $E,F$. Perpendicular projection gives $OE=\sqrt{25^2-15^2}=20$ and $OF=\sqrt{25^2-7^2}=24$. Since $OE\perp EP$ and $OF\perp FP$, both $E,F$ lie on the circle with diameter $OP$. Triangle $OEF$ has sides $20,24,12$ and area $K=\sqrt{28\cdot8\cdot4\cdot16}=32\sqrt{14}$. Its circumradius is $20\cdot24\cdot12/(4K)=45/\sqrt{14}$, so $OP=90/\sqrt{14}$ and $OP^2=4050/7$. Thus the requested remainder is $57$.

**Answer:** 057.

**Methods:** chord midpoint, diameter circle, circumradius, Heron formula.

**Verification:** Independent Cartesian intersection of the two chord lines gives OP squared and the specified midpoint distance.

**Source comparison:** All seven entries were reviewed. The diameter-circle method avoids the vertex-order ambiguities of Ptolemy and trigonometric approaches. Several longer alternatives have mislabeled segments or angles; these do not affect the clean circumradius proof. One entry calls the circumcircle an inscribed circle.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The chord midpoints and intersection lie on the circle with diameter OP.

## 2011 AIME II Problem 11: A tridiagonal determinant series

For $n\ge1$, let $D_n$ be the determinant of the $n$ by $n$ matrix with diagonal entries $10$, entries $3$ immediately above and below the diagonal, and all other entries zero. If $\sum_{n=1}^{\infty}(8D_n+1)^{-1}=p/q$ in lowest terms, find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Set $D_0=1$. Expanding along the first row and then the first column of its second minor gives $D_n=10D_{n-1}-9D_{n-2}$ for $n\ge2$, with $D_1=10$. Hence $D_n-D_{n-1}=9(D_{n-1}-D_{n-2})$ and induction gives $D_n-D_{n-1}=9^n$. Thus $D_n=(9^{n+1}-1)/8$. The desired series is $\sum_{n=1}^{\infty}9^{-n-1}=(1/81)/(1-1/9)=1/72$, yielding $73$.

**Answer:** 073.

**Methods:** determinant recurrence, first differences, geometric series.

**Verification:** Independently computed determinants by full cofactor expansion for sizes 1 through 7; the infinite-series conclusion is analytic.

**Source comparison:** The sole entry was reviewed. Its cofactor recurrence is correct; explicitly subtracting the previous determinant turns the observed numerical pattern into an immediate inductive proof.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Cofactor expansion gives a second-order recurrence whose first differences are geometric.

## 2011 AIME II Problem 13: Circumcenters along a square diagonal

Point $P$ lies inside diagonal $AC$ of square $ABCD$, with $AP>CP$ and side length $12$. Let $O_1,O_2$ be the circumcenters of $ABP,CDP$. If $\angle O_1PO_2=120^\circ$ and $AP=\sqrt a+\sqrt b$ for positive integers $a,b$, find $a+b$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Put $A=(-s,0)$, $B=(0,s)$, $C=(s,0)$, $D=(0,-s)$, where $s=6\sqrt2$, and $P=(p,0)$ with $0<p<s$. The perpendicular bisectors give $O_1=((p-s)/2,(s-p)/2)$ and $O_2=((p+s)/2,-(p+s)/2)$. Both vectors from $P$ have squared length $(p^2+s^2)/2$, and their dot product is $(p^2-s^2)/2$. Therefore $(p^2-s^2)/(p^2+s^2)=\cos120^\circ=-1/2$, so $p=s/\sqrt3=2\sqrt6$. Thus $AP=s+p=\sqrt{72}+\sqrt{24}$ and the answer is $96$.

**Answer:** 096.

**Methods:** circumcenter, dot product, diagonal coordinates.

**Verification:** Independent distance and dot-product checks verify the proposed circumcenter configuration and 120-degree angle.

**Source comparison:** All nine entries were reviewed, along with the extra solution accidentally attached to the primary statement. The diagonal-coordinate method is reliable and short. Several angle-chasing alternatives interchange circumcenter labels or omit factors of two; one coordinate entry misstates a midpoint while using the correct resulting line.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Diagonal coordinates make the angle between two circumradius vectors explicit.

## 2011 AIME II Problem 15: Floor equality on three intervals

Let $P(x)=x^2-3x-9$ and choose $x$ uniformly on $[5,15]$. The probability that $\lfloor\sqrt{P(x)}\rfloor=\sqrt{P(\lfloor x\rfloor)}$ has form $(\sqrt a+\sqrt b+\sqrt c-d)/e$. Find $a+b+c+d+e$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

The right side must be integral. For integer inputs $5$ through $14$, $P(k)$ is square only at $k=5,6,13$, with square roots $1,3,11$. Since $P$ is increasing, the successful intervals run from each $k$ until $P(x)$ reaches the next square $4,16,144$. Their upper endpoints are $(3+\sqrt{61})/2,(3+\sqrt{109})/2,(3+\sqrt{621})/2$. Each upper endpoint is less than $k+1$, so the floor of $x$ stays at $k$ throughout. Sum their lengths and divide by ten to obtain $(\sqrt{61}+\sqrt{109}+\sqrt{621}-39)/20$. The requested sum is $850$.

**Answer:** 850.

**Methods:** continuous probability, floor stratification.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: The substitution mishandles the floor: floor(2x-3) is not 2 floor(x)-3. The subsequent intervals actually use the latter expression, so the written transformed equation is invalid. Source 3: The answer format is used to assert interval bounds without proof. The bounds should be checked directly.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra, number_theory. Continuous probability reduces to integer square values of a polynomial on floor cells.

## 2012 AIME I Problem 2: The sum increase reveals the number of terms

An arithmetic progression has total $715$. Increasing its $k$th term by $2k-1$ changes the total to $836$. Find the sum of the original first, middle, and last terms.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

If there are $n$ terms, the total increase is the sum of the first $n$ odd positive integers, namely $n^2$. Hence $n^2=836-715=121$ and $n=11$. The middle term is the average $715/11=65$, while the first and last sum to twice that average. The requested sum is therefore $3\cdot65=195$.

**Answer:** 195.

**Methods:** arithmetic progressions, symmetric pairing.

**Verification:** Exact increase 121 gives eleven terms, with average sixty-five.

**Source comparison:** All three stored entries inspected. The third chooses one convenient progression after deriving its average; the invariant proof here shows directly why the answer is independent of that choice.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. An arithmetic-progression symmetry determines a sum without determining its common difference.

## 2012 AIME I Problem 4: A shared horse and the first integer meeting point

Two travelers start together along a road with mileposts at every positive integer distance. Their walking speeds are $4$ and $5/2$ mph; their shared horse carries either at $6$ mph. The slower walker rides first to post one and leaves the horse. Thereafter each rider passes the other traveler, leaves the horse at the next post, and walks on. At their first meeting at a milepost, the distance is $n$ miles and elapsed time is $t$ minutes. Find $n+t$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Call the faster walker $B$ and the slower walker $S$. If both meet at post $n$ and $B$ has ridden a total of $a$ miles, the horse has traveled $n$ miles and $S$ has ridden $n-a$. All riding segments end at integer posts, including the current segment at the meeting, so $a$ is integral. Their times in hours are
$$T_B=\frac a6+\frac{n-a}{4},\qquad T_S=\frac{n-a}{6}+\frac{2a}{5}.$$
Equality gives $5n=19a$, so any positive milepost meeting is at least nineteen miles away.

It remains to prove that the specified handoff rule actually reaches this candidate. At a handoff post $n$, let $a$ be $B$'s accumulated riding distance. If $B$ next rides, its catch-up position is $u=19(n-a)/14$; if $S$ next rides, it is $u=19a/5$. These follow by using the same travel-time formulas at a variable position $u$: in the first case $B$'s riding distance becomes $a+u-n$, and in the second it stays $a$. For a nonintegral catch position, the horse is left at $\lfloor u\rfloor+1$.

Starting after the first ride, the successive handoff states $(n,a)$ are
$$(1,0),(2,1),(4,1),(5,2),(8,2),(9,3),(12,3),(13,4),(16,4),(17,5).$$
The corresponding next catch positions are
$$\frac{19}{14},\frac{19}{5},\frac{57}{14},\frac{38}{5},\frac{57}{7},\frac{57}{5},\frac{171}{14},\frac{76}{5},\frac{114}{7},19.$$
Each noninteger value produces precisely the next listed post, so this is a valid execution of the rule. The final catch is at post nineteen. Its elapsed time is $5/6+14/4=13/3$ hours, or $260$ minutes. Thus $n+t=279$.

**Answer:** 279.

**Methods:** travel-time invariants, integer meeting points, discrete recurrence.

**Verification:** Exact rational simulation of the handoff recurrence reaches post 19 with five miles ridden by the faster walker.

**Source comparison:** The sole stored solution is explicitly marked nonrigorous because it does not establish the candidate handoff pattern. The new proof supplies the exact catch-position recurrence and every state through the first integer meeting.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Travel-time invariants give a divisibility obstruction, and a discrete handoff recurrence proves attainability.

## 2012 AIME I Problem 6: A positive imaginary part selects a root-of-unity denominator

Complex numbers satisfy $z^{13}=w$ and $w^{11}=z$. Suppose $\operatorname{Im}z=\sin(m\pi/n)$ for coprime positive integers $m<n$. Determine $n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

The specified sine is positive, so $z\ne0$. Substitution gives $z^{143}=z$, hence $z^{142}=1$. Its positive-imaginary roots are $z=e^{ik\pi/71}$ for $1\le k\le70$. Two angles in $(0,\pi)$ have the same sine exactly when they are equal or supplementary. Therefore $m/n=k/71$ or $(71-k)/71$. Since $71$ is prime and both numerators lie between one and seventy, either fraction has reduced denominator $71$. Thus $n=71$.

**Answer:** 071.

**Methods:** roots of unity, sine symmetry, reduced fractions.

**Verification:** The denominators of k/71 and (71−k)/71 are seventy-one for all 1≤k≤70.

**Source comparison:** The sole stored proof inspected. The new exposition adds the equal-or-supplementary sine alternative, so the given rational angle is not assumed to equal the root argument uniquely.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. A power cycle gives roots of unity, and sine symmetry fixes the reduced rational angle denominator.

## 2012 AIME I Problem 7: Stationary coins on a network

On a connected undirected network, one central vertex has degree five, five vertices have degree three, and ten have degree four. The vertices hold $3360$ coins and simultaneously split all coins equally among neighbors; every holding remains unchanged. Find the central holding.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Write the holding at vertex $v$ as $d(v)r_v$. Stationarity says $d(v)r_v=\sum_{u\sim v}r_u$, so $r_v$ is the average of its neighbors' ratios. At a maximum, all neighboring ratios equal that maximum; connectivity propagates equality everywhere. Thus holdings are proportional to degrees. The degree sum is $5+5\cdot3+10\cdot4=60$, giving $56$ coins per degree and central holding $5\cdot56=280$.

**Answer:** 280.

**Methods:** graphs, maximum principle, stationary distributions.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** The principal archived solution assumes equal holdings on symmetric rings. The maximum-principle argument proves uniqueness without that assumption. Audit findings: Source 1: Equal gifts are asserted without a uniqueness argument. Dividing holdings by vertex degree and applying the finite harmonic maximum principle supplies it. Source 3: Visual symmetry does not prove an arbitrary stationary allocation is symmetric. Use the harmonic maximum principle or sum the layer equations.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Stationarity on a connected graph is a linear averaging system with a maximum-principle invariant.

## 2012 AIME I Problem 9: Logarithmic coordinates expose a fixed monomial

Positive $x,y,z$ satisfy the defined nonzero common value
$$2\log_x(2y)=2\log_{2x}(4z)=\log_{2x^4}(8yz)\ne0.$$
Write $xy^5z=2^{-p/q}$ with coprime positive integers $p,q$, and find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Set $X=\log_2x$, $Y=\log_2y$, $Z=\log_2z$, and denote the common value by $k\ne0$. Every positive real number has such logarithmic coordinates, so this is no restriction. Change of base gives
$$2(Y+1)=kX,\quad2(Z+2)=k(X+1),\quad Y+Z+3=k(4X+1).$$
Adding the first two and comparing with twice the third yields $k(2X+1)=2k(4X+1)$, hence $X=-1/6$. Then $Y=-1-k/12$ and $Z=-2+5k/12$, giving
$$X+5Y+Z=-\frac{43}{6}.$$
The bases are legitimate because their base-two logarithms are $-1/6,5/6,1/3$, all nonzero. Any nonzero real $k$ in these formulas gives positive $y,z$ and realizes the equations, so the invariant is attained. Thus $p+q=43+6=49$.

**Answer:** 049.

**Methods:** logarithmic coordinates, linear elimination, monomial invariants.

**Verification:** Exact exponent identities hold symbolically for the free parameter k; sample rational values are independently checked.

**Source comparison:** All four stored entries inspected. The first assumes a convenient common value without proving the target is independent of it; the last contains incorrect parameter formulas. The new proof retains the free nonzero parameter throughout and verifies every logarithm base.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A common nonzero logarithm value cancels to determine one exponent and a weighted exponent sum.

## 2012 AIME I Problem 13: Equilateral triangles with three prescribed center distances

Three circles have a common center and radii $3,4,5$. Among equilateral triangles having one vertex on each circle, maximize the area. Write it as $a+(b/c)\sqrt d$, with positive integers, $b,c$ coprime and $d$ squarefree, and find $a+b+c+d$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Let the side length be $s>0$. Place the triangle at $A=(-s/2,0)$, $B=(s/2,0)$, $C=(0,\sqrt3s/2)$ and let the common circle center be $O=(u,v)$, with distances $OA=3$, $OB=4$, $OC=5$. Subtraction and addition of the first two squared-distance equations, followed by the third, give
$$u=-\frac7{2s},\qquad v=\frac{s^2-25}{2\sqrt3s},\qquad 2u^2+2v^2+\frac{s^2}{2}=25.$$
Substituting yields $s^4-50s^2+193=0$, hence
$$s^2=25\pm12\sqrt3.$$
Both values are positive. For either value, the displayed real coordinates $u,v$ satisfy all three original squared-distance equations: the last displayed equation and $2us=-7$ restore $OA^2=9,OB^2=16$, and the expression for $v$ restores $OC^2=25$. Thus both candidate shapes exist, regardless of whether their center is inside the triangle. Area increases with $s^2$, so the maximum is
$$\frac{\sqrt3}{4}(25+12\sqrt3)=9+\frac{25}{4}\sqrt3.$$
The required sum is $9+25+4+3=41$.

**Answer:** 041.

**Methods:** distance-difference linearization, equilateral triangles, quadratic elimination, attainment.

**Verification:** Substitution in the three distance equations verifies both positive squared-side roots.

**Source comparison:** All five stored alternatives inspected. They use a 60-degree rotation, angle equations, Fermat/pedal geometry, coordinates, or another rotation construction. The first assumes an interior center, while the coordinate route handles both configurations. The new proof explicitly reconstructs the center for both algebraic roots and therefore proves the maximum is attainable.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Subtracting distance equations determines the circle center and a quadratic in the squared side length, with a converse.

## 2012 AIME I Problem 14: A zero root sum places the triangle centroid at the origin

The complex roots $a,b,c$ of $z^3+qz+r$ form a nondegenerate right triangle in the complex plane and satisfy $|a|^2+|b|^2+|c|^2=250$. If its hypotenuse is $h$, find $h^2$. The coefficients $q,r$ need not be real.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Vieta gives $a+b+c=0$. Expanding squared complex distances gives the identity
$$|a-b|^2+|b-c|^2+|c-a|^2
=3(|a|^2+|b|^2+|c|^2)-|a+b+c|^2=750.$$
For a right triangle, the two leg squares add to the hypotenuse square, so the sum of all three side squares is $2h^2$. Consequently $h^2=750/2=375$. No conjugate-root symmetry or isosceles condition is needed.

**Answer:** 375.

**Methods:** Vieta formulas, centroids, squared-distance identity.

**Verification:** For arbitrary right-triangle legs, translating its centroid to zero gives total squared vertex norm two-thirds of its hypotenuse square.

**Source comparison:** All seven stored entries inspected. The second and fourth assume real coefficients or an isosceles triangle without authorization; a source comment recognizes this defect. The new proof works for arbitrary complex coefficients and needs only the zero root sum and the right angle.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. Vieta and the centroid squared-distance identity determine the hypotenuse without a real-coefficient assumption.

## 2012 AIME II Problem 2: Eliminate a geometric ratio without finding its sign

Two geometric progressions with the same nonzero common ratio satisfy $a_1=27$, $b_1=99$, and $a_{15}=b_{11}$. Find $a_9$. The nonzero-ratio convention is discussed in the source note.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

Let the common ratio be $r\ne0$. Then $27r^{14}=99r^{10}$, so division by $27r^{10}$ gives $r^4=11/3$. Hence
$$a_9=27r^8=27\left(\frac{11}{3}\right)^2=363.$$
Either real sign of the ratio gives the same answer. If a definition of geometric sequence allows ratio zero, the archived wording also permits $r=0$ and $a_9=0$; the reported answer uses the nonzero-ratio convention.

**Answer:** 363.

**Methods:** geometric progressions, power elimination, domain conventions.

**Verification:** Exact computation 27·(11/3)²=363; the r=0 alternative is separately verified.

**Source comparison:** The one stored solution inspected. It divides by the tenth power of the ratio without stating that the ratio is nonzero. The restatement explicitly states the convention required for the reported answer and records the additional zero-ratio case.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Source correction:** **Type:** zero_ratio_convention **Note:** The reviewed source wording does not explicitly exclude a zero common ratio. Under a definition allowing it, a9=0 is another possibility. The reported 363 requires a nonzero common ratio.

**Subject classification:** algebra. A shared nonzero ratio fixes its fourth power and therefore the requested eighth power.

## 2012 AIME II Problem 4: Three equal travel times determine a rectangle

From a rectangle's northeast corner, riders of speeds $8.6$, $6.2$, and $5$ m/s start together. The first follows the boundary westward, the second southward, and the third rides straight to a point $D$ on the south side. They first reach $D$ simultaneously. The east-west side is longer. Find the primitive ratio of length, width, and distance from the southeast corner to $D$, and report its three entries' sum.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Scale lengths so the common travel time is one second. Let the east-west length be $L$, north-south width $W$, and the southeast-to-$D$ distance $d$. The three route lengths give
$$2L+W-d=43/5,\qquad W+d=31/5,\qquad W^2+d^2=25.$$
Subtracting the first two yields $L-d=6/5$. Also $(W-d)^2=2(25)-(31/5)^2=(17/5)^2$, so $\{W,d\}=\{7/5,24/5\}$. If $W=24/5,d=7/5$, then $L=13/5<W$, forbidden. Thus $W=7/5,d=24/5,L=6$, with $0<d<L$. The ratio is $30:7:24$, and its entries sum to $61$.

**Answer:** 061.

**Methods:** rates, rectangle geometry, symmetric elimination, branch selection.

**Verification:** Exact squared-distance check (7/5)²+(24/5)²=25 and route lengths 43/5,31/5.

**Source comparison:** Both stored entries inspected. They derive the same unordered pair and use the long-side condition to choose it. The new exposition explicitly verifies that D lies inside the south edge.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Path lengths and a diagonal produce two symmetric dimensions, then the long-side condition selects the branch.

## 2012 AIME II Problem 6: A complex-distance maximum fixes a fourth power

Choose $z=a+bi$ with $|z|=5$ and $b>0$ to maximize $|(1+2i)z^3-z^5|$. If $z^4=c+di$, find $c+d$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Factor out $z^3$: the quantity is $125|1+2i-z^2|$. Since $|z^2|=25$, the triangle inequality bounds it by $125(\sqrt5+25)$. Equality requires $z^2$ to point directly opposite $1+2i$, so
$$z^2=-\frac{25}{\sqrt5}(1+2i).$$
This nonreal number has two opposite square roots, exactly one with positive imaginary part, so the bound is attained under the given restriction. Squaring the displayed equation gives
$$z^4=125(1+2i)^2=-375+500i.$$
Therefore $c+d=125$.

**Answer:** 125.

**Methods:** complex modulus, triangle inequality, equality feasibility.

**Verification:** The resulting fourth power has real and imaginary parts −375 and 500, with modulus 625 as required.

**Source comparison:** Both stored alternatives inspected. One uses vector direction and the other arguments. The new proof gives the explicit triangle-inequality equality condition and checks the upper-half-plane square-root restriction.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. The triangle inequality on a circle determines the maximizing direction and an attainable square-root branch.

## 2012 AIME II Problem 8: Solve directly for a complex product

Nonzero complex numbers $z,w$ obey $z+20i/w=5+i$ and $w+12i/z=-4+10i$. Find the minimum possible $|zw|^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Let $u=zw$. Multiplying the original equations gives
$$u+32i-\frac{240}{u}=-30+46i,$$
so
$$u^2+(30-14i)u-240=(u-6-2i)(u+36-12i)=0.$$
The two candidate squared moduli are $40$ and $1440$. The smaller one is feasible: $z=1-i$, $w=2+4i$ have product $6+2i$ and directly satisfy both original equations. Thus the minimum is $40$.

**Answer:** 040.

**Methods:** target elimination, complex quadratic, existence check.

**Verification:** Exact Gaussian-rational substitution of (1−i,2+4i) verifies both equations.

**Source comparison:** The sole stored entry inspected. It obtains the two product candidates but does not reconstruct z,w. The new proof includes an explicit nonzero pair attaining the smaller squared modulus; the stored auxiliary norm expansion also contains a minor typo.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Multiplying the equations eliminates the individual variables; a reconstruction proves the smaller root is feasible.

## 2012 AIME II Problem 9: Ratios determine squared trigonometric coordinates

Real angles $x,y$ satisfy $\sin x/\sin y=3$ and $\cos x/\cos y=1/2$. Express $\sin(2x)/\sin(2y)+\cos(2x)/\cos(2y)$ as a reduced positive fraction $p/q$ and find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

The sine double-angle ratio is the product of the two given ratios, hence $3/2$. Put $t=\sin^2y$. Squaring the original ratios and using $\sin^2x+\cos^2x=1$ gives $9t+(1-t)/4=1$, so $t=3/35$ and $\sin^2x=27/35$. Therefore
$$\frac{\cos2x}{\cos2y}=\frac{1-54/35}{1-6/35}=-\frac{19}{29}.$$
The denominator is nonzero, as are the two original denominators, so all target terms are defined. The sum is $3/2-19/29=49/58$, giving $p+q=107$.

**Answer:** 107.

**Methods:** trigonometric identities, squared coordinates, domain checks.

**Verification:** Exact rational calculation gives sin²y=3/35 and total 49/58.

**Source comparison:** All four stored entries inspected. They use squared sines, squared cosines, right triangles, or a direct substitution. The second reverses a displayed ratio before quoting the correct result, and the fourth has a final denominator-label typo. The new proof needs no assumption that the angles are acute.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. The Pythagorean identity and double-angle formulas evaluate the target without selecting angles.

## 2012 AIME II Problem 10: A floor-product range is a disjoint union of integer blocks

Count positive integers $n<1000$ representable as $x\lfloor x\rfloor$ for some positive real $x$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Let $k=\lfloor x\rfloor$. Since $n>0$, $k\ge1$. On $k\le x<k+1$, multiplication by $k$ maps the interval bijectively onto $[k^2,k(k+1))$. Hence its integer outputs are exactly
$$k^2,k^2+1,\ldots,k^2+k-1,$$
a set of $k$ values. These blocks are disjoint, because $k(k+1)<(k+1)^2$. The complete blocks for $1\le k\le31$ lie below $1000$, with last endpoint $31\cdot32-1=991$, while $k=32$ begins at $1024$. Therefore the count is $1+2+\cdots+31=496$. Every counted integer is attained at $x=n/k$, so this counts outputs, not merely necessary bounds.

**Answer:** 496.

**Methods:** floor functions, interval images, disjoint counting.

**Verification:** Enumeration by n with k=floor(√n) confirms exactly 496 representable values below 1000.

**Source comparison:** All four stored alternatives inspected. Some blur x and its integer part or write an incorrect endpoint before using the correct range. The new proof explicitly gives the bijection on each half-open interval and proves the output blocks disjoint.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Counting integer points in the disjoint images of floor intervals gives a triangular sum.

## 2012 AIME II Problem 11: A fractional-linear map has period three

Let $f(x)=2/3-3/(3x+1)$, and write $f^{\circ n}$ for its $n$-fold composition wherever all steps are defined. Solve $f^{\circ1001}(x)=x-3$; express the solution as a reduced positive fraction $m/n$ and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Write $f(x)=(6x-7)/(9x+3)$ and associate the matrix
$$M=\begin{pmatrix}6&-7\\9&3\end{pmatrix}.$$
Direct multiplication gives $M^3=-729I$, so $f^{\circ3}(x)=x$ wherever the iterates are defined. Since $1001\equiv2\pmod3$, the required equation becomes
$$\frac{3x+7}{6-9x}=x-3.$$
Clearing the nonzero denominator gives $(3x-5)^2=0$, hence the only candidate is $x=5/3$. Its orbit is $5/3\mapsto1/6\mapsto-4/3\mapsto5/3$; none is the pole $-1/3$, so all $1001$ iterates exist. Also the second image is $-4/3=5/3-3$, verifying the equation. Thus $m+n=8$.

**Answer:** 008.

**Methods:** fractional-linear iteration, matrix powers, domain verification.

**Verification:** Exact matrix multiplication gives M³=−729I; the rational three-cycle is checked directly.

**Source comparison:** The sole stored argument inspected. It recognizes the period from initial iterates but omits a proof and domain check. The new exposition proves the matrix identity and verifies the complete orbit of the candidate.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A scalar matrix cube establishes the iterate cycle, with orbit-domain verification.

## 2012 AIME II Problem 13: Sum squared distances before computing rotated vertices

An equilateral triangle $ABC$ has side $\sqrt{111}$. The two points $D_1,D_2$ satisfy $AD_i=\sqrt{111}$ and $BD_i=\sqrt{11}$. For each segment $AD_i$, construct both equilateral third vertices, giving four points $E_1,\ldots,E_4$. Find $\sum_{j=1}^4 CE_j^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Use vector coordinates with $A=0$, $B=(s,0)$, $C=(s/2,\sqrt3s/2)$ and $s^2=111$. Subtracting $|D_i-B|^2=11$ from $|D_i|^2=111$ gives $(D_i)_x=211/(2s)$. The two circle intersections have opposite vertical coordinates, so $D_1+D_2=(211/s,0)$.

The two equilateral third vertices built on $AD_i$ are the rotations $R_{60}D_i$ and $R_{-60}D_i$. Their sum is $2\cos60^\circ D_i=D_i$, and each has squared norm $111$. Therefore $\sum_jE_j=D_1+D_2$ and
$$\sum_{j=1}^4|C-E_j|^2
=4|C|^2+\sum_j|E_j|^2-2C\cdot\sum_jE_j
=888-211=677.$$
This computes the aggregate without evaluating any individual radical coordinate.

**Answer:** 677.

**Methods:** rotation sums, vector projections, squared distances.

**Verification:** The common horizontal projection is 211/(2√111); the four squared distances sum to 888−211.

**Source comparison:** All five stored alternatives inspected, using angle-sum cosines, complex rotations, or paired cosine rules. The new proof isolates the common cancellation as a two-rotation vector identity, avoiding the labeling and repeated-term typos in some entries.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Pairing opposite rotations cancels perpendicular components and leaves a single projection.

## 2013 AIME I Problem 1: Travel time in fixed speed ratios

A race consists of swimming $1/2$ mile, cycling $30$ miles, and running $8$ miles. The three constant speeds have ratio $1:10:5$. Total time is $255$ minutes. Find the cycling time in minutes.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

If the swimming speed is $v$, the three times are proportional to $(1/2)/v$, $30/(10v)$, and $8/(5v)$, hence to $5:30:16$. Cycling therefore occupies $30/51=10/17$ of the total time. Its duration is $255(10/17)=150$ minutes. The common speed is positive, so all three stages realize these time proportions.

**Answer:** 150.

**Methods:** rates, proportional reasoning.

**Verification:** Exact time ratio 5+30+16=51 and 255·30/51=150.

**Source comparison:** Inspected the one stored solution. It solves for swimming speed; the new exposition instead computes the requested time share directly.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Rate equations reduce to a single common reciprocal-speed factor.

## 2013 AIME I Problem 3: Area fractions determine a reciprocal side ratio

Two perpendicular cuts parallel to the sides partition a square into two squares and two nonsquare rectangles. Let $a,b$ be the two segment lengths into which either cut divides its perpendicular side. The two smaller squares occupy $9/10$ of the original area. Find $a/b+b/a$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

The two smaller squares must be diagonally opposite: adjacent square cells would force all four cells to be squares, contrary to the two nonsquare rectangles. Thus their sides are $a,b$, and each rectangle has sides $a,b$. Hence
$$a^2+b^2=\frac9{10}(a+b)^2,\qquad 2ab=\frac1{10}(a+b)^2.$$
Dividing gives $(a^2+b^2)/(ab)=18$, the requested sum. Positive unequal lengths exist: the ratio solves $t^2-18t+1=0$, with positive roots $9\pm4\sqrt5$.

**Answer:** 018.

**Methods:** square partitions, symmetric sums, area ratios.

**Verification:** The positive ratio roots have product one and sum eighteen.

**Source comparison:** All seven stored entries inspected. They use area complements, normalization, Vieta, or an explicit quadratic. The present argument retains the common invariant and explains why the square cells are opposite.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A square partition gives a symmetric ratio invariant from areas.

## 2013 AIME I Problem 5: A cubic hides a difference of cubes

Express the real root of $8x^3-3x^2-3x-1=0$ as $(\sqrt[3]a+\sqrt[3]b+1)/c$ with positive integers $a,b,c$, and determine $a+b+c$ in this form.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

The equation is exactly $9x^3=(x+1)^3$. Real cube roots are single-valued, so $(\sqrt[3]9-1)x=1$, proving there is exactly one real root. With $t=\sqrt[3]9$,
$$x=\frac1{t-1}=\frac{t^2+t+1}{t^3-1}=\frac{\sqrt[3]{81}+\sqrt[3]9+1}{8}.$$
Thus the indicated integers are $81,9,8$, whose sum is $98$.

**Answer:** 098.

**Methods:** difference of cubes, radical rationalization.

**Verification:** Direct expansion verifies 9x³−(x+1)³ equals the original polynomial.

**Source comparison:** All four stored entries inspected: direct cube recognition, reciprocal-polynomial recognition, a field-automorphism discussion, and coefficient matching. The cube identity supplies a complete real-root argument without the unproved field-structure assumptions in the third entry.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Recognizing a cube gives the real root and rationalizes its denominator.

## 2013 AIME I Problem 8: A function domain imposes an integer divisor

For positive integers $m>1,n$, the real domain of $\arcsin(\log_m(nx))$ has length $1/2013$. Find the least possible $m+n$, reduced modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

The logarithm must lie in $[-1,1]$, so the domain is $[1/(mn),m/n]$. Its length condition gives
$$n=2013m-\frac{2013}{m}.$$
Thus $m$ must divide $2013=3\cdot11\cdot61$. Conversely every divisor $m>1$ gives a positive integer $n$ and the required domain. The target $m+n=2014m-2013/m$ strictly increases for positive $m$, because its first term increases and its subtracted term decreases. The smallest allowed divisor is $m=3$, yielding $n=5368$ and $m+n=5371$. The remainder is $371$.

**Answer:** 371.

**Methods:** function domains, divisors, monotonicity.

**Verification:** Enumerating divisors of 2013 confirms the least admissible pair is (3,5368).

**Source comparison:** All three stored entries inspected. The divisor route is exact; the first entry uses an informal near-linearity argument, replaced here by strict monotonicity. The last begins with a mistaken bound on f rather than its arcsine input and uses a longer factor allocation.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Inverse-trigonometric domain constraints reduce the minimum to a divisor and monotonicity argument.

## 2013 AIME I Problem 10: Conjugate integer roots and distinct cubics

Consider all cubics $x^3-ax^2+bx-65$ with nonzero integers $a,b$ that have a root $r+si$ for nonzero integers $r,s$. For each distinct coefficient pair $(a,b)$, take the sum of its three roots. Find the sum of these values over all admissible pairs.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

The conjugate $r-si$ is also a root. The third root is $q=a-2r$, an integer, and coefficient comparison gives
$$q(r^2+s^2)=65,\qquad a=q+2r,\qquad b=r^2+s^2+2qr.$$
Since $r,s\ne0$, $q$ is a positive divisor of $65$ other than $65$. For $q=1,5,13$, the possible $r$ are respectively
$$\{\pm1,\pm4,\pm7,\pm8\},\quad\{\pm2,\pm3\},\quad\{\pm1,\pm2\}.$$
These lists follow by subtracting positive squares from $65,13,5$; only square complements are retained. For each listed $r$, the value of $s^2$ is fixed, and its two signs produce the same polynomial. Every listed $a$ is odd and nonzero; the formulas give nonzero $b$ as well. Distinct choices cannot duplicate a polynomial: its unique real root fixes $q$, and then $a$ fixes $r$.

By Vieta each root sum is $a=q+2r$. Pair $r$ with $-r$ in each list. The signed terms cancel, leaving $8\cdot1+4\cdot5+4\cdot13=80$.

**Answer:** 080.

**Methods:** complex conjugates, Vieta formulas, sum of two squares, finite classification, involution.

**Verification:** Exact integer enumeration finds sixteen distinct (a,b) pairs and sums a to eighty.

**Source comparison:** Inspected the sole stored argument. The new exposition adds why the third root is integral, excludes q=65, verifies the nonzero coefficient restrictions, and proves that the coefficient-pair count has no duplicates.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory, combinatorics. Distinct coefficient pairs require a finite classification modulo conjugation and a signed-pair cancellation.

## 2013 AIME I Problem 13: A self-similar union sums to one rational area

Begin with a triangle $AB_0C_0$ of side lengths $AB_0=12$, $B_0C_0=17$, $AC_0=25$. At each stage choose $B_n$ on $AB_{n-1}$ and $C_n$ on $AC_{n-1}$ so that, in the displayed vertex order,
$$AB_nC_n\sim B_{n-1}C_nC_{n-1}\sim AB_{n-1}C_{n-1}.$$
If the union of triangles $B_{n-1}C_nB_n$ for $n\ge1$ has reduced rational area $p/q$, determine $q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Heron's formula gives original area $\sqrt{27\cdot15\cdot10\cdot2}=90$. The similarity from $AB_0C_0$ to $B_0C_1C_0$ has scale $17/25$, hence $C_1C_0=289/25$ and $AC_1=336/25$. Thus the nested triangle $AB_1C_1$ has linear scale
$$t=\frac{336}{625}.$$
The same scale applies at every stage because all containing triangles are similar with the same ordered construction. The triangle $AB_0C_1$ has area $90t$, while $AB_1C_1$ has area $90t^2$; subtracting gives first target area $90t(1-t)$. Subsequent target triangles are scaled by successive factors $t^2$ in area. Their interiors are disjoint because each lies in the part removed from its containing nested triangle. Since $0<t<1$, the total is
$$\frac{90t(1-t)}{1-t^2}=\frac{90t}{1+t}=\frac{30240}{961}.$$
Now $961=31^2$ and $30240\equiv15\pmod{31}$, so the fraction is reduced. Therefore $q=961$.

**Answer:** 961.

**Methods:** similarity, geometric series, disjoint area decomposition.

**Verification:** Exact rational geometric-series computation gives 30240/961; gcd(30240,961)=1.

**Source comparison:** All four stored entries inspected. They sum either the target pieces or their complements. Several display inconsistent series powers or a missing original-area factor. The fourth incorrectly calls 961 prime; the final reduction here explicitly uses 961=31² and checks the numerator modulo 31.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Similar triangles produce disjoint geometric-series area contributions.

## 2013 AIME I Problem 14: Combine two trigonometric series into one complex series

For $\pi\le\theta<2\pi$, define the convergent series
$$P=\frac{\cos\theta}{2}-\frac{\sin2\theta}{4}-\frac{\cos3\theta}{8}+\frac{\sin4\theta}{16}+\cdots,$$
$$Q=1-\frac{\sin\theta}{2}-\frac{\cos2\theta}{4}+\frac{\sin3\theta}{8}+\frac{\cos4\theta}{16}+\cdots.$$
The four-term sign and sine/cosine patterns repeat, and the term of frequency $k$ has denominator $2^k$. Given $P/Q=2\sqrt2/7$, write $\sin\theta=-m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Absolute convergence permits pairing real and imaginary parts. With $z=ie^{i\theta}/2$, the displayed patterns give
$$Q+iP=\sum_{k=0}^{\infty}z^k=\frac{2}{2+\sin\theta-i\cos\theta}.$$
Rationalizing shows $Q>0$ and
$$\frac PQ=\frac{\cos\theta}{2+\sin\theta}.$$
Put $s=\sin\theta$. Squaring the given equation yields
$$49(1-s^2)=8(2+s)^2,\qquad (19s+17)(3s-1)=0.$$
The angle interval requires $s\le0$, so $s=-17/19$. The unsquared equation further requires positive cosine; the fourth-quadrant angle with this sine has $\cos\theta=6\sqrt2/19$ and indeed gives the required ratio. Thus the candidate is attained and $m+n=36$.

**Answer:** 036.

**Methods:** complex geometric series, trigonometric identities, domain restrictions.

**Verification:** Substitution s=−17/19 and cosθ=6√2/19 gives the unsquared ratio exactly.

**Source comparison:** All six stored entries inspected: angle-addition manipulations, two complex-series presentations, exponential splitting, and a real/imaginary equation. Several contain sign, variable-name, or denominator transcription errors. The new proof uses one absolutely convergent geometric series and verifies the cosine sign after squaring.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A complex geometric series compresses two alternating trigonometric sums, followed by a branch check.

## 2013 AIME II Problem 1: Convert a time by its fraction of a day

A decimal clock divides one day into $10$ hours of $100$ minutes each. At the instant corresponding to ordinary $6{:}36$ a.m., it reads $A{:}BC$. Determine the three-digit integer $100A+10B+C$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

Ordinary $6{:}36$ a.m. is $6\cdot60+36=396$ minutes after midnight, or $396/1440=11/40$ of a day. The decimal clock has $1000$ minutes per day, so it records $1000(11/40)=275$ elapsed minutes, displayed as $2{:}75$. The requested number is $275$.

**Answer:** 275.

**Methods:** unit conversion, proportions.

**Verification:** Exact fraction 396/1440 equals 11/40.

**Source comparison:** Both stored solutions inspected; one uses the conversion ratio and the other a day fraction. The newly written proof uses the latter invariant.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A unit conversion is a proportional equation.

## 2013 AIME II Problem 2: Nested logarithms impose a power-of-two divisor

For positive integers $a,b$, suppose $\log_2(\log_{2^a}(\log_{2^b}(2^{1000})))=0$. Sum the distinct possible values of $a+b$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

Undo the logarithms from outside inward. The outer argument must be one, its inner argument must be $2^a$, and therefore $1000/b=2^a$. Since $1000=2^3 5^3$ and $a>0$, the possible pairs are exactly $(1,500),(2,250),(3,125)$. All logarithms are defined for these pairs. Their sums $501,252,128$ are distinct and total $881$.

**Answer:** 881.

**Methods:** logarithms, prime valuations.

**Verification:** The three possibilities are exhaustive by the valuation v₂(1000)=3.

**Source comparison:** Both stored alternatives inspected. They differ only in the presentation of exponentiation and factorization. The new proof also checks domains and that summing pairs does not duplicate a value of a+b.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Undoing nested logarithms produces a prime-exponent restriction on integers.

## 2013 AIME II Problem 3: Half the burn time is a triangular-number boundary

A candle initially has height $119$ cm. Its $k$th centimeter from the top takes $10k$ seconds to burn. At half of its total burn time, its remaining height is $h$ cm. Determine $10h$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

The total time is $10(119\cdot120/2)=71400$ seconds. Burning the first $84$ centimeters takes $10(84\cdot85/2)=35700$ seconds, exactly half the total. Since every centimeter takes positive time, this is the unique cumulative boundary at the specified time. Thus $h=119-84=35$ and $10h=350$. No assumption about the speed within a centimeter is necessary, because the time lands exactly at a boundary.

**Answer:** 350.

**Methods:** arithmetic series, triangular numbers.

**Verification:** 119·120=2·84·85 verifies the exact halfway boundary.

**Source comparison:** The sole stored solution inspected. The new explanation notes that the stated per-centimeter totals suffice even without a rule for within-centimeter speed.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. An arithmetic-series cumulative time determines the consumed length.

## 2013 AIME II Problem 7: Staff reductions force a unique feasible integer solution

Each clerk sorts $30$ files per hour. Starting with $x$ clerks, the same positive number $t$ leaves after each of the first three hours. The remaining group finishes $1775$ files at time $3$ hours $10$ minutes. How many files were sorted during the first $90$ minutes?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

The total work equation is
$$30x+30(x-t)+30(x-2t)+5(x-3t)=1775,$$
so $19x-21t=355$. Modulo nineteen this forces $t\equiv3\pmod{19}$. Hence $t=3+19k$ and $x=22+21k$, where positivity of $t$ requires $k\ge0$. The final workforce must be positive because work continues for the last ten minutes; thus $x-3t=13-36k>0$, forcing $k=0$. This proves uniqueness rather than just selecting the least congruence solution. The first ninety minutes produce $30x+15(x-t)=660+285=945$ files.

**Answer:** 945.

**Methods:** rates, linear Diophantine equations, feasibility.

**Verification:** Exact enumeration of positive x,t with x>3t and 19x−21t=355 finds only (22,3).

**Source comparison:** Both stored solutions inspected. Each selects the smallest positive congruence solution without excluding larger ones. The new proof uses the positive workforce in the final interval to establish that the candidate is the only feasible solution.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. A rate equation and a linear congruence must be combined with a positive final workforce.

## 2013 AIME II Problem 12: Cubics with roots on two circles

Count monic integer-coefficient cubics all of whose complex roots have modulus either $13$ or $20$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

If all roots are real, they form a multiset of size three from $\{-20,-13,13,20\}$, giving $\binom63=20$. Otherwise there is one real root $r$ from those four values and a conjugate pair of modulus $R\in\{13,20\}$. Its quadratic factor is $z^2-tz+R^2$, where $t$ must be integral because the cubic's quadratic coefficient is integral and $r$ is integral. Nonreal roots require $|t|<2R$, giving $51$ or $79$ choices. Each choice yields integral coefficients and a unique cubic. Thus the count is $20+4(51+79)=540$.

**Answer:** 540.

**Methods:** multisets, algebraic enumeration.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: The squared magnitude is called the magnitude. The coefficient argument is correct after that distinction. Source 2: The discriminant condition needs an absolute value on p, and its displayed square root contains an extraneous square.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Conjugate-root structure and multiset counting classify integer-coefficient cubics.

## 2013 AIME II Problem 15: A triangle identity with a radical-sign branch condition

Triangle angles $A,B,C$ satisfy
$$\cos^2A+\cos^2B+2\sin A\sin B\cos C=15/8,$$
$$\cos^2B+\cos^2C+2\sin B\sin C\cos A=14/9.$$
The expression $\cos^2C+\cos^2A+2\sin C\sin A\cos B$ has the form $(p-q\sqrt r)/s$ for positive integers $p,q,r,s$, with $r$ squarefree and $\gcd(p+q,s)=1$. Determine $p+q+r+s$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

The sine rule permits a similar triangle with sides $\sin A,\sin B,\sin C$. Applying the cosine rule to it gives
$$\sin^2A+\sin^2B-2\sin A\sin B\cos C=\sin^2C.$$
Thus the first given expression equals $2-\sin^2C$; cyclically, the second equals $2-\sin^2A$, and the target equals $2-\sin^2B$. We obtain $\sin A=2/3$ and $\sin C=1/\sqrt8$.

Let $A_0,C_0$ be the acute angles with those sines. Since $A_0>C_0$, taking $C=\pi-C_0$ would force $A+C>\pi$, so $C=C_0$ and $\cos C=\sqrt{14}/4$. There remain two legitimate triangle branches, $A=A_0$ and $A=\pi-A_0$. Using $\sin B=\sin(A+C)$ gives
$$\sin^2B=\frac{33\pm4\sqrt{35}}{72},\qquad
2-\sin^2B=\frac{111\mp4\sqrt{35}}{72}.$$
The stipulated representation has a negative irrational term with a positive coefficient, so uniqueness of squarefree radical representation selects the minus sign in the target. This branch is feasible: $A_0,C_0$ are positive acute angles with sum less than $\pi$. Finally $\gcd(111+4,72)=1$, and the answer is $111+4+35+72=222$.

Without the stipulated negative-radical form, the two equations alone would allow both displayed target values.

**Answer:** 222.

**Methods:** sine rule, cosine rule, trigonometric identities, branch selection.

**Verification:** Both acute/supplementary A branches satisfy the two given equations; only the acute branch gives the specified negative radical coefficient.

**Source comparison:** All six stored entries inspected. They all choose positive cosines without proving the angle branch; one comment mentions an acute-triangle wording not present in the reviewed statement. The new solution keeps both feasible branches and uses the explicitly prescribed negative-radical form to select the requested one. Other sign/transcription errors in the alternatives do not affect the independently derived identity.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Source correction:** **Type:** missing_branch_argument_in_sources **Note:** The given equations allow two triangle shapes. The positive q in the prescribed p−q√r form selects the intended target; no blanket acute-triangle assumption is made.

**Subject classification:** geometry, algebra. The sine-rule cosine identity simplifies the expressions, but the prescribed radical sign is needed to select an angle branch.

## 2014 AIME I Problem 4: Two trains passing opposite cyclists

Two cyclists ride east and west at 20 mph. Two equal-length trains travel in opposite directions and each passes the eastbound cyclist in one minute. The westbound train takes ten times as long as the eastbound train to pass the westbound cyclist. If train length is $m/n$ miles in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Let the eastbound and westbound train speeds be $u,v$ mph. Their relative speeds past the eastbound cyclist are equal, so $u-20=v+20$, giving $u=v+40$. The other passing-time ratio gives $u+20=10(v-20)$. Hence $v=260/9$ and the common passing speed is $440/9$ mph. A one-minute pass therefore gives length $(440/9)/60=22/27$ miles, and the answer is $49$.

**Answer:** 049.

**Methods:** relative motion, linear systems.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three sources use the same relative-speed equations, interpreting a train passing a same-direction cyclist as overtaking that cyclist.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Two trains passing opposite cyclists; relative motion, linear systems supply the essential reduction.

## 2014 AIME I Problem 6: Two parabolas with a shared axis

The parabolas $y=3(x-h)^2+j$ and $y=2(x-h)^2+k$ have vertical intercepts 2013 and 2014. Each has two positive integer horizontal intercepts. Find $h$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

The first pair of roots has product $2013/3=671=11\cdot61$ and sum $2h$. Its possible unordered pairs are $(1,671)$ and $(11,61)$, with sums $672,72$. The second pair has product $2014/2=1007=19\cdot53$, giving pairs $(1,1007)$ and $(19,53)$ with sums $1008,72$. The common sum must be $72$, so $h=36$; both indicated factor pairs verify existence.

**Answer:** 036.

**Methods:** Vieta formulas, divisor pairs.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six sources inspected. Several omit the factor pair containing 1 or use an incorrect quadratic-formula denominator. Listing all positive factor pairs makes uniqueness immediate without assuming the answer is an integer.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Two parabolas with a shared axis; Vieta formulas, divisor pairs supply the essential reduction.

## 2014 AIME I Problem 7: The largest argument seen from an exterior point

Complex numbers satisfy $|w|=1$ and $|z|=10$. Let $\theta=\arg((w-z)/z)$. If the maximum of $\tan^2\theta$ is $p/q$ in lowest terms, find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

The complex number $w/z-1$ ranges over the circle of radius $1/10$ centered at $-1$. Its greatest angle away from the negative real axis occurs on a tangent ray from the origin. The resulting right triangle has hypotenuse $1$, opposite leg $1/10$, and adjacent leg $\sqrt{99}/10$. Therefore the largest squared tangent is $1/99$, giving $p+q=100$.

**Answer:** 100.

**Methods:** complex loci, tangent extremum.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three sources inspected. Differentiation, an AM-GM cosine bound, and the tangent-circle construction agree. The geometric tangent proof avoids calculus.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. The largest argument seen from an exterior point; complex loci, tangent extremum supply the essential reduction.

## 2014 AIME I Problem 9: A cubic designed around a radical

The real roots of $\sqrt{2014}x^3-4029x^2+2=0$ are $x_1<x_2<x_3$. Find $x_2(x_1+x_3)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

For $t=\sqrt{2014}$, the polynomial factors as $(tx-1)(x^2-2tx-2)$. The quadratic has one negative root and one root greater than $2t$, so the middle root is $1/t$. Its two companion roots sum to $2t$ by Vieta. Consequently $x_2(x_1+x_3)=(1/t)(2t)=2$.

**Answer:** 002.

**Methods:** factorization, root ordering, Vieta formulas.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight sources inspected. Direct factorization or scaling x removes the radical efficiently. Several alternatives infer integrality from the AIME answer format, and the final estimation argument explicitly is not a proof; the independent factorization needs neither assumption.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A cubic designed around a radical; factorization, root ordering, Vieta formulas supply the essential reduction.

## 2014 AIME I Problem 13: A square cut by equal perpendicular chords

Points $E,F,G,H$ lie respectively on sides $AB,BC,CD,DA$ of a square. Segments $EG,FH$ are perpendicular, each of length 34, and meet at $P$. The areas $AEPH,BFPE,CGPF,DHPG$ have ratio $269:275:405:411$. Find the square area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Let the side be $s$, with $A=(0,s),B=(0,0),C=(s,0),D=(s,s)$, and put $t=G_y-E_y$. The lower trapezoid has half the square area, so $E_y=(s-t)/2$ and $G_y=(s+t)/2$. Perpendicularity gives $H_x-F_x=-t$; the right trapezoid has area $3s^2/5$, giving $F_x+H_x=4s/5$. Thus the segment midpoints are $Q=(s/2,s/2)$ and $R=(2s/5,s/2)$. The right triangle $PQR$ has legs $s^2/(10\cdot34)$ and $st/(10\cdot34)$. Subtracting the equal corner triangles, or applying the shoelace formula to these coordinates, gives $[DHPG]=3s^2/10+[PQR]$. Since $411/1360-3/10=3/1360$, we obtain $st/34^2=15/34$, hence $st=510$. Also $s^2+t^2=34^2=1156$. Therefore $s^2$ is either $850$ or $306$; the latter would make the square diagonal shorter than 34. The area is $850$.

**Answer:** 850.

**Methods:** area ratios, perpendicular projections, quadratic elimination.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four sources inspected. Two rigorous area/projection arguments and a related similarity calculation agree. Index 2 merely guesses Pythagorean-type representations from the answer format and is not used as a proof.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A square cut by equal perpendicular chords; area ratios, perpendicular projections, quadratic elimination supply the essential reduction.

## 2014 AIME I Problem 14: Centering symmetric rational poles

Let $m$ be the largest real solution of $3/(x-3)+5/(x-5)+17/(x-17)+19/(x-19)=x^2-11x-4$. Write $m=a+\sqrt{b+\sqrt c}$ with positive integers $a,b,c$, and find $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Add $4$ to both sides. For $x\ne0$, division by $x$ gives $\sum_{r\in\{3,5,17,19\}}1/(x-r)=x-11$. Put $y=x-11$ and pair opposite poles: $2y/(y^2-64)+2y/(y^2-36)=y$. Besides $x=0$ and $y=0$, set $z=y^2$ to get $z^2-104z+2504=0$. Its roots are $52\pm\sqrt{200}$, both nonnegative and neither a pole. The greatest solution is $11+\sqrt{52+\sqrt{200}}$, larger than the separately retained roots 0 and 11. Thus $a+b+c=263$.

**Answer:** 263.

**Methods:** symmetric poles, substitutions, extraneous-root control.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** The sole source uses the same centered substitutions but discards 0 and 11 by appealing to the answer format. This proof retains them and compares them with the genuine largest root.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Centering symmetric rational poles; symmetric poles, substitutions, extraneous-root control supply the essential reduction.

## 2014 AIME I Problem 15: A circle through a right-triangle vertex

In right triangle $ABC$, $AB=3,BC=4,AC=5$. A circle meets $AB$ at $B,E$, $BC$ at $B,D$, and $AC$ at $F,G$. Suppose $EF=DF$ and $DG/EG=3/4$. Write $DE=a\sqrt b/c$ in reduced radical form and find $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Use $B=(0,0),A=(0,3),C=(4,0)$, $D=(d,0),E=(0,e)$. Since $\angle DBE=90^\circ$, $DE$ is a diameter. Equal chords $DF,EF$ subtend equal angles at $B$, so $BF$ bisects the right angle; intersecting $y=x$ with $3x+4y=12$ gives $F=(12/7,12/7)$. The chord ratio is $DG/EG=\sin\angle DBG/\sin\angle EBG=G_y/G_x=3/4$, so $G=(2,3/2)$. The circle through $B,D,E$ has equation $x^2+y^2=dx+ey$. Substituting $F,G$ yields $d+e=24/7$ and $4d+3e=25/2$. Hence $d=31/14,e=17/14$, and $DE=\sqrt{d^2+e^2}=25\sqrt2/14$. The answer is $41$.

**Answer:** 041.

**Methods:** equal chords, angle bisectors, circle equations.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All seven sources inspected. Equal chords identify the angle bisector and the 3:4 chord ratio identifies the hypotenuse midpoint. Source methods finish with power of a point, Ptolemy, or trigonometry; a circle equation supplies a compact independent finish.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A circle through a right-triangle vertex; equal chords, angle bisectors, circle equations supply the essential reduction.

## 2014 AIME II Problem 1: Changing work rates as painters join

Abe paints a room in 15 hours; Bea works 50 percent faster and Coe twice as fast as Abe. Abe works alone for 90 minutes, then Bea joins until half the room is painted, then Coe joins until completion. Find total elapsed minutes.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

The hourly rates are $1/15,1/10,2/15$. Abe first completes $1/10$ of the room. The next $2/5$ takes $(2/5)/(1/6)=12/5$ hours with Abe and Bea; the final half takes $(1/2)/(3/10)=5/3$ hours with all three. Total time is $90+144+100=334$ minutes.

**Answer:** 334.

**Methods:** work-rate equations, piecewise rates.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** The single stored source uses the same phase-by-phase rate calculation.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Changing work rates as painters join; work-rate equations, piecewise rates supply the essential reduction.

## 2014 AIME II Problem 4: Compatible repeating blocks

Digits $a,b,c$ satisfy $0.\overline{ab}+0.\overline{abc}=33/37$. Find the three-digit integer $100a+10b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Put $u=10a+b$. Then $u/99+(10u+c)/999=33/37$, which simplifies to $221u+11c=9801$. Reducing modulo 11 gives $u\equiv0\pmod{11}$, so $a=b$. Substitution yields $221a+c=891$. Since $0\le c\le9$, necessarily $a=4,c=7$. The requested number is 447.

**Answer:** 447.

**Methods:** repeating decimals, denominator cancellation, digit bounds.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four sources inspected. The denominator factor 11 forces equal first two digits; this avoids carrying through six-digit repeating blocks.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Compatible repeating blocks; repeating decimals, denominator cancellation, digit bounds supply the essential reduction.

## 2014 AIME II Problem 5: Two cubics with translated roots

Two roots of $p(x)=x^3+ax+b$ are $r,s$; two roots of $q(x)=x^3+ax+b+240$ are $r+4,s-3$. Find the sum of all possible values of $|b|$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Vieta gives the third roots $-r-s$ and $-r-s-1$. Equating the linear coefficients yields $rs-(r+s)^2=(r+4)(s-3)-(r+s+1)^2$, hence $s=(5r+13)/2$. Since $p(s)=0$, we have $q(s)=240$; its factored form gives $3(s-r-4)(r+2s+1)=240$. Substituting for $s$ reduces this to $(3r+5)(3r+7)=80$, or $r^2+4r-5=0$. Thus $(r,s)=(1,9)$ or $(-5,-6)$. The constant term is $b=rs(r+s)$, giving $90$ or $-330$. Both factorizations meet the conditions, so the requested sum is 420.

**Answer:** 420.

**Methods:** Vieta formulas, translated roots, evaluating factored polynomials.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four sources inspected. Comparing root sums and the linear coefficient gives a linear relation; evaluating q at s avoids the longer constant-term expansion.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Two cubics with translated roots; Vieta formulas, translated roots, evaluating factored polynomials supply the essential reduction.

## 2014 AIME II Problem 7: An alternating logarithmic product

Let $f(x)=(x^2+3x+2)^{\cos(\pi x)}$. Find the sum of positive integers $n$ satisfying $|\sum_{k=1}^n\log_{10}f(k)|=1$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

For integer $k$, the exponent is $(-1)^k$ and the base is $(k+1)(k+2)$. Telescoping gives $\prod_{k=1}^n f(k)=(n+2)/2$ for even $n$, and $1/[2(n+2)]$ for odd $n$. The absolute logarithm equals 1 exactly when this product is 10 or 1/10. The even case yields $n=18$ and the odd case $n=3$. Their sum is 21.

**Answer:** 021.

**Methods:** telescoping products, parity, logarithms.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both stored solutions use the same parity-dependent telescoping, one at the product level and one at the logarithm level.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. An alternating logarithmic product; telescoping products, parity, logarithms supply the essential reduction.

## 2014 AIME II Problem 8: Three mutually tangent circles and a diameter

A radius-2 circle has diameter $AB$. A smaller circle is internally tangent at $A$. A third circle is internally tangent to the large circle, externally tangent to the second circle, and tangent to $AB$. The second radius is three times the third. Write it as $\sqrt m-n$ and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Let the third radius be $r$. Put the large center at $(0,0)$ and $A=(-2,0)$; the second center is $(3r-2,0)$. Reflect if necessary so the third center is $(x,r)$. Its distance to the second center is $4r$, so their horizontal separation is $\sqrt{15}r$. The left-hand choice would give $x=(3-\sqrt{15})r-2<-2$, impossible inside the large circle. Hence $x=(3+\sqrt{15})r-2$. Internal tangency gives $x^2+r^2=(2-r)^2$. Removing the positive factor $r$ yields $(24+6\sqrt{15})r=8+4\sqrt{15}$. Thus $3r=4\sqrt{15}-14=\sqrt{240}-14$, and the answer is 254.

**Answer:** 254.

**Methods:** circle tangency, distance equations.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four sources inspected. Direct coordinates, a cosine-law calculation, and Descartes after reflection agree. The independent coordinate argument checks the horizontal-sign choice explicitly.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Three mutually tangent circles and a diameter; circle tangency, distance equations supply the essential reduction.

## 2014 AIME II Problem 10: A reciprocal equation creates an equilateral triangle

Let $|z|=2014$. Form the polygon with vertices $z$ and all complex $w$ satisfying $1/(z+w)=1/z+1/w$. Its area is $n\sqrt3$. Find $n$ modulo 1000.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

The equation becomes $w^2+wz+z^2=0$, so $w/z$ is one of the two nontrivial cube roots of unity. The three vertices therefore form an equilateral triangle with circumradius 2014 and area $(3\sqrt3/4)2014^2=3\cdot1007^2\sqrt3$. Thus $n\equiv3\cdot7^2=147\pmod{1000}$.

**Answer:** 147.

**Methods:** roots of unity, complex ratios, regular polygons.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four sources inspected. Algebraic factorization, direct coordinates, and complex-angle interpretations all identify the equilateral triangle.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. A reciprocal equation creates an equilateral triangle; roots of unity, complex ratios, regular polygons supply the essential reduction.

## 2014 AIME II Problem 11: An isosceles extension of a triangle

In triangle $RED$, angles at $R,E$ are 75 and 45 degrees and $RD=1$. Let $M$ be the midpoint of $RD$, and choose $C$ on $ED$ with $RC\perp EM$. Extend $DE$ beyond $E$ to $A$ so that $AC=AR$. If $AE=(a-\sqrt b)/c$ in reduced form, find $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Let $P$ be the foot from $A$ to $RC$. Since $AC=AR$, $P$ is the midpoint of $RC$. The midpoint theorem gives $PM\parallel CD$ and $PM=CD/2$; also $AP\parallel EM$. Thus $APME$ is a parallelogram and $AE=CD/2$. Set $D=(0,0)$, $R=(1/2,\sqrt3/2)$, $E=((1+\sqrt3)/2,0)$. Then $M=(1/4,\sqrt3/4)$, and perpendicular slopes give $C_x=(\sqrt3-1)/(1+2\sqrt3)$. Consequently $AE=(\sqrt3-1)/(2+4\sqrt3)=(7-3\sqrt3)/22=(7-\sqrt{27})/22$, giving 56.

**Answer:** 056.

**Methods:** midpoint theorem, perpendicular slopes, isosceles triangles.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three source solutions inspected. The midpoint-parallelogram relation reduces the construction to CD/2; direct coordinates then give the required radical.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. An isosceles extension of a triangle; midpoint theorem, perpendicular slopes, isosceles triangles supply the essential reduction.

## 2014 AIME II Problem 12: A triple-angle condition forces one angle

Triangle angles satisfy $\cos3A+\cos3B+\cos3C=1$. Two sides have lengths 10 and 13. The greatest possible third side is $\sqrt m$; find $m$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Since $C=\pi-A-B$, the condition becomes $\cos3A+\cos3B-\cos(3A+3B)-1=0$. Sum-to-product factors the left side as $4\sin(3A/2)\sin(3B/2)\cos(3(A+B)/2)$. With positive triangle angles, its vanishing means $A=120^\circ$, $B=120^\circ$, or $C=120^\circ$. Conversely each case satisfies the condition. To maximize the unknown side, put it opposite that 120-degree angle; any other placement makes it shorter than the known longest side 13. The cosine law gives $m=10^2+13^2-260\cos120^\circ=399$.

**Answer:** 399.

**Methods:** trigonometric factorization, cosine law, extremal side length.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four sources inspected. The sum-to-product solution is complete. The first introduces unsigned square roots for sine values, and the last simply guesses 120 degrees from answer integrality; these arguments are not used.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A triple-angle condition forces one angle; trigonometric factorization, cosine law, extremal side length supply the essential reduction.

## 2015 AIME I Problem 1: Pairing two alternating product sums

Let $A=1\cdot2+3\cdot4+\cdots+37\cdot38+39$ and $B=1+2\cdot3+4\cdot5+\cdots+38\cdot39$. Find $|A-B|$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

Pair terms sharing the even factor: $B-A=1-39+\sum_{j=1}^{19}[2j(2j+1)-(2j-1)2j]=-38+4\sum_{j=1}^{19}j=-38+760=722$.

**Answer:** 722.

**Methods:** telescoping differences, arithmetic sums.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Pairing by the shared even factor is shortest. The finite-difference alternative contains inconsistent listed first differences; direct subtraction avoids these slips.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Pairing two alternating product sums; telescoping differences, arithmetic sums supply the essential reduction.

## 2015 AIME I Problem 9: When a multiplicative recurrence reaches zero

For $1\le x, y, z\le 10$ initialize $a_1=x, a_2=y, a_3=z$ and $a_n=a_{n-1}|a_{n-2}-a_{n-3}|$. Count initial triples whose sequence eventually reaches zero.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Write $d=|y-x|$ and $e=|z-y|$. If $d$ or $e$ is $0$ or $1$, a zero or adjacent equality occurs and eventually forces zero. If $d, e\ge 2$, then $a_4=zd, a_5=zde$. The exceptional case $z=1, d=2$ gives $a_6=a_5$ and hence zero. Otherwise $a_4-a_3=z(d-1)\ge 2$ and $a_5-a_4=zd(e-1)\ge 2$. Thereafter each multiplier is at least two, preserving positive gaps of at least two, so zero is impossible. The first two events each contain $280$ triples; their intersection has $2\cdot2^2+8\cdot3^2=80$. The exceptional condition adds $14$ new triples. Total: $280+280-80+14=494$.

**Answer:** 494.

**Methods:** recurrence invariants, inclusion-exclusion.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The source growth argument is informal; the invariant on successive differences makes the exclusion rigorous.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. When a multiplicative recurrence reaches zero; the proof uses recurrence invariants, inclusion-exclusion.

## 2015 AIME I Problem 10: A cubic attaining only two levels

A real cubic polynomial $f$ satisfies $|f(j)|=12$ for $j=1,2,3,5,6,7$. Find $|f(0)|$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

Each of $f-12$ and $f+12$ has at most three roots, so each contains exactly three of the six given inputs. Their leading and quadratic coefficients agree, so the two root triples have equal sums, necessarily 12. The only partition into such triples is $\{1,5,6\}$ and $\{2,3,7\}$. Put $P=(x-1)(x-5)(x-6)$ and $Q=(x-2)(x-3)(x-7)$; their expansions show $P-Q=12$. The two polynomial levels differ by 24, so the leading coefficient has magnitude 2. Taking $f-12=-2P$ gives $f(0)=72$; reversing signs gives $-72$. Thus $|f(0)|=72$.

**Answer:** 072.

**Methods:** root counting, Vieta formulas, polynomial level sets.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All nine alternatives inspected. Root partition and coefficient comparison rigorously force the level assignment; several sketches merely assume its shape, and the last guesses the leading coefficient from answer integrality.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A cubic attaining only two levels; root counting, Vieta formulas, polynomial level sets supply the essential reduction.

## 2015 AIME I Problem 13: A product over all odd degree angles

Write $\prod_{k=1}^{45}\csc^2((2k-1)^\circ)=m^n$ with integers $m,n>1$. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

The roots of $z^{90}+1$ are $e^{(2k-1)\pi i/90}$ for $1\le k\le90$. Evaluate the factored polynomial at 1 and take absolute values: $2=2^{90}\prod_{k=1}^{90}\sin((2k-1)^\circ)$. Pairing complementary angles about 90 degrees shows the product on the right equals the square of the product for $k=1,\ldots,45$. The requested reciprocal square is consequently $2^{89}$. Since 89 is prime and $m,n>1$ are integers, $m=2,n=89$, giving 91.

**Answer:** 091.

**Methods:** roots of unity, trigonometric products, prime exponents.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All seven alternatives inspected. Repeated double-angle cancellation also works; evaluating a roots-of-unity polynomial supplies the general identity directly. Several displayed angle/product indices in the longer alternatives have typographical errors.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A product over all odd degree angles; roots of unity, trigonometric products, prime exponents supply the essential reduction.

## 2015 AIME I Problem 14: Parity of piecewise-linear area

Let $A(n)$ be the area under $y=x \lfloor\sqrt{x}\rfloor$ from $x=1$ to $x=n$. Count $2\le n\le 1000$ for which $A(n)$ is integral.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Put $m=\lfloor\sqrt n\rfloor$. Twice the area is $\sum_{k=1}^{m-1}k((k+1)^4-k^4)+m(n^2-m^4)$, whose parity is $mn-m(m+1)/2$. Therefore $m\equiv0 \pmod{4}$ always works; $m\equiv2 \pmod{4}$ never works; $m\equiv1 \pmod{4}$ requires odd $n$; $m\equiv3 \pmod{4}$ requires even $n$. The full even-$m$ blocks contribute $\sum_{j=1}^7(8j+1)=231$. Odd-$m$ blocks $m=1,5,\ldots,29$ contribute $128$; blocks $m=3,7,\ldots,27$ contribute $105$; $m=31$ contributes $20$. Exclude $n=1$: total $231+128+105+20-1=483$.

**Answer:** 483.

**Methods:** parity, block counting.

**Verification:** Exact parity formula and block counts independently reproduce 483.

**Source comparison:** The first archived solution reverses odd-block parity and incorrectly counts half an odd block. Its reversed parity conditions happen to cancel in the final count.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Parity of piecewise-linear area; the proof uses parity, block counting.

## 2015 AIME II Problem 4: Logarithmic lengths form a familiar triangle

An isosceles trapezoid has bases $\log3,\log192$ and altitude $\log16$, with a common logarithm base greater than 1. Its perimeter is $\log(2^p3^q)$. Find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Put $L=\log2$. Half the base difference is $\tfrac12\log64=3L$, and the altitude is $4L$. Each leg is therefore $5L$. The perimeter is $\log3+\log192+10L=16\log2+2\log3=\log(2^{16}3^2)$. The answer is 18.

**Answer:** 018.

**Methods:** logarithm laws, isosceles trapezoids, Pythagorean triples.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Each reduces to a 3-4-5 triangle; one changes the logarithm base without explaining that this uniformly rescales all lengths.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Logarithmic lengths form a familiar triangle; logarithm laws, isosceles trapezoids, Pythagorean triples supply the essential reduction.

## 2015 AIME II Problem 6: Two possible cubics with positive integer roots

The polynomial $2x^3-2ax^2+(a^2-81)x-c$ has three positive integer roots, counted with multiplicity. Knowing $a$ still leaves exactly two possible values of $c$. Find their sum.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

For roots $u\le v\le w$, Vieta gives $u+v+w=a$ and $2(uv+uw+vw)=a^2-81$. Subtraction yields $u^2+v^2+w^2=81$. Here $u\le5$; for each $u=1,2,3,4,5$, testing $u\le v\le\sqrt{(81-u^2)/2}$ gives respectively $(v,w)=(4,8)$, none, $(6,6)$, $(4,7)$, none. Thus the triples are $(1,4,8),(3,6,6),(4,4,7)$, with sums 13,15,15. The ambiguity forces $a=15$, and $c=2uvw$ is 216 or 224. Their sum is 440.

**Answer:** 440.

**Methods:** Vieta formulas, sums of three squares, bounded enumeration.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. The sum-of-squares reduction is complete. The derivative alternative assumes the stationary point is an integer without justification and is not used.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Two possible cubics with positive integer roots; Vieta formulas, sums of three squares, bounded enumeration supply the essential reduction.

## 2015 AIME II Problem 8: An integer inequality bounds a cubic quotient

Positive integers $a,b$ satisfy $(ab+1)/(a+b)<3/2$. If the largest possible value of $(a^3b^3+1)/(a^3+b^3)$ is $p/q$ in lowest terms, find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Assume $a\le b$. The given inequality is equivalent to $(2a-3)(2b-3)<5$. If $a=1$, the objective equals 1. If $a\ge2$, both factors are positive odd integers, so the only unordered possibilities are $(a,b)=(2,2),(2,3)$. Their objective values are $65/16$ and $217/35=31/5$. The latter is greatest, giving 36.

**Answer:** 036.

**Methods:** shifted product bounds, finite integer optimization.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. The factored inequality gives an exhaustive classification. The last two alternatives rely on unproved optimization claims or guesses; they are unnecessary.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. An integer inequality bounds a cubic quotient; shifted product bounds, finite integer optimization supply the essential reduction.

## 2015 AIME II Problem 13: Negative partial sums of successive sines

For $n\ge1$, let $a_n=\sum_{k=1}^n\sin k$, with angles in radians. Find the index of the hundredth negative term.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Telescoping $2\sin(1/2)\sin k=\cos(k-1/2)-\cos(k+1/2)$ gives $a_n=\sin(n/2)\sin((n+1)/2)/\sin(1/2)$. The denominator is positive. The two numerator factors have opposite signs exactly when a multiple $k\pi$ lies strictly between $n/2$ and $(n+1)/2$. Thus $2\pi k-1<n<2\pi k$. Each such interval for positive integer $k$ contains exactly one integer, namely $\lfloor2\pi k\rfloor$, since $\pi$ is irrational. The hundredth is $\lfloor200\pi\rfloor=628$.

**Answer:** 628.

**Methods:** trigonometric telescoping, irrational rotations, floor sequences.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Product-to-sum and geometric series yield equivalent sign conditions. The complex-argument alternative has loose wording about a complex number being negative; the real sine sign test is precise.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Negative partial sums of successive sines; trigonometric telescoping, irrational rotations, floor sequences supply the essential reduction.

## 2015 AIME II Problem 14: Extract the requested symmetric quantity directly

Real numbers $x,y$ satisfy $x^4y^5+y^4x^5=810$ and $x^3y^6+y^3x^6=945$. Find $2x^3+(xy)^3+2y^3$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Put $s=x+y$ and $t=xy$. The equations become $t^4s=810$ and $t^3(s^3-3ts)=945$. Adding three times the first to the second gives $(st)^3=3375$, hence $st=15$. Therefore $t^3=810/15=54$, and the second original equation gives $x^3+y^3=945/54=35/2$. The requested value is $2(35/2)+54=89$.

**Answer:** 089.

**Methods:** symmetric polynomials, elimination, target-oriented substitution.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All ten alternatives inspected. The shortest methods eliminate to st directly without solving for x and y. Several longer alternatives have copied errors, including 945-810 written 115, a missing cube on xy, and the second right-hand side written 810.

**Archived entries inspected:** 10 of 10. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Extract the requested symmetric quantity directly; symmetric polynomials, elimination, target-oriented substitution supply the essential reduction.

## 2015 AIME II Problem 15: Equal areas cut from two tangent circles

Two externally tangent circles have radii 1 and 4 and meet at $A$. A common external tangent touches them at $B,C$. A line through $A$ meets the circles again at $D,E$, respectively. If $B,C$ lie on the same side of the line and $[DBA]=[ACE]=m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Place the centers at $(-1,0)$ and $(4,0)$, with $A=(0,0)$. A common tangent has contacts $B=(-8/5,-4/5)$ and $C=(8/5,-16/5)$, as follows by using a unit normal with horizontal component $-3/5$. The homothety of ratio $-4$ centered at $A$ gives $AE=4AD$. Thus equal areas require the distance from $B$ to the line to be four times that from $C$. Write its equation $ux+vy=0$. Since $B,C$ are on the same side, their signed values satisfy $uB_x+vB_y=4(uC_x+vC_y)$, giving $-40u+60v=0$. Hence the line is $3x+2y=0$. Its second intersection with $(x+1)^2+y^2=1$ is $D=(-8/13,12/13)$, so $AD=4/\sqrt{13}$. The distance from $B$ to this line is $32/(5\sqrt{13})$. The common area is $\tfrac12(4/\sqrt{13})(32/(5\sqrt{13}))=64/65$, giving 129.

**Answer:** 129.

**Methods:** homothety, signed distances, circle equations.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eleven alternatives inspected. Homothety makes the equal-area condition a linear signed-distance equation. The coordinate and tangent-secant methods are efficient; several longer angle-chasing alternatives contain reversed homothety ratios or mislabeled lengths, so every sign and coordinate is derived explicitly here.

**Archived entries inspected:** 11 of 11. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equal areas cut from two tangent circles; homothety, signed distances, circle equations supply the essential reduction.

## 2016 AIME I Problem 1: Opposite-ratio geometric series

For $|r|<1$, let $S(r)=12+12r+12r^2+\cdots$. If $S(a)S(-a)=2016$, find $S(a)+S(-a)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

Since $S(r)=12/(1-r)$, the product is $144/(1-a^2)$ and the sum is $24/(1-a^2)$. The sum is therefore one sixth of the product, namely 336.

**Answer:** 336.

**Methods:** geometric series, shared denominators.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** The single source uses the same common-denominator relation; solving for a is unnecessary.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Opposite-ratio geometric series; geometric series, shared denominators supply the essential reduction.

## 2016 AIME I Problem 5: Two arithmetic totals share a day count

A reader starts with $n$ pages in $t$ minutes, then increases both quantities by one each day. She reads on at least two days, finishing 374 pages in 319 minutes; $n,t$ are positive integers. Find $n+t$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

If there are $k$ days, the totals give $k(2n+k-1)=748$ and $k(2t+k-1)=638$. Subtraction gives $k(n-t)=55$, so $k$ divides both 55 and $\gcd(748,638)=22$. Hence $k\mid11$; since $k\ge2$, $k=11$. The two equations now give $n=29,t=24$, and $n+t=53$.

**Answer:** 053.

**Methods:** arithmetic sums, divisibility, common factors.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. The fully justified gcd argument also excludes even day counts; several alternatives simply infer eleven days from the common factor without this step.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Two arithmetic totals share a day count; arithmetic sums, divisibility, common factors supply the essential reduction.

## 2016 AIME I Problem 7: Real values of a complex radical expression

Using principal square roots, count ordered integer pairs $(a,b)$ for which $\sqrt{ab+2016}/(ab+100)-i\sqrt{|a+b|}/(ab+100)$ is defined and real.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

If $ab\ge-2016$, the imaginary part vanishes exactly when $b=-a$. Then $|a|\le44$, excluding $a=\pm10$ because the denominator would vanish:87 pairs. If $ab<-2016$, reality means $-ab-2016=|a+b|$. The signs are opposite; first take $a>0,b=-c<0$. For $c>a$, this becomes $(a-1)(c+1)=2015=5\cdot13\cdot31$. The positive factor pairs with the first smaller are $(1,2015),(5,403),(13,155),(31,65)$, giving four solutions; each satisfies $ac>2016$. Interchanging $a,c$ gives four more, and reversing both signs gives eight further pairs. Total: $87+16=103$.

**Answer:** 103.

**Methods:** principal complex square roots, shifted factorization, divisor pairs.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** The sole source correctly separates the real-radical and imaginary-radical cases. Counting only vanishing second radicals would miss sixteen pairs; the denominator exclusions are also essential.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Real values of a complex radical expression; principal complex square roots, shifted factorization, divisor pairs supply the essential reduction.

## 2016 AIME I Problem 9: A rectangle optimization with a segment inconsistency

Triangle $ABC$ has $AB=40$, $AC=31$, and $\sin A=1/5$. It lies in rectangle $AQRS$ with $B$ on segment $QR$ and $C$ on segment $RS$. Determine the maximum rectangle area. The reported contest answer is 744; the segment conditions require the correction below.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Place $A=(0,0)$, $B=40(\cos\theta,\sin\theta)$, and $C=31(\cos(\theta+A),\sin(\theta+A))$, with $Q=(B_x,0)$ and $S=(0,C_y)$. Necessarily $A$ is acute, so $\cos A=2\sqrt6/5$. The area is $620[\sin(2\theta+A)+1/5]$, whose unrestricted maximum 744 occurs at $\theta_*=(\pi/2-A)/2$. But there $B_y\le C_y$ would require $\tan\theta_*\le31/40$, whereas $\tan\theta_*=\sqrt6/3>31/40$. Thus 744 is unattainable for the literal statement. The segment constraint instead gives $\tan\theta\le t=31/(200-62\sqrt6)<\tan\theta_*$. The area increases throughout this allowed interval, so the true maximum occurs at $B=R$, namely $1600t/(1+t^2)=248(1600-496\sqrt6)/(2561-992\sqrt6)$. At this boundary $C_x<B_x$, so the second segment condition holds. The reported answer 744 solves the relaxed problem permitting B on the line containing QR.

**Reported answer:** 744.

**Methods:** trigonometric optimization, feasibility of equality, segment constraints.

**Verification:** The equality configuration fails the explicit segment inequality; the exact boundary maximizer is derived and meets both segment constraints.

**Source comparison:** All five stored alternatives inspected. The final entry explicitly warns that 744 violates the side condition. The licensed LIVE archive independently confirms the same lengths and segment wording, but also incorrectly asserts the equality configuration is allowed.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Source correction:** **Type:** literal_statement_inconsistency **Reported answer:** 744 **Literal maximum:** $\dfrac{248(1600-496\sqrt6)}{2561-992\sqrt6}$ **Verified statement url:** [Verified source](https://live.poshenloh.com/past-contests/aime/2016I) **Note:** The licensed archive retains the segment condition and the reported answer744. The proof distinguishes the literal feasible maximum from the relaxed intended calculation.

**Subject classification:** geometry, algebra. A rectangle optimization with a segment inconsistency; trigonometric optimization, feasibility of equality, segment constraints supply the essential reduction.

## 2016 AIME I Problem 10: Alternating geometric and arithmetic triples

A strictly increasing positive integer sequence has every triple $a_{2k-1},a_{2k},a_{2k+1}$ geometric and every triple $a_{2k},a_{2k+1},a_{2k+2}$ arithmetic. Given $a_{13}=2016$, find $a_1$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

Let $b_k=\sqrt{a_{2k+1}}$ for $k\ge0$. Geometric triples give $a_{2k+2}=b_kb_{k+1}$; the arithmetic condition then gives $b_k+b_{k+2}=2b_{k+1}$. Thus $b_k=x+kd$ with $x,d>0$. For every $k$, $b_kd=a_{2k+2}-a_{2k+1}$ is an integer, so subtracting consecutive such values shows $D=d^2$ is a positive integer. Since $b_6=12\sqrt{14}$, the integer $N=b_6d$ satisfies $N^2=2016D$. Prime factorization forces $168\mid N$, so $d=j\sqrt{14}$ for a positive integer $j$. Now $x=b_6-6d=(12-6j)\sqrt{14}>0$ forces $j=1$. Therefore $a_1=x^2=504$. Conversely $b_k=(6+k)\sqrt{14}$ generates an increasing integer sequence with all required properties.

**Answer:** 504.

**Methods:** square-root linearization, integer differences, square divisibility.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. Their square-pattern observations are useful, but several assume rational factors are integers or guess a smallest step. The integer-difference argument proves the step restriction and uniqueness.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Alternating geometric and arithmetic triples; square-root linearization, integer differences, square divisibility supply the essential reduction.

## 2016 AIME I Problem 11: A polynomial shift equation

A nonzero polynomial satisfies $(x-1)P(x+1)=(x+2)P(x)$ for every real $x$ and $P(2)^2=P(3)$. If $P(7/2)=m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Substituting $x=1,0,-1$ gives zeros at $1,0,-1$. Write $P(x)=x(x-1)(x+1)Q(x)$. The given identity, after polynomial cancellation, becomes $Q(x+1)=Q(x)$. A nonconstant polynomial of degree $d$ would have a nonzero difference of degree $d-1$, so $Q=c$ is constant. Now $(6c)^2=24c$ and $c\ne0$ imply $c=2/3$. Hence $P(7/2)=(2/3)(7/2)(5/2)(9/2)=105/4$, giving 109.

**Answer:** 109.

**Methods:** polynomial functional equations, forced roots, periodic polynomials.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. Factoring the forced roots and proving the quotient constant is rigorous. A few alternatives ignore root multiplicity or infer a global degree from only five sampled values; those shortcuts do not suffice.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A polynomial shift equation; polynomial functional equations, forced roots, periodic polynomials supply the essential reduction.

## 2016 AIME II Problem 1: A geometric allocation becomes arithmetic

Alex, Betty, and Charlie initially have 444 peanuts in a strictly increasing geometric progression. They eat 5,9,25 peanuts respectively, after which their counts, in the same order, form an arithmetic progression. Find Alex’s initial count.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

The remaining total is 405, so the middle arithmetic term is 135. Betty initially had 144. The two other initial counts $a,c$ satisfy $a+c=300$ and $ac=144^2$. Thus they are roots of $u^2-300u+20736=0$, namely 108 and 192. Alex had the smaller count 108; the remaining counts 103,135,167 verify the arithmetic condition.

**Answer:** 108.

**Methods:** arithmetic mean, geometric mean, quadratic roots.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. Recovering the middle term from the remaining total avoids solving simultaneously for a scale and a geometric ratio. The guessing alternative does not establish uniqueness.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A geometric allocation becomes arithmetic; arithmetic mean, geometric mean, quadratic roots supply the essential reduction.

## 2016 AIME II Problem 3: Three logarithms share one product

Real $x,y,z$ satisfy $\log_2(xyz-3+\log_5x)=5$, $\log_3(xyz-3+\log_5y)=4$, and $\log_4(xyz-3+\log_5z)=4$. Find $|\log_5x|+|\log_5y|+|\log_5z|$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

The logarithms require $x,y,z>0$. Set $t=xyz$. Exponentiating and summing gives $3t+\log_5t=32+81+256+9=378$. This function is strictly increasing for $t>0$, and $t=125$ satisfies it, so it is the unique solution. Substituting yields $\log_5x=-90$, $\log_5y=-41$, and $\log_5z=134$. Their absolute values sum to 265.

**Answer:** 265.

**Methods:** logarithm elimination, monotonicity, shared products.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** The sole source finds the same product but incorrectly says it must be a power of 5. Strict monotonicity proves that the verified value 125 is unique without that assumption.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Three logarithms share one product; logarithm elimination, monotonicity, shared products supply the essential reduction.

## 2016 AIME II Problem 5: An infinite chain of right-triangle altitudes

Right triangle $ABC_0$ has pairwise coprime positive integer sides and perimeter $p$. Let $C_1$ be the foot from $C_0$ to $AB$; for $n\ge2$, let $C_n$ be the foot from $C_{n-1}$ to $C_{n-2}B$. If $C_0C_1+C_1C_2+\cdots=6p$, find $p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Put $a=BC_0$, $b=AC_0$, $c=AB$. The first altitude is $ab/c$, and successive similar right triangles multiply it by $a/c$. Thus the total is $ab/(c-a)=6(a+b+c)$. Using $c^2=a^2+b^2$ to simplify gives $7a=6(b+c)$. Hence $6b=7a-6c$; squaring and substituting for $b^2$ yields $85a^2=84ac$, so $a/c=84/85$. Coprimality forces $a=84,c=85$, and then $b=13$. Therefore $p=182$.

**Answer:** 182.

**Methods:** similarity chains, geometric series, primitive Pythagorean triples.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. The geometric-series derivation is reliable; several finish by guessing a triple or choose the wrong parity orientation in Euclid’s parametrization. Eliminating with the Pythagorean identity proves the unique primitive ratio.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra, number_theory. An infinite chain of right-triangle altitudes; similarity chains, geometric series, primitive Pythagorean triples supply the essential reduction.

## 2016 AIME II Problem 6: Absolute coefficient sum by parity

For $P(x)=1-x/3+x^2/6$ and $Q(x)=P(x)P(x^3)P(x^5)P(x^7)P(x^9)$, find numerator plus denominator of the sum of absolute coefficients of $Q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Every chosen negative term has odd degree, and every positive term even degree. All contributions to a degree $j$ coefficient therefore have sign $(-1)^j$, with no cancellation. The absolute coefficient sum is $Q(-1)=P(-1)^5=(3/2)^5=243/32$, giving $275$.

**Answer:** 275.

**Methods:** generating functions, parity.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Absolute coefficient sum by parity; the proof uses generating functions, parity.

## 2016 AIME II Problem 9: An arithmetic sequence plus a geometric sequence

Increasing positive integer sequences satisfy $a_1=b_1=1$, with $a_n$ arithmetic and $b_n$ geometric. Put $c_n=a_n+b_n$. If $c_{k-1}=100$ and $c_{k+1}=1000$, find $c_k$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Write $a_n=1+(n-1)d$ and $b_n=r^{n-1}$, where $d\ge1,r\ge2$ are integers. Since $c_1=2$, $k\ge3$. The arithmetic contribution at $k+1$ is less than three times that at $k-1$, hence less than 300. Therefore $700<r^k<1000$. Also $r^3<1000$, so $2\le r\le9$. Checking these eight bases, the only powers in that interval with exponent at least 3 are $3^6=729$ and $9^3=729$. In the first case $k=6$ and $d=(99-3^4)/4=9/2$, impossible. In the second $k=3,r=9,d=90$. Thus $c_k=1+2(90)+9^2=262$, and the given neighboring values are verified.

**Answer:** 262.

**Methods:** mixed sequences, exponential bounds, divisibility.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. One gives a valid power-interval search, while several merely guess k=3 or dismiss larger cases without details. The bounded power list proves uniqueness.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. An arithmetic sequence plus a geometric sequence; mixed sequences, exponential bounds, divisibility supply the essential reduction.

## 2016 AIME II Problem 15: An apparent maximum forced by Cauchy equality

Set $a_i=2^{-i}$ for $1\le i\le215$ and $a_{216}=2^{-215}$. Positive numbers $x_i$ satisfy $\sum x_i=1$ and $\sum_{i<j}x_ix_j=107/215+\sum_i a_ix_i^2/[2(1-a_i)]$. If the greatest possible $x_2=m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Using $2\sum_{i<j}x_ix_j=1-\sum x_i^2$, rearrange the second condition to $\sum_i x_i^2/(1-a_i)=1/215$. Also $\sum a_i=1$, so $\sum(1-a_i)=215$. Cauchy–Schwarz gives $\bigl(\sum x_i\bigr)^2\le\bigl(\sum x_i^2/(1-a_i)\bigr)\bigl(\sum(1-a_i)\bigr)=1$. Equality holds, forcing $x_i=c(1-a_i)$ for every i. Normalization gives $c=1/215$, so the only possible $x_2$ is $(3/4)/215=3/860$. All these values are positive and satisfy the equations. Thus the maximum is this forced value, and the answer is 863.

**Answer:** 863.

**Methods:** Cauchy-Schwarz equality, quadratic constraints, normalization.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** The single source correctly recognizes an equality case of weighted Cauchy–Schwarz. The positivity and normalization also verify existence rather than merely a necessary bound.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. An apparent maximum forced by Cauchy equality; Cauchy-Schwarz equality, quadratic constraints, normalization supply the essential reduction.

## 2017 AIME I Problem 10: A real cross ratio traces a circle

Let $z_1=18+83i$, $z_2=18+39i$, and $z_3=78+99i$. Among complex $z\ne z_3$ making $\frac{z_3-z_1}{z_2-z_1}\frac{z-z_2}{z-z_3}$ real, take the one with greatest imaginary part. Find its real part.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

A real cross ratio means the directed angles subtending the fixed endpoints $z_2,z_3$ agree modulo $\pi$; thus the locus is their circle through $z_1$, with $z_3$ removed. Its center lies on the perpendicular bisector $y=61$ of $z_1z_2$ and on the perpendicular bisector $y=-x+117$ of $z_2z_3$. Therefore the center is $(56,61)$. The topmost point has real part 56 and is not the excluded point $z_3$, so the answer is 56.

**Answer:** 056.

**Methods:** real cross ratios, cyclic loci, perpendicular bisectors.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight stored entries inspected; the first four are connected pieces of one geometric discussion. Some assert angle equality without its moduloπ qualification, and one informally includes the undefined point z 3. The circle-locus formulation handles both issues.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. A real cross ratio traces a circle; real cross ratios, cyclic loci, perpendicular bisectors supply the essential reduction.

## 2017 AIME I Problem 14: Nested logarithms become a monotone power equation

For $a>1,x>1$, suppose $\log_a(\log_a(\log_a2)+\log_a24-128)=128$ and $\log_a(\log_ax)=256$. Find $x$ modulo 1000.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Put $b=a^{a^{128}}>1$. Exponentiating the first equation gives $24\log_a2=a^{128}b$. Multiplying by $\log a$ yields $24\log2=b\log b$, so $b^b=2^{24}=8^8$. The function $u\log u$ is strictly increasing for $u>1$, hence $b=8$. Now put $t=a^{128}$; raising $b=a^t$ to 128 gives $t^t=8^{128}=64^{64}$, so $t=64$ and $a=2^{3/64}$. The second condition gives $x=a^{a^{256}}=a^{4096}=2^{192}$. Repeated squaring modulo 1000 gives the successive residues for exponents $3,6,12,24,48,96,192$ as $8,64,96,216,656,336,896$. The answer is 896.

**Answer:** 896.

**Methods:** nested logarithms, monotonic power functions, repeated squaring.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. The first has the useful power-tower substitution but does not state its uniqueness justification; the second guesses a parameter from its apparent factorization. Monotonicity makes both substitutions rigorous.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Nested logarithms become a monotone power equation; nested logarithms, monotonic power functions, repeated squaring supply the essential reduction.

## 2017 AIME I Problem 15: The smallest equilateral triangle between three sides

A right triangle has legs 5 and $2\sqrt3$. An equilateral triangle has one vertex on each side. Its least possible area is $m\sqrt p/n$, where $m/n$ is reduced and $p$ squarefree. Find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Place the outer vertices at $(0,0),(5,0),(0,2\sqrt3)$. Let two inner vertices be $(a,0),(0,b)$. The third, inside the first quadrant, is $((a+\sqrt3b)/2,(\sqrt3a+b)/2)$. Requiring it on the hypotenuse gives $7\sqrt3a+11b=20\sqrt3$. By Cauchy–Schwarz, $1200\le(147+121)(a^2+b^2)$, so the squared inner side is at least $300/67$. Equality holds at $a=105/67$, $b=55\sqrt3/67$; both lie on the required legs, and the third vertex $(135/67,80\sqrt3/67)$ lies on the hypotenuse. Thus the minimum area is $75\sqrt3/67$, giving 145.

**Answer:** 145.

**Methods:** rotation coordinates, linear constraints, Cauchy-Schwarz equality.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All thirteen alternatives inspected. Coordinate rotation and a point-to-line distance give the shortest proof. Many sources omit the equality placement or mislabel side length versus its square; the explicit feasible coordinates establish attainment.

**Archived entries inspected:** 13 of 13. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The smallest equilateral triangle between three sides; rotation coordinates, linear constraints, Cauchy-Schwarz equality supply the essential reduction.

## 2017 AIME II Problem 5: Four pair sums force a complementary pair

Four distinct real numbers have six pairwise sums. Four of these are 189,320,287,234; the remaining two are $x,y$. Find the greatest possible $x+y$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Let the four numbers sum to $T$. Their six pair sums split into three complementary pairs, each totaling $T$: $(a+b,c+d)$, $(a+c,b+d)$, $(a+d,b+c)$. Among the four known sums, two must belong to one complementary pair by pigeonhole. Hence $T$ is at most the sum of the two largest known values, $320+287=607$. All six sums total $3T$, so $x+y=3T-(189+320+287+234)\le791$. Equality is attained by the distinct numbers $103/2,275/2,365/2,471/2$: their four specified sums are 189,234,287,320 and the remaining sums are 373,418. Therefore the maximum is 791.

**Answer:** 791.

**Methods:** complementary edge matchings, pigeonhole principle, equality construction.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. The complementary-pair argument proves the upper bound; several sources assume the unknown sums are the two largest without establishing it. An explicit four-number witness proves that the upper bound is attainable.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, combinatorics. The six edges of K4 split into three complementary matchings. Pigeonhole among four known edge sums bounds the vertex sum; an explicit realization proves equality.

## 2017 AIME II Problem 7: Count parameters after enforcing the logarithm domain

Count integers $k\in[-500,500]$ for which $\log(kx)=2\log(x+2)$ has exactly one real solution.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

The domain is $x>-2$ and $kx>0$. Exponentiation gives $f(x)=x^2+(4-k)x+4=0$. For $k<0$, $f(-2)=2k<0$ and $f(0)=4>0$, so one root lies in $(-2,0)$; the other lies below $-2$, since the monic quadratic is positive at negative infinity. Exactly one root is admissible. For $k>0$, the discriminant is $k(k-8)$: there are no roots for $0<k<8$, one positive double root at $k=8$, and two positive roots for $k>8$. The case $k=0$ is outside the logarithm domain. Thus the 500 negative integers and 8 give 501 choices.

**Answer:** 501.

**Methods:** logarithm domains, parameter quadratics, root location.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. The domain removes one negative quadratic root for every negative k. Evaluating the polynomial at−2 and 0 proves the root locations without lengthy radical inequalities.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Count parameters after enforcing the logarithm domain; logarithm domains, parameter quadratics, root location supply the essential reduction.

## 2017 AIME II Problem 12: The limit point of rotating nested circles

Starting with a unit circle centered at $O$, choose $A_0$ on it. For $n\ge1$, a circle of radius $r^n$ is internally tangent to the preceding circle at $A_{n-1}$, and $A_n$ is 90 degrees counterclockwise from that tangency point on the new circle. For $r=11/60$, write the distance from $O$ to the common limit point as $m/n$ and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Use complex coordinates with $O=0,A_0=1$. The successive center displacements are $(1-r),(1-r)ri,(1-r)(ri)^2,\ldots$, because each construction rotates the contact radius 90 degrees and scales it by r. Their sum is $B=(1-r)/(1-ri)$. The nested radii tend to zero, so this is their unique common point; indeed its distance from the nth center is $r^n|B|<r^n$. Hence $OB=(1-r)/\sqrt{1+r^2}=(49/60)/(61/60)=49/61$. The answer is 110.

**Answer:** 110.

**Methods:** complex geometric series, nested circles, contraction limits.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. Center displacements give the complex series directly and prove uniqueness of the common point. One invariant-based alternative has an inverted squared-distance formula; the last coordinate alternative prints 538 where the imaginary numerator should be 539.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The limit point of rotating nested circles; complex geometric series, nested circles, contraction limits supply the essential reduction.

## 2017 AIME II Problem 15: The geometric median of a disphenoid

A tetrahedron has opposite edge pairs $AD=BC=28$, $AC=BD=44$, and $AB=CD=52$. If the least possible value of $AX+BX+CX+DX$ over points $X$ in space is $m\sqrt n$ with squarefree $n$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Realize the vertices as $A=(u,v,w)$, $B=(u,-v,-w)$, $C=(-u,v,-w)$, $D=(-u,-v,w)$. The edge equations give $u^2+v^2=196$, $u^2+w^2=484$, $v^2+w^2=676$, so $(u^2,v^2,w^2)=(2,194,482)$. This realizes the given tetrahedron and places all vertices at distance $R=\sqrt{678}$ from the origin, with vector sum zero. For any $X$ and vertex $V$, Cauchy–Schwarz gives $|X-V|\ge(V-X)\cdot V/R=R-X\cdot V/R$. Summing cancels the dot products, giving total distance at least $4R$, with equality at $X=0$. Thus the minimum is $4\sqrt{678}$; since $678=2\cdot3\cdot113$ is squarefree, the answer is 682.

**Answer:** 682.

**Methods:** disphenoid coordinates, supporting-plane inequality, geometric median.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Symmetrization also proves the centroid minimizes the sum, but one source invokes central symmetry incorrectly: a tetrahedron is not centrally symmetric. The equal-radius and zero-vector-sum inequality proves the minimum globally.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The geometric median of a disphenoid; disphenoid coordinates, supporting-plane inequality, geometric median supply the essential reduction.

## 2018 AIME I Problem 1: Integer-root quadratics counted by a sum

Count modulo $1000$ pairs $(a, b)$ with $1\le a\le 100, b\ge 0$ for which $x^2+ax+b$ splits over the integers.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

Write $(x+u)(x+v)$, where $0\le u\le v$ and $u+v=a$. These unordered roots uniquely determine $(a, b)$. For fixed $a$ there are $\lfloor a/2\rfloor+1$ choices. Hence the count is $\sum_{a=1}^{100}(\lfloor a/2\rfloor+1)=2500+100=2600$; remainder $600$.

**Answer:** 600.

**Methods:** lattice point counting, algebra hybrid.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All nine source solutions inspected. Root-pair counting, triangular lattice points, stars and bars with diagonal correction, and discriminant parity agree on 2600. Several alternatives have harmless endpoint/notational slips: the discriminant version excludes c=0 in words while its formula includes it; one stars-and-bars version writes modulo 100 instead of 1000. The independent proof counts equal roots and zero roots correctly.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Integer-root quadratics counted by a sum; the proof uses lattice point counting, algebra hybrid.

## 2018 AIME I Problem 5: Two logarithmic equations restrict a homogeneous ratio

For real $(x,y)$ satisfying $\log_2(2x+y)=\log_4(x^2+xy+7y^2)$, choose $K$ so that $\log_3(3x+y)=\log_9(3x^2+4xy+Ky^2)$. Find the product of all possible K.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

The first equation, with $2x+y>0$, is equivalent to $(2x+y)^2=x^2+xy+7y^2$, or $(x-y)(x+2y)=0$. The zero pair is excluded, so either $x=y>0$ or $x=-2y$ with $y<0$. Both cases have $3x+y>0$. Squaring the positive argument in the second equation gives $6x^2+2xy+(1-K)y^2=0$. Substituting the two ratios yields respectively $K=9$ and 21. Both are realized by admissible pairs, and their product is 189.

**Answer:** 189.

**Methods:** change of logarithm base, homogeneous factorization, domain checks.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. The domain-aware source confirms both ratios are admissible; the first two suppress these checks. The zero case must be excluded before division by y.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Two logarithmic equations restrict a homogeneous ratio; change of logarithm base, homogeneous factorization, domain checks supply the essential reduction.

## 2018 AIME I Problem 6: Two disjoint root-of-unity families

Count complex numbers $z$ satisfying $|z|=1$ and $z^{720}-z^{120}\in\mathbb R$. Find the count modulo 1000.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

For $|z|=1$, $\overline z=1/z$. Equating the expression to its conjugate and multiplying by $z^{720}$ gives $(z^{840}+1)(z^{600}-1)=0$. These factors have 840 and 600 distinct roots respectively, all on the unit circle. They share none: a common root would give $z^{4200}=(-1)^5=-1$ from the first equation and $z^{4200}=1^7=1$ from the second. Thus the count is 1440 and the remainder 440.

**Answer:** 440.

**Methods:** conjugation on the unit circle, roots of unity, disjoint root families.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All seven alternatives inspected. Trigonometric families give the same count, but several omit checking overlap. The polynomial degree alone is insufficient; the explicit factorization and incompatible powers prove distinctness.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Two disjoint root-of-unity families; conjugation on the unit circle, roots of unity, disjoint root families supply the essential reduction.

## 2018 AIME II Problem 1: A return trip has twice the meeting time

Points $A,B,C$ occur in order on a path, with $AC=1800$ meters. Eve runs at speed $v$, Ina at $2v$, Paul at $4v$. Ina starts at A toward C, Paul at B toward C, and Eve at C toward A. Paul turns upon meeting Eve; Paul and Ina reach B together. Find AB.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

Let $AB=x$. Paul and Eve meet after $(1800-x)/(5v)$; Paul’s return to B takes the same time. Ina takes $x/(2v)$ to reach B. Thus $x/(2v)=2(1800-x)/(5v)$, giving $5x=7200-4x$ and $x=800$.

**Answer:** 800.

**Methods:** relative speed, equal-time equations.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. The outward and return legs have equal lengths and speed, so doubling the first meeting time directly gives the needed equation.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A return trip has twice the meeting time; relative speed, equal-time equations supply the essential reduction.

## 2018 AIME II Problem 5: Recover a norm without choosing square-root branches

Complex numbers satisfy $xy=-80-320i$, $yz=60$, and $zx=-96+24i$. If $x+y+z=a+bi$ with real a,b, find $a^2+b^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

All variables are nonzero, so division of the given products yields $x^2=(xy)(xz)/(yz)=256+480i$, $y^2=(xy)(yz)/(xz)=200i$, and $z^2=(xz)(yz)/(xy)=-18i$. Consequently $(x+y+z)^2=x^2+y^2+z^2+2(xy+yz+zx)=24+70i$. Taking absolute values gives $a^2+b^2=|x+y+z|^2=|24+70i|=\sqrt{24^2+70^2}=74$.

**Answer:** 074.

**Methods:** symmetric complex expressions, modulus of a square, branch avoidance.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All nine alternatives inspected. Several explicit-root computations mix the signs or interchange y and z; the squared-sum norm calculation avoids every square-root choice and uses only the given products.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Recover a norm without choosing square-root branches; symmetric complex expressions, modulus of a square, branch avoidance supply the essential reduction.

## 2018 AIME II Problem 6: Random parameter with four real roots

For $a$ chosen uniformly in $[-20,18]$, find numerator plus denominator of the probability that $x^4+2ax^3+(2a-2)x^2+(-4a+3)x-2$ has only real roots.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

The polynomial factors as $(x-1)(x+2)(x^2+(2a-1)x+1)$. The last factor has real roots iff $(2a-1)^2\ge 4$, equivalent to $a\le -1/2$ or $a\ge 3/2$. Only an interval of length $2$ within the length $38$ sample space fails. Probability $18/19$; answer $37$.

**Answer:** 037.

**Methods:** continuous probability, algebra hybrid.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The sole source determines parameter intervals by the two quadratic branches of the absolute value. The original solution uses the same root-counting condition.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Random parameter with four real roots; the proof uses continuous probability, algebra hybrid.

## 2018 AIME II Problem 12: An area balance bisects one diagonal

A convex quadrilateral has $AB=CD=10$, $BC=14$, $AD=2\sqrt{65}$. Its diagonals meet at P, with $[APB]+[CPD]=[BPC]+[APD]$. Find its area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Using the common sine of the diagonal angles, the area condition factors as $(AP-CP)(BP-DP)=0$. We may assume $AP=CP=u$: if instead BD is bisected, relabel $(A,B,C,D)$ as $(D,C,B,A)$, which preserves every stated side length and exchanges the diagonals. Set $BP=v,DP=w$, and $c=\cos\angle APB$. The cosine law gives $u^2+v^2=148$, $uvc=24$, $u^2+w^2=180$, and $uwc=40$. Hence $w/v=5/3$ and $w^2-v^2=32$, giving $v=3\sqrt2,w=5\sqrt2,u=\sqrt{130}$. Thus $c=4/\sqrt{65}$ and the diagonal-angle sine is $7/\sqrt{65}$. The area is $u(v+w)\sin\angle APB=\sqrt{130}(8\sqrt2)(7/\sqrt{65})=112$.

**Answer:** 112.

**Methods:** opposite area balance, diagonal bisection, cosine-law systems.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eleven alternatives inspected. Several discard one of the two possible bisected diagonals without proof or incorrectly claim one case makes a parallelogram. The explicit label symmetry preserves all side data, so it rigorously handles both cases.

**Archived entries inspected:** 11 of 11. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. An area balance bisects one diagonal; opposite area balance, diagonal bisection, cosine-law systems supply the essential reduction.

## 2019 AIME I Problem 4: Ordered substitutions

A team has $11$ active players and $11$ unused substitutes. Count modulo $1000$ histories with at most $3$ successive substitutions, with removed players unable to return.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

At substitution $j$ there are $11$ choices of departing active player and $12-j$ unused entrants, irrespective of previous choices. Thus the count is $\sum_{k=0}^3 11^k(11)_k=1+121+13310+1317690$. The last two terms sum to a multiple of $1000$, leaving $122$.

**Answer:** 122.

**Methods:** sequential counting, falling factorials.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All three source counts track histories of substitutions; the choices of departed players and unused replacements are distinguished.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Ordered substitutions; the proof uses sequential counting, falling factorials.

## 2019 AIME I Problem 7: Prime exponents hidden in gcd and lcm logarithms

Positive integers x,y satisfy $\log_{10}x+2\log_{10}\gcd(x,y)=60$ and $\log_{10}y+2\log_{10}\operatorname{lcm}(x,y)=570$. If m,n count the prime factors of x,y with multiplicity, find $3m+2n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Adding and using $\gcd(x,y)\operatorname{lcm}(x,y)=xy$ gives $xy=10^{210}$. Thus only 2 and 5 divide either number. From $x\gcd(x,y)^2=10^{60}$, each prime exponent in x is at most 60; the corresponding exponent in y is at least 150. Hence $x\mid y$ and $\gcd(x,y)=x$. Therefore $x^3=10^{60}$, giving $x=10^{20}$ and $y=10^{190}$. Thus $m=40,n=380$ and $3m+2n=880$.

**Answer:** 880.

**Methods:** gcd-lcm product, prime valuations, logarithms.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All seven alternatives inspected. Valuations rigorously establish x divides y. Several alternatives assume both numbers are powers of 10, or infer coordinatewise exponent inequalities merely from x<y; neither shortcut alone is justified.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Prime exponents hidden in gcd and lcm logarithms; gcd-lcm product, prime valuations, logarithms supply the essential reduction.

## 2019 AIME I Problem 8: Two-variable power sums from one product

For real x, $\sin^{10}x+\cos^{10}x=11/36$. If $\sin^{12}x+\cos^{12}x=m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

Put $u=\sin^2x,v=\cos^2x$, so $u+v=1$ and $p=uv\le1/4$. The sums $S_k=u^k+v^k$ satisfy $S_k=S_{k-1}-pS_{k-2}$. In particular $S_5=1-5p+5p^2=11/36$, giving $p=1/6$ or 5/6; the bound excludes 5/6. Then $S_4=1-4p+2p^2=7/18$ and $S_6=S_5-pS_4=13/54$. The answer is 67.

**Answer:** 067.

**Methods:** symmetric power sums, recurrence, trigonometric normalization.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight alternatives inspected. The power-sum recurrence keeps the degrees low. Any algebraic root for the product must be checked against its range 0≤p≤1/4.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Two-variable power sums from one product; symmetric power sums, recurrence, trigonometric normalization supply the essential reduction.

## 2019 AIME I Problem 10: Read coefficients before expanding a large cube

Distinct complex numbers $z_1,\ldots,z_{673}$ satisfy $\prod_j(x-z_j)^3=x^{2019}+20x^{2018}+19x^{2017}+g(x)$, where $\deg g\le2016$. Write $|\sum_{j<k}z_jz_k|=m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

Write $\prod_j(x-z_j)=x^{673}+ax^{672}+bx^{671}+\cdots$. In its cube, the next two coefficients are $3a$ and $3b+3a^2$. Hence $a=20/3$ and $b=(19-400/3)/3=-343/9$. Vieta identifies b as the requested pairwise sum before absolute value. Thus the answer is $343+9=352$.

**Answer:** 352.

**Methods:** Vieta formulas, low-degree coefficient extraction, repeated roots.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight alternatives inspected. Treating the polynomial as a cube avoids accounting individually for 2019 repeated roots. The expanded-root alternatives agree after multiplicities are handled correctly.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Read coefficients before expanding a large cube; Vieta formulas, low-degree coefficient extraction, repeated roots supply the essential reduction.

## 2019 AIME I Problem 12: A right angle becomes a purely imaginary quotient

Let $f(z)=z^2-19z$. Complex numbers z,f(z),f(f(z)) form a nondegenerate right triangle, with right angle at f(z). One admissible z is $m+\sqrt n+11i$ for positive integers m,n, with n squarefree. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

The quotient of the two directed successive sides is $\frac{f(f(z))-f(z)}{f(z)-z}=(z-19)(z+1)=(z-9)^2-100$, provided $z\ne0,20$. A right angle makes this quotient purely imaginary. Writing $z=u+11i$, its real part is $(u-9)^2-221$, so $u=9\pm\sqrt{221}$. The stated positive form selects $u=9+\sqrt{221}$; since $221=13\cdot17$, it is squarefree. The quotient has nonzero imaginary part $22\sqrt{221}$, verifying nondegeneracy. Thus the answer is 230.

**Answer:** 230.

**Methods:** complex angle quotient, polynomial cancellation, nondegeneracy.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. Factoring the differences first reduces the fourth-degree iterate to a quadratic expression. The nonzero-side and nonzero-quotient checks ensure the formal right-angle condition really gives a triangle.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. A right angle becomes a purely imaginary quotient; complex angle quotient, polynomial cancellation, nondegeneracy supply the essential reduction.

## 2019 AIME II Problem 3: Overlapping products of seven integers

Count positive integer tuples $(a, b, c, d, e, f, g)$ satisfying $abc=70, cde=71, efg=72$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

Since $71$ is prime and divides neither $70$ nor $72$, necessarily $c=e=1,d=71$. The independent choices are $ab=70$ and $fg=72$, giving $\tau(70)\tau(72)=8\cdot12=96$.

**Answer:** 096.

**Methods:** product rule, divisor distributions.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both factorizations reduce to the same finite exponent count.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Overlapping products of seven integers; the proof uses product rule, divisor distributions.

## 2019 AIME II Problem 6: A nested logarithm is a second linear variable

All unmarked logarithms have an unknown base $b\ge2$. For $x>1$, $3\log_b(\sqrt x\log_bx)=56$ and $\log_{\log_bx}x=54$. Find b.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Put $u=\log_bx$ and $v=\log_bu$. Expanding the first equation and changing base in the second gives $3u/2+3v=56$ and $u=54v$. Thus $u=36,v=2/3$. Consequently $\log_b36=2/3$, so $b=36^{3/2}=216$. Taking $x=216^{36}$ verifies both original equations and their logarithm domains.

**Answer:** 216.

**Methods:** nested-log substitution, change of base, linear systems.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight alternatives inspected. Treating the logarithm and its iterate as two variables avoids repeated exponentiation and makes the domain check straightforward.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A nested logarithm is a second linear variable; nested-log substitution, change of base, linear systems supply the essential reduction.

## 2019 AIME II Problem 8: A coefficient bound attained at a sixth root of unity

Real numbers $a,b,c\le2019$ define $f(z)=az^{2018}+bz^{2017}+cz^{2016}$. If $f((1+\sqrt3i)/2)=2015+2019\sqrt3i$, find the remainder of $f(1)$ upon division by 1000.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Let $\omega=(1+\sqrt3i)/2$, so $\omega^6=1$ and $f(\omega)=a\omega^2+b\omega+c$. Comparing imaginary parts gives $a+b=4038$. Since each is at most 2019, both must equal 2019. The real-part equation $-a/2+b/2+c=2015$ then gives $c=2015$. Thus $f(1)=6053$, whose remainder is 53.

**Answer:** 053.

**Methods:** roots of unity, real-imaginary comparison, equality in an upper bound.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. The coefficient upper bounds, rather than integrality or positivity, force equality and remove the apparent free parameter.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A coefficient bound attained at a sixth root of unity; roots of unity, real-imaginary comparison, equality in an upper bound supply the essential reduction.

## 2019 AIME II Problem 10: A tangent sign itinerary fixes every binary digit

An angle $0<\theta<90^\circ$ has $\tan(2^n\theta)>0$ precisely when $3\mid n$, and negative otherwise, for every integer $n\ge0$. Write $\theta=p/q$ degrees in lowest terms and find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Put $t=\theta/180\in(0,1/2)$. The sign of $\tan(180\cdot2^nt)$ is positive when the fractional part of $2^nt$ lies below 1/2, and negative when it lies above 1/2. In a binary expansion, this reads the next digit:0 for positive,1 for negative. No dyadic endpoint is allowed, because tangent there is zero or undefined. Thus the unique expansion is $t=0.\overline{011}_2=3/(2^3-1)=3/7$. Hence $\theta=540/7$ degrees and the answer is 547.

**Answer:** 547.

**Methods:** binary expansion, doubling dynamics, trigonometric signs.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. The binary-digit argument proves uniqueness. Several sources infer periodic angles directly from periodic signs without proof; that implication requires the complete itinerary, supplied here.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory, combinatorics. An infinite tangent-sign itinerary is encoded by the binary digits of a doubling orbit, and the periodic word determines the permitted angle.

## 2019 AIME II Problem 15: Two chord powers recover both sides of a triangle

In acute triangle ABC, P is the perpendicular foot from C to AB and Q the foot from B to AC. Line PQ meets the circumcircle at X,Y in the order X,P,Q,Y, with $XP=10$, $PQ=25$, $QY=15$. If $AB\cdot AC=m\sqrt n$ with n squarefree, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Write $AP=p$, $PB=q$, $AQ=r$, $QC=s$. Chord power gives $pq=10\cdot40=400$ and $rs=15\cdot35=525$. Since B,C,P,Q lie on the circle with diameter BC, power at A gives $p(p+q)=r(r+s)$, hence $p^2-r^2=125$. Also $\cos A=r/(p+q)$. The cosine law in APQ yields $625=p^2+r^2-2pr^2/(p+q)$. Substituting $p^2=r^2+125$ and $p(p+q)=r^2+525$ reduces this to $500=800r^2/(r^2+525)$, so $r^2=875$. Therefore $p=10\sqrt{10}$, $q=4\sqrt{10}$, $r=5\sqrt{35}$, $s=3\sqrt{35}$. Their side product is $(p+q)(r+s)=560\sqrt{14}$, giving 574.

**Answer:** 574.

**Methods:** power of a point, diameter circle, linearized cosine law.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five stored entries inspected, including an author-only entry. The two circle powers reduce the system to one variable. The orthic-triangle alternative is valid but introduces extra half-angle calculations.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Two chord powers recover both sides of a triangle; power of a point, diameter circle, linearized cosine law supply the essential reduction.

## 2020 AIME I Problem 2: A geometric progression with negative logarithm terms

The numbers $\log_8(2x)$, $\log_4x$, $\log_2x$ form a geometric progression with positive ratio. For the unique positive x, write $x=m/n$ reduced and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

Let $u=\log_2x$. The terms are $(u+1)/3,u/2,u$. If u=0 the first term is 1/3 and the next is 0, incompatible with a positive ratio. Otherwise the last two terms force ratio 2, so $u/2=2(u+1)/3$. Hence $u=-4$ and $x=1/16$. The actual terms are−1,−2,−4, verifying ratio 2. The answer is 17.

**Answer:** 017.

**Methods:** change of logarithm base, geometric progression, zero-case exclusion.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight alternatives inspected. One incorrectly takes the middle term to be the positive square root of the endpoint product, even though all valid terms are negative. The signed ratio calculation avoids that issue.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A geometric progression with negative logarithm terms; change of logarithm base, geometric progression, zero-case exclusion supply the essential reduction.

## 2020 AIME I Problem 6: Equal spheres resting in unequal circular holes

Two circular holes of radii 1 and 2 have centers 7 units apart in a horizontal board. Two equal spheres rest in the holes, with their centers above the board, and touch each other. If their common radius squared is $m/n$ reduced, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

Put $u=r^2$. The center heights are $\sqrt{u-1}$ and $\sqrt{u-4}$, while the horizontal separation is 7 and the center distance is 2 r. Thus $49+(\sqrt{u-1}-\sqrt{u-4})^2=4u$, giving $22-u=\sqrt{(u-1)(u-4)}$. Squaring and canceling $u^2$ yields $39u=480$, so $u=160/13$. This has u≥4 and 22−u>0, and substitution verifies the unsquared equation. The answer is 173.

**Answer:** 173.

**Methods:** sphere cross-sections, center distances, radical equations.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. The vertical-plane cross-section gives one equation and a required sign check. The radical-axis approach is valid but substantially longer.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equal spheres resting in unequal circular holes; sphere cross-sections, center distances, radical equations supply the essential reduction.

## 2020 AIME I Problem 8: A shrinking spiral is a complex geometric series

A bug starts at O and walks 5 units east. Before each later walk it turns 60 degrees counterclockwise and halves its walking distance. Its positions converge to P. If $OP^2=m/n$ reduced, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

In complex coordinates, consecutive displacement vectors have ratio $q=(1+i\sqrt3)/4$, of modulus 1/2. Their absolutely convergent sum is $P=5/(1-q)$. Therefore $OP^2=25/|1-q|^2=25/((3/4)^2+(\sqrt3/4)^2)=100/3$. The answer is 103.

**Answer:** 103.

**Methods:** complex geometric series, rotation and scaling, modulus.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All seven alternatives inspected. Complex summation and coordinate sums agree. The final source incorrectly replaces the square of a sum by the sum of squares; it happens to reach the same number, but its omitted cross terms require justification and the argument is not used.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. A shrinking spiral is a complex geometric series; complex geometric series, rotation and scaling, modulus supply the essential reduction.

## 2020 AIME I Problem 11: Counting coefficients through common images

For integer $a, b, c$ in $[-10,10]$, set $f(x)=x^2+ax+b$ and $g(x)=x^2+cx+d$. Count triples for which an integer $d$ makes $g(f(2))=g(f(4))=0$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

If $a=-6$, the two images coincide and every $b, c$ admits the integer choice $d=-f(2)^2-cf(2)$, giving $441$. Otherwise the two images are the roots of $g$, so $c=-20-6a-2b$; the constraint is $-15\le3a+b\le-5$. The exact sum $\sum_{a=-10,a\ne-6}^{10}\max(0,\min(10,-5-3a)-\max(-10,-15-3a)+1)=69$. Hence $441+69=510$.

**Answer:** 510.

**Methods:** bounded lattice counting, algebra hybrid.

**Verification:** The displayed interval sum was evaluated exactly and gives 69.

**Source comparison:** All three entries separate the coincident-image case correctly; the third includes an explicit 69-term-case subtotal table.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Counting coefficients through common images; the proof uses bounded lattice counting, algebra hybrid.

## 2020 AIME I Problem 14: Two fibers of a monic quadratic

A monic quadratic P with complex coefficients has four distinct solutions 3,4,a,b to $P(P(x))=0$. Find the sum of all possible values of $(a+b)^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

If $P(3)=P(4)$, the coefficient of x in P is−7, so the other fiber has roots a,b with a+b=7. This case exists: $P(x)=x^2-7x+15+i\sqrt3$ gives two distinct roots in each fiber, with the fibers disjoint. Otherwise put $u=P(3),v=P(4)$, the two distinct roots of P. Then $P(x)=(x-u)(x-v)$, and evaluating at 3,4 gives $u=(3-u)(3-v)$ and $v=(4-u)(4-v)$. Subtracting yields v=7/2; substitution gives u=−3. Both fibers have root sum u+v=1/2, so the remaining roots are−5/2,−7/2, with sum−6. These are distinct from 3,4. Thus the possible squares are 49 and 36, whose sum is 85.

**Answer:** 085.

**Methods:** polynomial composition, quadratic fibers, Vieta formulas, existence checks.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. Splitting by whether 3 and 4 share a fiber is exhaustive. The explicit complex polynomial verifies existence of the first case, which most alternatives leave implicit; the final radical proof incorrectly orders complex quantities.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Two fibers of a monic quadratic; polynomial composition, quadratic fibers, Vieta formulas, existence checks supply the essential reduction.

## 2020 AIME I Problem 15: An orthocenter tangent determines a chord and an altitude

An acute triangle ABC has orthocenter H and circumcircle omega. The tangent at H to the circumcircle of HBC meets omega at X,Y. Given $HA=3$, $HX=2$, $HY=6$, write $[ABC]=m\sqrt n$ with n squarefree and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Let D be the foot from A to BC. The reflection of H in BC lies on omega, so power at H gives $3(2HD)=2\cdot6$, hence HD=2 and AD=5. Use coordinates $H=(0,0),A=(0,3),D=(0,-2)$. The reflected point is $(0,-4)$, so omega has equation $x^2+y^2+ux+y-12=0$ for some real u. Its intersections B,C with y=−2 have x-coordinates satisfying $x^2+ux-10=0$. The circle HBC consequently has equation $x^2+y^2+ux+7y=0$, and its tangent at H is $ux+7y=0$. Parameterize this line by $(x,y)=t(c,s)$ with $c^2+s^2=1$. Substitution into omega gives $t^2-6st-12=0$, since uc+7 s=0. Its roots are−2 and 6 after choosing direction, so s=2/3 and c²=5/9. Therefore $u^2=49s^2/c^2=196/5$. The squared difference of the two base coordinates is $BC^2=u^2+40=396/5$. Thus $[ABC]=(5/2)BC=3\sqrt{55}$, giving 58.

**Answer:** 058.

**Methods:** orthocenter reflection, circle equations, tangent line, chord roots.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight alternatives inspected. The reflected orthocenter fixes the altitude immediately. Explicit circle equations supply the remaining length without assumptions about the relative positions of auxiliary circumcenters.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. An orthocenter tangent determines a chord and an altitude; orthocenter reflection, circle equations, tangent line, chord roots supply the essential reduction.

## 2020 AIME II Problem 3: Cancel a common logarithm factor

If $\log_{2^x}(3^{20})=\log_{2^{x+3}}(3^{2020})$, write x=m/n reduced and find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

Changing both bases to 2 gives $20\log_2(3)/x=2020\log_2(3)/(x+3)$. The nonzero common factor cancels, yielding $20(x+3)=2020x$. Hence x=3/100, which avoids the forbidden bases x=0,−3. The answer is 103.

**Answer:** 103.

**Methods:** change of base, domain restrictions.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. Direct cancellation is sufficient; the final source uses incorrect equality notation between a logarithm and an exponential equation, although its subsequent manipulation reaches the same answer.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Cancel a common logarithm factor; change of base, domain restrictions supply the essential reduction.

## 2020 AIME II Problem 6: A rational recurrence with a five-step return

Set $t_1=20,t_2=21$ and $t_n=(5t_{n-1}+1)/(25t_{n-2})$ for n≥3. Write $t_{2020}=p/q$ reduced and find p+q.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Put $u_n=5t_n$, giving $u_n=(u_{n-1}+1)/u_{n-2}$. Starting from arbitrary positive values a,b, the next five terms are $(b+1)/a$, $(a+b+1)/(ab)$, $(a+1)/b$, a,b. Thus the full two-term state repeats after five steps, proving period 5. Here a=100,b=105, so $t_{2020}=t_5=(a+1)/(5b)=101/525$. The answer is 626.

**Answer:** 626.

**Methods:** rational recurrence, symbolic periodicity, state repetition.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Returning to both initial terms establishes the period; the final source stops after only the first repeated term, which by itself would not prove a second-order recurrence periodic.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A rational recurrence with a five-step return; rational recurrence, symbolic periodicity, state repetition supply the essential reduction.

## 2020 AIME II Problem 8: Zeros of nested absolute values form a parity interval

Let $f_1(x)=|x-1|$ and $f_n(x)=f_{n-1}(|x-n|)$ for n>1. Find the least n for which the sum of the distinct real zeros of $f_n$ exceeds 500000.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Inductively the zero set is the arithmetic progression from $n-n(n-1)/2$ to $n+n(n-1)/2$, with step 2. For the induction, zeros of $f_n$ are n plus or minus the nonnegative zeros of $f_{n-1}$. Those nonnegative zeros start at 0 or 1 and end at $n(n-1)/2$, so their positive and negative reflections fill exactly the asserted parity interval; the initial cases n=1,2 are immediate. There are $1+n(n-1)/2$ zeros and their average is n. Their sum is $n(n^2-n+2)/2$, strictly increasing for positive n. At n=100 it is 495100; at n=101 it is 510151. Thus the least n is 101.

**Answer:** 101.

**Methods:** absolute-value preimages, arithmetic zero sets, induction.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. The first gives an induction, while the second infers the pattern from initial terms. Explicitly identifying the nonnegative part and its reflected parity interval completes the induction.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, combinatorics. The proof constructs exact recursively generated zero sets, removes duplicate signed representations, and tracks their parity-restricted intervals.

## 2020 AIME II Problem 11: Three pairwise sums of monic quadratics

Let $P(x)=x^2-3x-7$. Monic quadratics Q,R have the property that each pair among P+Q,P+R,Q+R has a common root, with three distinct common roots. Given Q(0)=2, write R(0)=m/n reduced and find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Let the pairwise common roots be p,q,r so that $P+Q=2(x-p)(x-q)$, $P+R=2(x-p)(x-r)$, and $Q+R=2(x-q)(x-r)$. Adding the first two and subtracting the third, then halving, gives $P=x^2-2px+pq+pr-qr$. Thus p=3/2. The analogous Q constant is $pq+qr-pr=2$, whereas P constant is−7. Adding gives 2 pq=−5 and q=−5/3. Substitution gives r=−27/19. Therefore $R(0)=pr+qr-pq=52/19$, so the answer is 71. The explicit polynomials $Q=x^2+(10/3)x+2$ and $R=x^2+(54/19)x+52/19$ verify the three distinct shared roots.

**Answer:** 071.

**Methods:** shared-root factorization, Vieta formulas, linear reconstruction.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Reconstructing P,Q,R from their sums exposes the fixed shared root immediately; explicit polynomials verify that the algebraic values are realizable.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Three pairwise sums of monic quadratics; shared-root factorization, Vieta formulas, linear reconstruction supply the essential reduction.

## 2020 AIME II Problem 13: Tangent lengths and a monotone angle sum

A convex pentagon ABCDE has an incircle and side lengths $AB=5$, $BC=CD=DE=6$, $EA=7$. Find its area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Equal tangents from each vertex give tangent lengths 3,2,4,2,4 in order, by solving adjacent sums equal to the side lengths. If the inradius is r, half the exterior angle at a vertex with tangent length t is $\arctan(t/r)$. The exterior angles sum to 360 degrees, so $\arctan(3/r)+2\arctan(2/r)+2\arctan(4/r)=180^\circ$. The left side strictly decreases with r. At r=4, the last term is 90 degrees, while $2\arctan(1/2)$ is acute with tangent 4/3 and hence complements $\arctan(3/4)$. Thus r=4 is the unique solution. The area is the inradius times semiperimeter, $4\cdot15=60$.

**Answer:** 060.

**Methods:** tangent-length systems, exterior-angle closure, monotonicity.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight alternatives inspected. Monotonic angle closure verifies r=4 and excludes the spurious small root of the quartic without extra geometric casework. The approximation and answer-format guessing alternatives are not proofs.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Tangent lengths and a monotone angle sum; tangent-length systems, exterior-angle closure, monotonicity supply the essential reduction.

## 2020 AIME II Problem 14: Iterated fractional-part preimages

Define $f(x)=x\{x\}$, where $\{x\}=x-\lfloor x\rfloor$. Count modulo $1000$ the solutions of $f(f(f(x)))=17$ in $[0,2020]$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

On each interval $[k,k+1)$, $f$ increases continuously from $0$ to the excluded endpoint $k+1$. For positive $y$, there is exactly one preimage in that interval iff $k+1>y$. Starting at $y=17$, the first branch index $k$ is at least $17$; its preimage lies strictly between $k$ and $k+1$, so each next branch index is at least the previous one. All three indices are at most $2019$. Consequently solutions correspond bijectively to weakly increasing triples from $2003$ integers. Their count is $\binom{2005}3$, with remainder $10$.

**Answer:** 010.

**Methods:** inverse branches, combinations with repetition.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All three branch-count arguments agree. The endpoint 2020 is excluded because its iterates are 0; positive target 17 avoids the separate zero-level issue.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Iterated fractional-part preimages; the proof uses inverse branches, combinations with repetition.

## 2021 AIME I Problem 5: Integer arithmetic progressions satisfying a square identity

A strictly increasing three-term integer arithmetic progression is special when the sum of its squared terms equals its middle term times the square of its common difference. Find the sum of the final terms of all special progressions.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Write the terms as a−d,a,a+d with integer d>0. The condition gives $3a^2+2d^2=ad^2$, so a>2 and $d^2=3a+6+12/(a-2)$. Thus a−2 is a positive divisor of 12, leaving a=3,4,5,6,8,14. The corresponding squared differences are 27,24,25,27,32,49. Only a=5,d=5 and a=14,d=7 work. Their final terms are 10 and 21, whose sum is 31.

**Answer:** 031.

**Methods:** arithmetic progression symmetry, rational divisibility, square testing.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. Dividing the polynomial expression reduces to six possible middle terms and keeps the allowed zero first term. Several squarefree-kernel alternatives suppress the rational-square justification, which the divisor list avoids.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Integer arithmetic progressions satisfying a square identity; arithmetic progression symmetry, rational divisibility, square testing supply the essential reduction.

## 2021 AIME I Problem 7: Simultaneous sine maxima

Count $1\le m<n\le 30$ for which some real $x$ satisfies $\sin(mx)+\sin(nx)=2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Both sines must be $1$. After removing the common power of $2$ from $m, n$, this is possible exactly when the remaining odd parts are congruent modulo $4$. Necessity follows from $m/n=(4u+1)/(4v+1)$ after reducing; sufficiency follows by multiplying equal odd residues by $1$ or $3$ to make both $1$ modulo $4$. Partition $1\ldots30$ by $2$-adic valuation and odd part modulo $4$. Class sizes are $8,7$; $4,4$; $2,2$; $1,1$; $1$. The answer is $\binom82+\binom72+2\binom42+2\binom22=63$.

**Answer:** 063.

**Methods:** equivalence classes, trigonometry hybrid.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 0 makes an invalid claim that its scale k>1 must be integral; source 1 contains an unrelated corrupted paragraph; source 2 leaves a 14-pair count unexplained. Equal 2-adic valuations and equal odd residues mod 4 give the clean necessary-and-sufficient criterion.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Simultaneous sine maxima; the proof uses equivalence classes, trigonometry hybrid.

## 2021 AIME I Problem 8: Counting levels with twelve preimages

Count integers $c$ for which $||20|x|-x^2|-c|=21$ has $12$ distinct real solutions.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

For $h(x)=|20|x|-x^2|$, a horizontal level $t$ has $6$ preimages exactly when $0<t<100$, and fewer otherwise. The equation uses disjoint levels $t=c-21$ and $c+21$. Twelve preimages require both levels in $(0,100)$, equivalently $21<c<79$. There are $57$ integers.

**Answer:** 057.

**Methods:** preimage counting, algebra hybrid.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 1 repeats x=10 where its second zero should be 20. Source 3 calls the square root the discriminant and does not fully impose the signs introduced by absolute values. Horizontal-level multiplicity gives the rigorous count.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Counting levels with twelve preimages; the proof uses preimage counting, algebra hybrid.

## 2021 AIME I Problem 15: Perpendicular parabolas share a circle of intersection

For positive integer k, consider $y=x^2-k$ and $x=2(y-20)^2-k$. Let S contain k for which the curves meet at four distinct points on a circle of radius at most 21. Find the sum of the least and greatest members of S.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Adding the first equation to half the second and completing squares shows every intersection lies on $(x-1/4)^2+(y-41/2)^2=(24k+325)/16$. Thus the radius restriction is exactly k≤280. Substitution gives $F_k(x)=2(x^2-k-20)^2-x-k=0$. For k≥6, put $t=\sqrt{k+20}<k$. Then $F_k(-t)<0$, $F_k(0)>0$, $F_k(t)<0$, and $F_k(x)\to+\infty$ at both ends. Four disjoint sign-changing intervals give four distinct real roots. For k=5, x=−5 is a root with derivative−1, so F is negative just to its right; together with F(0)>0,F(5)<0 and the positive tail, this again gives four distinct roots. For k≤4, a negative intersection must have −k≤x≤0, giving y≤k²−k≤12 from the first curve, but $y\ge20-\sqrt{k/2}>18$ from the second, impossible. The quartic has at most two positive roots by its two coefficient sign changes. Thus S consists exactly of integers 5 through 280, and the answer is 285.

**Answer:** 285.

**Methods:** linear combinations of conics, circle completion, real-root sign intervals.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. The circle equation is elementary; one longer focal-parameter source gives an incorrect radius formula. The sign-interval proof replaces sketch-based claims that four intersections exist and handles the boundary k=5 explicitly.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Perpendicular parabolas share a circle of intersection; linear combinations of conics, circle completion, real-root sign intervals supply the essential reduction.

## 2021 AIME II Problem 4: Missing coefficients determine a shared conjugate pair

Real-coefficient cubics $x^3+ax+b$ and $x^3+cx^2+d$ have roots−20 and−21 respectively, and share a root $m+i\sqrt n$ with positive integers m,n. Find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

The conjugate $m-i\sqrt n$ is also a root of both cubics. In the first cubic, the root sum is zero, so −20+2 m=0 and m=10. In the second, the coefficient of x is zero, so $-21(2m)+(m^2+n)=0$. Thus n=420−100=320, and m+n=330. The common factor $x^2-20x+420$ multiplied by x+20 or x+21 verifies both missing coefficients.

**Answer:** 330.

**Methods:** conjugate roots, Vieta formulas, missing coefficients.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. The two zero coefficients give the answer immediately. Some longer alternatives assume a real coefficient is an integer divisor or stop after finding one numerical candidate; neither is needed.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Missing coefficients determine a shared conjugate pair; conjugate roots, Vieta formulas, missing coefficients supply the essential reduction.

## 2021 AIME II Problem 7: Partial symmetric sums determine variables in reverse order

Real a,b,c,d satisfy $a+b=-3$, $ab+bc+ca=-4$, $abc+bcd+cda+dab=14$, and $abcd=30$. Write $a^2+b^2+c^2+d^2=m/n$ reduced and find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

The cubic-sum equation is $abc-4d=14$. Using abc=30/d gives $4d^2+14d-30=0$, so d=−5 or 3/2. Also ab=3 c−4, hence $3c^2-4c=abc$. If d=−5 then abc=−6 and this quadratic has negative discriminant 16−72. Thus d=3/2,abc=20, and c=−2 or 10/3. The latter would give ab=6 together with a+b=−3, again impossible for real a,b. Therefore c=−2,ab=−10, and {a,b}={−5,2}. The square sum is $25+4+4+9/4=141/4$, giving 145.

**Answer:** 145.

**Methods:** triangular symmetric elimination, discriminant feasibility.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. Solving from the highest partial symmetric sum downward gives only quadratic equations. The last source repeatedly prints abc=14 instead of 20 and 3/10 instead of 10/3; the corrected elimination excludes all nonreal branches.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Partial symmetric sums determine variables in reverse order; triangular symmetric elimination, discriminant feasibility supply the essential reduction.

## 2021 AIME II Problem 15: Walking to the next square with two step sizes

For positive integers n, define f(n)=$\sqrt{n}$ at squares and f(n)=1+f(n+1) otherwise. Define g(n)=$\sqrt{n}$ at squares and g(n)=2+g(n+2) otherwise. Find the least n for which f(n)/g(n)=4/7.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

A square gives ratio 1, so write n=m²+k with integers m≥1 and 0<k<2 m+1. If k is odd, n has the same parity as $(m+1)^2$, and both recursions stop there, giving equal values. Thus k is even, and g skips that square to $(m+2)^2$. Directly summing the increments gives $f(n)=3m+2-k$ and $g(n)=5m+6-k$. The ratio equation reduces to m=3 k+10. Positive even k has minimum 2, giving m=16,n=258, and n increases with k. This candidate satisfies k<2 m+1 and gives f=48,g=84, verifying the ratio.

**Answer:** 258.

**Methods:** next-square stopping times, parity, linear Diophantine reduction.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. Using distance above the preceding square turns the ratio condition directly into m=3 k+10. The longer quadratic-formula approaches require additional interval checks and do not shorten the proof.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Walking to the next square with two step sizes; next-square stopping times, parity, linear Diophantine reduction supply the essential reduction.

## 2022 AIME I Problem 1: Cancel the quadratic terms before evaluating

Quadratics P,Q have leading coefficients 2 and−2, respectively, and both graphs pass through (16,54) and (20,53). Find P(0)+Q(0).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

The quadratic terms cancel in R=P+Q, so R is linear. Its values are R(16)=108 and R(20)=106, giving slope−1/2. Therefore $R(0)=108+16/2=116$.

**Answer:** 116.

**Methods:** linear cancellation, interpolation.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. Adding the polynomials first reduces the task to a line; solving for all four lower coefficients is unnecessary.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Cancel the quadratic terms before evaluating; linear cancellation, interpolation supply the essential reduction.

## 2022 AIME I Problem 4: Roots-of-unity exponent pairs

Let $w=(\sqrt3+i)/2$ and $z=(-1+i \sqrt3)/2$. Count $1\le r, s\le 100$ with $iw^r=z^s$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Polar angles reduce the equation to $r+3\equiv4s\pmod{12}$. Hence $r=4t-3$ for $1\le t\le 25$ and $s=t$ modulo $3$. Among $t$ there are $9$ of residue $1$, and $8$ each of $0,2$; among $s$ there are $34$ of residue $1$, and $33$ each of $0,2$. Count $9\cdot34+16\cdot33=834$.

**Answer:** 834.

**Methods:** residue counting, roots of unity.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both polar-angle reductions give the same residue-class count.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Roots-of-unity exponent pairs; the proof uses residue counting, roots of unity.

## 2022 AIME I Problem 5: Subtract squared swimming velocities

A 264-foot-wide river flows east at 14 feet per minute. Melanie, swimming at 80 feet per minute relative to the water, starts D feet downstream from Sherry, whose swimming speed is 60. They swim straight to the same opposite-bank point, equally far from their starting points, and arrive together. Find D.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Equal travel times and equal ground distances give equal ground speeds. Their ground velocity vectors are therefore (−u,v) and (u,v), with v>0, since the destination lies above their starting midpoint. Relative to the water these become (−u−14,v) and (u−14,v). Subtracting their squared speed equations gives $56u=80^2-60^2=2800$, so u=50. Then $v^2=60^2-36^2=2304$, giving v=48. The travel time is 264/48=11/2 minutes, and D=2 u(11/2)=550.

**Answer:** 550.

**Methods:** relative velocity, difference of squares, symmetry.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. Equal-time symmetry makes the two horizontal ground velocities opposites; subtracting their squared speeds eliminates the crossing speed immediately.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. Subtract squared swimming velocities; relative velocity, difference of squares, symmetry supply the essential reduction.

## 2022 AIME I Problem 15: Eliminate radicals while retaining their signs

Positive x,y,z satisfy $\sqrt{2x-xy}+\sqrt{2y-xy}=1$, $\sqrt{2y-yz}+\sqrt{2z-yz}=\sqrt2$, and $\sqrt{2z-zx}+\sqrt{2x-zx}=\sqrt3$. Write $[(1-x)(1-y)(1-z)]^2=m/n$ reduced; find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Put u=1−x,v=1−y,w=1−z. Squaring once gives uv≥1/2, vw≥0, uw≥−1/2. Squaring again and simplifying gives $u^2+v^2-uv=3/4$, $v^2+w^2=1$, and $u^2+w^2+uw=3/4$. Subtracting the first and third factors as $(v+w)(v-w-u)=0$. If v+w=0, the middle equation gives vw=−1/2, contradicting vw≥0. Hence u=v−w. Substituting into the other equations yields vw=1/4 and u squared=1/2. Therefore $(uvw)^2=(1/2)(1/16)=1/32$, and the answer is 33. Existence is verified, for example, by $x=2\cos^2(22.5^\circ)$, $y=2\cos^2(7.5^\circ)$, $z=2\cos^2(37.5^\circ)$.

**Answer:** 033.

**Methods:** radical elimination, retained sign constraints, symmetric factorization.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. Trigonometric parametrizations require supplementary-angle checks. The algebraic proof retains the first-squaring signs, which also justify rejecting the v+w=0 branch omitted in one source.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Eliminate radicals while retaining their signs; radical elimination, retained sign constraints, symmetric factorization supply the essential reduction.

## 2022 AIME II Problem 4: Divide exponentiated logarithm identities

For positive x other than 1/20 and 1/2, $\log_{20x}(22x)=\log_{2x}(202x)$. Their common value is $\log_{10}(m/n)$ with m,n coprime positive integers. Find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Call the common value a. Exponentiation gives $(20x)^a=22x$ and $(2x)^a=202x$. Division cancels x and yields $10^a=11/101$. Thus a=log base 10 of 11/101, and the answer is 112. For completeness a is negative, and $x^{a-1}=202/2^a$ has one positive solution. This solution cannot equal either forbidden base value, since the corresponding exponential equation would read 1=11/10 or 1=101.

**Answer:** 112.

**Methods:** change of base, exponential cancellation, logarithm domains.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. Dividing the exponentiated equations eliminates x without a quadratic in log x. The domain restrictions are compatible with the resulting solution.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Divide exponentiated logarithm identities; change of base, exponential cancellation, logarithm domains supply the essential reduction.

## 2022 AIME II Problem 6: Sharp bounds for two ordered coordinates

Reals $x_1\le\cdots\le x_{100}$ satisfy $\sum |x_i|=1$ and $\sum x_i=0$. Write the maximum of $x_{76}-x_{16}$ as m/n in lowest terms; find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

The positive terms total 1/2, and the absolute values of negative terms total 1/2. If x 76>0, the last 25 terms give 25 x 76≤1/2; if x 76≤0, the same upper bound is automatic. Thus x 76≤1/50. Similarly the first 16 terms give x 16≥−1/32, with the nonnegative case automatic. Therefore the difference is at most $1/50+1/32=41/800$. Equality is attained by 16 entries−1/32,59 zeros, and 25 entries 1/50. The answer is 841.

**Answer:** 841.

**Methods:** ordered-coordinate bounds, positive-negative mass, equality construction.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Bounds on partial sums, rather than unjustified equalities for them, prove the upper bound. The explicit sequence proves it is a maximum.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Sharp bounds for two ordered coordinates; ordered-coordinate bounds, positive-negative mass, equality construction supply the essential reduction.

## 2022 AIME II Problem 11: Two angle-bisector reflections determine a quadrilateral

A convex quadrilateral ABCD has AB=2,AD=7,CD=3. The acute angles DAB and ADC have internal bisectors meeting at the midpoint M of BC. Find the square of its area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Take A=(0,0),D=(7,0). Reflection in AM takes B to P=(2,0), while reflection in DM takes C to Q=(4,0). Since MB=MC, we have MP=MQ; hence M=(3,h) with h>0. The reflection formulas give $B=\frac{12}{9+h^2}(3,h)-(2,0)$ and $C=(10,0)+\frac{24}{16+h^2}(-4,h)$. Because B+C=2 M, their vertical coordinates yield $6/(9+h^2)+12/(16+h^2)=1$. This simplifies to $(h^2-5)(h^2+12)=0$, so h=$\sqrt{5}$. M is equidistant from the three lines AB,AD,DC; its distance to each is h. Decomposing the quadrilateral into ABM,ADM,DCM gives area $(2+7+3)h/2=6\sqrt5$. Its square is 180.

**Answer:** 180.

**Methods:** reflection in angle bisectors, midpoint coordinates, equidistance area sum.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All seven alternatives inspected. Reflection gives a short coordinate derivation without an unproved similarity. Several alternatives contain mislabeled angle variables or a typographical AM-squared identity; the final barycentric approach is also valid once its extended-line configuration is established.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Two angle-bisector reflections determine a quadrilateral; reflection in angle bisectors, midpoint coordinates, equidistance area sum supply the essential reduction.

## 2022 AIME II Problem 12: Pair the foci of two intersecting ellipses

Reals a>4,b>1,x,y satisfy $x^2/a^2+y^2/(a^2-16)=1$ and $(x-20)^2/(b^2-1)+(y-11)^2/b^2=1$. Find the minimum of a+b.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

The first ellipse has foci U=(−4,0),V=(4,0), and the second has foci W=(20,10),Z=(20,12). For P=(x,y), their focal definitions give $2(a+b)=PU+PV+PW+PZ\ge UW+VZ=26+20=46$. Equality holds when P lies on both segments UW and VZ. Their intersection is P=(14,15/2), giving PU=39/2,PV=25/2,PW=13/2,PZ=15/2, hence a=16,b=7. These satisfy the strict parameter bounds. The attained minimum is 23.

**Answer:** 023.

**Methods:** ellipse focal definition, paired triangle inequalities, equality verification.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** The single stored solution inspected. Pairing the foci proves the bound, and the explicit segment intersection verifies simultaneous equality and both strict parameter restrictions.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Pair the foci of two intersecting ellipses; ellipse focal definition, paired triangle inequalities, equality verification supply the essential reduction.

## 2022 AIME II Problem 13: A coefficient reduced to stars and bars

Find coefficient $x^{2022}$ in $(x^{2310}-1)^6/[(x^{105}-1)(x^{70}-1)(x^{42}-1)(x^{30}-1)]$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Below degree $2310$, the numerator contributes only $1$. Geometric-series expansion counts $105a+70b+42c+30d=2022$ in nonnegative integers. Modular reductions force $a=2A,b=3B,c=5C+1,d=7D+3$. Substitution gives $A+B+C+D=9$. This bijection yields $\binom{12}3=220$.

**Answer:** 220.

**Methods:** generating functions, modular reduction, stars and bars.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 0 drops binomial coefficients from a full expansion, harmless only after restricting to degree 2022. Source 1 skips the modular exhaustion argument. Sources 2 and 4 write infinite series after polynomial divisions; that equality needs truncation. The original proof uses formal coefficients below 2310 and explicit residues.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra, number_theory. A coefficient reduced to stars and bars; the proof uses generating functions, modular reduction, stars and bars.

## 2023 AIME I Problem 2: Two logarithms reduce to one variable

Positive b,n with b≠1 satisfy $\sqrt{\log_b n}=\log_b\sqrt n$ and $b\log_b n=\log_b(bn)$. Write n=j/k reduced and find j+k.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

Put t=log base b of n. The equations become $\sqrt{t}$=t/2 and bt=1+t. The second excludes t=0; the first then gives t=4. Hence b=5/4 and $n=b^4=625/256$. The answer is 881.

**Answer:** 881.

**Methods:** logarithm laws, substitution, excluded zero branch.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Explicitly excluding t=0 before division closes the only branch issue.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Two logarithms reduce to one variable; logarithm laws, substitution, excluded zero branch supply the essential reduction.

## 2023 AIME I Problem 9: A cubic with one other equal-value integer

Count monic cubics $x^3+ax^2+bx+c$ with $a, b, c$ in $[-20,20]$ for which exactly one integer $m$ unequal $2$ satisfies $p(m)=p(2)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Divide by $m-2$ to obtain $m^2+(a+2)m+(4+2a+b)=0$. Since one integer root forces the other integer, we need either a double root other than $2$, or two distinct roots with one equal $2$. The double-root condition is $b=(a-2)^2/4-4$; the bounds allow $9$ even values of $a$ but $a=-6$ must be excluded, giving $8$. The root $2$ condition is $b=-4a-12$, allowing $a=-8,\ldots,2$, but again excluding $-6$, giving $10$. The coefficient $c$ has $41$ choices. Total $(8+10)41=738$.

**Answer:** 738.

**Methods:** root multiplicities, bounded counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both stored solutions inspected. They classify the factorization into one double root and one simple root. The alternate source has a constant-term copy typo in its second case, but the admissible-root counts 10 and 8 and total 738 are sound.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. A cubic with one other equal-value integer; the proof uses root multiplicities, bounded counting.

## 2023 AIME I Problem 10: Bound the floor error before summing residues

For a positive integer a, put $U=\sum_{n=1}^{2023}\lfloor(n^2-na)/5\rfloor$. Exactly one a makes −1000<U<1000. Find a+U.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

The sum without floors is $T=\frac{2023\cdot1012}{5}(1349-a)$. Since 0≤T−U<2023, the prescribed range forces −1000<T<3023. The coefficient 2023 times 1012/5 exceeds 400000, so the only integral a is 1349, giving T=0. For n modulo 5 equal to 0,1,2,3,4, the residues of n(n−1349) are 0,2,1,2,0. Each of residues 1,2,3 occurs 405 times in 1 through 2023. The total fractional-part correction is 405(2+1+2)/5=405. Thus U=−405 and a+U=944.

**Answer:** 944.

**Methods:** floor-error bounds, residue cycles, polynomial sums.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. A rigorous error bound identifies a before the residue calculation. The integral approximation in the final alternative does not by itself prove uniqueness and also gives the fractional-part sum the wrong sign.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Bound the floor error before summing residues; floor-error bounds, residue cycles, polynomial sums supply the essential reduction.

## 2023 AIME I Problem 13: A Gram determinant distinguishes two rhombohedra

Every face of each of two noncongruent parallelepipeds is a rhombus with diagonals $\sqrt{21}$ and $\sqrt{31}$. Write the larger volume divided by the smaller as m/n reduced; find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Let u,v,w be the three edge vectors at a vertex. The parallelogram law gives squared edge length 13 and each pairwise dot product equal to plus or minus 5/2. The squared volume is the Gram determinant $13^3-13\cdot3(5/2)^2+2(u\cdot v)(v\cdot w)(w\cdot u)$. Consequently its two possible values are $13^3-975/4\pm125/4$, namely 3969/2 and 1922. Both are positive and realized by taking all three off-diagonal dot products positive or all negative. Changing the sign of an edge reverses two dot-product signs, so the two product signs exhaust the possibilities up to congruence. The volume ratio is $\sqrt{(3969/2)/1922}=63/62$, giving 125.

**Answer:** 125.

**Methods:** Gram determinant, parallelogram law, sign invariants.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. The determinant treats all sign patterns at once and explains why only two volumes occur. The tetrahedron alternatives are shorter numerically but require establishing their symmetric vertex choices.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A Gram determinant distinguishes two rhombohedra; Gram determinant, parallelogram law, sign invariants supply the essential reduction.

## 2023 AIME I Problem 15: A bounded Gaussian-integer search with all sign cases

Find the largest prime p<1000 for which a Gaussian integer z has absolute value $\sqrt{p}$ and p,Re(z cubed),Im(z cubed) are positive side lengths of a triangle.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Gaussian units and conjugation permute and change signs of the two cubic components. Thus existence is equivalent to testing their absolute values for z=a+bi with integers a≥b≥0 and a squared+b squared=p. The case b=0 cannot give a prime norm, while a=b gives only p=2. For a>b, if a squared≤3 b squared, the absolute component difference is $(a-b)(a^2+4ab+b^2)>p$, impossible. Otherwise both components are positive, their sum exceeds their Euclidean norm $p^{3/2}>p$, and the remaining triangle condition is $(a+b)|a^2-4ab+b^2|<a^2+b^2$. The bounds are 1≤b≤15 and $\sqrt{3}$ times b<a≤floor($\sqrt{999−b squared}$). Testing these explicit integer intervals gives the following possible norm lists for b=1 through 8: (10,17),(53,68),(130,153),(241),(349,386),(520,565),(725,778),(905,964); for b=9 through 15 there are none. The prime norms are 17,53,241,349. Finally z=18+5 i has cube 4482+4735 i, whose component difference 253 is less than 349. Hence the largest prime is 349.

**Answer:** 349.

**Methods:** Gaussian integer norms, triangle inequalities, exhaustive bounded search.

**Verification:** Exhaustive integer pairs in the stated bounds reproduce the displayed table; primality and the witness cube are independently checked.

**Source comparison:** Both alternatives inspected. Their reductions of the signs are not fully justified: mixed signs can give positive cubic components. Gaussian-unit symmetry followed by the separate a squared≤3 b squared branch covers every sign case. The explicit bounded table makes the finite exclusion reproducible.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. A bounded Gaussian-integer search with all sign cases; Gaussian integer norms, triangle inequalities, exhaustive bounded search supply the essential reduction.

## 2023 AIME II Problem 1: Pair opposite terms of an arithmetic progression

Six tree yields form an arithmetic progression, with largest twice smallest and total 990. Find the largest yield.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

Pairing first with last, second with fifth, and third with fourth shows the sum is three times the sum of the extreme yields. If the smallest is x, this is 3(x+2 x)=990, so x=110 and the largest is 220. The common difference is 22, giving integral yields as required.

**Answer:** 220.

**Methods:** arithmetic progression endpoint pairing.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. Endpoint pairing gives the total immediately; the common difference checks the count interpretation.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Pair opposite terms of an arithmetic progression; arithmetic progression endpoint pairing supply the essential reduction.

## 2023 AIME II Problem 4: Subtract a symmetric quadratic system

Real x,y,z satisfy xy+4 z=yz+4 x=zx+4 y=60. Find the sum of squares of all distinct possible x values.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Subtracting pairs gives $(x-z)(y-4)=(y-x)(z-4)=(z-y)(x-4)=0$. If all variables are equal to t, then t squared+4 t=60, so t=6 or−10. Otherwise a pair differs, forcing the third variable to be 4. Substitution then forces another variable to be 4 and the remaining one to be 11. Thus the full solution set consists of (6,6,6),(−10,−10,−10) and permutations of (4,4,11). The distinct x values are 6,−10,4,11, with square sum 273.

**Answer:** 273.

**Methods:** subtraction and factorization, symmetric systems, exhaustive branches.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. Factored differences give all branches without division. A quadratic-formula source has sign errors and unjustifiably assumes real variables are integer divisors; those assumptions are avoided.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Subtract a symmetric quadratic system; subtraction and factorization, symmetric systems, exhaustive branches supply the essential reduction.

## 2023 AIME II Problem 8: Conjugate pairs collapse a seventh-root product

Let omega be a primitive seventh root of unity. Evaluate $\prod_{k=0}^6(\omega^{3k}+\omega^k+1)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

For k=1,2,3, put t=omega to the k. Pairing its factor with the conjugate gives $(1+t+t^3)(1+t^{-1}+t^{-3})=3+t+t^{-1}+t^2+t^{-2}+t^3+t^{-3}$. The six nonconstant terms sum to−1, because t is a nontrivial seventh root. Thus each conjugate pair contributes 2. The k=0 factor is 3, so the product is 3 times 2 cubed=24.

**Answer:** 024.

**Methods:** roots of unity, conjugate pairing, geometric sums.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. Pairing conjugates proves positivity as well as the value. One source incorrectly prints the zeroth factor as 0, and another doubles the exponent indices inconsistently; the direct expansion is unambiguous.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Conjugate pairs collapse a seventh-root product; roots of unity, conjugate pairing, geometric sums supply the essential reduction.

## 2023 AIME II Problem 13: Prove the integrality class before counting last digits

For acute A, tan A=2 cos A. Count positive n≤1000 for which sec to the nth power A plus tan to the nth power A is an integer ending in 9.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Put alpha=sec A,beta=tan A, so alpha beta=2 and alpha squared−beta squared=1. Thus $u=\alpha^2=(\sqrt{17}+1)/2$ and $v=\beta^2=(\sqrt{17}-1)/2$. Conjugation in the field of $\sqrt{17}$ sends u to−v and v to−u. Therefore u to an odd power plus v to that power is nonzero and changes sign under conjugation, so is irrational. If n is odd, $(\alpha^n+\beta^n)^2=u^n+v^n+2^{n+1}$ is irrational; if n=2 k with k odd, the original sum is irrational. For n=4 m, let c_m=u to the power 2 m plus v to the power 2 m. Since u squared+v squared=9 and u squared times v squared=16, $c_0=2,c_1=9,c_m=9c_{m-1}-16c_{m-2}$, proving integrality. For m≥1 the terms are odd. Modulo 5 their residues repeat 4,4,2, so the units digit is 9 exactly when 3 does not divide m. There are 250−floor(250/3)=167 such m.

**Answer:** 167.

**Methods:** quadratic conjugation, irrationality, power-sum recurrence, residue periods.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. Each asserts without proof that only multiples of 4 yield integers. The conjugation argument supplies that missing exclusion, including all odd exponents. The recurrence then rigorously gives the last-digit cycle.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Prove the integrality class before counting last digits; quadratic conjugation, irrationality, power-sum recurrence, residue periods supply the essential reduction.

## 2024 AIME I Problem 1: Subtract travel times to eliminate a fixed stop

A 9-kilometer walk plus a fixed coffee stop takes 4 hours at speed s km/h and 2 hours 24 minutes at speed s+2. How many minutes does the same trip take at speed s+1/2?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

Write the stop duration as t hours. Subtracting $9/s+t=4$ and $9/(s+2)+t=12/5$ gives $18/[s(s+2)]=8/5$. Hence $(2s-5)(2s+9)=0$, and positivity gives s=5/2. Then t=2/5. At speed 3 the total time is 3+2/5=17/5 hours, or 204 minutes.

**Answer:** 204.

**Methods:** rate equations, elimination, positive-root selection.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. Subtracting eliminates the common stop. The second alternative guesses a rational speed using an unjustified numerator-divisibility claim; the quadratic proves the value.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Subtract travel times to eliminate a fixed stop; rate equations, elimination, positive-root selection supply the essential reduction.

## 2024 AIME I Problem 2: Multiply reciprocal logarithms

Reals x,y>1 satisfy $\log_x(y^x)=\log_y(x^{4y})=10$. Find xy.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

The equations are $x\log_x y=10$ and $4y\log_y x=10$. Multiplying and using $\log_x y\log_y x=1$ gives 4 xy=100, so xy=25.

**Answer:** 025.

**Methods:** reciprocal logarithms, multiplication of equations.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. The first three correctly determine the product. The last two incorrectly conclude x=10,y=5/2; these individual values do not satisfy the original logarithm equations.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Multiply reciprocal logarithms; reciprocal logarithms, multiplication of equations supply the essential reduction.

## 2024 AIME I Problem 7: A reciprocal becomes a conjugate on a circle

For complex z with |z|=4, find the largest possible real part of $(75+117i)z+(96+144i)/z$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Write z=a+bi, so a squared+b squared=16 and $1/z=\overline z/16$. The required real part simplifies to 81 a−108 b. Cauchy–Schwarz bounds it by $\sqrt{81^2+108^2}\sqrt{a^2+b^2}=135\cdot4=540$. Equality holds at $(a,b)=(12/5,-16/5)$, so 540 is attained.

**Answer:** 540.

**Methods:** conjugate reciprocal, linear optimization on a circle, Cauchy–Schwarz.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All ten alternatives inspected. Several introduce sign errors or incorrect imaginary coefficients while retaining the correct final maximum. The conjugate identity and equality case give a complete two-step optimization.

**Archived entries inspected:** 10 of 10. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. A reciprocal becomes a conjugate on a circle; conjugate reciprocal, linear optimization on a circle, Cauchy–Schwarz supply the essential reduction.

## 2024 AIME I Problem 9: A rhombus approaches a hyperbola’s asymptote

Four points on $x^2/20-y^2/24=1$ form a rhombus with diagonal intersection at the origin. Find the greatest real number strictly below BD squared for every such rhombus.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

The diagonals are perpendicular and bisect each other. Write their lines as y=mx and y=−x/m. Each must meet the hyperbola, so $5/6<m^2<6/5$. A point B on the first line has $x^2=120/(6-5m^2)$, hence $BD^2=480(1+m^2)/(6-5m^2)$. This is strictly increasing in m squared; as m squared decreases to 5/6 it tends to 480, without reaching it. Every m squared inside the stated interval yields four valid points and a rhombus, so values approach 480 arbitrarily closely. Therefore 480 is the greatest strict lower bound.

**Answer:** 480.

**Methods:** perpendicular diagonals, hyperbola asymptotes, unattained infimum.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four stored entries inspected. One entry explicitly warns that its square argument is wrong, and another merely guesses a product of constants. The slope interval proves both the bound and its sharpness.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A rhombus approaches a hyperbola’s asymptote; perpendicular diagonals, hyperbola asymptotes, unattained infimum supply the essential reduction.

## 2024 AIME I Problem 12: Count branch pairs with a rigorous curvature certificate

Define $f(t)=||t|-1/2|$ and $g(t)=||t|-1/4|$. How many real pairs satisfy $y=4g(f(\sin(2\pi x)))$ and $x=4g(f(\cos(3\pi y)))$?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Put $H(t)=4g(f(t))$, $F(x)=H(\sin(2\pi x))$, and $G(y)=H(\cos(3\pi y))$. All solutions lie in the unit square. On 0≤t≤1, H has values 1,0,1,0,1 at t=0,1/4,1/2,3/4,1 and is linear between them. Hence F has 16 full monotone branches and G has 24. We prove each branch pair has exactly one intersection, except the final pair, which has two.

Here is the needed calculus lemma. For a three-times differentiable function u with nonzero derivative, define its Schwarzian by $S(u)=u^{\prime\prime\prime}/u^{\prime}-\tfrac32(u^{\prime\prime}/u^{\prime})^2$. Direct differentiation gives $S(v\circ u)=S(v)(u)(u^{\prime})^2+S(u)$. Every affine sine branch has $S(u)=-c^2[1+\tfrac32\tan^2(cx+d)]<0$; cosine branches have the analogous cotangent formula. Thus a composition h of two such branches has S(h)<0. When h is increasing, $\phi=(h^{\prime})^{-1/2}$ satisfies $\phi^{\prime\prime}=-S(h)\phi/2>0$. There cannot be two fixed points a<b with h derivative at least 1 at both: strict convexity would give phi<1 between them, hence h derivative>1, contradicting $h(b)-h(a)=b-a$ after integration. Consequently, if h(x)−x is negative at the left end and positive at the right, it has exactly one zero. Indeed continuity gives an upward crossing; any additional downward crossing or tangency forces a second zero with derivative of h at least 1, which was excluded.

Fix one branch of F and one of G. Restrict the x interval so that F traverses the domain of that G branch, and put h=G composed with F. At its ends h takes values 0 and 1. If h decreases, h(x)−x strictly decreases and has exactly one zero. If h increases and the endpoints are interior to the unit interval, the lemma gives exactly one zero. A solution at any branch boundary would have x or y equal 0 or 1; using F(0)=F(1)=G(0)=G(1)=1 shows that only (1,1) is possible. Thus no ordinary branch pairs share solutions.

For the final pair, the interval ends at 1, h is increasing, h(1)=1, and its left endpoint a has h(a)=0<a. Moreover the left derivative at 1 is h derivative=G derivative at 1 times F derivative at 1=0. Hence h(x)−x is positive just left of 1, giving an interior upward crossing. The same convexity lemma excludes any further interior zero. This pair therefore contributes that interior point and (1,1). The exact total is $16\cdot24+1=385$.

**Answer:** 385.

**Methods:** piecewise monotone branches, Schwarzian derivative, strict convexity, intersection counting.

**Verification:** Exact branch counts and the analytic uniqueness proof certify 385; numerical verification is supplemental, not the basis for the count.

**Source comparison:** All four stored entries inspected, including the figure-link entry. The source branch counts do not prove uniqueness per branch pair, and a small-angle approximation cannot certify the extra corner root. The self-contained negative-Schwarzian lemma repairs both gaps and was independently checked by the parent reviewer.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, combinatorics. The intersection count uses sixteen by twenty-four monotone branch pairs, a rigorous uniqueness certificate on each pair, and a separate extra corner intersection.

## 2024 AIME I Problem 15: A double-root boundary gives the largest box diagonal

Consider all rectangular boxes of surface area 54 and volume 23. Let r be the least radius such that each box fits inside a sphere of radius r. Write r squared=p/q reduced; find p+q.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

For edge lengths x,y,z, we have xy+yz+zx=27 and xyz=23. The least enclosing radius of that box is half its space diagonal: opposite vertices give the lower bound and the midpoint sphere attains it. Thus maximize $x^2+y^2+z^2=(x+y+z)^2-54$. The feasible set is compact: each coordinate lies between 23/27 and 729/92, the latter from 27≥2 $\sqrt{23 x}$. At a maximum of S=x+y+z, at least two edges coincide. Otherwise the cubic $t^3-St^2+27t-23$ has three distinct positive roots, and a small increase in S preserves three positive roots by the intermediate value theorem on three disjoint root neighborhoods, contradicting maximality. Put y=z=a. Then $(a-2)(a^2+2a-23)=0$, so a=2 or−1+2 $\sqrt{6}$. The respective sums S are 39/4 and $(96\sqrt6-21)/23$; the latter is smaller, since $\sqrt{6}$<5/2 gives it less than 219/23<39/4. Hence the maximum occurs at (23/4,2,2). Therefore $r^2=[(23/4)^2+8]/4=657/64$, giving 721.

**Answer:** 721.

**Methods:** enclosing sphere, symmetric cubic, repeated-root extremum, compactness.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. Symmetry alone does not prove two edges are equal at an optimum. The compactness and root-perturbation argument supplies that step, and comparing both positive double-root candidates establishes the global maximum.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A double-root boundary gives the largest box diagonal; enclosing sphere, symmetric cubic, repeated-root extremum, compactness supply the essential reduction.

## 2024 AIME II Problem 3: Digits constrained by row and column sums

Fill a $2\times3$ array with decimal digits, allowing leading zeroes. The two three-digit rows sum to $999$, and the three two-digit columns sum to $99$. Count fillings.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

The row condition forces each vertical digit pair to sum to $9$: the units column has no carry, and the same follows successively for the other columns. Write the top digits as $a,b,c$ and the lower digits as $9-a,9-b,9-c$. The column-number sum is $9(a+b+c)+27$, so $a+b+c=8$. No digit upper bound is active. Stars and bars gives $\binom{10}2=45$.

**Answer:** 045.

**Methods:** digit carries, stars and bars.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The sole source uses column digit complements followed by stars and bars; the independent proof explicitly rules out carries.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. Digits constrained by row and column sums; the proof uses digit carries, stars and bars.

## 2024 AIME II Problem 4: Pair logarithm equations to isolate variables

Positive x,y,z satisfy $\log_2(x/(yz))=1/2$, $\log_2(y/(xz))=1/3$, $\log_2(z/(xy))=1/4$. Write $|\log_2(x^4y^3z^2)|=m/n$ reduced; find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Put a=log base 2 of x,b=log base 2 of y,c=log base 2 of z. Adding equations in pairs gives −2 a=7/12,−2 b=3/4,−2 c=5/6. Hence $4a+3b+2c=-7/6-9/8-5/6=-25/8$. Taking the absolute value gives answer 25+8=33.

**Answer:** 033.

**Methods:** logarithmic linearization, pairwise elimination.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. Pairwise sums isolate the variables immediately. Some sources use multiplication notation where addition of logarithms is intended; the linear system is explicit here.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Pair logarithm equations to isolate variables; logarithmic linearization, pairwise elimination supply the essential reduction.

## 2024 AIME II Problem 11: A symmetric cubic counting problem

Count ordered nonnegative integer triples with $a+b+c=300$ and $a^2b+a^2c+b^2a+b^2c+c^2a+c^2b=6000000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Using $\sum_{\rm sym}a^2b=(a+b+c)(ab+bc+ca)-3abc$, the equation is equivalent to $(100-a)(100-b)(100-c)=0$. Thus at least one coordinate is $100$. For a specified coordinate there are $201$ possibilities for the other two. All pairwise and triple intersections are the single triple $(100,100,100)$. Inclusion-exclusion gives $3\cdot201-3+1=601$.

**Answer:** 601.

**Methods:** factorization, inclusion-exclusion.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All five sources inspected. The direct product factorization is sound. Source index 1 invokes unnecessary Fermat theory; index 3 contains erroneous quadratic formulas and swaps the x=0 and x=100 endpoint descriptions; index 4 confuses shifted and original variables and misprints the common triple. The independent factorization avoids these errors.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra. A symmetric cubic counting problem; the proof uses factorization, inclusion-exclusion.

## 2024 AIME II Problem 12: The unique ladder through a point touches an astroid

Let A=(1/2,0),B=(0,$\sqrt{3}$/2). Among unit segments joining the positive coordinate axes, there is a unique interior point C of AB lying on no other such segment. Write OC squared=p/q reduced, where O is the origin; find p+q.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

For an interior point C=(x,y), a unit segment has intercepts cos theta,sin theta, with 0<theta<$\pi$/2, and contains C exactly when $F(\theta)=x\sec\theta+y\csc\theta=1$. This function tends to infinity at both ends and is strictly convex, because both secant and cosecant have positive second derivatives on this interval. Consequently it has exactly one solution precisely when its minimum equals 1. For the segment AB, theta=$\pi$/3. The derivative condition is $x\sin\theta/\cos^2\theta=y\cos\theta/\sin^2\theta$, so $x/\cos^3\theta=y/\sin^3\theta$. Together with F=1 this gives x=cos cubed theta=1/8 and y=sin cubed theta=3 $\sqrt{3}$/8. Thus OC squared=28/64=7/16, giving 23.

**Answer:** 023.

**Methods:** fixed-length intercept segments, convex envelope, uniqueness via strict convexity.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. A stationary envelope calculation alone does not prove that exactly one segment passes through the point. Strict convexity and endpoint divergence provide the necessary-and-sufficient uniqueness argument.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The unique ladder through a point touches an astroid; fixed-length intercept segments, convex envelope, uniqueness via strict convexity supply the essential reduction.

## 2024 AIME II Problem 13: Evaluate a root product at two conjugate constants

Let omega≠1 satisfy omega to the 13 th power=1. Find the product of $2-2\omega^k+\omega^{2k}$ for k=0 through 12, modulo 1000.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Since 13 is prime, the powers of omega run through all 13 th roots. Factor each term as $(1+i-\omega^k)(1-i-\omega^k)$. Using $\prod_{k=0}^{12}(z-\omega^k)=z^{13}-1$, the product is $|(1+i)^{13}-1|^2$. Now $(1+i)^{13}=(1+i)(2i)^6=-64-64i$. Thus the product is 65 squared+64 squared=8321, whose remainder is 321.

**Answer:** 321.

**Methods:** roots-of-unity resultant, conjugate norm, modular remainder.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. Factoring first turns the 13-factor product into one exact Gaussian-integer norm; the primality of 13 ensures every nontrivial 13 th root is primitive.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Evaluate a root product at two conjugate constants; roots-of-unity resultant, conjugate norm, modular remainder supply the essential reduction.

## 2025 AIME I Problem 8: A circle has exactly one point on each tangent

For real k, the equations $|25+20i-z|=5$ and $|z-4-k|=|z-3i-k|$ have exactly one complex solution z. Write the sum of all possible k as m/n reduced; find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

Writing z=a+bi, the first locus is a circle centered(25,20) of radius 5. Squaring and subtracting in the second gives the line 8 a−6 b−8 k−7=0. There is exactly one common point precisely when its distance from the circle center is 5: $|200-120-8k-7|/10=5$. Hence 73−8 k=±50, giving k=23/8 or 123/8. Their sum is 73/4, so the answer is 77.

**Answer:** 077.

**Methods:** complex distance loci, perpendicular bisector, tangent-line distance.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. The distance-to-line equation proves there are exactly two parameter values. A source’s arbitrary opposite-point experiment is unnecessary and includes a pair that is not diametrically opposite.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A circle has exactly one point on each tangent; complex distance loci, perpendicular bisector, tangent-line distance supply the essential reduction.

## 2025 AIME I Problem 9: Use reflection symmetry to construct the required intersection

Rotate the parabola y=x squared−4 by 60 degrees counterclockwise about the origin. Its unique fourth-quadrant intersection with the original has y-coordinate $(a-\sqrt b)/c$, with a,c coprime positive integers. Find a+b+c.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

The original parabola is invariant under reflection in the y-axis. Composing that reflection with the 60-degree rotation is reflection in the line of angle 120 degrees, namely y=−$\sqrt{3}$ times x. Thus a point of the original parabola on this line also belongs to the rotated parabola. Solving $x^2-4=-\sqrt3x$ gives the positive root $x=(\sqrt{19}-\sqrt3)/2$, which has y<0. By the stated uniqueness, this is the requested intersection. Its height is $y=(3-\sqrt{57})/2$, giving 3+57+2=62.

**Answer:** 062.

**Methods:** reflection-rotation composition, symmetry construction, quadratic intersection.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. One incorrectly claims equal distances force equal y-coordinates, overlooking another algebraic branch; another equates coordinates of differently parameterized points. The reflection construction uses only the uniqueness explicitly supplied by the problem.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Use reflection symmetry to construct the required intersection; reflection-rotation composition, symmetry construction, quadratic intersection supply the essential reduction.

## 2025 AIME I Problem 11: Pair sawtooth intersections by Vieta

Define f periodically with period 4 by f(x)=x on −1≤x<1 and f(x)=2−x on 1≤x<3. Intersect its graph with x=34 y squared. Write the sum of all intersection heights as $(a+b\sqrt c)/d$ in normalized squarefree form; find a+b+c+d.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Every intersection has 0≤x≤34 and −1≤y≤1. On increasing segments y=x−4 k, substitution gives $34y^2-y-4k=0$. For k=0 through 8, both roots lie in the permitted segment (equivalently, −1≤y≤1); no later k works. Their total is 9/34 by Vieta. On decreasing segments y=4 k+2−x, the equation is $34y^2+y-(4k+2)=0$. For k=0 through 7 both roots lie in[−1,1], contributing−8/34; at k=8 only the positive root $(-1+5\sqrt{185})/68$ lies in that interval. These root bounds follow by evaluating the upward quadratics at−1,0,1; no endpoint y=±1 is a root, so adjacent segments do not duplicate points. The total is $(1+5\sqrt{185})/68$, and the answer is 259.

**Answer:** 259.

**Methods:** piecewise quadratic intersections, Vieta pairing, segment-domain checks.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. The full-line roots must be checked against their finite sawtooth segments. The authored proof states those bounds and explains why the final unpaired root is retained.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Pair sawtooth intersections by Vieta; piecewise quadratic intersections, Vieta pairing, segment-domain checks supply the essential reduction.

## 2025 AIME I Problem 12: Order chambers divide an equilateral simplex

In the plane x+y+z=75, the strict inequalities $x-yz<y-zx<z-xy$ describe three disjoint convex regions, exactly one of finite area. Write that finite area as a $\sqrt{b}$ with b squarefree; find a+b.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Put X=x+1,Y=y+1,Z=z+1, so X+Y+Z=78. The inequalities factor as $(X-Y)Z<0$ and $(Y-Z)X<0$. In the positive-coordinate triangle they are exactly 0<X<Y<Z. This is a full connected component: leaving it would require crossing X=0,Z=0,X=Y,or Y=Z, all excluded by the strict inequalities. It is bounded, so the given uniqueness identifies it as the desired component. The positive-coordinate triangle has vertices(78,0,0),(0,78,0),(0,0,78), side 78 $\sqrt{2}$ and area 3042 $\sqrt{3}$. Permuting coordinates partitions it into six congruent order chambers, so the required area is 3042 $\sqrt{3}$/6=507 $\sqrt{3}$. The answer is 510.

**Answer:** 510.

**Methods:** inequality factorization, translated simplex, permutation symmetry.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Translating by 1 reveals the sign structure and divides the positive-coordinate simplex into six congruent regions. This avoids a diagram-only identification and swapped vertex coordinates in one source.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Order chambers divide an equilateral simplex; inequality factorization, translated simplex, permutation symmetry supply the essential reduction.

## 2025 AIME II Problem 4: Telescope both the logarithms and their exponents

Write $\prod_{k=4}^{63}\frac{\log_k(5^{k^2-1})}{\log_{k+1}(5^{k^2-4})}=m/n$ in lowest terms. Find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Extracting exponents splits the product into $\prod_{k=4}^{63}(k^2-1)/(k^2-4)$ times $\prod_{k=4}^{63}\log_k5/\log_{k+1}5$. The logarithms telescope to log base 4 of 64=3. Factoring the quadratics gives the other product as $\prod[(k-1)/(k-2)]\prod[(k+1)/(k+2)]=(62/2)(5/65)=31/13$. Thus the full value is 93/13 and the answer is 106.

**Answer:** 106.

**Methods:** logarithm laws, double telescoping, difference of squares.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. One writes the final logarithm with its bases reversed while still evaluating it as 3; the correct surviving ratio is explicitly log base 4 of 64.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Telescope both the logarithms and their exponents; logarithm laws, double telescoping, difference of squares supply the essential reduction.

## 2025 AIME II Problem 9: Count sine levels and identify double zeros

Let n count roots of $\sin(7\pi\sin(5x))=0$ in 0<x<2 $\pi$, and t count those roots where the graph is tangent to the x-axis. Find n+t.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Roots occur exactly at sin(5 x)=k/7 for integers−7≤k≤7. Over the five periods, each of the twelve nonzero levels with absolute value below 1 has ten crossings, the zero level has nine because both interval endpoints are excluded, and each extreme level±1 has five. Thus n=120+9+10=139. At a root the derivative is $35\pi\cos(k\pi)\cos(5x)$; since cos(kpi)=±1, it vanishes exactly at the ten extreme-level roots. There the inner sine has a nondegenerate extremum while the outer sine has nonzero derivative, so the zero has order two and the axis is tangent. Hence t=10 and n+t=149.

**Answer:** 149.

**Methods:** periodic level counting, endpoint exclusion, root multiplicity.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. Level counts require removing the two open-interval endpoints. The derivative and nondegenerate-extremum observation distinguish genuine tangencies from crossings.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, combinatorics. Periodic level sets are counted separately by interior levels, endpoints, and extreme levels; the extreme-level count also gives tangencies.

## 2025 AIME II Problem 12: Equal-area fan triangles alternate their radial lengths

A nonconvex 11-gon A 1,...,A 11 has perimeter 20. For i=2 through 10, triangle Ai,A 1,A(i+1) has area 1 and cosine of its angle at A 1 equal 12/13. Write A 1 A 2+A 1 A 11 as $(m\sqrt n-p)/q$ in normalized squarefree form; find m+n+p+q.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

The common angle sine is 5/13. If consecutive radial lengths are r_i,r_(i+1), the area equation gives r_i r_(i+1)=26/5. Thus the ten radial lengths alternate between positive u,v, with uv=26/5. The nine outer edges all have squared length $u^2+v^2-2uv(12/13)=(u+v)^2-20$. Put S=u+v, which is also the requested sum. The perimeter equation is $S+9\sqrt{S^2-20}=20$. Squaring with S<20 gives $4S^2+2S-101=0$, whose positive root is $(9\sqrt5-1)/4$. It satisfies the original equation, so the answer is 9+5+1+4=19.

**Answer:** 019.

**Methods:** equal-area products, alternating recurrence, cosine law, perimeter equation.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. Only nine consecutive product equations are given; one source adds an unwarranted closing radial-product equation, though it happens to be consistent with the alternation. The authored proof uses precisely the nine specified triangles.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equal-area fan triangles alternate their radial lengths; equal-area products, alternating recurrence, cosine law, perimeter equation supply the essential reduction.

## 2025 AIME II Problem 13: Track reduction before simplifying a rational recurrence

Define $x_1=25/11$ and $x_{k+1}=(x_k+1/x_k-1)/3$. If x 2025=m/n reduced with positive integers m,n, find (m+n) modulo 1000.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Write x=a/b reduced, with S=a+b divisible by 3; this holds initially. Then neither a nor b is divisible by 3, and the next unreduced fraction is $(a^2-ab+b^2)/(3ab)$. Its numerator is coprime to ab and divisible by 3, so exactly the common factor 3 cancels. The next reduced numerator and denominator are $(a^2-ab+b^2)/3$ and ab, whose sum is S squared/3, again divisible by 3. Thus $S_k=3\cdot12^{2^{k-1}}$. To reduce S 2025 modulo 1000, it is 0 modulo 8. Modulo 125, Euler’s theorem reduces the exponent modulo 100. Since 2 to the 2024 th power is 0 modulo 4 and 16 modulo 25, it is 16 modulo 100. Repeated squaring gives 12 to the 16 th power≡41 modulo 125, so S 2025≡123 modulo 125. The unique residue below 1000 satisfying this and divisibility by 8 is 248.

**Answer:** 248.

**Methods:** fraction reduction invariant, numerator-denominator sum, exponent reduction, Chinese remainder theorem.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. The first leaves its reduction invariant to an assertion about modulus 9; the second omits the cancellation proof. Coprimality plus the invariant 3 divides a+b proves the reduced recurrence directly.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. Track reduction before simplifying a rational recurrence; fraction reduction invariant, numerator-denominator sum, exponent reduction, Chinese remainder theorem supply the essential reduction.

## 2025 AIME II Problem 14: An equilateral triangle inside a right triangle controls area

Right triangle $ABC$ has $\angle A=90^\circ$ and $BC=38$. Interior points $K,L$ satisfy $AK=AL=BK=CL=KL=14$. The area of $BKLC$ is $n\sqrt3$; find $n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Choose A=(0,0),B=(0,2 b),C=(2 a,0). Equal distances place K=(d,b),L=(a,c), with a,b,c,d>0. The length equations are $a^2+b^2=361$, $a^2+c^2=b^2+d^2=196$, and $(a-d)^2+(b-c)^2=196$. Consequently $a^2-d^2=b^2-c^2=165$, so x=a−d,y=b−c are positive. We have x squared+y squared=196 and $a=(x+165/x)/2$, $b=(y+165/y)/2$. Substituting into a squared+b squared=361 gives $1444=196+660+165^2\cdot196/(x^2y^2)$, hence xy=55 $\sqrt{3}$. Triangle AKL is equilateral, so its area is $(ab-cd)/2=49\sqrt3$. The shoelace formula for BKLC rearranges as $(ab-cd)/2+(a-d)(b-c)$, giving 49 $\sqrt{3}$+55 $\sqrt{3}$=104 $\sqrt{3}$. Thus n=104.

**Answer:** 104.

**Methods:** perpendicular bisectors, equilateral area, symmetric elimination, shoelace formula.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All twelve alternatives inspected, including the incomplete entries and linked-diagram note. Many solve for every coordinate or rely on a particular drawing orientation. The positive differences a−d,b−c and their product determine the area directly without choosing either symmetric coordinate solution.

**Archived entries inspected:** 12 of 12. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. An equilateral triangle inside a right triangle controls area; perpendicular bisectors, equilateral area, symmetric elimination, shoelace formula supply the essential reduction.

## 2025 AIME II Problem 15: Two equal minima force a squared quadratic

For positive k define $f(x)=(x-18)(x-72)(x-98)(x-k)/x$ on x>0. Exactly three k give a minimum attained at two distinct positive x values. Find their sum.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Let the common minimum be M, attained at alpha,beta. The monic quartic $P(x)=(x-18)(x-72)(x-98)(x-k)-Mx$ is nonnegative for x>0. Each positive zero has even multiplicity, so $P(x)=(x-\alpha)^2(x-\beta)^2$. Put S=alpha+beta and T=alpha beta. Comparing the cubic, quadratic, and constant coefficients gives $S=94+k/2$, $S^2+2T=10116+188k$, and $T^2=127008k$. Since T>0, put u=$\sqrt{k/8}$>0 to obtain T=1008 u,S=94+4 u squared. Elimination gives $u^4-47u^2+126u-80=(u-1)(u-2)(u-5)(u+8)=0$. Hence the only candidates are k=8,32,200. They all work: their pairs (S,T) are(98,1008),(110,2016),(194,5040), each with S,T>0 and S squared>4 T, so the quadratic has two distinct positive roots. Choosing $M=2ST-127008-10116k$ matches the remaining coefficient and gives the exact identity $f(x)-M=(x^2-Sx+T)^2/x\ge0$. Equality occurs at exactly those two roots. The required sum is 8+32+200=240.

**Answer:** 240.

**Methods:** equal minima, even root multiplicity, coefficient comparison, global square certificate.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. One changes the denominator to x squared and solves a different problem; another states a false general claim about derivative multiplicities. The quartic nonnegativity argument proves necessity, and the explicit square certificates prove sufficiency and exact attainment for all three candidates.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Two equal minima force a squared quadratic; equal minima, even root multiplicity, coefficient comparison, global square certificate supply the essential reduction.

## 2026 AIME I Problem 1: Three staggered starts and a common arrival

Patrick walks from school to a park. Tanya starts one hour later, running 2 mph faster; Jose starts another hour later, cycling 7 mph faster than Tanya. All travel at constant speeds and arrive together. If the distance is $m/n$ miles in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

Let Patrick travel for $T$ hours at $p$ mph. Equal distances give $pT=(p+2)(T-1)=(p+9)(T-2)$. The first equality gives $p=2T-2$; the first and last give $2p=9T-18$. Thus $T=14/5$, $p=18/5$, and the distance is $252/25$. All three travel times are positive and substitution verifies their common distance. The answer is $252+25=277$.

**Answer:** 277.

**Methods:** relative motion, linear systems.

**Verification:** Exact rational substitution gives travel times 14/5, 9/5, 4/5 and speeds 18/5, 28/5, 63/5, each producing distance 252/25.

**Source comparison:** All three alternatives read. Source 0 prints incorrect signs and drops the factor two when clearing its time equations; its stated result is nevertheless correct. The time-variable and catch-up approaches work after restoring omitted display equations.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra. Three equal distances with starts one hour apart reduce to two linear equations for speed and travel time.

## 2026 AIME I Problem 6: A logarithmic quadratic determines a product

Let $P$ be the product of all positive real solutions of $\sqrt[20]{x^{\log_{2026}x}}=26x$. Find the number of positive divisors of $P$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

Set $u=\log_{2026}x$. Taking logarithms gives $u^2-20u-20\log_{2026}26=0$. Its discriminant is positive, so its two real roots correspond bijectively to two positive solutions. Their sum is 20; hence their corresponding $x$ values have product $2026^{20}$. Since $2026=2\cdot1013$ and 1013 is prime (none of the primes through 31 divides it), the divisor count is $(20+1)^2=441$.

**Answer:** 441.

**Methods:** logarithmic substitution, Vieta formulas, divisor count.

**Verification:** The discriminant is strictly positive because log base 2026 of 26 is positive; primality of 1013 checked by trial division through its square root.

**Source comparison:** All six alternatives read. Sources 0, 1, 4, and 5 use a logarithmic quadratic, though several displays are missing. Source 2 is answer guessing rather than a proof. Source 3 inserts an invalid exponent quotient before arriving at the correct quadratic. Taking logarithms directly repairs that step.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. A logarithmic quadratic determines the product by Vieta, after which prime exponents determine its divisor count.

## 2026 AIME I Problem 12: Sphere radii form an affine function

In a plane, $AB=6$, $AC=4$, and $\angle BAC=90^\circ$. Reflect the centroid of $ABC$ across $BC$ to obtain $D$. Spheres of radii $1,2,3,r$ touch the plane at $A,B,C,D$ on the same side. All also touch a second plane on the same side of it. Find numerator plus denominator of $r$ in lowest terms.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Use $A=(0,0)$, $B=(6,0)$, $C=(0,4)$ in the plane $z=0$. Orient a unit normal to the second plane so that its signed distance from every center equals the corresponding radius. Its equation yields $ax+by+(c-1)z+d=0$ for all centers. Since the second plane is distinct, $c\ne1$; thus the radius $z$ is an affine function of its contact point. The first three radii determine $z=1+x/6+y/2$. The centroid is $(2,4/3)$, and reflection across $2x+3y=12$ gives $D=(42/13,124/39)$. Hence $r=1+7/13+62/39=122/39$, giving 161. Existence is verified by the second plane $6x+18y-13z+36=0$: its normal has length 23 and its signed distance from each center equals its radius.

**Answer:** 161.

**Methods:** signed plane distances, affine interpolation, reflection.

**Verification:** Exact reflection gives D=(42/13,124/39); substituting all four centers into the normalized second-plane equation returns their radii.

**Source comparison:** All four alternatives read. Source 0 asserts coplanarity of the centers without explanation, source 1 proves it implicitly through signed distances, source 2 invokes linearity informally, and source 3 uses the intersection line of the tangent planes. The affine equation establishes the common missing justification and the explicit second plane verifies existence.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equal signed distances to two tangent planes make sphere radii affine in their contact points; reflection locates the fourth input.

## 2026 AIME I Problem 13: Binomial residue sums over a finite field

For $0\le r<502$, let $S_r$ sum $\binom{10000}{k}$ over $0\le k\le10000$ congruent to $r$ modulo $502$. How many $S_r$ are divisible by $503$?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Over $\mathbb F_{503}$, put $P(x)=\sum_{r=0}^{501}S_rx^r$. For every nonzero $x$, Fermat gives $P(x)=(1+x)^{10000}=(1+x)^{462}$, since $10000\equiv462\pmod{502}$; the equality also holds at $x=-1$. The difference has degree at most $501$ and $502$ roots, so it is identically zero. Thus $S_r=\binom{462}{r}$ modulo $503$ for $r\le462$, and $S_r=0$ for larger $r$. No binomial coefficient in row $462$ vanishes modulo the larger prime $503$, because all relevant factorials are invertible. Exactly $501-462=39$ sums qualify.

**Answer:** 039.

**Methods:** finite-field interpolation, binomial coefficients.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both sources inspected. The finite-field root argument and quotient-ring interpretation are valid; they must handle x=-1 separately before reducing the exponent. Direct modular coefficient calculation confirms 39 zeros.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, algebra, number_theory. Binomial coefficients grouped by congruence class are analyzed using polynomial identities over a finite field.

## 2026 AIME I Problem 14: Closure controls an equiangular pentagon

An equiangular pentagon has side-length squares summing to 308 and diagonal-length squares summing to 800. Its perimeter squared is $m\sqrt n$, where $m,n$ are positive integers and $n$ is squarefree. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Let $S=\sum a_i^2=308$, $J=\sum a_i a_{i+1}$, $K=\sum a_i a_{i+2}$, with cyclic indices, and put $\phi=(1+\sqrt5)/2$. Since the angle between successive side vectors is $72^\circ$, summing the squared diagonal lengths gives $800=2S+J/\phi$, so $J=184\phi$. The five side vectors sum to zero. Taking the squared norm and grouping adjacent and nonadjacent pairs gives $0=S+J/\phi-\phi K$, because $2\cos72^\circ=1/\phi$ and $2\cos144^\circ=-\phi$. Thus $K=492/\phi$. Therefore the perimeter squared is $S+2J+2K=308+368\phi+984(\phi-1)=676\sqrt5$, giving 681.

**Answer:** 681.

**Methods:** vector closure, golden-ratio angles, cyclic quadratic sums.

**Verification:** Exact arithmetic in Q(√5) verifies J=184φ, K=492/φ and perimeter squared 676√5.

**Source comparison:** All five alternatives read. The extended-side constructions and complex-vector closure lead to the same two equations for adjacent and nonadjacent products. Source 2 guesses the missing rational cancellation from the requested answer form and is not a proof. The closure identity determines it without guessing.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equiangular side-vector closure relates adjacent and nonadjacent products, determining the perimeter from two quadratic sums.

## 2026 AIME II Problem 1: Arithmetic progressions indexed by common divisors

Find the sum of the eleventh terms of all integer arithmetic sequences beginning with 4 and containing both 24 and 34. An alternate archived version asks for the tenth terms instead.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

The common difference $d$ is a positive integer dividing both $24-4=20$ and $34-4=30$. Conversely every positive divisor of their gcd 10 gives such a sequence. Thus $d=1,2,5,10$. The eleventh terms are $4+10d$, and their sum is $4\cdot4+10(1+2+5+10)=196$. For the alternate tenth-term version the same calculation is $4\cdot4+9\cdot18=178$.

**Answer:** 196.

**Methods:** arithmetic sequences, greatest common divisor, divisor sums.

**Verification:** Enumerating the four positive divisors of 10 gives eleventh-term sum 196 and tenth-term sum 178.

**Source comparison:** The sole stored alternative read. It solves the main eleventh-term statement and obtains 196. The clean alternate statement asks for tenth terms and reports 178. These are genuinely different requests, and both are solved explicitly here.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, number_theory. Allowed integer common differences are the positive divisors of the gcd of two term offsets.

## 2026 AIME II Problem 6: Normal distances from a point to a parabola

Find the sum of all radii of circles centered at $(4,39)$ that are tangent to the parabola $2y=x^2-8x+12$ at at least one point.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Parametrize the parabola by $(x,y)=(4+u,u^2/2-2)$. Its squared distance from the given center is $F(u)=u^2+(u^2/2-41)^2=u^4/4-40u^2+1681$. A circle is tangent at this regular point exactly when its radius vector is perpendicular to the tangent vector, equivalently $F^{\prime}(u)=u(u^2-80)=0$. At $u=0$ the radius is 41; at $u=\pm\sqrt{80}$ it is 9. Both are positive and the tangent condition is satisfied, so the requested sum is $41+9=50$.

**Answer:** 050.

**Methods:** normal-line tangency, squared-distance critical points, quartic factorization.

**Verification:** F′ factors as u(u²−80), with F(0)=1681 and F(±√80)=81; these exhaust the stationary distances.

**Source comparison:** All four alternatives read. The normal-slope and derivative methods are valid. A discriminant in y alone misses the vertex tangency unless treated separately. Source 3 estimates a radius and assumes it is an integer because of the contest format; that is not a proof. The parameter derivative lists all tangencies exactly.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Tangency is a stationary-distance condition along the parabola, producing all admissible radii from one factored quartic derivative.

## 2026 AIME II Problem 8: An integer isosceles triangle with a tiny incenter triangle

In an isosceles triangle $ABC$, $AB=BC$ and $I$ is the incenter. The perimeters of $ABC$ and $AIC$ have ratio $125:6$. All side lengths of both triangles are integers. Find the least possible $AB$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Write $AC=2x$, $AB=L$, and $AI=CI=u$. The altitude from $B$ contains $I$, so $\cos A=x/L$ and $\cos(A/2)=x/u$. With $t=u/x>1$, the double-angle formula gives $L/x=t^2/(2-t^2)$, where $t<\sqrt2$. The perimeter ratio becomes $2/((2-t^2)(t+1))=125/6$, or $(t-7/5)(t^2+12t/5+34/25)=0$. The quadratic factor is positive for $t>0$, so $t=7/5$ and $L/x=49$. If $AC=b$ is an integer, then $AI=7b/10$ forces $10\mid b$; also $L=49b/2$. Hence $L\ge245$, attained at side lengths $245,245,10$ and $AI=CI=7$. These lengths satisfy the ratio and the angle identity, verifying attainment.

**Answer:** 245.

**Methods:** half-angle identity, unique positive root, integrality scaling.

**Verification:** The cubic factors exactly as shown; for base 10 the altitude is 100√6, the inradius is 2√6, and AI²=5²+(2√6)²=49. Perimeters 500 and 24 have ratio 125:6.

**Source comparison:** All three alternatives read. Source 0 introduces an integer substitution after normalization without proving it and then guesses the root. Source 1 mislabels the base as BC but contains the intended half-angle reduction. Source 2 finds a working example without proving minimality. The factored cubic proves the unique shape, and divisibility by 10 then proves the minimum.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra, number_theory. A half-angle relation determines a unique isosceles shape, and denominator divisibility gives its smallest integral scale.

## 2026 AIME II Problem 9: A divisor-generating decimal with controlled carries

Let $S=\sum_{k\ge1}1/(10^k-1)$. Find $\lfloor10^{100}S\rfloor$ modulo 1000.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Expand each summand as $\sum_{j\ge1}10^{-kj}$. Since all terms are positive, regrouping gives $S=\sum_{m\ge1}\tau(m)10^{-m}$. After multiplying by $10^{100}$, the terms through $m=100$ are integers. Their last three places contribute $100\tau(98)+10\tau(99)+\tau(100)=600+60+9=669$. It remains to rule out a carry from the infinite tail $T$. Here $\tau(101)=2$, and for $j\ge2$ the divisor-pair bound gives $\tau(100+j)\le2\sqrt{100+j}\le20+j$. Therefore $0<T\le2/10+\sum_{j\ge2}(20+j)10^{-j}=361/810<1$. Thus the tail contributes zero to the floor and the remainder is 669.

**Answer:** 669.

**Methods:** Lambert series, divisor function, rigorous tail bound.

**Verification:** Exact divisor counts are τ(98)=6, τ(99)=6, τ(100)=9; the geometric tail majorant is 361/810<1. Rational truncation with a rigorous remainder bound independently confirms the floor residue 669.

**Source comparison:** Both alternatives read. They correctly identify divisor counts as the uncarried decimal coefficients but dismiss all later carrying solely because 101 is prime. That observation alone is insufficient; the explicit bound on the entire infinite tail completes the proof.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** number_theory, algebra. The repeating-decimal series has divisor-count coefficients, and a rigorous tail bound controls the final carry.

## 2026 AIME II Problem 11: Seven signed square-root sums force a zero sum

Find the greatest integer $n$ such that $x^3-(n/6)x^2+(n-11)x-400$ has roots $\alpha^2,\beta^2,\gamma^2$ and the choices of square roots yield exactly seven distinct values of $\alpha+\beta+\gamma$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

The set of signed sums is closed under negation. A finite such set of odd size must contain zero, so choose signs with $\alpha+\beta+\gamma=0$. Vieta gives $\alpha^2+\beta^2+\gamma^2=n/6$ and $\alpha^2\beta^2+\beta^2\gamma^2+\gamma^2\alpha^2=n-11$. Thus $q=\alpha\beta+\beta\gamma+\gamma\alpha=-n/12$, while $q^2=n-11$ because its cross terms are $2\alpha\beta\gamma(\alpha+\beta+\gamma)=0$. Hence $n^2-144n+1584=0$, giving $n=12$ or 132. To attain 132, choose $\alpha=4$, $\beta=-2+i$, $\gamma=-2-i$. Their squares are the roots of $x^3-22x^2+121x-400$. Their signed sums are exactly $0,\pm8,\pm(-4+2i),\pm(-4-2i)$, seven distinct values. Therefore the greatest integer is 132.

**Answer:** 132.

**Methods:** negation involution, signed sums, Vieta formulas, attainment.

**Verification:** Exact Gaussian-integer expansion verifies roots 16,3−4 i,3+4 i and exactly seven distinct signed sums; the necessary quadratic has only integer roots 12 and 132.

**Source comparison:** Both alternatives read. Source 0 asserts that other sign collisions give too few values without proof; central symmetry supplies a one-line rigorous reason that zero must occur. Source 1 has a sign slip in the coefficient comparison for its auxiliary cubic. Neither explicitly verifies seven distinct sums at the larger candidate; the concrete roots do so.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, combinatorics. The negation involution on seven distinct signed square-root sums forces zero. Vieta then bounds the parameter, and explicit signed-sum enumeration proves attainment.
