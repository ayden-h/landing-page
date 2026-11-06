# AIME Combinatorics Worked Solutions

New exposition after consultation of published solutions. Source review and verification are recorded for each item; an answer-key comparison is not an independent proof check. See the coverage report for limitations.

## 1983 AIME Problem 7: Adjacent knights

Three of 25 labeled seats around a circle are selected uniformly. For the probability that a selected pair is adjacent, find the sum of numerator and denominator in lowest terms.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1983_AIME_Problems/Problem_7) · MAA AMC.

### Solution

For each of the 25 circle edges, count triples containing its endpoints: there are 23. A triple is counted twice exactly when it consists of three consecutive seats; there are 25 such triples. No triple contains three circle edges. Thus the favorable count is $25(23)-25=550$, while the total is $\binom{25}{3}=2300$. The probability is $11/46$, giving $57$.

**Answer:** 057.

**Methods:** inclusion-exclusion, circular adjacency.

**Verification:** Independent exact check passed: Enumerated all 2300 selected seat triples. Result 550. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 8 archived solution entries. Alternatives use complement gaps, circular seating, ordered selections and edge inclusion-exclusion.

**Archived alternatives reviewed:** 8 of 8. Indices in the data are zero-based.

**Status:** solved.

## 1983 AIME Problem 10: One repeated decimal digit

Count four-digit integers beginning with 1 whose digit multiplicities are exactly 2,1,1.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1983_AIME_Problems/Problem_10) · MAA AMC.

### Solution

If 1 is repeated, choose its second position in 3 ways and fill the remaining positions with two different digits other than 1 in $9\cdot8$ ways. If another digit is repeated, choose it in 9 ways, its two positions among the last three in 3 ways, and the remaining digit in 8 ways. The two cases are disjoint and exhaustive, so the count is $3\cdot9\cdot8+9\cdot3\cdot8=432$.

**Answer:** 432.

**Methods:** digits, multiplicity.

**Verification:** Independent exact check passed: Enumerated all 1000 candidate numerals. Result 432. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 4 archived solution entries. Alternatives use digit symmetry and a complement partition by multiplicity pattern.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 1983 AIME Problem 13: Sum of alternating subset sums

For every nonempty subset of 1 through 7, list its elements decreasingly and alternately add and subtract them, starting with plus. Sum these values over all subsets.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1983_AIME_Problems/Problem_13) · MAA AMC.

### Solution

Give the empty set value 0. Pair each subset $U\subseteq\{1,\ldots,6\}$ with $U\cup\{7\}$. Adding 7 at the front reverses every old sign, so the two values sum to 7. There are $2^6$ pairs, hence the required total is $7\cdot2^6=448$. Removing the empty set changes nothing.

**Answer:** 448.

**Methods:** involution, weighted subsets.

**Verification:** Independent exact check passed: Directly summed the 127 nonempty subset values. Result 448. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 5 archived solution entries. Alternatives use maximum-element pairing, a recurrence and cancellation of individual coefficients.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 1984 AIME Problem 10: A score that determines the number correct

A 30-question test scores 30+4c−w, with c correct, w wrong and the rest blank. Find the smallest score above 80 that uniquely determines c.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1984_AIME_Problems/Problem_10) · MAA AMC.

### Solution

If $w\ge4$, replacing $(c,w)$ by $(c-1,w-4)$ preserves the score and is feasible (a score above 80 ensures $c>0$). If at least five questions are blank, $(c+1,w+4)$ is another feasible pair. Uniqueness therefore requires $w\le3$ and $c+w\ge26$. Hence $c\ge23$ and $s\ge30+4(23)-3=119$. For $s=119$, $w=4c-89$ and $0\le w\le30-c$ force $23\le c\le23$, so 119 is achievable and uniquely identifies $c=23$.

**Answer:** 119.

**Methods:** integer feasibility, extremal.

**Verification:** Independent exact check passed: Enumerated all feasible correct/wrong counts. Result 119. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 4 archived solution entries. Alternatives use score intervals and equivalent feasible-answer transformations.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 1984 AIME Problem 11: Separated birches

A row contains three maples, four oaks and five birches, arranged uniformly. Find numerator plus denominator for the probability that no birches are adjacent.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1984_AIME_Problems/Problem_11) · MAA AMC.

### Solution

The set of five birch positions is uniform among the $\binom{12}{5}$ position sets: each set admits the same number of arrangements of the other trees. Arrange the seven non-birches first. Their eight gaps, including both ends, can each hold at most one birch, so $\binom85$ position patterns work. Thus $P=56/792=7/99$, giving $106$.

**Answer:** 106.

**Methods:** gaps, probability.

**Verification:** Independent exact check passed: Enumerated the 792 possible birch-position sets. Result 56. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 5 archived solution entries. Alternatives use deletion of separators, stars and bars, marked-adjacency inclusion-exclusion and labeled species counts.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 1984 AIME Problem 12: Root orbits under two reflections

A real function is unchanged by reflection about 2 and about 7, and vanishes at 0. Find the fewest roots it can have in [−1000,1000].

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1984_AIME_Problems/Problem_12) · MAA AMC.

### Solution

The symmetries are $x\mapsto4-x$ and $x\mapsto14-x$; their compositions translate by 10. Thus every $10k$ and $4+10k$ is forced to be a root. There are respectively 201 and 200 such points in the interval. This lower bound is attained: define $f(x)=0$ on those two residue classes and $f(x)=1$ elsewhere. Both reflections preserve their union and its complement. Hence exactly $401$ roots are possible.

**Answer:** 401.

**Methods:** group orbit, hybrid algebra.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 4 archived solution entries. Valid approaches use the orbit generated by two reflections; attaining the lower bound must also be justified.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 1985 AIME Problem 8: Balanced integer rounding

Round 2.56,2.61,2.65,2.71,2.79,2.82,2.86 to integers with total 19, minimizing the largest absolute error M. Find 100M.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1985_AIME_Problems/Problem_8) · MAA AMC.

### Solution

A choice using only 2 and 3 has all errors below 1, whereas any other integer causes an error above 1. Thus an optimum uses exactly two 2s and five 3s. Among the two entries assigned 2, one is at least 2.61, forcing $M\ge0.61$. Assigning 2 to the first two entries and 3 to all others attains maximum error 0.61. Therefore $100M=61$.

**Answer:** 061.

**Methods:** exchange argument, discrete optimization.

**Verification:** Independent exact check passed: Enumerated all binary rounding assignments using exact hundredths; proof excludes other integers. Result 61. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1985 AIME Problem 10: Values of a floor sum

How many integers from 1 through 1000 occur as floor(2x)+floor(4x)+floor(6x)+floor(8x) for real x?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1985_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Put $t=2x$ and $F(t)=\lfloor t\rfloor+\lfloor2t\rfloor+\lfloor3t\rfloor+\lfloor4t\rfloor$. Then $F(t+1)=F(t)+10$. On $0\le t<1$, the breakpoints are $0,1/4,1/3,1/2,2/3,3/4$ and the values are respectively $0,1,2,4,5,6$. Thus exactly six residue classes modulo 10 are attainable, and each occurs 100 times among 1 through 1000. The answer is $600$.

**Answer:** 600.

**Methods:** floor partition, periodic counting.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 9 archived solution entries. Alternatives enumerate breakpoints, use half-period shifts or express the floor sum through Hermite’s identity.

**Archived alternatives reviewed:** 9 of 9. Indices in the data are zero-based.

**Status:** solved.

## 1985 AIME Problem 12: Random walk on a tetrahedron

A bug starts at one vertex of a unit-edge tetrahedron and repeatedly chooses each incident edge with probability 1/3. Its chance of returning after seven moves is n/729. Find n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1985_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Let $p_j$ be its chance of being at the starting vertex after $j$ moves. From that vertex it must leave; from any other vertex it returns with probability $1/3$. Hence $p_{j+1}=(1-p_j)/3$, $p_0=1$. Subtracting the fixed point $1/4$ gives $p_j=1/4+(3/4)(-1/3)^j$. Consequently $p_7=182/729$, and $n=182$.

**Answer:** 182.

**Methods:** Markov state, recurrence.

**Verification:** Independent exact check passed: Four-vertex integer walk count, independent of the scalar probability recurrence. Result 182/729. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 11 archived solution entries. Alternatives include scalar and four-state recurrences, a roots-of-unity filter, first-return compositions and a modular walk encoding.

**Archived alternatives reviewed:** 11 of 11. Indices in the data are zero-based.

**Status:** solved.

## 1985 AIME Problem 14: Tournament score balance

Every player in a round robin earns half their points against the ten lowest-scoring players; wins score 1 and draws 1/2 each. Determine the total number of players.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1985_AIME_Problems/Problem_14) · MAA AMC.

### Solution

Let $h$ players be outside the bottom ten. Games within the bottom group contribute 45 points, so that group also earns 45 points in cross-group games. The top group earns $\binom h2$ internally and the same amount across groups. Cross-group games contribute $10h$ points in total, giving $45+\binom h2=10h$, or $(h-6)(h-15)=0$. The bottom group averages 9 points and the top group averages $h-1$. Since every top score is at least every bottom score, $h-1\ge9$, excluding $h=6$. Thus the total is $15+10=25$.

**Answer:** 025.

**Methods:** double counting, tournament.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 3 archived solution entries. All alternatives double-count internal and cross-group points; excluding the 16-player candidate needs the score-order constraint.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 1986 AIME Problem 7: Ranking subsets by ternary value

Arrange all positive sums of distinct nonnegative powers of 3 in increasing order. Find the hundredth term.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1986_AIME_Problems/Problem_7) · MAA AMC.

### Solution

These are exactly positive ternary numerals using only 0 and 1. Reading the same digit strings in binary preserves order: the first differing digit dominates all following digits in either base. Thus the hundredth ternary string is the binary representation of 100, namely $1100100$. Its ternary value is $3^6+3^5+3^2=981$.

**Answer:** 981.

**Methods:** order-preserving bijection, subsets.

**Verification:** Independent exact check passed: Enumerated and sorted every nonempty subset of the first eight ternary powers. Result 981. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 5 archived solution entries. Alternatives are binary-to-ternary conversion and recursive blocks of subset sums.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 1986 AIME Problem 10: Recovering a permuted numeral

The five digit permutations of a three-digit numeral other than its original ordering have sum 3194. Recover the original numeral, allowing leading zeros in rearrangements.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1986_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Across all six position permutations, each digit appears twice in every place, so their sum is $222(a+b+c)$. If the original numeral is $N$, then $N+3194=222(a+b+c)$, hence $N\equiv136\pmod{222}$. The three-digit candidates are 136,358,580,802. Substitution of their digit sums into the identity leaves only $358$: $358+3194=222(3+5+8)$.

**Answer:** 358.

**Methods:** digit incidence, hybrid algebra.

**Verification:** Independent exact check passed: Checked every three-digit original numeral, retaining multiplicities of all six position permutations. Result [358]. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 4 archived solution entries. Alternatives supplement digit incidence with congruences modulo 9 and 222.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 1986 AIME Problem 12: A maximum set with distinct subset sums

Choose a subset S of {1,…,15} so that no two disjoint nonempty subsets have equal sums. Maximize the sum of S.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1986_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Any equal subset sums can have their intersection removed, so all subset sums must be distinct. Six selected elements have $1+6+15+20+15=57$ subsets of size at most four, but their sums lie in $0,\ldots,54$; pigeonhole forbids six elements. Four elements sum to at most 54. If five elements sum above 61, they must contain both 14 and 15, since omitting either gives at most $15+13+12+11+10=61$. Their other three elements cannot include consecutive integers: $u+14=(u-1)+15$. To exceed 61 they must then be 13,11,9; omitting 13 gives at most $15+14+12+10+8=59$, while with 13 the greatest nonconsecutive remaining pair is 11,9. But $15+9=13+11$, a contradiction. The set $\{8,11,13,14,15\}$ attains 61. Its pair sums are the ten distinct numbers $19,21,22,23,24,25,26,27,28,29$, separated from its singleton sums; its triple sums are complements of those pair sums and lie in 32 through 42; its four-element sums lie in 46 through 53, and the full sum is 61. Thus all 32 subset sums are distinct.

**Answer:** 061.

**Methods:** pigeonhole, extremal subsets.

**Verification:** Independent exact check passed: Exhaustive subset-sum collision search over subsets of 1,…,15, pruning only provably invalid supersets. Result 61. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 1 archived solution entries. The consulted source gives the same upper-bound strategy but only asserts that the candidate works. The explicit separation of all subset-sum sizes supplies that missing verification.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1986 AIME Problem 13: Prescribed adjacent transitions

Count 15-letter H/T strings with exactly 2 HH, 3 HT, 4 TH and 5 TT adjacent pairs.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1986_AIME_Problems/Problem_13) · MAA AMC.

### Solution

There is one more TH transition than HT, so the string begins with T and ends with H. Collapsing runs leaves THTHTHTH: four T-runs and four H-runs. The five TT pairs are five extra Ts distributed among four nonempty runs, in $\binom83$ ways; the two HH pairs are two extra Hs distributed among four runs, in $\binom53$ ways. These choices uniquely recover the string. The count is $56\cdot10=560$.

**Answer:** 560.

**Methods:** runs, compositions.

**Verification:** Independent exact check passed: Enumerated all 32768 coin words and their 14 adjacent transitions. Result 560. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 2 archived solution entries. Both sources encode the alternating runs and distribute extra letters.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1987 AIME Problem 1: Addition without carrying

Count ordered nonnegative integer pairs (m,n) summing to 1492 with no decimal carry.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1987_AIME_Problems/Problem_1) · MAA AMC.

### Solution

For a target digit $d$, choose the corresponding digit of $m$ from 0 through $d$; the digit of $n$ is then forced. Leading zeros are allowed and the four positions are independent. Hence the count is $(1+1)(4+1)(9+1)(2+1)=300$.

**Answer:** 300.

**Methods:** digit product rule.

**Verification:** Independent exact check passed: Enumerated all nonnegative summand pairs. Result 300. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1987 AIME Problem 7: LCM triples

Count positive ordered triples (a,b,c) with lcm(a,b)=1000 and lcm(a,c)=lcm(b,c)=2000.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1987_AIME_Problems/Problem_7) · MAA AMC.

### Solution

Only primes 2 and 5 can occur. For the 2-exponents $(u,v,w)$, the conditions are $\max(u,v)=3$ and $\max(u,w)=\max(v,w)=4$. Thus $w=4$ and $(u,v)\in\{0,1,2,3\}^2$ has maximum 3, giving $4^2-3^2=7$ choices. For the 5-exponents, every pair has maximum 3, so at least two exponents are 3. There are $1+3\cdot3=10$ choices. Independent prime-exponent choices give $7\cdot10=70$.

**Answer:** 070.

**Methods:** prime exponent product, hybrid number theory.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 2 archived solution entries. Alternatives count prime exponents independently or split on the exponent pattern of c.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1987 AIME Problem 13: One bubble pass

A random ordering of 40 distinct numbers undergoes one left-to-right bubble-sort pass. Find numerator plus denominator for the chance that the original twentieth number finishes thirtieth.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1987_AIME_Problems/Problem_13) · MAA AMC.

### Solution

The number must be larger than the preceding 19 numbers, or their maximum swaps it left at its first comparison. It must then exceed positions 21 through 30 to move to position 30, and be smaller than position 31 to stop there. Equivalently, among the first 31 entries, position 31 contains the maximum and position 20 the second maximum. Their ordered locations are uniform among $31\cdot30$ possibilities, so the chance is $1/930$ and the answer is $931$.

**Answer:** 931.

**Methods:** relative rank, algorithm invariant.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1988 AIME Problem 1: More lock combinations

A ten-button lock originally accepts any five-element button set as a possible code. If codes of every size 1 through 9 become available, how many additional codes exist?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_1) · MAA AMC.

### Solution

There are $2^{10}-2$ nonempty proper subsets of the button set. Subtract the $\binom{10}{5}=252$ old codes. The increase is $1024-2-252=770$.

**Answer:** 770.

**Methods:** subsets, complement.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1988 AIME Problem 5: Divisor probability

A divisor of 10^99 is chosen uniformly. Find numerator plus denominator for its probability of being divisible by 10^88.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_5) · MAA AMC.

### Solution

Write the divisor as $2^a5^b$ with $0\le a,b\le99$. All 10000 exponent pairs correspond to distinct divisors. Divisibility by $10^{88}$ requires both exponents at least 88, giving $12^2=144$ pairs. Thus the chance is $9/625$, giving $634$.

**Answer:** 634.

**Methods:** exponent lattice, probability.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1988 AIME Problem 10: Interior diagonals of a polyhedron

A convex polyhedron has 12 square, 8 regular hexagonal and 6 regular octagonal faces, one of each at every vertex. Count vertex-pair segments lying in its interior.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Counting square corners gives $V=12\cdot4=48$. Three edges meet at every vertex, hence $E=3V/2=72$. A k-gon has $k(k-3)/2$ diagonals, so face diagonals total $12\cdot2+8\cdot9+6\cdot20=216$. In a convex polyhedron, every vertex-pair segment is an edge, a face diagonal, or an interior diagonal; a face diagonal belongs to only one face. Therefore the answer is $\binom{48}{2}-72-216=840$.

**Answer:** 840.

**Methods:** incidence, combinatorial geometry.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 5 archived solution entries. Alternatives count face incidences, permissible endpoints, face diagonals or use Euler’s formula.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 1988 AIME Problem 15: Stack output after lunch

Letters 1 through 9 arrive in order at a last-in-first-out inbox. At lunch, letter 8 has already been typed. Count distinct possible sequences of letters typed afterward, including the empty sequence.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_15) · MAA AMC.

### Solution

Any subset $U$ of letters 1 through 7 can remain in the stack when 8 is removed: pop each unwanted letter immediately on its arrival and retain wanted letters. If $|U|=k$, their later output order is forced to be decreasing. Letter 9 is either already typed, giving one sequence, or still to be typed and can be inserted in any of the $k+1$ places in this decreasing sequence by choosing its arrival time. These outputs are all distinct and exhaust the possibilities. Thus the count is $\sum_{k=0}^7\binom7k(k+2)=7\cdot2^6+2\cdot2^7=704$.

**Answer:** 704.

**Methods:** stack, weighted subsets.

**Verification:** Independent exact check passed: Enumerated all legal stack output histories and every lunch cut after the output of 8; deduplicated suffixes. Result 704. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 3 archived solution entries. Alternatives count stack subsets and insertion positions or split by the letter immediately before 9; histories must be deduplicated.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 1989 AIME Problem 2: Polygons from circle points

Ten points lie on a circle. Count convex polygons with at least three vertices selected from those points.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1989_AIME_Problems/Problem_2) · MAA AMC.

### Solution

Every subset of at least three points gives exactly one convex polygon, by taking its points in circular order. Remove subsets of sizes 0,1,2 from all subsets: $2^{10}-1-10-\binom{10}{2}=968$.

**Answer:** 968.

**Methods:** bijection, subsets.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1989 AIME Problem 5: Recovering a biased coin

For five independent flips of a fixed biased coin, the positive probabilities of exactly one and exactly two heads agree. Find numerator plus denominator for the probability of exactly three heads.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1989_AIME_Problems/Problem_5) · MAA AMC.

### Solution

Let the head probability be $p$, with $0<p<1$. Equality gives $5p(1-p)^4=10p^2(1-p)^3$. Cancelling positive factors yields $1-p=2p$, so $p=1/3$. The desired probability is $\binom53(1/3)^3(2/3)^2=40/243$, giving $283$.

**Answer:** 283.

**Methods:** binomial probability.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 2 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1989 AIME Problem 11: Largest mode-minus-mean

A sample of 121 integers in [1,1000] has one unique most frequent value. Maximize the integer part of that value minus the sample mean.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1989_AIME_Problems/Problem_11) · MAA AMC.

### Solution

Let the mode be $u$ and occur $k\ge2$ times. The other $121-k$ entries have multiplicity at most $k-1$. Their sum is minimized, even if we temporarily ignore whether u is excluded, by filling 1,2,3,… to that capacity. Also $u\le1000$. Thus $121D\le(121-k)1000-S_k$, where $S_k$ is that minimal sum. For $k=2,3,4,5,6$, respectively, $S_k=7140,3540,2340,1740,1380$. The corresponding upper numerators are $111860,114460,114660,114260,113620$; the largest is $114660$, with quotient $947+73/121$. For $k\ge7$, already $D<114000/121<948$. Finally four 1000s and three copies of each integer 1 through 39 form 121 entries and attain $D=114660/121$. The requested maximum is $947$.

**Answer:** 947.

**Methods:** capacity bound, extremal multiset.

**Verification:** Independent exact check passed: Exact capacity-minimal sums for every possible mode multiplicity 2,…,121. Result 947. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 2 archived solution entries. Both archived entries need stronger optimization justification; the replacement proof checks all frequency ranges exactly.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1989 AIME Problem 13: Avoiding differences four and seven

Find the maximum size of a subset of {1,…,1989} with no pair differing by 4 or 7.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1989_AIME_Problems/Problem_13) · MAA AMC.

### Solution

In each consecutive block of 11 integers, the forbidden-difference graph contains an 11-cycle: relative labels $1,5,9,2,6,10,3,7,11,4,8,1$. An independent set in an odd cycle has at most 5 vertices, since every selected vertex requires an unselected successor. Split 1989 into 180 such blocks and a final block of 9. In the last block, four disjoint pairs $(1,5),(2,6),(3,7),(4,8)$ allow at most five selected numbers. Hence the bound is $180\cdot5+5=905$. Select residues $1,3,4,6,9$ modulo 11. Their nonzero differences modulo 11 are never 4 or 7, so the construction is valid and includes five in the final block. Thus the bound is attained.

**Answer:** 905.

**Methods:** independent set, periodic construction.

**Verification:** Independent exact check passed: Exact seven-bit transfer dynamic program for all 1989 positions, forbidding separations 4 and 7. Result 905. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 1 archived solution entries. The consulted source omits a rigorous upper bound for its exceptional end block. The cycle-and-matching argument closes that gap.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1990 AIME Problem 1: Ranking nonsquares and noncubes

List positive integers that are neither perfect squares nor perfect cubes. Find the five-hundredth.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1990_AIME_Problems/Problem_1) · MAA AMC.

### Solution

Up to $N$, inclusion-exclusion gives $N-\lfloor\sqrt N\rfloor-\lfloor\sqrt[3]N\rfloor+\lfloor\sqrt[6]N\rfloor$ admissible numbers. At $N=528$ this is $528-22-8+2=500$, while at 527 it is 499. Therefore the five-hundredth term is $528$.

**Answer:** 528.

**Methods:** inclusion-exclusion, rank inversion.

**Verification:** Independent exact check passed: Direct filtering of all integers through 599. Result 528. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 2 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1990 AIME Problem 6: Tagged fish population estimate

Of 60 fish tagged in May, 25% are assumed gone by September. A representative September sample of 70 contains three tagged fish; 40% of September fish are new. Estimate the May population.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1990_AIME_Problems/Problem_6) · MAA AMC.

### Solution

The assumed number of surviving tagged fish is $60(3/4)=45$. Their September fraction is $3/70$, giving September population $45/(3/70)=1050$. Of these, $60\%$ or 630 survived from May. This is $75\%$ of the May population, so the estimate is $630/(3/4)=840$. This is the model-based estimate specified by the assumptions, not an exact statistical inference from one random sample.

**Answer:** 840.

**Methods:** sampling model, probability.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 2 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1990 AIME Problem 8: Interleaving three target stacks

Targets occupy three labeled vertical columns of sizes 3,3,2. Each shot must hit the lowest remaining target of its chosen column. Count complete shooting orders.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1990_AIME_Problems/Problem_8) · MAA AMC.

### Solution

A complete order is uniquely encoded by its sequence of column labels: the chosen label determines the lowest remaining target. Choose positions for the three shots in the first column, then the three in the second; the rest belong to the third. The count is $\binom83\binom53=8!/(3!3!2!)=560$.

**Answer:** 560.

**Methods:** interleavings, multinomial.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1990 AIME Problem 9: No consecutive heads

Toss a fair coin ten times. Find numerator plus denominator for the probability of no adjacent heads.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1990_AIME_Problems/Problem_9) · MAA AMC.

### Solution

Let $a_n$ count legal n-toss words. A legal word ends either in T after any legal length-$n-1$ word, or in TH after any legal length-$n-2$ word. Thus $a_n=a_{n-1}+a_{n-2}$ with $a_0=1,a_1=2$. The values through $a_{10}$ are $1,2,3,5,8,13,21,34,55,89,144$. Therefore $P=144/1024=9/64$, giving $73$.

**Answer:** 073.

**Methods:** finite state, Fibonacci.

**Verification:** Independent exact check passed: Enumerated all 1024 toss sequences. Result 144. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 3 archived solution entries. Alternatives are the Fibonacci recurrence and a head-count gap sum.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 1990 AIME Problem 10: Products of two root-of-unity groups

Let $A=\{z:z^{18}=1\}$ and $B=\{w:w^{48}=1\}$. How many distinct complex numbers occur as $zw$ with $z\in A$ and $w\in B$?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1990_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Let $\zeta=e^{2\pi i/144}$. Every product has the form $\zeta^{8a+3b}$, so it is among the $144$ powers of $\zeta$. Conversely, fix any integer $k$. Choose $a\in\{0,1,2\}$ with $8a\equiv k\pmod3$, and set $b=(k-8a)/3$. Then $\zeta^{8a}$ is an eighteenth root and $\zeta^{3b}$ is a forty-eighth root, and their product is $\zeta^k$. Thus all $144$ distinct powers occur.

**Answer:** 144.

**Methods:** roots of unity, finite cyclic groups, image counting, least common multiple.

**Verification:** The multiplication map has 18·48 inputs and kernel {(u,u⁻¹):u⁶=1} of size 6, independently giving 864/6=144 products. Independent exact check passed: Enumerate all864 root-product exponents, independently checking the image size.

**Source comparison:** All three alternatives read. The first uses a Frobenius-number argument that needs explicit reduction of exponent ranges. The second comment incorrectly claims every integer 0 through 143 is literally representable with nonnegative bounded exponents; modular representability is sufficient. The third uses synchronized exponents, which does generate all 144 values but needs an order calculation.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 1990 AIME Problem 12: Sum of dodecagon chords

For a regular 12-gon of circumradius 12, write the sum of all side and diagonal lengths as a+b√2+c√3+d√6. Find a+b+c+d.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1990_AIME_Problems/Problem_12) · MAA AMC.

### Solution

For circular separation $j=1,\ldots,5$, there are 12 chords of length $24\sin(15j^\circ)$; there are six diameters of length 24. The five shorter lengths are $6(\sqrt6-\sqrt2),12,12\sqrt2,12\sqrt3,6(\sqrt6+\sqrt2)$. Thus the total is $288+144\sqrt2+144\sqrt3+144\sqrt6$, whose coefficient sum is $720$. The diameter class has six rather than twelve members because the two directions reach the same endpoint.

**Answer:** 720.

**Methods:** orbit size, chord counting.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 4 archived solution entries. Alternatives evaluate the same six chord classes using trigonometry, cosine law or complex coordinates.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 1990 AIME Problem 13: Leading nines in powers

Among 9^0,…,9^4000, count those beginning with decimal digit 9, given that 9^4000 has 3817 digits and begins with 9.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1990_AIME_Problems/Problem_13) · MAA AMC.

### Solution

Write $d_k$ for the digit length of $9^k$. Multiplication by 9 increases length by either 0 or 1. For $k\ge1$, $d_k=d_{k-1}$ precisely when $9^k$ begins with 9: the two inequalities become $9\cdot10^{d_k-1}\le9^k<10^{d_k}$. Among 4000 transitions, exactly $3817-1=3816$ increase the digit length, and the other 184 preserve it. Since $9^0=1$ does not begin with 9, the answer is $184$.

**Answer:** 184.

**Methods:** telescoping, leading digits.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 3 archived solution entries. Alternatives group powers by digit length or count length-preserving multiplication steps.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 1991 AIME Problem 3: The peak of a weighted binomial row

For $0\le k\le1000$, let $A_k=\binom{1000}{k}(0.2)^k$. Find the index $k$ for which $A_k$ is largest.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_3) · MAA AMC.

### Solution

For $0\le k<1000$, $A_{k+1}/A_k=(1000-k)/(5(k+1))$. This ratio exceeds 1 exactly when $k<995/6$, and is less than 1 exactly when $k>995/6$. Thus the sequence strictly increases through $A_{166}$ and strictly decreases afterward. Its unique maximum is at $k=166$.

**Answer:** 166.

**Methods:** binomial coefficients, successive ratios, unimodality.

**Verification:** A₁₆₆/A₁₆₅=835/830>1, while A₁₆₇/A₁₆₆=834/835<1. Independent exact check passed: Compare all1001 weighted binomial terms after multiplying by the common denominator5^1000.

**Source comparison:** All five alternatives read. Index 0 contains a false factorial simplification and its general maximum formula needs a two-mode caveat when the threshold is integral. Indices 1 and 4 confuse the threshold index in prose. The exact neighboring ratio establishes both monotonicity and uniqueness.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 1991 AIME Problem 5: Coprime factor allocations

How many reduced fractions strictly between 0 and 1 have numerator times denominator equal to 20!?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_5) · MAA AMC.

### Solution

The eight distinct primes dividing $20!$ are $2,3,5,7,11,13,17,19$. Coprimality requires each prime power in $20!$ to be placed wholly in the numerator or wholly in the denominator, giving $2^8$ ordered allocations. Swapping numerator and denominator pairs them, with no fixed point because the coprime factors cannot be equal. Exactly half have numerator smaller, so the count is $128$.

**Answer:** 128.

**Methods:** prime allocation, involution.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1991 AIME Problem 10: Lexicographic transmission errors

Send aaa and bbb through independent channels that flip each letter with probability 1/3. The first received word precedes the second with probability p. Find the numerator of p in lowest terms.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_10) · MAA AMC.

### Solution

At one position the letters agree with probability $2(2/3)(1/3)=4/9$, while the first is a and the second b with probability $(2/3)^2=4/9$. Lexicographic order is decided by the first differing position. Hence $p=4/9+(4/9)^2+(4/9)^3=(324+144+64)/729=532/729$. The numerator is $532$; it is coprime to 729 because it is not divisible by 3.

**Answer:** 532.

**Methods:** first difference, probability.

**Verification:** Independent exact check passed: Summed exact probabilities over all 64 pairs of received strings. Result 532/729. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 4 archived solution entries. Alternatives use an eight-string table or condition on the first differing letter.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 1991 AIME Problem 13: Sock counts from a probability

At most 1991 socks, red or blue, are in a drawer. Two drawn without replacement have the same color with probability 1/2. Maximize the number of red socks.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_13) · MAA AMC.

### Solution

Write $N=r+b$. The equation $\binom r2+\binom b2=\tfrac12\binom N2$ simplifies to $(r-b)^2=N$. Therefore $N=t^2$ and the larger color class has $(t^2+t)/2$ socks. Since $t^2\le1991$, $t\le44$. Choosing $t=44$, red $r=44\cdot45/2=990$ and blue $946$ satisfies the equation and the size bound. The maximum is $990$.

**Answer:** 990.

**Methods:** sampling without replacement, Diophantine probability.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 6 archived solution entries. All six forms reduce to the square identity (r−b)²=r+b, with different algebraic parametrizations.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 1992 AIME Problem 1: Pairing reduced fractions around five

Find the sum of all positive rational numbers less than $10$ whose reduced denominator is $30$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_1) · MAA AMC.

### Solution

These numbers are $k/30$ with $1\le k<300$ and $\gcd(k,30)=1$. In every block of thirty integers the allowed residues are $1,7,11,13,17,19,23,29$, so there are $80$ fractions. The map $k\mapsto300-k$ pairs them without a fixed point, and each pair of fractions sums to $10$. Their total is therefore $40\cdot10=400$.

**Answer:** 400.

**Methods:** totient function, involution, reduced fractions, residue classes.

**Verification:** The eight allowed residues avoid divisibility by 2,3,5, and complementing a numerator preserves coprimality to 30. Independent exact check passed: Direct exact sum over all reduced numerators.

**Source comparison:** All three alternatives read. The first two correctly count eight reduced residues per unit interval. Index 2 uses φ(300)=80; this happens to apply because 30 and 300 have the same prime divisors, a fact that should be made explicit rather than treated as automatic.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 1992 AIME Problem 2: Strictly increasing digits

Count positive decimal integers of at least two digits whose digits strictly increase from left to right.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_2) · MAA AMC.

### Solution

Zero cannot occur, because it would have to be the leading digit. Any subset of $\{1,\ldots,9\}$ of size at least two determines one increasing numeral. Thus the count is $2^9-1-9=502$.

**Answer:** 502.

**Methods:** subset bijection, digits.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 2 archived solution entries. The second entry proves the same binomial count through the hockey-stick identity.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1992 AIME Problem 4: Three consecutive binomial coefficients in a ratio

Rows of Pascal's triangle are numbered from row $0$, containing only $1$. In which row do three consecutive entries occur in the ratio $3:4:5$?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_4) · MAA AMC.

### Solution

Write the entries as $\binom n{k-1},\binom nk,\binom n{k+1}$. Neighboring ratios give $k/(n-k+1)=3/4$ and $(n-k)/(k+1)=5/4$. Hence $4k=3(n-k+1)$ and $4(n-k)=5(k+1)$. Solving gives $k=27,n=62$. These indices lie inside row $62$, and the two ratios verify the required triple.

**Answer:** 062.

**Methods:** Pascal triangle, binomial ratios, linear systems.

**Verification:** At n=62,k=27, k/(n−k+1)=27/36=3/4 and (n−k)/(k+1)=35/28=5/4. Independent exact check passed: Compare exact adjacent binomial integers in the first101 rows.

**Source comparison:** Both alternatives correctly reduce adjacent-binomial ratios to linear equations. No large binomial coefficients need to be evaluated.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1992 AIME Problem 5: Numerators of repeating decimals

For all numbers 0.abcabc… strictly between 0 and 1, count distinct numerators after reducing the fraction.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_5) · MAA AMC.

### Solution

Every fraction is $u/999$ with $1\le u\le998$, and $999=3^3\cdot37$. A reduced numerator n occurs exactly when some divisor d of 999 satisfies $n<d$ and $\gcd(n,d)=1$. If n is divisible by neither 3 nor 37, take d=999; there are $\varphi(999)=648$ such n. If 3 divides n but 37 does not, a coprime denominator must divide 37, so precisely $n=3,6,\ldots,36$ work, adding 12. If 37 divides n, any coprime denominator is at most 27, smaller than n, so none work. The total is $660$.

**Answer:** 660.

**Methods:** distinct image, inclusion-exclusion.

**Verification:** Independent exact check passed: Reduced every numerator 1,…,998 over 999 and deduplicated. Result 660. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 1 archived solution entries. The consulted source counts reductions of multiples of 81. Characterizing possible reduced denominators makes exhaustiveness explicit.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1992 AIME Problem 6: Consecutive integers without carries

Count consecutive pairs whose members are both in [1000,2000] and whose decimal addition produces no carry.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_6) · MAA AMC.

### Solution

Write the smaller member as 1ABC. If it has no trailing 9, all three digits A,B,C must be 0 through 4, giving $5^3$. If it has exactly one trailing 9, A and B must be 0 through 4, giving $5^2$. With exactly two trailing 9s, A has five choices. The remaining pair 1999,2000 also works. These disjoint cases give $125+25+5+1=156$.

**Answer:** 156.

**Methods:** carry states, digits.

**Verification:** Independent exact check passed: Direct decimal-digit carry test on all 1000 consecutive pairs. Result 156. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 3 archived solution entries. The reliable partition is by the number of trailing nines of the smaller integer.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 1992 AIME Problem 12: Chomp positions

On a 5-by-7 board, a move removes one cell and all cells above and to its right. Count all possible remaining cell sets, including the full and empty boards.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Remaining cells form a lower-left order ideal: if a cell remains, all cells below and left of it remain. Conversely any such ideal can be realized by removing the upper-right quadrants based at the minimal excluded cells. The boundary between kept and removed cells is a monotone path across the enclosing rectangle with five vertical and seven horizontal steps, and this correspondence is bijective. Hence the count is $\binom{12}{5}=792$.

**Answer:** 792.

**Methods:** order ideal, lattice path.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 2 archived solution entries. The alternatives identify monotone boundaries or nondecreasing row lengths.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1992 AIME Problem 15: Missing factorial trailing-zero counts

A positive integer is attainable if it is the exact number of trailing zeros of some factorial. How many positive integers below 1992 are unattainable?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_15) · MAA AMC.

### Solution

Let $z(m)=\sum_{j\ge1}\lfloor m/5^j\rfloor$. It is constant on each block $5k,\ldots,5k+4$, and increases strictly between blocks. At $m=7975$, $z(m)=1595+319+63+12+2=1991$, while $z(7980)=1596+319+63+12+2=1992$. Therefore exactly the 1595 positive block values for $k=1,\ldots,1595$ occur below 1992. Of the 1991 positive target integers, $1991-1595=396$ are missing.

**Answer:** 396.

**Methods:** monotone image, valuation counting.

**Verification:** Independent exact check passed: Enumerated all distinct trailing-zero counts until the first value 1992. Result 396. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 2 archived solution entries. The second method counts skipped values at higher powers of five.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1993 AIME Problem 1: Even numbers with distinct digits

Count even integers strictly between 4000 and 7000 whose four digits are distinct.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_1) · MAA AMC.

### Solution

The thousands digit is 4,5 or 6. If it is 4 or 6, the units digit has four even choices; if it is 5, the units digit has five. Once those digits are fixed, the middle positions have 8 and 7 choices. Thus $(2\cdot4+5)8\cdot7=728$. The endpoints have repeated digits and do not affect the count.

**Answer:** 728.

**Methods:** digits, casework.

**Verification:** Independent exact check passed: Enumerated every integer strictly between the endpoints. Result 728. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 2 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1993 AIME Problem 4: Equal outer and inner sums

Count integer quadruples 0<a<b<c<d<500 satisfying a+d=b+c and bc−ad=93.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_4) · MAA AMC.

### Solution

Set $u=b-a=d-c>0$ and $v=c-b>0$. Then $(a,b,c,d)=(a,a+u,a+u+v,a+2u+v)$ and $bc-ad=u(u+v)=93$. Thus $(u,u+v)$ is either $(1,93)$ or $(3,31)$; the reversed factor pairs violate $v>0$. The spans d−a are respectively 94 and 34, allowing $499-94=405$ and $499-34=465$ positive starting values a. The total is $870$.

**Answer:** 870.

