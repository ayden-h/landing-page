---
title: "Olympiad Combinatorics"
subtitle: "Certificates, Structure, and Short Proofs"
author: "Ayden Bi"
date: "Research edition • 5 November 2026"
lang: en-US
---

\thispagestyle{empty}

# Before using this book {.unnumbered}

This is a rigorous methods manuscript and a research archive, not a claim to have finished a complete historical encyclopedia. The accompanying coverage report states exactly which records were recovered, which are only candidates, which have supplied solutions, and which worked solutions were checked and rewritten for this edition. A year range does not certify every year in the range. A source-provided solution is not an independently verified solution.

The target is deliberately large: combinatorics from ten demanding school olympiads, together with the IMO selection systems of the ten highest-ranked teams in the official 2026 results. No authoritative ranking of the world's ten hardest competitions exists. The selected contest families are IMO, Romanian Master of Mathematics, China Mathematical Olympiad, USAMO, All-Russian Mathematical Olympiad, Iranian Mathematical Olympiad, Vietnam Mathematical Olympiad, APMO, Balkan Mathematical Olympiad, and EGMO. This is an editorial selection of proof competitions, not a measured difficulty league table. Shortlists are valuable supplementary material but are not additional competitions.

The country convention selects China, United States, Russia, Singapore, Vietnam, Republic of Korea, India, Democratic People's Republic of Korea, United Kingdom, and Japan. It measures one recent year's performance, not all-time national strength. North Korean selection archives are particularly sparse; national contests and training exercises must not silently substitute for unpublished final selection tests.

The results developed here are classical mathematics or explicitly identified deductions and organizational propositions. Their arrangement, explanations, diagnostic questions, and proof comparisons form the contribution of this manuscript. No claim of research-level novelty is made. Nor is there a theorem that makes every hard olympiad problem short: choosing the right representation can itself be the difficult part.

**How to use the three components.** Attempt a problem from the collection without seeing its solution. Consult the recognition questions in the relevant chapter. Read a worked solution only after writing down your own obstruction or partial invariant. Finally, reconstruct the proof from its certificate and solve a nearby variation. The separate worked-solutions volume supplies the full arguments for the historical case studies cited as W01, W02, and so on.

**Prerequisites.** Comfort with sets, induction, elementary inequalities, modular arithmetic, and elementary graph language is assumed. Linear algebra over finite fields and basic group language are introduced when needed. The polynomial and matroid chapters are advanced enrichment; their proofs are included so that the book does not depend on unexplained machinery.

\newpage

# What a short proof actually needs

## Objects, moves, and certificates

A combinatorial problem has four ingredients: a class of configurations, a set of permitted operations or constraints, a quantity to control, and a desired conclusion. The story often conceals the first two. People and acquaintances may mean vertices and edges. A collection of subsets may mean a bipartite incidence graph or a zero-one matrix. Repeated switches may mean vector addition over a finite field.

**Definition 1.1 (certificate).** A certificate for a claim is an auxiliary object together with a short verification that it implies the claim. Examples include a matching, a deficient set in Hall's theorem, a conserved parity, a strictly decreasing integer, or weights whose sum proves an upper bound.

There are two different tasks:

1. Find the certificate.
2. Verify it.

Olympiad solutions often compress the second task beautifully while hiding the first. Training must practice both. After reading a proof, record the sentence that made the certificate visible: “choose a maximum rainbow forest,” “count separated pairs of subsets,” or “label columns in binary.”

**Definition 1.2 (obstruction).** An obstruction is a witness that a desired construction cannot exist. The most useful theorems identify *all* obstructions, rather than a few necessary conditions. Hall's theorem says exactly which obstruction prevents a matching. Linear algebra identifies every linear obstruction to a toggle configuration.

**Proposition 1.3 (two-certificate method).** To prove that an extremal value is \(M\), it is enough to give:

- a feasible construction of value \(M\);
- a certificate that every feasible construction has value at most \(M\).

The proposition is elementary; the discipline is not. A good-looking construction alone does not establish optimality. A counting bound alone does not establish attainability.

In a game, the analogous pair is a strategy forcing at least \(M\), and an opposing strategy preventing more than \(M\). These strategies must work against every legal response.

## A representation table

| Surface feature | Useful model | First certificate to seek |
|:--|:--|:--|
| Distinct assignments or representatives | Bipartite graph | Hall deficiency or augmenting path |
| Local flips and parity | Vector space over \(\mathbf F_2\) | Kernel vector of the transpose |
| Many intersections or repeated coincidences | Incidence matrix | Double count or second moment |
| Simultaneous involutions | Permutation action | Orbits and commuting generators |
| A geometric sum with powers \(x\) and \(1-x\) | Random subset | Disjoint exhaustive events |
| “For every subcollection” inequalities | Rank or submodularity | Tight subsets and contraction |
| A process that appears to improve | Directed state graph | Well-founded potential |
| Alternating placements | Conflict graph | Pairing, independent set, or strategy stealing |
| Uniquely representable sums | Digit system | Forced next place value |
| Large finite family with forbidden containment | Boolean lattice | Random chain or compression |

A model is useful only when it preserves the actual problem. In particular, allowing an operation that the original problem forbids can invalidate a proof. Before changing models, write one sentence explaining the correspondence in both directions.

## The three-line proof skeleton

For a first attempt, write:

> I will encode the configuration as ______.  
> I will find or control ______.  
> If that object exists or has the required value, then ______.

If the last line is not justified, you have an attractive reformulation rather than a proof plan.

**Failure test.** Try the smallest legal configuration, an empty boundary case, a highly symmetric example, and a configuration concentrated in one part. These often reveal a missing quantifier or an unattainable equality case before you invest an hour.

# Invariants and well-founded progress

## Linear invariants are a complete theory for unrestricted toggles

Let a state be a vector \(x\in\mathbf F_p^n\), where \(p\) is prime. Suppose move \(j\) adds a fixed vector \(v_j\). Put these vectors into the columns of an \(n\times m\) matrix \(A\).

**Theorem 2.1 (reachability and dual invariants).** If every move may be repeated without state-dependent restrictions, then a target \(y\) is reachable from \(x\) exactly when
\[
y-x\in\operatorname{im}A.
\]
Equivalently,
\[
w^{\mathsf T}(y-x)=0
\quad\hbox{for every }w\in\ker A^{\mathsf T}.
\]

**Proof.** A move sequence adds a linear combination of the columns. Conversely, every coefficient in \(\mathbf F_p\) is realized by a nonnegative number of repetitions between \(0\) and \(p-1\). For the second assertion, every vector in \(\operatorname{im}A\) is orthogonal to \(\ker A^{\mathsf T}\). Both \(\operatorname{im}A\) and its double orthogonal complement have dimension \(\operatorname{rank}A\), so they are equal. \(\square\)

The theorem gives both necessity and sufficiency. A coloring argument is often a kernel vector written as a board. Finding *one* invariant proves some targets impossible, but generally does not characterize every reachable target.

**Warning.** If a switch is legal only when its square is occupied, the theorem may give necessary conditions but no longer sufficient ones. Legal reachability is then a directed-graph problem, not merely a span calculation.

**Case study W04: APMO 2007, Problem 5.** The five-by-five “plus” toggle puzzle has five possible singleton targets: the center and the four cells \((2,2),(2,4),(4,2),(4,4)\). Two explicit parity masks eliminate all other cells; two explicit switch patterns, together with rotations, prove sufficiency. The worked solution includes both certificates and a finite-field check. This is the proper way to use computation: verify explicit finite certificates, rather than substitute a search log for a proof.

## Monotonicity must live in a well-founded order

A decreasing positive real number need not reach zero. The sequence \(1,1/2,1/3,\ldots\) is the simplest warning.

**Theorem 2.2 (termination).** A process terminates if each legal move strictly decreases a value in a well-founded ordered set. In particular, a strictly decreasing nonnegative integer potential proves termination.

**Proof.** An infinite run would induce an infinite strictly decreasing chain, contrary to well-foundedness. \(\square\)

A finite tuple of nonnegative integers with lexicographic order is also well-founded. The earlier coordinate has absolute priority: later coordinates may increase arbitrarily when an earlier one decreases.

**Proposition 2.3 (scalarizing a bounded lexicographic potential).** Suppose \(0\le a_i\le B_i\) are integers and every move decreases \((a_1,\ldots,a_r)\) lexicographically. Define \(W_r=1\) and
\[
W_i=1+\sum_{j>i}B_jW_j.
\]
Then \(\Phi=\sum_iW_ia_i\) strictly decreases.

**Proof.** At the first changed coordinate \(i\), the loss is at least \(W_i\). All possible increases in later coordinates total at most \(\sum_{j>i}B_jW_j=W_i-1\). \(\square\)

