# irn_2015_b3bad7

IranMO | Iran | 2015 | Third Round | 2

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [irn_2015_b3bad7](https://mathnet.mit.edu/data_v2/full/iran/irn_2015_b3bad7.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Iran

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We claim that it is possible to roll the polyhedron in each direction, as far as we want.
Firstly, we draw a line from a point inside the face of polyhedron touching the ground to the destination point. Since the polyhedron is convex, this line intersects one of edges of that face. We can roll the polyhedron around this edge. After this motion, the distance from the destination point and the intersection of polygon and the ground became smaller. We can continue the same process to get the destination point. To this end, we should prove that there is some positive number $\epsilon$ such that after each motion our distance will be decrease at least by $\epsilon$. In the other words, if we denote our distance after $n$-th step by $d_n$, the sequence $d_n - d_{n-1}$ has a lower bound or equivalently cannot tend to zero. If this sequence tends to zero, we deduce that the polyhedron has been rolled around some edge connecting to a single vertex (after some step), infinitely many times.

**Lemma 1.** We can roll the polyhedron around one of its vertices at most *n* times, where *n* is the number of edges connecting to that vertex.
*Proof.* Look at the trace of the line (on the ground) on the polyhedron. If we open the polyhedron, the trace became a straight line. Since a line in the plane intersect each convex polygon at most once, we deduce that during the motions around each vertex each face containing that vertex touches the ground at most once. □

Reffering to the lemma, we infer that $d_n - d_{n-1}$ cannot tend to zero and so we will get our destination point. This shows that if there is no canyon we can get everywhere in the plane.

Now for the case that we have a bridge, we can connect the initial point and the center of cavity by a broken line. So using above method we can roll the polyhedron on this path to drop into the cavity.