**Methods:** gap parametrization, hybrid number theory.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 6 archived solution entries. Alternatives factor a translation-invariant product using gaps, a shifted origin or centered coordinates.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 1993 AIME Problem 7: Fitting one random brick into another

Choose six distinct values uniformly from 1 through 1000, three for brick dimensions and three for box dimensions. Find numerator plus denominator for the probability that the brick fits with parallel sides after rotation.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_7) · MAA AMC.

### Solution

Sort both triples. A fitting assignment exists exactly when the ith smallest brick dimension is below the ith smallest box dimension: necessity follows by counting available larger box dimensions, and sorted matching proves sufficiency. In the sorted list of all six values, write A for brick and B for box. The condition says every prefix has at least as many As as Bs. Of the $\binom63=20$ equally likely label words, reflection counts $\binom63-\binom62=5$ good ones. Hence $p=1/4$ and the requested sum is $5$.

**Answer:** 005.

**Methods:** ballot path, relative order.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 4 archived solution entries. Alternatives list rank words or use Catalan numbers and the hook-length formula.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 1993 AIME Problem 8: Unordered covering subset pairs

For a six-element set S, count unordered pairs of subsets, allowing equality, whose union is S.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_8) · MAA AMC.

### Solution

For an ordered pair, each element belongs only to the first subset, only to the second, or to both, giving $3^6$ pairs. Swapping the two subsets fixes just $(S,S)$; every other pair has two orderings. Therefore the unordered count is $(3^6-1)/2+1=365$.

**Answer:** 365.

**Methods:** Burnside, nonuniform fibers.

**Verification:** Independent exact check passed: Enumerated every unordered pair of six-bit subsets. Result 365. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 7 archived solution entries. Alternatives use element states, a recurrence, overlap size or subset-size partitions; the identical pair is exceptional.

**Archived alternatives reviewed:** 7 of 7. Indices in the data are zero-based.

**Status:** solved.

## 1993 AIME Problem 10: Uniform vertex face incidences

A convex polyhedron has 32 triangular or pentagonal faces. At each vertex, T triangles and P pentagons meet. Determine 100P+10T+V.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Let t,p be the face counts. Incidence counting gives $3t=TV$, $5p=PV$, so $V(5T+3P)=15(t+p)=480$. Every vertex has degree $T+P$, hence Euler gives $V(T+P-2)=60$. Eliminating V yields $5T+3P=8(T+P-2)$, or $3T+5P=16$. Its only nonnegative integer solution is $T=P=2$. Therefore $V=60/(4-2)=30$, and the answer is $200+20+30=250$.

**Answer:** 250.

**Methods:** Euler formula, double counting.

**Verification:** Independent exact check passed: Exhausted the integer incidence equations; no regular-face assumption. Result [(30, 2, 2)]. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 4 archived solution entries. The incidence-based alternative is sound and avoids unwarranted regularity or visual uniqueness assumptions.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 1993 AIME Problem 11: Loser starts the next game

Two players alternate fair coin flips until the first head wins. The loser starts the next game. Alfred starts game one. If his probability of winning game six is m/n in lowest terms, find the last three digits of m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_11) · MAA AMC.

### Solution

A game starter wins with probability $1/2+1/8+\cdots=2/3$. Let p_j be Alfred’s win probability in game j. If he just won he starts second next time; otherwise he starts first. Thus $p_{j+1}=p_j/3+2(1-p_j)/3=(2-p_j)/3$, with $p_1=2/3$. The successive values are $2/3,4/9,14/27,40/81,122/243,364/729$. This last fraction is reduced, and $364+729=1093$, giving $093$.

**Answer:** 093.

**Methods:** Markov recurrence, conditioning.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 4 archived solution entries. Alternatives use state recurrences or count an odd number of switches of the starting player.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 1993 AIME Problem 12: Undoing random midpoint choices

Inside the triangle with vertices (0,0),(0,420),(560,0), a point undergoes six midpoint moves toward arbitrarily selected vertices and ends at (14,92). Determine the sum of its starting coordinates.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Undoing the affine recurrence gives $x_1=64(14)-560J$ and $y_1=64(92)-420K$, where J and K are integers encoding choices of the two nonzero vertices. Because the start is interior, $0<x_1<560$ and $0<y_1<420$. These inequalities force $J=1,K=14$, so $(x_1,y_1)=(336,8)$. The two binary encodings 1 and 14 have disjoint 1-bits, so they correspond to valid vertex choices; the remaining bits correspond to the origin. Also $336/560+8/420<1$, confirming the start is interior. The coordinate sum is $344$.

**Answer:** 344.

**Methods:** binary coding, affine state.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 2 archived solution entries. Both sources reverse the affine midpoint process, either stepwise or through binary weights.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1994 AIME Problem 5: A weighted sum over digit strings

For each positive integer n, multiply its nonzero decimal digits. Let S be the sum of these products for n=1,…,999. Find the largest prime divisor of S.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_5) · MAA AMC.

### Solution

Use three-digit strings with leading zeros, assigning weight 1 to a zero and its usual value to every other digit. Independence of the three positions gives total weight $(1+1+2+\cdots+9)^3=46^3$ over 000 through 999. Remove the artificial all-zero string, of weight 1. Thus $S=46^3-1=45\cdot2163=3^3\cdot5\cdot7\cdot103$, and the largest prime factor is $103$.

**Answer:** 103.

**Methods:** weighted product rule, digits.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 2 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1994 AIME Problem 6: Small triangles in three line families

For every integer k from −10 to 10, draw y=k, y=√3x+2k and y=−√3x+2k. Count equilateral triangles of side 2/√3 whose edges lie on the lines.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_6) · MAA AMC.

### Solution

Choose line indices a,b,c in the horizontal, positive-slope and negative-slope families. The sloped lines meet at height b+c, so the triangle’s altitude is $|a-b-c|$ and its side is $2|a-b-c|/\sqrt3$. Thus count triples with $a-b-c=\pm1$. For a fixed sum $s=b+c$, there are $21-|s|$ pairs when $|s|\le20$. The +1 case requires $-11\le s\le9$ and contributes $21^2-(66+45)=330$. Symmetry gives 330 for −1. Each triangle has a unique three-line description, so the answer is $660$.

**Answer:** 660.

**Methods:** lattice counting, combinatorial geometry.

**Verification:** Independent exact check passed: Enumerated all 21³ triples of line indices with unit altitude. Result 660. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 3 archived solution entries. Alternatives use hexagon area, missing horizontal lines or an enclosing triangle.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 1994 AIME Problem 7: Lines with only integral circle intersections

Count real pairs (a,b) for which ax+by=1 and x²+y²=50 have at least one common point and every common point has integral coordinates.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_7) · MAA AMC.

### Solution

The circle’s integral points are $(\pm1,\pm7),(\pm7,\pm1),(\pm5,\pm5)$, twelve in all. A qualifying line is either tangent at one of these twelve points or a secant through two of them. There are $\binom{12}{2}$ secants, but the six antipodal pairs give lines through the origin, which cannot have equation $ax+by=1$. All other secants and all tangents have unique normalized equations of that form. Hence the answer is $66-6+12=72$.

**Answer:** 072.

**Methods:** geometric pairs, exceptional fibers.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The finite lattice-point model determines all tangent and secant possibilities; antipodal pairs require a separate exclusion.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1994 AIME Problem 9: Matched tiles without three open pairs

Six labeled pairs of tiles are drawn uniformly without replacement. A pair is discarded as soon as matched. The process loses if three unmatched tiles are ever held. Find numerator plus denominator for the probability of emptying the bag.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_9) · MAA AMC.

### Solution

Let $P_k$ be success probability starting with $k$ pairs and an empty hand. Drawing one arbitrary tile changes no success probability, by symmetry. For $k\ge2$, either the second tile matches the first (probability $1/(2k-1)$), or it does not and the third must match one of those two (probability $[(2k-2)/(2k-1)] [2/(2k-2)]$). After removal of that first completed pair, the state is $k-1$ pairs, with zero or one arbitrary first tile already exposed, so its success probability is $P_{k-1}$. Therefore $P_k=3P_{k-1}/(2k-1)$, $P_1=1$. Hence $P_6=3^5/(3\cdot5\cdot7\cdot9\cdot11)=9/385$, giving $394$.

**Answer:** 394.

**Methods:** renewal, state compression.

**Verification:** Independent exact check passed: Independent exact dynamic program by unopened pairs and held unmatched tiles. Result 9/385. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 2 archived solution entries. Both sources condition on completing the first pair and use the same reduced-state equivalence.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1994 AIME Problem 11: Distinct heights of a brick tower

Build a tower of 94 bricks, each contributing height 4,10 or 19. Count distinct possible total heights.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_11) · MAA AMC.

### Solution

Subtract the base height $94\cdot4$ and divide by 3. The offset is $t=2a+5b$, where $a,b\ge0$ and $a+b\le94$. Whenever $a\ge5$, replace five height-2 contributions by two height-5 contributions and three zero contributions; this preserves both height and the 94-brick total. Repetition gives a canonical description with $0\le a\le4$. Such descriptions are unique: t modulo 5 determines a, then t determines b. For each a, the choices are $b=0,\ldots,94-a$, giving $95-a$ heights. Hence the total is $95+94+93+92+91=465$.

**Answer:** 465.

**Methods:** sumset, bounded occupancy.

**Verification:** Independent exact check passed: Enumerated all feasible orientation-count pairs and deduplicated heights. Result 465. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 2 archived solution entries. Alternative index 1 is the shortest: reduce the count of height-2 offset bricks modulo five, obtaining unique canonical descriptions.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1995 AIME Problem 3: First hitting a lattice point

A planar random walk starts at (0,0) and chooses each unit cardinal step with probability 1/4. Find numerator plus denominator for the chance it visits (2,2) within six steps.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_3) · MAA AMC.

### Solution

Parity and distance allow a first visit only at step 4 or 6. There are $\binom42=6$ four-step routes. A six-step route ending there has steps RRRUUL or RRUUUD, giving $2\cdot6!/(3!2!)=120$. Of these, $6\cdot4=24$ first arrive at step 4 and then make an out-and-back pair. Thus the required probability is $6/4^4+(120-24)/4^6=3/64$, and the answer is $67$.

**Answer:** 067.

**Methods:** first passage, multinomial.

**Verification:** Independent exact check passed: Enumerated all 4096 six-step walks and tested first or later visits. Result 3/64. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 2 archived solution entries. Both sources separate paths hitting at time 4 from those first hitting at time 6, with different denominator bookkeeping.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1995 AIME Problem 6: Divisors below a square root

Let n=2^31·3^19. Count divisors of n² that are smaller than n but do not divide n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_6) · MAA AMC.

### Solution

The $63\cdot39$ divisors of $n^2$ pair under $d\mapsto n^2/d$, with unique fixed point n. Hence $(63\cdot39-1)/2=1228$ lie below n. Every proper divisor of n lies among these; there are $32\cdot20-1=639$. Subtraction gives $1228-639=589$.

**Answer:** 589.

**Methods:** divisor involution, complement.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 3 archived solution entries. The general two-prime simplification is that the requested count equals the product of the two exponents.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 1995 AIME Problem 8: Two simultaneous integer ratios

Count positive integer pairs $y<x\le100$ for which $x/y$ and $(x+1)/(y+1)$ are integers.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_8) · MAA AMC.

### Solution

The two conditions are equivalent to both $y$ and $y+1$ dividing $x-y$. Since they are coprime, $x-y=t y(y+1)$ for an integer $t\ge1$. Conversely this expression satisfies both conditions. For a given $y$ the count is $\lfloor(100-y)/(y(y+1))\rfloor$. Only $y=1,\ldots,9$ contribute, with counts $49,16,8,4,3,2,1,1,1$. Their sum is $85$.

**Answer:** 085.

**Methods:** parametric counting, divisibility.

**Verification:** Independent exact check passed: Checked every bounded integer pair directly. Result 85. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 3 archived solution entries. Alternatives derive the same y(y+1) divisibility parametrization or enumerate its small y-cases.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 1995 AIME Problem 11: A self-similar cut prism

An integer-sided rectangular prism has sorted sides $a\le b\le c$ with $b=1995$. A face-parallel cut produces a smaller similar prism. Count possible triples $(a,b,c)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_11) · MAA AMC.

### Solution

The similar piece has scale factor q<1 and sorted sides qa,qb,qc, two of which are unchanged original side lengths. The unchanged lengths cannot include c, since qc<c; they therefore are a and b, forcing qb=a and qc=b. Consequently $ac=b^2$ and $a<b<c$. Conversely any such factor pair works: cut the c-side to length $qa=a^2/b$, which is positive and less than c; the remaining two dimensions are a,b, as required. Now $1995=3\cdot5\cdot7\cdot19$, so $b^2$ has $3^4=81$ divisors. Excluding the central pair a=c=b and pairing reciprocal divisors gives $(81-1)/2=40$ triples.

**Answer:** 040.

**Methods:** factor pairing, hybrid geometry.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1995 AIME Problem 15: Five heads before two tails

Flip a fair coin until either five consecutive heads or two consecutive tails first appears. Find numerator plus denominator for the probability that the five-head run wins.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_15) · MAA AMC.

### Solution

A successful stopped word has an optional initial T, followed by zero or more blocks $H^jT$ with $1\le j\le4$, then HHHHH. This parsing is unique: the blocks are the completed head-runs before the winning run. The optional prefix contributes weight $1+1/2=3/2$; each block has total probability weight $\sum_{j=1}^4 2^{-(j+1)}=15/32$; the last run has weight 1/32. Summing disjoint stopped words gives $p=(3/2)(1/32)\sum_{k\ge0}(15/32)^k=3/34$. Thus the answer is $37$.

**Answer:** 037.

**Methods:** unique blocks, absorbing probability.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 4 archived solution entries. Alternatives use geometric block sums or finite absorbing-state equations; the bare terminal-weight ratio needs justification.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 1996 AIME Problem 2: Even logarithm floors

Count positive integers $n<1000$ for which $\lfloor\log_2 n\rfloor$ is positive and even.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_2) · MAA AMC.

### Solution

The allowed floor values are 2,4,6,8. Value 2j corresponds exactly to $2^{2j}\le n<2^{2j+1}$, a block of $2^{2j}$ integers. All four blocks lie below 1000, and the next begins at 1024. The count is $4+16+64+256=340$.

**Answer:** 340.

**Methods:** interval partition, hybrid algebra.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1996 AIME Problem 3: Counting monomials after expansion

Find the least positive n for which (xy−3x+7y−21)^n has at least 1996 nonzero monomials after collecting terms.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_3) · MAA AMC.

### Solution

Factor the expression as $(x+7)^n(y-3)^n$. For each pair $0\le i,j\le n$, the monomial $x^iy^j$ has coefficient $\binom ni7^{n-i}\binom nj(-3)^{n-j}\ne0$. Different exponent pairs are distinct monomials, so exactly $(n+1)^2$ terms survive. Since $44^2=1936<1996\le45^2=2025$, the minimum is $n=44$.

**Answer:** 044.

**Methods:** Cartesian product, polynomial support.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 2 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1996 AIME Problem 6: No perfect or winless team

Five teams play every pair once, with equally likely independent outcomes. Find numerator plus denominator for the probability that each team both wins and loses at least once.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_6) · MAA AMC.

### Solution

A specified team wins all four games with probability 1/16; these five events are mutually exclusive. The same holds for losing all four. For a specified distinct undefeated team and winless team, seven outcomes are forced (their shared game only once), giving probability 1/128. There are 20 such ordered pairs, and no higher intersections. Thus the forbidden probability is $5/16+5/16-20/128=15/32$. The desired probability is $17/32$, giving $49$.

**Answer:** 049.

**Methods:** inclusion-exclusion, tournament.

**Verification:** Independent exact check passed: Enumerated all 1024 labeled tournament orientations. Result 17/32. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 2 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1996 AIME Problem 7: Two marked squares up to rotation

Two cells of a 7-by-7 board are yellow and the rest green. Count colorings up to rotations of the board, with reflections remaining distinct.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_7) · MAA AMC.

### Solution

Apply Burnside to the four rotations. The identity fixes $\binom{49}{2}=1176$ colorings. A half-turn fixes exactly the 24 opposite pairs of noncentral cells. A quarter-turn or three-quarter-turn fixes none: noncentral cell orbits have size four and the center alone cannot provide two yellow cells. Hence the orbit count is $(1176+24)/4=300$.

**Answer:** 300.

**Methods:** Burnside, rotational symmetry.

**Verification:** Independent exact check passed: Canonicalized every marked-cell pair under four explicit coordinate rotations. Result 300. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 2 archived solution entries. Sources split exceptional symmetry classes directly; Burnside consolidates their cases.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1996 AIME Problem 8: Integer pairs of prescribed harmonic mean

Count positive integer pairs x<y whose harmonic mean is 6^20.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_8) · MAA AMC.

### Solution

Put $H=6^{20}/2=2^{19}3^{20}$. The equation is $xy=H(x+y)$, so $(x-H)(y-H)=H^2$. Both factors are positive, because $1/x+1/y=1/H$ forces x,y>H. Thus strict pairs x<y correspond bijectively to factor pairs of $H^2=2^{38}3^{40}$ with unequal factors. There are $39\cdot41=1599$ divisors and one central equal pair, so the answer is $(1599-1)/2=799$.

**Answer:** 799.

**Methods:** factor-pair bijection, hybrid number theory.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1996 AIME Problem 9: Alternating elimination along lockers

Initially lockers 1,…,1024 are closed. On alternating left-to-right and right-to-left passes, open every other still-closed locker, starting with the first encountered. Find the last opened locker.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_9) · MAA AMC.

### Solution

The closed lockers after each pass remain an arithmetic progression. If it has even length and step d, a left-to-right pass removes positions 1,3,…, so its first entry increases by d; a right-to-left pass removes its even positions, leaving the first entry unchanged. Every pass doubles the step and halves the length. Starting with first entry 1 and step 1, the odd-numbered passes 1,3,5,7,9 increase the first entry by $1,4,16,64,256$. After ten passes a single locker remains, numbered $1+1+4+16+64+256=342$; it is opened next and last.

**Answer:** 342.

**Methods:** elimination recurrence, algorithm invariant.

**Verification:** Independent exact check passed: Simulated alternating passes over the actual list of closed lockers. Result 342. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 3 archived solution entries. A valid alternative recurrence is L_n=2^n+2−2L_{n−1}; the third entry is only an invitation to simulate.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 1996 AIME Problem 12: Mean sum of five pair distances

Permute 1,…,10 uniformly, pair adjacent entries in five disjoint pairs, and add their absolute differences. If the mean is p/q in lowest terms, find p+q.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Each pair is uniform among the $\binom{10}{2}=45$ unordered pairs. Difference d occurs for exactly 10−d pairs, so its expected difference is $\sum_{d=1}^9d(10-d)/45=165/45=11/3$. Linearity of expectation applies even though the five pairs are dependent, giving total mean $55/3$. Hence p+q is $58$.

**Answer:** 058.

**Methods:** linearity of expectation, weighted pairs.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 4 archived solution entries. Alternatives use average pair distance, signed contribution of each number or exchangeability of order-statistic gaps.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 1996 AIME Problem 14: Cubes crossed by a space diagonal

A box of side lengths 150,324,375 is partitioned into unit cubes. Count cubes whose interiors meet a long diagonal.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_14) · MAA AMC.

### Solution

Parametrize the diagonal by $(150t,324t,375t)$, 0<t<1. A new cube begins at each distinct interior crossing of a coordinate-integer plane. The three crossing sets have sizes 149,323,374; pairwise overlaps have sizes $\gcd(150,324)-1=5$, $\gcd(324,375)-1=2$, $\gcd(150,375)-1=74$, and the triple overlap has size $\gcd(150,324,375)-1=2$. Inclusion-exclusion gives 767 crossing times. They divide the diagonal into 768 open intervals, each lying in exactly one cube interior. The answer is $768$.

**Answer:** 768.

**Methods:** inclusion-exclusion, lattice geometry.

**Verification:** Independent exact check passed: Built the exact union of all interior rational crossing times. Result 768. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 2 archived solution entries. Both sources use inclusion-exclusion of simultaneous coordinate-plane crossing times.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1997 AIME Problem 1: Differences of squares

Count integers 1 through 1000 that are differences of squares of nonnegative integers.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_1) · MAA AMC.

### Solution

Every odd integer $2a+1$ equals $(a+1)^2-a^2$, and every positive multiple $4b$ equals $(b+1)^2-(b-1)^2$. Conversely squares are 0 or 1 modulo 4, so a difference cannot be 2 modulo 4. The qualifying integers are exactly the 500 odds and 250 multiples of 4, totaling $750$.

**Answer:** 750.

**Methods:** residue classification, constructive counting.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1997 AIME Problem 2: Squares among grid rectangles

Let r be the number of rectangles and s the number of squares formed by the nine horizontal and nine vertical lines of a standard 8-by-8 board. Reduce s/r=m/n and find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_2) · MAA AMC.

### Solution

A rectangle is determined by two horizontal and two vertical boundary lines, so $r=\binom92^2=1296$. A square of side k cells has $(9-k)^2$ placements, giving $s=\sum_{j=1}^8j^2=204$. Thus $s/r=17/108$ and the answer is $125$.

**Answer:** 125.

**Methods:** grid counting, boundary choices.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1997 AIME Problem 5: Decimal numbers closest to two sevenths

Count four-place decimals 0.abcd for which 2/7 is the closest fraction whose numerator is 1 or 2 and whose denominator is an integer.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_5) · MAA AMC.

### Solution

The neighboring distinct admissible fractions around $2/7$ are $1/4=2/8$ and $1/3=2/6$. All fractions with numerator 1 also occur with numerator 2 and an even denominator, so there are no omitted intervening candidates. The nearest-fraction cell is between the midpoints $15/56$ and $13/42$. Multiplying by 10000 gives bounds $2678.57\ldots$ and $3095.23\ldots$, neither an integer. Thus the allowed integers abcd are 2679 through 3095, numbering $417$.

**Answer:** 417.

**Methods:** interval lattice count, nearest neighbor.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1997 AIME Problem 8: Balanced sign arrays

Count 4-by-4 arrays of ±1 in which every row and column sums to zero.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_8) · MAA AMC.

### Solution

Each row and column must have two plus signs. Choose the plus positions of the first row in six ways. Relative to them, the second row overlaps in 2,0,or1 positions. Overlap 2 has one choice and forces the last two rows, giving 1 completion. Overlap 0 has one choice and allows any two plus positions in row three, with row four forced, giving 6. Overlap 1 has four choices; then one column requires two minuses, one two pluses, and the remaining two columns must split signs oppositely across the last two rows, giving 2 completions per choice. Total: $6(1+6+4\cdot2)=90$.

**Answer:** 090.

**Methods:** binary matrices, overlap casework.

**Verification:** Independent exact check passed: Enumerated all $6^4$ row patterns and checked column sums. Result 90. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 3 archived solution entries. The first two entries use legitimate row/column overlap cases; the final complementary-row sketch has a partition gap.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 1997 AIME Problem 10: Complementary attribute triples

A deck has all 27 combinations of three attributes, each with three values. Count three-card sets in which each attribute is either constant across the cards or takes all three values.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Any two distinct cards determine a unique third: in each coordinate repeat their value if they agree, and choose the unused third value if they disagree. At some coordinate the original cards differ, so the completed card is distinct from both. The resulting three-card set is complementary, and each complementary set is generated by its three unordered pairs. Therefore the count is $\binom{27}{2}/3=117$.

**Answer:** 117.

**Methods:** constant fibers, finite geometry.

**Verification:** Independent exact check passed: Checked all 2925 three-card subsets directly. Result 117. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 3 archived solution entries. Alternatives are attribute casework, unique pair completion and ordered triples divided by 6.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 1997 AIME Problem 14: A short arc probability

Two distinct 1997th roots of unity are chosen uniformly. Find numerator plus denominator for the chance that $|v+w|\ge\sqrt{2+\sqrt3}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_14) · MAA AMC.

### Solution

If $\theta$ is their shorter angular separation, then $|v+w|^2=2+2\cos\theta$. The condition is $\cos\theta\ge\sqrt3/2$, or $\theta\le30^\circ$. Fixing $v$, the circular step distance can be any of $1,\ldots,\lfloor1997/12\rfloor=166$ in either direction. Thus 332 of the 1996 possible values of $w$ qualify. The probability is $83/499$, giving $582$.

**Answer:** 582.

**Methods:** cyclic symmetry, geometric probability.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 4 archived solution entries. Valid sources use rotation invariance and the cosine of the angular separation; one geometric derivation has incorrect equations.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 1998 AIME Problem 1: Counting possible LCM partners

How many positive integers k satisfy lcm(6^6,8^8,k)=12^12?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_1) · MAA AMC.

### Solution

The existing least common multiple is $2^{24}3^6$ and the target is $2^{24}3^{12}$. Thus k has no other prime factors, its 3-exponent must be 12, and its 2-exponent can be any integer from 0 to 24. There are $25$ choices.

**Answer:** 025.

**Methods:** prime exponent product.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 2 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1998 AIME Problem 2: Integer points between two slope bounds

Count positive integer pairs with $x\le2y\le60$ and $y\le2x\le60$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_2) · MAA AMC.

### Solution

The inequalities require $1\le x,y\le30$, excluding points with x>2y or y>2x. These exclusions are disjoint. For x>2y, y ranges from 1 to 14 and there are 30−2y choices of x. The excluded count on one side is $\sum_{y=1}^{14}(30-2y)=210$. Therefore $30^2-2(210)=480$ pairs remain.

**Answer:** 480.

**Methods:** complement, lattice points.

**Verification:** Independent exact check passed: Directly tested all bounded positive lattice pairs. Result 480. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 5 archived solution entries. The reliable sources use Pick’s theorem or explicit sums of lattice rows; pattern-only alternatives are not proofs.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 1998 AIME Problem 4: Three odd hand sums

Randomly divide tiles numbered 1,…,9 among three labeled players, three tiles each. Find numerator plus denominator for the probability that all three hand sums are odd.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_4) · MAA AMC.

### Solution

There are five odd tiles and four even ones. For all hand sums to be odd, the odd counts must be 3,1,1. Regard the nine dealt positions as three groups of three; the five odd positions form a uniform five-subset. Favorable placements choose the all-odd player in 3 ways, then one odd position in each other hand in $3^2$ ways. Thus $P=27/\binom95=3/14$, giving $17$.

**Answer:** 017.

**Methods:** parity, hypergeometric.

**Verification:** Independent exact check passed: Enumerated all 126 parity placements among the dealt positions. Result 3/14. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 3 archived solution entries. All three methods reduce to odd-tile counts 3,1,1 and differ only in the sample-space encoding.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 1998 AIME Problem 7: Odd positive compositions

Let n count ordered quadruples of positive odd integers summing to 98. Find n/100.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_7) · MAA AMC.

### Solution

Write $x_i=2y_i+1$ with $y_i\ge0$. This is a bijection to $y_1+y_2+y_3+y_4=47$. Separating 47 indistinguishable units into four ordered boxes gives $\binom{50}{3}=19600$ quadruples. Dividing by 100 gives $196$.

**Answer:** 196.

**Methods:** stars and bars, parity bijection.

**Verification:** Independent exact check passed: Enumerated the first three odd parts and tested the forced fourth. Result 19600. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 5 archived solution entries. Alternatives use positive or nonnegative compositions, paired units, a convolution sum or a generating function.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 1998 AIME Problem 9: Overlapping coffee breaks

Two people arrive independently and uniformly during one hour and each stays m minutes. Their visits overlap with probability 40%. Write m=a−b√c with c squarefree and find a+b+c.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_9) · MAA AMC.

### Solution

The two arrival times form a uniform point in a 60-by-60 square. Nonoverlap is $|x-y|>m$, two corner triangles of total area $(60-m)^2$. Therefore $(60-m)^2/3600=3/5$. Taking the root with $0\le m\le60$ gives $m=60-12\sqrt{15}$ and $a+b+c=87$.

**Answer:** 087.

**Methods:** continuous probability, area complement.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 2 archived solution entries. The alternative conditions on one arrival time; its linear average needs the endpoint intervals to be handled correctly.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 1998 AIME Problem 13: Complex weights over subsets

For each nonempty subset of {1,…,n}, list its elements increasingly and weight the jth by i^j. Let S_n sum these weighted subset sums. Given S_8=−176−64i and S_9=p+qi, find |p|+|q|.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_13) · MAA AMC.

### Solution

Pair each subset $U$ of $\{1,\ldots,8\}$, including the empty set, with $U\cup\{9\}$. Old terms contribute twice $S_8$. If $U$ has $k$ elements, the new term is $9i^{k+1}$, so the total extra contribution is $9i\sum_{k=0}^8\binom8k i^k=9i(1+i)^8=144i$. Consequently $S_9=2(-176-64i)+144i=-352+16i$, giving $368$.

**Answer:** 368.

**Methods:** weighted subsets, binomial theorem.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1998 AIME Problem 15: Longest domino chain

A chain uses distinct ordered pairs $(i,j)$, $1\le i,j\le40$, $i\ne j$, with successive pairs sharing the connecting endpoint. It may not use both $(i,j)$ and $(j,i)$. Maximize its length.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_15) · MAA AMC.

### Solution

Forget orientations: a chain is an edge trail in the complete graph K_40. Its used degrees must be even except possibly at its two endpoints. Since all 40 full degrees are 39, at least 38 vertices must lose an incident edge. Deleting one edge affects at most two vertices, so at least 19 of the 780 edges are omitted, giving length at most 761. To attain it, delete a matching covering 38 vertices. The remaining graph is connected (every degree is at least 38) and has exactly two odd-degree vertices. It therefore has an Euler trail: adding an edge between the odd vertices makes all degrees even, and the usual cycle-splicing construction gives an Euler circuit; remove the added edge. Orient every traversed edge along that trail. No edge is repeated or reversed, yielding a valid chain of length $761$.

**Answer:** 761.

**Methods:** Euler trail, extremal graph.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 5 archived solution entries. Alternative indices 1 and 2 supply existence through Euler trails or an explicit induction; other sketches lack that essential step.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 1999 AIME Problem 5: Possible digit-sum changes

Let S(x) be the decimal digit sum and T(x)=|S(x+2)−S(x)| for positive integers x. Count distinct T-values at most 1999.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_5) · MAA AMC.

### Solution

In adding 2, each carry reduces the digit-sum change by 9. Thus $S(x+2)-S(x)=2-9k$ for some $k\ge0$. Every $k$ occurs: $k=0$ at $x=1$, and $k\ge1$ at $x=10^k-2$. Therefore possible absolute changes are 2 and $9k-2$ for $k\ge1$, with no repetitions. The latter are at most 1999 exactly when $k\le\lfloor2001/9\rfloor=222$. Total: $223$.

**Answer:** 223.

**Methods:** carry invariant, distinct image.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1999 AIME Problem 7: Four-position divisor switches

Switches labeled $2^x3^y5^z$ for $0\le x,y,z\le9$ cycle $A\to B\to C\to D\to A$. Processing every label once advances all switches whose labels divide it. Starting at A, how many finish at A?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_7) · MAA AMC.

### Solution

A switch with exponents x,y,z advances once for each multiple label, namely $(10-x)(10-y)(10-z)$ times. It returns to A iff this product is divisible by 4. Each factor ranges independently over 1,…,10. The complementary products have either no factor of 2, giving $5^3=125$ triples, or exactly one factor of 2, giving $3\cdot3\cdot5^2=225$ (choose its location and one of 2,6,10). Hence $1000-125-225=650$ switches return to A.

**Answer:** 650.

**Methods:** valuation complement, divisor incidence.

**Verification:** Independent exact check passed: Checked the advance count for all 1000 switch labels. Result 650. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1999 AIME Problem 8: Exactly two thresholds on a simplex

On the nonnegative triangle $x+y+z=1$, take points satisfying exactly two of $x\ge1/2,y\ge1/3,z\ge1/6$. If their area fraction is $m/n$ reduced, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_8) · MAA AMC.

### Solution

The region satisfying $x\ge a,y\ge b$ is a translated copy of the original simplex scaled by $1-a-b$, so its area fraction is $(1-a-b)^2$. For the three pairs of thresholds, the residual scales are $1/6,1/3,1/2$. Their triple intersection is only the point $(1/2,1/3,1/6)$, since the thresholds sum to 1, so overlaps have zero area. The desired fraction is $1/36+1/9+1/4=7/18$, giving $25$.

**Answer:** 025.

**Methods:** exact multiplicity, geometric probability.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 1999 AIME Problem 10: A triangle among four chosen segments

From the 45 segments joining ten points with no three collinear, choose four uniformly. Find numerator plus denominator for the probability that three form a triangle on the given points.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Choose the three triangle vertices in $\binom{10}{3}$ ways and the extra segment in 45−3=42 ways. There is no overcount: two distinct triangles require at least five edges, so four selected edges contain at most one triangle. Thus $P=\binom{10}{3}42/\binom{45}{4}=16/473$, giving $489$.

**Answer:** 489.

**Methods:** graph counting, unique witness.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 3 archived solution entries. Alternatives expose the triangle first or split by four versus five used endpoints.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 1999 AIME Problem 13: Distinct tournament win totals

Forty teams play each pair once with equally likely independent winners. If the probability that all win totals differ is $m/n$ in lowest terms, find $\log_2 n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_13) · MAA AMC.

### Solution

The 40 distinct win totals must be exactly 0,…,39. A team with 39 wins beats all others; removing it leaves distinct totals 0,…,38. Induction shows that a ranking uniquely determines every result, so favorable outcomes number $40!$. There are $2^{\binom{40}{2}}=2^{780}$ equally likely tournaments. The power of 2 in $40!$ is $20+10+5+2+1=38$. After cancellation the denominator is $2^{780-38}=2^{742}$, giving $742$.

**Answer:** 742.

**Methods:** transitive tournament, valuation.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2000 AIME I Problem 3: Adjacent binomial coefficients

For coprime positive integers $a,b$, the coefficients of $x^2$ and $x^3$ in $(ax+b)^{2000}$ agree. Determine $a+b$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

The ratio of the $x^3$ coefficient to the $x^2$ coefficient is $\frac{1998a}{3b}=\frac{666a}{b}$. Equality forces $b=666a$. Coprimality gives $(a,b)=(1,666)$, hence $667$.

**Answer:** 667.

**Methods:** binomial coefficients.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2000 AIME I Problem 5: Two urns with a fixed total

Two urns each contain both black and white balls, with $25$ balls in total. Independent uniform draws, one per urn, are both black with probability $27/50$. Write the probability of two whites as reduced $m/n$ and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Let the urn sizes be $a\ge b$. Since $50\mid ab$ and $a+b=25$, both are multiples of $5$, so $(a,b)=(20,5)$ or $(15,10)$. The black counts must have products $54$ or $81$, respectively. The bounds imposed by a white ball in each urn force black counts $(18,3)$ or $(9,9)$. In either case the white probability is $1/25$, so the answer is $26$.

**Answer:** 026.

**Methods:** probability, divisibility.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: Arithmetic slip: the largest feasible denominator is 156, not 154. The candidate multiple 150 and final answer remain valid. Source 2: The exhibited urn sizes establish existence but need an exclusion argument for uniqueness.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2000 AIME I Problem 11: Independent prime exponents

Sum $a/b$ over ordered pairs of coprime positive divisors of $1000$. If the sum is $S$, find $\lfloor S/10\rfloor$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

For each prime $p\in\{2,5\}$, coprimality allows its exponent on only one side. The exponent of $p$ in the ratio therefore ranges uniquely over $-3,-2,\ldots,3$. Independence gives $S=(\sum_{j=-3}^3 2^j)(\sum_{j=-3}^3 5^j)=\frac{127}{8}\frac{19531}{125}=2480.437$. Thus the answer is $248$.

**Answer:** 248.

**Methods:** weighted counting, product principle, prime exponents.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 3: The numerical approximation is unnecessary; the exact finite sum used here avoids rounding.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2000 AIME I Problem 12: Reflection orbits

A real function satisfies $f(x)=f(398-x)=f(2158-x)=f(3214-x)$ for every real $x$. What is the largest number of different values among $f(0),\ldots,f(999)$?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Composing reflections gives periods $1760$ and $1056$, hence period $352$. On residues modulo $352$, the remaining identification is $r\sim46-r$. There are two fixed residues, $23$ and $199$; all other $350$ residues occur in pairs. Thus there are $2+350/2=177$ orbits. Assign a separate value to each orbit (and extend using the same reflection action on the reals); all $177$ values occur in $0,\ldots,999$.

**Answer:** 177.

**Methods:** orbits, invariants.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2000 AIME I Problem 15: Alternating elimination

A stack of $2000$ labeled cards is processed by removing the top card, then moving the next card to the bottom, repeatedly. Removed labels are $1,2,\ldots,2000$. How many cards originally preceded label $1999$?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Track positions rather than labels. Let $E(n,k)$ be the original position of the $k$th removed card. Then $E(n,1)=1$ and, for $k>1$, $E(n,k)=2+(E(n-1,k-1)\bmod(n-1))$: after the first removal and rotation the old positions are $3,4,\ldots,n,2$. Repeated substitution gives $E(2000,1999)=928$. This recurrence is a bijection at every step, so the required number above the card is $927$.

**Answer:** 927.

**Methods:** recurrences, permutations, inverse processes.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 4: The final product has an incorrect multiplier in its displayed arithmetic. Source 5: The concluding modulus is mistyped as 2056 rather than 2048.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2000 AIME II Problem 2: Lattice points on a difference of squares

Count all ordered integer pairs $(x,y)$ satisfying $x^2-y^2=2000^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

The factors $x-y,x+y$ have equal parity and product $2000^2$, so both are even. Put $u=(x-y)/2$ and $v=(x+y)/2$. Then $uv=10^6=2^6 5^6$, and conversely every integer factor pair gives exactly one point $(x,y)=(u+v,v-u)$. There are $7\cdot7=49$ choices of positive $u$ and another 49 negative choices, with $v$ determined. Hence there are $98$ points.

**Answer:** 098.

**Methods:** difference of squares, divisor counting, bijections.

**Verification:** Brute-force integer-square test for every y in the analytically bounded range, counting both signs of x.

**Source comparison:** The sole source was checked. Its factor allocation is sound; the explicit inverse here clarifies why the factor of 2 accounts for signs without an additional factor for order.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2000 AIME II Problem 3: A second matching pair

A deck has four cards of each rank $1,\ldots,10$. Remove two cards of one rank. Two further cards are sampled uniformly without replacement. If their matching probability is $m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

Among the $\binom{38}{2}=703$ possible unordered draws, nine intact ranks contribute $9\binom42=54$ pairs and the depleted rank contributes one. Thus $P=55/703$, giving $758$.

