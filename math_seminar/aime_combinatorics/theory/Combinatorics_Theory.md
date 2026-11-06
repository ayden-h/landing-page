---
title: "AIME Combinatorics"
subtitle: "Structure, short proofs, and exact enumeration"
author: "Ayden Bi"
date: "Research edition · November 2026"
lang: en-US
---

# The discipline of a short solution

A short combinatorial solution is a proof that the objects have a simpler description. Multiplying three numbers is not the hard part. The hard part is proving that the three choices are independent, that every desired object appears, and that none appears twice. This book develops the tools for that proof.

The accompanying historical collection identifies AIME problems by year, examination, and number. `1983-A-07` means Problem 7 of the single 1983 examination; `2026-II-02` means Problem 2 of AIME II in 2026. Mathematical restatements and newly written solutions are distinguished from the linked published sources. The coverage report gives the exact inclusion rule and verification status. Probability and substantive algebraic, geometric, and number-theoretic counting problems belong to the collection; merely having finitely many integer answers does not make a problem combinatorics.

The results below are classical unless explicitly called a derived proposition. The contribution is their arrangement into a working system and their application to the archive. A new name for a useful observation is not a claim of a new mathematical discovery.

## Four questions before the first formula

1. **What is an object?** A subset, ordered tuple, word, function, partition, path, or equivalence class? Write its definition.
2. **What distinctions survive?** Are labels, order, orientation, repeated values, and rotations relevant?
3. **What data determine it?** Seek a reversible encoding with the fewest constraints.
4. **What is actually requested?** A count, probability, weighted sum, maximum, remainder, or numerator-plus-denominator? Avoid solving a harder problem.

If a formula divides by a factorial, name the operation whose fibers have that size. If a probability divides two counts, state why the denominator's elementary outcomes are equally likely. If a recurrence merges states, explain why the discarded information cannot influence the future.

## The compression hierarchy

Try, in order: a bijection; a complement; a distinguished feature; gaps or runs; a small disjoint case split; inclusion-exclusion; a recurrence on a sufficient state; a generating function; symmetry averaging. This order is a default, not a law. A permutation constrained by its powers almost asks for cycle decomposition; a residue condition often asks immediately for a residue state or filter.

The strongest simplification is structural. In 2026-II-02, a path through a strip with ten diagonals can be encoded by the one rightward crossing chosen in each strip. Once existence and uniqueness of the intervening vertical moves are proved, the count is $3^{10}$. A large path recursion was avoidable because a global bijection existed.

## Notation and boundary conventions

Write $[n]=\{1,\ldots,n\}$. For integer $n\ge0$, use $\binom nk=0$ when $k<0$ or $k>n$. A coefficient $[x^n]F(x)$ is zero for $n<0$ when $F$ is a power series. The empty word, empty set, and empty selection each contribute one object. The empty product is one. The factorial $0!$ equals one.

These conventions remove many exceptions, but not all. A composition of zero into a positive number of positive parts does not exist; the empty composition is a separate object. A cycle of length one and a cycle of length two require care when a graph argument assumes distinct neighbors.

# 1. Bijections, fibers, and weighted counting

## 1.1 The basic theorem

**Definition.** A bijection is a map that is both injective and surjective. A fiber of $f:X\to Y$ is $f^{-1}(y)$ for a particular $y\in Y$.

**Theorem 1.1 (fiber counting).** For finite sets,

$$|X|=\sum_{y\in Y}|f^{-1}(y)|.$$

In particular, a surjection with exactly $r$ preimages per target gives $|X|=r|Y|$.

**Proof.** The fibers partition $X$: every element has one image, and two different images have disjoint preimages. Count the parts. $\square$

**When it shortens a solution.** Introduce labels or a distinguished point to make construction easy; divide them away only after proving constant multiplicity. Arranging $n$ distinct people around an unmarked oriented table has $n!/n=(n-1)!$ possibilities. The same division is false for a necklace with repeated colors: some necklaces have more rotational symmetries than others.

**Theorem 1.2 (weighted double counting).** For a relation $R\subseteq X\times Y$ and weights $w(x,y)$,

$$\sum_{x\in X}\sum_{y:(x,y)\in R}w(x,y)
=\sum_{y\in Y}\sum_{x:(x,y)\in R}w(x,y).$$

**Proof.** Both sides add the weight of every pair in $R$ once. $\square$

This is the finite combinatorial form of interchanging sums. To sum subset sizes, count incidences $(S,i)$ with $i\in S$. Each of the $n$ elements occurs in $2^{n-1}$ subsets, so

$$\sum_{S\subseteq[n]}|S|=n2^{n-1}.$$

To sum a nonlinear statistic, first see whether it counts smaller features. For example, $\binom{|S|}{r}$ counts the $r$-subsets contained in $S$:

$$\sum_{S\subseteq[n]}\binom{|S|}{r}=\binom nr2^{n-r}.$$

## 1.2 Cancellation by an involution

**Definition.** An involution is a map $\iota:X\to X$ with $\iota(\iota(x))=x$.

**Lemma 1.3.** If $w(\iota(x))=-w(x)$ on all nonfixed pairs, then $\sum_Xw$ equals the sum of weights at fixed points.

**Proof.** Pair $x$ with $\iota(x)$. Each nontrivial pair contributes zero. $\square$

**Derived proposition 1.4 (alternating subset sum).** Arrange each nonempty subset of $[n]$ in decreasing order and alternately add and subtract its entries, starting with plus. The total over all subsets is $n2^{n-1}$.

**Proof.** For an entry $j<n$, toggle the membership of $j+1$ in each subset containing $j$. This reverses the parity of the number of entries above $j$, hence cancels its signed contribution. The entry $n$ always has positive sign and occurs in $2^{n-1}$ subsets. $\square$

**Historical use.** For 1983-A-13, $n=7$ and the answer is $448$. The proof never lists subsets and never evaluates their individual sums. Its generalization is the useful object to remember.

**Failure test.** A proposed cancellation must preserve the domain. Toggling an element is invalid if subsets are required to have a fixed cardinality, unless the mapping is modified accordingly.

# 2. Linear and circular gaps

## 2.1 Compositions from separators

**Theorem 2.1 (stars and bars).** The number of nonnegative integer solutions of $x_1+\cdots+x_k=N$, for $k\ge1$ and $N\ge0$, is $\binom{N+k-1}{k-1}$. The number of positive solutions is $\binom{N-1}{k-1}$ when $N\ge k$.

**Proof.** Encode a nonnegative solution by $N$ stars separated into $k$ possibly empty blocks by $k-1$ bars. Choose the bar positions. For positive solutions put $y_i=x_i-1$. $\square$

**Corollary 2.2.** The number of ordered compositions of a positive integer $N$, with arbitrary positive length, is $2^{N-1}$.

**Proof.** Between $N$ consecutive units there are $N-1$ gaps. Independently insert a separator or do not. $\square$

**Historical use.** In 2026-I-02, a zero-free decimal palindrome with digit sum $13$ has an odd central digit $c$. Its left half has sum $(13-c)/2\in\{2,3,4,5,6\}$. All parts are automatically at most $9$, so the total is $2^1+2^2+2^3+2^4+2^5=62$. The upper digit bound matters for larger sums; do not silently use unrestricted compositions there.

## 2.2 Separation on a line

**Theorem 2.3 (gap removal).** For $k\ge1,d\ge0$ and $n\ge k+d(k-1)$, the $k$-subsets $1\le a_1<\cdots<a_k\le n$ satisfying $a_{i+1}-a_i\ge d+1$ are counted by

