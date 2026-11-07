# jpn_2008_fcdcf8

JMO | Japan | 2008 | Final | 3

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2008_fcdcf8](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_fcdcf8.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: Japan Mathematical Olympiad
- Subtitle: The 18 Japanese Mathematical Olympiad: The First Round, The Final Round And The 6 Japanese Junior Mathematical Olympiad
- Year: 2008
- Organization: The Mathematical Olympiad Foundation of Japan
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let us denote by $(XYZ)$ the directed angle determined by the 3 points $X, Y, Z$. More precisely, we set $(XYZ)$ to be equal to $\alpha$ if the line $XY$ comes on top of the line $YZ$ when $XY$ is rotated around $Y$ counterclockwise by $\alpha$ degrees. When an integral multiple of $180^\circ$ is added to such an $\alpha$, the same condition on the line $XY$ will be satisfied, so, in the sequel we identify two values differing by an integral multiple of $180^\circ$, when we refer to directed angles. Let us prove the following simple lemma.

**Lemma.** If four distinct points $X, Y, Z, W$ lie on the circumference of a same circle, then $(XZY) = (XWY)$ holds.

**Proof.** The circumference of the circle are divided into 2 disjoint arcs by the points $X, Y$. If the 2 points $Z, W$ lie on a same arc given by this division, then by the well-known theorem on inscribed angles, we have $\angle XZY = \angle XWY$, and since these angles have the same direction, we have $(XZY) = (XWY)$ in this case. On the other hand, if $Z$ and $W$ lie on different arcs, from a well-known property of a quadrilateral inscribed in a circle, we can conclude that $\angle XZY = 180^\circ - \angle XWY$. Since the direction of these angles are reversed in this situation, we have $(XZY) = 180^\circ - (-(XWY)) = (XWY)$ in this case also.

Let us denote by $M, N$ the midpoints of the sides $AB$ and $AC$ of the triangle $ABC$, respectively. From the fact that $OM \perp AM, ON \perp AN$ it follows that the four points $A, O, M, N$ lie on the circumference of a same circle, and hence by Lemma, we have $(MON) = (MAN)$. Since $A, O, P, Q$ also lie on the circumference of a same circle, we also have $(POQ) = (PAQ)$. Furthermore, since the three points $A, P, M$ lie on a same line and so do the three points $A, Q, N$, we have $(MAN) = (PAQ)$, and therefore, we conclude that $(MON) = (POQ)$, from which we obtain $(MOP) = (MON) - (PON) = (POQ) - (PON) = (NOQ)$.

If we denote by $B'$ the point situated symmetrically to the point $B$ with respect to the point $P$, then we have $\vec{AB}' = 2\vec{MP}$ since $\vec{BA} = 2\vec{BM}$ and $\vec{BB}' = 2\vec{BP}$ hold. Similarly, if we let $C'$ be the point situated symmetrically to the point $C$ with respect to the point $Q$, then we have $\vec{AC}' = 2\vec{NQ}$.

Since $\vec{MP} \cdot (\vec{NQ})$ coincides with the vector obtained by rotating $\vec{OM} \cdot (\vec{ON})$, respectively counterclockwise by $90^\circ$ and multiplied by $\tan(MOP)\ (= \tan(NOQ))$, we can conclude that $\vec{AB}' \cdot (\vec{AC}')$ coincides with the vector obtained by rotating $\vec{OM} \cdot (\vec{ON})$, respectively counterclockwise by $90^\circ$ and multiplied by $2\tan(MOP)$. Therefore, $\vec{B'C}'$ coincides with the vector obtained by rotating $\vec{MN}$ counterclockwise by $90^\circ$ and multiplied by $2\tan(MOP)$. In particular, we have $\vec{B'C}' \perp \vec{BC}$, since $\vec{MN} \parallel \vec{MN}$.

Denote by $H$ the point of intersection of the lines $B'C'$ and $BC$, and let $P'(Q')$ be the foot of the perpendicular line drawn from $P(Q)$, respectively, to the line $BC$. Then, since $P'(Q')$, respectively, is the midpoint of the line segment $HB(HC$, respectively), we have $P'Q' = \frac{1}{2}BC = \frac{1}{2}PQ$.

If we let $\theta$ be the angle formed by the lines $PQ$ and $BC$ ($0^\circ \le \theta \le 90^\circ$ and $\theta = 0$ if the two lines are parallel), then we see that $P'Q' = PQ \cos \theta$ holds so that we get $\cos \theta = \frac{1}{2}$ and therefore, $\theta = 60^\circ$.