**Answer:** 758.

**Methods:** probability, combinations.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2000 AIME II Problem 5: Ordered rings on fingers

Choose five of eight distinct rings and distribute them on four labeled fingers. Their vertical order matters; empty fingers are allowed. Find the first three nonzero digits of the number of arrangements.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Choose and order the five rings in $(8)_5$ ways, then split that ordered list into four possibly empty consecutive lists. The split is a weak composition of $5$ into $4$ parts, counted by $\binom83$. Thus the count is $(8)_5\binom83=376320$, yielding $376$.

**Answer:** 376.

**Methods:** stars and bars, permutations.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2000 AIME II Problem 7: Half a binomial row

Define $N$ by $\sum_{k=2}^{9}1/(k!(19-k)!)=N/18!$. Find the greatest integer strictly smaller than $N/100$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Multiply by $19!$. Complementation pairs the subsets of sizes $0,\ldots,9$ with those of sizes $19,\ldots,10$, so their binomial sum is $2^{18}$. Consequently $19N=2^{18}-1-19=262124$, hence $N=13796$ and the requested integer is $137$.

**Answer:** 137.

**Methods:** binomial identities, complement.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 2: The common denominator is described as 19 factorial although the displayed reduced numerators correspond to 18 factorial.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2001 AIME I Problem 6: Sorted dice

Four independent fair six-sided dice rolls are nondecreasing in time with probability $m/n$ in lowest terms. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

A nondecreasing outcome is uniquely determined by the six face multiplicities, nonnegative integers summing to $4$. There are $\binom94=126$ outcomes out of $6^4=1296$. Thus $P=7/72$ and $m+n=79$.

**Answer:** 079.

**Methods:** stars and bars, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 12 of 12. Indices in the data are zero-based.

**Status:** solved.

## 2001 AIME I Problem 10: Parity classes of lattice points

Choose two distinct points uniformly from $\{0,1,2\}\times\{0,1,2,3\}\times\{0,1,2,3,4\}$. Their midpoint belongs to the same set with probability $m/n$ in lowest terms. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

The midpoint has integer coordinates precisely when the endpoints agree in all three coordinate parities. Counting ordered pairs, including coincidences, gives $(2^2+1^2)(2^2+2^2)(3^2+2^2)=520$. Subtract the $60$ coincident pairs. Therefore $P=460/(60\cdot59)=23/177$, yielding $200$. The coordinate bounds automatically hold for every midpoint.

**Answer:** 200.

**Methods:** parity, probability, product principle.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2001 AIME I Problem 11: Two numberings of a rectangular array

In a $5\times N$ array choose one point per row. Row-major labels $x_i$ and column-major labels $y_i$ obey $x_1=y_2,x_2=y_1,x_3=y_4,x_4=y_5,x_5=y_3$. Find the smallest $N$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

If the chosen columns are $c_i$, then $x_i=(i-1)N+c_i$ and $y_i=5c_i-5+i$. The first two relations give $N=24c_2-19$, $c_1=5c_2-3$. Eliminating $c_4,c_5$ from the last three gives $124c_3=117N+51$. Reduction modulo $31$ forces $c_2\equiv7\pmod{31}$, so $N\ge149$. At $N=149$, the columns $(32,7,141,88,107)$ satisfy all five relations and lie in $[1,N]$. Thus $149$ is attained.

**Answer:** 149.

**Methods:** permutations, congruences.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2001 AIME I Problem 14: Binary strings with two forbidden runs

Count binary strings of length $19$ containing neither $11$ nor $000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

For length $n\ge2$, count endings $00,01,10$ by $(a_n,b_n,c_n)$. Appending one symbol gives $(a_{n+1},b_{n+1},c_{n+1})=(c_n,a_n+c_n,b_n)$, with $(a_2,b_2,c_2)=(1,1,1)$. These transitions are exhaustive and disjoint. Iterating yields $(a_{19},b_{19},c_{19})=(86,151,114)$, totaling $351$.

**Answer:** 351.

**Methods:** finite states, forbidden patterns.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: The specialized index for T_19 disagrees with the immediately preceding general recurrence. Source 5: The claimed recurrence for words ending in zero misses extensions ending in two zeros. Its intermediate counts are wrong; the final total is coincidental.

**Archived alternatives reviewed:** 7 of 7. Indices in the data are zero-based.

**Status:** solved.

## 2001 AIME I Problem 15: Hamilton cycles in a cube complement

Label the eight faces of a regular octahedron randomly by $1,\ldots,8$. No consecutive labels, including $8,1$, may share an edge. Express the probability as reduced $m/n$ and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Dualize the faces to cube vertices. Allowed consecutive moves form two disjoint $K_4$ graphs joined by a perfect matching. A Hamilton cycle uses either two or four matching edges. With two, choose their endpoints in $\binom42=6$ ways and order the two internal vertices in each $K_4$ in $2!^2$ ways: $24$ undirected cycles. With four, choose one of three perfect matchings inside the first $K_4$ and one of two different matchings inside the second: $6$ cycles. Thus there are $30\cdot8\cdot2=480$ labelings among $8!$, giving $1/84$ and answer $85$.

**Answer:** 085.

**Methods:** graphs, Hamilton cycles, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 3: The proposed unique-completion claim is false: some partial assignments have zero or two completions. The later averaging remark does not prove the claimed bijection.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2001 AIME II Problem 1: Digit adjacency as a directed graph

Find the leading three digits of the largest positive integer whose every adjacent two-digit block is a perfect square.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

Allowed edges between successive digits are $1\to6$, $2\to5$, $3\to6$, $4\to9$, $6\to4$, and $8\to1$. This directed graph has no cycles. Its longest directed path is $8\to1\to6\to4\to9$, producing the only five-digit candidate, $81649$. Every other path gives fewer digits. The answer is $816$.

**Answer:** 816.

**Methods:** directed graphs, extremal paths.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2001 AIME II Problem 2: Bounds on an intersection

Among $2001$ students everyone studies Spanish or French. Between $80\%$ and $85\%$ study Spanish and between $30\%$ and $40\%$ study French. Find the difference between the maximum and minimum possible numbers studying both.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

The integer counts range over $1601\le s\le1700$ and $601\le f\le800$. The intersection size is $s+f-2001$, hence ranges from $201$ to $499$. Both extreme choices give nonnegative Venn-region counts, so both are attainable. Their difference is $298$.

**Answer:** 298.

**Methods:** inclusion exclusion, extremal counting.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2001 AIME II Problem 5: Triangle-free ordered sets

Every ten-element subset of $\{4,5,\ldots,n\}$ must contain three side lengths of a nondegenerate triangle. Find the largest such $n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

For increasing $b_1<\cdots<b_{10}$ to avoid triangles, necessarily and sufficiently $b_{i+2}\ge b_i+b_{i+1}$. Sufficiency holds because the two largest entries below $b_{i+2}$ maximize their sum. Starting with the smallest possible pair $4,5$ gives the coordinatewise least forbidden set: $4,5,9,14,23,37,60,97,157,254$. Thus no forbidden ten-set fits below $254$, while this one fits at $254$. The answer is $253$.

**Answer:** 253.

**Methods:** extremal principle, greedy bounds, recurrences.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2001 AIME II Problem 9: Avoiding red subsquares

Color the nine cells of a $3\times3$ board independently red or blue, equally likely. Express the probability of no all-red $2\times2$ subsquare as reduced $m/n$ and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Apply inclusion-exclusion to the four bad subsquares. Single-event counts total $4\cdot2^5=128$. Pair intersections total $4\cdot2^3+2\cdot2^2=40$, according as the two subsquares share an edge or only the center. Triple intersections total $4\cdot2=8$; the fourfold intersection has size $1$. Hence there are $512-(128-40+8-1)=417$ good colorings. The probability is $417/512$, giving $929$.

**Answer:** 929.

**Methods:** inclusion exclusion, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 2: Some case labels and grid descriptions are inconsistent; inclusion-exclusion gives an unambiguous alternative.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2001 AIME II Problem 10: Counting exponent gaps

How many different numbers $10^j-10^i$, with $0\le i<j\le99$, are divisible by $1001$?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Since $1001$ is coprime to $10$, divisibility depends only on $d=j-i$. Modulo $1001$, $10^3\equiv-1$, while direct checking of $10,10^2,10^3$ shows the order is $6$. Thus $d=6,12,\ldots,96$. For each $d$ there are $100-d$ pairs, totaling $\sum_{k=1}^{16}(100-6k)=784$. Different pairs give different decimal strings (a block of nines followed by zeros), so no further quotient is needed.

**Answer:** 784.

**Methods:** residue classes, summation.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** The first archived proof has a divisibility typo in its necessity step; the order-of-10 argument here supplies the missing justification. Audit findings: Source 2: The period-six argument is sound, but one congruence and the index names are mistyped.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2001 AIME II Problem 11: Wins versus losses

A team independently wins, draws, or loses each of six games, with all three outcomes equally likely. Write the probability of more wins than losses as reduced $m/n$ and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Interchanging wins and losses pairs the unequal cases. Equal counts occur in $\sum_{j=0}^{3}6!/(j!j!(6-2j)!)=141$ of the $729$ outcome strings. Hence $P=(729-141)/(2\cdot729)=98/243$, giving $341$.

**Answer:** 341.

**Methods:** symmetry, multinomial coefficients, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: Several win/tie/loss descriptions and a case count are mistyped, although the final probability formula is correct.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2001 AIME II Problem 12: Recursive tetrahedral growth

Begin with a unit-volume regular tetrahedron. At each stage replace the middle quarter-triangle of every triangular face by the three exposed faces of an outward regular tetrahedron. Find numerator plus denominator of the volume after three stages.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Each current triangular face produces six triangles of half its edge length: three old corner pieces and three new faces. Thus the number of new tetrahedra is multiplied by $6$ each stage while each new volume is multiplied by $1/8$. The added volumes are $1/2,3/8,9/32$. The final volume is $1+1/2+3/8+9/32=69/32$, so the answer is $101$.

**Answer:** 101.

**Methods:** recursive counting, geometric scaling.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2002 AIME I Problem 1: A palindrome in either block

A uniformly random plate consists of three letters from a 26-letter alphabet followed by three decimal digits. Either block may be a palindrome. Find numerator plus denominator of the probability that at least one is.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

The first and third characters match with probabilities $1/26$ and $1/10$ in the two independent blocks. The required union probability is $1/26+1/10-1/260=7/52$, hence $59$.

**Answer:** 059.

**Methods:** inclusion exclusion, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2002 AIME I Problem 3: Reversed two-digit ages

One person is currently $25$, and another is older. In a positive integer number $n$ of years their ages are two-digit reversals. Count the possible ordered pairs consisting of the older person's present age and $n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

Write the future younger age as $10a+b$. The older age is $10b+a$, so $1\le a<b\le9$, and $10a+b>25$. Conversely each such digit pair uniquely determines both requested integers. There are $\binom92=36$ pairs; exclude eight with $a=1$ and three with $a=2,b\le5$. The result is $25$.

**Answer:** 025.

**Methods:** bijections, digit counting.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2002 AIME I Problem 5: Squares through dodecagon vertices

How many squares in the plane have at least two vertices among the vertices of a fixed regular dodecagon?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Each pair of dodecagon vertices defines three squares: one using the pair as a diagonal and two using it as a side. This gives $3\binom{12}{2}=198$ incidences. Any square having three dodecagon vertices lies on the same circumcircle, so also has its fourth vertex there. Exactly three squares have all four vertices in the dodecagon. Each was counted $\binom42=6$ times rather than once; subtract $3\cdot5$. The answer is $183$.

**Answer:** 183.

**Methods:** double counting, geometry hybrid.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2002 AIME I Problem 9: Three arithmetic progressions partition the integers

Three progressions start at $1,2,3$ and have positive integer steps $h,t,u$. They partition the positive integers exactly once. Sum $100h+10t+u$ over all valid triples.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

No step is $1$, and $h\ne2$. To cover $4$, either $h=3$ or $t=2$. If $h=3$, avoiding its residue class forces $3\mid t,u$; covering $5,6$ then forces $t=u=3$. Otherwise $t=2$ covers every even integer, so $h,u$ are even. We cannot have $u=2$, since its odd progression would eventually meet the first. Covering $5$ forces $h=4$, and covering $7$ forces $u=4$. Both $(3,3,3)$ and $(4,2,4)$ work. Their encoded sum is $757$.

**Answer:** 757.

**Methods:** covering systems, extremal first gap.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** The first archived solution rejects larger h using the AIME answer range, which is not a proof. The first-uncovered-integer argument here closes that gap. Audit findings: Source 0: Excluding larger step sizes merely from the three-digit answer format is not a proof. The original solution here proves exhaustion by the first uncovered integer. Source 2: The assertion that the smallest step must divide the other steps needs additional justification beyond the stated congruence argument.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2002 AIME I Problem 14: Integer means after deletion

A set of distinct positive integers contains $1$, has maximum $2002$, and has integral mean after deleting any single member. Find its largest possible size.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Write the size as $r+1$ and total as $T$. Integrality says every member is congruent to $T\pmod r$, hence to $1\pmod r$. Therefore $r\mid2001$ and the $(r+1)$st possible positive member is $1+r^2\le2002$. Thus $r\le44$ and $r\mid3\cdot23\cdot29$, giving $r\le29$. The set $\{1,30,59,\ldots,813,2002\}$ has $30$ members, all $1\pmod{29}$, and satisfies the deletion condition. The maximum is $30$.

**Answer:** 030.

**Methods:** extremal sets, congruence invariants.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2002 AIME II Problem 9: Unordered disjoint nonempty subsets

Count unordered pairs of nonempty disjoint subsets of a ten-element set; give the remainder modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

For ordered disjoint pairs, each element chooses membership in the first set, second set, or neither. Exclude the two empty-set events by inclusion-exclusion: $3^{10}-2\cdot2^{10}+1$. Swapping the two nonempty disjoint sets has no fixed point, so divide by $2$. This gives $28501$, hence $501$.

**Answer:** 501.

**Methods:** inclusion exclusion, free symmetry, subsets.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2002 AIME II Problem 12: A rational ballot boundary

Independent shots succeed with probability $2/5$. Require exactly four successes in ten shots and a success fraction at most $2/5$ after every earlier shot. Express the probability as $p^a q^b r/s^c$, with the stated factors prime, and find $(p+q+r+s)(a+b+c)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Let $D(i,j)$ count legal prefixes with $i$ misses and $j$ hits. Use $D(0,0)=1$, set $D(i,j)=0$ when $3j>2i$, and otherwise use $D(i,j)=D(i-1,j)+D(i,j-1)$, interpreting negative indices as zero. The last row $D(6,j)$ for $0\le j\le4$ is $1,5,14,23,23$. Thus $23$ legal words each have probability $(2/5)^4(3/5)^6$. The required value is $(2+3+23+5)(4+6+10)=660$.

**Answer:** 660.

**Methods:** lattice paths, rational ballot, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2003 AIME I Problem 3: Charge each pair to its maximum

For each two-element subset of $\{1,2,3,5,8,13,21,34\}$, record its larger member. Find the sum of the recorded numbers.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

The $k$th entry in increasing order is the maximum of exactly $k-1$ pairs. Therefore the total is $0\cdot1+1\cdot2+2\cdot3+3\cdot5+4\cdot8+5\cdot13+6\cdot21+7\cdot34=484$.

**Answer:** 484.

**Methods:** contribution counting.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2003 AIME I Problem 6: Triangle types in a cube

Sum the areas of all triangles with vertices among the eight vertices of a unit cube. Write the sum as $m+\sqrt n+\sqrt p$ with integer parameters and find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

The $\binom83=56$ triangles split into three types. A face supplies four half-square triangles, giving $24$ of area $1/2$. Each cube edge belongs to two further right triangles with legs $1,\sqrt2$, giving $24$ of area $\sqrt2/2$. The remaining eight join three neighbors of one vertex and are equilateral with side $\sqrt2$, of area $\sqrt3/2$. Thus the sum is $12+12\sqrt2+4\sqrt3=12+\sqrt{288}+\sqrt{48}$, giving $348$.

**Answer:** 348.

**Methods:** double counting, geometry hybrid.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2003 AIME I Problem 9: Equal digit sums

Count four-digit decimal integers whose first two digits have the same sum as their last two digits.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Condition on the common sum $s$. For $1\le s\le9$, the first pair has $s$ choices and the second $s+1$. For $10\le s\le18$, both have $19-s$ choices. Therefore the count is $\sum_{s=1}^9s(s+1)+\sum_{s=10}^{18}(19-s)^2=330+285=615$.

**Answer:** 615.

**Methods:** digit counting, convolution.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2003 AIME I Problem 11: Triangle inequalities as interval probability

Choose $x$ uniformly from $(0,90^\circ)$. The probability that $\sin^2x,\cos^2x,\sin x\cos x$ fail to form a triangle is $d/n$, where $d$ is the degree measure of $\arctan m$ and $m+n<1000$. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Reflection $x\mapsto90^\circ-x$ preserves the event. On $(0,45^\circ)$ the largest length is $\cos^2x$, so failure means $\cos2x\ge\tfrac12\sin2x$, or $x\le\tfrac12\arctan2$. The two symmetric intervals have total length $\arctan2$, hence probability $(\arctan2)/90$. The requested value is $2+90=92$. Endpoints have probability zero.

**Answer:** 092.

**Methods:** continuous probability, symmetry.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2003 AIME I Problem 13: A majority of binary ones

Let $N$ count integers from $1$ through $2003$ whose binary expansions contain more ones than zeros. Find $N\bmod1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

For a binary length $r+1$, fix the leading one and choose at least $\lceil r/2\rceil$ further ones among $r$ slots. Summing through length $11$ and using binomial symmetry gives $(2047+\sum_{j=0}^{5}\binom{2j}{j})/2=(2047+351)/2=1199$. Each integer $2004,\ldots,2047$ has at least six ones: numbers $1985$ through $2015$ have the first five bits $11111$ and a nonzero suffix, and $2016$ onward already have six leading ones. Remove these $44$ integers. Thus $N=1155$, giving $155$.

**Answer:** 155.

**Methods:** binomial symmetry, binary digits.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 2: A displayed count uses its residue modulo 1000 before explicitly saying so.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2003 AIME II Problem 3: Uniform outdegree words

Count length-seven words on $\{A,B,C\}$ that avoid the adjacent blocks $AB,BC,CA$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

There are three initial letters. After any letter exactly two next letters are permitted, independent of the previous history. The multiplication principle gives $3\cdot2^6=192$.

**Answer:** 192.

**Methods:** product principle, finite states.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2003 AIME II Problem 12: Minimum occupancy with percentage constraints

Twenty-seven candidates receive integer vote counts totaling $s$. For each candidate, its vote count exceeds its exact percentage of all votes by at least one. Find the smallest $s$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

A count $v$ must satisfy $v(1-100/s)\ge1$. If $s\le133$, then any $v\le4$ fails, so every candidate needs at least five votes, forcing $s\ge135$, a contradiction. At $s=134$, the counts $4,5,\ldots,5$ satisfy the inequality, since even $4(1-100/134)>1$. Thus the minimum is $134$.

**Answer:** 134.

**Methods:** pigeonhole principle, extremal occupancy.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: An intermediate denominator changes sign incorrectly; retain the positive denominator when deriving the inequality.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2003 AIME II Problem 13: Return walk on a triangle

A walker starts at a vertex of a triangle and at each step chooses uniformly one of the other two vertices. Find numerator plus denominator of its probability of returning after ten steps.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Let $p_n$ be the return probability. A return on the next step requires first being away and then selecting the start, so $p_{n+1}=(1-p_n)/2$, $p_0=1$. Subtracting the fixed point $1/3$ gives $p_n=1/3+(2/3)(-1/2)^n$. Thus $p_{10}=171/512$ and the answer is $683$.

**Answer:** 683.

**Methods:** Markov recurrences, symmetry, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 3: The presentation conflates probability transitions and integer walk counts. Source 4: The constant term in the displayed characteristic polynomial has the wrong sign; the listed eigenvalues correspond to the corrected sign. Source 5: The limiting distribution and the answer format do not determine the exact finite-step probability. This is a heuristic, not a proof. Source 6: The polynomial reduction should explicitly be stated modulo x cubed minus one.

**Archived alternatives reviewed:** 8 of 8. Indices in the data are zero-based.

**Status:** solved.

## 2004 AIME I Problem 3: Pairs of polyhedron vertices

A convex polyhedron has $26$ vertices, $60$ edges, $24$ triangular faces and $12$ quadrilateral faces. Count pairs of vertices whose segment is neither an edge nor contained in a face.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

Every pair determines an edge, a face diagonal, or a space diagonal. There are $\binom{26}{2}=325$ pairs, $60$ edges, and $12\cdot2=24$ face diagonals. Convexity ensures a nonedge cannot be a diagonal in two distinct faces. The required count is $325-60-24=241$.

**Answer:** 241.

**Methods:** complement, geometric incidence.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2004 AIME I Problem 6: Alternating four-digit permutations

Count four-digit integers with distinct digits satisfying $a_1<a_2>a_3<a_4$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

On any four increasing values there are five alternating permutations: rank words $1324,1423,2314,2413,3412$. If zero is absent, all five work, giving $5\binom94$. If zero is present it cannot lead, leaving the final three rank words and $3\binom93$ possibilities. The total is $630+252=882$.

**Answer:** 882.

**Methods:** relative order, permutations.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2004 AIME I Problem 7: Pair contributions to a coefficient

Find the absolute value of the coefficient of $x^2$ in $\prod_{k=1}^{15}(1+(-1)^k kx)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Put $a_k=(-1)^k k$. The desired coefficient is $\sum_{i<j}a_i a_j=((\sum a_i)^2-\sum a_i^2)/2$. Here $\sum a_i=-8$ and $\sum a_i^2=15\cdot16\cdot31/6=1240$. The coefficient is $(64-1240)/2=-588$, giving $588$.

**Answer:** 588.

**Methods:** contribution counting, generating functions.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: An ordered-pair index is used where an unordered-pair index is required before doubling. Source 3: A positive contribution subtotal is mistyped; the printed arithmetic does not give the claimed result. Source 4: The final coefficient sign is reversed; its absolute value is still correct. Source 6: The displayed product does not retain the original alternating signs, so that expansion cannot justify the requested coefficient.

**Archived alternatives reviewed:** 7 of 7. Indices in the data are zero-based.

**Status:** solved.

## 2004 AIME I Problem 8: Regular star polygons

Count similarity classes of connected regular $1000$-vertex star polygons with equal edge lengths and equal counterclockwise turning angles less than $180^\circ$, requiring a genuine edge crossing.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

Equal turns and lengths make successive edges a geometric progression of unit directions. Closure and distinct vertices therefore give the regular star $\{1000/k\}$, with $\gcd(k,1000)=1$. The counterclockwise turn condition chooses $1\le k<500$; $k=1$ is the convex polygon and must be excluded. Coprime residues pair as $k,1000-k$, so the number is $\varphi(1000)/2-1=400/2-1=199$.

**Answer:** 199.

**Methods:** cyclic permutations, totient, geometry hybrid.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2004 AIME I Problem 10: A random disk avoids a diagonal

A unit-radius disk has its center uniformly distributed among positions where it fits in a $15\times36$ rectangle. Find numerator plus denominator of the probability that it misses a fixed diagonal.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

Allowed centers form a $13\times34$ rectangle. The centers of disks entirely on one side of the diagonal form the triangle obtained by shifting each side of a $15,36,39$ right triangle inward by one. Its original inradius is $(15+36-39)/2=6$, so the new triangle has similarity ratio $5/6$ and area $(15\cdot36/2)(5/6)^2=375/2$. The two sides contribute total area $375$. Thus $P=375/442$ and the answer is $817$.

**Answer:** 817.

**Methods:** continuous probability, geometry hybrid.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: For a nonsquare rectangle, the claimed diagonal reflection is not a symmetry. Central symmetry justifies the equal-area conclusion.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2004 AIME I Problem 15: Reverse dynamics and forbidden operation runs

Iterate $f(1)=1$, $f(x)=x/10$ when $10\mid x$, and $f(x)=x+1$ otherwise. Let $d(x)$ be the first index with value $1$, starting at index one. If $m$ integers have $d(x)=20$, find the sum of distinct prime factors of $m$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Reverse the trajectory: the first reverse step is $1\to10$, followed by $18$ operations $A:y\mapsto y-1$ or $B:y\mapsto10y$. An initial run of nine $A$'s would return to $1$, and after a $B$ ten consecutive $A$'s are impossible because subtraction would use a multiple-of-ten predecessor. These are the only restrictions. Among $2^{18}$ words, the first bad type contributes $2^9$; the second contributes $8\cdot2^7$, since the block $BA^{10}$ has eight positions and cannot occur twice or coexist with the first bad type. Distinct legal inverse words have distinct starting integers because the forward map is deterministic. Thus $m=2^{18}-2^9-8\cdot2^7=2^9\cdot509$, and $509$ is prime. The answer is $511$.

**Answer:** 511.

**Methods:** inverse processes, forbidden patterns, injectivity.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2004 AIME II Problem 2: Matching unordered color profiles

From ten red and ten blue candies, one person draws two and then a second draws two without replacement. The probability that their unordered color combinations agree is reduced $m/n$. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

There are $\binom{20}{2}\binom{18}{2}$ equally likely ordered pairs of disjoint two-candy sets. Two monochromatic draws contribute $2\binom{10}{2}\binom82$ favorable cases. Two mixed draws contribute $10^2\cdot9^2$. Therefore $P=[2\binom{10}{2}\binom82+8100]/[\binom{20}{2}\binom{18}{2}]=118/323$, giving $441$.

**Answer:** 441.

**Methods:** conditional probability, combinations.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2004 AIME II Problem 3: Hidden cubes

A rectangular block made of unit cubes has exactly $231$ cubes invisible when three mutually adjacent faces are viewed. Find the least possible total number of cubes.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

For side lengths $a+1,b+1,c+1$, the unseen block has dimensions $a,b,c$, so $abc=231$. Assume $a\le b\le c$. Then $a\le\sqrt[3]{231}<7$, hence $a=1$ or $3$. If $a=1$, the possibilities $(b,c)=(1,231),(3,77),(7,33),(11,21)$ have minimum total $2\cdot12\cdot22=528$. If $a=3$, the only ordered possibility with $b\ge3$ is $(b,c)=(7,11)$, giving $4\cdot8\cdot12=384$.

**Answer:** 384.

**Methods:** finite case analysis, geometry hybrid.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** The first archived source asserts that balancing factors minimizes the product without proving the discrete case. Explicit factor enumeration here justifies the minimum.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2004 AIME II Problem 4: At most two decimal symbols

Count positive integers below $10000$ whose decimal expansions use at most two distinct digits.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

For each length $\ell=1,2,3,4$, single-symbol numbers contribute $9$. Choosing two nonzero digits contributes $\binom92(2^\ell-2)$. Choosing zero and a nonzero digit contributes $9(2^{\ell-1}-1)$, since the first digit is forced nonzero and a zero must occur. Summing gives $36+36\cdot22+9\cdot11=927$.

**Answer:** 927.

**Methods:** digit counting, inclusion exclusion.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2004 AIME II Problem 8: Divisor counts as exponent allocations

How many divisors of $2004^{2004}$ have exactly $2004$ positive divisors?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Write a divisor as $2^a3^b167^c$. The divisor-count condition is $(a+1)(b+1)(c+1)=2004=2^2\cdot3\cdot167$. Allocate the two factors of $2$ among three labeled slots in $\binom42=6$ ways and allocate each other prime in three ways. All resulting exponents are at most $2003$, so the original upper bounds are automatic. The answer is $6\cdot3\cdot3=54$.

**Answer:** 054.

**Methods:** stars and bars, multiplicative counting.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2004 AIME II Problem 10: Two binary ones modulo nine

Choose uniformly an integer below $2^{40}$ with exactly two binary ones. Find numerator plus denominator of the probability that it is divisible by $9$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Write the integer uniquely as $2^a+2^b$, $0\le a<b<40$. Since the order of $2$ modulo $9$ is $6$ and $2^3\equiv-1$, divisibility is equivalent to $b-a\equiv3\pmod6$. The favorable count is $37+31+25+19+13+7+1=133$, out of $\binom{40}{2}=780$. The fraction is reduced, so the answer is $913$.

**Answer:** 913.

**Methods:** binary digits, residue classes, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 2: A residue of minus one modulo nine is mistyped as plus one in the exponent classification.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2004 AIME II Problem 14: Distinct digit lengths of a sum

A string of $n$ sevens is split into decimal integers by inserting plus signs. How many values of $n$ can give a total of $7000$?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Only blocks of lengths one, two, three can occur. If their counts are $a,b,c$, then $a+11b+111c=1000$ and $n=a+2b+3c=1000-9k$, where $k=b+12c$. For fixed $k$, cost $11b+111c=11k-21c$ is minimized at $c=\lfloor k/12\rfloor$, $b=k\bmod12$. Thus feasibility is exactly $111\lfloor k/12\rfloor+11(k\bmod12)\le1000$. For $0\le k\le111$, all work except $107,109,110,111$; values $k>111$ give $n\le0$. Hence there are $112-4=108$ lengths.

**Answer:** 108.

**Methods:** projection of integer solutions, greedy optimization.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: One displayed three-digit value is miscomputed. The transformation interpretation also requires careful treatment of overlapping occurrences.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2004 AIME II Problem 15: Track a layer through folds

A strip of $1024$ numbered unit squares is repeatedly folded right half over left until one stack remains. How many squares lie below the square originally numbered $942$ from the left?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Use zero-based horizontal position $p=941$ and layer index $b=0$ counted from the bottom. Initially strip length $L=1024$ and stack height $h=1$. At each fold, if $p<L/2$ leave $p,b$ unchanged; otherwise replace $p$ by $L-1-p$ and $b$ by $2h-1-b$, because the right stack reverses and lands above the left. Then set $L\leftarrow L/2$, $h\leftarrow2h$. Ten applications give $b=593$. The update explicitly tracks every reversal, so this is precisely the number below the target.

**Answer:** 593.

**Methods:** invariants, recursive permutations.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2005 AIME I Problem 3: Exactly three small proper divisors

How many positive integers have exactly three positive proper divisors, all less than 50?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

Exactly three proper divisors means four divisors in total, so the integer is either $p^3$ or pq for distinct primes p,q. In the cube case the largest proper divisor is $p^2<50$, allowing $p=2,3,5,7$, hence four integers. In the pq case both primes must be below 50. The fifteen such primes are $2,3,5,7,11,13,17,19,23,29,31,37,41,43,47$, giving $\binom{15}{2}=105$ products. The cases are disjoint, so the total is $109$.

**Answer:** 109.

**Methods:** divisor patterns, prime counting.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source was reviewed. Its prime-power classification, prime list, and unordered pair count are complete.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2005 AIME I Problem 5: Coin colors and orientations separate

Stack four identical gold coins and four identical silver coins. Each has a marked face, and adjacent marked faces may not face each other. Count distinct stacks, including orientations.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Choose the four gold positions in $\binom84=70$ ways. Reading upward, a forbidden contact is an upward-facing mark immediately followed by a downward-facing mark. Thus all downward-facing coins precede all upward-facing coins. The switch has nine possible locations, including the two constant orientations. Color and orientation choices are independent, giving $70\cdot9=630$.

**Answer:** 630.

**Methods:** product principle, forbidden patterns.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 2: The intuition paragraph lists nine coins rather than the eight in the problem; the preceding recurrence gives the correct result.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2005 AIME I Problem 9: Local exposure types in a random cube

Each of $27$ unit cubes has four painted faces, with its two unpainted faces adjacent. Orient them independently uniformly in a $3\times3\times3$ cube. If the probability that the outer surface is painted is $p^a/(q^b r^c)$ in prime form, find $a+b+c+p+q+r$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

The interior cube is unrestricted. Each of six face-center cubes succeeds with probability $4/6=2/3$. Each of twelve edge cubes exposes a pair of adjacent faces: five of the twelve possible pairs are both painted, giving $5/12$. Each of eight corner cubes exposes three incident faces; two of eight such triples are fully painted, giving $1/4$. Independence gives $(2/3)^6(5/12)^{12}(1/4)^8=5^{12}/(2^{34}3^{18})$. The requested sum is $74$.

**Answer:** 074.

**Methods:** local types, product probability, geometric incidence.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2005 AIME I Problem 12: Parity changes only at squares

Let $S(n)=\sum_{k=1}^n\tau(k)$, where $\tau$ counts positive divisors. Among $1\le n\le2005$, let $a$ and $b$ count odd and even values of $S(n)$. Find $|a-b|$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Pair divisors $d$ and $k/d$: $\tau(k)$ is odd exactly for squares. Therefore $S(n)\equiv\lfloor\sqrt n\rfloor\pmod2$. Its odd blocks are $[(2j-1)^2,(2j)^2-1]$ for $1\le j\le22$, of lengths $4j-1$. Their total is $a=\sum_{j=1}^{22}(4j-1)=990$, so $b=1015$ and $|a-b|=25$.

**Answer:** 025.

**Methods:** parity, involutions, block counting.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2005 AIME I Problem 13: Diagonal separators in lattice paths

Count paths from $(0,0)$ to $(5,5)$ with steps $(1,0),(0,1),(1,1)$ and with no consecutive horizontal and vertical steps in either order.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

If there are $d$ diagonal steps, the $d+1$ gaps between them contain only horizontal steps, only vertical steps, or nothing. Their generating function is $G(x,y)=1+x/(1-x)+y/(1-y)$. The count for this $d$ is $[x^{5-d}y^{5-d}]G^{d+1}$. For $d=0,1,2,3,4,5$ these coefficients are $0,2,18,42,20,1$. Summing gives $83$. The separator decomposition is unique, so neither empty gaps nor long runs create overcounting.

**Answer:** 083.

**Methods:** generating functions, gaps, lattice paths.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2005 AIME II Problem 1: A binomial ratio determines deck size

A deck with $n\ge6$ distinct cards has six times as many six-card subsets as three-card subsets. Find $n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

Cancel factorials in $\binom n6=6\binom n3$ to obtain $(n-3)(n-4)(n-5)=720$. The left side increases strictly for $n\ge6$. Since $10\cdot9\cdot8=720$, the unique solution is $n=13$.

**Answer:** 013.

**Methods:** binomial coefficients.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2005 AIME II Problem 2: Three balanced meal bags

There are three rolls of each of three types. Randomly divide them into three labeled bags of size three. Find numerator plus denominator of the probability that every bag contains all three types.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

The first bag is balanced with probability $3^3/\binom93=9/28$. Given this, the second is balanced with probability $2^3/\binom63=2/5$; the third is then forced. Thus the probability is $9/70$ and the answer is $79$. Distinguishing physical rolls during counting avoids an unequal sample space.

**Answer:** 079.

**Methods:** conditional probability, balanced allocation.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2005 AIME II Problem 4: Union of divisor sets

Count positive integers dividing at least one of $10^{10},15^7,18^{11}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

The three divisor sets have sizes $121,64,276$. Intersections are divisor sets of gcds, so their pairwise sizes are $8,11,8$, and their triple intersection is $\{1\}$. Inclusion-exclusion yields $121+64+276-8-11-8+1=435$.

**Answer:** 435.

**Methods:** inclusion exclusion, divisor sets.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2005 AIME II Problem 6: Fixed points of a shuffle

A stack labeled $1,\ldots,2n$ top to bottom is cut into two equal halves. Restack by alternately placing the next card from the lower half and then the upper half on top. At least one card from each half stays fixed, including card $131$. Find $2n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

A card $j\le n$ from the upper half ends at position $2(n-j)+1$ from the top; a card $n+j$ from the lower half ends at position $2(n-j)+2$. Since $131$ is odd it must be from the upper half, and $131=2(n-131)+1$ gives $n=196$. The lower-half fixed-point equation $n+j=2(n-j)+2$ then gives $j=66$, valid. Thus the required stack has $392$ cards.

**Answer:** 392.

**Methods:** permutations, fixed points.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2006 AIME I Problem 2: No gaps among fixed-size subset sums

How many different sums can a $90$-element subset of $\{1,\ldots,100\}$ have?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

The minimum and maximum are $4095$ and $4995$. Every intermediate sum occurs: write its excess over $4095$ as $90q+r$, $0\le r<90$. Add $q$ to the first $90-r$ entries of $(1,\ldots,90)$ and $q+1$ to the last $r$ entries. The result remains strictly increasing and at most $100$; at the endpoint use $q=10,r=0$. Thus the number is $4995-4095+1=901$.

**Answer:** 901.

**Methods:** subset sums, constructive intervals.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2006 AIME I Problem 6: Uniform digit contributions

Sum all repeating decimals $0.\overline{abc}$ with three distinct decimal digits, allowing $a=0$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

There are $10\cdot9\cdot8=720$ digit strings. In any fixed position each digit occurs $9\cdot8=72$ times. Since $0.\overline{abc}=(100a+10b+c)/999$, the sum is $72(0+\cdots+9)(100+10+1)/999=360$. Distinct triples represent distinct values here.

**Answer:** 360.

**Methods:** contribution counting, digit symmetry.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2006 AIME I Problem 11: Insert the largest block

Permute blocks of sizes $1,\ldots,8$ bottom to top, requiring every size to be at most two greater than the size immediately below. Find the count modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

For a valid arrangement of $1,\ldots,m$, insert $m+1$ either at the bottom, immediately above $m$, or immediately above $m-1$. These are exactly its three possible positions when $m\ge2$. Removing the largest block preserves validity: if it had a predecessor, that predecessor was at least $m-1$, so the new successor is still allowed. Thus the insertion is bijective and $T_8=T_2\cdot3^6=2\cdot3^6=1458$. The residue is $458$.

**Answer:** 458.

**Methods:** insertion bijections, recurrences.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2006 AIME I Problem 13: Valuation layers

For even $x$, let $g(x)$ be the largest power of two dividing $x$. Set $S_n=\sum_{k=1}^{2^{n-1}}g(2k)$. Find the greatest $n<1000$ for which $S_n$ is a square.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

For $1\le j<n$, exactly $2^{n-j-1}$ terms have $g=2^j$; the final term has $g=2^n$. Hence $S_n=(n-1)2^{n-1}+2^n=2^{n-1}(n+1)$. If $n$ is even, its exponent of two is odd, impossible. If $n$ is odd, $2^{n-1}$ is a square and we need $n+1$ to be a square. The largest even square at most $1000$ is $30^2=900$, so $n=899$.

**Answer:** 899.