This is a precise version of “choose a sufficiently large coefficient.” Use a lexicographic potential directly when no convenient bounds exist.

## Terminal classification is a separate task

A potential proves the process ends, but says nothing by itself about whether all runs end in the same state.

**Proposition 2.4 (termination plus a separating invariant).** Suppose a process terminates. If an invariant takes different values on different terminal states, then the invariant uniquely determines the terminal state.

**Proof.** Every terminal state reached from the same initial state has the initial invariant value. Injectivity on terminal states makes these terminal states equal. \(\square\)

**Case study W01: IMO 2026, Problem 1, viewed as a mixed combinatorics problem.** For the operation
\[
(m,n)\longmapsto
\left(\gcd(m,n),\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right),
\]
the pair consisting of the product of all entries and the number of entries greater than one decreases lexicographically. For every prime \(p\), the greatest common divisor of all \(p\)-adic exponents is invariant. The first object gives termination; the second identifies the last nonunit. Confusing those two roles makes the proof longer.

## Construct potentials backwards

Start with a forbidden cycle of moves. Ask which statistic would have to return to its old value. If ordinary sums are conserved, try a convex sum such as \(\sum x_i^2\). If that fluctuates, try a lexicographic pair, a weighted sum based on distance, or the number of violations of a local rule.

For averaging operations on a finite connected graph, the maximum is nonincreasing and the minimum nondecreasing. But strict convergence to consensus requires more: every relevant edge or vertex must be updated often enough, or a stronger finite-state argument must apply. “The maximum never increases” is not a termination proof.

# Extremal choice, augmentation, and matching

## Choose an object whose failure can be repaired

A maximum object has largest possible size. A maximal object merely cannot be extended by inclusion. This distinction matters.

**Lemma 3.1 (maximal independent set).** In a finite graph, every vertex outside a maximal independent set has a neighbor in it.

**Proof.** Otherwise that vertex could be added. \(\square\)

This is a covering conclusion, not a maximum-size conclusion. A maximal independent set can be much smaller than a maximum one.

**Lemma 3.2 (uncrossing a shortest geometric matching).** Given equally many red and blue points in the plane, with no three points collinear, there is a red-blue perfect matching whose straight segments do not cross.

**Proof.** Among all red-blue bijections choose one minimizing total segment length. If \(r_1b_1\) crosses \(r_2b_2\) at \(z\), replace them by \(r_1b_2,r_2b_1\). The strict triangle inequality gives
\[
|r_1b_2|+|r_2b_1|
<
(|r_1z|+|zb_2|)+(|r_2z|+|zb_1|),
\]
which equals the previous total for the two edges. Contradiction. \(\square\)

The minimizer is a certificate. The proof never constructs it algorithmically, because finiteness already supplies existence.

## Hall's theorem, including the failure certificate

Let \(G=(L,R,E)\) be bipartite. For \(X\subseteq L\), write \(N(X)\) for all right vertices adjacent to at least one vertex of \(X\).

**Theorem 3.3 (Hall).** A matching covering all of \(L\) exists if and only if
\[
|N(X)|\ge |X|\qquad(X\subseteq L).
\]

**Proof.** Necessity is immediate: distinct matched partners of \(X\) lie in \(N(X)\).

For sufficiency, take a maximum matching \(M\). Suppose \(u\in L\) is unmatched. Explore alternating paths starting at \(u\): unmatched edges go from left to right, matched edges return from right to left. Let \(X\) and \(Y\) be the reached vertices in \(L\) and \(R\). No vertex of \(Y\) is unmatched, for then reversing matched and unmatched edges along a path would enlarge \(M\). Every neighbor of \(X\) lies in \(Y\), and every vertex of \(X\setminus\{u\}\) is the matched partner of a vertex of \(Y\). Thus \(N(X)=Y\) and \(|X|=|Y|+1\), violating Hall's inequality. \(\square\)

Notice what a failed greedy matching omitted: it needed permission to rearrange earlier choices. An alternating path is precisely that rearrangement.

**Theorem 3.4 (deficiency form).**
\[
\nu(G)=|L|-\max_{X\subseteq L}\bigl(|X|-|N(X)|\bigr),
\]
where \(\nu(G)\) is the maximum matching size.

**Proof.** Every matching leaves at least \(|X|-|N(X)|\) members of \(X\) unmatched. Conversely, let the maximum deficiency be \(d\), add \(d\) new right vertices adjacent to all of \(L\), and apply Hall. Removing the new vertices destroys at most \(d\) matching edges. \(\square\)

The empty set ensures \(d\ge0\). This theorem is often a cleaner target than perfect matching: allow a quantified defect and then prove it vanishes.

**Corollary 3.5.** Every finite \(d\)-regular bipartite graph with \(d>0\) has a perfect matching.

**Proof.** Counting edges from \(X\subseteq L\) yields \(d|X|\le d|N(X)|\). Regularity also implies \(|L|=|R|\). Apply Hall. \(\square\)

Repeating the argument after deleting a perfect matching decomposes a regular bipartite graph into perfect matchings. This solves many scheduling problems in one paragraph.

## Covers and matchings are dual certificates

**Theorem 3.6 (Kőnig).** In a bipartite graph, the minimum vertex-cover size equals the maximum matching size.

**Proof.** A cover needs at least one endpoint from every edge of a matching. For the reverse inequality, take a maximum matching and explore alternating paths from *all* unmatched vertices of \(L\). Let \(Z_L,Z_R\) be the reached sets. Then
\[
C=(L\setminus Z_L)\cup Z_R
\]
covers every edge: an uncovered edge would go from \(Z_L\) to \(R\setminus Z_R\), contradicting reachability. No unmatched vertex lies in \(C\), and exactly one endpoint of each matched edge lies in \(C\). Therefore \(|C|=|M|\). \(\square\)

A complete proof of an optimum can now consist of a matching and a cover of equal size. The construction and upper bound become the same mathematical language.

# Double counting, energy, and equality

## Count incidences before counting configurations

Let \(I\subseteq X\times Y\) be a finite relation. Then
\[
\sum_{x\in X}|I(x)|=\sum_{y\in Y}|I^{-1}(y)|.
\]
The identity is simple. The art is choosing a relation whose fibers are both understandable.

**Proposition 4.1 (weighted covering certificate).** Suppose every object \(y\in Y\) receives total weight at least one from a collection of witnesses:
\[
\sum_{x:(x,y)\in I}w_x\ge1,\qquad w_x\ge0.
\]
If witness \(x\) is incident with at most \(d_x\) objects, then
\[
|Y|\le\sum_xw_xd_x.
\]

**Proof.** Sum the first inequality over \(y\), exchange the order of summation, and use the degree bounds. \(\square\)

This includes ordinary counting, fractional covers, and many “charge each bad configuration to a local cause” arguments. The important design question is whether every bad configuration is charged at least once and whether any witness is charged too often.

## The second moment detects collisions

If nonnegative occupancies \(d_1,\ldots,d_n\) sum to \(D\), then
\[
\sum_i d_i^2\ge D^2/n.
\]
Consequently,
\[
\sum_i\binom{d_i}{2}\ge \frac{D^2}{2n}-\frac D2.
\]

The left side counts pairs sharing a container. Use the integer refinement when equality matters: for a fixed integer sum, a sum of squares is minimized when the entries differ by at most one. Replacing \((a,b)\) by \((a-1,b+1)\) decreases the sum of squares whenever \(a\ge b+2\).

**Theorem 4.2 (triangle supersaturation).** A simple graph with \(n\) vertices, \(m\) edges, and \(t\) triangles satisfies
\[
t\ge \frac{4m^2/n-mn}{3}
=\frac{4m}{3n}\left(m-\frac{n^2}{4}\right).
\]

**Proof.** For an edge \(uv\),
\[
|N(u)\cap N(v)|\ge d(u)+d(v)-n.
\]
Summing over edges counts every triangle three times, while each degree \(d(v)\) occurs \(d(v)\) times:
\[
3t\ge\sum_vd(v)^2-mn\ge(2m)^2/n-mn.
\]
\(\square\)

**Case study W03: APMO 1989, Problem 4.** Its pairs of integers are edges; its desired triples are triangles. Once translated, the theorem is the solution. An imported transcription reverses the first inequality. That sign matters even though subsequent lines use the correct direction.

## Equality is information

**Principle 4.3 (saturation analysis).** If a chain of inequalities has equal first and last terms, every intermediate inequality is an equality. Write down all equality conditions before trying another estimate.

