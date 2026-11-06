# imo_2020_c1c2cc

IMO-SL | IMO | 2020 | Combinatorics | C2

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2020_c1c2cc](https://mathnet.mit.edu/data_v2/full/imo/imo_2020_c1c2cc.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Call a quadrilateral skew-colored, if it has three corners of one color and one corner of the other color. We will prove the following

Claim. If the vertices of a convex $(4k+1)$-gon $P$ are colored black and white such that each color is used at least $k$ times, then there exist $k$ pairwise disjoint skew-colored quadrilaterals whose vertices are vertices of $P$. (One vertex of $P$ remains unused.)

The problem statement follows by removing 3 arbitrary vertices of the 100-gon and applying the Claim to the remaining 97 vertices with $k=24$.

Proof of the Claim. We prove by induction. For $k=1$ we have a pentagon with at least one black and at least one white vertex. If the number of black vertices is even then remove a black vertex; otherwise remove a white vertex. In the remaining quadrilateral, there are an odd number of black and an odd number of white vertices, so the quadrilateral is skew-colored.

For the induction step, assume $k \geqslant 2$. Let $b$ and $w$ be the numbers of black and white vertices, respectively; then $b, w \geqslant k$ and $b+w=4k+1$. Without loss of generality we may assume $w \geqslant b$, so $k \leqslant b \leqslant 2k$ and $2k+1 \leqslant w \leqslant 3k+1$.

We want to find four consecutive vertices such that three of them are white, the fourth one is black. Denote the vertices by $V_{1}, V_{2}, \ldots, V_{4k+1}$ in counterclockwise order, such that $V_{4k+1}$ is black, and consider the following $k$ groups of vertices:

$$
\left(V_{1}, V_{2}, V_{3}, V_{4}\right),\left(V_{5}, V_{6}, V_{7}, V_{8}\right), \ldots,\left(V_{4k-3}, V_{4k-2}, V_{4k-1}, V_{4k}\right)
$$

In these groups there are $w$ white and $b-1$ black vertices. Since $w > b-1$, there is a group, $\left(V_{i}, V_{i+1}, V_{i+2}, V_{i+3}\right)$ that contains more white than black vertices. If three are white and one is black in that group, we are done. Otherwise, if $V_{i}, V_{i+1}, V_{i+2}, V_{i+3}$ are all white then let $V_{j}$ be the first black vertex among $V_{i+4}, \ldots, V_{4k+1}$ (recall that $V_{4k+1}$ is black); then $V_{j-3}, V_{j-2}$ and $V_{j-1}$ are white and $V_{j}$ is black.

Now we have four consecutive vertices $V_{i}, V_{i+1}, V_{i+2}, V_{i+3}$ that form a skew-colored quadrilateral. The remaining vertices form a convex $(4k-3)$-gon; $w-3$ of them are white and $b-1$ are black. Since $b-1 \geqslant k-1$ and $w-3 \geqslant (2k+1)-3 > k-1$, we can apply the Claim with $k-1$.