$$\binom{n-d(k-1)}k.$$

If $n<k+d(k-1)$ there are no such subsets.

**Proof.** Put $b_i=a_i-d(i-1)$. The inequalities become $1\le b_1<\cdots<b_k\le n-d(k-1)$. The map and its inverse preserve integer sequences. $\square$

The theorem is preferable to placing chosen objects and then trying to distribute unused locations: its inverse certifies that no end-gap condition was lost.

## 2.3 Separation on a labeled circle

**Theorem 2.4.** For integers $n\ge1,k\ge1,d\ge0$, on a circle of $n$ labeled positions choose $k$ positions so that every clockwise gap between successive chosen positions contains at least $d$ unchosen positions. If $n\ge(d+1)k$, the count is

$$\frac nk\binom{n-dk-1}{k-1}
=\frac{n}{n-dk}\binom{n-dk}{k}.$$

**Proof.** Distinguish one chosen position: $n$ choices. Let $g_i\ge d$ be the $k$ intervening unchosen-gap sizes. They sum to $n-k$. After subtracting $d$ from each, stars and bars gives $\binom{n-dk-1}{k-1}$. Every unmarked selection has $k$ choices for the distinguished position. $\square$

**Historical use.** In 1983-A-07, the complement of having an adjacent pair is choosing three nonadjacent positions on a 25-cycle. It has $\frac{25}{22}\binom{22}{3}=1750$ choices. Out of $\binom{25}{3}=2300$, the desired probability is $550/2300=11/46$, giving $57$.

**Trap.** The factor $n/k$ counts distinguished selections on a labeled circle; it is not the quotient by rotation. These are different counting problems.

# 3. Runs, blocks, and local constraints

**Definition.** A run in a word is a maximal consecutive block of equal symbols.

**Theorem 3.1 (binary run count).** A binary word containing $a>0$ copies of $A$ and $b>0$ copies of $B$, with $r$ runs of $A$ and $s$ runs of $B$, has

$$\binom{a-1}{r-1}\binom{b-1}{s-1}c(r,s)$$

realizations, where $c(r,s)=2$ if $r=s$, $1$ if $|r-s|=1$, and $0$ otherwise.

**Proof.** Choose the positive run lengths of each color. The run colors must alternate. If their counts agree either color can start; otherwise the more frequent run color must start and end. $\square$

**Corollary 3.2.** A word of length $N$ with $R$ runs has $R-1$ adjacent unequal pairs and $N-R$ adjacent equal pairs.

**Proof.** Unequal pairs occur precisely at boundaries between runs. The remaining $N-1-(R-1)$ pairs are equal. $\square$

This converts a comparison of adjacent-pair counts into a single equation in the number of runs. Equal numbers of equal and unequal adjacent pairs force $N=2R-1$. With five copies of one color, there are at most five runs of that color and at most six of the other. Thus $R\le11$, immediately bounding the total length by $21$. The extremal arrangement has five isolated copies of the first color between six nonempty runs of the second. This is the structural core of 2011-II-07.

**Proposition 3.3 (forced blocks).** When a specified collection of distinct objects must be consecutive in a linear arrangement, contract it to a single block and multiply by its admissible internal arrangements.

The proposition is a bijection only if the decomposition into blocks is unambiguous. Overlapping adjacency requirements are better represented by a graph: required adjacencies on distinct objects can form disjoint paths, but a vertex of required degree three is impossible in a line. A required cycle of more than two vertices cannot appear in a linear arrangement using each vertex once.

**Diagnostic.** Use blocks for mandatory adjacency; gaps for forbidden adjacency; runs for a specified number of changes. Using the wrong one usually manufactures unnecessary cases.

# 4. Occupancy, capacities, and inclusion-exclusion

## 4.1 The model precedes the formula

Putting $n$ distinct objects into $k$ labeled boxes has $k^n$ outcomes. Putting $n$ indistinguishable objects into those boxes has $\binom{n+k-1}{k-1}$ outcomes. Neither formula describes unlabeled boxes. Write down what distinguishes the objects and boxes before using either.

**Theorem 4.1 (inclusion-exclusion).** For forbidden properties $A_1,\ldots,A_m$ in a finite universe $U$, the count avoiding all properties is

$$\sum_{J\subseteq[m]}(-1)^{|J|}\left|\bigcap_{j\in J} A_j\right|,$$

where the empty intersection is $U$.

**Proof.** An object with exactly $t$ forbidden properties has total coefficient $\sum_{j=0}^t(-1)^j\binom tj=(1-1)^t$. This equals one for $t=0$ and zero otherwise. $\square$

## 4.2 Bounded compositions

**Theorem 4.2.** The number of solutions of $x_1+\cdots+x_k=N$ with $0\le x_i\le u_i$ is

$$\sum_{J\subseteq[k]}(-1)^{|J|}
\binom{N-\sum_{j\in J}(u_j+1)+k-1}{k-1},$$

interpreting a term as zero if its remaining sum is negative.

**Proof.** For the event $x_j\ge u_j+1$, subtract $u_j+1$ from that coordinate. Apply stars and bars to every intersection and then Theorem 4.1. $\square$

If all bounds equal $u$, group intersections by cardinality:

$$\sum_{j=0}^{\lfloor N/(u+1)\rfloor}(-1)^j\binom kj
\binom{N-j(u+1)+k-1}{k-1}.$$

Lower bounds are removed first. Unequal upper bounds usually favor a generating function or a short dynamic program over a $2^k$ expansion.

## 4.3 Surjections and fixed points

**Corollary 4.3.** The number of onto functions $[n]\to[k]$ is

$$\sum_{j=0}^k(-1)^j\binom kj(k-j)^n.$$

**Proof.** Forbid the omission of each target label. Omitting a specified $j$ labels leaves $(k-j)^n$ functions. $\square$

**Corollary 4.4.** The number of permutations of $n$ labels with no fixed point is $D_n=n!\sum_{j=0}^n(-1)^j/j!$. The number with exactly $r$ fixed points is $\binom nrD_{n-r}$.

**Proof.** Forcing $j$ designated fixed points leaves $(n-j)!$ permutations. For exactly $r$, choose those points and derange everything else. $\square$

**Trap.** Choosing $r$ fixed points and freely permuting the others counts permutations with *at least* those fixed points, not exactly $r$ fixed points.

# 5. Permutation cycles and symmetry

## 5.1 Powers of a permutation

**Theorem 5.1.** A permutation $\pi$ satisfies $\pi^m=\mathrm{id}$ if and only if every cycle length divides $m$.

**Proof.** On a cycle of length $d$, $\pi^m$ moves a point $m$ steps. It fixes every point of that cycle exactly when $d\mid m$. The cycles are disjoint. $\square$

**Theorem 5.2 (cycle inventory).** If nonnegative integers $c_d$ satisfy $\sum_dc_dd=n$, then the number of permutations with $c_d$ cycles of length $d$ for each $d$ is

$$\frac{n!}{\prod_d d^{c_d}c_d!}.$$

**Proof.** Arrange the labels in a list and cut into blocks of the specified lengths. Each cycle is represented $d$ times by rotating its list, and equal-length cycles can be ordered in $c_d!$ ways. Divide exactly those repetitions. $\square$