**Methods:** contribution counting, valuation layers.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: The recurrence is valid with n at least two and S_1=2; the written artificial S_0=1 is not compatible with the actual definition. Source 2: The recurrence is explicitly guessed without proof, and smallest/largest language is reversed. A valuation count proves the formula directly. Source 3: The closing least/greatest wording and a summation index are mistyped; the valuation argument otherwise works.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2006 AIME I Problem 15: A telescoping potential

Start with $x_0=0$ and choose $x_k$ subject to $|x_k|=|x_{k-1}+3|$. Find the minimum of $|x_1+\cdots+x_{2006}|$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Let $b_k=x_k/3$, so $b_k^2=(b_{k-1}+1)^2$. Summing this identity gives $\sum_{k=1}^{2006}b_k=((b_{2006}+1)^2-2007)/2$. Every $b_k$ is integral. The nearest integer square to $2007$ is $2025$, so the absolute sum is at least $9$. Attain it by alternating $-1,0$ through time $1962$, then taking $44$ successive increments to finish at $b_{2006}=44$. Multiplying by three gives $27$.

**Answer:** 027.

**Methods:** invariants, telescoping, extremal construction.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 2: The proposed attaining sequence alternates two positive values that do not satisfy the recurrence. The telescoping lower bound is valid, but a different construction is necessary. Source 3: The exhibited construction gives the answer but does not prove that a smaller absolute sum is impossible.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2006 AIME II Problem 4: A permutation with one valley

Count permutations of $1,\ldots,12$ satisfying $a_1>\cdots>a_6<a_7<\cdots<a_{12}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

The valley must be the global minimum, so $a_6=1$. Choose the five values to its left in $\binom{11}{5}$ ways. Their descending order and the ascending order of the remaining six values are forced. This bijection gives $462$.

**Answer:** 462.

**Methods:** bijections, permutations.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2006 AIME II Problem 5: Opposite-face bias

A die assigns probability $1/6+t$ to a face, $1/6-t$ to its opposite, and $1/6$ to the four others; opposite labels sum to seven. Two independent such dice sum to seven with probability $47/288$. Find numerator plus denominator of the larger face probability.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

The sum-seven probability is $4/36+2(1/6+t)(1/6-t)=1/6-2t^2$. Thus $2t^2=1/288$, so $t=1/24$. The larger face probability is $5/24$, giving $29$.

**Answer:** 029.

**Methods:** probability, symmetry.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2006 AIME II Problem 7: Complementary decimal numbers

Count ordered positive integer pairs $(a,b)$ with $a+b=1000$ and no zero digit in either number.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

There are $999$ choices for $a$. Exclude the $99$ multiples of $10$, which also make $b$ end in zero. Among the rest, a zero can occur only in a genuine tens position: $a=101,\ldots,109;201,\ldots,209;\ldots;901,\ldots,909$, giving $81$ cases, and likewise $81$ for $b$. These two classes are disjoint because their complements have tens digit nine. Thus $999-99-81-81=738$.

**Answer:** 738.

**Methods:** complement, digit counting.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2006 AIME II Problem 8: Three corners modulo all permutations

Build an equilateral triangle from four congruent small equilateral triangles. Each may have one of six colors. Identify configurations under rotations and reflections. Count the resulting colorings.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

The center triangle is fixed by every symmetry and has six choices. The three corner positions are acted on by the full symmetric group $S_3$, so their orbit is determined exactly by the multiset of three colors. There are $\binom{6+3-1}{3}=56$ such multisets. The total is $6\cdot56=336$.

**Answer:** 336.

**Methods:** orbits, multisets.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2006 AIME II Problem 10: A one-point head start

Seven teams play each other once, with independent fair win-loss outcomes. Given that $A$ defeats $B$, find numerator plus denominator of the probability that $A$ finishes with more wins than $B$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Let $X,Y$ be their wins in the remaining five games each. The ten relevant games are distinct and independent, so $X,Y$ are independent $\mathrm{Bin}(5,1/2)$. We need $1+X>Y$, or $X\ge Y$. Symmetry gives probability $(1+P(X=Y))/2$. Vandermonde yields $P(X=Y)=\sum_k\binom5k^2/2^{10}=\binom{10}{5}/1024=63/256$. Thus $P=319/512$ and the answer is $831$.

**Answer:** 831.

**Methods:** symmetry, Vandermonde, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2006 AIME II Problem 13: Five representations by consecutive odd integers

How many integers $N<1000$ have exactly five representations as a sum of one or more consecutive positive odd integers, counting distinct sequence lengths?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

A length-$j$ sum beginning at $2t+1$ is $N=j(2t+j)$ with $t\ge0$. Thus representations correspond exactly to factor pairs $u\le v$ of $N$ with equal parity. For odd $N$, their number is $\lceil\tau(N)/2\rceil$; for $4\mid N$, it is $\lceil\tau(N/4)/2\rceil$; for $N\equiv2\pmod4$, it is zero. Five representations require a divisor count of $9$ or $10$. The possible exponent patterns are $p^8,p^2q^2,p^9,p^4q$ with distinct primes $p,q$. The pure prime powers exceed the relevant bounds. Odd $N<1000$ therefore give $225,441,405,567,891$. For $N/4<250$, the possibilities are $36,100,196,225,48,80,112,176,208,162$. The lists are exhaustive by the prime-power bounds in the two remaining patterns. Thus there are $5+10=15$ values.

**Answer:** 015.

**Methods:** divisor pairs, consecutive sums, prime exponent patterns.

**Verification:** Enumerated every consecutive positive odd sequence with sum below 1000, independently of divisor-count classification.

**Source comparison:** Both entries reviewed. Their lists are correct, but they omit mentioning the pure prime-power exponent patterns; the size bounds exclude those, as made explicit here.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2006 AIME II Problem 14: Reciprocal digit frequency

Let $S_n$ be the sum of reciprocals of all nonzero decimal digits appearing in $1,\ldots,10^n$. Find the least positive $n$ for which $S_n$ is integral.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Pad $0,\ldots,10^n-1$ to $n$ digits. Each nonzero digit appears $n10^{n-1}$ times, and $10^n$ contributes one extra $1$. Thus $S_n=1+n10^{n-1}H_9$. Since $H_9=7129/2520$ in lowest terms and $2520=2^3\cdot3^2\cdot5\cdot7$, integrality requires $63\mid n$. The candidate $n=63$ supplies all the factors of two and five as well, so it is minimal.

**Answer:** 063.

**Methods:** contribution counting, digit frequency.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2007 AIME I Problem 5: A periodic rounding map

Convert an integer Fahrenheit temperature in $[32,1000]$ to Celsius using $C=5(F-32)/9$, round to the nearest integer, convert back, and round again. Count temperatures recovered exactly.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Write $F-32=9q+r$, $0\le r<9$. The round trip depends only on $r$ and sends it to $\operatorname{round}((9/5)\operatorname{round}(5r/9))$. Checking the nine residues yields the fixed set $\{0,2,4,5,7\}$. The range $0\le F-32\le968$ contains $107$ complete nine-blocks and the residues $0,\ldots,5$ of one last block. Hence the count is $107\cdot5+4=539$. No half-integer rounding ambiguity occurs.

**Answer:** 539.

**Methods:** residue classes, finite states.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2007 AIME I Problem 6: Next-multiple walks

From an integer position a frog jumps to the next larger multiple of $3$ or of $13$. Count distinct coordinate sequences from $0$ to $39$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

Use an acyclic graph on $0,3,6,\ldots,39,13,26$. At each vertex connect to the distinct next multiples, discarding values above $39$. Starting with $D(0)=1$, add $D(v)$ to each successor. In increasing vertex order the nonzero counts are $D(3)=D(6)=D(9)=D(12)=1$, $D(13)=5$, $D(15)=D(18)=D(21)=D(24)=6$, $D(26)=29$, $D(27)=D(30)=D(33)=D(36)=35$, and $D(39)=169$. At $36$ the two next multiples coincide, so that edge is counted once.

**Answer:** 169.

**Methods:** acyclic paths, dynamic programming.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 4: Several intermediate backward-recurrence equalities have incorrect indices or duplicated terms, although the final recurrence values are correct.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2007 AIME I Problem 10: Binary matrices with fixed margins

A $6\times4$ binary matrix has two ones in every row and three in every column. Find the number of such matrices modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

Choose the three rows containing a one in the first column in $\binom63=20$ ways. In these rows, the second ones occupy the last three columns with occupancy types $(3,0,0),(2,1,0),(1,1,1)$. The first type gives $3$ completions. The second gives $3\cdot2\cdot3=18$ top choices and three bottom completions, totaling $54$. The third gives $3!=6$ top choices and $3!=6$ bottom completions, totaling $36$. Hence the count is $20(3+54+36)=1860$, giving $860$.

**Answer:** 860.

**Methods:** fixed margins, occupancy.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 5: The initial normalization multiplier and the final multiplier disagree; the asserted normalization needs a uniform-fiber argument. Source 6: One case refers to column four when the calculation concerns the first three columns.

**Archived alternatives reviewed:** 8 of 8. Indices in the data are zero-based.

**Status:** solved.

## 2007 AIME I Problem 11: Rounding square roots in blocks

For each positive integer $p$, let $b(p)$ be its square root rounded to the nearest integer. Find $\sum_{p=1}^{2007}b(p)\pmod{1000}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

We have $b(p)=k$ precisely for $k^2-k+1\le p\le k^2+k$, a block of $2k$ integers. Blocks $k=1,\ldots,44$ are complete; $p=1981,\ldots,2007$ contributes $27$ copies of $45$. Thus the sum is $2\sum_{k=1}^{44}k^2+27\cdot45=59955$, whose residue is $955$.

**Answer:** 955.

**Methods:** block counting, weighted sums.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2007 AIME II Problem 1: A repeated symbol in a license string

Form five-character strings from the multiset $\{A,I,M,E,2,0,0,7\}$ without exceeding any multiplicity. If the count is $N$, find $N/10$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

Strings with at most one zero are ordinary selections without replacement from seven distinct symbols, counted by $(7)_5=2520$. For exactly two zeros, choose their positions and order three of the other six symbols: $\binom52(6)_3=1200$. Hence $N=3720$ and $N/10=372$.

**Answer:** 372.

**Methods:** multiset permutations, case analysis.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2007 AIME II Problem 2: Divisibility becomes a composition

Count ordered positive triples $(a,b,c)$ with $a\mid b$, $a\mid c$, and $a+b+c=100$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

Write $b=ax,c=ay$ with $x,y\ge1$. For each divisor $d=100/a\ge3$, the condition is $x+y=d-1$, with $d-2$ solutions. Therefore the count is $\sum_{d\mid100,d\ge3}(d-2)=2+3+8+18+23+48+98=200$.

**Answer:** 200.

**Methods:** compositions, divisor decomposition.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2007 AIME II Problem 5: Grid cells below a rational line

Count unit grid squares whose interiors lie in the first quadrant and below $9x+223y=2007$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

The intercept rectangle has $223\cdot9=2007$ cells. Its diagonal crosses $223+9-\gcd(223,9)=231$ cells: one initial cell and one new cell for each interior grid-line crossing. Since the intercepts are coprime, no interior horizontal and vertical crossings coincide. Half of the remaining cells lie on each side by central symmetry. Thus the answer is $(2007-231)/2=888$.

**Answer:** 888.

**Methods:** lattice geometry, symmetry.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2007 AIME II Problem 6: Uniform indegrees in a digit graph

Count four-digit integers such that an odd digit is followed by a larger digit and an even digit by a smaller digit.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

The first three digits cannot be $0$ or $9$, because those have no legal successor. For each target digit $d\in\{1,\ldots,8\}$, exactly four digits of $\{1,\ldots,8\}$ can precede it: smaller odds or larger evens. Thus every allowed second digit has four prefixes, and every allowed third digit has sixteen. Each final digit $0,\ldots,9$ also has exactly four allowed predecessors, so has $64$ full strings. The total is $10\cdot64=640$.

**Answer:** 640.

**Methods:** finite states, digit graphs.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2007 AIME II Problem 8: Optimizing a rectangular grid

Draw full lines parallel to the sides of a $4\times5$ sheet, with total drawn length $2007$. Basic rectangles must have four drawn sides and no drawn line inside. Find the maximal number modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

With $h$ lines of length $5$ and $v$ of length $4$, we have $5h+4v=2007$ and $(h-1)(v-1)$ basic rectangles. Thus $h\equiv3\pmod4$ and the objective is the concave quadratic $(h-1)(2003-5h)/4$, centered at $h=1004/5$. The two nearest permissible values are $199,203$, giving $49896$ and $49894$. Concavity excludes all others. The answer is $896$.

**Answer:** 896.

**Methods:** grid counting, discrete optimization.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2007 AIME II Problem 10: Containment in a set or its complement

Independently choose uniform subsets $A,B$ of a six-element set. The probability that $B\subseteq A$ or $B\subseteq A^c$ is $m/n^r$ in reduced prime-denominator form. Find $m+n+r$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

For $B\subseteq A$, each element has three allowed membership pairs out of four; hence probability $(3/4)^6$. The complementary containment has the same probability. Both occur precisely when $B$ is empty, of probability $2^{-6}$. Inclusion-exclusion gives $2(3/4)^6-2^{-6}=697/2^{11}$, yielding $710$.

**Answer:** 710.

**Methods:** elementwise encoding, inclusion exclusion, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2007 AIME II Problem 13: Pascal propagation modulo three

Place eleven binary digits in the bottom row of a triangular array. Each upper entry is the sum of its two children. Count assignments making the top entry divisible by $3$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

The top is $\sum_{j=0}^{10}\binom{10}{j}x_j$, by Pascal's identity or path counting. Modulo three, $(1+t)^{10}\equiv(1+t^9)(1+t)$, so only coefficients $j=0,1,9,10$ survive, each equal to one. Their sum must be zero or three, giving $\binom40+\binom43=5$ choices. The other seven bits are free, so the answer is $5\cdot2^7=640$.

**Answer:** 640.

**Methods:** binomial propagation, modular generating functions.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2008 AIME I Problem 6: Summing an arithmetic row repeatedly

The top row is $1,3,\ldots,99$. Each row below sums adjacent entries until one remains. Count all entries divisible by $67$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

At row $r$ and position $k$, with $1\le r\le50$ and $1\le k\le51-r$, induction gives $a_{r,k}=2^{r-1}(r+2k-2)$. The parenthetical factor lies between $r$ and $100-r$, so divisibility by $67$ means it equals $67$. This has exactly one integral $k$ for each odd $r\le33$ and none otherwise. There are $17$ such rows.

**Answer:** 017.

**Methods:** recurrences, binomial propagation.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2008 AIME I Problem 7: Occupied hundred-blocks

For $0\le i\le999$, let $S_i=\{100i,\ldots,100i+99\}$. How many of these sets contain no perfect square?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

The first $26$ blocks $S_0,\ldots,S_{25}$ all contain squares: up to $50^2$, consecutive square gaps are at most $99$, and $50^2$ lies in $S_{25}$. Above $50^2$, successive squares differ by more than $100$, so $51^2,\ldots,316^2$ occupy $266$ new distinct blocks. These are all squares below $100000$. Hence $1000-26-266=708$ blocks are empty.

**Answer:** 708.

**Methods:** complement, gap bounds.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2008 AIME I Problem 9: Random crate heights

Ten independent crates have heights $3,4,6$ with equal probabilities. The probability their total height is $41$ is reduced $m/n$. Find $m$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Let counts be $a,b,c$. Subtracting $3(a+b+c)=30$ from the height equation gives $b+3c=11$. The admissible triples are $(1,8,1),(3,5,2),(5,2,3)$. Therefore $P=[10!/(1!8!1!)+2\cdot10!/(3!5!2!)]/3^{10}=5130/59049=190/2187$. Thus $m=190$.

**Answer:** 190.

**Methods:** multinomial coefficients, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2008 AIME I Problem 11: Parity restrictions on runs

Count length-$14$ words on $\{A,B\}$ with every maximal $A$-run even and every maximal $B$-run odd.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Let $a_n,b_n$ count legal words ending in $A,B$. Removing two terminal $A$'s gives $a_n=a_{n-2}+b_{n-2}$. A terminal odd $B$-run has length one (append $B$ to an $A$-ending word) or at least three (remove two $B$'s), giving $b_n=a_{n-1}+b_{n-2}$. Start from $(a_1,b_1)=(0,1)$ and $(a_2,b_2)=(1,0)$. The recurrence for $n\ge3$ gives $(a_{14},b_{14})=(80,92)$, totaling $172$.

**Answer:** 172.

**Methods:** runs, recurrences.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 3: The final displayed sum omits the second singleton case; the stated total includes it.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2008 AIME I Problem 12: Maximum traffic through a fixed point

All cars are $4$ meters long and travel at common speed $v>0$ km/h. The gap behind each car is exactly $4\lceil v/15\rceil$ meters. A roadside detector counts passing cars for one hour. Over all speeds and initial placements, let $M$ be the largest possible whole count. Find the integer quotient $M/10$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Put $n=\lceil v/15\rceil$. Consecutive fronts cross at intervals $\delta=4(n+1)/(1000v)\ge(n+1)/(3750n)>1/3750$ hours. Thus $3751$ crossings would span $3750\delta>1$ hour and are impossible. Conversely choose $v=15n$ with $n=3750$. Then $3749\delta=3749\cdot3751/(3750^2)<1$, so an initial phase places $3750$ consecutive crossings strictly within the hour. Therefore $M=3750$, and the requested quotient is $375$.

**Answer:** 375.

**Methods:** interval packing, ceiling functions, throughput.

**Verification:** Exact crossing-span check for the attaining finite speed; the analytic headway bound excludes 3751 at every speed.

**Source comparison:** All three entries reviewed. The first recognizes the endpoint-count issue, though it phrases it using partial units. The second omits car length from the headway; the third uses floor instead of ceiling for nonmultiple speeds. The exact crossing-span proof resolves these ambiguities.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2008 AIME II Problem 10: Increasing distances on a small grid

On the sixteen points $\{0,1,2,3\}^2$, a path visits distinct points with strictly increasing successive distances. Let $m$ be its maximum number of points and $r$ the number of paths attaining that maximum. Find $mr$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

The only squared distances are $1,2,4,5,8,9,10,13,18$, so $m\le10$. Reverse a maximal path. Up to eight square symmetries its first three points are $(0,0),(3,3),(1,0)$. The required remaining squared lengths force $(2,3),(2,0),(0,2),(2,1),(0,1),(1,2)$; alternatives at each stage either repeat a vertex or prevent the next required length. The final unit step has three choices: $(1,1),(2,2),(1,3)$. Thus ten-point paths exist and $r=8\cdot3=24$, giving $240$.

**Answer:** 240.

**Methods:** extremal paths, symmetry, finite enumeration.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2008 AIME II Problem 12: A separator that behaves like a blue flag

Distribute ten identical blue and nine identical green flags onto two labeled nonempty flagpoles, with vertical order relevant and no adjacent greens on either pole. Find the arrangement count modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Insert one extra distinguished blue separator between the poles. The eleven blue positions create twelve gaps, of which nine receive a green. Choose the distinguished blue among eleven positions, giving $11\binom{12}{9}$. An empty pole occurs when the separator is at an end with no green outside it; each side contributes $\binom{11}{9}$. Thus $N=11\binom{12}{9}-2\binom{11}{9}=2310$, whose residue is $310$.

**Answer:** 310.

**Methods:** gaps, separators, bijections.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 3: The summation index is written as n while the summand and bounds use b. The Vandermonde evaluation is valid after this correction.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2009 AIME I Problem 3: Cancel symmetric binomial coefficients

Eight independent coin flips have head probability $p$. The chance of three heads is one twenty-fifth of the chance of five heads. Find numerator plus denominator of $p$ in lowest terms.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

The equal binomial coefficients cancel, leaving $(1-p)^2/p^2=1/25$. Since $0<p<1$, take the positive square root: $(1-p)/p=1/5$. Thus $p=5/6$ and the answer is $11$.

**Answer:** 011.

**Methods:** binomial probability.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2009 AIME I Problem 8: Sum of pairwise differences

Sum all positive differences between pairs from $\{1,2,4,\ldots,2^{10}\}$, and report the remainder modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

The value $2^k$ occurs positively in $k$ differences and negatively in $10-k$, so the sum is $\sum_{k=0}^{10}(2k-10)2^k=16398$. (Use $\sum2^k=2047$ and $\sum k2^k=18434$.) Distinct pairs yield distinct differences because the exact power of two dividing the difference identifies the smaller exponent. The residue is $398$.

**Answer:** 398.

**Methods:** contribution counting, weighted sums.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2009 AIME I Problem 9: Three prices from seven digits

Form an ordered triple of positive prices at most $9999$ using exactly four digits $1$ and three digits $3$ in total. Count possible triples.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Concatenate the three prices. There are $\binom73=35$ possible digit strings. Split into three positive lengths summing to seven: $\binom62=15$ cuts, but reject lengths $(5,1,1)$ and its three placements, leaving twelve. There are no leading-zero issues. The encoding is bijective, so the count is $35\cdot12=420$.

**Answer:** 420.

**Methods:** separator encoding, bounded compositions.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2009 AIME I Problem 10: Cyclic species runs

Arrange five distinct members of each of three species around fifteen numbered seats. Seat $1$ is $M$, seat $15$ is $E$, and allowed changes clockwise are only $M\to V\to E\to M$. If the count is $N(5!)^3$, find $N$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

After ignoring identities within each species, every admissible word is $k$ successive nonempty runs of each type in the repeated order $M,V,E$, with $1\le k\le5$. Split each species' five occurrences into $k$ positive run lengths independently: $\binom4{k-1}^3$ choices. Thus $N=\sum_{k=1}^{5}\binom4{k-1}^3=1+64+216+64+1=346$. The fixed first and last species remove any cyclic-cut ambiguity.

**Answer:** 346.

**Methods:** runs, compositions, cyclic words.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2009 AIME I Problem 11: Integral triangle areas on a line

Choose distinct nonnegative lattice points $P,Q$ on $41x+y=2009$. Count triangles $OPQ$ of positive integer area, where $O=(0,0)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Write the two x-coordinates as $u,v\in\{0,\ldots,49\}$. Their determinant is $2009(u-v)$, so the area is integral exactly when $u,v$ have the same parity. Each parity class contains $25$ values. Every distinct pair yields positive area, hence the count is $2\binom{25}{2}=600$.

**Answer:** 600.

**Methods:** parity, geometry hybrid.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 2: The inference that the base is an integral multiple of twice the primitive lattice length requires the lattice-spacing condition; integrality of area alone is insufficient.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2009 AIME I Problem 14: Minimizing a second moment with fixed first and fourth moments

A sequence of $350$ entries, each in $\{1,2,3,4\}$, satisfies $\sum a_i=513$ and $\sum a_i^4=4745$. Find the smallest possible $\sum a_i^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Let $w,x,y,z$ count the entries equal to $1,2,3,4$. Subtracting the count equation from the two moment equations gives $x+2y+3z=163$ and $15x+80y+255z=4395$. Eliminating $x$ gives $5y+21z=195$. Thus $z\equiv0\pmod5$ and $0\le z\le9$, so $(y,z)$ is $(39,0)$ or $(18,5)$. These give $(w,x)=(226,85)$ or $(215,112)$ respectively. Their second moments are $917$ and $905$, so the minimum is $905$, attained by the latter frequencies.

**Answer:** 905.

**Methods:** frequency variables, integer optimization, moments.

**Verification:** Enumerated every feasible frequency vector using the count and moment constraints, and minimized the second moment.

**Source comparison:** The sole source correctly reduces the constraints to two feasible frequency vectors. The explicit second moments here certify which is minimal.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2009 AIME II Problem 6: At least one consecutive pair

Count five-element subsets of $\{1,\ldots,14\}$ containing consecutive integers, and give the residue modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

For a subset $x_1<\cdots<x_5$ with no consecutive elements, subtract $0,1,2,3,4$ from successive entries. This is a bijection to five-element subsets of $\{1,\ldots,10\}$. Complementary counting gives $\binom{14}{5}-\binom{10}{5}=1750$, hence $750$.

**Answer:** 750.

**Methods:** gap compression, complement.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 2: The examples motivate the gap reduction but do not by themselves prove a bijection; rank compression supplies the missing argument. Source 3: The final total-subset binomial coefficient is mistyped.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2009 AIME II Problem 8: Nearby geometric stopping times

Two people independently roll fair dice until the first six. Find numerator plus denominator of the probability that their numbers of rolls differ by at most one.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Put $q=5/6$. The probability that the first person needs at least two more rolls than the second is $\sum_{t\ge1}(1-q)q^{t-1}q^{t+1}=(1-q)q^2/(1-q^2)=25/66$. The opposite discrepancy has the same probability and is disjoint. Hence the required probability is $1-2(25/66)=8/33$, giving $41$.

**Answer:** 041.

**Methods:** geometric series, complement, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 2: In the first-roll case, a success factor is mistyped as a failure factor. The subsequent numerical contribution uses the correct probability.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2009 AIME II Problem 9: An injection leaves two boundary slices

Let $m,n$ count positive integer solutions to $4x+3y+2z=2009$ and $4x+3y+2z=2000$, respectively. Find $(m-n)\bmod1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Adding three to $y$ injects the second solution set into the first. In the first equation $y$ is odd, and the image consists exactly of solutions with $y\ge5$. The missing slices are $y=1$ and $y=3$. They give $2x+z=1003$ and $2x+z=1000$, with $501$ and $499$ positive solutions. Thus $m-n=1000$, giving $0$.

**Answer:** 000.

**Methods:** injections, boundary counting.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2009 AIME II Problem 12: Distinct pair sums with disjoint endpoints

Choose disjoint pairs of distinct elements from $\{1,\ldots,2009\}$, requiring all pair sums distinct and at most $2009$. Find the greatest number of pairs.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

For $k$ pairs, the total of their $2k$ endpoints is at least $k(2k+1)$, while the distinct sums total at most $k(4019-k)/2$. Thus $5k\le4017$, giving $k\le803$. Attain $803$ by pairing $2j+1$ with $1205-j$ for $0\le j\le401$, and $2j+2$ with $1606-j$ for $0\le j\le400$. These use each integer $1,\ldots,1606$ exactly once; the sums run without repetition from $1206$ through $2008$. Hence the maximum is $803$.

**Answer:** 803.

**Methods:** extremal sums, constructive matching.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2010 AIME I Problem 1: One square divisor in a pair

Choose two distinct positive divisors of $2010^2$ uniformly. Find numerator plus denominator of the probability that exactly one is a square.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

Since $2010=2\cdot3\cdot5\cdot67$, there are $3^4=81$ divisors, of which $2^4=16$ have all exponents even. The favorable unordered pairs number $16\cdot65$, so $P=1040/\binom{81}{2}=26/81$. The answer is $107$.

**Answer:** 107.

**Methods:** prime exponents, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2010 AIME I Problem 4: Collision probability of head counts

Two fair coins and one coin with head probability $4/7$ are flipped independently by each of two people. Find numerator plus denominator of the probability that their head counts agree.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

The head-count probability generating function is $(1+x)^2(3+4x)/28=(3+10x+11x^2+4x^3)/28$. For two independent copies, equality has probability equal to the sum of squared probabilities: $(3^2+10^2+11^2+4^2)/28^2=123/392$. The answer is $515$.

**Answer:** 515.

**Methods:** generating functions, collision probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: Two named two-head outcomes are assigned each other's probabilities; the total distribution remains correct.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2010 AIME I Problem 7: Exactly three pairwise intersection elements

Count ordered triples $(A,B,C)$ of subsets of a seven-element set such that each pairwise intersection has size one and the triple intersection is empty. Report the residue modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

The three intersection elements are distinct and occupy the labeled roles $AB,BC,CA$, giving $(7)_3=210$ choices. Each remaining element can lie in $A$ alone, $B$ alone, $C$ alone, or no set: four independent choices. Hence $N=210\cdot4^4=53760$, yielding $760$.

**Answer:** 760.

**Methods:** Venn regions, elementwise encoding.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2010 AIME I Problem 10: Digits allowed to carry

Count representations $2010=1000a_3+100a_2+10a_1+a_0$ with every integer $a_i$ between $0$ and $99$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

Choose $a_3,a_1$ first with $1000a_3+10a_1\le2010$. The remainder has a unique quotient and remainder on division by $100$, which supply $a_2,a_0$ within the permitted bounds. For $a_3=0,1$ all $100$ choices of $a_1$ work. For $a_3=2$ only $a_1=0,1$ work. Thus the count is $202$.

**Answer:** 202.

**Methods:** mixed radix, quotient remainder bijection.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 2: One congruence omits a division by ten, and the two exceptional ordered pairs are transposed/mistyped. Source 5: The multiple-of-ten condition belongs to a_0, not a_1. The regrouped place-value equation also omits a factor ten.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2010 AIME I Problem 12: A multiplicative two-color threshold

Find the least $m\ge3$ such that every two-coloring of $\{3,\ldots,m\}$ has a monochromatic solution $ab=c$, allowing $a=b$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

At $m=243$, color $3$ red. Avoiding monochromatic products forces $9$ blue, $81$ red, and $27$ blue (since $3\cdot27=81$). Then $243=3\cdot81=9\cdot27$ cannot have either color. For $m=242$, color $[3,8]\cup[81,242]$ red and $[9,80]$ blue. Products of two small red entries lie in $[9,64]$; any product using a large red entry exceeds $242$; products of two blue entries are at least $81$ and cannot be blue. Thus $243$ is sharp.

**Answer:** 243.

**Methods:** Ramsey theory, extremal coloring.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2010 AIME II Problem 2: Distance to the nearest side

Choose a point uniformly inside a unit square. Its distance to the nearest side is $d$. Find numerator plus denominator of $P(1/5\le d\le1/3)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

The event $d\ge t$ is a concentric square of side $1-2t$. Thus the desired area is $(3/5)^2-(1/3)^2=56/225$, and the answer is $281$.

**Answer:** 281.

**Methods:** continuous probability, complement.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: The two inner-square areas are attached to the wrong distance thresholds. Their difference is nevertheless computed correctly.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2010 AIME II Problem 3: Valuation of all pair differences

Let $K=\prod_{1\le a<b\le20}(b-a)$. Find the largest exponent $n$ for which $2^n\mid K$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

A difference $d$ occurs $20-d$ times. Count each factor of two by its level: $v_2(K)=\sum_{j=1}^{4}\sum_{1\le d\le19,\,2^j\mid d}(20-d)$. The four sums are $90,40,16,4$, totaling $150$. This avoids multiplying the large product.

**Answer:** 150.

**Methods:** valuation layers, contribution counting.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2010 AIME II Problem 4: A short gate change

Twelve gates are equally spaced $100$ feet apart. A traveler is assigned one uniformly, then reassigned uniformly to a different gate. Find numerator plus denominator of the probability of walking at most $400$ feet.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

An unordered pair at distance $100d$ has $12-d$ choices. For $d=1,2,3,4$, there are $11+10+9+8=38$ such pairs out of $\binom{12}{2}=66$. Thus $P=19/33$, giving $52$.

**Answer:** 052.

**Methods:** distance stratification, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2010 AIME II Problem 8: A set cannot contain its own size

Partition $\{1,\ldots,12\}$ into ordered nonempty sets $A,B$, requiring $|A|\notin A$ and $|B|\notin B$. Count the partitions.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Let $|A|=k$. For $k\ne6$, the element $k$ is forced into $B$ and the distinct element $12-k$ into $A$; choose the other $k-1$ elements of $A$ from the remaining ten. If $k=6$, the element $6$ would have to lie in neither part, impossible. Therefore the count is $\sum_{k=1}^{11}\binom{10}{k-1}-\binom{10}{5}=1024-252=772$.

**Answer:** 772.

**Methods:** forced choices, binomial identities.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: The varying forced and forbidden elements cannot be treated as one fixed ten-element sample space without explanation. Sum the fixed-size binomial counts to justify the same result.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2010 AIME II Problem 10: Quadratics modulo interchange of roots

Count quadratic polynomials with integer coefficients and integer roots whose constant coefficient is $2010$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Write $f(x)=a(x-r)(x-s)$, so $ars=2010$. Since $2010$ has four distinct prime factors, assigning each prime to $|a|,|r|,|s|$ gives $3^4$ ordered magnitude triples. There are four sign assignments with positive product, hence $324$ ordered signed triples. Swapping $r,s$ leaves the polynomial unchanged and fixes exactly two triples, with $r=s=1$ or $r=s=-1$ and $a=2010$. Burnside gives $(324+2)/2=163$.

**Answer:** 163.

**Methods:** Burnside lemma, prime allocations.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2010 AIME II Problem 11: Tic-tac-toe line counts

Count $3\times3$ binary boards with five ones and four zeros such that at most one row, column, or long diagonal is monochromatic.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

There are $\binom95=126$ boards. If each color has a monochromatic line, the two lines must be parallel rows or parallel columns. Choose their color-labeled locations in $3\cdot2$ ways and the extra zero in the remaining line in three ways: $36$ boards. If only ones have multiple lines, exactly two intersecting lines use all five ones. The pairs are row-column ($9$), row/column-diagonal ($12$), or two diagonals ($1$), giving $22$. Four zeros cannot form two lines, and these bad cases are disjoint. Thus $126-36-22=68$.

**Answer:** 068.

**Methods:** complement, line incidence.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2010 AIME II Problem 13: Two fixed cards share a rank team

Four people draw distinct uniform cards from $1,\ldots,52$ and the two lowest form one team. Two specified people hold $a,a+9$. Among choices with their same-team probability at least $1/2$, find numerator plus denominator of the smallest probability.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

The other two cards must both lie below $a$ or both above $a+9$. Hence $p(a)=[\binom{a-1}{2}+\binom{43-a}{2}]/\binom{50}{2}$. Writing $a=22+t$ makes the numerator $420+t^2$. Thus $p(a)\ge1/2$ requires $t^2\ge192.5$, whose least allowable value is $196$ at $|t|=14$. The minimum is $616/1225=88/175$, yielding $263$.

**Answer:** 263.

**Methods:** conditional probability, convexity.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2011 AIME I Problem 5: Sliding sums force periodic residues

Label a regular nonagon by $1,\ldots,9$, requiring every three consecutive labels to have sum divisible by $3$. Identify rotations but not reflections. Count arrangements.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Subtract consecutive triple-sum congruences to obtain $a_{i+3}\equiv a_i\pmod3$. Since each residue class occurs exactly three times, the three position classes modulo three must receive the three residues in a permutation. There are $3!$ residue patterns on labeled vertices and $(3!)^3$ assignments of actual labels. Every rotation orbit has size nine because all labels are distinct. Thus the number is $3!(3!)^3/9=144$.

**Answer:** 144.

**Methods:** sliding windows, periodicity, rotations.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2011 AIME I Problem 7: Splitting a power into equal smaller powers

For how many positive integers $m$ can one power $m^{x_0}$ equal a sum of exactly $2011$ powers $m^{x_i}$ with all exponents nonnegative?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

The case $m=1$ is impossible. For $m>1$, reduction modulo $m-1$ gives $1\equiv2011$, so $m-1\mid2010$. Conversely, let $k=2010/(m-1)$. Start with $m^k$ and repeatedly replace one positive-exponent term $m^j$ by $m$ copies of $m^{j-1}$, following a descending chain for $k$ splits. Each split adds $m-1$ terms, ending at exactly $2011$ nonnegative-exponent powers. Thus valid $m$ correspond to divisors of $2010=2\cdot3\cdot5\cdot67$, of which there are $16$.

**Answer:** 016.

**Methods:** refinement, invariants, m-ary trees.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 3: Pattern examples suggest the splitting construction but do not establish necessity; reduction modulo m-1 is required. Source 4: Splitting proves sufficiency. Necessity still needs a merging argument or the residue invariant. Source 5: The constructed family proves sufficiency but its form cannot simply be assumed for every representation.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2011 AIME I Problem 10: Obtuse triangles in a regular polygon

Three vertices are chosen uniformly from a regular $n$-gon. Their triangle is obtuse with probability $93/125$. Find the sum of all possible $n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

An obtuse triangle has a unique circular gap greater than a semicircle. The vertex after that gap is a unique anchor, and its other two vertices must be among the next $h=\lfloor(n-1)/2\rfloor$ vertices. Thus $P=n\binom h2/\binom n3$. If $n=2t$, this simplifies to $3(t-2)/(2(2t-1))$, giving $t=188$ and $n=376$. If $n=2t-1$, it is $3(t-2)/(2(2t-3))$, giving $t=64$ and $n=127$. The sum is $503$.

**Answer:** 503.

**Methods:** cyclic gaps, geometric probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: The obtuse-triangle formula has an off-by-one error and does not produce the two values subsequently claimed. Trial values also do not prove exhaustiveness.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2011 AIME I Problem 12: Conditioning on no isolated men

Six men and $w$ women stand uniformly in a row. Given that no man is isolated, find the least $w$ for which the probability of a male run of length at least four is at most $1/100$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Ignore identities, which contribute a common factor. The possible positive male run lengths are $(2,2,2),(3,3),(2,4),(4,2),(6)$. Choosing occupied gaps among the $w+1$ gaps around women gives denominator $\binom{w+1}{3}+3\binom{w+1}{2}+w+1$. Favorable patterns give numerator $2\binom{w+1}{2}+w+1$. The ratio simplifies to $6(w+1)/(w^2+8w+6)$. The bound is equivalent to $w(w-592)\ge594$. Values $w\le592$ fail, $593$ fails by one, and $594$ works.

**Answer:** 594.

**Methods:** conditional probability, runs, gaps.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2011 AIME II Problem 6: Reflect the outer gaps

Count $1\le a<b<c<d\le10$ with $a+d>b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

The five nonnegative gaps $(a-1,b-a-1,c-b-1,d-c-1,10-d)$ sum to six. Swapping their second and fourth components reverses the strict inequality, so count all $\binom{10}{4}=210$ possibilities, remove ties, and halve. Ties have common gap $j=0,1,2,3$, giving $\sum_{j=0}^3\binom{8-2j}{2}=28+15+6+1=50$. Thus the answer is $(210-50)/2=80$.

**Answer:** 080.

**Methods:** involutions, gaps, stars and bars.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 3: The displayed triangular-number sum is missing a factor two; the equality-case count 50 is correct. Source 5: The rational generating function is missing one factor 1/(1-x); its later binomial coefficients use the correct exponent. Source 7: The gap substitution reverses the required inequality. Reflection shows the reverse inequality has the same count, but that step is absent.

**Archived alternatives reviewed:** 8 of 8. Indices in the data are zero-based.

**Status:** solved.

## 2011 AIME II Problem 7: Transitions bound the number of marbles