**Case study W05: India TST 2016, Problem 5.** Assuming every unit square has at least two red sides, at most \(n^2\) red edges force every square to have exactly two red sides and every red edge to be internal. Checkerboard coloring then forces equal numbers of black and white squares. This is impossible for odd \(n\).

The first count alone does not give a contradiction. It creates a rigid situation in which parity can finish the problem.

## Count modulo a prime

When counting modulo two, a fiber of size \(2^r\) vanishes unless \(r=0\). This simple observation often replaces a complicated involution.

**Theorem 4.4 (parity of two-sided domination).** In any finite bipartite graph, the number of subsets of \(L\) that meet the neighborhood of every vertex in \(R\) has the same parity as the corresponding number of covering subsets of \(R\).

**Proof.** Count pairs \((A,B)\), with \(A\subseteq L,B\subseteq R\), such that no edge joins \(A\) to \(B\). For fixed \(A\), there are \(2^{|R\setminus N(A)|}\) choices of \(B\). Modulo two, this contributes one precisely when \(A\) covers \(R\). Count in the other order. \(\square\)

This is RMM 2012, Problem 1 (W02). The common count is the certificate. There is no need to build an explicit bijection between the two types of covering sets.

# Order, set families, and density

## Labels turn subsequences into a pigeonhole argument

**Theorem 5.1 (Erdős–Szekeres).** A sequence of \(ab+1\) distinct real numbers contains an increasing subsequence of length \(a+1\) or a decreasing subsequence of length \(b+1\).

**Proof.** Label position \(i\) by \((u_i,v_i)\), the lengths of the longest increasing and decreasing subsequences ending there. If \(i<j\), then either the value at \(i\) is smaller, giving \(u_j>u_i\), or larger, giving \(v_j>v_i\). All label pairs are distinct. If the desired subsequences did not exist, all labels would lie in \([a]\times[b]\), only \(ab\) possibilities. \(\square\)

The method generalizes: assign each object a finite signature that must differ for distinct objects. The difficult part is proving the signatures cannot coincide.

## Random chains normalize different set sizes

An antichain is a family of subsets with no distinct member containing another.

**Theorem 5.2 (LYM inequality).** For an antichain \(\mathcal A\subseteq2^{[n]}\),
\[
\sum_{A\in\mathcal A}\frac1{\binom n{|A|}}\le1.
\]

**Proof.** Choose a uniformly random permutation of \([n]\) and its chain of initial sets. A fixed \(k\)-set occurs with probability \(k!(n-k)!/n!=1/\binom nk\). A chain contains at most one member of the antichain. Take expectations. \(\square\)

**Corollary 5.3 (Sperner).**
\[
|\mathcal A|\le\binom n{\lfloor n/2\rfloor}.
\]
Equality is attained by a middle layer.

The denominators are not a trick to memorize. They compensate for how rarely a set of each size appears in a random maximal chain.

## Density can force an exact infinite structure

A sum-free set \(A\subseteq\mathbb N\) contains no \(x,y,z\in A\) with \(x+y=z\), allowing \(x=y\).

**Case study W11: USA selection material, 2013.** Suppose an increasing enumeration \(a_1<a_2<\cdots\) is sum-free and \(a_k=2k-1\) for infinitely many \(k\). Then \(a_k=2k-1\) for every \(k\).

The proof uses a *defect propagation* argument. Let \(m=a_1\). No interval of \(2m\) consecutive integers can contain \(m+1\) members of the set, because its integers can be paired at distance \(m\). Hence
\[
a_{k+m}\ge a_k+2m.
\]
A whole block of \(m\) positive defects \(a_i-(2i-1)\) would propagate forever, contradicting infinitely many exact hits. The first two blocks then force \(m=1\).

This is a useful pattern: establish a nonnegative or monotone defect, show a strict defect propagates, and use infinitely many equality cases to rule it out.

## Build large families by independent blocks

**Case study W12: IMO Shortlist 2007, C7.** For every
\[
\alpha<\delta=\frac{3-\sqrt5}{2},
\]
one can find two disjoint families \(\mathcal S,\mathcal T\subseteq2^{[n]}\), each larger than \(\alpha2^n\), such that every member of \(\mathcal S\) meets every member of \(\mathcal T\).

Partition the ground set into \(k\) blocks of size \(m\). Let \(\mathcal S\) consist of sets meeting every block. Let \(\mathcal T\) consist of sets containing a whole block but missing another block. Then
\[
\frac{|\mathcal S|}{2^{km}}=(1-2^{-m})^k,\qquad
\frac{|\mathcal T|}{2^{km}}
=1-2(1-2^{-m})^k+(1-2^{1-m})^k.
\]
Choosing \(k\) approximately \(c2^m\) gives limiting densities \(x=e^{-c}\) and \((1-x)^2\). Balance them:
\[
x=(1-x)^2,\quad x=\delta.
\]

The golden-ratio constant is not guessed from nowhere. It comes from balancing two competing family sizes. The exact integer choice and limiting argument appear in W12. This construction proves the stated lower bound; it does **not** prove that \(\delta\) is the optimal possible density.

# Symmetry as algebra

## Involutions: count the fixed points

**Theorem 6.1.** If \(\iota:X\to X\) satisfies \(\iota^2=\mathrm{id}\) on a finite set, then
\[
|X|\equiv|\operatorname{Fix}(\iota)|\pmod2.
\]

**Proof.** Every nonfixed orbit is a pair. \(\square\)

A common construction chooses the first defect of an object and toggles it. One must prove that the same defect is chosen after the toggle; otherwise the map need not be an involution.

**Theorem 6.2 (Burnside).** A finite group \(G\) acting on a finite set \(X\) has
\[
\frac1{|G|}\sum_{g\in G}|\operatorname{Fix}(g)|
\]
orbits.

**Proof.** Count pairs \((g,x)\) with \(gx=x\). On an orbit of size \(s\), each point has stabilizer size \(|G|/s\), so that orbit contributes \(|G|\). \(\square\)

This counts orbits, not objects. Dividing by the group order without accounting for fixed points is generally wrong.

## Commuting involutions create binary blocks

**Theorem 6.3.** Let \(g_1,\ldots,g_k\) be commuting involutions acting on a finite set. Every orbit of the generated group has size a power of two.

**Proof.** Every group element can be written as \(g_1^{\epsilon_1}\cdots g_k^{\epsilon_k}\), with \(\epsilon_i\in\{0,1\}\). The group is a quotient of \(\mathbf F_2^k\), hence has order a power of two. Orbit-stabilizer gives the assertion. \(\square\)

**Corollary 6.4.** If \(x,g_1x,\ldots,g_kx\) are distinct for every \(x\), every orbit has size at least \(k+1\), and therefore is divisible by the least power of two at least \(k+1\).

**Case study W08: IMO Shortlist 2006, C5.** Each round of the tournament is a fixed-point-free involution sending a player to their opponent. The rectangular compatibility rule says the involutions commute. The corollary gives the divisibility condition on \(n\); translations by nonzero vectors in \(\mathbf F_2^t\) give the construction. This reduces a long component argument to an orbit argument, provided the group terminology is already available.

## Binary coordinates can reveal the entire move group

**Case study W09: RMM 2024, Problem 1.** On a \(2^n\times2^n\) board with one bishop per column in a common row, a legal simultaneous jump of height \(h\) must have \(2h\mid2^n\). The horizontal permutation is forced: successive blocks of length \(h\) swap in pairs. Thus \(h=2^d\), and the jump toggles bit \(d\) of every zero-based column index.

All attainable column permutations are XOR translations. Ending on the opposite extreme row forces the low bit to change, leaving exactly \(2^{n-1}\) possibilities. The worked solution gives a legal path for every such translation, not just an algebraic description.

**Recognition rule.** When operations are involutions, ask whether they commute. When component sizes repeatedly double, ask whether an elementary abelian two-group is hiding in the problem. When rows of a permutation split into equal blocks, label positions by binary strings.




# Probability and canonical decomposition

## Expectations provide witnesses

**Theorem 7.1 (averaging).** A real-valued function on a finite probability space takes a value at least its expectation and a value at most its expectation.

**Proof.** If every value were strictly smaller than the expectation, their weighted average would be smaller too. The other direction is identical. \(\square\)

No independence is needed for linearity of expectation. Independence matters when multiplying probabilities, not when adding expectations.

**Corollary 7.2.** Every graph has a cut containing at least half its edges.

**Proof.** Independently place each vertex on either side with probability one half. Each edge crosses with probability one half, so the expected cut size is \(m/2\). \(\square\)

**Theorem 7.3 (Caro–Wei bound).** Every graph has an independent set of size at least
\[
\sum_v\frac1{d(v)+1}.
\]

