---
title: "Olympiad Geometry: A Calculus of Configurations"
author: "Ayden Bi"
date: "Research edition • 6 November 2026"
lang: en-US
---

# Preface {.unnumbered}

A successful geometry solution preserves a small amount of information through a complicated configuration. An angle survives a change of circle. A ratio survives a similarity. A power survives a change of secant. A reflection exchanges two difficult objects and fixes the point we want. The skill is to choose the information that reaches the conclusion with the fewest justified steps.

This book organizes those operations into a rigorous working language. Each tool has hypotheses, a proof, a recognition cue, and a link to the checked cases G01–G16 in the companion volume. It includes synthetic, vector, coordinate and complex methods because their efficiencies depend on the configuration. A preference for one method should never outweigh a shorter exact certificate from another.

The historical archive is a research collection with coverage gaps. Its source-provided proofs are not all independently verified. The present synthesis is based on sixteen reviewed case studies and classical results, not on a claim of having solved every geometry problem from a century of competitions. Theorems and organizational labels introduced here carry no claim of research novelty. Original problem attribution and source-booklet credits remain in the worked volume and ledger.

# The language must be exact

## Points, lines, circles, and directed angles

For distinct points $A,B,C$, define the directed angle $\angle ABC$ modulo $180^\circ$ as the angle from line $BA$ to line $BC$. Modulo $180^\circ$, reversing a ray does not change the line angle. Thus an angle calculation remains valid when an intersection moves from a segment to its extension. Ordinary angles, used for inequalities or a sum of interior angles, still lie in their stated ranges and must not be confused with these residues.

The addition rule is
$$\angle(\ell_1,\ell_3)=\angle(\ell_1,\ell_2)+\angle(\ell_2,\ell_3).$$
Rotations and direct similarities preserve directed angles. Reflections negate them. Two nonparallel lines are perpendicular precisely when their angle is $90^\circ$ modulo $180^\circ$.

**Theorem 1.1 (cyclicity criterion).** Four distinct points, with no relevant collinear triple, are concyclic exactly when $\angle ABC=\angle ADC\pmod {180^\circ}$.

**Proof.** On a circle, both angles subtend the same chord $AC$, so the inscribed-angle theorem gives the equality. Conversely, the circle through $A,B,C$ meets the ray from $D$ toward $C$ in the direction determined by that chord angle; the constant-angle locus of segment $AC$ consists of the two corresponding circular arcs. The angle equality therefore places $D$ on that circle. Equivalently, using coordinates $A=(0,0)$, $C=(1,0)$, the equation of every circle through them is $x^2+y^2-x+vy=0$, and the cotangent of the directed subtended angle determines the same coefficient $v$ for $B$ and $D$.

The coordinate version also proves the converse without an appeal to a diagram. Degenerate collinear points require a line rather than a circle and must be separated before applying the theorem.

## A dependency ledger

When adding a line or circle to a solution, write why it is useful: to transfer one angle, encode one equal distance, or create one power equality. This prevents auxiliary constructions from becoming an unstructured list. In G12, the intended intersection is defined first; two cyclic quadrilaterals are then constructed around it to force the remaining collinearity.

The conclusion itself suggests the certificate:

| Goal | Exact certificate | Cases |
|:--|:--|:--|
| Four points on a circle | Equal chord angles, or equal powers | G04, G12 |
| A point on a perpendicular bisector | Two equal distances, or a fixed reflection | G05, G15 |
| A common tangent at a shared point | Equal tangent–chord angles, or powers equal to a squared distance | G10, G14 |
| Concurrency on an axis | Reflection exchanges the two lines | G02 |
| A fixed ratio of lengths | A chain of similarities or one circle equation | G01, G08, G13 |
| A distance minimum | A fixed circle with a known center | G03 |
| A radius inequality | Containment and homothety | G07 |
| A parallel line | Equal directed angles or equal heights | G11 |

# Similarity is a transport rule

## The triangle similarity certificate