Arrange five identical green and some identical red marbles in a row. The number of equal-color adjacencies equals the number of unequal-color adjacencies. At the maximum possible red count, count arrangements modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Each green can participate in at most two color changes, so at most ten of the $R+4$ adjacencies are unequal. Equality of the two types gives $R+4\le20$, hence $R\le16$. Equality is attained exactly when all five greens are isolated and both ends are red. Thus distribute $16$ reds among the six nonempty gaps around the greens: $\binom{15}{5}=3003$ arrangements. The residue is $3$.

**Answer:** 003.

**Methods:** runs, extremal transitions, compositions.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2011 AIME II Problem 12: Avoid a monochromatic triple on a circle

Seat three delegates from each of three countries randomly around a nine-seat circle. Every delegate must have a neighbor from another country. Find numerator plus denominator of the success probability.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Treat country labels as indistinguishable and seats as numbered, giving $9!/(3!)^3=1680$ words. Failure occurs when all three members of some country form a consecutive block. For a specified country there are $9\binom63=180$ words. For two specified country blocks there are $9\cdot4=36$, by contracting the two blocks on the circle. All three blocks give $9\cdot2=18$. Inclusion-exclusion gives $3\cdot180-3\cdot36+18=450$ failures. Thus $P=1230/1680=41/56$, giving $97$.

**Answer:** 097.

**Methods:** circular blocks, inclusion exclusion, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2011 AIME II Problem 14: Permutations respecting residue partitions

Count permutations $a_1,\ldots,a_{30}$ of $1,\ldots,30$ satisfying $a_{i+m}\equiv a_i\pmod m$ for $m=2,3,5$ wherever defined. Give the residue modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

For each modulus, values in any one position residue class share a value residue. Equal class sizes and bijectivity force a permutation of the residue classes. Choose these residue permutations independently in $2!,3!,5!$ ways. The Chinese remainder theorem then specifies a unique value modulo $30$ at each position and guarantees all thirty values are distinct. Therefore $N=2!3!5!=1440$, giving $440$.

**Answer:** 440.

**Methods:** Chinese remainder theorem, permutation products.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 2: The relevant CRT hypothesis is pairwise coprimality; a collective gcd of one is not sufficient in general. Source 3: The optional extension to sixty symbols is incorrect: after choosing residue permutations, each of thirty residue classes has an independent two-element permutation.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2011 AIME II Problem 15: Floor equality on three intervals

Let $P(x)=x^2-3x-9$ and choose $x$ uniformly on $[5,15]$. The probability that $\lfloor\sqrt{P(x)}\rfloor=\sqrt{P(\lfloor x\rfloor)}$ has form $(\sqrt a+\sqrt b+\sqrt c-d)/e$. Find $a+b+c+d+e$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

The right side must be integral. For integer inputs $5$ through $14$, $P(k)$ is square only at $k=5,6,13$, with square roots $1,3,11$. Since $P$ is increasing, the successful intervals run from each $k$ until $P(x)$ reaches the next square $4,16,144$. Their upper endpoints are $(3+\sqrt{61})/2,(3+\sqrt{109})/2,(3+\sqrt{621})/2$. Each upper endpoint is less than $k+1$, so the floor of $x$ stays at $k$ throughout. Sum their lengths and divide by ten to obtain $(\sqrt{61}+\sqrt{109}+\sqrt{621}-39)/20$. The requested sum is $850$.

**Answer:** 850.

**Methods:** continuous probability, floor stratification.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: The substitution mishandles the floor: floor(2x-3) is not 2 floor(x)-3. The subsequent intervals actually use the latter expression, so the written transformed equation is invalid. Source 3: The answer format is used to assert interval bounds without proof. The bounds should be checked directly.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2012 AIME I Problem 1: Divisibility in both digit directions

Count three-digit integers $abc$ with $a,c\ne0$ such that both $abc$ and $cba$ are divisible by four.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

The conditions are $2b+c\equiv0\pmod4$ and $2b+a\equiv0\pmod4$. For even $b$, each of $a,c$ is $4$ or $8$; for odd $b$, each is $2$ or $6$. Every one of the ten choices for $b$ therefore permits four pairs $(a,c)$, giving $40$.

**Answer:** 040.

**Methods:** digit counting, residues.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 2: The initial even-middle-digit factor is mistyped as four rather than five.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2012 AIME I Problem 3: Exactly one correct meal type

Nine labeled diners order three meals of each of three types. The nine meal types are assigned to diners, with identical meals indistinguishable. Count assignments with exactly one diner receiving the ordered type.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

Choose the unique correct diner in nine ways. Suppose that diner ordered type $B$. Two remaining $B$-diners must get only $C,F$. If both get $C$, the other groups are forced apart from three placements of the one $C$ among the $F$-diners; likewise both $F$ gives three. If they get one of each, there are two orders, then three choices for the sole $B$ in each other group, giving $18$. Thus each correct diner permits $3+3+18=24$ assignments, and the total is $216$.

**Answer:** 216.

**Methods:** contingency tables, exact matches.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: The source itself acknowledges that its argument obtains the correct count coincidentally. Independent residual meal assignments are not justified.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2012 AIME I Problem 5: Consecutive binary numbers with equal weight

Let $B$ contain all thirteen-bit strings with eight ones and five zeros, allowing leading zeros. Count ordered pairs $(u,v)\in B^2$ with numeric difference $u-v=1$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

If $v$ ends in $t$ ones, adding one changes its one-count by $1-t$. Equal one-counts therefore force $t=1$, so $v$ ends in $01$ and $u$ in $10$. Their shared eleven-bit prefix must contain seven ones. This condition is sufficient and unique, yielding $\binom{11}{7}=330$.

**Answer:** 330.

**Methods:** binary carries, bijections.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2012 AIME I Problem 7: Stationary coins on a network

On a connected undirected network, one central vertex has degree five, five vertices have degree three, and ten have degree four. The vertices hold $3360$ coins and simultaneously split all coins equally among neighbors; every holding remains unchanged. Find the central holding.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Write the holding at vertex $v$ as $d(v)r_v$. Stationarity says $d(v)r_v=\sum_{u\sim v}r_u$, so $r_v$ is the average of its neighbors' ratios. At a maximum, all neighboring ratios equal that maximum; connectivity propagates equality everywhere. Thus holdings are proportional to degrees. The degree sum is $5+5\cdot3+10\cdot4=60$, giving $56$ coins per degree and central holding $5\cdot56=280$.

**Answer:** 280.

**Methods:** graphs, maximum principle, stationary distributions.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** The principal archived solution assumes equal holdings on symmetric rings. The maximum-principle argument proves uniqueness without that assumption. Audit findings: Source 1: Equal gifts are asserted without a uniqueness argument. Dividing holdings by vertex degree and applying the finite harmonic maximum principle supplies it. Source 3: Visual symmetry does not prove an arbitrary stationary allocation is symmetric. Use the harmonic maximum principle or sum the layer equations.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2012 AIME I Problem 11: Reachability in a lattice semigroup

From $(0,0)$ allow jumps $(7,2),(2,7),(-5,-10),(-10,-5)$. Let $M$ count reachable lattice points with $|x|+|y|\le100$. Find $M\bmod1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Necessarily $x+y=3u$, $x-y=5v$ for integers $u,v$ of the same parity. Conversely the jumps in $(u,v)$ are $(3,\pm1),(-5,\pm1)$. Choose large nonnegative $C\equiv u\pmod3$ and put $A=(u+5C)/3$. Then $3A-5C=u$, while $L=A+C\ge|v|$ and $L\equiv u\equiv v\pmod2$. Among these $L$ jumps choose $(L+v)/2$ plus signs, obtaining the target with nonnegative counts. Hence the invariants are sufficient. Now $|x|+|y|=\max(|3u|,|5v|)$, so $-33\le u\le33$, $-20\le v\le20$. Equal parities give $33\cdot21+34\cdot20=1373$ points, hence $373$.

**Answer:** 373.

**Methods:** lattice invariants, reachability, parity.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** The first archived sufficiency argument does not clearly enforce nonnegative jump counts. Taking a sufficiently large solution and assigning signs here proves actual reachability.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2012 AIME I Problem 15: Multiplication changes every circular separation

Reseat $n$ people on a numbered circle by $k\mapsto ak\pmod n$. Require this to be a permutation and require every pair's circular separation to change even up to reversal. Count possible $1<n<1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Permutation requires $\gcd(a,n)=1$. A nonzero difference $d$ must never satisfy $ad\equiv d$ or $ad\equiv-d\pmod n$, equivalent to $\gcd(a-1,n)=\gcd(a+1,n)=1$. Thus three consecutive integers must all be coprime to $n$, impossible if $2\mid n$ or $3\mid n$. Conversely if $\gcd(n,6)=1$, choose $a=2$, and all three gcds are one. Inclusion-exclusion on $1,\ldots,999$ gives $999-499-333+166=333$ values, of which $n=1$ is excluded. The result is $332$.

**Answer:** 332.

**Methods:** cyclic permutations, modular invariants.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2012 AIME II Problem 1: Count lattice points on a positive Diophantine segment

Count ordered positive integer pairs $(m,n)$ satisfying $20m+12n=2012$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

Divide by four: $5m+3n=503$. Modulo three this forces $m\equiv1\pmod3$, and positivity of $n$ forces $m\le100$. Conversely every $m=1+3j$ for $0\le j\le33$ gives $n=(503-5m)/3$, a positive integer. This is a bijection with thirty-four integers $j$, so there are $34$ ordered pairs.

**Answer:** 034.

**Methods:** linear Diophantine equations, lattice-point counting, congruences.

**Verification:** Direct enumeration of positive pairs gives thirty-four.

**Source comparison:** All four stored alternatives inspected. They use either congruences or a lattice slope. The last initially states a false divisibility-by-twenty criterion before adding the missing tens-digit condition; the congruence proof here is exact from the outset.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2012 AIME II Problem 3: Department and gender margins

Three departments each contain two men and two women. Choose a six-person committee with two members per department and three of each gender. Count committees.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

The male counts by department must be $(1,1,1)$ or a permutation of $(0,1,2)$. The first contributes $(2\cdot2)^3=64$. Each of the six second-type patterns contributes $1\cdot4\cdot1=4$. Thus the total is $64+24=88$. Equivalently it is $[x^3](1+4x+x^2)^3$.

**Answer:** 088.

**Methods:** fixed margins, generating functions.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2012 AIME II Problem 7: Unranking a binary subset

List positive integers with exactly eight binary ones in increasing order. Find the $1000$th integer modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Numbers fitting in twelve bits number $\binom{12}{8}=495$, so bit $12$ is one and the remaining rank is $505$ among twelve-bit strings of weight seven. Since $\binom{11}{7}=330$, bit $11$ is one and rank becomes $175$. Bit $10$ is zero because $\binom{10}{6}=210\ge175$. Skipping $\binom96=84$ then $\binom85=56$ makes bits $9,8$ one and leaves rank $35$ for weight four below bit eight. Since $\binom74=35$, take the largest seven-bit weight-four string, $1111000$. Thus $N=2^{12}+2^{11}+2^9+2^8+2^6+2^5+2^4+2^3=7032$, giving $32$.

**Answer:** 032.

**Methods:** binomial unranking, binary subsets.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

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

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2012 AIME II Problem 12: Independent forbidden residues

A positive integer is $p$-safe if its distance from every multiple of $p$ exceeds two. Count integers at most $10000$ that are simultaneously $7$-, $11$-, and $13$-safe.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

The allowed residues modulo $p$ are $3,\ldots,p-3$, a total of $p-5$. By the Chinese remainder theorem there are $2\cdot6\cdot8=96$ safe residues per block of $1001$. Thus $1,\ldots,10010$ contains $960$ safe numbers. Among the last ten integers only $10006,10007$ qualify (their residues are respectively $-4,-3$ modulo all three moduli). Subtract these to obtain $958$.

**Answer:** 958.

**Methods:** Chinese remainder theorem, residue counting.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2012 AIME II Problem 14: Labeled two-regular graphs

Nine labeled people each shake hands with exactly two others. Count possible sets of handshakes modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

The handshake graph is a disjoint union of simple cycles of length at least three. The possible component sizes are $9$, $6+3$, $5+4$, and $3+3+3$. Their counts are $8!/2=20160$, $\binom93(5!/2)=5040$, $\binom94(3!/2)(4!/2)=4536$, and $9!/((3!)^3 3!)=280$. The sum is $30016$, giving residue $16$. Division by two reverses each cycle; division by $3!$ removes the ordering of equal-sized components.

**Answer:** 016.

**Methods:** graphs, cycle decompositions, symmetry.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: The case-tree idea is valid, but several displayed subscripts and parentheses omit multiplicative factors.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2013 AIME I Problem 2: Uniform digit sums modulo five

Count five-digit integers divisible by five whose first and last digits agree and whose digit sum is divisible by five.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

The first and last digits must both be $5$, so write the integer $5abc5$. Choose $a,b$ arbitrarily in $100$ ways. Exactly two choices of $c\in\{0,\ldots,9\}$ give $a+b+c\equiv0\pmod5$. The count is $200$.

**Answer:** 200.

**Methods:** residue uniformity, digit counting.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2013 AIME I Problem 4: Coloring the orbits of a quarter-turn

A thirteen-cell figure has one central cell and three four-cell orbits under a quarter-turn. Choose eight cells red and five blue uniformly. The probability of quarter-turn invariance is $1/n$. Find $n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

An invariant coloring is constant on each orbit. Since there are eight red cells, exactly two of the three size-four orbits are red and the center is blue. Thus there are three invariant colorings among $\binom{13}{8}=1287$ choices. The probability is $3/1287=1/429$, giving $429$.

**Answer:** 429.

**Methods:** group orbits, invariant colorings, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2013 AIME I Problem 6: Track only the special books

Randomly pack twelve distinct books into labeled boxes of sizes three, four, and five. Three books are mathematics books. Find numerator plus denominator of the probability that all three share a box.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

Imagine twelve labeled capacity slots. The three mathematics books occupy a uniform three-subset of the slots. Favorable subsets lie entirely within one box, giving $\binom33+\binom43+\binom53=1+4+10=15$. Hence $P=15/\binom{12}{3}=3/44$, and the answer is $47$.

**Answer:** 047.

**Methods:** sample-space compression, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

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

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2013 AIME I Problem 15: Two arithmetic progressions with reordered residues

Count $0\le A<B<C\le99$ forming an arithmetic progression for which a prime $p$ and residues $0\le b<a<c<p$ satisfy $A\equiv a$, $B\equiv b$, $C\equiv c\pmod p$, with $(b,a,c)$ also an arithmetic progression.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Write $(A,B,C)=(B-D,B,B+D)$ and $(b,a,c)=(a-d,a,a+d)$. Subtracting the congruences gives $D\equiv-d\equiv2d\pmod p$, hence $p\mid3d$. Since $0<d<p$, $p=3$, and the residues are $(a,b,c)=(1,0,2)$. Thus $B=3k$ and $D\equiv2\pmod3$, with $D\le\min(B,99-B)$. For $k=1,\ldots,16$ there are $k$ choices of $D$; for $k=17,\ldots,32$ there are $33-k$. These conditions are also sufficient using $p=3$. The count is $2(1+\cdots+16)=272$.

**Answer:** 272.

**Methods:** residue constraints, arithmetic progressions, case counting.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: The listed ranges and counts for the progression difference disagree, and the final arithmetic sum is not 272. The middle-term count in the original solution avoids these errors.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2013 AIME II Problem 9: Colored compositions use all colors

Tile a seven-cell row by positive integer-length tiles colored red, blue, or green, requiring all three colors. Adjacent tiles of the same color remain distinct tiles. Find the tiling count modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

With $q$ available colors, a tiling is encoded by its first tile color ($q$ choices) and at each of the six internal cell boundaries either no cut or a cut followed by one of $q$ colors. Thus $T(q)=q(q+1)^6$. Inclusion-exclusion on missing colors gives $T(3)-3T(2)+3T(1)=3\cdot4^6-6\cdot3^6+3\cdot2^6=8106$, with residue $106$.

**Answer:** 106.

**Methods:** compositions, boundary encoding, inclusion exclusion.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: The number of divisions into i pieces is C(6,i-1), not the displayed C(6,i).

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2013 AIME II Problem 11: Functions whose second iterate is constant

Count functions on a seven-element labeled set for which $f\circ f$ is constant, and give the count modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Let the constant be $c$. Since $f^2(f(x))=c=f(f^2(x))$, we have $f(c)=c$. Choose $c$ in seven ways. Let $K=f^{-1}(c)\setminus\{c\}$ have size $k$. Every other element must map into $K$, and conversely any such map works. Thus $N=7\sum_{k=1}^{6}\binom6k k^{6-k}=7399$, giving $399$. The definition of $K$ makes the decomposition unique and prevents duplicate counting.

**Answer:** 399.

**Methods:** functional graphs, rooted structures.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: The exposition confuses the image with the preimage of the fixed point, omits a binomial factor in the written sum, and mistypes the exponent base. The final evaluated sum corresponds to the corrected rooted-layer count.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2013 AIME II Problem 12: Cubics with roots on two circles

Count monic integer-coefficient cubics all of whose complex roots have modulus either $13$ or $20$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

If all roots are real, they form a multiset of size three from $\{-20,-13,13,20\}$, giving $\binom63=20$. Otherwise there is one real root $r$ from those four values and a conjugate pair of modulus $R\in\{13,20\}$. Its quadratic factor is $z^2-tz+R^2$, where $t$ must be integral because the cubic's quadratic coefficient is integral and $r$ is integral. Nonreal roots require $|t|<2R$, giving $51$ or $79$ choices. Each choice yields integral coefficients and a unique cubic. Thus the count is $20+4(51+79)=540$.

**Answer:** 540.

**Methods:** multisets, algebraic enumeration.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: The squared magnitude is called the magnitude. The coefficient argument is correct after that distinction. Source 2: The discriminant condition needs an absolute value on p, and its displayed square root contains an extraneous square.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2014 AIME I Problem 2: Matching colors from two urns

Two independent draws use urns with color counts $(4,6)$ and $(16, N)$. Their colors agree with probability $29/50$. Determine $N$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

The two matching events are disjoint. Thus $(4\cdot16+6N)/(10(16+N))=29/50$. Cross multiplication gives $320+30N=464+29N$, hence $N=144$.

**Answer:** 144.

**Methods:** probability, total probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2014 AIME I Problem 3: Reduced fractions with fixed numerator-plus-denominator

Count reduced fractions strictly between zero and one whose positive numerator and denominator sum to 1000.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

Write the fraction as $a/(1000-a)$ with $1\le a\le499$. It is reduced exactly when $\gcd(a,1000)=1$, so $a$ must be divisible by neither $2$ nor $5$. Inclusion-exclusion gives $499-249-99+49=200$. Equivalently, complementary residues pair the $\varphi(1000)=400$ coprime values into reciprocal fractions.

**Answer:** 200.

**Methods:** Euclidean algorithm, totient, inclusion-exclusion.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight sources inspected. Totient pairing and exclusion of multiples of 2 and 5 agree. Some alternatives reverse divisibility notation or say a divides 1000 rather than shares a prime factor; the gcd equivalence is the correct criterion.

**Archived alternatives reviewed:** 8 of 8. Indices in the data are zero-based.

**Status:** solved.

## 2014 AIME I Problem 5: Disk-separable vertex subsets

Count subsets of a regular dodecagon that are precisely its vertices strictly inside some circle.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

On the circumcircle $|X|=R$, the disk condition $|X-c|^2<r^2$ becomes the linear inequality $c\cdot X>(R^2+|c|^2-r^2)/2$. Consequently a nonempty proper subset must be a consecutive cyclic interval. Conversely each such interval is cut off by a suitable line, and a disk realizes the same strict inequality on the circumcircle. There are $12$ intervals of each size $1$ through $11$; add the empty and full sets: $12\cdot11+2=134$.

**Answer:** 134.

**Methods:** cyclic intervals, geometry counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The source identifies consecutive vertices; this proof supplies the missing linearization and converse.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2014 AIME I Problem 11: Diagonal endpoint of a random walk

A planar simple random walk starts at the origin and takes six unit axis steps. Find numerator plus denominator of its probability of ending on either diagonal $y=x$ or $y=-x$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Use coordinates $u=x+y, v=x-y$. Each step independently chooses a uniform sign for $u$ and for $v$, so $u$ and $v$ are independent six-step one-dimensional walks. Each is zero with probability $\binom63/2^6=5/16$. Thus $P(uv=0)=2(5/16)-(5/16)^2=135/256$. Answer: $391$.

**Answer:** 391.

**Methods:** random walks, coordinate bijection, inclusion-exclusion.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2014 AIME I Problem 12: Disjoint ranges of random functions

Choose independently two maps from a four-element set to itself. Find the numerator of the reduced probability that their images are disjoint.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

If the first map has $k$ image values, choose them in $\binom4k$ ways. For $k=1,2,3$, the counts of onto maps to those values are $1,14,36$, respectively, by inclusion-exclusion. The second map may use any of the other $4-k$ values. Thus the favorable count is $4(1)(3^4)+6(14)(2^4)+4(36)(1^4)=1812$. Dividing by $4^8$ gives $453/16384$, with numerator $453$.

**Answer:** 453.

**Methods:** surjections, Stirling numbers, probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2014 AIME II Problem 2: Conditional probability from Venn atoms

Three events each have exclusive probability $0.10$; every exclusive pair has probability $0.14$. Given $A$ and $B$, all three occur with probability $1/3$. Find numerator plus denominator of the probability of no events conditional on not $A$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

Write $t=P(A\cap B\cap C)$. Then $t/(0.14+t)=1/3$, so $t=0.07$. The probability of none is $1-3(0.10)-3(0.14)-0.07=0.21$. Also $P(A)=0.10+2(0.14)+0.07=0.45$. Therefore the requested probability is $0.21/0.55=21/55$ and the answer is $76$.

**Answer:** 076.

**Methods:** probability, conditional probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2014 AIME II Problem 6: A hidden die and Bayesian updating

Choose equally between a fair die and one whose six-probability is $2/3$. After two sixes, find the reduced numerator plus denominator of the probability of another six.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

The likelihood ratio biased:fair after two sixes is $(2/3)^2:(1/6)^2=16:1$. Conditional on the observations, the next six therefore has probability $(16/17)(2/3)+(1/17)(1/6)=65/102$. Answer: $167$.

**Answer:** 167.

**Methods:** Bayes theorem, probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2014 AIME II Problem 9: A run of three on a cycle

Among the subsets of ten labeled cyclic seats, count those containing three consecutive seats.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Count the complement by a transfer matrix. States $0,1,2$ record the number of consecutive selected seats since the last unselected seat. The allowed transitions are $0\to0,1$; $1\to0,2$; $2\to0$. With matrix $M=((1,1,0),(1,0,1),(1,0,0))$, each cyclic binary word without $111$ has exactly one compatible state at each labeled position; the all-selected word is excluded. Therefore the complement is $\operatorname{tr}(M^{10})=443$. For direct evaluation, $c_n=\operatorname{tr}(M^n)$ satisfies $c_n=c_{n-1}+c_{n-2}+c_{n-3}$, with $c_0=3, c_1=1, c_2=3$. Hence $2^{10}-443=581$.

**Answer:** 581.

**Methods:** transfer matrices, cyclic runs.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The source uses lengthy size-by-size casework; a cyclic transfer matrix removes overlapping runs.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2014 AIME II Problem 13: Shoe matching and long cycles

Randomly match ten left shoes to ten right shoes. No subset of fewer than five resulting pairs may contain exactly the complete shoes of that many owners. Find numerator plus denominator of the probability.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

A matching is a permutation of owners; a closed collection of pairs is a union of cycles. The condition therefore forbids cycles shorter than five. The only cycle types are $(10)$ and $(5,5)$, with probabilities $1/10$ and $1/(2\cdot5^2)$. Their sum is $3/25$, giving $28$.

**Answer:** 028.

**Methods:** permutation cycles, probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2014 AIME II Problem 15: Prime multiplication as binary carrying

For positive $k$, let $p(k)$ be the smallest prime not dividing $k$, and let $X(k)$ be the product of smaller primes, with empty product 1. Define $x_0=1$ and $x_{n+1}=x_np(x_n)/X(x_n)$. Find the first $t>0$ with $x_t=2090$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Every term is squarefree. Encode it by a binary integer whose bit $j-1$ records whether the $j$th prime divides it. The smallest missing prime identifies the first zero bit; dividing by all smaller primes clears exactly the preceding consecutive one bits, and multiplying by that prime sets the zero bit. This is precisely binary addition of 1. Starting from $x_0=1$, the encoded integer is therefore $n$. Since $2090=2\cdot5\cdot11\cdot19$ uses prime indices 1,3,5,8, its index is $2^0+2^2+2^4+2^7=149$. The encoding is bijective, proving this is the first occurrence.

**Answer:** 149.

**Methods:** binary carrying, squarefree integers, conjugate dynamics.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three sources inspected. The binary encoding and its induction version explain the recurrence; the brute-force suggestion alone does not prove first occurrence.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2015 AIME I Problem 2: Exactly one repeated nationality

Select three of nine distinct delegates, with nationality group sizes $2,3,4$. Find numerator plus denominator of the probability their nationality multiplicities are $2$ and $1$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

Choose the nationality of the pair, then the pair and the outsider. The favorable count is $\binom22(7)+\binom32(6)+\binom42(5)=55$. All $\binom93=84$ triples are equally likely. Thus the answer is $55+84=139$.

**Answer:** 139.

**Methods:** casework, combinations, probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2015 AIME I Problem 5: First matching sock pair on day three

Ten socks form five color pairs. Draw two without replacement on each of three days. Find numerator plus denominator of the probability only the third day produces a matching pair.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Reveal day three first. Its pair matches with probability $1/9$. Conditional on that, eight socks form four complete pairs. For the first two days, inclusion-exclusion gives probability $1-2/7+1/(7\cdot5)=26/35$ of neither pair matching. Therefore the desired probability is $26/315$ and the answer is $341$.

**Answer:** 341.

**Methods:** deferred decisions, inclusion-exclusion, probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2015 AIME I Problem 9: When a multiplicative recurrence reaches zero

For $1\le x, y, z\le 10$ initialize $a_1=x, a_2=y, a_3=z$ and $a_n=a_{n-1}|a_{n-2}-a_{n-3}|$. Count initial triples whose sequence eventually reaches zero.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Write $d=|y-x|$ and $e=|z-y|$. If $d$ or $e$ is $0$ or $1$, a zero or adjacent equality occurs and eventually forces zero. If $d, e\ge 2$, then $a_4=zd, a_5=zde$. The exceptional case $z=1, d=2$ gives $a_6=a_5$ and hence zero. Otherwise $a_4-a_3=z(d-1)\ge 2$ and $a_5-a_4=zd(e-1)\ge 2$. Thereafter each multiplier is at least two, preserving positive gaps of at least two, so zero is impossible. The first two events each contain $280$ triples; their intersection has $2\cdot2^2+8\cdot3^2=80$. The exceptional condition adds $14$ new triples. Total: $280+280-80+14=494$.

**Answer:** 494.

**Methods:** recurrence invariants, inclusion-exclusion.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The source growth argument is informal; the invariant on successive differences makes the exclusion rigorous.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2015 AIME I Problem 12: Mean minimum of a large subset

Choose uniformly a $1000$-element subset of $\{1,\ldots,2015\}$. Find numerator plus denominator of its expected minimum.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

For a $k$-subset of $[N]$, the $k+1$ gaps of omitted elements before, between, and after its selected elements are exchangeable and sum to $N-k$. Therefore the first gap has mean $(N-k)/(k+1)$, and the minimum has mean $(N+1)/(k+1)$. Here this is $2016/1001=288/143$, giving $431$.

**Answer:** 431.

**Methods:** gap bijection, expectation.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2015 AIME I Problem 14: Parity of piecewise-linear area

Let $A(n)$ be the area under $y=x \lfloor\sqrt{x}\rfloor$ from $x=1$ to $x=n$. Count $2\le n\le 1000$ for which $A(n)$ is integral.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Put $m=\lfloor\sqrt n\rfloor$. Twice the area is $\sum_{k=1}^{m-1}k((k+1)^4-k^4)+m(n^2-m^4)$, whose parity is $mn-m(m+1)/2$. Therefore $m\equiv0 \pmod{4}$ always works; $m\equiv2 \pmod{4}$ never works; $m\equiv1 \pmod{4}$ requires odd $n$; $m\equiv3 \pmod{4}$ requires even $n$. The full even-$m$ blocks contribute $\sum_{j=1}^7(8j+1)=231$. Odd-$m$ blocks $m=1,5,\ldots,29$ contribute $128$; blocks $m=3,7,\ldots,27$ contribute $105$; $m=31$ contributes $20$. Exclude $n=1$: total $231+128+105+20-1=483$.

**Answer:** 483.

**Methods:** parity, block counting.

**Verification:** Exact parity formula and block counts independently reproduce 483.

**Source comparison:** The first archived solution reverses odd-block parity and incorrectly counts half an odd block. Its reversed parity conditions happen to cancel in the final count.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2015 AIME II Problem 2: Conditioning on enrollment

Class fractions are $0.40,0.30,0.20,0.10$; Latin participation rates respectively are $1,0.80,0.50,0.20$. Given a Latin student, find numerator plus denominator of the probability of second-year status.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

The joint second-year-and-Latin probability is $0.30(0.80)=0.24$. Total Latin probability is $0.40+0.24+0.10+0.02=0.76$. The conditional probability is $0.24/0.76=6/19$, so the answer is $25$.

**Answer:** 025.

**Methods:** conditional probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2015 AIME II Problem 5: Adjacent cells in a random pair

Two different cells are chosen uniformly from an $n$ by $n$ square grid. Find the least $n$ for which their probability of sharing an edge is below $1/2015$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

The grid has $2n(n-1)$ adjacent unordered pairs. Thus the probability is $2n(n-1)/\binom{n^2}2=4/[n(n+1)]$. We require $n(n+1)>8060$. Since $89\cdot90=8010$ and $90\cdot91=8190$, the least $n$ is $90$.

**Answer:** 090.

**Methods:** double counting, probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2015 AIME II Problem 10: Permutations with bounded downward steps

Count permutations of $1$ through $7$ in which $a_k-a_{k+1}\le 2$ for every adjacent pair.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Insert the new maximum $n$ into a valid permutation of $1,\ldots, n-1$. It can go only immediately before $n-1$, immediately before $n-2$, or at the end. All three work. Conversely deleting $n$ preserves validity: if its successor is $n-1$ or $n-2$, every possible predecessor remains legal. Thus $F_n=3F_{n-1}$ for $n\ge 3$ and $F_2=2$; $F_7=2\cdot3^5=486$.

**Answer:** 486.

**Methods:** insertion bijection, recurrences.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2015 AIME II Problem 12: Binary strings with bounded runs

Count length-ten binary words whose constant runs have length at most three.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Let $F_n$ count such words. For $n\ge 4$, remove the terminal run of length $1,2$, or $3$; its color is forced opposite the preceding letter. Thus $F_n=F_{n-1}+F_{n-2}+F_{n-3}$, with $F_1=2, F_2=4, F_3=8$. The next values are $14,26,48,88,162,298,548$.

**Answer:** 548.

**Methods:** runs, recurrences.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 7 of 7. Indices in the data are zero-based.

**Status:** solved.

## 2016 AIME I Problem 2: Weighted dice

Each independent die has $P(k)=k/21$ for $k=1,\ldots,6$. Find numerator plus denominator of the probability their sum is seven.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

The numerator over $21^2$ is $\sum_{k=1}^6k(7-k)=56$. Thus the probability is $8/63$ and the answer is $71$.

**Answer:** 071.

**Methods:** weighted counting, probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2016 AIME I Problem 3: Downward simple paths on an icosahedron

Orient an icosahedron with top and bottom vertices and two horizontal pentagons. Count vertex-simple edge paths from top to bottom that never move upward.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

Choose the first upper vertex in $5$ ways. A simple path on a pentagon from a fixed start has $1+2\cdot4=9$ possibilities: stay, or move $1$ through $4$ steps in either direction. From the last upper vertex choose one of two descending edges. The lower pentagon again offers $9$ paths, followed by its edge to the bottom. Total $5\cdot9\cdot2\cdot9=810$.

**Answer:** 810.

**Methods:** product rule, graph paths.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2016 AIME I Problem 8: Minimizing a digit-column sum

Permute digits $1,\ldots,9$ into three three-digit numbers. Among sums ending in $0$, let $m$ be the least sum and $n$ its number of permutations. Find $|m-n|$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

Let $H, T, U$ be the sums of hundreds, tens, units digits. Then the sum is $450+90H-9U$, with $H\ge 6$ and $U\le 24$; $U$ must be $10$ or $20$. Hence the minimum requires $H=6, U=20$, attainable with hundreds $\{1,2,3\}$. Units sets are $\{4,7,9\},\{5,6,9\},\{5,7,8\}$; tens are forced. Therefore $m=810$ and $n=3(3!)^3=648$; difference $162$.

**Answer:** 162.

**Methods:** digit arrangements, extremal counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2016 AIME I Problem 13: Reflected random walk hitting time

A frog starts at height $21$. Above $0$ it chooses four unit axis moves uniformly; at height $0$ only the two horizontal moves and upward move are allowed. Find expected steps to reach height $24$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Let $E_y$ denote the expected remaining time. First-step conditioning gives $E_{24}=0, E_0-E_1=3$, and $E_y=1+(E_{y-1}+2E_y+E_{y+1})/4$. Thus differences $D_y=E_y-E_{y+1}$ satisfy $D_y=D_{y-1}+4$, so $D_y=4y+3$. Therefore $E_{21}=D_{21}+D_{22}+D_{23}=87+91+95=273$. Finite expectation follows from a uniformly positive chance of $24$ successive upward moves in every $24$-step block.

**Answer:** 273.

**Methods:** hitting times, difference equations.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2016 AIME I Problem 14: Lattice shapes intersected by a rational line

At every lattice point place a radius $1/10$ circle and an axis-parallel side $1/5$ square. Count the total shapes meeting the segment from $(0,0)$ to $(1001,429)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

The line is $3x-7y=0$. A centered circle meets it only when $|3x-7y|/\sqrt{58}\le 1/10$, forcing the integer numerator to $0$. There are $144$ such centers, $(7k,3k),0\le k\le 143$. A square meets the line exactly when $|3x-7y|\le 1$, because its half-width changes this linear form by at most $1$. Besides $144$ on-line centers, each of the $143$ fundamental strips has one center of each offset $\pm 1$. Endpoints create no extra centers. Thus there are $144$ circles and $430$ squares, for a total of $574$.

**Answer:** 574.

**Methods:** lattice counting, periodicity.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2016 AIME II Problem 2: Dependent rain events

Saturday rain has probability $2/5$ and Sunday rain $3/10$. Sunday rain is twice as likely after Saturday rain as after no Saturday rain. Find numerator plus denominator for rain on at least one day.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

Let $q$ be the probability of Sunday rain conditional on a dry Saturday. Total probability gives $(3/5)q+(2/5)(2q)=3/10$, hence $q=3/14$. Both days dry has probability $(3/5)(11/14)=33/70$. The answer is $37+70=107$.

**Answer:** 107.

**Methods:** total probability, complements.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2016 AIME II Problem 4: Layer counts determine a colored box

An $a\times b\times c$ box of unit cubes has $9$ red and $12$ green cubes in each layer perpendicular to the $a$-direction, and $20$ green and $25$ yellow cubes in each layer perpendicular to the $b$-direction. Find its minimum volume.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Counting green cubes gives $12a=20b$, so $a=5t, b=3t$. Total red, green, yellow counts are $45t,60t,75t$; hence volume is $180t$ and $c=12/t$. The minimum is at $t=1$. It is realizable: in each of the $15$ columns of height $12$, put $3$ red, $4$ green, and $5$ yellow cubes. Its layers have exactly the required totals. Answer $180$.

**Answer:** 180.

**Methods:** double counting, constructive existence.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2016 AIME II Problem 6: Absolute coefficient sum by parity

For $P(x)=1-x/3+x^2/6$ and $Q(x)=P(x)P(x^3)P(x^5)P(x^7)P(x^9)$, find numerator plus denominator of the sum of absolute coefficients of $Q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Every chosen negative term has odd degree, and every positive term even degree. All contributions to a degree $j$ coefficient therefore have sign $(-1)^j$, with no cancellation. The absolute coefficient sum is $Q(-1)=P(-1)^5=(3/2)^5=243/32$, giving $275$.

**Answer:** 275.

**Methods:** generating functions, parity.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2016 AIME II Problem 8: Three distinct factors of a product

Count unordered triples of distinct positive integers whose product is $11\cdot 21\cdot 31\cdot 41\cdot 51\cdot 61$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

The product is $3^2$ times six distinct primes. Labeled triples receive the two factors $3$ in $\binom42=6$ ways and each other prime in $3$ ways, giving $6\cdot3^6$. An equal pair must both be $1$ or both $3$, because all other prime exponents are $1$. Each type has $3$ choices for the unequal coordinate; all-equal is impossible. Remove $6$ ordered triples and divide by $3!: (6\cdot3^6-6)/6=728$.

**Answer:** 728.

**Methods:** prime-exponent distributions, stars and bars, symmetry.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2016 AIME II Problem 11: Divisor counts of perfect powers

Call $N$ $k$-nice when some $k$th power has exactly $N$ positive divisors. Count $1\le N<1000$ that are neither $7$-nice nor $8$-nice.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

The divisor formula shows $N$ is $k$-nice exactly when $N\equiv1 \pmod{k}$: necessity follows by multiplying factors $ke_i+1$; sufficiency uses $(2^{(N-1)/k})^k$. There are $143$ integers $1\pmod7$, $125$ integers $1 \pmod{8}$, and $18$ integers $1 \pmod{56}$ in $[1,999]$. Inclusion-exclusion leaves $999-(143+125-18)=749$.

**Answer:** 749.

**Methods:** inclusion-exclusion, divisor counts.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The archived count omits N=1 in two intermediate totals, though the errors cancel. This version counts every endpoint consistently.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2016 AIME II Problem 12: Proper colorings of a six-cycle

Six fixed cyclic regions are colored with four colors; adjacent regions must differ. Count colorings.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

The chromatic polynomial of a cycle $C_n$ is $(q-1)^n+(-1)^n(q-1)$. To derive it, fix the first color and track whether the current color agrees with it; the two-state transition gives this expression after closing the cycle. For $q=4, n=6$, the count is $3^6+3=732$. Rotations remain distinct because the regions are fixed.