**Proof.** Choose a random ordering of the vertices. Select a vertex when it precedes all its neighbors. Adjacent vertices cannot both be selected. A vertex is earliest in its closed neighborhood with probability \(1/(d(v)+1)\). Apply expectation. \(\square\)

This is often stronger than \(n/(\Delta+1)\), and it exploits the whole degree sequence rather than its maximum.

## Conditional expectation turns existence into a procedure

Suppose a random construction is specified by finitely many choices \(X_1,\ldots,X_s\), and a score \(F\) has expected value at least \(M\). After fixing the first \(i-1\) choices, choose \(X_i\) so that the conditional expectation does not decrease. Such a choice exists because the current conditional expectation is an average over the next choice.

At the end, every choice is fixed, and the conditional expectation is the actual score. This yields a deterministic construction of score at least \(M\), provided the conditional expectations can be computed.

**Important distinction.** An efficiently checkable certificate need not be efficiently discoverable. “There exists a choice preserving expectation” is a valid existence proof even when computing the best choice is difficult.

## A sum of complicated terms may be a partition of probability one

**Theorem 7.4 (canonical-fiber identity).** Let \(U\) be finite, and assign every subset \(T\subseteq U\) a canonical descriptor \(C(T)\). Suppose the fiber for descriptor \(c\) consists exactly of subsets containing a fixed set \(R_c\), avoiding a disjoint fixed set \(F_c\), and choosing the remaining elements freely. Then, for independent inclusion probability \(x\),
\[
\Pr(C(T)=c)=x^{|R_c|}(1-x)^{|F_c|},
\]
and
\[
\sum_c x^{|R_c|}(1-x)^{|F_c|}=1
\]
for every real \(x\).

**Proof.** The probability formula holds for \(0\le x\le1\), with free choices contributing factors \(x+(1-x)=1\). The fibers partition all subsets. Both sides are polynomials, so equality on the interval implies equality identically. \(\square\)

**Case study W07: IMO Shortlist 2006, C3.** The canonical descriptor is the convex hull of a random subset. Its vertices are required, points outside are forbidden, and interior points are free. This directly explains the exponents in the problem and gives a short proof for all real \(x\).

The theorem is an organizational formulation of a standard probability/bijection argument. It is not a new theorem of convexity, and it fails if a purported fiber has additional hidden restrictions.

## The local lemma, with its actual hypothesis

**Theorem 7.5 (symmetric Lovász local lemma).** Let \(E_1,\ldots,E_N\) be bad events. Suppose each has probability at most \(p\), and there is a dependency graph of maximum degree \(d\): each event is independent of the sigma-algebra generated by all its nonneighbors. If \(ep(d+1)\le1\), then there is positive probability that no bad event occurs.

Here is the proof mechanism in a more general form. If numbers \(0<x_i<1\) satisfy
\[
\Pr(E_i)\le x_i\prod_{j\sim i}(1-x_j),
\]
then, by induction on the number of conditioned events,
\[
\Pr\left(E_i\,\middle|\,\bigcap_{j\in S}E_j^c\right)\le x_i
\qquad(i\notin S).
\]
Split \(S\) into neighbors \(S_1\) and nonneighbors \(S_2\). Independence removes \(S_2\) from the numerator estimate, while the chain rule and the induction hypothesis bound the denominator by
\(\prod_{j\in S_1}(1-x_j)\). This proves the conditional bound. The chain rule then gives
\[
\Pr\left(\bigcap_iE_i^c\right)\ge\prod_i(1-x_i)>0.
\]

For \(d\ge1\), take \(x_i=1/(d+1)\); the inequality
\[
\frac1{d+1}\left(\frac d{d+1}\right)^d\ge\frac1{e(d+1)}
\]
gives the symmetric statement. If \(d=0\), independence and \(p<1\) suffice.

**Why the hypothesis is strong.** Pairwise independence alone is not enough. An event must be independent of every joint event generated by its nonneighbors. In olympiad applications built from independent random variables, disjoint variable supports give the required dependency graph.

# Linear algebra and polynomial certificates

## Oddtown and Eventown

Represent a subset of \([n]\) by its incidence vector in \(\mathbf F_2^n\). Dot products record intersection sizes modulo two.

**Theorem 8.1 (Oddtown).** If \(A_1,\ldots,A_m\subseteq[n]\) each have odd size and distinct pairs have even intersection, then \(m\le n\).

**Proof.** Their incidence vectors \(v_i\) satisfy \(v_i\cdot v_j=\delta_{ij}\). In any relation \(\sum c_iv_i=0\), dotting with \(v_j\) gives \(c_j=0\). Thus the vectors are linearly independent. \(\square\)

**Theorem 8.2 (Eventown).** If all sets in a distinct family have even size and every pair has even intersection, then the family has size at most \(2^{\lfloor n/2\rfloor}\).

**Proof.** Their span \(W\) satisfies \(W\subseteq W^\perp\). Since the dot product on \(\mathbf F_2^n\) is nondegenerate,
\[
\dim W+\dim W^\perp=n,
\]
so \(\dim W\le n/2\). The family consists of distinct vectors in \(W\), giving the bound. Pair the ground-set elements and take all unions of complete pairs to attain it. \(\square\)

The difference between the two problems is not superficial: in one, the Gram matrix is the identity; in the other, the span is self-orthogonal.

## The coefficient formula

Let \(F\) be a field, let \(S_i\subset F\) have size \(t_i+1\), and let \(P\in F[x_1,\ldots,x_r]\) have total degree at most \(t_1+\cdots+t_r\).

**Theorem 8.3 (coefficient formula).**
\[
[x_1^{t_1}\cdots x_r^{t_r}]P
=
\sum_{s_i\in S_i}
\frac{P(s_1,\ldots,s_r)}
{\displaystyle\prod_{i=1}^r\prod_{a\in S_i\setminus\{s_i\}}(s_i-a)}.
\]

**Proof.** Both sides are linear in \(P\), so test a monomial \(\prod x_i^{e_i}\). In one variable, Lagrange interpolation gives
\[
\sum_{s\in S_i}\frac{s^e}{\prod_{a\ne s}(s-a)}
=
\begin{cases}
0,&0\le e<t_i,\\
1,&e=t_i.
\end{cases}
\]
If \((e_i)\ne(t_i)\) while \(\sum e_i\le\sum t_i\), at least one exponent is smaller than its corresponding \(t_i\), so the product of one-variable sums is zero. For the target monomial it is one. This is exactly the coefficient on the left. \(\square\)

**Corollary 8.4 (Combinatorial Nullstellensatz, grid form).** If the coefficient on the left is nonzero, \(P\) cannot vanish on all of \(S_1\times\cdots\times S_r\).

The technique has two jobs: encode the forbidden conclusion by factors, and make one coefficient computable. If you cannot do the second job, introducing a polynomial may only complicate the problem.

## Cauchy–Davenport from one coefficient

**Theorem 8.5.** For nonempty \(A,B\subseteq\mathbf F_p\),
\[
|A+B|\ge\min(p,|A|+|B|-1).
\]

**Proof.** Put \(a=|A|,b=|B|\). If \(a+b>p\), then for every \(c\in\mathbf F_p\), the sets \(A\) and \(c-B\) intersect; thus \(A+B=\mathbf F_p\).

Otherwise, assume \(|A+B|\le a+b-2\), and extend \(A+B\) to a set \(C\subseteq\mathbf F_p\) of size \(a+b-2\). The polynomial
\[
P(x,y)=\prod_{c\in C}(x+y-c)
\]
vanishes on \(A\times B\). Its coefficient of \(x^{a-1}y^{b-1}\) is
\(\binom{a+b-2}{a-1}\), nonzero modulo \(p\) because \(a+b-2<p\). Corollary 8.4 gives a contradiction. \(\square\)

## Zero sums: a complete proof, not just a named theorem

**Theorem 8.6 (Chevalley–Warning, prime-field form).** If polynomials \(f_1,\ldots,f_s\) over \(\mathbf F_p\) satisfy
\[
\sum_j\deg f_j<N,
\]
then the number of common zeros in \(\mathbf F_p^N\) is divisible by \(p\).

**Proof.** Modulo \(p\), count zeros using
\[
Z=\sum_{x\in\mathbf F_p^N}\prod_j(1-f_j(x)^{p-1}).
\]
The summand is one exactly at common zeros, by Fermat's theorem. Every monomial in the expansion has total degree less than \(N(p-1)\). Therefore some variable has exponent less than \(p-1\). Summing its powers over \(\mathbf F_p\) gives zero: for exponent zero the sum is \(p=0\), and for an exponent strictly between zero and \(p-1\) use multiplication by a field element whose power is not one. Thus every monomial contributes zero. \(\square\)