Two triangles are similar if two corresponding angles agree, or if two corresponding side ratios agree and their included angles agree. In the first case, the sine rule gives every remaining side ratio. In the second, scale one triangle so the two sides coincide; the included angle determines the third vertex, proving congruence after scaling.

Record the correspondence explicitly. A ratio such as $AB/DE=AC/DF$ means $A\leftrightarrow D$, $B\leftrightarrow E$, $C\leftrightarrow F$. Many plausible-looking geometry errors are inverted correspondences, not difficult theorems.

**Lemma 2.1 (intersecting-chord ratio).** In a cyclic quadrilateral $PQRS$, let $U=PR\cap QS$ lie inside both diagonals. Then
$$\frac{QU}{US}=\frac{PQ\cdot QR}{PS\cdot SR}.$$

**Proof.** The triangles $PQR$ and $PSR$ share base $PR$. Their areas are in the ratio $QU/US$, because perpendicular distances to $PR$ are proportional along the line $QS$. Their areas are also $PQ\cdot QR\sin\angle PQR/2$ and $PS\cdot SR\sin\angle PSR/2$. The opposite angles of a cyclic quadrilateral are supplementary, so their sines are equal. Equate the two ratios. For exterior intersections use oriented areas and directed ratios, recording their signs.

G08 links this lemma to a similarity between two triangles whose vertices lie on different circles. The remaining expression is a half-angle ratio and hence a ratio of tangent lengths. The chain is short because every intermediate ratio has a specific destination.

## A reusable two-stage pattern

Suppose one similarity yields $U/V=X/Y$ and another yields $R/S=U/V$. The useful auxiliary object is the one realizing the shared ratio $U/V$. In G01, the ratio $MH/MC$ appears both in an orthocenter configuration and in two secants of an auxiliary circle. Once $MI=MH$ is inserted, the target equality follows without further angle chasing.

This suggests a practical search: write the desired length equality as a ratio equal to one; list the ratios naturally available from midpoints, parallels, or cyclicity; then find a similarity that connects the lists. Avoid calculating every angle in the figure.

# Power, radical axes, and tangency

## Power from a quadratic

**Definition.** For a circle with center $O$ and radius $r$, the power of $P$ is $\operatorname{Pow}(P)=|P-O|^2-r^2$. It is positive outside, zero on the circle, and negative inside.

**Theorem 3.1.** If an oriented line through $P$ meets the circle at signed distances $t_1,t_2$, then $t_1t_2=\operatorname{Pow}(P)$. If the line is tangent at $T$, then $PT^2=\operatorname{Pow}(P)$.

**Proof.** Parametrize the line by $P+t\mathbf u$, with $|\mathbf u|=1$. Substitution into the circle equation gives
$$t^2+2\mathbf u\cdot(P-O)t+|P-O|^2-r^2=0.$$
Vieta gives the product of its two roots. A tangent is a double root, whose square is the power. This proof explains both the sign convention and the converse: if a line through a known circle point has its squared distance equal to power, the other intersection coincides with that point.

**Theorem 3.2 (radical axis).** The points of equal power to two nonconcentric circles form a line perpendicular to their line of centers. If the circles share two points, that line is their common chord line. If they are tangent, it is their common tangent.

**Proof.** Subtract the two expressions $|P-O_i|^2-r_i^2$. The quadratic terms cancel, leaving a nonconstant linear equation whose normal vector is $O_2-O_1$. Shared points have zero power to both circles. In the tangent case the line passes through the common point and is perpendicular to the common radius line, hence is the tangent.

For three circles, any finite intersection of two radical axes lies on the third because equality of powers is transitive. This does **not** say that three radical axes always have a finite intersection: parallel or coincident axes can occur. G14 verifies finiteness using the asymmetry $AB>AC$.

## The tangent-transfer certificate

**Proposition 3.3.** Let two distinct circles pass through $K$. If a point $S\ne K$ satisfies
$$\operatorname{Pow}_1(S)=\operatorname{Pow}_2(S)=SK^2,$$
then $SK$ is their common tangent at $K$.