**Short route.** For $\pi^6=\mathrm{id}$ on six labels, only lengths $1,2,3,6$ are allowed. Partitions using $1,2$ alone contribute $1+15+45+15=76$; a single 3-cycle with the rest of lengths 1 or 2 contributes $40+120$; two 3-cycles contribute $40$; a 6-cycle contributes $120$. Total $396$. This solves 2026-I-07 by classifying cycle structure before arranging labels.

## 5.2 Burnside's lemma

**Definition.** A finite group $G$ acts on a set $X$ by permutations compatible with group multiplication. An orbit is the set of objects obtained from one object under the action. A stabilizer is $G_x=\{g:g(x)=x\}$.

**Theorem 5.3 (Burnside).** The number of orbits is

$$\frac1{|G|}\sum_{g\in G}|\operatorname{Fix}(g)|.$$

**Proof.** Count pairs $(g,x)$ with $g(x)=x$. Within an orbit $O$, every stabilizer has size $|G|/|O|$ by the bijection between cosets of a stabilizer and orbit points. Therefore that orbit contributes $|O|\cdot|G|/|O|=|G|$ pairs. $\square$

**Corollary 5.4.** A rotation by $r$ positions on $n$ positions has $\gcd(n,r)$ position-cycles. The number of $q$-colorings it fixes is $q^{\gcd(n,r)}$.

For fixed color multiplicities, each position-cycle must be monochromatic and consumes its entire length. A rotation with all position-cycles of length $d$ fixes no coloring unless every color multiplicity is divisible by $d$.

**Trap.** A painted cube, necklace, bracelet, and labeled circular seating have different equivalence relations. List the allowed transformations first. Include reflections only when the statement identifies mirror images.

# 6. Recurrences and sufficient states

## 6.1 The state theorem

**Definition.** Two partial constructions have the same future type if every allowable continuation of one corresponds to an allowable continuation of the other, preserving the statistic being counted.

**Theorem 6.1 (exact state compression).** If partial constructions are partitioned into future types and the number or weight of each extension depends only on the type, counting transitions between types gives the exact total.

**Proof.** Induct on the construction length. At the initial length the type counts are correct. Every longer object has a unique predecessor and last extension; summing the appropriate transitions counts it once. $\square$

This is the theorem behind dynamic programming. It is also a proof standard: a recurrence must specify its state, transitions, initial conditions, terminal sum, and why no hidden history matters.

## 6.2 A complete example

Count binary strings of length $n$ containing no consecutive ones. Let $a_n$ be the count. Split by their final block: a string ending in $0$ follows any valid length-$n-1$ string; a string ending in $1$ either has length one or ends in $01$ after a valid length-$n-2$ string. Thus

$$a_n=a_{n-1}+a_{n-2},\qquad a_0=1,\ a_1=2.$$

Alternatively keep two states for the last symbol, with transition matrix

$$T=\begin{pmatrix}1&1\\1&0\end{pmatrix}.$$

The scalar recurrence is shorter. The two-state view generalizes more easily when a second constraint, such as the number of ones modulo three, is added.

## 6.3 Residues and digit states

For a base-$b$ numeral, appending a digit $d$ changes the residue $r$ modulo $m$ to $br+d\pmod m$. Combine this with the necessary suffix information and a leading-zero flag. A state might be $(i,r,\ell)$: length $i$, residue $r$, last digit $\ell$.

For subset products modulo $m$, the transition is $r\mapsto ar\pmod m$ when the next element $a$ is included. Multiplication may not be invertible: merging residues by a false cancellation destroys the count when $\gcd(a,m)>1$.

**Derived proposition 6.2 (complementary information).** If a construction has a conserved total, storing all but one coordinate is sufficient; the last coordinate is determined by the total and the others.

This often reduces a two-dimensional occupancy table to one dimension, or a seven-variable residue search to six free variables. The proposition saves work only after the conservation law and allowed range of the recovered coordinate have been checked.

## 6.4 Matrix and scalar forms

If $v_{n+1}=Tv_n$ for a fixed finite matrix, then $v_n=T^nv_0$. Matrix powers are an evaluation device; the combinatorial proof remains the transition bijection. For small AIME parameters, writing out the short recurrence is usually clearer than diagonalizing a large matrix.

**Boundary test.** Evaluate the recurrence for lengths zero, one, and two by hand. Most faulty recurrences first fail at a boundary, not at the requested large index.

# 7. Generating functions as exact encodings

## 7.1 The coefficient theorem

**Definition.** The ordinary generating function of counts $a_n$ is the formal series $A(x)=\sum_{n\ge0}a_nx^n$. Formal series need no convergence argument when each requested coefficient is obtained from finitely many choices.

**Theorem 7.1 (occupancy coefficient).** If labeled box $i$ allows occupancies from a set $S_i\subseteq\mathbb Z_{\ge0}$, then the number of occupancy vectors totaling $N$ is

$$[x^N]\prod_i\left(\sum_{s\in S_i}x^s\right).$$

**Proof.** Choosing a term in each factor chooses its box's occupancy. Multiplication adds the occupancies as exponents. The coefficient counts exactly the choices with total $N$. $\square$

If an occupancy $s$ has $w_i(s)$ internal realizations, replace $x^s$ by $w_i(s)x^s$. This weighted form unifies almost every elementary generating-function argument.

**Theorem 7.2 (distinct objects).** For $N$ distinct objects assigned to labeled boxes under the same occupancy restrictions, the count is

$$N![x^N]\prod_i\left(\sum_{s\in S_i}\frac{x^s}{s!}\right).$$

**Proof.** A vector $(s_1,\ldots,s_k)$ has $N!/(s_1!\cdots s_k!)$ assignments. The coefficient supplies exactly that factorial weight. $\square$

Ordinary coefficients count occupancy vectors; factorial-weighted coefficients count allocations of distinct objects. Choosing the wrong one changes the probability distribution as well as the count.

## 7.2 Unique concatenation and first returns

**Theorem 7.3.** Suppose every finite ordered sequence of allowed nonempty blocks forms an object, and each object has exactly one such decomposition. Let the block generating function be $B(x)$, with size additive under concatenation. Then its generating function, including the empty object, is

$$F(x)=\frac1{1-B(x)}.$$

**Proof.** Exactly $j$ blocks contribute $B(x)^j$. Unique parsing prevents duplicate descriptions; positive block size makes each coefficient a finite sum. Sum the geometric series. $\square$

**Counterexample.** With blocks `0` and `00`, the word `00` has two descriptions. The formula counts block descriptions, not distinct words. A canonical cut, such as a first return or a compulsory separator, is often the missing ingredient.

**Theorem 7.4 (Catalan recurrence).** Let $C_n$ count paths with $n$ up-steps and $n$ down-steps that start at height zero and never go below zero. Then

$$C_0=1,\qquad C_n=\sum_{j=0}^{n-1}C_jC_{n-1-j}.$$

**Proof.** The first up-step has a unique matching down-step at the first return to height zero. The intervening path, shifted down one unit, and the remaining path are independently nonnegative balanced paths. Their numbers of up-steps sum to $n-1$. This decomposition is reversible. $\square$

The recurrence also counts many recursively nested objects, but a picture that resembles parentheses is not enough. Establish the first-return decomposition for the particular objects.

## 7.3 Rational functions and recurrences

**Proposition 7.5.** If $a_n=c_1a_{n-1}+\cdots+c_ra_{n-r}$ for $n\ge r$, then

$$A(x)=\frac{P(x)}{1-c_1x-\cdots-c_rx^r},\qquad \deg P<r.$$

**Proof.** Multiply the series by the denominator. Every coefficient of degree at least $r$ vanishes by the recurrence. The remaining coefficients form $P$. $\square$