**Theorem 8.7 (Erdős–Ginzburg–Ziv).** Among any \(2n-1\) integers, some \(n\) have sum divisible by \(n\).

**Proof for prime \(n=p\).** Work modulo \(p\), with the given integers \(a_1,\ldots,a_{2p-1}\), and use
\[
f=\sum_i x_i^{p-1},\qquad
g=\sum_i a_ix_i^{p-1}.
\]
The degree sum is \(2p-2<2p-1\). A common zero has support of size either zero or \(p\). If \(N_p\) is the number of \(p\)-subsets with zero sum, then the total number of common zeros is
\[
1+(p-1)^pN_p\equiv1-N_p\pmod p.
\]
For \(p=2\), the same congruence holds because \(1=-1\) modulo two. Hence \(N_p\equiv1\pmod p\), so \(N_p>0\).

**Product step.** Suppose the result holds for \(a\) and \(b\). Starting with \(2ab-1\) integers, repeatedly extract disjoint \(a\)-element blocks with sum divisible by \(a\), until \(2b-1\) such blocks have been obtained. Before the last extraction at least \(2a-1\) integers remain, so every extraction is justified. Divide each block sum by \(a\). Among these \(2b-1\) integers, choose \(b\) with sum divisible by \(b\). Their blocks contain \(ab\) original integers with sum divisible by \(ab\). Prime factorization completes the proof, with \(n=1\) trivial. \(\square\)

**Transfer question.** If a problem asks for a subset satisfying two simultaneous congruences, try support-indicator variables \(x_i^{p-1}\). Check the degree budget before doing anything else.

# Games: strategies, pairing, and draws

## Finite normal-play games

A finite impartial normal-play game has the same legal moves for both players; the player with no move loses. A position is a P-position if the player about to move loses against perfect play, and an N-position otherwise.

**Theorem 9.1.** In an acyclic finite game graph:

- a position is N if it has a move to a P-position;
- it is P if every move goes to an N-position.

**Proof.** Induct backward from terminal positions along a topological ordering. \(\square\)

Define the Grundy value by
\[
g(x)=\operatorname{mex}\{g(y):x\to y\},
\]
where mex is the least missing nonnegative integer.

**Theorem 9.2 (sum rule).** The Grundy value of a disjoint sum of finite impartial games is the bitwise XOR of their values.

**Proof.** Induct on the total remaining game depth. Write \(G=g_1\oplus\cdots\oplus g_s\). A move changes exactly one \(g_i\) to a value different from it, so no option has XOR \(G\). For any \(h<G\), inspect the highest bit at which \(G\) and \(h\) differ. Choose a component whose Grundy value has a one in that bit, and set
\[
g_i'=g_i\oplus G\oplus h.
\]
Then \(g_i'<g_i\), so the mex definition guarantees an option with value \(g_i'\). The resulting XOR is \(h\). Thus the mex of option values is \(G\). \(\square\)

Do not apply this theorem to games with cycles unless you first prove termination. Infinite play introduces draws and changes the theory.

## Pairing strategies need two separate checks

A pairing strategy partitions some board into pairs, then responds to a move in one member by playing in its mate.

To prove it works, establish:

1. The responding move is always available and legal.
2. A losing pattern cannot appear even immediately after the opponent's move.

The second check is easy to miss.

**Case study W10: RMM 2018, Problem 3.** Pair grid edges into corners on the two sides of a vertical line. Ann orients the mate so both arrows enter, or both leave, the common corner. Every possible directed cycle would use an extreme corner of this type. The first edge of an unplayed pair cannot complete a cycle using both edges; the second edge is oriented by Ann incompatibly. Thus Bob cannot create a directed cycle, including on his own turns.

## Packing games need a lower and an upper strategy

**Case study W16: IMO Shortlist 2018, C2.** Horst places nonattacking black knights and Queenie occupies squares with white queens. Horst can guarantee 100 knights on a \(20\times20\) board by using one checkerboard color. Queenie can prevent 101 by partitioning the knight graph into one hundred four-cycles and always occupying the vertex opposite Horst's latest move.

The queen's movement rules are irrelevant: in this game it is an occupying piece. Translating the rules literally prevents importing a restriction from ordinary chess that the problem never imposed.

## A valuation game with genuine draws

**Case study W23: Balkan MO 2018, Problem 3.** A move takes half of an even pile and adds it to the other pile. The total number of coins stays fixed, so the state space is finite, but the game need not terminate. For instance, \((1,2)\) and \((2,1)\) repeat forever.

If the pile valuations are equal to \(k\), every move lowers both valuations to \(k-1\); exactly \(k\) moves remain. If the valuations are unequal, with minimum \(k\), halving the lower-valuation pile, when legal, creates equal valuations \(k-1\). Halving the other pile keeps the valuations unequal with the same minimum.

Therefore equal even valuations are losing positions; unequal odd minimum gives an immediate move to a losing position; unequal even minimum allows both players to avoid losing indefinitely. The full proof in W23 explicitly accounts for draws. A finite state space is not the same as a finite game.

# Induction that remembers the boundary

## Why a stronger induction hypothesis can be easier

Removing an object may destroy the original symmetry. A proof that remembers the boundary data can survive removal.

For example, counting domino tilings of a strip needs to know which cells at the cut are already covered by tiles crossing the cut. Recording only the strip length discards necessary information.

**Theorem 10.1 (finite-interface recurrence).** Suppose objects are built in layers, and every partial object has one of finitely many interface states. Suppose legal continuations depend only on that state. If \(M_{ij}\) counts one-layer transitions from state \(i\) to state \(j\), then the vector of counts after \(t\) layers is
\[
v_t=v_0M^t.
\]
The generating function for any fixed terminal condition is rational.

**Proof.** Partition extensions by their previous interface state to obtain \(v_{t+1}=v_tM\). Formally,
\[
\sum_{t\ge0}v_tz^t=v_0(I-zM)^{-1},
\]
and the inverse has rational-function entries by the adjugate formula. \(\square\)

The theorem is useful only after proving that the interface is sufficient. If two partial objects have the same recorded state but different legal continuations, the state description is incomplete.

## Unique representations force a digit system

Suppose a multiset contains distinct values
\[
1=w_1<w_2<\cdots<w_s
\]
with multiplicities \(c_1,\ldots,c_s\ge1\). A subsum records how many copies of each value are used, so identical copies are indistinguishable.

**Theorem 10.2 (complete unique subsums).** Every integer from zero to the total sum is represented exactly once if and only if
\[
w_1=1,\qquad
w_{j+1}=1+\sum_{i\le j}c_iw_i.
\]
Equivalently, with \(d_i=c_i+1\),
\[
w_j=d_1\cdots d_{j-1},\qquad
1+\sum_i c_iw_i=d_1\cdots d_s.
\]

**Proof.** For necessity, suppose the smaller values represent every integer from zero to \(S\) uniquely. If the next value is at most \(S\), it duplicates an existing representation; if it exceeds \(S+1\), the integer \(S+1\) is missing. Thus it equals \(S+1\). Its \(0,\ldots,c\) copies produce adjacent disjoint intervals
\[
[0,S],\ [S+1,2S+1],\ldots,[c(S+1),(c+1)(S+1)-1].
\]
This also proves sufficiency inductively and yields the product identities. \(\square\)

**Case study W20: India TST 2013, Problem 3.** Requiring all values \(w_j\) to be odd means all radices except possibly the last are odd. Since \(9999+1=2^4\cdot5^4\), the earlier radices are positive powers of five, whose ordered exponents have total at most four. There are \(1+\sum_{t=1}^4 2^{t-1}=16\) possibilities.

The crucial convention is that equal copies are indistinguishable. If subsums were distinguished by index sets, repeated values would immediately violate uniqueness.

## Path sums can exhaust a global budget

**Case study W15: IMO 2018, Problem 3 / Shortlist C4.** In an anti-Pascal pyramid, follow the larger child at each step. The values encountered accumulate a sum of one new positive entry per row. If the pyramid contains each integer from \(1\) to \(n(n+1)/2\) exactly once, that path exhausts the smallest possible sum of \(n\) distinct positive integers. Its contributions must therefore be exactly \(1,\ldots,n\).

A large subtriangle avoiding that path then has its own accumulation path, but all its contributions exceed \(n\). This exceeds the available largest number for \(n\ge15\), in particular for \(n=2018\). The complete argument identifies the disjoint region carefully.

The pattern is worth remembering: a first extremal path consumes all small resources; a disjoint second path becomes too expensive.

# Rank, contraction, and colored structures

## Matroids: the useful minimum