**Proof.** On the line $SK$, each circle has one intersection at signed distance $SK$. The product formula forces the other intersection to have the same distance. Thus both intersections are double, proving tangency.

The nontrivial part is finding $S$. G14 obtains it as the midpoint of a diameter in a fourth cyclic configuration. An auxiliary circle through $H,M,F$ converts a secant product $\overline{SM}\,\overline{SF}$ into a tangent square $SH^2$, while the diameter construction gives $SH=SK$. This is a useful design principle: if the desired tangent is unknown, manufacture a point whose power can be evaluated in two different ways.

![An admissible G14 configuration. The green line SK is the common tangent; the two target circles are blue and ochre.](figures/tangent_transfer.pdf){width=90%}

# Circles as linear equations in a quadratic variable

## Circles through the origin

**Theorem 4.1.** A nondegenerate circle through the vector origin has equation $|\mathbf x|^2=\mathbf u\cdot\mathbf x$ for a nonzero fixed vector $\mathbf u$. Its center is $\mathbf u/2$ and radius $|\mathbf u|/2$.

**Proof.** Complete the square: $|\mathbf x-\mathbf u/2|^2=|\mathbf u|^2/4$. Conversely, a circle through zero has radius equal to the distance of its center from zero and therefore has this form.

**Corollary 4.2.** If $A,C,T$ lie on such a circle and $T=pA+qC$ as vectors, then
$$|T|^2=p|A|^2+q|C|^2.$$
This follows by evaluating the linear functional $\mathbf u\cdot\mathbf x$. The coefficients need not be positive. The identity is conditional on all three points lying on the circle; it is not a general norm identity for arbitrary vectors.

G13 uses the corollary twice. The two circles have the same quadratic part but different linear functionals. The midpoint $M=(A+C)/2$ contributes a factor of one half, and the parallelogram vertex $T=P+Q$ contributes the corresponding full sum. The ratio $BT/BM=\sqrt2$ emerges immediately.

## When coordinates shorten a proof

Choose the origin at a point common to the relevant circles. Put a midpoint or symmetry axis on a coordinate axis. Leave the remaining dimensions symbolic. This preserves the geometric structure and avoids an expansion with six unrelated coordinates.

For example, in G05 the angle bisector is horizontal, so the two sides of the angle have directions $(\cos\theta,\pm\sin\theta)$. Reflection in the perpendicular bisector of $AT$ is then simply $(x,y)\mapsto(t-x,y)$. The calculation is useful because it resolves which of two circle intersections is inside the triangle, an issue that an unqualified symmetry assertion would leave open.

Coordinates are not numerical verification. A proof must retain arbitrary parameters and establish each required identity for every admissible configuration. Numerical plots can catch mistakes but cannot certify a general theorem.

# Reflection, homothety, and fixed points

## Reflection exchanges lines

**Proposition 5.1.** If reflection in a line $\ell$ exchanges two distinct intersecting lines $r,s$, then $r\cap s$ lies on $\ell$.

**Proof.** The reflection sends their unique intersection to the intersection of their images, hence fixes it. The fixed points of a reflection are exactly its axis. If the exchanged lines are parallel, there is no finite intersection; if they coincide, the argument does not identify a unique point.

G02 identifies the axis first as the line of centers of two circles. The equal-radius chord endpoints $F,G$ are exchanged by reflection. One angle identity then shows that their attached lines are exchanged as well. G05 uses the same proposition with the perpendicular bisector of $AT$ as axis.

## Homothety and inradius

**Definition.** A homothety with center $A$ and ratio $t\ne0$ sends $X$ to $A+t(X-A)$. It multiplies all lengths by $|t|$, preserves parallelism, and sends a circle to a circle with radius multiplied by $|t|$.

**Lemma 5.2.** If one triangle is contained in another, its inradius is no larger than the other's.