This provides a useful two-way conversion. A rational generating function may reveal a small recurrence; a recurrence may reveal a factorization or telescoping identity. Do not expand a high-degree rational expression when a few recurrence steps give the desired coefficient.

# 8. Paths, barriers, and reflection

## 8.1 Unrestricted and constrained paths

A north-east path from $(0,0)$ to $(a,b)$ is a word with $a$ east steps and $b$ north steps, hence there are $\binom{a+b}{b}$ paths. Passing through a specified intermediate point splits the path into two independent segments. Avoiding several points is a problem about intersections of forbidden events; incompatible point orders give zero intersection counts.

**Theorem 8.1 (reflection principle).** For $a\ge b\ge0$, the number of north-east paths from $(0,0)$ to $(a,b)$ that never enter $y>x$ is

$$\binom{a+b}{b}-\binom{a+b}{b-1}.$$

**Proof.** A bad path first reaches $y=x+1$. Interchange north and east steps up to that first reach. The transformed path has $a+1$ east steps and $b-1$ north steps. Conversely, a path with those totals must first reach $x=y+1$; reflecting that prefix restores a unique bad path. Subtract the bad paths. $\square$

**Corollary 8.2.** $C_n=\binom{2n}{n}/(n+1)$.

**Proof.** Set $a=b=n$ and simplify the difference. $\square$

## 8.2 Shifted barriers

**Proposition 8.3.** Suppose $a,b,h$ are nonnegative integers and $b\le a+h$. The number of paths to $(a,b)$ satisfying $y\le x+h$ at every prefix is

$$\binom{a+b}{b}-\binom{a+b}{b-h-1}.$$

**Proof.** Reflect the prefix through its first visit to $y=x+h+1$. In that prefix, north steps exceed east steps by $h+1$. Interchanging the steps transforms the final totals to $(a+h+1,b-h-1)$. The same first-crossing construction reverses the map. $\square$

**Trap.** The final inequality does not enforce all prefix inequalities. Reflection proves a statement about the entire path. With two barriers or unequal step sizes, the one-reflection formula usually fails; a height recurrence may be simpler.

## 8.3 A path-solving protocol

Translate geometry into a word of moves. Determine which portions of the path are forced after the essential choices. If a barrier remains, locate the *first* forbidden event. If reflection changes the allowed step set or creates another restriction, use a finite state. For a circle or periodic strip, verify the final-to-initial compatibility explicitly.

# 9. Probability without a misleading sample space

## 9.1 Conditional probability and revelation

**Definition.** For an event $B$ with positive probability, $P(A\mid B)=P(A\cap B)/P(B)$.

**Theorem 9.1 (conditioning).** If $B_1,\ldots,B_k$ partition the sample space, then

$$P(A)=\sum_{i:P(B_i)>0}P(B_i)P(A\mid B_i).$$

**Proof.** The events $A\cap B_i$ partition $A$. $\square$

Reveal the variable that removes dependence: the first repeated outcome, the occupied colors, the maximum selected value, or the last occurrence of a distinguished symbol. Revealing a convenient variable does not make its possible values equally likely.

**Theorem 9.2 (hypergeometric sampling).** A uniform sample of $s$ distinct objects from a population with category sizes $n_1,\ldots,n_k$ has occupancy vector $(a_1,\ldots,a_k)$ with probability

$$\frac{\prod_i\binom{n_i}{a_i}}{\binom{\sum_i n_i}{s}},\qquad \sum_i a_i=s.$$

**Proof.** Choose the sampled subset within each category. All $s$-subsets of the population are equally likely. $\square$

**Derived proposition 9.3 (adjacent occupancy ratio).** In a two-color population of $r$ red and $b$ blue objects, write $p_j$ for the probability of exactly $j$ red objects in a sample of size $s$. Wherever both probabilities are positive,

$$\frac{p_{j+1}}{p_j}=\frac{r-j}{j+1}\frac{s-j}{b-s+j+1}.$$

**Proof.** Divide the two formulas in Theorem 9.2 and cancel adjacent binomial coefficients. $\square$

This ratio is often far shorter than expanding factorials. For 2026-II-05, equality of the four-red and five-red probabilities in a seven-object sample gives $3(r-4)=5(b-2)$. Put $r=5t+4$ and $b=3t+2$; both colors at least seven force $t\ge2$. The five least total populations are $22,30,38,46,54$, summing to $190$.

## 9.2 Indicators and factorial moments

**Definition.** The indicator $I_A$ of an event is one on $A$ and zero otherwise.

**Theorem 9.4.** $E[I_A]=P(A)$, and for any finite collection of random variables with finite expectations,

$$E[X_1+\cdots+X_k]=E[X_1]+\cdots+E[X_k].$$

**Proof.** Expand the expectations as finite weighted sums and interchange the sums. Independence is unnecessary. $\square$

If $X=\sum_iI_i$, then

$$E\binom X2=\sum_{i<j}P(I_i=I_j=1).$$

This follows by counting unordered pairs of successful indicators. It is often the clean route to a second moment.

**Example.** For integers $n\ge3$ and $0\le k\le n$, a uniform $k$-subset of the vertices of an $n$-cycle contains an expected $k(k-1)/(n-1)$ cycle edges: each of the $n$ edges has both endpoints selected with probability $k(k-1)/(n(n-1))$. Neighboring edge events are dependent, but linearity remains valid.

**Trap.** In general $E[X/Y]\ne E[X]/E[Y]$. For a nonnegative integer-valued count $X$, $P(X\ge1)$ need not equal $E[X]$; they agree exactly when $X$ is an indicator almost surely.

## 9.3 Last occurrence and overwritten labels

If labels are placed successively onto randomly chosen boxes and later labels cover earlier labels, a label remains visible exactly when its box is not chosen later. This changes a physical story into a restriction on repeated positions in a word. Conditioning on several labels remaining visible imposes restrictions on overlapping suffixes, not independent survival events. Count the compatible words or expose the protected boxes in reverse time.

This representation is useful in 2026-I-09. Its value lies in identifying the elementary outcomes before computing the conditional probability. Multiplying unconditional survival probabilities would overlook their dependence.

# 10. Continuous probability and order

Continuous probability belongs in a counting course when its structure is a finite symmetry or a volume decomposition. A density must be specified: choosing a chord by endpoints, midpoint, or distance from the center gives different probability models.

## 10.1 Sorting uniform samples

**Theorem 10.1 (order regions).** If $U_1,\ldots,U_n$ are independent uniform random variables on $[0,1]$, every strict ordering of their coordinates has probability $1/n!$.

**Proof.** Coordinate permutations preserve volume in the unit cube and carry any ordering region to any other. Ties lie on finitely many hyperplanes of zero volume. The $n!$ regions partition the cube outside those hyperplanes. $\square$

**Proposition 10.2 (extreme-value tails).** For $0\le t\le1$,

$$P(\max U_i\le t)=t^n,\qquad P(\min U_i>t)=(1-t)^n.$$

**Proof.** In the first event all coordinates lie in $[0,t]$; in the second all lie in $(t,1]$. Independence multiplies the interval lengths. $\square$

**Theorem 10.3 (random gaps).** For integer $n\ge2$, sorting $n-1$ independent uniform points in $[0,1]$ produces $n$ nonnegative gaps totaling one, uniformly distributed in the corresponding simplex with respect to $(n-1)$-dimensional volume. For $0\le t\le1$, a specified gap exceeds $t$ with probability $(1-t)^{n-1}$.