**Answer:** 732.

**Methods:** graph coloring, transfer matrices.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 12 of 12. Indices in the data are zero-based.

**Status:** solved.

## 2016 AIME II Problem 13: Mean minimum score of a permutation board

Place six nonattacking rooks on a labeled $6$ by $6$ board. Each square scores row+column. Find numerator plus denominator of the mean minimum occupied score.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

For score $X$, use $E[X]=\sum_{t=1}^7P(X\ge t)$. The counts for thresholds $t=1,\ldots,7$ are $720,720,600,384,162,32,1$. For $t\ge 2$, assign rows $1$ through $t-2$ first: each has exactly $8-t$ available columns after previous choices. The other $8-t$ rows are unrestricted, so the count is $(8-t)^{t-2}(8-t)!$. Summing gives $2619$; dividing by $720$ gives $291/80$, hence $371$.

**Answer:** 371.

**Methods:** tail-sum expectation, restricted permutations.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The source computes exact-score counts with extensive inclusion-exclusion. Nested forbidden regions give a shorter tail calculation.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2017 AIME I Problem 1: Triangles from boundary points

A triangle has $3$ additional points on one side, $4$ on another, and $5$ on the third. Count nondegenerate triangles whose vertices are among all $15$ marked points.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

Choose any three points and remove collinear triples. A line not equal to a side meets the triangle boundary at at most two points, so only side triples are degenerate. The count is $\binom{15}3-\binom53-\binom63-\binom73=455-10-20-35=390$.

**Answer:** 390.

**Methods:** complementary counting, geometry counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2017 AIME I Problem 6: A chord intersecting an isosceles triangle

An inscribed isosceles triangle has equal angles $x$ degrees. A chord with two independent uniform endpoints intersects the triangle with probability $14/25$. Find the difference between possible $x$ values.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

The complementary event has both endpoints on the same one of the three complementary arcs. Their normalized lengths are $x/180, x/180,1-2x/180$. Thus $2(x/180)^2+(1-2x/180)^2=11/25$. This yields $x^2-120x+3024=0$, with roots $36$ and $84$. Difference $48$.

**Answer:** 048.

**Methods:** geometric probability, complementary counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2017 AIME I Problem 7: A triple Vandermonde sum

Evaluate modulo $1000$ the sum of $C(6, a)C(6, b)C(6, a+b)$ over $a, b\ge 0, a+b\le 6$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Put $c=6-a-b$ and use $\binom6{a+b}=\binom6c$. The summands count choosing $6$ objects from three labeled classes of $6$ according to the three class counts. Hence the sum is $\binom{18}6=18564$, with remainder $564$.

**Answer:** 564.

**Methods:** Vandermonde identity, double counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 8 of 8. Indices in the data are zero-based.

**Status:** solved.

## 2017 AIME I Problem 8: Two random right-triangle vertices

On the same semicircle of diameter $OP=200$, select $Q, R$ so that angles $POQ$ and $POR$ are independently uniform between $0$ and $75$ degrees. Find numerator plus denominator of $P(QR\le 100)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

The central angle between $Q, R$ is $2|a-b|$, so $QR=200\sin|a-b|$. The condition is $|a-b|\le 30$. In the $75$ by $75$ parameter square, the excluded triangles have combined area $45^2$. Thus the probability is $1-45^2/75^2=16/25$; answer $41$.

**Answer:** 041.

**Methods:** geometric probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2017 AIME I Problem 11: Median of row medians

Arrange $1,\ldots,9$ in a $3$ by $3$ array. Count modulo $1000$ arrangements whose median of the three row medians is $5$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

This occurs exactly when $5$ is a row median. Necessity is immediate. For sufficiency, that row consumes one value below $5$ and one above $5$, leaving three on each side; the two remaining row medians must therefore lie on opposite sides. Choose the position of $5$ in $9$ ways, its lower and upper row partners in $4\cdot4$ ways, their order in $2$ ways, and the other entries in $6!$ ways. The count is $9\cdot32\cdot720=207360$; remainder $360$.

**Answer:** 360.

**Methods:** order statistics, symmetry.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 7 of 7. Indices in the data are zero-based.

**Status:** solved.

## 2017 AIME I Problem 12: Product-free subsets

Count subsets $S$ of $\{1,\ldots,10\}$ containing no $a,b,c$ (possibly equal) with $ab=c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

One cannot occur. If $2$ occurs, $4$ is excluded; on $\{3,6,9\}$ the allowed subsets are empty, $\{3\},\{6\},\{9\},\{6,9\}$, giving $5$ choices; on $\{5,10\}$ choose at most one, giving $3$; $7$ and $8$ are free. This gives $60$. If $2$ is absent and $3$ present, $9$ is absent and six other entries are free, giving $64$. If $2$ and $3$ are absent, every subset of $\{4,\ldots,10\}$ works, giving $128$. Total $252$.

**Answer:** 252.

**Methods:** forbidden configurations, casework.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2017 AIME II Problem 1: Subsets avoiding two containers

Count subsets of $[8]$ contained in neither $\{1,2,3,4,5\}$ nor $\{4,5,6,7,8\}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

The two forbidden families have $32$ members each, and their intersection consists of the $4$ subsets of $\{4,5\}$. Inclusion-exclusion gives $256-32-32+4=196$.

**Answer:** 196.

**Methods:** inclusion-exclusion, subsets.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2017 AIME II Problem 2: Weighted tournament champion

Four teams indexed $1,\ldots,4$ play semifinals $1$ versus $4$ and $2$ versus $3$. Team $i$ beats team $j$ with probability $i/(i+j)$, independently by match. Find numerator plus denominator for team $4$ winning.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

Condition on the other finalist. The probability is $(4/5)[(2/5)(4/6)+(3/5)(4/7)]=256/525$. Thus the answer is $781$.

**Answer:** 781.

**Methods:** total probability, tournaments.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2017 AIME II Problem 3: Voronoi region inside a triangle

A point is uniform in the triangle with vertices $(0,0),(12,0),(8,10)$. Find numerator plus denominator of its probability of being closest to $(12,0)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

The relevant perpendicular bisectors are $x=6$ and $y=2x/5+1$. Their intersection is $(6,17/5)$. The favorable region has vertices $(6,0),(12,0),(10,5),(6,17/5)$, with area $109/5$ by the shoelace formula. The whole area is $60$, giving probability $109/300$ and answer $409$.

**Answer:** 409.

**Methods:** geometric probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2017 AIME II Problem 4: Ternary digit avoidance

Count positive integers at most $2017$ with no zero digit in base $3$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Since $2017=2202201_3$, every valid number of at most $6$ digits is allowed, contributing $\sum_{k=1}^6 2^k=126$. A valid $7$-digit numeral must begin $1$ or $21$, giving $2^6+2^5=96$ more. A prefix $22$ forces the next positive digit above the bound. Total $222$.

**Answer:** 222.

**Methods:** digit counting, prefix decomposition.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2017 AIME II Problem 5: Four pair sums force a complementary pair

Four distinct real numbers have six pairwise sums. Four of these are 189,320,287,234; the remaining two are $x,y$. Find the greatest possible $x+y$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Let the four numbers sum to $T$. Their six pair sums split into three complementary pairs, each totaling $T$: $(a+b,c+d)$, $(a+c,b+d)$, $(a+d,b+c)$. Among the four known sums, two must belong to one complementary pair by pigeonhole. Hence $T$ is at most the sum of the two largest known values, $320+287=607$. All six sums total $3T$, so $x+y=3T-(189+320+287+234)\le791$. Equality is attained by the distinct numbers $103/2,275/2,365/2,471/2$: their four specified sums are 189,234,287,320 and the remaining sums are 373,418. Therefore the maximum is 791.

**Answer:** 791.

**Methods:** complementary edge matchings, pigeonhole principle, equality construction.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. The complementary-pair argument proves the upper bound; several sources assume the unknown sums are the two largest without establishing it. An explicit four-number witness proves that the upper bound is attainable.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2017 AIME II Problem 9: An eight-edge bipartite covering

Choose $8$ cells of a $7$ by $7$ board uniformly, conditional on hitting every row and column. Find numerator plus denominator of the probability one cell can be removed while still hitting all rows and columns.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Exactly one row and one column have degree $2$; fix them. Removal is possible precisely when their intersection is chosen. In that case choose its two other neighbors in $6^2$ ways and match the five remaining rows and columns: $6^2\cdot5!=4320$. Otherwise each special vertex chooses two neighbors, giving $\binom62^2\cdot4!=5400$. The conditional probability is $4320/(4320+5400)=4/9$; answer $13$.

**Answer:** 013.

**Methods:** bipartite graphs, conditional probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 7 of 7. Indices in the data are zero-based.

**Status:** solved.

## 2017 AIME II Problem 11: Strong tournaments on five vertices

Orient every edge of $K_5$. Count orientations in which every vertex can reach every other vertex.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

A tournament that is not strongly connected has a linearly ordered sequence of strongly connected components. A nontrivial component has at least $3$ vertices, so for $5$ vertices failure forces a singleton initial or final component: a source or sink. There are $5\cdot2^6$ source tournaments and equally many sink tournaments. A source-sink pair occurs in $5\cdot4\cdot2^3$ orientations. Thus $1024-640+160=544$.

**Answer:** 544.

**Methods:** tournaments, strong connectivity, inclusion-exclusion.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2017 AIME II Problem 13: Isosceles triangles in regular polygons

Let $f(n)$ count isosceles vertex triangles of a regular $n$-gon, including equilateral ones. Find the sum of $n\ge 3$ satisfying $f(n+1)-f(n)=78$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Choose the apex and equally distant vertices, then correct equilateral overcounting: $f(n)=n\lfloor(n-1)/2\rfloor-(2n/3)[3\mid n]$. For residues $n\equiv0,1,2,3,4,5 \pmod{6}$, the differences are respectively $13n/6, (n-1)/2, (5n-4)/6, (7n-3)/6,3n/2,(-n-7)/6$. Solving and enforcing each residue leaves $n=36,157,52$. Their sum is $245$.

**Answer:** 245.

**Methods:** geometry counting, periodic cases.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2017 AIME II Problem 14: Lines containing exactly eight lattice points

In $\{1,\ldots,10\}^3$ count lines containing exactly $8$ grid points.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

A primitive direction has coordinate steps in $\{0,\pm 1\}$; any larger coordinate step permits at most $5$ points. Axis-parallel lines have $10$ points. For two nonzero coordinates there are $3\cdot2=6$ unoriented directions. Each has $2$ offsets of length $8$ in its coordinate square and $10$ choices of constant coordinate, giving $120$. For three nonzero coordinates there are $4$ unoriented directions. After reflecting to $(1,1,1)$, the initial point lies in $\{1,2,3\}^3$ with minimum $1$ and maximum $3:3^3-2\cdot2^3+1=12$ choices. Thus $120+4\cdot12=168$.

**Answer:** 168.

**Methods:** lattice lines, primitive directions.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2018 AIME I Problem 1: Integer-root quadratics counted by a sum

Count modulo $1000$ pairs $(a, b)$ with $1\le a\le 100, b\ge 0$ for which $x^2+ax+b$ splits over the integers.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

Write $(x+u)(x+v)$, where $0\le u\le v$ and $u+v=a$. These unordered roots uniquely determine $(a, b)$. For fixed $a$ there are $\lfloor a/2\rfloor+1$ choices. Hence the count is $\sum_{a=1}^{100}(\lfloor a/2\rfloor+1)=2500+100=2600$; remainder $600$.

**Answer:** 600.

**Methods:** lattice point counting, algebra hybrid.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All nine source solutions inspected. Root-pair counting, triangular lattice points, stars and bars with diagonal correction, and discriminant parity agree on 2600. Several alternatives have harmless endpoint/notational slips: the discriminant version excludes c=0 in words while its formula includes it; one stars-and-bars version writes modulo 100 instead of 1000. The independent proof counts equal roots and zero roots correctly.

**Archived alternatives reviewed:** 9 of 9. Indices in the data are zero-based.

**Status:** solved.

## 2018 AIME I Problem 3: Contiguous color blocks in a sample

Randomly order five cards drawn without replacement from five red and five green cards. Find numerator plus denominator of the chance that each color appears in at most one block.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

Write $(5)_r=5!/(5-r)!$. For a fixed red count $r$ with $1\le r\le 4$, there are two valid color words, each realized in $(5)_r(5)_{5-r}$ labeled draws. For $r=0,5$ there is one word each. Thus the probability is $[2\cdot5!+2\sum_{r=1}^4(5)_r(5)_{5-r}]/(10)_5=31/126$; answer $157$.

**Answer:** 157.

**Methods:** multiset sampling, runs, probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All six sources inspected. Counting full ten-card color words avoids treating five-card color patterns as equally likely. Labeled-card and conditional-probability alternatives give the same 31/126.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2018 AIME I Problem 7: Isosceles triangles in a hexagonal prism

A right regular hexagonal prism has base side $1$ and height $2$. Count isosceles triangles among its $12$ vertices.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Each base has $6$ triangles of side pattern $(1,1,\sqrt3)$ and $2$ equilateral triangles, giving $16$. In a mixed triangle, choose its solitary vertex on one base in $12$ ways. From that vertex, two vertices on the other base can be symmetric one step or two steps away ($2$ choices), or they can be the directly opposite-base vertex and its diametrical partner ($1$ choice, because both the height and base diameter equal $2$). These exhaust equal-distance possibilities. Total $16+12\cdot3=52$.

**Answer:** 052.

**Methods:** geometry counting, distance classes.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All six sources inspected. Counting equal-distance neighbor pairs at each apex gives 60, then subtracting twice each of four equilateral triangles gives 52. Some alternative geometric casework is informal; index 2 calls the equilateral side length 1 although it is sqrt 3. The independent distance-multiplicity argument is complete.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2018 AIME I Problem 9: Two prescribed pair sums

Count four-element subsets of $[20]$ having a pair summing $16$ and a pair summing $24$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

There are $7$ edges of sum $16$ and $8$ of sum $24$. Choosing disjoint edges gives $56-10=46$ different sets. If they meet at $a$, the three vertices are $\{a,16-a,24-a\}$; exactly $10$ values $a=4,\ldots,15$ other than $8,12$ work. Each allows $17$ fourth vertices. Six resulting sets are counted twice: $\{1,7,9,15\},\{2,6,10,14\},\{3,5,11,13\},\{5,11,13,19\},\{6,10,14,18\},\{7,9,15,17\}$. The disjoint-edge case cannot overlap this case, since then cancellation would force equal distinct vertices. Total $46+170-6=210$.

**Answer:** 210.

**Methods:** overcount correction, graph edges.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All three sources inspected. They split disjoint sum-pairs from overlapping sum-pairs and remove six duplicated four-sets. The independent count was exhaustively checked over all 4845 four-subsets.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2018 AIME I Problem 10: Directed walk on two pentagonal rings

Two five-vertex cycles have opposite one-way orientations and bidirectional matching spokes. Count modulo $1000$ fifteen-step walks returning to a fixed start.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

A returning walk uses an even number $2s$ of spokes. Write $u, v$ for moves on the starting and opposite rings. Then $u+v+2s=15$ and $u-v$ is divisible by $5$. For $s>0$ the run slots give $\binom{u+s}{s}\binom{v+s-1}{s-1}$ walks. For $s=0$ only the $15$-move ring traversal returns. Summing the cases $u-v=5$ and $-5$ with Vandermonde gives $\binom{14}5$ and $\binom{14}4$; differences $\pm 15$ contribute only the no-spoke walk. Therefore $1+2002+1001=3004$, remainder $4$.

**Answer:** 004.

**Methods:** walks, run decomposition, Vandermonde identity.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All six sources inspected. Binary destination-ring encoding, state recurrences, and spoke-run compositions lead to 3004. Source index 3 has an inconsistent A_0 value, and index 5 treats the position-dependent transitions as commuting complex multiplications without justification; that shortcut is not relied on. The independent proof counts runs between spoke transitions.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2018 AIME I Problem 12: Subset sums modulo three

Choose a subset of $[18]$ uniformly. Find the numerator of its reduced probability of having sum divisible by $3$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

The six multiples of $3$ do not affect the probability. Pair the six residue $1$ entries with the six residue $2$ entries. A pair contributes residues $0,1,2$ with multiplicities $2,1,1$. If $A_k$ counts residue $0$ choices among $k$ pairs and $B_k$ either nonzero residue, then $A_k+2B_k=4^k$ and $A_k-B_k=1$. Thus $A_6=(4^6+2)/3=1366$. The probability is $1366/4^6=683/2048$; requested numerator $683$.

**Answer:** 683.

**Methods:** residue states, generating functions.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All thirteen sources inspected. Roots-of-unity filtering, residue convolution, Vandermonde sums, and block recurrences all prove the count. Indices 9 and 10 are empirical pattern/answer guesses, not proofs. Source index 6 pairs wrong residue-count classes, but their equal cardinalities conceal the error. The independent root-of-unity calculation is valid.

**Archived alternatives reviewed:** 13 of 13. Indices in the data are zero-based.

**Status:** solved.

## 2018 AIME I Problem 14: First arrival on a heptagon

A walk starts at $S$ on a seven-cycle whose target $E$ is three edges away in one direction and four in the other. Count walks reaching $E$ for the first time within $12$ steps.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Cut at $E$ to obtain positions $0,\ldots,7$, absorbing at $0$ and $7$, and start at $3$. Let $v_0(3)=1$, other entries $0$; for $1\le j\le 6$ set $v_{t+1}(j)=v_t(j-1)+v_t(j+1)$, with boundary values $0$. First arrivals at step $t+1$ are $v_t(1)+v_t(6)$. For $t=0,\ldots,11$ these are $0,0,1,1,3,4,9,14,28,47,89,155$. Their sum is $351$.

**Answer:** 351.

**Methods:** absorbing walks, dynamic programming.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both sources inspected. The absorbing-path transfer count and the shorter endpoint recurrence agree on first-arrival counts 0,0,1,1,3,4,9,14,28,47,89,155, summing 351.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2018 AIME II Problem 6: Random parameter with four real roots

For $a$ chosen uniformly in $[-20,18]$, find numerator plus denominator of the probability that $x^4+2ax^3+(2a-2)x^2+(-4a+3)x-2$ has only real roots.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

The polynomial factors as $(x-1)(x+2)(x^2+(2a-1)x+1)$. The last factor has real roots iff $(2a-1)^2\ge 4$, equivalent to $a\le -1/2$ or $a\ge 3/2$. Only an interval of length $2$ within the length $38$ sample space fails. Probability $18/19$; answer $37$.

**Answer:** 037.

**Methods:** continuous probability, algebra hybrid.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The sole source determines parameter intervals by the two quadratic branches of the absolute value. The original solution uses the same root-counting condition.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2018 AIME II Problem 8: Axis jumps of sizes one and two

Count paths from $(0,0)$ to $(4,4)$ using steps $(1,0),(2,0),(0,1),(0,2)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Let $F(i, j)=0$ for negative coordinates, $F(0,0)=1$, and otherwise $F(i, j)=F(i-1, j)+F(i-2, j)+F(i, j-1)+F(i, j-2)$. The last-step alternatives are disjoint and exhaustive. Rows $j=0,\ldots,4$ are $(1,1,2,3,5),(1,2,5,10,20),(2,5,14,32,71),(3,10,32,84,207),(5,20,71,207,556)$. Answer $556$.

**Answer:** 556.

**Methods:** lattice paths, dynamic programming.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All four sources inspected. Multinomial move types, interleaving coordinate compositions, and a four-predecessor grid recurrence agree on 556.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2018 AIME II Problem 10: Functions whose second image is fixed

Count maps $f:[5]\to [5]$ satisfying $f^2=f^3$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

The functional graph has fixed roots and trees of depth at most $2$. Choose $k\ge 1$ roots, then $j$ of the $5-k$ other vertices that map directly to roots; choose their images in $k^j$ ways. Every remaining vertex maps to one of these $j$ vertices, in $j^{5-k-j}$ ways. This classification is unique. Thus $\sum_{k=1}^5\binom5k\sum_{j=0}^{5-k}\binom{5-k}j k^j j^{5-k-j}=205+380+150+20+1=756$, with $0^0=1$.

**Answer:** 756.

**Methods:** functional graphs, labeled structures.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All three sources inspected. Functional graphs have only fixed-point cycles and depth at most two. Fixed-point casework and the three-level allocation formula both give 756.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2018 AIME II Problem 11: Indecomposable permutations

Count permutations of $[6]$ such that no proper initial block contains precisely its smallest $k$ labels.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Let $c_n$ be the number of indecomposable permutations of $[n]$. Every permutation has a unique shortest nonempty initial block containing $[ k ]$; that block is indecomposable and the suffix arbitrary. Hence $n!=\sum_{k=1}^n c_k(n-k)!$, so $c_n=n!-\sum_{k<n}c_k(n-k)!$. Starting $c_1=1$ gives $c_2=1, c_3=3, c_4=13, c_5=71, c_6=461$.

**Answer:** 461.

**Methods:** canonical decomposition, recurrences.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All six sources inspected. First or last closed-prefix decomposition gives indecomposable-permutation recurrence; inclusion-exclusion gives the same 461. Source index 5 has a 12/21 prefix typo and describes the complement ambiguously; the independent first-component decomposition avoids those ambiguities.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2018 AIME II Problem 13: Parity of waiting for a die pattern

Roll a fair die until $123$ first appears in consecutive rolls. Find numerator plus denominator of the chance the stopping time is odd.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Let $h_j=E[(-1)^T]$ for additional time $T$, where $j=0,1,2$ is the currently matched prefix length. First-step conditioning yields $h_0=-(5h_0+h_1)/6, h_1=-(4h_0+h_1+h_2)/6, h_2=-(4h_0+h_1+1)/6$. Solving gives $h_0=-1/431$. Since $h_0=P(T\text{ even})-P(T\text{ odd})$, the odd probability is $216/431$ and the answer $647$.

**Answer:** 647.

**Methods:** pattern automata, probability generating functions.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All eight sources inspected. Prefix-state Markov chains and the nonoverlap avoidance recurrence are sound. Source index 1 asserts an unsupported ratio shift; indices 5 and 7 incorrectly treat disjoint three-roll blocks as detecting all occurrences, missing occurrences across boundaries. Their numerical agreement is not a proof. The independent parity transform of the correct prefix automaton gives 216/431.

**Archived alternatives reviewed:** 8 of 8. Indices in the data are zero-based.

**Status:** solved.

## 2018 AIME II Problem 15: Integer bi-Lipschitz sequences

Count integer-valued functions on $\{0,\ldots,6\}$ with $f(0)=0, f(6)=12$ and $|x-y|\le |f(x)-f(y)|\le 3|x-y|$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Adjacent increments lie in $\{\pm 1,\pm 2,\pm 3\}$. Two negative increments would make the total at most $10$, so there is at most one. With none, the coefficient $[x^{12}](x+x^2+x^3)^6$ is $141$. A $-2$ increment is impossible by the two-step lower bound. A $-3$ increment would force an adjacent $+1$, making the total at most $-3+1+4\cdot3=10$, also impossible. Thus the only negative increment can be $-1$, and its neighbors must be $3$. If the negative step is at an end, the remaining four positive steps sum $10$, with $10$ choices; two ends give $20$. At an internal position, two neighbors are $3$, and three remaining positive steps sum $7$, with $6$ choices; four positions give $24$. These local conditions also ensure every longer interval has sum at least its length. Total $141+20+24=185$.

**Answer:** 185.

**Methods:** bounded compositions, local constraints.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All three sources inspected. Increment classification and bounded stars-and-bars counts give 141 positive-increment cases and 44 one-negative cases. The audit repaired a small independent-proof gap: an increment−3 can pair with+1 locally, but then the total is at most 10, contradicting 12;−2 fails the local two-step bound. The remaining negative step is−1 with adjacent+3 values.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2019 AIME I Problem 2: A gap between ordered samples

Choose distinct $J, B$ uniformly from $[20]$ in order. Find numerator plus denominator of $P(B-J\ge 2)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

Symmetry gives $P(B>J)=1/2$. There are $19$ adjacent increasing pairs among $380$ ordered pairs, so the desired probability is $1/2-19/380=9/20$. Answer $29$.

**Answer:** 029.

**Methods:** symmetry, probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The symmetry, order-statistic, and direct pair counts agree; the original proof specifies the uniform subset model.

**Archived alternatives reviewed:** 7 of 7. Indices in the data are zero-based.

**Status:** solved.

## 2019 AIME I Problem 4: Ordered substitutions

A team has $11$ active players and $11$ unused substitutes. Count modulo $1000$ histories with at most $3$ successive substitutions, with removed players unable to return.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

At substitution $j$ there are $11$ choices of departing active player and $12-j$ unused entrants, irrespective of previous choices. Thus the count is $\sum_{k=0}^3 11^k(11)_k=1+121+13310+1317690$. The last two terms sum to a multiple of $1000$, leaving $122$.

**Answer:** 122.

**Methods:** sequential counting, falling factorials.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All three source counts track histories of substitutions; the choices of departed players and unused replacements are distinguished.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2019 AIME I Problem 5: Hitting the corner before either axis

From $(4,4)$, independently subtract $(1,0),(0,1)$, or $(1,1)$, each with probability $1/3$, until an axis is reached. Write the chance of first hitting $(0,0)$ as $m/3^n$ with $3$ not dividing $m$. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

The final move must be diagonal from $(1,1)$. Before it, choose $d$ diagonal moves, $0\le d\le3$, and $3-d$ moves of each axis type. Monotonicity ensures these paths stay positive. Thus the probability is $\sum_{d=0}^3\frac{(6-d)!}{(3-d)!^2d!}3^{-(7-d)}=245/2187$. Therefore $m+n=245+7=252$.

**Answer:** 252.

**Methods:** lattice paths, multinomial counting, probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The path recurrence and ballot decompositions agree. Source 0 writes P(y,0) where the second boundary should read P(0,y).

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2019 AIME II Problem 2: Hitting a site with jumps one and two

A frog starts on $1$ and independently advances $1$ or $2$ with equal probabilities. Find numerator plus denominator of its chance of visiting $7$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

For remaining distance $d$, let $p_0=1,p_{-1}=0$ and $p_d=(p_{d-1}+p_{d-2})/2$. Last-jump conditioning proves the recurrence. Values for $d=1$ through $6$ are $1/2,3/4,5/8,11/16,21/32,43/64$. Thus the answer is $107$.

**Answer:** 107.

**Methods:** hitting probabilities, recurrences.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The recurrence and parity decompositions agree. Conditioning is on the first jump from the remaining distance, not the last jump.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2019 AIME II Problem 3: Overlapping products of seven integers

Count positive integer tuples $(a, b, c, d, e, f, g)$ satisfying $abc=70, cde=71, efg=72$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

Since $71$ is prime and divides neither $70$ nor $72$, necessarily $c=e=1,d=71$. The independent choices are $ab=70$ and $fg=72$, giving $\tau(70)\tau(72)=8\cdot12=96$.

**Answer:** 096.

**Methods:** product rule, divisor distributions.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both factorizations reduce to the same finite exponent count.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2019 AIME II Problem 4: A square product of four die rolls

Find numerator plus denominator of the probability that four fair die outcomes have square product.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

The number of fives must be $0,2$, or $4$. On the other five faces, parity of prime exponents gives four states: the zero state has $2$ labels $(1,4)$, each other state one. If $a_k$ counts square products, $a_0=1$ and $a_{k+1}=a_k+5^k$, hence $a_2=7,a_4=157$. The favorable count is $157+\binom42 7+1=200$. Probability $200/6^4=25/162$; answer $187$.

**Answer:** 187.

**Methods:** parity vectors, recurrence, probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Parity recurrence and exhaustive casework agree. The final two stored alternatives were read in the separate 2023 audit supplement. Indices 5 and 6 reviewed. The minimal square-product blocks are single squares, equal nonsquare pairs, and the triple 2,3,6; their length-four casework gives 200. The parity-generating-function alternative is multiplication in the group algebra with x^2=y^2=z^2=1, and its constant coefficient is also 200. Both support 25/162.

**Archived alternatives reviewed:** 8 of 8. Indices in the data are zero-based.

**Status:** solved.

## 2019 AIME II Problem 5: Ambassadors with adjacent advisors

Four distinct ambassador-advisor pairs occupy $12$ labeled cyclic chairs. Ambassadors use even chairs; each advisor must neighbor their ambassador. Count modulo $1000$ valid seatings.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Choose the two unused even chairs. If these are adjacent on the six-cycle, separated by one chair, or opposite, there are $6,6,3$ choices. Occupied even-chair runs then have lengths $4$; $3,1$; or $2,2$. A run of $r$ ambassadors has $r+1$ adjacent odd seats, and choosing the one unused odd seat uniquely determines its advisor matching, so contributes $r+1$. Assign ambassadors in $4!$ ways. Total $4![6\cdot5+6\cdot4\cdot2+3\cdot3^2]=2520$, remainder $520$.

**Answer:** 520.

**Methods:** runs, cyclic arrangements, matchings.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All five arrangements count the same two-advisor boundary condition; the circular-edge and linear-run bijections provide independent viewpoints.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2019 AIME II Problem 10: A tangent sign itinerary fixes every binary digit

An angle $0<\theta<90^\circ$ has $\tan(2^n\theta)>0$ precisely when $3\mid n$, and negative otherwise, for every integer $n\ge0$. Write $\theta=p/q$ degrees in lowest terms and find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Put $t=\theta/180\in(0,1/2)$. The sign of $\tan(180\cdot2^nt)$ is positive when the fractional part of $2^nt$ lies below 1/2, and negative when it lies above 1/2. In a binary expansion, this reads the next digit:0 for positive,1 for negative. No dyadic endpoint is allowed, because tangent there is zero or undefined. Thus the unique expansion is $t=0.\overline{011}_2=3/(2^3-1)=3/7$. Hence $\theta=540/7$ degrees and the answer is 547.

**Answer:** 547.

**Methods:** binary expansion, doubling dynamics, trigonometric signs.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. The binary-digit argument proves uniqueness. Several sources infer periodic angles directly from periodic signs without proof; that implication requires the complete itinerary, supplied here.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2019 AIME II Problem 12: Divisibility chains with prescribed sum

Count finite strictly increasing positive integer sequences, each term dividing the next, whose sum is $360$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Let $h(N)$ count such chains summing $N$ with first term at least $2$; set $h(0)=1,h(1)=0$. Removing first term $d$ and dividing the suffix by $d$ is a bijection, so $h(N)=\sum_{d\mid N,d\ge2}h(N/d-1)$. Allowing first term $1$ gives total $\sum_{d\mid360}h(360/d-1)$. Its nontrivial values are $h(119)=6,h(44)=8,h(39)=6,h(35)=4,h(14)=3,h(9)=2,h(8)=2,h(4)=1$; all remaining divisor terms sum $15$. Total $47$.

**Answer:** 047.

**Methods:** divisor recurrences, canonical normalization.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The source recurrence is valid with its initial values and the summation of partial chains; the new exposition makes those values explicit.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2019 AIME II Problem 14: A three-denomination Frobenius problem

With unlimited stamps of denominations $5, n, n+1$, the largest unattainable value is $91$. Find the sum of possible $n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

If $n\le23$, one of $n, n+1$ is coprime to $5$ with value at most $23$(or at most $21$ when $5$ divides $n$); the two-denomination Frobenius bound is then at most $87$. Hence $n\ge24$. Since $96$ is attainable but $91$ is not, a representation of $96$ uses no $5$-stamp. Using at most $4$ other stamps forces $n\in\{24,31,32,47,48,95,96\}$. For $31$ and $32,91$ is attainable; $48$ cannot make $92$; $95$ and $96$ cannot make $92$. Values $24$ and $47$ fail at $91$ but make every value $92$ through $96$, after which adding $5$ covers all larger values. Sum $71$.

**Answer:** 071.

**Methods:** numerical semigroups, residue classes.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Several alternatives skip coprimality or finite-case justification. The original proof makes the choice of a denomination coprime to 5 explicit and checks the remaining candidates.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2020 AIME I Problem 5: One deletion makes a permutation monotone

Count permutations of $[6]$ from which deleting one entry leaves an increasing or decreasing sequence.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

For increasing order, start with $123456$ and move one selected entry to one of its $5$ other positions. This gives $30$ constructions. Every nonidentity permutation has a unique movable entry except an adjacent transposition, which has two; there are $5$ such transpositions. Indeed, if either of two different entries can be removed, every inversion must involve both of them; the sole inversion then swaps adjacent values in adjacent positions. Including the identity gives $30-5+1=26$. Reversing gives $26$ decreasing cases. The two families are disjoint: increasing and decreasing subsequences of length $5$ in a length $6$ permutation would overlap in at least $4$ positions, impossible for opposite orders. Total $52$.

**Answer:** 052.

**Methods:** insertion-deletion bijection, overcount correction.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All 12 stored entries read. Several count insertion histories without fully proving their only collisions; the adjacent-swap exception and disjointness of ascending/descending families are the key checks. Source 10 needs a stronger argument than merely having one descent.

**Archived alternatives reviewed:** 12 of 12. Indices in the data are zero-based.

**Status:** solved.

## 2020 AIME I Problem 7: A balanced committee bijection

Choose a committee from $11$ men and $12$ women with exactly one more woman than man. Find the sum of distinct prime divisors of the number of committees.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Replace the selected men by the unselected men. The transformed selection always contains $12$ people; this is invertible. Thus there are $\binom{23}{12}$ committees. Its factorization is $2\cdot7\cdot13\cdot17\cdot19\cdot23$, whose distinct primes sum $81$.

**Answer:** 081.

**Methods:** complement bijection, Vandermonde identity.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The complementary-selection bijection, Vandermonde sums, and prime factorization agree.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2020 AIME I Problem 9: A random chain of divisors

Independently sample three divisors $a, b, c$ of $20^9$ uniformly with replacement. Find the reduced numerator of $P(a\mid b\text{ and }b\mid c)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Write divisors as $2^u5^v$, with $0\le u\le18,0\le v\le9$. Divisibility requires weakly increasing triples separately in both coordinates. The numbers of such triples are $\binom{21}3$ and $\binom{12}3$ by stars and bars. Probability $\binom{21}3\binom{12}3/190^3=77/1805$; numerator $77$.

**Answer:** 077.

**Methods:** order-preserving tuples, stars and bars, probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The shifted strictly increasing triples, stars and bars, and equality-case split give the same probability.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2020 AIME I Problem 11: Counting coefficients through common images

For integer $a, b, c$ in $[-10,10]$, set $f(x)=x^2+ax+b$ and $g(x)=x^2+cx+d$. Count triples for which an integer $d$ makes $g(f(2))=g(f(4))=0$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

If $a=-6$, the two images coincide and every $b, c$ admits the integer choice $d=-f(2)^2-cf(2)$, giving $441$. Otherwise the two images are the roots of $g$, so $c=-20-6a-2b$; the constraint is $-15\le3a+b\le-5$. The exact sum $\sum_{a=-10,a\ne-6}^{10}\max(0,\min(10,-5-3a)-\max(-10,-15-3a)+1)=69$. Hence $441+69=510$.

**Answer:** 510.

**Methods:** bounded lattice counting, algebra hybrid.

**Verification:** The displayed interval sum was evaluated exactly and gives 69.

**Source comparison:** All three entries separate the coincident-image case correctly; the third includes an explicit 69-term-case subtotal table.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2020 AIME II Problem 2: A random slope in a square

Choose $P$ uniformly in the unit square. Find numerator plus denominator of the chance that its slope from $(5/8,3/8)$ is at least $1/2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

The comparison line is $y=x/2+1/16$. For $x<5/8$ choose points below it; for $x>5/8$ choose points above it. The two trapezoid areas total $\frac12(1/16+3/8)(5/8)+\frac12(5/8+7/16)(3/8)=43/128$. Answer $171$.

**Answer:** 171.

**Methods:** geometric probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both area decompositions agree. The vertical line has measure zero and does not affect the probability.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2020 AIME II Problem 8: Zeros of nested absolute values form a parity interval

Let $f_1(x)=|x-1|$ and $f_n(x)=f_{n-1}(|x-n|)$ for n>1. Find the least n for which the sum of the distinct real zeros of $f_n$ exceeds 500000.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Inductively the zero set is the arithmetic progression from $n-n(n-1)/2$ to $n+n(n-1)/2$, with step 2. For the induction, zeros of $f_n$ are n plus or minus the nonnegative zeros of $f_{n-1}$. Those nonnegative zeros start at 0 or 1 and end at $n(n-1)/2$, so their positive and negative reflections fill exactly the asserted parity interval; the initial cases n=1,2 are immediate. There are $1+n(n-1)/2$ zeros and their average is n. Their sum is $n(n^2-n+2)/2$, strictly increasing for positive n. At n=100 it is 495100; at n=101 it is 510151. Thus the least n is 101.

**Answer:** 101.

**Methods:** absolute-value preimages, arithmetic zero sets, induction.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. The first gives an induction, while the second infers the pattern from initial terms. Explicitly identifying the nonnegative part and its reflected parity interval completes the induction.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2020 AIME II Problem 9: Avoiding former neighbors

Six people formerly sat in order $123456$. Count new orders in which no formerly adjacent pair is adjacent.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Apply inclusion-exclusion to the five path edges. A chosen edge subset with $k$ edges and $r$ nonempty runs contracts to $6-k$ blocks, with $2^r(6-k)!$ orders. There are $\binom{k-1}{r-1}\binom{6-k}{r}$ such subsets. Therefore the answer is $6!+\sum_{k=1}^5(-1)^k(6-k)!\sum_r2^r\binom{k-1}{r-1}\binom{6-k}{r}=90$. The run count follows by composing $k$ into $r$ positive lengths and placing gaps between them.

**Answer:** 090.

**Methods:** inclusion-exclusion, block contraction.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 1 has a sign/bracket error in its final PIE display although its component counts are correct. Other entries either list cases or derive a valid recurrence. The new run-of-edges PIE formula avoids long casework.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2020 AIME II Problem 12: A line crossing a numbered grid

An odd $m$ by odd $n$ row-major grid has label $200$ in its top row and $2000$ in its bottom row. Count $(m, n)$ for which the line through those cell centers enters cell $1099$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

The midpoint of the two centers is the center of cell $1100$; cell $1099$ is immediately left in the same middle row. Thus the line enters its interior exactly when its slope has absolute value below $1$: $|1800-(m-1)n|>m-1$. The endpoint-row requirements give $m=3,5,7,9$. Their odd $n$ ranges and exclusions are respectively $667\ldots999$ excluding $899,901$; $401\ldots499$ excluding $449,451$; $287\ldots333$ excluding $299,301$; $223\ldots249$ excluding $225$. Counts $165,48,22,13$ sum $248$.