**Proof.** Its incircle is a disk contained in the larger triangle. If a disk of radius $\rho$ and center $X$ lies inside a triangle of area $\Delta$ and semiperimeter $s$, the perpendicular distances from $X$ to each side are at least $\rho$. Decomposing the area into three triangles gives $\Delta\ge\rho s$, so $\rho\le\Delta/s$, the larger triangle's inradius. This proves the claim without assuming the centers coincide.

The combination of containment and homothety gives G07: two contained triangles similar to $ABC$ have scale factors $AM/AB$ and $MB/AB$, which sum to one. Ceva is used only to select a pair for which the containments hold.

## The incenter half-turn

**Proposition 5.3.** Reflect a vertex $A$ of a tangential angle in the center $I$ of a circle tangent to its two sides. The image $A'=2I-A$ is the intersection of the other two tangents parallel to those sides.

**Proof.** The half-turn about $I$ preserves the circle and maps each tangent to the opposite parallel tangent. Their original intersection is $A$, so the image intersection is $A'$. This constructs both new tangents simultaneously. In G16, a second homothety, centered at $A$ with ratio two, sends the midpoint triangle $KIL$ to $BA'C$. Two auxiliary cyclicities then reduce the target angle sum to the angles of triangle $BA'C$.

# Ceva and the geometry of ratios

## Barycentric coordinates as an elementary proof tool

For a nondegenerate triangle $ABC$, a point with barycentric coordinates $(x:y:z)$ is the vector $(xA+yB+zC)/(x+y+z)$, provided the denominator is nonzero. Multiplying all coordinates by the same nonzero scalar does not change the point. A point on $BC$ has first coordinate zero; for an interior point $D=(0:y:z)$, $BD/DC=z/y$.

**Theorem 6.1 (Ceva for internal cevians).** For interior points $D\in BC$, $E\in CA$, $F\in AB$, the lines $AD,BE,CF$ concur exactly when
$$\frac{BD}{DC}\frac{CE}{EA}\frac{AF}{FB}=1.$$

**Proof.** If their common point has positive coordinates $(x:y:z)$, their traces have coordinates $(0:y:z)$, $(x:0:z)$, $(x:y:0)$, so the product is $(z/y)(x/z)(y/x)=1$. Conversely, choose positive $x,y,z$ realizing the first two ratios. The product condition supplies the third. The point $(x:y:z)$ then lies on all three cevians. This proves sufficiency as well as necessity.

Directed versions allow exterior points but require consistent signs. The internal version is enough for G07. It turns a geometric concurrency into three positive numbers with product one. A cyclic list with product one has a transition from a number at least one to a number at most one; that tiny ordering observation chooses the two triangles that fit.

**Theorem 6.2 (Menelaus, directed form).** Points $D,E,F$ on the three side lines of a triangle, none at a vertex, are collinear exactly when the directed product $BD/DC\cdot CE/EA\cdot AF/FB$ is $-1$.

**Proof.** Write the three homogeneous coordinate rows as $(0,y,z)$, $(u,0,v)$, $(w,t,0)$. Collinearity is equivalent to their determinant being zero, or $yvw+zut=0$. Divide by $yvw$ to obtain $(z/y)(u/v)(t/w)=-1$. The coordinates directly encode the directed ratios, so the equivalence is exact.

Ceva concerns lines through the vertices; Menelaus concerns points on one line. Their similar-looking products should not be memorized without that distinction.

# Spiral similarity and rotation centers

## Complex coordinates with a purpose

Identify the plane with $\mathbb C$. A direct similarity is $z\mapsto qz+b$ with $q\ne0$. If $q\ne1$, its unique center is $t=b/(1-q)$, and the map is $z\mapsto t+q(z-t)$. Its scale is $|q|$ and its rotation angle is $\arg q$. If $|q|=1$ and $q\ne1$, it is a rotation.