**Definition 11.1.** A matroid on a finite ground set \(E\) is a nonempty family of independent subsets closed under taking subsets, with the augmentation property: if independent \(I,J\) satisfy \(|I|<|J|\), some \(e\in J\setminus I\) makes \(I\cup\{e\}\) independent. The rank \(r(S)\) is the largest size of an independent subset of \(S\).

Examples:

- linear independence of vectors;
- forests in a graph;
- subsets containing at most one element from each part of a partition.

For the graphic matroid on a graph with \(v\) vertices,
\[
r(F)=v-c(F),
\]
where isolated vertices count as components.

Rank is monotone and submodular:
\[
r(A)+r(B)\ge r(A\cup B)+r(A\cap B).
\]
One proof extends a basis of \(A\cap B\) to a basis of \(A\), and then to a basis of \(A\cup B\); the newly added elements may be taken from \(B\setminus A\), and together with the first basis are independent inside \(B\). The displayed inequality follows by counting their sizes.

If \(D\) is independent, contraction by \(D\) has rank
\[
r_D(S)=r(S\cup D)-|D|.
\]
It represents what independence remains after committing to \(D\). Deleting \(D\) from independent sets containing it verifies the matroid axioms; equivalently, this rank formula gives the same matroid.

## Hall's theorem with independence in place of distinctness