**Proof.** The ordered-point region has constant density $(n-1)!$. Passing to successive gaps is a linear map with determinant one in the first $n-1$ coordinates. Requiring a gap to exceed $t$, then subtracting $t$ from it, leaves a simplex whose linear scale is $1-t$ in $n-1$ dimensions. $\square$

**Example.** Two uniform cuts of a unit stick form a triangle exactly when no gap exceeds $1/2$. The three events of a specified gap exceeding $1/2$ are disjoint apart from boundaries. Their total probability is $3(1/2)^2=3/4$, so the triangle probability is $1/4$.

**Trap.** This model is not the same as choosing the first cut uniformly and then choosing one resulting piece uniformly to cut again. The second procedure changes the distribution.

# 11. Residues, digits, and finite fields

## 11.1 Filters

**Theorem 11.1 (root-of-unity filter).** For a polynomial $F(x)=\sum_jc_jx^j$ and $\omega=e^{2\pi i/m}$,

$$\sum_{j\equiv r\ (\mathrm{mod}\ m)}c_j
=\frac1m\sum_{t=0}^{m-1}\omega^{-rt}F(\omega^t).$$

**Proof.** After expanding $F$, the multiplier of $c_j$ is $m^{-1}\sum_t\omega^{t(j-r)}$. A finite geometric sum makes it one when $m\mid j-r$ and zero otherwise. $\square$

Use the filter when polynomial evaluations collapse. Otherwise a residue recurrence is usually easier. “There are $m$ residue classes” does not imply that the counts are equal.

## 11.2 Binomial coefficients modulo a prime

**Theorem 11.2 (Lucas).** Let $p$ be prime and write $n=\sum n_ip^i$, $k=\sum k_ip^i$ in base $p$. Then

$$\binom nk\equiv\prod_i\binom{n_i}{k_i}\pmod p.$$

**Proof.** Over the field $\mathbb F_p$, $(1+x)^p=1+x^p$ because the intermediate binomial coefficients are divisible by $p$. Thus $(1+x)^n=\prod_i(1+x^{p^i})^{n_i}$. Each exponent choice has a unique base-$p$ expansion since $0\le n_i<p$. Compare the coefficient of $x^k$. $\square$

**Corollary 11.3.** $\binom nk$ is nonzero modulo $p$ precisely when $k_i\le n_i$ for every digit. The number of nonzero binomial coefficients in row $n$ modulo $p$ is $\prod_i(n_i+1)$.

For $p=2$, the allowed $k$ are exactly the bitwise submasks of $n$. A divisibility problem becomes a digit-choice problem.

## 11.3 A finite-field coefficient sieve

**Lemma 11.4.** For prime $p$ and integer $e>0$,

$$\sum_{a\in\mathbb F_p}a^e=
\begin{cases}-1,&p-1\mid e,\\0,&p-1\nmid e,\end{cases}$$

in $\mathbb F_p$. For $e=0$, the sum is $p=0$ in the field.

**Proof.** Multiplication by a nonzero element permutes the $p-1$ nonzero elements. Taking their product proves $a^{p-1}=1$. Reduce $e$ modulo $p-1$. If its remainder is zero, every nonzero summand is one. Otherwise the remainder $r$ lies between one and $p-2$, so the polynomial $X^r-1$ has fewer than $p-1$ roots. Choose nonzero $t$ with $t^r\ne1$. Scaling the sum by the permutation $a\mapsto ta$ shows $S=t^rS$, forcing $S=0$. $\square$

This sieve is useful when coefficient sums follow an arithmetic progression in the exponent. The constant term is exceptional: forgetting it changes the congruence. The root-of-unity filter is over the complex numbers with division by $m$; this field sum is a congruence statement and requires its own hypotheses.

## 11.4 Digit inventories

A numeral with prescribed digit counts $(c_0,\ldots,c_9)$ and total length $n$ has

$$\frac{n!}{\prod_dc_d!}
-\mathbf1_{c_0>0}\frac{(n-1)!}{(c_0-1)!\prod_{d=1}^9c_d!}$$

valid arrangements: subtract those with initial zero. For divisibility by three or nine, only the digit sum matters. For divisibility by eleven, track the alternating-position sum. For a general modulus, positional weights are necessary.

**Example.** In 1983-A-10, four-digit numerals beginning with $1$ must have multiplicity pattern $(2,1,1)$. If the repeated digit is $1$, choose its other position and then two distinct digits from the remaining nine: $3\cdot9\cdot8=216$. If the repeated digit is different, choose it in nine ways, choose its two positions among the final three, and choose the remaining digit in eight ways: another $216$. Total $432$.

# 12. Graphs, invariants, and exact extrema

## 12.1 Incidences

**Theorem 12.1 (handshaking).** In a finite undirected graph, the sum of vertex degrees is twice the number of edges, counting a loop twice.

**Proof.** Every edge has two ends. Count incident edge-ends by vertices. $\square$

**Proposition 12.2 (capacity bound).** If every object in a family contains $q>0$ features, and each of the $M$ possible features belongs to at most $t$ objects, then the family has at most $Mt/q$ objects.

**Proof.** Count object-feature incidences in two orders. $\square$

The right feature can be a point, pair, triple, edge, or local pattern. Choosing pairs rather than points often strengthens a weak pigeonhole estimate.

## 12.2 Complete invariants

**Definition.** An invariant is a quantity unchanged by every permitted move. A necessary invariant becomes a complete reachability criterion only when every target satisfying it is reachable.

**Theorem 12.3 (edge toggles).** In a graph whose vertices carry bits, suppose a move toggles both endpoints of a chosen edge. A target is reachable from a starting configuration if and only if their bit sums agree modulo two in every connected component.

**Proof.** Each move preserves component parity. For sufficiency, choose a rooted spanning tree in each component. Process leaves toward the root. Toggle a leaf's parent edge exactly when needed to correct that leaf, then remove it. All nonroot vertices are corrected permanently. Component parity forces the final root to be correct as well. $\square$

**Trap.** A parity obstruction alone does not establish sufficiency for a different move set. Write the construction or identify the linear span of the permitted move vectors.

## 12.3 The upper-bound plus witness standard

**Proposition 12.4.** To prove that a feasible integer statistic has maximum $M$, it is sufficient and necessary to prove both: every feasible object has statistic at most $M$, and at least one feasible object has statistic $M$.

The statement is elementary; its omission is not. Equality conditions in an upper-bound proof often construct the extremizer. If the upper bound treats local constraints independently, check whether their equality conditions can hold simultaneously.

**Example.** For a graph with real labels $a_v$, the sum $\sum_{uv\in E}|a_u-a_v|$ can be studied by orienting each edge from smaller to larger label. Then the coefficient of $a_v$ is its indegree minus its outdegree. Sorting possible coefficient assignments provides an upper bound, but the orientation must still arise from one ordering of the vertex labels. A checkerboard pattern on a bipartite graph may supply the missing witness; an arbitrary degree assignment need not.

# 13. Geometric counting without a picture trap

## 13.1 Subsets as geometric objects

For $n$ points in convex position, triangles correspond to three-element subsets and diagonals to nonadjacent vertex pairs. An interior crossing of two diagonals corresponds to four vertices in cyclic order *if no three diagonals meet at the same interior point*. Without that hypothesis, $\binom n4$ counts crossing pairs with multiplicity, not distinct intersection points.