Four complex points $z_1,z_2,z_3,z_4$ are concyclic or collinear exactly when
$$\frac{(z_4-z_1)(z_2-z_3)}{(z_4-z_3)(z_2-z_1)}\in\mathbb R,$$
where denominators are nonzero. This is the directed-angle criterion written as an argument of a quotient. One must separately exclude collinearity when a circle is claimed.

## The equal-segment center theorem

**Theorem 7.1.** Let distinct lines $BE$ and $CF$ intersect at $P$, with the named points distinct from $P$ and $B\ne E$, $C\ne F$. The center of the direct similarity sending $B\mapsto C$, $E\mapsto F$ lies on $(PBC)$, allowing that center to equal $P$. If $BE=CF$, that center belongs to both perpendicular bisectors of $BC$ and $EF$.

**Proof.** Put $P=0$, write $B=bu$, $E=eu$, $C=cv$, $F=fv$ with real nonzero scalars and unit complex directions $u,v$. The lines are distinct, so $v/u$ is not real. The similarity multiplier is $q=(f-c)v/((e-b)u)$, which is nonreal and hence not one. Let its center be $T$. Then $C-T=q(B-T)$, giving
$$\frac{T-B}{T-C}\frac CB=\frac1q\frac{cv}{bu}
=\frac{c(e-b)}{b(f-c)}\in\mathbb R.$$
The cyclicity criterion places $T$ on $(PBC)$; if $T=P$, the conclusion is immediate. If $BE=CF$, then $|q|=1$, so $TB=TC$ and $TE=TF$. This proves membership in both perpendicular bisectors. They may coincide when $T=P$, so uniqueness of their intersection is not asserted.

In G15, a congruence proves $BE=CF$ and an angle identity proves $P\in(ABCD)$. The theorem supplies both perpendicular bisectors at once. This is more efficient than constructing their intersection and attempting two unrelated distance calculations.

# Inversion as a controlled change of model

Inversion is not required in the sixteen core solutions, but it extends the same circle-and-tangent strategy to configurations with many circles through one point. It belongs in an advanced toolbox only with its transformation rules proved.

**Definition.** Inversion with center zero and radius $R>0$ maps a nonzero vector $\mathbf x$ to $R^2\mathbf x/|\mathbf x|^2$. It is an involution and satisfies $OX\cdot OX'=R^2$.

**Theorem 8.1.** Inversion maps a circle through its center to a line not through the center; a circle not through the center to another circle; a line not through the center to a circle through the center; and a line through the center to itself, with the center excluded.

**Proof.** Substitute $\mathbf x=R^2\mathbf y/|\mathbf y|^2$ into $|\mathbf x-\mathbf o|^2=r^2$, then multiply by $|\mathbf y|^2$. The image equation is
$$ (|\mathbf o|^2-r^2)|\mathbf y|^2-2R^2\mathbf o\cdot\mathbf y+R^4=0.$$
When the original circle passes through zero, the quadratic coefficient vanishes and the image is a line. Otherwise completing the square gives a circle. Substituting into a line equation $\mathbf u\cdot\mathbf x=c$ gives $c|\mathbf y|^2-R^2\mathbf u\cdot\mathbf y=0$, yielding the remaining cases. The excluded center is handled by the domain, not treated as an ordinary image point.

**Proposition 8.2.** Inversion preserves the magnitude of intersection angles and reverses their orientation; consequently it preserves tangency away from its center.

**Proof.** Its derivative at a nonzero point is the positive scalar $R^2/|\mathbf x|^2$ times $I-2\mathbf e\mathbf e^{\mathsf T}$, where $\mathbf e=\mathbf x/|\mathbf x|$. The latter matrix is reflection in the line perpendicular to $\mathbf e$. It preserves angle magnitudes and reverses orientation. Applying this to tangent directions proves the statement. An elementary proof follows from the similar triangles determined by $OX\cdot OX'=OY\cdot OY'$ and taking secants approaching the tangent.