**Answer:** 248.

**Methods:** lattice geometry, casework.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 0 states an imprecise modular slope criterion. Source 1 and the new proof use the signed horizontal displacement and exclude slopes of absolute value 1.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2020 AIME II Problem 14: Iterated fractional-part preimages

Define $f(x)=x\{x\}$, where $\{x\}=x-\lfloor x\rfloor$. Count modulo $1000$ the solutions of $f(f(f(x)))=17$ in $[0,2020]$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

On each interval $[k,k+1)$, $f$ increases continuously from $0$ to the excluded endpoint $k+1$. For positive $y$, there is exactly one preimage in that interval iff $k+1>y$. Starting at $y=17$, the first branch index $k$ is at least $17$; its preimage lies strictly between $k$ and $k+1$, so each next branch index is at least the previous one. All three indices are at most $2019$. Consequently solutions correspond bijectively to weakly increasing triples from $2003$ integers. Their count is $\binom{2005}3$, with remainder $10$.

**Answer:** 010.

**Methods:** inverse branches, combinations with repetition.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All three branch-count arguments agree. The endpoint 2020 is excluded because its iterates are 0; positive target 17 avoids the separate zero-level issue.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2021 AIME I Problem 1: One loss in a persistent two-state process

Zou wins race $1$. Thereafter the previous winner wins the next race with probability $2/3$. Find numerator plus denominator of the chance Zou wins exactly $5$ of $6$ races.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

If the unique loss is race $2,3,4$, or $5$, there are two switches and three repetitions, each pattern having probability $(1/3)^2(2/3)^3$. A loss in race $6$ has probability $(1/3)(2/3)^4$. Total $4\cdot8/243+16/243=16/81$; answer $97$.

**Answer:** 097.

**Methods:** Markov chains, weighted words.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Sources 2 and 3 mislabel which race is lost in places, but their pattern probabilities agree. The new proof labels the unique loss by its actual race number.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2021 AIME I Problem 3: Differences of powers of two

Count positive integers below $1000$ expressible as a difference of integral powers of $2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

For an integral positive difference the exponents must be nonnegative; a negative smaller exponent would leave an odd numerator over a power of $2$. Write $2^b(2^{a-b}-1)$ with $a>b$. The $2$-adic valuation uniquely determines $b$, and then a, so no duplicates arise. Necessarily $a\le 10$. Of the $\binom{11}2=55$ exponent pairs, only $a=10, b=0,1,2,3,4$ exceed $999$. Thus $50$.

**Answer:** 050.

**Methods:** unique representations, valuation counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 3 claims geometric sequences always have distinct differences, which is not a valid general principle. Binary valuation gives the required uniqueness for this sequence; source 0 also supplies it.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2021 AIME I Problem 4: Three strictly increasing piles

Count integer triples $0<a<b<c$ with $a+b+c=66$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Fix $a$. Then $a+1\le b\le\lfloor(65-a)/2\rfloor$, and $c$ is determined. Necessarily $1\le a\le 21$. Thus the count is $\sum_{a=1}^{21}(\lfloor(65-a)/2\rfloor-a)$. Separating odd and even $a$ gives $176+155=331$.

**Answer:** 331.

**Methods:** partitions, floor sums.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The direct floor sum, gap variables, and equality-case subtraction agree. Source 1 initially describes weakly ordered triples but actually starts from all ordered positive triples.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2021 AIME I Problem 7: Simultaneous sine maxima

Count $1\le m<n\le 30$ for which some real $x$ satisfies $\sin(mx)+\sin(nx)=2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Both sines must be $1$. After removing the common power of $2$ from $m, n$, this is possible exactly when the remaining odd parts are congruent modulo $4$. Necessity follows from $m/n=(4u+1)/(4v+1)$ after reducing; sufficiency follows by multiplying equal odd residues by $1$ or $3$ to make both $1$ modulo $4$. Partition $1\ldots30$ by $2$-adic valuation and odd part modulo $4$. Class sizes are $8,7$; $4,4$; $2,2$; $1,1$; $1$. The answer is $\binom82+\binom72+2\binom42+2\binom22=63$.

**Answer:** 063.

**Methods:** equivalence classes, trigonometry hybrid.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 0 makes an invalid claim that its scale k>1 must be integral; source 1 contains an unrelated corrupted paragraph; source 2 leaves a 14-pair count unexplained. Equal 2-adic valuations and equal odd residues mod 4 give the clean necessary-and-sufficient criterion.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2021 AIME I Problem 8: Counting levels with twelve preimages

Count integers $c$ for which $||20|x|-x^2|-c|=21$ has $12$ distinct real solutions.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

For $h(x)=|20|x|-x^2|$, a horizontal level $t$ has $6$ preimages exactly when $0<t<100$, and fewer otherwise. The equation uses disjoint levels $t=c-21$ and $c+21$. Twelve preimages require both levels in $(0,100)$, equivalently $21<c<79$. There are $57$ integers.

**Answer:** 057.

**Methods:** preimage counting, algebra hybrid.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 1 repeats x=10 where its second zero should be 20. Source 3 calls the square root the discriminant and does not fully impose the signs introduced by absolute values. Horizontal-level multiplicity gives the rigorous count.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2021 AIME I Problem 10: A rational recurrence reduces at its first shared prime

Start with $a_1=2020/2021$. When $a_k=m/n$ is reduced with positive integers m,n, define $a_{k+1}=(m+18)/(n+19)$. Find the sum of all j for which $a_j=t/(t+1)$ for a positive integer t.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

Start at a term $m/(m+1)$. Before any reduction, k further steps give $(m+18k)/(m+1+19k)$, whose numerator-denominator gcd is $\gcd(m-18,k+1)$. If m−18>1, the first reduction occurs at k=p−1, where p is its least prime divisor. The denominator difference k+1 then equals p, so after reduction the next special numerator is $18+(m-18)/p$. Between these reductions the denominator difference exceeds 1 and the fractions are reduced, so no other term is special. Beginning with m=2020, the successive m−18 values are 2002,1001,143,13,1; the primes removed are 2,7,11,13. The special indices are therefore 1,2,8,18,30. Once m−18=1, the gcd is always 1 and no later special term occurs. Their sum is 59.

**Answer:** 059.

**Methods:** Euclidean algorithm, prime-driven reductions, rational recurrence.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. The first source states reducibility as full divisibility of k+1, which is not true in general; the first-event argument works because the first common factor is the least prime divisor. The second source supplies this distinction.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2021 AIME I Problem 12: Three frogs until their first collision

Three independent symmetric walkers begin equally spaced on a $12$-cycle. They stop when two occupy the same vertex. Find numerator plus denominator of their expected stopping time.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Before collision, the unordered cyclic gap types are $A=(4,4,4), B=(2,4,6), C=(2,2,8)$. Enumerating the $8$ simultaneous direction choices gives $E_A=1+(2E_A+6E_B)/8$, $E_B=1+(E_A+4E_B+E_C)/8$, $E_C=1+(2E_B+2E_C)/8$; omitted transitions are collisions. Solving gives $E_B=4,E_A=16/3$. Thus the answer is $19$. A collision has a uniformly positive chance within finitely many steps, justifying finite expectations.

**Answer:** 019.

**Methods:** symmetry reduction, absorbing Markov chains.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 1 claims the expectation for three walkers is one third of the two-walker expectation merely by symmetry; that inference is unjustified. Sources 0 and 2 use valid joint-gap states. The new proof also checks that the expectation is finite.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2021 AIME II Problem 1: Mean of three-digit palindromes

Find the arithmetic mean of all decimal three-digit palindromes.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

Write a palindrome as $101a+10b$, with $a$ uniform on $1,\ldots,9$ and $b$ uniform on $0,\ldots,9$. Linearity gives mean $101\cdot5+10\cdot(9/2)=550$.

**Answer:** 550.

**Methods:** linearity of expectation, digit symmetry.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All six symmetry, pairing, and digit-average arguments agree.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2021 AIME II Problem 3: Cyclic products modulo three

Permute $1,\ldots,5$ around five labeled positions. Count permutations for which the sum of the five products of three cyclically consecutive entries is divisible by $3$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

Choose the position of $3$ in $5$ ways. The three terms containing it vanish modulo $3$; the other two factor as a nonzero product times the sum of the two entries neighboring $3$. These neighbors must have opposite nonzero residues: there are $2\cdot2\cdot2=8$ ordered choices from $\{1,4\}$ and $\{2,5\}$. Arrange the remaining entries in $2$ ways. Total $5\cdot8\cdot2=80$.

**Answer:** 080.

**Methods:** residue classes, cyclic counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All five residue counts agree; the position of 3 is chosen before counting the two nonzero residue classes.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2021 AIME II Problem 6: An equality characterizing nested sets

Count ordered subset pairs $(A, B)$ of $[5]$ with $|A||B|=|A\cap B||A\cup B|$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Let $x=|A\setminus B|, y=|B\setminus A|, z=|A\cap B|$. The equality is $(x+z)(y+z)=z(x+y+z)$, or $xy=0$. Thus one set contains the other. For $A$ contained in $B$, each element has $3$ states, giving $3^5$. Reverse containment gives another $3^5$; equal pairs, numbering $2^5$, were counted twice. Answer $2\cdot3^5-2^5=454$.

**Answer:** 454.

**Methods:** set atoms, inclusion-exclusion.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All six stored entries agree. Entries 3 and 4 are continuations of entry 2, not independent proofs; entry 5 has a summation-index typo.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2021 AIME II Problem 8: Nonbacktracking walk on a cube

On a cube, an ant starts at a bottom vertex, chooses its first edge uniformly, and thereafter uniformly chooses either edge that does not reverse its previous step. Find numerator plus denominator of its chance of being on top after $8$ steps.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Count paths by last-edge types $BB, BT, TB, TT$. Start with $(2,1,0,0)$. If the vector is $(a, b, c, d)$, the next is $(a+2c,a,d,d+2b)$: a horizontal edge allows one horizontal and one vertical continuation, a vertical edge two horizontal continuations. Seven iterations give $(118,66,62,138)$. Thus top probability $(66+138)/(3\cdot2^7)=17/32$, answer $49$.

**Answer:** 049.

**Methods:** memory states, nonbacktracking walks.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 4 multiplies dependent marginal probabilities and therefore gives an invalid derivation, even though cancellation happens to produce the correct linear recurrence. The four last-edge states, or a properly conditioned two-step recurrence, are sufficient.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2021 AIME II Problem 9: Counting exponent pairs by valuations

Count ordered $1\le m, n\le 30$ with $\gcd(2^m+1,2^n-1)>1$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Since $2^m-1$ and $2^m+1$ are coprime, the $\gcd$ condition is equivalent to $\gcd(2m,n)>\gcd(m,n)$, using $\gcd(2^u-1,2^v-1)=2^{\gcd(u,v)}-1$. Thus $v_2(n)>v_2(m)$. The valuation class sizes are $15,8,4,2,1$. Count $15(15)+8(7)+4(3)+2(1)=295$.

**Answer:** 295.

**Methods:** valuation classes, number theory hybrid.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 1 establishes necessity through multiplicative order but does not prove sufficiency. Its auxiliary GCD proof falsely says gcd(d 1,k)=gcd(d 2,k)=1; the valid assertion needed is gcd(xy,k)=1. The prime-exponent GCD factorization in the new proof proves both directions.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2021 AIME II Problem 11: Learning from simultaneous ignorance

Four logical students each know one member of an unknown set of four consecutive two-digit integers. The set has different multiples of $6$ and $7$. Initially none can determine it; hearing this, all can. Find the sum of possible maximum elements.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Form candidate intervals $[t,t+3]$, $10\le t\le 96$, containing distinct multiples of $6$ and $7$. For each visible value $v$, let $d(v)$ count candidate intervals containing $v$. An interval survives the first announcement exactly when all its four $d$ values exceed $1$. Listing these intervals leaves $[34,37],[47,50],[76,79],[89,92]$. They are pairwise disjoint, so each student now identifies the unique surviving interval containing their value. The possible maxima sum $37+50+79+92=258$.

**Answer:** 258.

**Methods:** epistemic elimination, finite sets.

**Verification:** Finite interval enumeration and two announcement filters verified.

**Source comparison:** Entries 0–3 read; entry 4 is only a video link and the video itself was not reviewed. Source 2 final display writes 89 instead of 79 while retaining the correct 258; source 3 contains residue-label typos. The candidate-interval filtering proof makes the information update explicit.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2022 AIME I Problem 4: Roots-of-unity exponent pairs

Let $w=(\sqrt3+i)/2$ and $z=(-1+i \sqrt3)/2$. Count $1\le r, s\le 100$ with $iw^r=z^s$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Polar angles reduce the equation to $r+3\equiv4s\pmod{12}$. Hence $r=4t-3$ for $1\le t\le 25$ and $s=t$ modulo $3$. Among $t$ there are $9$ of residue $1$, and $8$ each of $0,2$; among $s$ there are $34$ of residue $1$, and $33$ each of $0,2$. Count $9\cdot34+16\cdot33=834$.

**Answer:** 834.

**Methods:** residue counting, roots of unity.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both polar-angle reductions give the same residue-class count.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2022 AIME I Problem 6: Avoiding four-term progressions

Count choices $5<a<b<30$ such that $\{3,4,5, a, b,30,40,50\}$ contains no four-term arithmetic progression.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

Values $6$ and $20$ are forbidden individually, leaving $22$ eligible values and $\binom{22}2=231$ pairs. Any further forbidden progression must use both $a, b$ and two fixed terms. Checking the two fixed endpoints or the fixed initial pair yields exactly $(a, b)=(7,9),(12,21),(16,28)$. Other fixed-term pairs yield nonintegers or values outside the allowed range. Thus $231-3=228$.

**Answer:** 228.

**Methods:** forbidden subsets, casework.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 2 defines overlapping A,B,C but subtracts them as disjoint after silently reassigning cases, and prints |C|=65 instead of 5. The other entries and the new proof remove 6,20 first and then exactly three additional pairs.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2022 AIME I Problem 7: A minimal positive ratio of digit products

Partition digits $1$ through $9$ into three ordered triples. Find numerator plus denominator of the least positive value $(abc-def)/(ghi)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

If the numerator is at least $2$, the ratio is at least $2/(7\cdot8\cdot9)>1/288$. For numerator $1$, write $u=v+1$ for the two triple products. Their six distinct factors have product at least $6!=720$, so $v\ge27$. The pair $27,28$ would require the triples $\{1,3,9\}$ and $\{1,4,7\}$, which overlap. Every consecutive pair with lower member $28,\ldots,34$ contains one of $29,31,33,34$, impossible as a product of available digits because it has a prime factor greater than $7$. Products $35,36$ are possible using $\{1,5,7\}$ and $\{2,3,6\}$, leaving denominator $4\cdot8\cdot9=288$. Larger consecutive products have smaller remaining denominator $9!/(uv)$. Hence the minimum is $1/288$, and the answer is $289$.

**Answer:** 289.

**Methods:** extremal counting, product partitions.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 0 omits the impossible overlapping 27/28 factor triples; sources 1–2 rely on search or skip candidates and do not fully prove the minimum. The original proof explicitly eliminates 27/28 and proves that all numerator values at least 2 are worse.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2022 AIME I Problem 9: Two copies in opposite parity positions

Randomly arrange two indistinguishable blocks of each of six colors. Find numerator plus denominator of the probability that every equal-color pair has an even number of intervening blocks.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Each pair must occupy one odd and one even position. Assign the six colors to odd slots and independently to even slots: $(6!)^2$ arrangements. All multiset arrangements number $12!/2^6$. Probability $2^6(6!)^2/12!=16/231$, answer $247$.

**Answer:** 247.

**Methods:** parity bijection, multiset permutations.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All three constructions give the same parity-slot bijection. Source 2 writes a fraction equal to 247, confusing the probability 16/231 with the requested numerator-plus-denominator.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2022 AIME I Problem 12: Summing intersection sizes

Let $S_n$ sum $|A\cap B|$ over ordered equal-sized subset pairs of $[n]$. If $S_{2022}/S_{2021}=p/q$ in lowest terms, find $(p+q) \pmod{1000}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Mark an element of the intersection. It has $n$ choices, and after removing it the residual sets have equal size. Thus $S_n=n\sum_k\binom{n-1}k^2=n\binom{2n-2}{n-1}$. Consequently the ratio is $4044\cdot4041/2021^2$, already reduced since $2021$ is coprime to both factors. The requested remainder is $44\cdot41+21^2\equiv245$.

**Answer:** 245.

**Methods:** pointing, double counting, Vandermonde identity.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All four double counts agree. Source 0 has imprecise residual-subset notation, but its marked-element argument and ratio reduction are correct.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2022 AIME I Problem 13: Distinct reduced numerators

Consider all nonzero repeating four-digit decimals. Count their distinct reduced numerators modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Each fraction has denominator dividing $D=9999=3^2\cdot11\cdot101$. A positive numerator $u$ occurs iff it is at most the largest divisor of $D$ coprime to $u$. If $101$ divides $u$, this bound is at most $99$, impossible. If neither $3$ nor $11$ divides $u$, there are $\varphi(D)=6000$ choices. If $3$ alone divides $u$, the bound $1111$ gives $\lfloor1111/3\rfloor-\lfloor1111/33\rfloor-\lfloor1111/303\rfloor=334$. If $11$ alone divides $u$, the bound $909$ gives $82-27=55$. If both divide $u$, the bound $101$ allows $33,66,99$. Total $6392$, remainder $392$.

**Answer:** 392.

**Methods:** inclusion-exclusion, divisor lattice.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 1 reverses divisibility signs and contains false logical equivalences. Source 0 has imprecise wording about cancellation but its case counts are valid. The new maximal-coprime-divisor criterion states the exact necessary-and-sufficient condition.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2022 AIME II Problem 2: A randomly seeded tournament

Four tennis players include $A, C, J, S$. $C$ beats $A$ with probability $1/3$; $A$ and $C$ each beat $J$ or $S$ with probability $3/4$. Semifinal pairings are uniform. Find numerator plus denominator for $C$ becoming champion.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

With probability $1/3, C$ first meets $A$ and wins the tournament with probability $(1/3)(3/4)$. Otherwise $C$ first beats a weaker player with probability $3/4$, and the other finalist is $A$ with probability $3/4$. Total $\frac13\frac13\frac34+\frac23\frac34(\frac34\frac13+\frac14\frac34)=29/96$. Answer $125$.

**Answer:** 125.

**Methods:** conditioning, tournaments.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The sole source correctly conditions on the semifinal opponent and then on the other semifinal winner.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2022 AIME II Problem 5: Prime-difference triangles

Twenty cyclic vertices are labeled $1,\ldots,20$; connect labels whose ordinary difference is prime. Count triangles with original vertices.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

For increasing labels $x<y<z$, all three gaps must be prime and the largest is the sum of the other two. Thus one smaller gap is $2$, and the other is a twin-prime lower member $p=3,5,11,17$. Each $p$ has two gap orders and $20-(p+2)$ starting labels. Count $2(15+13+7+1)=72$.

**Answer:** 072.

**Methods:** gap encoding, prime parity.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 0 falsely treats 18 starting positions as available for every prime pair and obtains 72 coincidentally. Entry 1 warns about this; entry 2 gives the valid separate spans 15,13,7,1 and both gap orders.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2022 AIME II Problem 8: Identifiability from three floor values

Count positive integers $n\le 600$ uniquely determined among positive integers by $\lfloor n/4\rfloor,\lfloor n/5\rfloor,\lfloor n/6\rfloor$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

The common fiber is a consecutive integer interval. It is a singleton exactly when a floor jumps at $n$ and another jumps at $n+1$; equivalently $n$ and $n+1$ are each divisible by at least one of $4,5,6$. This repeats modulo $60$. The qualifying residues are $4,5,15,24,35,44,54,55$. Ten periods give $80$. The upper bound restricts which $n$ are counted, not the possible comparison integers. If the comparison integers are instead restricted to be at most $600$, the value $600$ becomes one additional singleton, giving $81$.

**Answer:** 080.

**Methods:** floor fibers, periodicity.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 1 wrongly lists divisors 3,4,5 instead of 4,5,6. Sources 2–3 use 24 instead of lcm(4,6)=12 in overlap formulas, with compensating arithmetic errors. All-positive comparison gives 80; bounded comparison adds 600 and gives 81. Archived notes report both accepted, but this audit has not obtained a primary MAA acceptance notice.

**Archived alternatives reviewed:** 7 of 7. Indices in the data are zero-based.

**Status:** solved.

## 2022 AIME II Problem 9: Regions between two supporting lines

Join all $m$ marked points on one line to all $n$ on a parallel line, with no triple interior intersection. Including the supporting lines, count bounded regions for $m=7, n=5$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

For $n=1$, the $m$ segments and supporting line create $m-1$ bounded regions. Adding the jth lower point creates $m$ new regions from its fan, and $(j-1)\binom m2$ more from crossings with previous fans; the no-triple condition makes all these crossings distinct. Thus $R(m,n)=mn-1+\binom m2\binom n2$. At $(7,5)$ this is $34+210=244$.

**Answer:** 244.

**Methods:** planar regions, incremental counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The fan-insertion and planar Euler counts agree. The no-triple-crossing hypothesis is essential for counting intersections by endpoint pairs.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2022 AIME II Problem 10: Choosing two edges

Evaluate modulo $1000$ the sum from $k=3$ to $40$ of $\binom{\binom{k}{2}}{2}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Choose two distinct edges of a complete graph on $k$ vertices. They either share a vertex, contributing $3\binom k3$, or are disjoint, contributing $3\binom k4$. Hence the summand is $3\binom{k+1}4$. Hockey-stick summation gives $3\binom{42}5=38\cdot39\cdot41\cdot42\equiv4\pmod{1000}$.

**Answer:** 004.

**Methods:** double counting, hockey-stick identity.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 2 guesses a pattern from six values and does not prove it. The other sources prove the binomial identity or telescope it; the new edge-pair bijection explains the factor 3.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2022 AIME II Problem 13: A coefficient reduced to stars and bars

Find coefficient $x^{2022}$ in $(x^{2310}-1)^6/[(x^{105}-1)(x^{70}-1)(x^{42}-1)(x^{30}-1)]$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Below degree $2310$, the numerator contributes only $1$. Geometric-series expansion counts $105a+70b+42c+30d=2022$ in nonnegative integers. Modular reductions force $a=2A,b=3B,c=5C+1,d=7D+3$. Substitution gives $A+B+C+D=9$. This bijection yields $\binom{12}3=220$.

**Answer:** 220.

**Methods:** generating functions, modular reduction, stars and bars.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 0 drops binomial coefficients from a full expansion, harmless only after restricting to degree 2022. Source 1 skips the modular exhaustion argument. Sources 2 and 4 write infinite series after polynomial divisions; that equality needs truncation. The original proof uses formal coefficients below 2310 and explicit residues.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2022 AIME II Problem 14: Complete coverage by a finite stamp collection

For denominations $a<b<c$, let $f$ be the minimum number of stamps, using every denomination, whose subcollections represent every value from $1$ through $1000$. Find and sum the three least values of $c$ permitting $f=97$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Necessarily $a=1$. A sorted stamp collection covers every value up to its total exactly when each next stamp is at most one plus the preceding total. Choosing the largest currently admissible denomination maximizes the total after each step, so is optimal. Put $q=\lceil c/b\rceil$. Use $b-1$ ones, then $q-1$ stamps of value $b$, reaching $L=bq-1$, then $t=\max(1,\lceil(1000-L)/c\rceil)$ stamps of value $c$. Thus $f=b+q-2+t$. For $c\le10$, $97$ stamps have insufficient total. Let $T=\lceil1001/c\rceil$. Since $bq\ge c$, we have $t\le T-1$ for $c<1001$; and $b+q\le c+1$, giving $f\le c-2+T$. For $12\le c\le86$, the inequality $c(98-c)\ge1001$ makes this bound at most $96$. For $c=87$ and $b\le85$, $b+\lceil87/b\rceil\le87$ gives $f\le96$; the remaining $b=86$ also gives $96$ directly. Finally $(c,b)=(11,7),(88,87),(89,87)$ give $f=97$. These are therefore the three least possible $c$, whose sum is $188$.

**Answer:** 188.

**Methods:** complete sequences, greedy dominance, coverage.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The sole stored entry contains its own corrections but still uses an invalid general minimum formula and wrong witnesses b=86 for c=88,89. The new coverage-interval greedy proof gives the exact minimum and witnesses(11,7),(88,87),(89,87).

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2023 AIME I Problem 1: No opposite pair of men

Five men and nine women stand randomly at $14$ cyclic positions. Find numerator plus denominator of the probability every man is opposite a woman.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

The five male positions are uniform among $\binom{14}5$ subsets. Choose five distinct diameters among $7$, and one of their two endpoints for each man: $\binom75 2^5$ favorable subsets. Probability $48/143$; answer $191$.

**Answer:** 191.

**Methods:** opposite pairs, probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All nine stored solutions inspected. Diameter selection, sequential placement, sequential opposite-partner exposure, and labeled arrangements all give 48/143. Each method must consistently distinguish labeled positions from rotations; the independent diameter-subset count avoids extra symmetry factors.

**Archived alternatives reviewed:** 9 of 9. Indices in the data are zero-based.

**Status:** solved.

## 2023 AIME I Problem 3: Counting ordinary intersections

Forty lines have no parallel pair. There are exactly $3$ triple points, $4$ quadruple points, $5$ quintuple points, and $6$ sextuple points, and no higher multiplicity. Count double points.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

Every line pair has exactly one intersection. A $k$-fold point consumes $\binom k2$ pairs. Thus the answer is $\binom{40}2-3\binom32-4\binom42-5\binom52-6\binom62=607$.

**Answer:** 607.

**Methods:** incidence double counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The sole stored solution double-counts pairs of lines by intersection multiplicity. The independent proof uses the same incidence invariant.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2023 AIME I Problem 6: Optimal sequential color guesses

Three red and three black cards are revealed in random order. Before each reveal, guess the color using previous observations. Find numerator plus denominator of the optimal expected correct guesses.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

Guesses do not affect future information, so choose the currently more numerous remaining color. If $V(r,b)$ is the optimal expectation, then $V(r,b)=\max(r,b)/(r+b)+[rV(r-1,b)+bV(r,b-1)]/(r+b)$, with $V(r,0)=r$. Evaluating the $3$ by $3$ table gives $V(3,3)=41/10$ (stage success probabilities are $1/2,3/5,3/5,7/10,7/10,1$). Answer $51$.

**Answer:** 051.

**Methods:** optimal prediction, dynamic programming, expectation.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All five stored solutions inspected. The majority-remaining-color policy is optimal because a guess cannot affect subsequent information. Stage counting, full order tables, and dynamic programming all give 41/10; the independent solution states this policy justification explicitly.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2023 AIME I Problem 7: Pairwise-distinct remainders

Count positive $n<1000$ whose remainders modulo $2,3,4,5,6$ are all different.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

The condition repeats modulo $60$. If $n$ is even, the residues modulo $2,4$ must be $0,2$; distinctness then forces residues $1,4$ modulo $3,6$, and $3$ modulo $5$, so $n\equiv58 \pmod{60}$. If $n$ is odd, the $2,4$ residues are $1,3$; the $3,6$ residues must be $2,5$, and the $5$ residue $0$ or $4$, giving $n=35$ or $59 \pmod{60}$. The three counts are $16,17,16$, total $49$.

**Answer:** 049.

**Methods:** Chinese remainder theorem, residue patterns.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All four stored solutions inspected. They reduce to a period 60 and residues 35,58,59. The complete residue casework proves necessity; empirical listing alone needs exhaustive coverage. The independent argument derives the three classes.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2023 AIME I Problem 9: A cubic with one other equal-value integer

Count monic cubics $x^3+ax^2+bx+c$ with $a, b, c$ in $[-20,20]$ for which exactly one integer $m$ unequal $2$ satisfies $p(m)=p(2)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Divide by $m-2$ to obtain $m^2+(a+2)m+(4+2a+b)=0$. Since one integer root forces the other integer, we need either a double root other than $2$, or two distinct roots with one equal $2$. The double-root condition is $b=(a-2)^2/4-4$; the bounds allow $9$ even values of $a$ but $a=-6$ must be excluded, giving $8$. The root $2$ condition is $b=-4a-12$, allowing $a=-8,\ldots,2$, but again excluding $-6$, giving $10$. The coefficient $c$ has $41$ choices. Total $(8+10)41=738$.

**Answer:** 738.

**Methods:** root multiplicities, bounded counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both stored solutions inspected. They classify the factorization into one double root and one simple root. The alternate source has a constant-term copy typo in its second case, but the admissible-root counts 10 and 8 and total 738 are sound.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2023 AIME I Problem 11: Exactly one adjacent selected pair

Count subsets of $[10]$ containing exactly one pair of consecutive integers.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Such a binary word has one run $11$ and $r$ additional isolated ones, for $0\le r\le 4$. Choose which of its $r+1$ runs has length $2$. Its $10-(r+2)=8-r$ zeros must separate the runs with $r$ mandatory zeros; distributing the rest into $r+2$ gaps gives $\binom{9-r}{r+1}$. Thus the count is $\sum_{r=0}^4(r+1)\binom{9-r}{r+1}=9+56+105+60+5=235$.

**Answer:** 235.

**Methods:** run encoding, stars and bars.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All eight sources inspected. Fixed-pair Fibonacci products, coupled recurrences, positive gaps, and a monomino/domino/triomino encoding all give 235. Several contain notation mistakes: index 3 uses a shifted Fibonacci index; index 4 reverses the gap-variable substitution; index 7 uses dp where its first recurrence requires dp 2. The independent run-gap formula and exhaustive subset check avoid these slips.

**Archived alternatives reviewed:** 8 of 8. Indices in the data are zero-based.

**Status:** solved.

## 2023 AIME I Problem 14: Hamiltonian cycles of two clock hands

Two independently advancing clock hands start at $12$. Each move advances exactly one hand one step. Count modulo $1000$ the $144$-move tours visiting every ordered hand-position pair once before returning.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

View positions as $\mathbb Z_{12}^2$. Let $e(x, y)$ indicate a rightward outgoing edge. Having exactly one incoming edge forces $e(x-1,y)=e(x,y-1)$, so the outgoing direction is constant on each diagonal $x+y$ modulo $12$. Thus a tour is specified by $12$ binary directions, repeated each round. If $k$ directions are right, $12$ moves translate by $(k,-k)$; visiting all $12$ vertices of each diagonal is equivalent to $\gcd(k,12)=1$. Count $\binom{12}1+\binom{12}5+\binom{12}7+\binom{12}{11}=1608$, remainder $608$.

**Answer:** 608.

**Methods:** Hamiltonian cycles, conservation, cyclic groups.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All three sources inspected. Both torus sketches identify diagonal-constant directions; the matrix solution gives another periodicity argument but contains index-range typos. The independent incoming-edge conservation equation proves the diagonal claim, and translation order proves the gcd condition.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2023 AIME II Problem 6: Midpoints in an L-shaped region

Choose two independent uniform points in a $2$ by $2$ square with its upper-right unit square removed. Find numerator plus denominator of the chance their midpoint remains in the region.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

A midpoint can fail only when the points lie in the upper-left and lower-right squares, in either order, probability $2/9$. Conditional on that, each coordinate of the midpoint exceeds $1$ with probability $1/2$, independently. Failure probability is $1/18$, so success $17/18$ and answer $35$.

**Answer:** 035.

**Methods:** geometric probability, conditioning.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All four sources inspected. Complementary conditioning on diagonally separated unit squares gives a one-quarter conditional failure chance. Integration, coordinate independence, and four-point symmetry average are equivalent. The independent proof uses coordinate independence and symmetry.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2023 AIME II Problem 7: Avoiding monochromatic rectangles

Color $12$ cyclic vertices red or blue. Count colorings with no monochromatic rectangle among the vertices.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Every inscribed rectangle uses two diameters. Hence among the six opposite pairs, at most one may be $RR$ and at most one $BB$. With no monochromatic pair, there are $2^6$ colorings; with one, $6\cdot2\cdot2^5$; with one of each, $6\cdot5\cdot2^4$. Total $64+384+480=928$.

**Answer:** 928.

**Methods:** opposite-pair encoding, forbidden configurations.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All four sources inspected. Every inscribed rectangle uses two diameters, so monochromatic opposite-pair counts give a complete three-case classification. All reach 928.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2023 AIME II Problem 10: Balanced proper colorings of a ladder

Place $1,\ldots,12$ in a $2$ by $6$ grid so adjacent cells never have equal residues modulo $3$. Let $N$ count placements. Find the number of positive divisors of $N$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Each residue occurs $4$ times. Each column contains two distinct residues; counting appearances forces exactly two columns of each unordered type $01,02,12$. Order the types in $6!/(2!)^3=90$ ways. The first column has two orientations; each subsequent column has exactly one orientation avoiding a horizontal match. Thus $180$ residue patterns. Assign actual numbers in $(4!)^3$ ways, so $N=180(24)^3=2^{11}3^5 5$. Its divisor count is $12\cdot 6\cdot 2=144$.

**Answer:** 144.

**Methods:** graph coloring, multiset permutations.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both stored solutions inspected. The first uses residue-column types correctly. The second initially counts all column orientations without enforcing horizontal restrictions and compensates with an unjustified value-assignment count; its appended shorter formula has the right total. The independent proof explains why only two global orientations exist for each type order.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2023 AIME II Problem 11: Maximum intersecting families on five elements

Count collections of $16$ distinct pairwise-intersecting subsets of $[5]$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Complementary pairs force exactly one member of each pair into the family. If a singleton occurs, the family is its full star, giving $5$ choices. Otherwise all $4$- and $5$-sets occur; choosing a $2$-set excludes exactly its complementary $3$-set. Thus choose any pairwise-intersecting edge family in $K_5$. Such a family is empty, a single edge, a two-edge star, a three-edge star, a triangle, or a four-edge star: counts $1,10,30,20,10,5$. (Three intersecting edges without a common vertex form a triangle, which admits no additional edge.) Total $5+76=81$.

**Answer:** 081.

**Methods:** intersecting families, complement pairing.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All three sources inspected. Complementary-set pairing makes the size 16 family maximal. Reduction to pairwise-intersecting edge families gives 81. Source index 2 incorrectly claims only 2-set/3-set disjointness matters, then uses the wrong binomial coefficient for three-edge stars; its final number agrees only after inconsistent intermediate counts. The independent star-or-triangle classification is complete.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2023 AIME II Problem 15: A finite carry state detects repeated modular inverses

For each n≥1, let a_n be the smallest positive multiple of 23 congruent to 1 modulo 2 to the nth power. Count n≤1000 for which a_n=a_(n+1).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Put $b_n=(a_n-1)/2^n$. To pass to modulus $2^{n+1}$, the least admissible multiple is either a_n or a_n+23 times 2 to the nth power: all candidates for the old modulus differ by that increment. Consequently $b_{n+1}=b_n/2$ when b_n is even, and $(b_n+23)/2$ when it is odd. Starting at b_1=11, the successive states are 11,17,20,10,5,14,7,15,19,21,22, followed again by 11. Determinism proves the 11-term cycle repeats forever. Equality of consecutive a values occurs exactly at the even states, or n≡0,3,4,6 modulo 11. The 90 complete cycles in 1 through 990 contribute 360, and 991 through 1000 contribute three more. The answer is 363.

**Answer:** 363.

**Methods:** modular inverse lifting, finite-state recurrence, periodic carries.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. The carry-state recurrence proves periodicity exactly. The first source incorrectly makes the multipliers a_n/23 themselves periodic, and the binary discussion gives an unsupported 16-state bound; only the bounded carry state repeats.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2024 AIME I Problem 3: Winning residues in a subtraction game

Two players alternately remove either $1$ or $4$ counters. The player taking the last counter wins. Count initial sizes from $1$ through $2024$ for which the second player can force a win.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

The losing positions are precisely $n\equiv0,2\pmod5$. Indeed, either move from these residues reaches another residue, while from residues $1,3,4$ one can reach $0$ or $2$. Starting with the empty position, induction proves the claim. There are $404$ positive multiples of $5$ and $405$ numbers congruent to $2$. Thus the answer is $809$.

**Answer:** 809.

**Methods:** impartial games, periodicity.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All five stored solutions inspected. Residue induction and the complementary-move strategy establish the result; empirical pattern spotting alone is incomplete. The Grundy calculation contains a small mex transcription error but the period and losing positions are correct.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2024 AIME I Problem 4: The jackpot conditional on winning

A ticket chooses four of ten numbers; four winning numbers are drawn uniformly. A prize requires at least two matches. Find numerator plus denominator of the conditional probability of four matches, given a prize.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Fix the winning set. Tickets with exactly $2,3,4$ matches number $\binom42\binom62=90$, $\binom43\binom61=24$, and $1$. The conditional jackpot probability is $1/(90+24+1)=1/115$. The requested sum is $116$.

**Answer:** 116.

**Methods:** conditional probability, hypergeometric counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both stored solutions count the same three hypergeometric cases; the conditional sample space is correctly restricted to prize-winning tickets.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2024 AIME I Problem 6: Grid paths with four turns

Count paths from one corner of an $8\times8$ grid to the opposite corner, using only right and upward steps, with exactly four changes of direction.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

There are five nonempty runs, alternating directions. If the first run is rightward, the eight right steps split into three positive parts and the eight upward steps into two. This gives $\binom72\binom71$. Starting upward gives the same number. Therefore $2\binom72\binom71=294$.

**Answer:** 294.

**Methods:** runs, compositions.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All five stored solutions inspected. Run-length compositions and turning-point enumeration agree. The longest stars-and-bars version has a variable-copy typo; the positive-part count is correct.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2024 AIME I Problem 11: Rotating blue vertices away from themselves

Color the eight vertices of a regular octagon independently red or blue. Find numerator plus denominator of the probability that some rotation sends every blue vertex to a red vertex.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Let $B\subset\mathbb Z_8$ be the blue set. If $|B|\le3$, its difference set has at most $1+2\binom32=7$ elements, so some rotation makes $B$ disjoint from itself. If $|B|>4$, this is impossible. For $|B|=4$, a successful shift sends $B$ to its complement. An odd shift forces an alternating coloring, giving $2$ choices. A shift by $2$ or $6$ gives $4$ choices, alternating on each parity cycle. A shift by $4$ gives $2^4=16$ choices, one blue vertex per opposite pair. These three classes are disjoint because the first two are invariant under shift $4$. Thus there are $1+8+28+56+22=115$ successful colorings out of $256$, and the answer is $371$.

