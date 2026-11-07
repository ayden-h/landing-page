# jpn_2012_b90bde

JMO | Japan | 2012 | Final Round | 4

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2012_b90bde](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_b90bde.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: The 22nd Japanese Mathematical Olympiad and The 10th Japanese Junior Mathematical Olympiad
- Year: 2012
- Organization: The Mathematical Olympiad Foundation of Japan
- Series: Japan Mathematical Olympiad
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Given a circle $S$ and a point $Z$ in the plane, we define the power $p = p_S(Z)$ of $Z$ with reference to $S$ in the following way: Let $p = 0$ if the point $Z$ lies on the circumference of $S$. Otherwise draw a line through $Z$ and intersecting at the points $I_1$ and $I_2$ with the circle $S$. Then, $p = p_S(Z) = -ZI_1 \cdot ZI_2$ if $Z$ lies in the interior of $S$, and $= ZI_1 \cdot ZI_2$ if $Z$ lies in the exterior of $S$. Here we are considering the line segments $ZI_1, ZI_2$ to be directed. A well-known theorem (called the theorem on the power of a point) tells us that the value of the power $p$ of $Z$ w.r.t. the circle $S$ is independent of the choice of the line going through it and intersecting the circle $S$, and it is easy to give a proof of this theorem using the fact that angles subtended by an arc of a circle at any pair of points lying on the circle have the same magnitude and similarity of ensuing triangles. Also by considering the line going through $Z$ and the center $O$ of the circle $S$, we see that $p = ZO^2 - r^2$ holds, where $r$ is the radius of $S$.

Now going back to the problem, we see, from $PA \cdot PC - PB \cdot PD = 0$ and the fact that both of the points $X, Y$ lie on both of the circles $S_1, S_2$, that each of the three points $P, X, Y$ satisfies the following:
$$
p_{S_1}(\text{of the point}) + p_{S_2}(\text{of the point}) = 0 \quad (*)
$$
Let $r_i$ be the radius of the circle $S_i$ and $O_i$ be the center of $S_i$, ($i = 1, 2$), and denote by $M$ the mid-point of the line segment $O_1O_2$. Now for a point $Z$ on the plane note that the following statements are valid:
$$
\begin{align*}
Z \text{ satisfies the condition } (*) &\iff (ZO_1^2 - r_1^2) + (ZO_2^2 - r_2^2) = 0 \\
&\iff (ZO_1^2 + ZO_2^2) = r_1^2 + r_2^2 \\
&\iff 2(MO_1^2 + ZM^2) = r_1^2 + r_2^2 \\
&\iff ZM^2 = \frac{1}{2}(r_1^2 + r_2^2) - MO_1^2.
\end{align*}
$$
Since the right-hand side of the last identity above is independent on $Z$ we conclude that every point in the plane satisfying the condition (*) lies on the circumference of a same circle. In particular, $M$ coincides with the orthocenter of the triangle $PXY$.