**Recognition cue.** If three circles all pass through a point, inversion there makes them lines; incidences and tangencies may simplify dramatically. If the main information is a midpoint or a parallelism, inversion may destroy the useful structure. Choose the transformation for what it preserves, not because it is advanced.

# Orthocenter and incenter configurations

## Two orthocenter facts with proofs

**Lemma 9.1.** The reflection of the orthocenter $H$ of an acute triangle in a side lies on the circumcircle.

**Proof.** For side $BC$, the altitudes give $\angle BHC=180^\circ-A$. Reflection in $BC$ preserves this ordinary angle and places the image on the opposite side of $BC$ from $A$. The opposite angles then sum to $180^\circ$, proving cyclicity. Directed angles extend the statement to nondegenerate obtuse configurations with the appropriate point order.

**Lemma 9.2.** If $A'$ is the antipode of $A$ on the circumcircle and $M$ is the midpoint of $BC$, then $H,M,A'$ are collinear and $M$ is the midpoint of $HA'$.

**Proof.** The semicircle angles give $BA'\perp BA$ and $CA'\perp CA$. The altitudes give $CH\perp BA$ and $BH\perp CA$. Thus $BHCA'$ is a parallelogram, whose diagonals $BC$ and $HA'$ bisect each other. These two lemmas supply the missing setup of the difficult tangency problem G14.

## The incenter arc midpoint

**Lemma 9.3.** If $T$ is the midpoint of the arc $BC$ not containing $A$, then $A,I,T$ are collinear and $TB=TC=TI$.

**Proof.** Equal arcs imply $AB$ and $AC$ make equal angles with $AT$, so it is the internal bisector. The incenter lies on it between $A$ and $T$. Equal chords give $TB=TC$. In triangle $BIT$, the angle at $B$ is $A/2+B/2$, while the angle at $I$ is $180^\circ-\angle BIA=90^\circ-C/2=(A+B)/2$. Therefore $TB=TI$.

The circle $(BCI)$ thus has a center on $AI$. G03 combines this with a constant-angle locus and the triangle inequality. Memorizing the conclusion without its hypotheses would be dangerous: the other arc midpoint corresponds to external angle-bisector geometry and a different point order.

# Transfer workshop

## Exercises

1. Prove that two distinct circles cannot have more than two common points.
2. Two circles meet at $A,B$. A line through $P$ meets the first at $X,Y$ and the second at $U,V$. Prove that $P\in AB$ exactly when the directed products $PX\cdot PY$ and $PU\cdot PV$ agree.
3. A reflection exchanges $A,T$ and sends $M,N$ to $X,Y$. If $MN$ and $XY$ are distinct and intersect, prove their intersection is equidistant from $A,T$.
4. With $B$ at the origin, let $A,C,T$ lie on a circle and $T=pA+qC$. Derive the norm identity in Corollary 4.2 directly from a completed square.
5. For an interior point $M$ on $AB$, draw parallels through $M$ to $BC$ and $AC$, making triangles similar to $ABC$ at $A$ and $B$. Show their inradii sum to that of $ABC$.
6. Prove the intersecting-chord ratio lemma using areas, and identify where cyclicity is used.
7. Let $B=(1,0)$, $E=(3,0)$, $C=(0,2)$, $F=(0,4)$. Find the center of the rotation $B\mapsto C$, $E\mapsto F$, and verify it lies on $(0BC)$.
8. Under inversion of radius two centered at the origin, find the image of $x^2+y^2-4x=0$.
9. Prove that the largest disk contained in a triangle has radius $\Delta/s$, even when its center is not initially assumed to be the incenter.
10. Given positive numbers $a,b,c$ with $abc=1$, prove that some cyclic adjacent pair has first component at least one and second at most one. Explain how this selects the pair in G07.
11. Show that the circle with diameter $HM$, where $F$ is the perpendicular projection of $H$ onto a line through $M$, has tangent at $H$ perpendicular to $HM$ and contains $F$.
12. Let $S$ have equal power to two circles meeting at $K$, and suppose one tangent from $S$ touches the first circle at $K$. Prove it is tangent to the second at $K$.

