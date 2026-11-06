# Reusable results from the supplemental 2026 audit

The 16 newly written solutions are complete; all 50 stored alternatives were read. The 14 existing combinatorics records were reused unchanged. Sixteen independent exact checks pass. The two documented statement variants are 2026-II-01 (eleventh-term sum 196 versus tenth-term sum 178) and 2026-II-10 (maximum 340 versus sum 850).

## Equiangular pentagon identity — 2026-I-14

For any convex equiangular pentagon, let $P$ be its perimeter, $S$ the sum of its squared side lengths, and $D$ the sum of its squared diagonal lengths. Then

$$P^2=\sqrt5\,(2D-3S).$$

Proof: put $\phi=(1+\sqrt5)/2$, $J=\sum a_i a_{i+1}$, and $K=\sum a_i a_{i+2}$, using cyclic indices. Squared diagonal lengths give $D=2S+J/\phi$. Closure of the five edge vectors gives $0=S+J/\phi-\phi K$. Therefore $J=\phi(D-2S)$, $K=(D-S)/\phi$, and substitution in $P^2=S+2J+2K$ gives the formula. The closure equation is essential: the requested radical format cannot justify guessing a missing product sum.

## Radii between two tangent planes are affine — 2026-I-12

Suppose spheres of positive radii touch $z=0$ at $(x_i,y_i,0)$ from above and touch another, distinct plane on a common side. Their radii satisfy $r_i=ax_i+by_i+c$ for some affine function. To see this, orient the other plane's unit normal $(A,B,C)$ so the signed center distance is the radius. Its equation becomes $Ax_i+By_i+(C-1)r_i+D=0$. The coefficient $C-1$ cannot vanish unless the two planes coincide.

Conversely, any positive radii given by $r_i=ax_i+by_i+c$ have such a second common tangent plane. Put $q=a^2+b^2$ and use the plane

$$2ax+2by+(q-1)z+2c=0.$$

Its normal has length $q+1$, and substitution of $(x_i,y_i,r_i)$ gives signed distance $r_i$. Thus three noncollinear contact points determine the affine radius function, and any fourth radius follows by planar affine interpolation. This is stronger and more useful than merely asserting that the centers are coplanar.

## Exactly seven signed sums — 2026-II-11

Let $a,b,c$ be nonzero complex numbers. Their eight signed sums form exactly seven distinct values if and only if signs can be chosen so that $a+b+c=0$ and the three chosen numbers are pairwise unequal even up to sign.

Necessity: the sum set is closed under negation; odd cardinality forces zero. After choosing that zero-sum orientation, every signed sum is in $\{0,\pm2a,\pm2b,\pm2c\}$. Seven distinct values require the stated noncollision conditions. Sufficiency follows from that same explicit set. This separates the involution argument from the Vieta algebra and also proves attainment instead of only producing candidate parameters.

## Repeating-denominator series require a carry estimate — 2026-II-09

For an integer base $b\ge2$,

$$\sum_{k\ge1}\frac1{b^k-1}=\sum_{m\ge1}\tau(m)b^{-m}.$$

This follows by expanding geometric series and regrouping nonnegative terms. The coefficients on the right are uncarried digits; they need not be less than the base. To extract a block through position $N$, bound the whole tail $\sum_{j\ge1}\tau(N+j)b^{-j}$, not merely its first coefficient. In the present problem the bound $2/10+\sum_{j\ge2}(20+j)10^{-j}=361/810<1$ proves that no carry reaches position 100. Both stored alternatives omitted this justification.

## Isosceles perimeter ratio determines the shape — 2026-II-08

For a nondegenerate isosceles triangle with base $2x$, equal side $L$, and incenter distance $u$ from either base vertex, put $t=u/x$. Then $1<t<\sqrt2$ and

$$\frac Lx=\frac{t^2}{2-t^2},\qquad
\frac{\operatorname{perimeter}(ABC)}{\operatorname{perimeter}(AIC)}=
\frac2{(2-t^2)(t+1)}.$$

The last expression increases strictly from 1 to infinity on this interval: the derivative of its denominator is $2-2t-3t^2<0$. Hence every ratio greater than one determines a unique shape. Once the ratio gives rational side proportions, the least integral instance is a denominator-divisibility question; a guessed working triangle does not prove minimality.