**Theorem 11.2 (Rado's independent-transversal theorem).** For subsets \(A_1,\ldots,A_s\) of a matroid, one can select distinct representatives \(a_i\in A_i\) whose set is independent if and only if
\[
r\left(\bigcup_{i\in I}A_i\right)\ge |I|
\qquad(I\subseteq[s]).
\]

**Proof.** Necessity is immediate. Prove sufficiency by induction on \(s\), with the one-set case clear.

Suppose some nonempty proper \(J\subset[s]\) is tight:
\[
r(U_J)=|J|,\qquad U_J=\bigcup_{j\in J}A_j.
\]
Induction gives an independent transversal \(D\) for \(J\), a basis of \(U_J\). Contract \(D\). For any \(I\subseteq[s]\setminus J\),
\[
r_D(U_I)=r(U_I\cup U_J)-|J|\ge |I|.
\]
Here adding \(U_J\) or its basis \(D\) has the same rank. Apply induction to the remaining sets in the contraction and combine the representatives.

Otherwise every nonempty proper \(I\) has rank at least \(|I|+1\). Choose a nonloop \(a_s\in A_s\) and contract it. For every nonempty \(I\subseteq[s-1]\),
\[
r_{\{a_s\}}(U_I)\ge r(U_I)-1\ge |I|.
\]
Induction completes the transversal. \(\square\)

This proof illustrates a central method: a tight subsystem is solved and contracted; absence of tightness creates enough slack to make an arbitrary first choice.

## Colored spanning trees with prescribed quotas

**Theorem 11.3 (color-quota criterion).** Partition a matroid's ground set into color classes \(E_1,\ldots,E_q\), and prescribe nonnegative integer quotas \(b_1,\ldots,b_q\). An independent set with exactly \(b_i\) elements of color \(i\) exists if and only if
\[
r\left(\bigcup_{i\in J}E_i\right)\ge\sum_{i\in J}b_i
\qquad(J\subseteq[q]).
\]

**Proof.** Necessity is clear. For sufficiency, make \(b_i\) copies of the set \(E_i\) and apply Theorem 11.2. For a subcollection of these copies, its union uses some set \(J\) of colors, and the number of copies is at most \(\sum_{i\in J}b_i\). \(\square\)

For a connected graph, quotas summing to \(v-1\) yield a spanning tree.

**Case study W17: RMM 2023, Problem 6.** There are three colors and quotas \(r,g,b\) summing to \(v-1\). A tree realizing the red quota supplies \(r\) independent red edges; a tree realizing the blue quota supplies \(r+g\) independent nonblue edges. These are precisely the singleton and two-color inequalities. The three-color inequality is connectivity. The theorem gives a tree realizing all three quotas simultaneously.

**Why three matters.** With four colors, single-color feasibility does not control every two-color rank inequality. An explicit six-vertex counterexample appears in the exercises. Do not extend the three-color theorem by analogy alone.

## A rainbow odd cycle without heavy machinery

**Theorem 11.4.** If an \(n\)-vertex graph has \(n\) edge colors, each color containing an odd cycle, then it has an odd cycle whose edges have pairwise distinct colors. Parallel edges cause no difficulty.

**Proof.** Choose a maximum forest with distinct edge colors. It uses at most \(n-1\) colors, so some color is absent. Every edge of that color joins vertices in a single forest component; otherwise it could be added. Thus an odd cycle of that color lies in one component. Bipartition the tree component. Some edge of the odd cycle has endpoints in the same part. Adding it to the tree path between its endpoints produces an odd rainbow cycle. \(\square\)

This is the graph form of RMM 2020, Problem 3 (W06). It is shorter than deploying a general matroid theorem. Advanced preparation includes knowing when elementary machinery already suffices.




# From one hard problem to a reusable theorem

This chapter develops two general statements from concrete solution mechanisms. They are mathematical deductions with complete proofs. They are not claims that the statements are new to the research literature.

## Exact sparse preservation in doubly stochastic matrices

A matrix is doubly stochastic if its entries are nonnegative and every row and column sums to one.

**Definition 12.1.** For \(n\le B\le2n-1\), let \(\Lambda(n,B)\) be the largest number such that every \(n\times n\) doubly stochastic matrix has a choice of at most \(B\) entries whose retained sum in each row and each column is at least that number.

**Theorem 12.2 (exact preservation threshold).** Put \(d=B-n+1\). Then
\[
\boxed{\displaystyle
\Lambda(n,B)=\frac{d}{\left\lfloor (n+d)^2/4\right\rfloor}.}
\]

The contest instance W18 has \(n=100,B=150\), so \(d=51\), the denominator is \(75\cdot76=5700\), and the answer is \(17/1900\).

**Proof of the guarantee.** Let
\[
s=2n-B=n-d+1,\qquad
\tau=\frac{d}{\lfloor(n+d)^2/4\rfloor}.
\]
Join a row to a column when their entry is at least \(\tau\). We claim this bipartite graph has a matching of size \(s\).

Otherwise the deficiency form of Hall gives \(k\) rows whose neighbors occupy at most \(k-d\) columns. Necessarily \(d\le k\le n\). Enlarge the neighboring column set, if necessary, to exactly \(k-d\) columns. The mass in these rows is \(k\), and those columns can contain at most \(k-d\) of that mass. Hence the remaining rectangle, of size
\[
k\times(n-k+d),
\]
has mass at least \(d\). But every entry in it is strictly smaller than \(\tau\), so its mass is less than
\[
\tau k(n+d-k)\le\tau\left\lfloor(n+d)^2/4\right\rfloor=d.
\]
Contradiction.

Keep the \(s\) matched entries. For each unmatched row keep a largest entry, and do the same for each unmatched column. At most
\[
s+(n-s)+(n-s)=B
\]
entries are kept. Every unmatched row or column receives at least \(1/n\), which is at least \(\tau\), because
\(\lfloor(n+d)^2/4\rfloor\ge nd\). Every matched one receives at least \(\tau\).

**Proof of sharpness.** Choose an integer \(k\in[d,n]\) maximizing \(k(n+d-k)\), so the maximum is \(\lfloor(n+d)^2/4\rfloor\). Put \(\ell=k-d\) and \(q=n-\ell=n-k+d\). Partition the rows into \(k\) and \(n-k\), and the columns into \(\ell\) and \(q\). Use the block matrix
\[
M=
\begin{pmatrix}
1/k&d/(kq)\\
0&1/q
\end{pmatrix},
\]
where each displayed number fills the entire corresponding block. Empty blocks are allowed. Direct row and column sums show that \(M\) is doubly stochastic.

There are \(k+q=n+d=B+1\) critical lines: the top \(k\) rows and the rightmost \(q\) columns. Suppose all retained line sums exceed \(\tau=d/(kq)\). If \(a\) entries are retained in the upper-left block and \(e\) in the lower-right block, at least \(B+1-a-e\) critical lines contain no such retained entry. Each of these lines needs at least two retained entries from the upper-right block. Each upper-right entry belongs to two critical lines, so at least \(B+1-a-e\) such entries are needed. In total at least \(B+1\) entries must be retained. This contradicts the budget \(B\). \(\square\)

**What made the generalization possible?** The original constants become three structural parameters: matching size, Hall deficiency, and the maximum area of a rectangle with a fixed sum of side lengths. The extremal construction is the deficient rectangle made uniform.

This suggests a disciplined way to generalize a solution: replace its constants by variables, preserve every inequality, and then build a configuration saturating the strongest one.

## Private witnesses and bounded-loss contraction

Call a family \(\mathcal F\) of proper nonempty subsets of an \(n\)-element set *admissible* if every nonempty subfamily whose union is proper has an element occurring in exactly one member.

**Theorem 12.3 (private-witness family bound).**
\[
|\mathcal F|\le2n-2,
\]
and equality is possible.

This is RMM 2017, Problem 3, expressed without the negative term “tight.” Its proof becomes shorter after identifying nearly identical columns in the incidence matrix.

**Proof.** Induct on \(n\), with \(n=1\) trivial. If the family is empty, there is nothing to prove. Choose an element \(x\) omitted by as many members as possible, and write
\[
\mathcal F_x=\{A\in\mathcal F:x\notin A\}.
\]
This subfamily is nonempty because every member is proper. Its union omits \(x\), so some \(y\ne x\) occurs in exactly one member \(D\) of \(\mathcal F_x\). Hence
\[
\mathcal F_x\setminus\{D\}\subseteq\mathcal F_y.
\]
Maximality of \(|\mathcal F_x|\) implies
\[
|\mathcal F_y\setminus\mathcal F_x|\le1.
\]

Remove \(D\) and, if present, the one member of \(\mathcal F_y\setminus\mathcal F_x\). In every remaining set, \(x\) and \(y\) now have identical membership. Contract them to one element. Distinct sets remain distinct and proper, and admissibility is preserved: a forbidden subfamily in the quotient would lift to one in the original family. Induction bounds the remaining family by \(2(n-1)-2\). At most two sets were removed, proving the bound.

For equality, take every proper nonempty initial segment and every proper nonempty final segment of a fixed ordering. There are \(2n-2\) such sets. In a subfamily whose union misses \(m\), every chosen initial segment ends before \(m\) and every chosen final segment starts after \(m\). If any initial segment is chosen, the endpoint of the largest one is private. Otherwise, the starting point of the largest chosen final segment is private. \(\square\)

**Proposition 12.4 (bounded-loss contraction scheme).** Suppose a class of set families is preserved by a contraction that identifies two ground-set elements after removing at most \(c\) members. If every nontrivial family admits such a contraction and the largest family on one element has size \(b\), then every family on \(n\) elements has size at most \(b+c(n-1)\).

**Proof.** Iterate the contraction \(n-1\) times, charging at most \(c\) deleted members to each step. \(\square\)

This proposition does not locate the contractible pair. In Theorem 12.3, the maximum-omission choice and the private witness do that work. Keeping this distinction explicit prevents a general framework from pretending to solve its own difficult hypothesis.

## A theory of useful proof compression

Three forms of compression recur in the reviewed solutions.

**Representation compression.** Replace many case distinctions by coordinates adapted to the moves. Examples: binary labels for bishops; incidence vectors for parity; digits for unique subsums.

**Certificate compression.** Replace a long process by an object whose existence forces the answer. Examples: a maximum rainbow forest, a Hall-deficient rectangle, or a minimum-length matching.

**Equality compression.** Use a rough bound until it is forced to be sharp, then classify equality. Examples: the odd grid, the anti-Pascal path, and the balanced-tree grid.

These are diagnostic categories, not mutually exclusive domains. A solution can use all three. The useful question is not “which chapter does the problem belong to?” but “which representation makes a small certificate possible?”

| Historical case | Hard step | Reusable statement |
|:--|:--|:--|
| RMM 2012/1 | Find the common count | Parity of separated subset pairs |
| APMO 1989/4 | Translate pairs into edges | Triangle supersaturation |
| India TST 2016/5 | Read all equality cases | Saturation followed by checkerboard parity |
| IMO SL 2006 C3 | Identify a canonical descriptor | Canonical-fiber probability identity |
| IMO SL 2006 C5 | Recognize commutation | Power-of-two orbit theorem |
| RMM 2024/1 | Classify one legal jump | Global XOR translations |
| RMM 2020/3 | Choose the right extremal object | Maximum rainbow forest |
| China TST 2023 matrix problem | Expose the deficient rectangle | Exact sparse preservation threshold |
| RMM 2017/3 | Find almost equal incidence columns | Bounded-loss contraction |
| India TST 2013 odd partitions | Make the uniqueness convention precise | Mixed-radix characterization |
| RMM 2023/6 | Check every color-subset obstruction | Rado's theorem with quotas |
| Balkan MO 2018/3 | Notice infinite play | Valuation classes with draws |

The archive is much larger than this reviewed case set. This table is based on the reviewed cases, not a claim to have read and verified every imported solution.

# Training that transfers to unfamiliar problems

## A four-stage session

Spend the first ten minutes identifying the model, the quantifiers, and small cases. Then work for a sustained interval without a solution. A productive unsuccessful attempt should leave a concrete artifact: a failed invariant, a candidate extremizer, a counterexample to a stronger claim, or a precise obstruction.

If stuck, reveal a structural hint rather than the whole proof. For instance: “use a maximum rainbow forest” gives the representation, but leaves the parity argument to discover.

After reading, close the solution and reconstruct it. Finally alter a hypothesis. Replace three colors by four, a prime by a composite, a finite game by a cyclic one, or indistinguishable copies by distinguishable copies. A theorem is understood when its failure boundary is understood.

## Suggested sixteen-week route

| Weeks | Focus | Reviewed cases |
|:--|:--|:--|
| 1–2 | Invariants, potentials, exact move rules | W01, W04, W22 |
| 3–4 | Double counting and equality | W02, W03, W05, W13, W14 |
| 5–6 | Matching, deficiency, sharp examples | W18, W19 |
| 7–8 | Symmetry, binary actions, finite games | W08, W09, W16, W23 |
| 9–10 | Probability, density, canonical decomposition | W07, W11, W12 |
| 11–12 | Boundary induction and unique representations | W15, W20, W24, W26 |
| 13–14 | Rank, contraction, colored graphs | W06, W17, W25 |
| 15–16 | Mixed timed papers and proof repair | W10, W21, plus unseen archive problems |

This is a reading sequence, not an assurance of mastery in sixteen weeks. Repeat a block if you can reproduce the solutions but cannot recognize the method in a new problem.

## A self-grading rubric

Give separate marks for correctness and insight. A brilliant idea with an unproved implication is incomplete; a correct long proof is still a proof.

- **Model:** Does the translation preserve every legal configuration and move?
- **Certificate:** Is the proposed invariant, matching, rank inequality, or weight assignment actually valid?
- **Quantifiers:** Does the argument work for every required configuration or opposing strategy?
- **Boundary cases:** Are zero, one, empty families, equal elements, and degenerate cases addressed?
- **Sharpness:** Does a construction attain the stated bound?
- **Termination:** If the argument iterates, why must it stop?
- **Attribution:** Is the statement the actual contest problem, a generalization, or an original exercise?

A useful error log records the first invalid sentence, not just “I used the wrong method.”

# Twenty transfer exercises

These are practice exercises and classical consequences, not additional historical contest attributions. Solutions follow, so attempt them before continuing.

1. A graph is \(d\)-regular and bipartite. Partition its edges into \(d\) matchings.
2. In a balanced bipartite graph with \(n\) vertices on each side and minimum degree at least \(n/2\), prove a perfect matching exists.
3. Among \(n+1\) distinct integers from \(\{1,\ldots,2n\}\), show that one divides another.
4. A matrix has entries \(+1,-1\). By flipping whole rows and columns, make every row sum and column sum nonnegative.
5. Characterize the binary \(m\times n\) boards obtainable from the zero board by toggling whole rows and columns.
6. A bipartite graph has \(n\) vertices on each side and no four-cycle. Bound its number of edges by \(n(1+\sqrt{4n-3})/2\).
7. Prove every red-blue coloring of the edges of \(K_6\) has a monochromatic triangle. Show that \(K_5\) need not.
8. A finite set of positive integers has \(N\) members. Prove it has a sum-free subset of size at least \(N/3\).
9. An \(r\)-uniform hypergraph has fewer than \(2^{r-1}\) edges. Show its vertices can be colored with two colors so that no edge is monochromatic.
10. Improve the preceding existence result when every edge intersects at most \(D\) other edges, using the local lemma.
11. Count domino tilings of a \(2\times n\) rectangle, including \(n=0\).
12. In a finite family of nonempty subsets of \([n]\), suppose every nonempty subfamily has an element in exactly one member. Prove the family has at most \(n\) members.
13. Show why Cauchy–Davenport fails in \(\mathbb Z/4\mathbb Z\).
14. For a graph, find a bipartition such that every vertex has at least half its neighbors on the opposite side.
15. Prove that equally many red and blue points in general position admit a crossing-free red-blue straight-line matching.
16. On left vertices \(1,\ldots,5\), let neighborhoods be \(\{1,2\},\{1,2\},\{1,2\},\{3,4\},\{4,5\}\). Find a maximum matching and an equal-size vertex cover.
17. For a matroid with two color classes and rank \(r\), show that a basis with exactly \(k\) elements of the first color exists whenever the two color ranks are at least \(k\) and \(r-k\).
18. Construct a four-color connected simple graph and quotas summing to \(v-1\) such that each individual quota occurs in a spanning tree, but the quotas cannot occur simultaneously.
19. For \(n=5,B=7\), compute the exact sparse-preservation threshold and write the sharp block matrix.
20. Determine the number of complete uniquely representable odd-part partitions of \(2^a5^b-1\), for \(a\ge1,b\ge0\), with identical copies indistinguishable.

# Solutions to the transfer exercises

**1.** Hall gives a perfect matching. Delete it; the remainder is \((d-1)\)-regular. Induct, with \(d=0\) trivial.

**2.** If \(0<|X|\le n/2\), any one vertex of \(X\) already has at least \(n/2\) neighbors. If \(|X|>n/2\) and some right vertex has no neighbor in \(X\), its degree is at most \(n-|X|<n/2\), impossible. Thus Hall holds.

**3.** Write each integer as \(2^tu\) with \(u\) odd. There are only \(n\) possible odd parts in \([2n]\). Two selected numbers have the same odd part, and the smaller power of two divides the larger.

**4.** Among all row-column flips choose a matrix with maximum total sum. A negative row or column could be flipped to increase that sum, a contradiction. This is an existence proof using a finite maximum.

**5.** The characterization is that every \(2\times2\) subrectangle has even sum modulo two. Necessity is preserved by every flip. For sufficiency, set the row-flip bits to the first-column entries and the column-flip bits to the first-row entries minus the top-left entry, all modulo two. The rectangle condition says that the resulting entry at every position is the desired one.

**6.** No two left vertices have two common right neighbors. Hence \(\sum_{v\in R}\binom{d(v)}2\le\binom n2\). With \(m=\sum d(v)\), Cauchy gives \(m^2/n-m\le n(n-1)\). Solve the quadratic inequality for \(m\).

**7.** Some vertex has three neighbors joined to it in one color, say red. Either there is a red edge among them, or all three edges between them are blue. For the lower example, color a five-cycle red and its complementary five-cycle blue.

**8.** Choose \(t\) uniformly from \([0,1)\) and select the integers \(a\) with \(\{at\}\in(1/3,2/3)\). Every integer is selected with probability \(1/3\). Two numbers in that interval have sum modulo one outside the interval, so the selected integers are sum-free. Averaging supplies at least \(N/3\) of them.

**9.** Color vertices independently. Each edge is monochromatic with probability \(2^{1-r}\). The expected number of monochromatic edges is less than one, so some coloring has none.

**10.** Use a bad event for each monochromatic edge. Events for disjoint edges involve disjoint random variables. Thus the local lemma applies when \(e(D+1)2^{1-r}\le1\).

**11.** Let \(f_0=1,f_1=1\). The leftmost column is covered either by one vertical domino or by two horizontal dominoes, so \(f_n=f_{n-1}+f_{n-2}\). Therefore \(f_n\) is the \((n+1)\)-st Fibonacci number with \(F_1=F_2=1\). The empty board has one tiling, not zero.

**12.** Incidence vectors are linearly independent over any field. In a nontrivial linear relation, consider the subfamily with nonzero coefficients; its private element makes the corresponding coordinate of the relation nonzero. Thus there are at most \(n\) vectors.

**13.** Take \(A=B=\{0,2\}\). Then \(A+B=\{0,2\}\), of size two rather than at least three. The field assumption is essential.

**14.** Maximize the number of crossing edges. Moving a vertex to the other side changes that number by its same-side degree minus its opposite-side degree. This change cannot be positive.

**15.** Choose a minimum-total-length red-blue perfect matching and uncross any pair of crossing segments, as in Lemma 3.2.

**16.** A matching is \(1\!-\!1,2\!-\!2,4\!-\!3,5\!-\!4\). A cover consists of right vertices \(1,2\) and left vertices \(4,5\). Both have size four, so both are optimal.

**17.** Apply Theorem 11.3. The only nontrivial color-subset conditions are the two assumed rank bounds and total rank \(r\).

**18.** Use vertices \(1,\ldots,6\). Color \(12,23\) red and \(13\) blue. On vertices \(3,4,5,6\), color \(34,45,56\) green and \(35,36,46\) yellow. The quotas are red \(2\), blue \(1\), green \(1\), yellow \(1\). Each quota is individually feasible: choose a tree in the first triangle and a tree in the second \(K_4\), adjusting the latter's colors as needed. Explicit trees for green one and yellow one use respectively \(\{34,35,36\}\) and \(\{34,45,36\}\) in the \(K_4\). But three red-or-blue edges would be the entire triangle, a cycle. Thus the joint quotas are impossible.

**19.** Here \(d=3\), so \(\Lambda=3/16\). Take \(k=4,\ell=1,q=4\). The first four rows have \(1/4\) in the first column and \(3/16\) elsewhere. The last row has zero in the first column and \(1/4\) elsewhere. Every row and column sums to one. Theorem 12.2 proves sharpness at seven retained entries.

**20.** The answer is \(2^b\). Earlier odd radices must be powers of five with positive exponents. If their exponent sum is \(t\), there is one choice for \(t=0\) and \(2^{t-1}\) ordered compositions for \(t\ge1\). The last radix is \(2^a5^{b-t}\), always at least two. Summing for \(0\le t\le b\) gives \(2^b\).

# Source notes and verification boundary {.unnumbered}

The case studies use public contest material and MathNet's source-attributed records. Original problem authors, organizations, and source solution authors remain credited in the accompanying records where available. Source solutions are not presented as newly invented work. Rewritten proofs use the mathematical ideas with new exposition; some proofs deliberately replace longer source approaches.

The mathematical checks performed for this edition include exhaustive finite-field reachability for the five-by-five toggle puzzle, explicit knight-cycle verification, small-board bishop reachability, retrograde analysis of the coin game, and exact arithmetic on the sharp stochastic-matrix constructions. These checks support the corresponding finite claims. They do not establish historical completeness, and they do not constitute machine-checked formal proofs of the general theorems.

The supplied archive is a research aid. Known extraction defects are listed in its errata. Unchecked text remains unchecked even when its source is prestigious.

Selected primary references:

- International Mathematical Olympiad: [official problem archive](https://www.imo-official.org/problems/) and [2026 team results](https://www.imo-official.org/results/team/year/2026/).
- Romanian Master of Mathematics: [official 2024 problems](https://rmms.lbi.ro/rmm2024/index.php?id=problems_math); yearly organizer sites are linked from the [UK team archive](https://bmos.ukmt.org.uk/home/rmm.shtml).
- APMO: [official problems and solutions](https://www.apmo-official.org/problems).
- EGMO: [official competition archive](https://www.egmo.org/).
- USA selection tests: [public TST archive](https://github.com/usa-tst-public/USA-TST-Archive).
- UK selection tests: [BMOS/BMOC archive](https://bmos.ukmt.org.uk/home/selection-tests.shtml).
- Shaden Alshammari, Kevin Wen, Abrar Zainal, Mark Hamilton, Navid Safaei, Sultan Albarakati, William T. Freeman, and Antonio Torralba. *MathNet: A Global Multimodal Benchmark for Mathematical Reasoning and Retrieval*, ICLR 2026. [Project and attribution](https://mathnet.mit.edu/); [dataset and license](https://huggingface.co/datasets/ShadenA/MathNet).
- Noga Alon. *Combinatorial Nullstellensatz*, Combinatorics, Probability and Computing 8 (1999), 7–29. [Publisher record](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/combinatorial-nullstellensatz/E32C7ED059D6B92C6C67E18CC716872A).
- Richard Rado. *A Theorem on Independence Relations*, Quarterly Journal of Mathematics, os-13 (1942), 83–89. [Original publication](https://doi.org/10.1093/qmath/os-13.1.83).
- Mathlib authors. [Formal treatment of Erdős–Ginzburg–Ziv](https://leanprover.github.io/hex/docs/Mathlib/Combinatorics/Additive/ErdosGinzburgZiv.html). This manuscript's proof is an informal exposition, not a claim to have run that formal development.

The historical audit is dated 5 November 2026. The century-wide collection and independent solution audit remain incomplete; consult the coverage report for the exact missing work rather than inferring completion from the size of the files.

