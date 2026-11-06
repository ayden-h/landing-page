---
title: "Olympiad Combinatorics: Worked Solutions"
subtitle: "26 historical case studies with proof certificates and transfer notes"
author: "Prepared for haohao"
date: "Research edition • 5 November 2026"
lang: en-US
---

# What has been checked {.unnumbered}

This volume contains 26 mathematical restatements and rewritten solutions. Each proof was examined for its logical steps; selected finite claims were also checked computationally. This is not external peer review or formal verification. The much larger accompanying archive contains source-supplied solutions that have **not** received this review. These categories must not be conflated.

Statements below are mathematical restatements, not photographic reproductions of contest papers. The source ledger gives the original record, attribution and available author credit. “Shortlist” means supplementary proposed problems, not necessarily a problem appearing on the six-question IMO paper. National selection rounds are identified only as precisely as the recovered source permits. KMO is national selection-pipeline material, not claimed to be a final team-selection test.

The theory book proves the general tools used here. Every case includes a hint, a complete argument or an explicitly cited theorem from that book, and a transfer lesson. Solutions draw on the mathematical ideas in attributed public source solutions; the exposition does not claim those ideas as new discoveries.

\newpage

# W01. A gcd–lcm process

**Source:** IMO 2026, Problem 1; [official paper](https://www.imo-official.org/assets/documents/problems/2026/2026_eng.pdf). Mixed number theory and combinatorics.

**Problem.** Begin with 2026 integers greater than one. A move chooses two current entries \(a,b>1\) and replaces them by \(g=\gcd(a,b)\) and \(\operatorname{lcm}(a,b)/g\). Prove that play must end with exactly one entry greater than one, and that this final entry is independent of all choices.

**Hint.** Use different quantities for termination and for identifying the terminal value.

**Solution.** Let \(P\) be the product of the entries and \(K\) the number greater than one. A move changes the product of its chosen entries from \(ab\) to \(ab/g\). If \(g>1\), the positive integer \(P\) decreases. If \(g=1\), the product stays fixed, but two nonunit entries become \(1,ab\), so \(K\) decreases. The lexicographically ordered pair \((P,K)\) therefore decreases in a well-founded set. Play ends with at most one nonunit entry. Every move produces at least one nonunit entry: either \(g>1\), or \(g=1\) and \(ab>1\). Thus exactly one remains.

Fix a prime \(p\). If its valuations in the two entries are \(u,v\), their new valuations are
\[
\min(u,v),\quad |u-v|.
\]
The gcd of the valuations of *all* entries is preserved, because \(\gcd(u,v)=\gcd(\min(u,v),|u-v|)\). At termination this gcd is the valuation of the sole possible nonunit entry. Thus that entry is
\[
M=\prod_p p^{\gcd(v_p(a_1),\ldots,v_p(a_{2026}))},
\]
with zero exponents omitted. This formula proves independence. The same proof works for any finite initial list of integers greater than one. \(\square\)

**Transfer.** A decreasing quantity need not determine the answer; an invariant need not prove termination. The two certificates play different roles.

# W02. Two covering counts have the same parity

**Source:** RMM 2012, Problem 1. **Record:** `rmm_2012_b79110`.

**Problem.** In a finite bipartite acquaintance graph with parts \(L,R\), a subset of either part covers the other part when every vertex of the other part has a neighbor in it. Prove that the numbers of covering subsets on the two sides have the same parity.

**Hint.** Count pairs of subsets between which there is no edge.

**Solution.** Let \(Z\) count pairs \((X,Y)\), where \(X\subseteq L\), \(Y\subseteq R\), with no edge from \(X\) to \(Y\). For fixed \(X\), its possible partners are all subsets of \(R\setminus N(X)\), giving
\[
Z=\sum_{X\subseteq L}2^{|R\setminus N(X)|}.
\]
Modulo two, a summand survives exactly when \(N(X)=R\). Thus \(Z\) has the parity of the number of covering subsets of \(L\). Counting first by \(Y\) gives the corresponding result for \(R\). Empty parts cause no exception: \(2^0=1\). \(\square\)

**Transfer.** In a parity problem, a power of two can act as an indicator for “no choices remain.”

# W03. Edges above the bipartite threshold force triangles

**Source:** APMO 1989, Problem 4. **Record:** `apm_1989_ab9780`.

**Problem.** A simple graph has \(n\) vertices and \(m\) edges. Prove that its number \(t\) of triangles satisfies
\[
t\ge\frac{4m(m-n^2/4)}{3n}.
\]

**Hint.** Sum common-neighbor counts over edges.

**Solution.** For an edge \(uv\), inclusion–exclusion gives
\[
|N(u)\cap N(v)|\ge d(u)+d(v)-n.
\]
Every triangle is counted on its three edges. Consequently,
\[
3t\ge\sum_{uv\in E}(d(u)+d(v)-n)
=\sum_v d(v)^2-mn
\ge\frac{(2m)^2}{n}-mn,
\]
where the last inequality is Cauchy–Schwarz. Rearranging proves the claim. A negative right side is harmless. \(\square\)

**Audit note.** The recovered source solution contains a reversed inequality in this chain. The displayed chain is the corrected argument.

**Transfer.** A local overlap lower bound followed by a second moment often yields a global supersaturation bound.

# W04. One illuminated square

**Source:** APMO 2007, Problem 5. **Record:** `apm_2007_1337e6`.

**Problem.** On a \(5\times5\) board, a switch toggles its own light and its orthogonally adjacent lights. Starting with all lights off, which positions can be the only illuminated square?

**Answer:** \((2,2),(2,4),(3,3),(4,2),(4,4)\), with rows and columns numbered from one.

**Hint.** Find two parity masks, then supply switches for representatives of the possible positions.

**Solution.** Consider the two masks
\[
A=\begin{pmatrix}1&1&0&1&1\\0&0&0&0&0\\1&1&0&1&1\\0&0&0&0&0\\1&1&0&1&1\end{pmatrix},
\qquad
B=\begin{pmatrix}1&0&1&0&1\\1&0&1&0&1\\0&0&0&0&0\\1&0&1&0&1\\1&0&1&0&1\end{pmatrix}.
\]
Every switch toggles an even number of marked cells in each mask, as checking its center and neighbors shows. Therefore the parity of the illuminated cells marked by each mask stays zero. A lone illuminated cell must be zero in both masks; exactly the five stated positions qualify.

For sufficiency, press the following switches once. The result is obtained by counting each light's incident presses modulo two:

- To light only \((3,3)\): \((1,2),(1,3),(1,5),(2,1),(2,5),(3,1),(3,3),(3,4),(4,3),(5,1),(5,2)\).
- To light only \((2,2)\): \((1,2),(1,4),(2,1),(2,2),(2,4),(2,5),(3,4),(4,1),(4,2),(4,3),(5,2)\).

Rotating the second pattern reaches the other three positions. This proves both necessity and sufficiency. \(\square\)

**Verification.** Gaussian elimination over \(\mathbf F_2\) gives move-matrix rank 23 and exactly these five reachable unit vectors. The explicit press lists were checked independently by the same matrix model.

**Transfer.** Invariants exclude targets; they do not by themselves construct the surviving targets.

# W05. An odd grid and a saturated count

**Source:** India IMO TST 2016, Problem 5. **Record:** `ind_2016_9a166a`.

**Problem.** Color each edge of an \(n\times n\) grid red or blue, where \(n\) is odd. If at most \(n^2\) edges are red, prove that a unit square has at least three blue edges.

**Hint.** Suppose every square has at least two red edges. All the resulting counting inequalities must be equalities.

**Solution.** Count incidences of red edges with unit squares. The supposition gives at least \(2n^2\) incidences. Each red edge contributes at most two, so there are at most \(2n^2\). Equality forces exactly two red edges on every square and no red boundary edges.

Checkerboard-color the unit squares. Every red edge now separates a black square from a white square, so the red-edge incidence totals on the two colors are equal. But each square contributes two, whereas an odd-by-odd board has different numbers of black and white squares. Contradiction. \(\square\)

**Transfer.** A bound that is only just strong enough is an invitation to inspect every equality condition.

# W06. An odd route with distinct airlines

**Source:** RMM 2020, Problem 3. **Record:** `rou_2020_2530c6`.

**Problem.** An \(n\)-vertex flight network has \(n\) airline colors. Each color supports an odd closed route. Prove that an odd closed route exists whose edges have pairwise different colors.

**Hint.** Take a maximum forest with no repeated color.

**Solution.** Choose a rainbow forest \(F\) with the maximum possible number of edges. It has at most \(n-1\) colors, so some color \(c\) is absent. Every \(c\)-edge joins vertices in one component of \(F\), since an edge between components could be added.

An odd closed walk contains an odd cycle: split at a repeated vertex, retaining an odd closed part, until no repetition remains. A \(c\)-colored odd cycle therefore lies in one tree component of \(F\). Bipartition that tree by distance parity. Some edge \(uv\) of the odd cycle has endpoints in the same part. Its tree path has even length. That path together with the \(c\)-edge is an odd rainbow cycle. \(\square\)

**Transfer.** Maximality can convert every unused object into a structural restriction. Choose a forest when paths and parity are the desired restrictions.

# W07. A convex-hull identity

**Source:** IMO Shortlist 2006, C3. **Record:** `imo_2006_f50971`.

**Problem.** Let \(S\) be a finite planar set with no three collinear points. For a convex polygon \(P\) with vertices in \(S\), let \(a(P)\) count its vertices and \(b(P)\) the points of \(S\) outside it. Include segments, points and the empty polygon. Prove for every real \(x\) that
\[
\sum_P x^{a(P)}(1-x)^{b(P)}=1.
\]

**Hint.** Initially restrict \(x\) to a probability.

**Solution.** For \(0<x<1\), choose each point of \(S\) independently with probability \(x\). The convex hull is \(P\) exactly when all its vertices are chosen and all points outside \(P\) are omitted; its interior points are unrestricted. No point lies on an edge except its endpoints, by general position. Hence
\[
\Pr(\operatorname{conv}(T)=P)=x^{a(P)}(1-x)^{b(P)}.
\]
Every random subset has exactly one hull, including the degenerate cases. Summing these disjoint exhaustive events gives one. Both sides are polynomials in \(x\), and equality on an interval implies equality for all real \(x\). \(\square\)

**Transfer.** Required choices, forbidden choices, and free choices often explain the three factors \(x\), \(1-x\), and \(1\).

# W08. Tournaments generated by commuting involutions

**Source:** IMO Shortlist 2006, C5. **Record:** `imo_2006_b88369`.

**Problem.** In each of \(k\) rounds, \(n\) players are paired, with no pair repeated. Require that whenever \(A,B\) and \(C,D\) are pairs in one round and \(A,C\) is a pair in another, then \(B,D\) is also a pair in that other round. Determine the possible positive integers \((n,k)\).

**Answer:** If \(2^t\) is the least power of two at least \(k+1\), precisely those pairs with \(2^t\mid n\).

**Solution.** Let \(g_i\) send a player to their opponent in round \(i\). It is a fixed-point-free involution. The compatibility condition says \(g_ig_j=g_jg_i\). The permutations they generate form a quotient of \(\mathbf F_2^k\). Each orbit consequently has power-of-two size, by the orbit–stabilizer formula. An orbit containing \(v\) includes the \(k+1\) distinct players \(v,g_1v,\ldots,g_kv\); thus its size is divisible by \(2^t\). Summing orbit sizes gives \(2^t\mid n\).

Conversely, partition the players into groups of size \(2^t\), labeled by \(\mathbf F_2^t\). Choose distinct nonzero vectors \(u_1,\ldots,u_k\). In round \(i\), pair \(v\) with \(v+u_i\) within each group. These are disjoint pairs, no pairing repeats, and translations commute. All requirements follow. \(\square\)

**Transfer.** Commuting involutions suggest binary coordinates even when the original objects have no visible geometry.

# W09. Synchronized bishops

**Source:** RMM 2024, Problem 1. **Record:** `rou_2024_d65b67`.

**Problem.** Put one labeled bishop in each square of the top row of a \(2^n\times2^n\) board. A jump moves every bishop diagonally so that they again occupy distinct squares in one common row. How many orders can occur on the bottom row?

**Answer:** \(2^{n-1}\).

**Solution.** Set \(N=2^n\), and number columns \(0,\ldots,N-1\). A jump between rows separated by \(h\) sends every column to a distinct column at distance \(h\). In each residue class modulo \(h\), the available columns form a path; the first vertex has only its next vertex as a destination, forcing those two to swap, and then forcing all subsequent swaps. Such a permutation exists exactly when all these paths have even length. Writing \(N=qh+r\), their lengths are \(q\) and, if \(r>0\), \(q+1\); hence \(r=0\) and \(q\) is even. Thus \(2h\mid N\), so \(h=2^d\) for some \(d\).

The forced swaps are precisely \(c\mapsto c\mathbin{\mathrm{xor}}2^d\). Every sequence of jumps therefore produces one XOR translation \(c\mapsto c\mathbin{\mathrm{xor}}u\). The total vertical displacement to the bottom is \(N-1\), which is odd, so an odd number of height-one jumps occurs. Consequently \(u\) is odd. There are at most \(N/2\) possibilities.

For any odd \(u<N\), first make downward jumps with heights the powers of two occurring in its binary expansion. They end at row \(u\) and produce XOR mask \(u\). Then make \(N-1-u\) downward jumps of height one. This number is even, so these last jumps do not change the mask. Every intermediate row is within the board. All \(N/2\) odd masks occur. \(\square\)

![A synchronized height-two jump on an eight-column board.](figures/bishop_xor.pdf){width=95%}

**Transfer.** Classify one legal move before attempting to classify all move sequences.

# W10. Preventing a directed cycle forever

**Source:** RMM 2018, Problem 3. **Record:** `rou_2018_a59bad`.

**Problem.** Ann and Bob alternately orient previously unoriented unit edges of the infinite square grid, with Ann first. Bob wins if a directed cycle ever appears, including after Ann's move. Can he force a win?

**Answer:** No.

**Solution.** Draw the vertical line \(x=0\). For each vertex \((x,y)\) with \(x<0\), pair its edge going right with its edge going up. For each vertex with \(x>0\), pair its edge going left with its edge going down. This partitions all grid edges except the vertical edges on \(x=0\) into pairs.

Ann first orients an edge on the exceptional line. Whenever Bob uses an edge of a pair, Ann immediately orients its mate so that both edges point into their shared vertex, or both point out. Whenever Bob uses an exceptional edge, Ann uses another unused exceptional edge, which always exists. Before each Bob move, a pair is either wholly unoriented or wholly oriented. Thus the required mate is always available.

Suppose a directed cycle appeared. If it has a vertex with negative \(x\), choose a leftmost vertex and, among those, a lowest one. The cycle's two edges there must go up and right. They form one of the designated pairs and cannot be consecutively traversed in a directed cycle. If the cycle has no negative \(x\), choose its rightmost, highest vertex; its two cycle edges go down and left. Its \(x\)-coordinate is positive, since a cycle cannot lie on a single vertical line. Again they form a forbidden pair.

This argument also applies immediately after Bob's move: an incomplete pair cannot contribute both edges to a cycle. Hence a directed cycle never appears. \(\square\)

**Transfer.** A pairing strategy needs a proof of response availability and a proof that the target configuration must use an incompatible pair.

# W11. A sum-free sequence at the density boundary

**Source:** USA TSTST 2013, Problem 1, as identified in the recovered selection booklet. **Record:** `usa_2013_bfa49c`.

**Problem.** Find all strictly increasing positive integer sequences \((a_i)\) with no equation \(a_i+a_j=a_k\), allowing repeated indices, and with \(a_k=2k-1\) for infinitely many \(k\).

**Answer:** \(a_k=2k-1\) for every \(k\).

**Solution.** Put \(m=a_1\). In any interval of \(2m\) consecutive integers, pair its elements at distance \(m\). At most one element of each pair belongs to the sequence, since their difference would otherwise equal the sequence term \(m\). Therefore
\[
a_{i+m}\ge a_i+2m.
\]
If \(m\) consecutive indices all satisfied \(a_i>2i-1\), this inequality would propagate the same strict inequality through every subsequent block of \(m\) indices. That would contradict the infinitely many equalities. Thus every block of \(m\) consecutive indices contains an index with \(a_i\le2i-1\).

For \(1\le i\le m\), increasingness gives \(a_i\ge m+i-1\), which exceeds \(2i-1\) when \(i<m\). Hence \(a_m=2m-1\), and the first block is exactly \(m,m+1,\ldots,2m-1\).

For the next block,
\[
a_{m+i}\ge a_i+2m=3m+i-1.
\]
This exceeds \(2(m+i)-1\) when \(i<m\). The same argument forces \(a_{2m}=4m-1\), so the second block is \(3m,\ldots,4m-1\). If \(m>1\), the sequence contains \(2m-1\) and \(4m-2=2(2m-1)\), impossible. Thus \(m=1\). Now \(a_{i+1}\ge a_i+2\), so \(a_i\ge2i-1\), while the block assertion with length one gives the reverse inequality. The odd positive integers satisfy all requirements. \(\square\)

**Transfer.** A one-sided defect recurrence turns infinitely many exact hits into rigidity.

# W12. Large disjoint cross-intersecting families

**Source:** IMO Shortlist 2007, C7. **Record:** `imo_2007_67267d`.

**Problem.** For every \(0<\alpha<(3-\sqrt5)/2\), find \(n,p\) with \(p>\alpha2^n\) and two disjoint families \(\mathcal S,\mathcal T\), each of \(p\) distinct subsets of \([n]\), such that each member of \(\mathcal S\) intersects every member of \(\mathcal T\).

**Hint.** Partition the ground set into blocks. “Meets every block” and “contains a full block” force intersection.

**Solution.** Put \(\delta=(3-\sqrt5)/2\). Partition \([km]\) into \(k\) blocks of size \(m\). Let \(\mathcal S\) consist of subsets meeting every block. Let \(\mathcal T\) consist of subsets containing at least one whole block and missing at least one whole block. They are disjoint, and every \(S\in\mathcal S\) meets the full block contained in any \(T\in\mathcal T\).

Their cardinalities are
\[
|\mathcal S|=(2^m-1)^k,
\qquad
|\mathcal T|=2^{mk}-2(2^m-1)^k+(2^m-2)^k.
\]
The second formula is inclusion–exclusion for having both a full block and an empty block. Choose \(k=\lfloor2^m\log(1/\delta)\rfloor\). As \(m\to\infty\),
\[
\frac{|\mathcal S|}{2^{mk}}\longrightarrow\delta,
\qquad
\frac{|\mathcal T|}{2^{mk}}\longrightarrow1-2\delta+\delta^2=\delta.
\]
For sufficiently large \(m\), both sizes exceed \(\alpha2^{mk}\). Set \(p\) to their minimum and discard surplus members of the larger family. \(\square\)

**Transfer.** Construct an exact finite family first, then tune its density by a limit. This argument does not claim that \(\delta\) is the best possible threshold for every version of the problem.

# W13. Fifteen subsets of a 56-element set

**Source:** China Mathematical Olympiad 2006, Problem 6, attributed to Leng Gangsong. **Record:** `chn_2006_c22bc5`.

**Problem.** Find the smallest integer \(N\) such that, if every seven of fifteen subsets of a 56-element set have union of size at least \(N\), some three subsets have a common element.

**Answer:** \(41\).

**Solution: upper bound.** Suppose no element occurs in three sets. Add memberships until every element occurs in exactly two sets; this preserves the absence of a triple intersection and can only increase unions. There are 112 memberships, so some set \(A\) has size \(a\ge8\).

Choose seven of the other fourteen sets uniformly. An element outside \(A\) belongs to two of these fourteen sets, and is covered with probability
\[
1-\frac{\binom{12}{7}}{\binom{14}{7}}=\frac{10}{13}.
\]
An element of \(A\) belongs to one of them and is covered with probability \(1/2\). The expected union size is therefore
\[
(56-a)\frac{10}{13}+\frac a2
=\frac{560}{13}-\frac{7a}{26}
\le\frac{532}{13}<41.
\]
Some seven sets have union at most 40, contrary to the required hypothesis with \(N=41\).

**Sharpness.** Use the 56 cells of a \(7\times8\) rectangle, with its seven rows and eight columns as the fifteen sets. No point belongs to three sets. A choice of \(s\) rows and \(7-s\) columns has union
\[
8s+7(7-s)-s(7-s)=(s-3)^2+40\ge40.
\]
Thus 40 does not suffice. \(\square\)

**Transfer.** Low multiplicity turns a set system into a weighted graph on the sets. Delete a high-degree vertex and average on the remainder.

# W14. Forcing a rainbow three-cell window

**Source:** RMM 2012, Problem 5. **Record:** `rmm_2012_704e6f`.

**Problem.** An \(n\times n\) board, \(n\ge3\), uses exactly \(C=\lfloor(n+2)^2/3\rfloor\) colors. Prove that some horizontal or vertical three-cell window has three different colors.

**Solution.** For a fixed color occurring \(p\) times, count windows containing that color at least twice. If \(p=1\), there are none. Suppose \(p\ge2\), and the color occupies \(r\) rows and \(c\) columns.

In one occupied row containing \(q\) occurrences, the number of such windows is at most \(3q/2-1\). For \(q=1\), there are zero, which satisfies the bound. For \(q\ge2\), count incidences between occurrences and windows containing at least two of them. Each occurrence is in at most three windows; the leftmost and rightmost occurrences are each in at most two such windows. Thus twice the number of windows is at most \(3q-2\). Summing over rows and columns gives at most
\[
3p-(r+c)\le3(p-1),
\]
because two or more cells occupy at least three rows-and-columns in total.

If no window were rainbow, each of the \(2n(n-2)\) windows would contain a repeated color. Summing the bound over colors would give
\[
2n(n-2)\le3(n^2-C).
\]
But \(3C\ge(n+2)^2-2=n^2+4n+2\), so the right side is at most \(2n(n-2)-2\), a contradiction. \(\square\)

**Transfer.** Charge every forbidden configuration to one color, and bound a color's contribution in terms of its occurrences minus one.

# W15. The anti-Pascal pyramid

**Source:** IMO 2018, Problem 3; also IMO Shortlist 2018, C4. **Record:** `imo_2018_55614a`.

**Problem.** In a triangular array, every entry above the bottom row equals the absolute difference of its two children. Can an array with 2018 rows contain every integer from 1 through \(1+2+\cdots+2018\) exactly once?

**Answer:** No. The following argument excludes every height \(n\ge15\).

**Solution.** Write \(T=n(n+1)/2\). Starting at the top entry \(b_1=a_1\), repeatedly follow the larger child \(b_i\); call the other child \(a_i\). Then
\[
b_i=b_{i-1}+a_i,
\qquad b_n=a_1+\cdots+a_n.
\]
The \(a_i\) occupy different rows, hence are distinct positive integers. Since \(b_n\le T\), their sum is at most \(T\), but any \(n\) distinct positive integers have sum at least \(T\). Equality forces the \(a_i\) to be exactly \(1,\ldots,n\).

The final two children occupy adjacent bottom positions \(r,r+1\). The subtriangle above bottom positions \(1,\ldots,r-1\), and the subtriangle above bottom positions \(r+2,\ldots,n\), contain none of the \(a_i\). Here is the boundary check: if the followed entry in row \(i\) has column \(p_i\), then \(p_i\le r\le p_i+n-1-i\). Its sibling has column between \(p_i-1\) and \(p_i+1\), and thus lies between \(r-n+i\) and \(r+1\); the left subtriangle ends at column \(r-n+i-1\), while the right begins at \(r+2\). The top entry also lies outside both.

One of these subtriangles has height
\[
\ell\ge\left\lceil\frac{n-2}{2}\right\rceil.
\]
Every entry in it exceeds \(n\), since all smaller entries have already been located among the \(a_i\). Applying the larger-child path argument within it yields a bottom entry at least
\[
(n+1)+\cdots+(n+\ell)=\frac{\ell(2n+\ell+1)}2.
\]
For \(n\ge15\) and the displayed lower bound on \(\ell\), this is greater than \(n(n+1)/2=T\). For even \(n=2s\ge16\), the difference of twice these bounds is \(s^2-7s\), positive; for odd \(n=2s+1\ge15\), it is \(s^2-3s-2\), positive. Contradiction. \(\square\)

**Transfer.** A first extremal path can consume every cheap resource, making a disjoint second path impossibly expensive.

# W16. Knights against blocking queens

**Source:** IMO Shortlist 2018, C2. **Record:** `imo_2018_eed763`.

**Problem.** Horst places a knight on an empty square of a \(20\times20\) board without attacking any previous knight. Queenie then occupies an empty square with a queen. They repeat until a player cannot move. Queens only occupy squares; they impose no attack restriction. What number of knights can Horst guarantee?

**Answer:** \(100\).

**Solution: guarantee.** Horst uses only one checkerboard color, containing 200 squares. Knights on that color do not attack one another. Before his 100th move, at most 99 knights and 99 queens occupy it, so an empty square remains. He can place 100 knights.

**Upper bound.** Partition the board into twenty-five \(4\times4\) blocks. In each block, partition its cells into four knight-move four-cycles. The following are their vertex sets, in local coordinates:
\[
\begin{aligned}
&\{(1,1),(2,3),(3,2),(4,4)\},\\
&\{(1,2),(2,4),(3,1),(4,3)\},\\
&\{(1,3),(2,1),(3,4),(4,2)\},\\
&\{(1,4),(2,2),(3,3),(4,1)\}.
\end{aligned}
\]
Every vertex in each set has exactly two knight neighbors in that set. Whenever Horst first uses a cycle, Queenie occupies the opposite vertex in that four-cycle. The two remaining vertices are attacked by Horst's knight. Thus Horst can never use that cycle again. A cycle he enters is untouched, so Queenie's response is always available. There are 100 cycles, giving the upper bound. \(\square\)

**Transfer.** A local conflict graph can give a global strategy when the board is partitioned into copies of it.

# W17. One spanning tree meeting three quotas

**Source:** RMM 2023, Problem 6. **Record:** `rou_2023_0cea08`.

**Problem.** A connected graph has \(r+g+b+1\) vertices, with red, green and blue edges. There is a spanning tree with exactly \(r\) red edges, another with exactly \(g\) green edges, and another with exactly \(b\) blue edges. Prove that one tree meets all three quotas simultaneously.

**Solution.** Use the graphic matroid: independent sets are forests and the rank of an edge set is its maximum forest size. The color-quota theorem, proved from Rado's theorem in the theory book, says that a forest with prescribed color counts exists precisely when every union of color classes has rank at least the sum of its quotas.

The assumed tree with \(r\) red edges supplies an independent set of \(r\) red edges, giving the red singleton condition. The other singleton conditions follow similarly. The assumed tree with \(b\) blue edges has \(r+g\) nonblue edges, proving the red-green condition. The other two-color conditions are analogous. Connectivity supplies total rank \(r+g+b\), and the empty condition is automatic.

Thus a forest with exactly \(r,g,b\) edges of the three colors exists. It has one less edge than the number of vertices, so it is a spanning tree. \(\square\)

**Transfer.** Individual feasibility happens to control all proper color subsets for three colors. With four colors, two-color obstructions remain; the theory book gives an explicit counterexample.

# W18. Keeping 150 entries of a doubly stochastic matrix

**Source:** China TST 2023, Test Three, Day 2, Problem 6. **Record:** `chn_2023_a44cf5`.

**Problem.** In any nonnegative \(100\times100\) matrix with every row sum and column sum equal to one, retain 150 entries and set the others to zero. What is the largest universal lower bound \(\lambda\) on all remaining row and column sums?

**Answer:** \(\lambda=17/1900=51/5700\).

**Solution: guarantee.** Put \(\tau=51/5700\). Make a bipartite graph joining row \(i\) to column \(j\) when its entry is at least \(\tau\). This graph has a matching of size at least 50. Otherwise Hall's deficiency formula supplies a set of \(k\) rows with at most \(k-51\) neighboring columns. The entries in these rows outside their neighboring columns have total mass at least 51. There are at most
\[
k(151-k)\le75\cdot76=5700
\]
such entries, each strictly below \(\tau\), a contradiction. If fewer than \(k-51\) neighbors occur, enlarge their column set to exactly \(k-51\); the mass bound remains valid.

Keep 50 matched entries. For each unmatched row and each unmatched column, keep a largest entry. This uses at most \(50+50+50=150\) entries. A matched row or column retains at least \(\tau\); every other row or column retains at least \(1/100\ge\tau\). If entries overlap, add arbitrary entries to reach exactly 150.

**Sharpness.** Split rows into 75 and 25, and columns into 24 and 76. Fill the four blocks as follows:
\[
\begin{pmatrix}
\frac1{75}\mathbf1_{75\times24}&\frac{17}{1900}\mathbf1_{75\times76}\\
0_{25\times24}&\frac1{76}\mathbf1_{25\times76}
\end{pmatrix}.
\]
Every row and column sums to one. Suppose all retained sums exceeded \(\tau\). Let \(a,c,e\) be the numbers retained in the top-left, top-right and bottom-right blocks. Among the 75 top rows and 76 right columns, at least \(151-a-e\) receive no retained entry from the first or last block. Each of those rows or columns must contain at least two retained top-right entries, since one equals only \(\tau\). Each top-right entry serves at most two such requirements. Hence
\[
c\ge151-a-e,
\]
requiring at least 151 retained entries, impossible. \(\square\)

![The sharp four-block doubly stochastic matrix.](figures/stochastic_blocks.pdf){width=70%}

**Generalization.** The theory book proves the exact answer for every \(n\times n\) matrix and every budget \(n\le B\le2n-1\):
\[
\Lambda(n,B)=\frac{B-n+1}{\left\lfloor(B+1)^2/4\right\rfloor}.
\]
This is a proved generalization in the manuscript, not a claim that the result is new to the literature.

# W19. A set whose largest half is constrained

**Source:** USAMO 2006, Problem 2. **Record:** `usa_2006_9454b3`.

**Problem.** For a positive integer \(k\), find the least \(N\) for which \(2k+1\) distinct positive integers have total sum greater than \(N\), while every \(k\)-element subset has sum at most \(N/2\).

**Answer:** \(2k^3+3k^2+3k\).

**Solution.** Sort the integers, and let their middle entry be \(m\). Let \(L\) be the sum of the bottom \(k+1\) entries and \(U\) the sum of the top \(k\). We have \(U\le N/2\), while \(L+U>N\), so \(L>U\). Distinctness gives
\[
L\le(k+1)m-\frac{k(k+1)}2,
\qquad
U\ge km+\frac{k(k+1)}2.
\]
Thus \(m>k(k+1)\), and since \(m\) is an integer, \(m\ge k^2+k+1\). Therefore
\[
N\ge2U\ge2k(k^2+k+1)+k(k+1)=2k^3+3k^2+3k.
\]
For equality, take the consecutive integers \(k^2+1,\ldots,k^2+2k+1\). Their total is \(N+1\), and their \(k\) largest entries sum to \(N/2\). Every other \(k\)-subset has no larger sum. \(\square\)

**Transfer.** Order the objects, isolate the median, and compare the forced arithmetic progressions on either side.

# W20. Unique subsums with odd parts

**Source:** India IMO TST 2013, Problem 3. **Record:** `ind_2013_5ef73e`.

**Problem.** A partition of 9999 into odd positive parts is called sum-friendly if each integer from 0 to 9999 has exactly one subsum representation. Equal copies of a part are indistinguishable: a representation specifies only how many copies of each distinct value are used. Count the sum-friendly partitions.

**Answer:** \(16\).

**Solution.** Write the distinct part values as \(w_1<\cdots<w_s\), with multiplicities \(c_i\). Necessarily \(w_1=1\). If earlier parts represent every integer from 0 to \(S\) uniquely, the next value must be \(S+1\): a smaller value duplicates a representation, while a larger value leaves \(S+1\) missing. Conversely, copies of a next part equal to \(S+1\) extend the represented interval by adjacent disjoint translates. Thus the condition is equivalent to
\[
w_j=\prod_{i<j}(c_i+1),\qquad
10000=\prod_{i=1}^s(c_i+1).
\]
Put \(d_i=c_i+1\ge2\). Since every \(w_j\) is odd, all \(d_i\) except possibly the last must be odd. Now \(10000=2^4 5^4\), so the earlier radices are powers \(5^{e_1},\ldots,5^{e_t}\) with positive exponents and total at most four. The last radix is forced to be \(2^4 5^{4-\sum e_i}\), which is always at least two.

For total exponent zero there is one choice, the empty earlier list. For total exponent \(j\ge1\), its ordered compositions number \(2^{j-1}\), by choosing the cuts between \(j\) unit marks. Therefore the answer is
\[
1+1+2+4+8=16.
\]
The digit construction proves every counted possibility works and that no two give the same partition. \(\square\)

**Transfer.** Completeness forbids gaps and uniqueness forbids overlaps; together they force the next place value exactly.

# W21. Equal totals but strongly unbalanced rows and columns

**Source:** Vietnam Mathematical Olympiad 2016, Day 1, Problem 4. **Record:** `vnm_2016_c11c43`.

**Problem.** An \(m\times n\) board contains equal numbers of two symbols. In each row their counts differ by at least \(n/2\), and in each column by at least \(m/2\). Show that \(m,n\) are divisible by four, and construct such a board for \(m=n=2016\).

**Solution.** Give entries values \(+1,-1\). No row or column has zero sum. Let \(p\) be the number of positive-sum rows and \(q\) the number of positive-sum columns. Both signs occur among rows and among columns because the total sum is zero. Put
\[
a=\min(p,m-p)>0,\qquad b=\min(q,n-q)>0.
\]
Let \(s_1\) count entries disagreeing with their row's majority sign. In a positive row at most \(n/4\) entries are negative; in a negative row at most \(n/4\) are positive. Write their respective total minority counts as \(u,v\). The global balance says \(u-v=n(p-m/2)\). From \(u\le pn/4\) and \(v\le(m-p)n/4\), we obtain both
\[
s_1=u+v\le\frac{n(m-p)}2,
\qquad s_1\le\frac{np}2.
\]
Thus \(s_1\le na/2\). Similarly the number \(s_2\) disagreeing with column majority satisfies \(s_2\le mb/2\).

The number of cells whose row and column majorities disagree is
\[
U=p(n-q)+(m-p)q.
\]
Every column contains at least \(a\) such cells and every row at least \(b\), so \(U\ge na\) and \(U\ge mb\). Each such cell disagrees with exactly one of its two majority signs. Therefore
\[
U\le s_1+s_2\le\frac{na+mb}{2}\le U.
\]
All inequalities are equalities. Equality in \(s_1\le na/2\) forces one nonempty row-sign class to attain its summed minority bound, so each row in that class has exactly \(n/4\) minority entries. Hence \(4\mid n\). Equality for columns gives \(4\mid m\).

For construction, repeat the following \(4\times4\) tile in both directions:
\[
\begin{pmatrix}
+&+&+&-\\
+&+&-&+\\
+&-&-&-\\
-&+&-&-
\end{pmatrix}.
\]
It contains eight of each sign, and every row and column has imbalance two. Repetition works whenever both dimensions are multiples of four, including 2016. \(\square\)

**Transfer.** Count disagreement with two competing classifications. A sandwich of bounds can force an integrality condition.

# W22. Cookie pebbling on an even cycle

**Source:** Korean Mathematical Olympiad 2010, Problem 5. National pipeline supplement. **Record:** `kor_2010_1dc4be`.

**Problem.** At the vertices of a cycle with \(2n\) vertices are nonnegative integer numbers of cookies. A move consumes two cookies at a vertex and places one at a neighboring vertex. Find the smallest total number guaranteeing that a prescribed vertex can obtain a cookie, regardless of the initial distribution.

**Answer:** \(2^n\).

**Lower bound.** Give a cookie at distance \(d\) from the target weight \(2^{-d}\). A move deletes weight \(2\cdot2^{-d}\) and adds at most \(2^{-(d-1)}\), so total weight cannot increase. If \(2^n-1\) cookies start at the antipode, their total weight is less than one. The target can never receive a cookie of weight one.

**Path lemma.** On a path of length \(h\), any \(2^h\) cookies suffice to reach an endpoint. Induct on \(h\), with \(h=0\) immediate. Ignore extras so the total is exactly \(2^h\). If the farthest vertex has \(c\) cookies, move \(\lfloor c/2\rfloor\) one step closer. On the shortened path remain
\[
2^h-c+\lfloor c/2\rfloor=2^h-\lceil c/2\rceil\ge2^{h-1}
\]
cookies. Apply induction.

**Upper bound.** The case \(n=1\) is immediate. Suppose \(n\ge2\) and the target initially has none. Let \(c\) cookies be at the antipode. The two open arcs between target and antipode contain \(2^n-c\) cookies; choose one containing at least \(\lceil(2^n-c)/2\rceil\). Move \(\lfloor c/2\rfloor\) cookies from the antipode into that arc. It now contains at least \(2^{n-1}\) cookies. Together with the target it is a path of length \(n-1\), so the lemma delivers a cookie. \(\square\)

**Audit note.** A source transcription rendered the exponential weight incorrectly. The reciprocal power is essential.

**Transfer.** A weighted obstruction often reveals the exact threshold; an induction on a path supplies the matching construction.

# W23. A finite state space with draws

**Source:** Balkan Mathematical Olympiad 2018, Problem 3. **Record:** `mkd_2018_3ac94a`.

**Problem.** Starting from positive piles \((a,b)\), Alice and Bob alternate, Alice first. A move chooses an even pile and transfers half of it to the other pile. A player with no legal move loses. Determine exactly when Bob can force a win.

**Answer:** Precisely when \(v_2(a)=v_2(b)\) is even. Some other positions are draws under optimal play.

**Solution.** If both valuations equal \(k\ge1\), halving either pile produces two piles with valuation \(k-1\): the transferred half has valuation \(k-1\), while the untouched pile previously had valuation \(k\). If \(k=0\), both piles are odd and no move exists. Thus equal valuations give exactly \(k\) further moves regardless of choices. The next player loses exactly when \(k\) is even.

Now suppose valuations are unequal, with minimum \(k\). Halving the lower-valuation pile, if \(k>0\), produces equal valuations \(k-1\). Halving the higher-valuation pile preserves unequal valuations with minimum \(k\). To check the borderline case where the valuations differ by one, the halved high pile has valuation \(k\), while its sum with the other pile has valuation greater than \(k\); they are still unequal.

If \(k\) is odd, the next player can halve the lower-valuation pile and leave equal even valuations, forcing a win. If \(k\) is even, either player can avoid defeat by always halving the higher-valuation pile. This move is always legal and stays in the same class. Halving the lower pile, when legal, would give the opponent equal odd valuations and a forced win. Hence neither player can force victory in this unequal-even class: continued optimal play draws.

Bob therefore has a forced win exactly in the equal-even class stated above. \(\square\)

**Verification.** Retrograde analysis of every positive ordered pair with \(a+b\le150\) agrees with the win/lose/draw classification.

**Transfer.** A finite graph of positions can contain directed cycles. Normal-play recursions require termination, or must explicitly handle draws.

# W24. The fewest tiles in a maximal placement

**Source:** EGMO 2016, Problem 5. **Record:** `rou_2016_9aa109`.

**Problem.** Let \(k\ge2\) and \(k\le n\le2k-1\). Place nonoverlapping \(1\times k\) or \(k\times1\) tiles on an \(n\times n\) board until no further tile fits. What is the smallest possible number of tiles?

**Answer:** \(n\) if \(n=k\); otherwise \(\min(n,2n-2k+2)\).

**Lower bound.** Call a row horizontal if it contains a horizontal tile, and a column vertical if it contains a vertical tile. Since \(n<2k\), a row contains at most one horizontal tile and a column at most one vertical tile. If all rows are horizontal or all columns vertical, there are at least \(n\) tiles.

Otherwise let \(r>0\) rows be nonhorizontal and \(c>0\) columns nonvertical. The nonhorizontal rows form an interval. Indeed, if a horizontal tile is in row \(h\) and fewer than \(k\) rows lie above it, no vertical tile can occupy any cell above it in its \(k\) columns: such a tile would cross row \(h\). Maximality therefore forces a horizontal tile in every row above. The analogous statement holds below. At least one side of any row has fewer than \(k\) rows, so the horizontal rows form a prefix and a suffix. The same reasoning makes the nonvertical columns an interval.

Their \(r\times c\) intersection is empty. Maximality implies \(r<k\) and \(c<k\), otherwise a vertical or horizontal tile would fit there. There are consequently at least \(n-k+1\) horizontal tiles and at least \(n-k+1\) vertical tiles, for a total of \(2n-2k+2\). Together the cases give the asserted lower bound, except that when \(n=k\), any horizontal tile forbids every vertical tile, so maximality forces all \(n\) parallel tiles.

**Constructions.** For \(n=k\), fill every row. For \(n=2k-1\), put one horizontal tile in every row: use columns \(1,\ldots,k\), except in row \(k\), where it uses \(k,\ldots,2k-1\). No horizontal gap reaches length \(k\); each vertical gap is interrupted by row \(k\) or by the other rows.

For \(k<n<2k-1\), use zero-based coordinates. On the upper-left \((k+1)\times(k+1)\) square place four tiles:

- row 0, columns \(0,\ldots,k-1\);
- column 0, rows \(1,\ldots,k\);
- row \(k\), columns \(1,\ldots,k\);
- column \(k\), rows \(0,\ldots,k-1\).

For each additional row, add a tile in columns \(1,\ldots,k\); for each additional column, add a tile in rows \(1,\ldots,k\). These tiles do not overlap. In the central rows and columns, the remaining central gap has length \(k-1\); outer gaps have length at most \(n-k<k\). Thus no further tile fits. The count is \(4+2(n-k-1)=2n-2k+2\). \(\square\)

![A maximal eight-tile placement for k=5 and n=8.](figures/maximal_tiles.pdf){width=70%}

**Audit note.** The four-tile construction needs a \((k+1)\times(k+1)\) square; a recovered description saying \(k\times k\) was corrected.

**Transfer.** “Maximal” means no legal addition, not maximum size. Identify the shape of the uncovered rows and columns before counting tiles.

# W25. A private witness in every proper-union subfamily

**Source:** RMM 2017, Problem 3. **Record:** `rou_2017_f8413b`.

**Problem.** Let \(|X|=n>1\). A family of distinct proper nonempty subsets of \(X\) has the following property: every nonempty subfamily whose union is not \(X\) has an element belonging to exactly one member of that subfamily. Find its maximum size.

**Answer:** \(2n-2\).

**Solution.** Induct on \(n\), allowing the empty family and starting with \(n=1\), where its size is zero. Choose \(x\) omitted by as many members as possible, and write \(\mathcal F_x\) for the members omitting \(x\). If the family is nonempty, \(\mathcal F_x\) is nonempty, since every member is proper. Its union omits \(x\), so some element \(y\ne x\) occurs in exactly one member \(D\) of \(\mathcal F_x\). Hence
\[
\mathcal F_x\setminus\{D\}\subseteq\mathcal F_y.
\]
Maximality of \(|\mathcal F_x|\) implies \(|\mathcal F_y\setminus\mathcal F_x|\le1\). Delete \(D\) and, if present, the one member in that difference. In all remaining sets, \(x,y\) have identical membership. Identify them as one element. The sets remain distinct, proper and nonempty; a forbidden subfamily after identification would lift to a forbidden subfamily before it. By induction at most \(2(n-1)-2\) sets remain. At most two were deleted, giving \(2n-2\).

For equality, order \(X\) and take every proper nonempty prefix and every proper nonempty suffix. There are \(2n-2\). In a subfamily missing an element \(m\), all prefixes end before \(m\) and all suffixes start after \(m\). If a prefix is selected, the endpoint of the largest selected prefix belongs to no other selected set; otherwise use the starting point of the largest selected suffix. This is the required private witness. \(\square\)

**Transfer.** Two almost-identical incidence columns permit contraction at bounded cost. Extremizing the number of omissions finds them.

# W26. Reducing a set by sum-and-difference moves

**Source:** RMM 2021, Problem 4. **Record:** `rmm_2021_03b2ae`.

**Problem.** Start with \(\{1,2,\ldots,n\}\), \(n\ge2\). Erase two distinct current numbers \(a,b\), and insert \(a+b\) and \(|a-b|\), suppressing any duplicate with an existing number. Can the set be reduced to exactly two elements?

**Answer:** Yes; in fact, every finite set of at least two distinct positive integers can.

**Solution.** A move never increases cardinality and never leaves fewer than two elements, since its two newly specified positive numbers are distinct. It is enough to prove that every set of size \(k\ge3\) can eventually decrease its size.

Suppose otherwise, and choose a bad \(k\)-element set with minimum sum. Every move from a bad set preserves size \(k\) and remains bad. Two consecutive sum-and-difference moves on a pair \(a<b\) replace it by \(2a,2b\); any intervening collision would already decrease size, contradicting badness. Thus any chosen pair can be doubled within a bad set.

We will also use a logical normalization: multiplying or dividing *all* entries by a common factor preserves whether a reduction exists, provided the normalized entries are integers. This follows by scaling every move in a proposed sequence. Division is not being asserted to be a legal move in the game.

If the bad set contains two even entries \(a,b\), obtain a bad set with those two entries halved and all others unchanged. For even \(k\), double the other \(k-2\) entries in pairs, then normalize by two. For odd \(k\), double all entries except \(a\) in pairs, then all except the current copy of \(b\), then normalize by four. In the latter case \(a,b\) were doubled once and every other entry twice. The resulting integer set is bad but has smaller sum, a contradiction.

Thus a minimum-sum bad set has at most one even entry. Since \(k\ge3\), choose odd entries \(a<b\). One move replaces them by the even entries \(a+b,b-a\). If a collision occurs, we are done; otherwise this is still a bad set. Apply the preceding simulated halving to those two entries. Their combined sum becomes \(b\), whereas initially it was \(a+b\); every other entry returns to its original value. This again produces a bad set of smaller sum, a contradiction.

No bad set exists. Reduce cardinality repeatedly until it equals two. \(\square\)

**Transfer.** A normalization can compare counterexamples without being a legal operation. State that distinction explicitly; otherwise a valid descent can look like an illegal strategy.

# Verification and reading notes {.unnumbered}

The accompanying `verify_examples.py` uses exact arithmetic, finite-field elimination, exhaustive subset enumeration and retrograde analysis. Its saved output records which finite cases were tested. Those checks supplement the mathematical proofs; they do not prove general statements or establish historical completeness.

Source-provided solution files outside W01–W26 are labeled **not independently reviewed**. The theory book was synthesized from this reviewed set and established mathematical theory, not from an assertion that every imported proof has been read and checked. The source ledger retains bibliographic metadata and known defects for further review.