**Answer:** 371.

**Methods:** difference sets, cyclic symmetry, complement pairing.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both source solutions enumerate blue-set shapes. Their small-support sufficiency arguments are informal. The independent difference-set bound and shift-cycle classification replace the shape testing.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

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

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2024 AIME II Problem 1: Recovering a fourfold intersection

Among $900$ residents everyone has a candy. Ring, club, and spade ownership totals are $195, 367$, and $562$. Exactly $437$ residents own two of the four items and $234$ own three. How many own all four?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

Count ownership incidences beyond the universal candy. Their number is $195+367+562=1124$. Residents with exactly two items contribute $437$, those with exactly three contribute $2\cdot234$, and those with four contribute $3x$. Hence $1124=437+468+3x$, so $x=73$.

**Answer:** 073.

**Methods:** incidence counting, set multiplicities.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All four stored solutions inspected. Venn-atom equations and incidence totals are equivalent; some use inconsistent variable names, without affecting the final linear equation.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2024 AIME II Problem 2: A mode and a missing median constrain an integer partition

A finite list of positive integers sums to 30, has unique mode 9, and has an integral median that is absent from the list. Find the sum of squared entries.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

The list length is even, and 9 occurs at least twice but at most three times. If it occurs three times, the remaining sum is 3: an even list has either one extra entry 3, giving median 9, or three entries 1, giving a tied mode. Thus exactly two 9 s occur and every other entry is distinct. Their sum is 12, so there are either two or four other entries; six distinct positive entries already sum to 21. Four distinct entries summing to 12 are only (1,2,3,6) or(1,2,4,5); each gives median 9/2 after the two 9 s are appended. For two entries, the distinct positive pairs summing to 12 are (1,11),(2,10),(3,9),(4,8),(5,7). Only(5,7) meets both the mode and median conditions. Thus the list is 5,7,9,9, and its square sum is 25+49+81+81=236.

**Answer:** 236.

**Methods:** integer partitions, multiplicity constraints, exhaustive case split.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. The first three analyze only four-element lists and leave longer lists unexcluded. The final source supplies the missing length analysis; the authored proof explicitly exhausts both the frequency and length possibilities.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2024 AIME II Problem 3: Digits constrained by row and column sums

Fill a $2\times3$ array with decimal digits, allowing leading zeroes. The two three-digit rows sum to $999$, and the three two-digit columns sum to $99$. Count fillings.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

The row condition forces each vertical digit pair to sum to $9$: the units column has no carry, and the same follows successively for the other columns. Write the top digits as $a,b,c$ and the lower digits as $9-a,9-b,9-c$. The column-number sum is $9(a+b+c)+27$, so $a+b+c=8$. No digit upper bound is active. Stars and bars gives $\binom{10}2=45$.

**Answer:** 045.

**Methods:** digit carries, stars and bars.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The sole source uses column digit complements followed by stars and bars; the independent proof explicitly rules out carries.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2024 AIME II Problem 6: Encoding a set by maxima of subsets

A finite set $A$ of positive integers has the property that exactly $2024$ finite nonempty sets of positive integers have maximum in $A$. Find the sum of the elements of $A$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Exactly $2^{k-1}$ sets have maximum $k$: include $k$ and choose any subset of the smaller positive integers. Thus $\sum_{k\in A}2^{k-1}=2024$. Its unique binary expansion is $2^{10}+2^9+2^8+2^7+2^6+2^5+2^3$. Therefore $A=\{11,10,9,8,7,6,4\}$ and its sum is $55$.

**Answer:** 055.

**Methods:** binary encoding, subset maxima.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both sources use unique binary expansion, once at 2024 and once at 4048. Both recover the same seven elements.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2024 AIME II Problem 9: Maximal monochromatic rows and columns

Place black and white chips on a $5\times5$ board, at most one per cell, so every occupied row and column is monochromatic. Count placements to which no chip can be added.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Every row and column must be nonempty: an empty row could receive a chip matching any occupied column, and the empty board is also not maximal. Label each row and column by its color. A cell is occupied exactly when its labels agree; otherwise it cannot be filled. If both colors occur, each must occur among both row labels and column labels. Hence there are $(2^5-2)^2$ mixed configurations. The two uniform full boards give the remaining possibilities. Total $900+2=902$.

**Answer:** 902.

**Methods:** maximal configurations, bipartite encoding.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All three sources inspected. They encode maximal placements by row and column colors; the detailed version explains why every compatible cell must be occupied.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2024 AIME II Problem 11: A symmetric cubic counting problem

Count ordered nonnegative integer triples with $a+b+c=300$ and $a^2b+a^2c+b^2a+b^2c+c^2a+c^2b=6000000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Using $\sum_{\rm sym}a^2b=(a+b+c)(ab+bc+ca)-3abc$, the equation is equivalent to $(100-a)(100-b)(100-c)=0$. Thus at least one coordinate is $100$. For a specified coordinate there are $201$ possibilities for the other two. All pairwise and triple intersections are the single triple $(100,100,100)$. Inclusion-exclusion gives $3\cdot201-3+1=601$.

**Answer:** 601.

**Methods:** factorization, inclusion-exclusion.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All five sources inspected. The direct product factorization is sound. Source index 1 invokes unnecessary Fermat theory; index 3 contains erroneous quadratic formulas and swaps the x=0 and x=100 endpoint descriptions; index 4 confuses shifted and original variables and misprints the common triple. The independent factorization avoids these errors.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2024 AIME II Problem 14: Digit-square conditions count CRT idempotents

For integer b≥2, call a positive integer special if its base-b representation has exactly two digits whose sum equals its square root. Find the least b with more than ten special integers.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Write the digits a,c and put k=a+c=$\sqrt{n}$, B=b−1. Since n<b squared, k≤B; the leading digit is positive, so k≥2. The equation k squared=ba+c becomes $k(k-1)=Ba$. Conversely every k in 2 through B satisfying B divides k(k−1) gives a=k(k−1)/B and c=k−a, with 1≤a≤k−1≤B−1 and 1≤c≤B−1, so it gives a valid distinct integer. For each prime power dividing B, coprimality of k,k−1 forces k≡0 or 1 modulo that power. The Chinese remainder theorem gives exactly $2^{\omega(B)}$ residues modulo B; representing them in 1 through B and excluding k=1 leaves $2^{\omega(B)}-1$ special integers. More than ten requires at least four distinct prime factors. The least B with four is 2 times 3 times 5 times 7=210, which gives 15 integers. Hence b=211.

**Answer:** 211.

**Methods:** Chinese remainder theorem, prime-power assignments, idempotent counting, digit bounds.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** The single alternative inspected. The authored proof supplies the full converse digit bounds and uses CRT for existence, not merely uniqueness, of every prime-power assignment.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2024 AIME II Problem 15: Rectangles supported by dodecagon chords

Count rectangles whose four sides lie on sides or diagonals of a regular dodecagon. Rectangle corners need not be polygon vertices.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Chord directions occur in multiples of $15^\circ$, giving six perpendicular direction pairs. Three pairs have one coordinate pattern and three have the pattern rotated by $15^\circ$. For a unit circumcircle in the first pattern, available horizontal levels are $0,\pm1/2,\pm\sqrt3/2$, with respective half-widths $1,\sqrt3/2,1/2$. Among pairs of horizontal lines, $3$ pairs allow $5$ vertical lines and $7$ pairs allow $3$, yielding $3\binom52+7\binom32=51$. In the rotated pattern the levels are $\pm\sin15^\circ,\pm\sin45^\circ,\pm\sin75^\circ$. Respectively $1,5,9$ horizontal pairs allow $6,4,2$ vertical lines, yielding $\binom62+5\binom42+9\binom22=54$. These counts follow by requiring all four intersections to lie within both chord segments. Every rectangle has a unique perpendicular direction pair. Total $3(51+54)=315$.

**Answer:** 315.

**Methods:** geometric enumeration, direction classes.

**Verification:** Independently enumerated horizontal and vertical chord endpoints for both orientation types: 51 and 54.

**Source comparison:** All three source solutions inspected. They split six direction classes into two symmetric triples, obtaining 51 and 54 per orientation. The independent chord-coordinate table verifies the segment-length restrictions without relying on missing diagrams.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2025 AIME I Problem 3: Flavor assignments with ordered popularity

Nine distinct people each choose one of three ice-cream flavors. Every flavor is chosen, with chocolate chosen more often than vanilla and vanilla more often than strawberry. Find the assignment count modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

The possible counts $(c,v,s)$ are $(6,2,1),(5,3,1),(4,3,2)$. Their multinomial counts sum to $9!/(6!2!)+9!/(5!3!)+9!/(4!3!2!)=252+504+1260=2016$. The remainder is $16$.

**Answer:** 016.

**Methods:** multinomial counting, integer partitions.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All five sources inspected. Each uses the same three strict count partitions and multinomial assignments; index 4 has missing displayed case details in the scrape.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2025 AIME I Problem 4: Count a union of two primitive lattice lines

Count ordered integer pairs (x,y) with −100≤x,y≤100 satisfying $12x^2-xy-6y^2=0$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Factor the expression as $(3x+2y)(4x-3y)$. On the first line, coprimality gives $(x,y)=(2t,-3t)$, with −33≤t≤33, yielding 67 pairs. On the second, $(x,y)=(3t,4t)$, with −25≤t≤25, yielding 51 pairs. The lines share only(0,0), so their union has 67+51−1=117 pairs.

**Answer:** 117.

**Methods:** factorization, primitive lattice directions, inclusion-exclusion.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Factoring without division retains the origin automatically; subtracting it once corrects the overlap of the two cases.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2025 AIME I Problem 5: Digit permutations divisible by twenty-two

Let $N$ count permutations of digits $1$ through $8$ that form an eight-digit integer divisible by $22$. Find $N-2025$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Divisibility by $11$ requires both alternating-position digit sums to be $18$: their difference is even and has absolute value at most $16$. The four-subsets summing to $18$ are $1278,1368,1458,1467,2358,2367,2457,3456$; the total number of even digits across this list is $16$. If such a subset occupies the even positions, choose its even final digit, then arrange the remaining positions in $3!4!$ ways. Thus the favorable count is $16\cdot3!4!=2304$. The requested difference is $2304-2025=279$.

**Answer:** 279.

**Methods:** divisibility tests, subset sums.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All four sources inspected. They split digits into two four-subsets of sum 18. Enumeration confirms eight subsets, each with two even digits, justifying the factor one-half for an even final digit. The independent solution uses an explicit subset list.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2025 AIME I Problem 7: The final alphabetized pair

Pair the twelve letters $A$ through $L$ uniformly into six unordered pairs. Sort each pair alphabetically and then sort the six pairs. Find numerator plus denominator of the probability the last pair contains $G$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

There are $11!!=10395$ pairings. If $G$ is first in its pair, choose its partner in $5$ ways, choose the pair of low letters among $A$ through $F$ in $\binom62$ ways, and match the four remaining low letters with the four remaining high letters in $4!$ ways. If $G$ is second, its partner must be $F$; match $A$ through $E$ with $H$ through $L$ in $5!$ ways. These give $1800+120=1920$ favorable pairings. The probability is $128/693$, and the answer is $821$.

**Answer:** 821.

**Methods:** perfect matchings, order statistics.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both sources inspected. Source index 1 has contradictory arithmetic (19 times 120 followed by 16 times 120); its stated final probability is correct but that derivation is not. The independent low-low-pair count gives 1800+120 favorable pairings.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2025 AIME I Problem 10: Counting Sudoku bands

Fill a $3\times9$ band with digits $1$ through $9$ so that every row and every consecutive $3\times3$ block contains each digit once. If the count is $2^a3^b5^c7^d$, find $2a+3b+5c+7d$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

There are $9!$ first rows. Classify digits by their first-row block. If $k$ digits from the first class go to the second block of row two, the row and block totals force every other class allocation. Choosing the allocated digits gives $\sum_{k=0}^3\binom3k^3=56$. Arrange the three second-row blocks internally in $(3!)^3$ ways. The third-row block sets are now determined and have another $(3!)^3$ arrangements. Thus $N=9!\cdot56\cdot6^6=2^{16}3^{10}5\cdot7^2$, and the requested weighted sum is $32+30+5+14=81$.

**Answer:** 081.

**Methods:** contingency tables, Latin rectangles.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All four sources inspected. Fixing the first row or first block leads to the same allocation factor 56 and total 9!*56*6^6. The exponent-weighted requested answer is 81.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2025 AIME I Problem 13: Expected regions from random chords

Two perpendicular diameters divide a disk into four quadrants. Add $25$ independent chords, each choosing uniformly a pair of distinct quadrants and then uniform endpoints within those quadrants. Find the expected number of regions.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

A chord crosses $1$ diameter when its quadrants are adjacent and $2$ when opposite, so the mean is $4/3$. For two random chords, condition on the first quadrant pair. If adjacent, among the six second pairs four share one quadrant (intersection chance $1/2$), one equals it (chance $1/2$), and one is disjoint (chance $0$): total $5/12$. If opposite, the disjoint pair instead intersects surely, giving $7/12$. Thus the unconditional probability is $(2/3)(5/12)+(1/3)(7/12)=17/36$. Each new chord adds one plus its number of crossings, almost surely. Expected regions are $4+25(1+4/3)+\binom{25}2(17/36)=204$.

**Answer:** 204.

**Methods:** linearity of expectation, random arrangements.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both sources inspected. Incremental regions and pair-crossing expectations agree. Source index 1 calls all 30 remaining quadrant-pair cases shared-one-quadrant cases, overlooking six identical pairs; these also have crossing probability one-half, so the result survives the inaccurate description.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2025 AIME I Problem 15: Cubic residues and three-variable counting

Count ordered triples $1\le a,b,c\le729$ with $a^3+b^3+c^3$ divisible by $2187$, and give the remainder modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Split inputs into category $A$ (multiples of $9$, size $81$), category $B$ (multiples of $3$ but not $9$, size $162$), and category $C$ (units, size $486$). Their cube residues are respectively $729j$ with multiplicity $27$; $\pm27+243j$ with multiplicity $9$; and $\pm1+9j$ with multiplicity $1$. These multiplicities follow by expanding a cube, or by $v_3(u^3-v^3)=v_3(u-v)+1$ for units of the same residue modulo $3$. Reduction modulo $9$ and then $243$ permits only patterns AAA, ABB, ACC, BCC. For any first two entries, the required third residue has the stated multiplicity. The ordered counts are $81^2\cdot27$, $3\cdot81\cdot162\cdot9$, $3\cdot81\cdot486$, and $3\cdot162\cdot486$. Their sum is $15\cdot3^{10}=885735$, giving $735$.

**Answer:** 735.

**Methods:** valuation stratification, residue distributions.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All four sources inspected. Source index 1 explicitly contains a false vanishing exponential-sum claim and then inserts an unjustified factor 5; it is rejected. Source index 2 has lengthy omitted and inconsistent modular subcounts and is not used as a proof. Source index 3 offers a useful valuation recursion, but its appeal to ordinary Hensel lifting needs justification because the cube derivative vanishes modulo 3. The independent cube-residue distribution was checked by exact convolution.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2025 AIME II Problem 3: Two red sides on every small square

Color the twelve unit edges of a $2\times2$ array of squares red or blue. Count colorings in which every small square has exactly two red edges.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

First color the four internal edges. Around the central vertex they form a cyclic binary word. A square whose two internal edges agree has one possible coloring of its two exterior edges; a square whose internal edges differ has two. Thus a word with $t$ transitions has weight $2^t$. The possible cyclic transition counts are $0,2,4$, attained by $2,12,2$ words. The total is $2+12\cdot4+2\cdot16=82$.

**Answer:** 082.

**Methods:** transfer weights, cyclic binary words.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** No solution text occurs in the downloaded source record. Independent transfer-weight proof and exhaustive twelve-edge coloring check both give 82.

**Archived alternatives reviewed:** 0 of 0. Indices in the data are zero-based.

**Status:** solved.

## 2025 AIME II Problem 7: The least common multiple of a random divisor subset

Choose uniformly a subset of the positive divisors of $2025$. Find numerator plus denominator of the probability that its least common multiple is $2025$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Since $2025=3^4 5^2$, there are $15$ divisors. The subset must contain a divisor of $3$-exponent $4$ and one of $5$-exponent $2$. There are respectively $3$ and $5$ such divisors, with one in common. Inclusion-exclusion gives $2^{15}-2^{12}-2^{10}+2^8$ favorable subsets. Dividing by $2^{15}$ yields $109/128$, so the answer is $237$.

**Answer:** 237.

**Methods:** divisor lattice, inclusion-exclusion.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All four source solutions inspected. Inclusion-exclusion and splitting on inclusion of 2025 are equivalent. Missing displayed expressions in two scraped alternatives do not obscure the underlying count.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2025 AIME II Problem 8: When greedy coin change succeeds

With coin values $1, 10$, and $25$, count amounts from $1$ through $1000$ for which repeatedly taking the largest affordable coin uses the fewest coins.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Write $N=25q+r$, $0\le r<25$, and put $h(s)=\lfloor s/10\rfloor+(s\bmod10)$, the optimal count using ones and tens. Using two fewer quarters changes the count by $-2+h(s+50)-h(s)=3$, so only $q$ and $q-1$ quarters need comparison. For $q\ge1$, using $q-1$ improves the count exactly when $r\bmod10\ge5$, namely $r=5,\ldots,9,15,\ldots,19$. There are $39$ complete positive-quarter blocks and thus $390$ failing amounts. The remaining $1000-390=610$ succeed.

**Answer:** 610.

**Methods:** greedy algorithms, periodic optimization.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The single stored source uses coin-case analysis. The independent two-quarter exchange explains why only the largest allowable quarter count and one less need comparison.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2025 AIME II Problem 9: Count sine levels and identify double zeros

Let n count roots of $\sin(7\pi\sin(5x))=0$ in 0<x<2 $\pi$, and t count those roots where the graph is tangent to the x-axis. Find n+t.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Roots occur exactly at sin(5 x)=k/7 for integers−7≤k≤7. Over the five periods, each of the twelve nonzero levels with absolute value below 1 has ten crossings, the zero level has nine because both interval endpoints are excluded, and each extreme level±1 has five. Thus n=120+9+10=139. At a root the derivative is $35\pi\cos(k\pi)\cos(5x)$; since cos(kpi)=±1, it vanishes exactly at the ten extreme-level roots. There the inner sine has a nondegenerate extremum while the outer sine has nonzero derivative, so the zero has order two and the axis is tangent. Hence t=10 and n+t=149.

**Answer:** 149.

**Methods:** periodic level counting, endpoint exclusion, root multiplicity.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. Level counts require removing the two open-interval endpoints. The derivative and nondegenerate-extremum observation distinguish genuine tangencies from crossings.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2025 AIME II Problem 10: Eight occupied seats with no triple

Select eight of sixteen seats in a row so that no three consecutive seats are selected. Find the number of selections modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

The eight unselected seats create nine gaps. Each gap contains $0,1,$ or $2$ selected seats, and their sum is $8$. Thus the count is $[x^8](1+x+x^2)^9$. Writing this as $(1-x^3)^9/(1-x)^9$ gives $\binom{16}8-9\binom{13}8+\binom92\binom{10}8=2907$. The remainder is $907$.

**Answer:** 907.

**Methods:** bounded compositions, generating functions.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All three sources inspected. Counting singleton and doubleton occupied runs agrees with bounded-gap compositions; exact seat enumeration gives 2907.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2025 AIME II Problem 11: Equal-length perfect matchings on a polygon

Pair all vertices of a regular $24$-gon so that the twelve resulting chords have the same length. Count the pairings.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Fix the cyclic step $d\in\{1,\ldots,12\}$. For $d<12$, the graph of chords of that length consists of $g=\gcd(24,d)$ cycles, each of length $24/g$. An odd cycle has no perfect matching; an even cycle has two, independently. The counts for $d=1,\ldots,11$ are $2,4,8,16,2,64,2,0,8,4,2$. For $d=12$, the diameters form one matching. Their sum is $113$.

**Answer:** 113.

**Methods:** cycle decomposition, perfect matchings.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** No solution text occurs in the downloaded source record. Independent equal-chord graph decomposition gives 113.

**Archived alternatives reviewed:** 0 of 0. Indices in the data are zero-based.

**Status:** solved.

## 2026 AIME I Problem 2: Palindromes as compositions

Count positive decimal palindromes with no zero digits and digit sum $13$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

The length is odd; let its center digit be $c\in\{1,3,5,7,9\}$. The left half has digit sum $s=(13-c)/2\in\{6,5,4,3,2\}$. Its nonzero digits form an arbitrary composition of $s$; the digit upper bound is automatic. There are $2^{s-1}$ compositions. Mirroring determines the right half, so the answer is $32+16+8+4+2=62$.

**Answer:** 062.

**Methods:** compositions, palindromes.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All five sources inspected. Palindromic compositions, central-digit compositions, and a two-operation construction all give 62. The independent central-digit count is complete and avoids the source notation slips.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2026 AIME I Problem 7: Permutations whose sixth power is identity

Count permutations of six labeled elements whose sixth iterate fixes every element.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Every cycle length must divide $6$, so allowed lengths are $1,2,3,6$. The possible cycle types are $6;3+3;2+2+2;1^6;3+1^3;2+1^4;2+2+1+1;3+2+1$. The formula $6!/\prod_j(j^{m_j}m_j!)$ gives respectively $120,40,15,1,40,15,45,120$. Their sum is $396$.

**Answer:** 396.

**Methods:** permutation cycles, cycle index.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All four sources inspected. Allowed-cycle enumeration and exclusion of 4- and 5-cycles agree. Several alternatives confuse cycle counts or describe orientation imprecisely; the standard cycle-index denominator removes these ambiguities.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2026 AIME I Problem 8: Divisor residues determined by exponent parity

Count divisors of $17017^{17}$ congruent to $5$ modulo $12$, and give the count modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

Factor $17017=7\cdot11\cdot13\cdot17$. A divisor is $7^a11^b13^c17^d$, with exponents from $0$ through $17$. Its residue is $5$ precisely when $a+b$ is even and $b+d$ is odd, by reduction modulo $4$ and $3$. Choose $b,c$ in $18^2$ ways; each determines the required parity of $a,d$, with $9$ choices each. Thus there are $18^2\cdot9^2=26244$ divisors, giving remainder $244$.

**Answer:** 244.

**Methods:** residue classes, exponent parity.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All four sources inspected. They reduce exponents to parity using residues 7,11,1,5 modulo 12. Both two-pattern enumeration and simultaneous modulo 3/modulo 4 conditions give 26244.

**Archived alternatives reviewed:** 4 of 4. Indices in the data are zero-based.

**Status:** solved.

## 2026 AIME I Problem 9: Visible even stickers on a die

Roll a fair die six times, placing sticker $k$ on the top face after roll $k$; a new sticker covers an old one. Given that stickers $2, 4$, and $6$ remain visible, find numerator plus denominator of the chance exactly one face is blank.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Choose distinct faces for stickers $2,4,6$ in $6\cdot5\cdot4$ ways. Sticker $1$ has $6$ choices; $3$ must avoid the face of $2$, giving $5$; $5$ must avoid the faces of $2,4$, giving $4$. Thus there are $14400$ equally likely assignments under the condition. Exactly five occupied faces means one repeated pair of sticker numbers. Its earlier number must be odd: there are $5+3+1=9$ such pairs. Assign the resulting five distinct blocks to faces in $6!$ ways. The probability is $9\cdot720/14400=9/20$, giving $29$.

**Answer:** 029.

**Methods:** conditional counting, set partitions.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All six sources inspected. Several correct conditional counts agree on 14400 and 6480. Source index 4 incorrectly divides raw probabilities by 6^4 rather than 6^6, which cancels in its ratio. Source index 5 allows invalid earlier-even-over-later-odd overlays and omits odd-over-odd collisions; its numerical agreement is accidental. The independent collision-pair enumeration was exhaustively checked.

**Archived alternatives reviewed:** 6 of 6. Indices in the data are zero-based.

**Status:** solved.

## 2026 AIME I Problem 11: Maximizing total variation on a grid

Place $1$ through $64$ bijectively in an $8\times8$ grid. Maximize the sum of absolute differences across all horizontal and vertical adjacencies; report the maximum modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

For any adjacent values, $|a-b|\le|a-32.5|+|b-32.5|$. Hence the total is at most $\sum_v\deg(v)|a_v-32.5|$. Rearrangement maximizes this bound by assigning the $36$ most extreme numbers to degree-$4$ interior cells, the next $24$ to degree-$3$ edge cells, and the middle four to corners. Color the grid as a checkerboard; each color has $18$ interior cells, $12$ edge cells, and $2$ corners. Put the smaller half on one color and the larger half on the other, in the degree order just specified. Every edge then attains equality. The maximum is $4(999-171)+3(486-294)+2(67-63)=3896$, giving $896$.

**Answer:** 896.

**Methods:** extremal arrangements, rearrangement inequality, bipartite graphs.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The sole source gives a plausible checkerboard arrangement and local exchanges but does not prove a global upper bound. The independent midpoint inequality plus rearrangement proves that 3896 is optimal.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2026 AIME I Problem 13: Binomial residue sums over a finite field

For $0\le r<502$, let $S_r$ sum $\binom{10000}{k}$ over $0\le k\le10000$ congruent to $r$ modulo $502$. How many $S_r$ are divisible by $503$?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Over $\mathbb F_{503}$, put $P(x)=\sum_{r=0}^{501}S_rx^r$. For every nonzero $x$, Fermat gives $P(x)=(1+x)^{10000}=(1+x)^{462}$, since $10000\equiv462\pmod{502}$; the equality also holds at $x=-1$. The difference has degree at most $501$ and $502$ roots, so it is identically zero. Thus $S_r=\binom{462}{r}$ modulo $503$ for $r\le462$, and $S_r=0$ for larger $r$. No binomial coefficient in row $462$ vanishes modulo the larger prime $503$, because all relevant factorials are invertible. Exactly $501-462=39$ sums qualify.

**Answer:** 039.

**Methods:** finite-field interpolation, binomial coefficients.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both sources inspected. The finite-field root argument and quotient-ring interpretation are valid; they must handle x=-1 separately before reducing the exponent. Direct modular coefficient calculation confirms 39 zeros.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2026 AIME I Problem 15: Five rectangular cell loops

A cell loop consists of the boundary cells of an axis-aligned rectangle with both dimensions at least two. Count partitions of a $10\times10$ board into five cell loops.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

For an $H\times W$ board with $H\ge W$, take the two cell diagonals $D=\{(i,i):1\le i\le W\}$ and $E=\{(H+1-i,i):1\le i\le W\}$. A rectangular boundary meets either in at most two cells. Thus a partition into $W/2$ loops forces every loop to meet each diagonal twice. Let the upper-left corner loop have dimensions $r\times c$. Its interior is a union of whole loops, so its two diagonal counts are equal: $\min(r,c)-2=r+c-H-2$. (The second count is nonnegative because the corner loop meets $E$ twice.) Hence $\max(r,c)=H$. A tall-board corner loop therefore spans its full height; a square-board corner loop spans at least one side. Its other dimension is even.

Let $T(a,b)$ count partitions of a $2a\times2b$ board into $b$ loops, where $a>b$. A corner loop of width $2k$ leaves independent rectangles $2(a-1)\times2(k-1)$ and $2a\times2(b-k)$, both using their minimum loop counts. Therefore $T(a,b)=\sum_{k=1}^b T(a-1,k-1)T(a,b-k)$, with empty-width count $1$. Induction using the Catalan recurrence gives $T(a,b)=C_b$.

For the square count $S_n$, a full outer-square loop contributes $S_{n-1}$. A proper full-height corner loop contributes $\sum_{k=1}^{n-1}C_{k-1}C_{n-k}$; full-width loops contribute the same. Thus $S_n=S_{n-1}+2(C_n-C_{n-1})$, and $S_0=1$ gives $S_n=2C_n-1$. Finally $S_5=2\binom{10}5/6-1=83$.

**Answer:** 083.

**Methods:** Catalan numbers, diagonal invariants, structural decomposition.

**Verification:** Independent exact-cover enumeration, without using the corner-loop lemma, gives 1,3,9,27,83 for square side lengths 2,4,6,8,10. The 10-by-10 count visits 3053 occupied-cell states.

**Source comparison:** All three archived solutions were read; their structural arguments have gaps or false claims. The independent two-diagonal corner-loop lemma proves the Catalan formula rigorously. See the detailed Catalan-loop addendum.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2026 AIME II Problem 2: Paths through a strip of diagonal squares

Ten adjacent squares each contain their rising diagonal. A path runs from the lower-left endpoint to the upper-right endpoint, never moving left and never reusing an edge. If there are $N$ paths, find $\sqrt N$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

At each vertical boundary a path may use its vertical edge once or not at all. Suppose $b,t$ count arrivals at the lower and upper vertices before this choice. After the optional vertical step there are $b+t$ possibilities at either endpoint. Crossing the next square gives new arrival counts $(b+t,2(b+t))$, using its bottom edge, top edge, or diagonal. Thus the total arrival count triples at each square. Initially $(b,t)=(1,0)$; after ten squares the total is $3^{10}$. At the final boundary every arrival has exactly one way to finish at the upper endpoint. Therefore $N=3^{10}$ and $\sqrt N=243$.

**Answer:** 243.

**Methods:** transfer matrices, path counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All three sources inspected. First-arrival states yield a valid transfer recurrence with total multiplied by 3. The original horizontal-choice claim is terse; the independent proof specifies the optional vertical traversal to make the bijection precise.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2026 AIME II Problem 4: A numeral equal to its value in a smaller base

For positive decimal $n$, reinterpret its digit string in the base one larger than its greatest digit. Count $n<1000$ unchanged by this operation.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Every one-digit number is unchanged. For a longer numeral the value is strictly increasing in its base, so equality requires base $10$, or equivalently a digit $9$. There are $90-8\cdot9=18$ qualifying two-digit numerals and $900-8\cdot9^2=252$ three-digit numerals. Including the nine one-digit numbers gives $9+18+252=279$.

**Answer:** 279.

**Methods:** complement counting, digit restrictions.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both sources inspected. Monotonicity in the base gives the clean criterion; the digit-by-digit alternative reaches the same count by inclusion-exclusion.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2026 AIME II Problem 5: Equal hypergeometric probabilities

An urn has at least seven marbles of each of two colors. Drawing seven without replacement gives equal probabilities of exactly four red marbles and exactly five red marbles. Sum the five smallest possible total populations.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

If the color counts are $r,b$, cancellation in $\binom r4\binom b3=\binom r5\binom b2$ gives $(b-2)/3=(r-4)/5$, or $3r-5b=2$. All solutions have $r=4+5k$, $b=2+3k$. Both counts are at least seven exactly when $k\ge2$. The five smallest totals are $22,30,38,46,54$, whose sum is $190$.

**Answer:** 190.

**Methods:** hypergeometric ratios, Diophantine counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both sources inspected. Cancellation of adjacent hypergeometric coefficients gives 3r-5b=2 and the five totals 22,30,38,46,54.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2026 AIME II Problem 7: Two successes of each kind before a stop

Independent trials choose $A, B$, or $C$ with equal probabilities. If the chance that $A$ and $B$ each occur at least twice before the first $C$ is $m/n$ in lowest terms, find $100m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Ignore $B$ trials when comparing $A$ with $C$. The chance of fewer than two $A$ trials before $C$ is $1/2+1/4=3/4$, and the same holds for $B$. For both counts to be below two, the word before $C$ is empty, one letter, or $AB$ or BA. Its probability is $(1/3)(1+2/3+2/9)=17/27$. Inclusion-exclusion gives $1-3/4-3/4+17/27=7/54$. Thus $100m+n=754$.

**Answer:** 754.

**Methods:** stopping times, inclusion-exclusion.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All five sources inspected. The short first-three-trial conditioning, finite-state recurrence, and terminal-success-word sums are sound. Source index 2 has an unclear overlapping series decomposition and is not relied on. Independent inclusion-exclusion gives 7/54.

**Archived alternatives reviewed:** 5 of 5. Indices in the data are zero-based.

**Status:** solved.

## 2026 AIME II Problem 11: Seven signed square-root sums force a zero sum

Find the greatest integer $n$ such that $x^3-(n/6)x^2+(n-11)x-400$ has roots $\alpha^2,\beta^2,\gamma^2$ and the choices of square roots yield exactly seven distinct values of $\alpha+\beta+\gamma$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

The set of signed sums is closed under negation. A finite such set of odd size must contain zero, so choose signs with $\alpha+\beta+\gamma=0$. Vieta gives $\alpha^2+\beta^2+\gamma^2=n/6$ and $\alpha^2\beta^2+\beta^2\gamma^2+\gamma^2\alpha^2=n-11$. Thus $q=\alpha\beta+\beta\gamma+\gamma\alpha=-n/12$, while $q^2=n-11$ because its cross terms are $2\alpha\beta\gamma(\alpha+\beta+\gamma)=0$. Hence $n^2-144n+1584=0$, giving $n=12$ or 132. To attain 132, choose $\alpha=4$, $\beta=-2+i$, $\gamma=-2-i$. Their squares are the roots of $x^3-22x^2+121x-400$. Their signed sums are exactly $0,\pm8,\pm(-4+2i),\pm(-4-2i)$, seven distinct values. Therefore the greatest integer is 132.

**Answer:** 132.

**Methods:** negation involution, signed sums, Vieta formulas, attainment.

**Verification:** Exact Gaussian-integer expansion verifies roots 16,3−4 i,3+4 i and exactly seven distinct signed sums; the necessary quadratic has only integer roots 12 and 132.

**Source comparison:** Both alternatives read. Source 0 asserts that other sign collisions give too few values without proof; central symmetry supplies a one-line rigorous reason that zero must occur. Source 1 has a sign slip in the coefficient comparison for its auxiliary cubic. Neither explicitly verifies seven distinct sums at the larger candidate; the concrete roots do so.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.

## 2026 AIME II Problem 13: Sets with a prescribed number of adjacent partners

Finite integer sets $S,T$ are cousins when they are disjoint, equally large, and admit a pairing with paired values differing by one. Find the smallest size of $S$ having exactly $4040$ cousins.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Build the bipartite graph joining each member of $S$ to its neighbors outside $S$. Components are alternating paths or isolated vertices. A component with more $S$ vertices than outside vertices makes cousins impossible. A component with equal counts has a unique matching saturating $S$. A component with $k$ vertices in $S$ and $k+1$ outside has exactly $k+1$ possible partner sets: omit one outside vertex; the matching is then forced. Consequently the number of cousins is a product of factors $k+1$, whose total vertex cost is at least $\sum k$. Splitting a composite factor $uv$ into $u,v$ decreases cost from $uv-1$ to $(u-1)+(v-1)$. Since $4040=101\cdot5\cdot2^3$, the minimum cost is $100+4+1+1+1=107$. Achieve it with widely separated arithmetic progressions of difference two and lengths $100,4,1,1,1$.

**Answer:** 107.

**Methods:** matching components, multiplicative partitions.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The sole source counts separated step-two progressions but omits justification for arbitrary integer sets. The independent bipartite-path component argument handles forced matchings, impossible components, and the prime-factor lower bound.

**Archived alternatives reviewed:** 1 of 1. Indices in the data are zero-based.

**Status:** solved.

## 2026 AIME II Problem 14: Compositions with parity-dependent subtraction

For integers $a,b$, define $a\circ b=a-b$ when $a$ is odd and $b$ even, and $a+b$ otherwise. Count positive-integer sequences of sum $12$ whose left-associated operation value is zero.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

The running parity equals the parity of the ordinary prefix sum. Therefore only even terms following an odd number of odd terms are subtracted. Added and subtracted totals must each be $6$. Suppose there are $2k$ odd terms with total $2h$, where $1\le k\le h\le3$. Their choices number $\binom{h+k-1}{2k-1}$. There are $k$ subtracted even gaps and $k+1$ added even gaps. Measuring even terms in units of two, a gap has generating function $F(z)=(1-z)/(1-2z)$, since a positive total $j$ has $2^{j-1}$ compositions. Thus the desired sum is $\sum_{1\le k\le h\le3}\binom{h+k-1}{2k-1}[z^3]F(z)^k\,[z^{3-h}]F(z)^{k+1}$. For $(k,h)=(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)$, the contributions are $20,16,12,36,48,25$. Their sum is $157$.

**Answer:** 157.

**Methods:** parity states, compositions, generating functions.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All three sources inspected. The parity-gap method and finite dynamic program are valid approaches. Source index 1 incorrectly states that an added-gap total 2 has 2k placements; it has $k$+1 placements. The independent generating-function sum and exhaustive 2048-composition check give 157.

**Archived alternatives reviewed:** 3 of 3. Indices in the data are zero-based.

**Status:** solved.

## 2026 AIME II Problem 15: A Fano-plane residue count

Count ordered seven-tuples with entries in $\{1,2,3\}$ for which both $\sum_i a_i$ and $\sum_i a_i a_{i+1}a_{i+3}$ are divisible by three; indices are cyclic modulo seven.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Replace entries by their residues $0,\pm1$. The seven triples $\{i,i+1,i+3\}$ are the lines of the Fano plane: each pair lies on one line. Classify by support size $w$. For $w=0,1,2,3$, counts are $1,0,42,56$: two signs must oppose, while three signs must agree and their support must avoid the seven lines. For $w=4$, signs split two and two; the support must contain no line, hence be the complement of a line. Count $7\binom42=42$. For $w=5$, its two contained lines meet at one point. Four signs agree and one differs; their two products cancel exactly when the minority sign is at one of the other four points. Count $\binom72\cdot8=168$. For $w=6$, all equal signs fail; among the $\binom63=20$ balanced assignments, exactly eight fail because the plus or minus triple is one of the four contained lines. Count $7(20-8)=84$. For $w=7$, signs split five and two; the seven products comprise three of one sign and four of the other, so none qualify. Total $1+42+56+42+168+84=393$.

**Answer:** 393.

**Methods:** finite geometry, Fano plane, residue counting.

**Verification:** Independently enumerated all $3^7=2187$ residue assignments; the support-count distribution is $1,0,42,56,42,168,84,0$.

**Source comparison:** Both sources inspected. Source index 0 incorrectly replaces entries by a_i-2 rather than their actual residues; its later support analysis corresponds to the correct residue mapping. Source index 1 uses the correct mapping but has mistaken line-containment wording and omits all-equal signs at weight 6, so it is not a complete proof. The independent Fano support count was exhaustively checked on all 2187 tuples. Clean statement includes all seven cyclic terms.

**Archived alternatives reviewed:** 2 of 2. Indices in the data are zero-based.

**Status:** solved.