**Theorem 13.1 (regions by insertion).** Draw straight chords one at a time in a disk, or segments whose endpoints lie on the boundary of a convex polygon. If a new segment has $t$ distinct interior intersection points with the existing drawing, crosses transversely, and overlaps no existing edge, it creates $t+1$ new regions.

**Proof.** The $t$ points split it into $t+1$ open subsegments. Each lies inside one existing region and splits that region in two. Count the new regions. $\square$

The words *distinct*, *interior*, and *transversely* carry mathematical content. A triple concurrence must be counted as one cut point on a newly inserted segment, even though it meets two older segments there.

## 13.2 Lattice triangles and rectangles

Count all point subsets, then subtract degeneracies if the degeneracies have a tractable classification. For axis-aligned rectangles in an $r$ by $s$ array of points, choose two rows and two columns: $\binom r2\binom s2$. Rotated rectangles require a new representation, often a diagonal midpoint and a distance.

**Derived proposition 13.2 (equal-diagonal encoding).** A nondegenerate quadrilateral is a rectangle if and only if its two diagonals have the same midpoint and the same length.

**Proof.** A common midpoint makes the quadrilateral a parallelogram. If adjacent side vectors are $u,v$, the squared diagonal lengths differ by $|u+v|^2-|u-v|^2=4u\cdot v$. Equality is equivalent to a right angle. The converse follows by reversing the argument. $\square$

Thus one may group unordered point pairs by midpoint and squared distance, then choose two distinct pairs in a group, excluding degeneracy. This is a common way for a geometric classification to make a combinatorial enumeration short.

# 14. Combining tools and shortening proofs

## 14.1 Gaps with congruences

**Derived proposition 14.1.** Under the gap-removal bijection of Theorem 2.3,

$$\sum_{i=1}^ka_i=\sum_{i=1}^kb_i+d\binom k2.$$

**Proof.** Sum $a_i=b_i+d(i-1)$. $\square$

A spacing restriction and a sum-residue restriction can therefore be separated: first shorten the interval, then shift the target residue by the fixed amount $d\binom k2$. There is no need to track every individual gap modulo the modulus.

## 14.2 Symmetry with inventory

**Derived proposition 14.2.** If a permutation of positions has cycle lengths $\ell_1,\ldots,\ell_t$, then the number of binary colorings it fixes with exactly $k$ marked positions is

$$[x^k]\prod_{j=1}^t(1+x^{\ell_j}).$$

**Proof.** A fixed coloring must be constant on each position-cycle; a marked cycle contributes its entire length. $\square$

Insert this count into Burnside rather than counting unrestricted colorings and trying to impose the inventory afterward.

## 14.3 The exact-event sieve

**Theorem 14.3.** For events $A_1,\ldots,A_m$, let $S_r$ be the sum of sizes of all $r$-fold intersections, with $S_0=|U|$. The number of objects belonging to exactly $j$ events is

$$N_j=\sum_{r=j}^m(-1)^{r-j}\binom rj S_r.$$

**Proof.** An object in $t$ events contributes

$$\sum_{r=j}^t(-1)^{r-j}\binom rj\binom tr
=\binom tj(1-1)^{t-j},$$

which is one if $t=j$ and zero otherwise. $\square$

This avoids inventing a separate inclusion-exclusion argument for “exactly one,” “exactly two,” and so forth. For exactly one, the correct coefficients are $1,-2,3,-4,\ldots$, not $1,-1,1,-1,\ldots$.

## 14.4 Forbidden assignments and rook numbers

**Theorem 14.4.** Mark forbidden cells in an $n$ by $n$ assignment board. Let $r_k$ count placements of $k$ marked cells with no repeated row or column. The number of permutations avoiding the board is

$$\sum_{k=0}^n(-1)^kr_k(n-k)!.$$

**Proof.** Forcing $k$ compatible forbidden assignments leaves $(n-k)!$ completions. Incompatible assignments have zero completions. Apply inclusion-exclusion. $\square$

If two boards use disjoint row sets and disjoint column sets, their rook generating polynomials multiply. Merely drawing the boards in visually separate regions does not establish that independence.

## 14.5 A shortening clinic

An answer like $\sum_{j=0}^{10}\binom{10}{j}\binom{10}{10-j}$ can be left as a ten-term calculation, or recognized as $\binom{20}{10}$ by choosing ten people from two groups of ten. The latter both evaluates and explains the identity.

**Vandermonde's identity.** For nonnegative $a,b$,

$$\sum_j\binom aj\binom b{k-j}=\binom{a+b}k.$$

**Proof.** Count $k$-subsets of two disjoint groups, conditioning on the number chosen from the first. $\square$

Likewise, $\sum_{j=r}^n\binom jr=\binom{n+1}{r+1}$ follows by grouping $(r+1)$-subsets by their largest element. Before performing a sum, ask what it counts.

## 14.6 Boundary counting instead of two large enumerations

**Derived proposition 14.5.** Let $F(N)$ count positive integer solutions of $a_1x_1+\cdots+a_kx_k=N$, with positive integer coefficients. For a fixed coordinate $j$ and integer $h\ge1$,

$$F(N+a_jh)-F(N)$$

counts precisely the solutions at total $N+a_jh$ with $1\le x_j\le h$.

**Proof.** Adding $h$ to coordinate $j$ injects the solutions at total $N$ into the solutions at total $N+a_jh$. Its image is exactly the solutions with $x_j\ge h+1$, because subtracting $h$ is then a legal inverse. $\square$

**Historical use.** For 2009-II-09, shift the variable with coefficient three by three. The difference of the totals is nine. In the larger equation parity forces that variable odd, so the complement consists of only the slices $y=1$ and $y=3$. Their counts are $501$ and $499$. Two large lattice-point counts have become two short boundary counts.

**Failure condition.** The injection must preserve every other constraint. An upper bound on $x_j$, a coprimality condition, or an ordering relation between variables may break it.

## 14.7 Every intermediate subset sum exists

**Derived proposition 14.6.** The sums of $k$ distinct elements of $[n]$, for $1\le k\le n$, comprise every integer from $k(k+1)/2$ to $k(2n-k+1)/2$. There are $k(n-k)+1$ different sums.

**Proof.** The endpoints follow by taking the smallest or largest elements. For excess $t$ above the minimum, write $t=kq+r$ with $0\le r<k$. Starting from $(1,\ldots,k)$, add $q$ to all entries and one more to the last $r$. The entries remain distinct. If $r>0$, the bound $t\le k(n-k)$ gives $q\le n-k-1$, so the largest entry is at most $n$; the case $r=0$ permits $q=n-k$. $\square$

**Historical use.** For 2006-I-02, choose $90$ of the first $100$ positive integers. The number of different sums is $90\cdot10+1=901$. Merely subtracting the extreme sums would leave a gap in the proof; the construction closes it.

## 14.8 Valuation layers

**Derived proposition 14.7.** For a prime $p$ and integer $n\ge1$,

$$\sum_{m=1}^{p^n}p^{v_p(m)}=p^{n-1}\bigl(n(p-1)+p\bigr),$$

where $v_p(m)$ is the exponent of $p$ in $m$.

**Proof.** For $0\le j<n$, exactly $(p-1)p^{n-j-1}$ integers have valuation $j$. Multiplication by their contribution $p^j$ gives the same amount $(p-1)p^{n-1}$ in every such layer. The remaining integer $p^n$ contributes $p^n$. $\square$

**Historical use.** The corresponding even-integer sum in 2006-I-13 is $(n+1)2^{n-1}$. Its square condition is now a parity and square test. The useful discovery is that the exponentially different layer sizes exactly cancel the exponentially different weights.