## Solutions

1. Their equal-power locus is a line, and substitution of a line parameter into a circle equation gives a quadratic with at most two roots. Concentric distinct circles have no common points.
2. Both products are the corresponding powers. Their equality is precisely membership in the radical axis, which is $AB$.
3. The reflection exchanges the two lines, so fixes their intersection. Its axis is the perpendicular bisector of $AT$; apply Proposition 5.1.
4. Write the circle as $|X-O|^2=|O|^2$, or $|X|^2=2O\cdot X$. Evaluate at $A,C,T$ and use the linear expression for $T$.
5. The similarity ratios are $AM/AB$ and $MB/AB$. Inradius scales by these factors, whose sum is one.
6. Compute $[PQR]/[PSR]$ first by the common base $PR$, then by two sides and included angle. Cyclicity makes the two included sines equal. Without it, the formula contains an additional sine ratio.
7. In complex notation the map is $z\mapsto iz+i$. Its center solves $t=it+i$, so $t=(-1+i)/2$. Thus $T=(-1/2,1/2)$. The circle through $(0,0),(1,0),(0,2)$ is $x^2+y^2-x-2y=0$, which $T$ satisfies. Its distances to $B,C$ agree, as do those to $E,F$.
8. Substitute $x=4u/(u^2+v^2)$, $y=4v/(u^2+v^2)$. The equation reduces to $u=1$. The original circle passes through the inversion center, which has no finite image.
9. A contained disk of radius $\rho$ gives $\Delta\ge\rho s$ by the three area decomposition. The incenter has equal distances $\Delta/s$ from all sides, so the bound is attained.
10. If not all are one, some exceeds one and some is below one. Following the cyclic order from an above-one entry, the first transition to a below-one entry provides the pair; entries equal to one can be included in either category. The products then give the containment inequalities in G07.
11. The angle $HFM$ is right, so $F$ lies on the diameter circle. Its radius at $H$ is parallel to $HM$, proving the tangent direction. This is the auxiliary circle in G14.
12. The tangent gives $SK^2=\operatorname{Pow}_1(S)$. Equal power gives the same equation for the second circle, and the secant quadratic has a double intersection at $K$.

# An eight-week geometry seminar

| Week | Focus | Cases | Required reconstruction |
|:--|:--|:--|:--|
| 1 | Directed angles and correspondence | G01, G06 | Name every similarity correspondence |
| 2 | Reflection and cyclicity | G02, G04, G05 | Specify the axis and prove the image claim |
| 3 | Incenter loci and distances | G03, G16 | Derive the arc-midpoint lemma |
| 4 | Ceva, containment, and radii | G07, G09 | Locate the hidden triangle |
| 5 | Ratio chains and tangents | G08, G10 | Close the chain without a diagram assumption |
| 6 | Equal heights and auxiliary circles | G11, G12 | Define the target intersection first |
| 7 | Circle equations and rotations | G13, G15 | Solve by a symbolic coordinate certificate |
| 8 | Radical axes and tangent transfer | G14 | Reconstruct the entire auxiliary setup |

After solving a problem, draw a second admissible configuration with a different shape. Identify which steps depend only on directed angles and which depend on an ordinary point order. Then rewrite the proof as a short dependency chain: hypotheses, auxiliary object, certificate, conclusion. Shortness should come from eliminating redundant work, while preserving every essential justification.

# Attribution and limits {.unnumbered}

Primary contest archive: https://www.imo-official.org/problems/ . The source records were retrieved from https://mathnet.mit.edu/ ; their booklet authors, editors, organizations and rights fields are preserved in `audit/source_ledger.jsonl`. The companion worked volume identifies every historical problem. Classical results retain their established names. This book does not claim an exhaustive taxonomy of geometry or external peer review; the coverage report distinguishes checked expositions, source-provided proofs, figure-dependent records and unavailable source texts.