## 14.9 Hamiltonian tours on a directed square torus

**Theorem 14.8.** On vertices $\mathbb Z_n^2$ with integer $n\ge2$, each move adds either $(1,0)$ or $(0,1)$. The number of move sequences starting at $(0,0)$, visiting every vertex once, and returning after $n^2$ moves is

$$\sum_{\substack{0\le k\le n\\\gcd(k,n)=1}}\binom nk.$$

**Proof.** A tour chooses one outgoing edge at each vertex. Write $e(x,y)=1$ for the horizontal choice and zero for the vertical choice. Exactly one incoming edge at $(x,y)$ means

$$e(x-1,y)+1-e(x,y-1)=1.$$

Therefore $e$ is constant along each diagonal $x+y$ modulo $n$. There are $n$ binary direction choices, encountered in the same order repeatedly. If $k$ are horizontal, a block of $n$ moves translates a vertex by $(k,n-k)=(k,-k)$ modulo $n$. Its order is $n/\gcd(k,n)$. A single tour covers all vertices exactly when this order is $n$. For each such $k$, choose the $k$ horizontal diagonals in $\binom nk$ ways. This argument proves necessity and sufficiency. $\square$

**Historical use.** For the two clock hands in 2023-I-14, $n=12$. The count is $\binom{12}{1}+\binom{12}{5}+\binom{12}{7}+\binom{12}{11}=1608$, with remainder $608$ modulo $1000$.

**Why the proof is short.** The incoming-edge equation converts a choice at each of $n^2$ vertices to one at each of $n$ diagonals. A global Hamiltonian condition then becomes a gcd condition. On a rectangular torus or with an additional move direction, redo the incoming-edge argument; the theorem does not automatically extend.

## 14.10 Canonical representatives for two generators

**Derived proposition 14.9.** Let $0<p<q$ be coprime integers and let $n$ be a nonnegative integer. The number of distinct integers expressible as $pa+qb$ with nonnegative integers $a,b$ and $a+b\le n$ is

$$\sum_{a=0}^{\min(q-1,n)}(n-a+1).$$

In particular, when $n\ge q-1$ it is $q(n+1)-q(q-1)/2$.

**Proof.** If $a\ge q$, replace $(a,b)$ by $(a-q,b+p)$. This preserves the integer represented, keeps the coefficients nonnegative, and decreases their total by $q-p$. Repetition gives a representative with $0\le a<q$. Two such representatives cannot have the same value: equality modulo $q$ forces their $a$ values to agree because $p$ is invertible modulo $q$, and then their $b$ values agree. Every attainable value therefore has exactly one representative in the stated range, and its total is no larger than that of the original representation. For each admissible $a$, there are $n-a+1$ choices of $b$. $\square$

**Historical use.** The offsets in 1994-A-11 are $2a+5b$ with $a+b\le94$. The distinct values number $95+94+93+92+91=465$. A long analysis of missing integers is replaced by unique representatives. If $p,q$ are not coprime, divide both by their gcd first; this does not change the number of distinct represented values.

## 14.11 A diagonal invariant discovers a Catalan recurrence

**Definition.** A rectangular cell loop consists of the boundary cells of an axis-aligned $r$ by $c$ rectangle, where $r,c\ge2$. A loop partition covers every board cell exactly once.

**Derived theorem 14.10.** A $2a$ by $2b$ board with $a>b\ge1$ has exactly $C_b$ partitions into $b$ rectangular cell loops. A $2n$ by $2n$ square has exactly $2C_n-1$ partitions into $n$ loops, where $C_n=\binom{2n}{n}/(n+1)$.

The discovery is a useful pattern: first prove that an extremal partition saturates two different bounds; then compare the equality cases inside a distinguished component.

**Diagonal lemma.** In an $H$ by $W$ board with $H\ge W$, each rectangular loop meets each of the cell sets

$$D=\{(i,i):1\le i\le W\},\qquad E=\{(H+1-i,i):1\le i\le W\}$$

in at most two cells. Following either diagonal through the bounding rectangle, only its first and last cells can be boundary cells. Consequently at least $W/2$ loops are necessary. When $W$ is even and exactly $W/2$ loops occur, each loop meets each diagonal exactly twice. $\square$

**Corner lemma.** In such a minimum partition, let the loop at the upper-left corner have dimensions $r$ by $c$. Its two intersections with $E$ imply $r+c\ge H+2$. Its strict interior contains $\min(r,c)-2$ cells of $D$ and $r+c-H-2$ cells of $E$. This interior is a union of whole loops: another connected boundary cannot pass from inside to outside without sharing a cell with the enclosing boundary. Each contained loop contributes two cells to each diagonal. Hence

$$\min(r,c)-2=r+c-H-2,\qquad\max(r,c)=H.$$

Thus on a tall board the corner loop spans the full height; on a square it spans a full side. Its other dimension is even, since its interior diagonal count is even. $\square$

**Proof of the theorem.** For $a>b$, let $T(a,b)$ count the minimum partitions, with $T(a,0)=1$. The corner loop has height $2a$ and width $2k$ for a unique $1\le k\le b$. Removing it leaves its interior, of size $2(a-1)$ by $2(k-1)$, and a right-hand remainder of size $2a$ by $2(b-k)$. Their diagonal lower bounds sum to the remaining $b-1$ loops, so both smaller boards attain their own minima. Conversely their partitions combine uniquely with the chosen corner loop. Both nonempty boards remain strictly taller than wide. Therefore

$$T(a,b)=\sum_{k=1}^bT(a-1,k-1)T(a,b-k)=\sum_{k=1}^b C_{k-1}C_{b-k}=C_b,$$

where induction on $b$ justifies the middle equality.

For squares let $S_n$ be the count and put $S_0=1$. The corner loop is either the full square boundary, a full-height proper-width rectangle, or its transpose. These three cases are disjoint and exhaustive. They give

$$S_n=S_{n-1}+2\sum_{k=1}^{n-1}C_{k-1}C_{n-k}
=S_{n-1}+2(C_n-C_{n-1}).$$

Telescoping gives $S_n=2C_n-1$. $\square$

**Historical use.** In 2026-I-15 the square is $10$ by $10$, so the answer is $2C_5-1=83$. An independent exact-cover enumeration, without the corner lemma, gives $1,3,9,27,83$ for side lengths $2,4,6,8,10$. The sequence alone is evidence; the diagonal invariant is the proof.

# 15. Exact verification and a research ledger

## 15.1 What each check establishes

An answer-key match checks the final integer against a source. It does not prove the derivation, and two copied archives are not independent mathematical witnesses. A second derivation checks more. Exhaustive enumeration checks one finite instance, provided that its generator exactly matches the definition. A proof gives a reason that transfers to all admissible parameters.

Keep these distinctions visible. In the companion collection, newly written means new exposition and reasoning after source consultation; it does not mean that the author solved the problem without seeing any published method.

## 15.2 A proof-carrying finite enumeration

Some AIME instances are best checked by a small exact program. A useful mathematical certificate contains:

1. A finite parameter set that covers every admissible object.
2. A proof of its multiplicity, preferably one-to-one.
3. Exact predicates equivalent to every original constraint.
4. An exact summation or recurrence and its evaluated result.
5. The final conversion to the requested remainder or reduced fraction.

“A computer gives 393” is not such a certificate. A six-variable enumeration over $\mathbb F_3$, with the seventh coordinate eliminated by a sum constraint, contains only $3^6$ cases; listing the exact remaining polynomial test and a short reproducible evaluator makes the computation auditable. A conceptual reduction beyond that is still valuable and should be sought for the main training solution.

## 15.3 Three dangerous shortcuts

**Using the AIME answer range as a proof.** The range $0$ through $999$ is a check on an interpretation, not a legitimate way to eliminate a mathematically feasible branch of an intermediate computation.

**Treating apparent symmetry as uniformity.** Occupancy vectors, rotation classes, and integer partitions are rarely uniform under a uniform experiment on labeled outcomes. Compute fiber sizes.

**Proving only an obstruction.** A parity invariant, capacity bound, or inequality may rule out possibilities without proving the others exist. Supply a witness or constructive algorithm.

## 15.4 Study by retrieval, then by transfer

First solve a problem without its method tags. Record the obstacle and the representation that removed it. Next prove a parameterized version before memorizing the numeric answer. Finally alter one hypothesis: use a circle instead of a line, identical objects instead of distinct objects, or exactly two events instead of at least one. If the method breaks, identify the line in the proof that used the old hypothesis.

The historical method index supplies exercises after each chapter. The original exercises below test transfer independently of recognizing an archived answer.

# 16. Original exercises

These exercises are newly written for this course. A star marks a problem requiring a combination of ideas.

1. Count six-element subsets of $[25]$ whose consecutive elements differ by at least three.
2. Count length-14 binary words with six ones and exactly three one-runs. Repeat for 14 labeled positions on a circle.
3. Count nonnegative triples totaling 12, with each coordinate at most five.
4. Count permutations of six labels with exactly two fixed points.
5. Count binary words of length eight avoiding consecutive ones in two ways.
6. Count north-east paths to $(7,4)$ staying in $y\le x$.
7. Count binary necklaces of length six under rotation. Then require exactly three marked positions.
8. A uniform four-subset of the vertices of a ten-cycle is chosen. Find the expected number of its contained cycle edges.
9. Prove the edge-toggle reachability theorem by a direct construction joining pairs of mismatched vertices with paths.
10. Find the number of positive compositions of eight whose parts are all odd.
11. Count length-eight words over three symbols using every symbol at least once.
12. Find the number of permutations of five labels satisfying $\pi^2=\mathrm{id}$.
13. Count subsets of $[10]$ with even cardinality without expanding a binomial sum.
14. Count binomial coefficients in row 2026 that are odd.
15. Count distributions of five distinct objects into three labeled boxes with no empty box; compare with five identical objects.
16. A random permutation of eight labels is chosen. Find the expected number of fixed points and the expected number of unordered pairs of fixed points.
17. Two independent uniform cuts divide a unit interval. Find the probability that every resulting piece has length at most $2/3$.
18. Count binary words with three ones and four zeros in which exactly two adjacent pairs are unequal.
19. (*) Find the number of five-element subsets of $[20]$ with no consecutive elements and even sum. Reduce to a coefficient rather than listing subsets.
20. (*) Count permutations of four labels avoiding the positions $(1,1),(1,2),(2,1),(2,2)$. Explain why treating the four forbidden cells as independent gives an incorrect sieve.

# 17. Exercise solutions

1. Subtract $2(i-1)$ from the $i$th chosen element. The answer is $\binom{15}{6}=5005$.
2. Linear: $\binom52\binom93=840$. Circular: mark one of the three one-runs, choose its first position, then choose the positive one-run and zero-run lengths. Divide by three: $\frac{14}{3}\binom52\binom72=980$.
3. Inclusion-exclusion gives $\binom{14}{2}-3\binom82+3\binom22=10$.
4. Choose the fixed points and derange the remaining four: $\binom62D_4=15\cdot9=135$.
5. The recurrence gives $a_0,\ldots,a_8=1,2,3,5,8,13,21,34,55$. Alternatively, with $k$ ones choose separated locations in $\binom{9-k}{k}$ ways and sum over $0\le k\le4$, obtaining $1+8+21+20+5=55$.
6. Reflection gives $\binom{11}{4}-\binom{11}{3}=165$.
7. Burnside gives $(64+2\cdot2+2\cdot4+8)/6=14$. With three marked positions, only the identity and the two rotations with cycles of length three contribute: $(20+2\cdot2)/6=4$.
8. The expectation is $10\binom82/\binom{10}{4}=4/3$.
9. Pair the mismatched vertices within each connected component. Toggle every edge on a path joining each pair. Internal path vertices are toggled twice and endpoints once; summing paths modulo two corrects exactly the mismatched vertices.
10. If $f_n$ counts these compositions, the first odd part gives generating function $1/(1-x-x^3-\cdots)=(1-x^2)/(1-x-x^2)$. Its coefficient at $x^8$ is $F_8=21$, where $F_1=F_2=1$. Equivalently, use $k$ odd parts with $k\equiv8\pmod2$ and sum $\binom{(8+k)/2-1}{k-1}$ for $k=2,4,6,8$, obtaining $4+10+6+1=21$.
11. Surjection counting gives $3^8-3\cdot2^8+3=5796$.
12. Only cycles of lengths one and two are possible. The count is $1+\binom52+\binom54\cdot3=26$.
13. Toggle the membership of the element 10. This pairs even and odd subsets, giving $2^9=512$ even subsets.
14. Since $2026=1024+512+256+128+64+32+8+2$ has eight one-bits, Lucas gives $2^8=256$ odd coefficients.
15. Distinct objects: $3^5-3\cdot2^5+3=150$. Identical objects: $\binom42=6$. These count different mathematical objects.
16. Eight indicators each have expectation $1/8$, so the first answer is one. A specified pair is fixed with probability $6!/8!=1/56$, giving $\binom82/56=1/2$ for the second.
17. A specified gap exceeds $2/3$ with probability $(1/3)^2$. The three events are mutually exclusive, so the answer is $1-3/9=2/3$.
18. There are three runs. A one-zero-one pattern contributes $\binom21=2$ choices for the two one-run lengths; a zero-one-zero pattern contributes $\binom31=3$. Total five.
19. Gap removal gives five-element subsets of $[16]$; the sum changes by $\binom52=10$, so parity is unchanged. In $[16]$ there are eight odd and eight even values. The count is $\sum_{j\text{ even}}\binom8j\binom8{5-j}$. The signed difference of even and odd sums is $[x^5](1-x)^8(1+x)^8=[x^5](1-x^2)^8=0$. Thus the answer is $\frac12\binom{16}{5}=2184$.
20. The rook numbers are $r_0=1,r_1=4,r_2=2$, and all higher ones vanish. Hence $4!-4\cdot3!+2\cdot2!=4$. Directly, the first two rows must use columns 3 and 4, while the last two use columns 1 and 2: $2!2!=4$.

# Further study and attribution

The contest problems are credited to the Mathematical Association of America, American Mathematics Competitions. Community solutions are credited through their individual source pages in the accompanying catalog. The original exposition in this volume uses standard results from enumerative combinatorics and elementary probability; it does not reproduce a textbook's presentation.

For a broader theoretical course, consult Richard P. Stanley's author-maintained [Enumerative Combinatorics materials](https://math.mit.edu/~rstan/ec/) and [Bijective Proof Problems](https://math.mit.edu/~rstan/bij.pdf). For a freely available proof-oriented foundation, see the authors' [Mathematics for Computer Science](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf), especially its treatments of counting, recurrences, and probability. These are further-study references, not sources for claims that the present archive has complete or independently verified coverage.

