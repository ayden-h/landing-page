# imo_2013_eb8b9e

IMO-SL | IMO | 2013 | Combinatorics | C2

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2013_eb8b9e](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_eb8b9e.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems with Solutions
- Year: 2013
- Editors: Ardila, Federico; Bogdanov, Ilya I.; Kós, Géza; Moreira, Carlos Gustavo Tamm de Araújo; Reiher, Christian
- Organization: International Mathematical Olympiad
- Place: Santa Marta, Colombia
- Series: International Mathematical Olympiad
- Volume: 54th
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Answer. $k=2013$.

Firstly, let us present an example showing that $k \geqslant 2013$. Mark 2013 red and 2013 blue points on some circle alternately, and mark one more blue point somewhere in the plane. The circle is thus split into 4026 arcs, each arc having endpoints of different colors. Thus, if the goal is reached, then each arc should intersect some of the drawn lines. Since any line contains at most two points of the circle, one needs at least $4026 / 2=2013$ lines.

It remains to prove that one can reach the goal using 2013 lines. First of all, let us mention that for every two points $A$ and $B$ having the same color, one can draw two lines separating these points from all other ones. Namely, it suffices to take two lines parallel to $A B$ and lying on different sides of $A B$ sufficiently close to it: the only two points between these lines will be $A$ and $B$.

Now, let $P$ be the convex hull of all marked points. Two cases are possible.

Case 1. Assume that $P$ has a red vertex $A$. Then one may draw a line separating $A$ from all the other points, pair up the other 2012 red points into 1006 pairs, and separate each pair from the other points by two lines. Thus, 2013 lines will be used.

Case 2. Assume now that all the vertices of $P$ are blue. Consider any two consecutive vertices of $P$, say $A$ and $B$. One may separate these two points from the others by a line parallel to $A B$. Then, as in the previous case, one pairs up all the other 2012 blue points into 1006 pairs, and separates each pair from the other points by two lines. Again, 2013 lines will be used.

## Supplied solution 2

If $n$ points in the plane, no three of which are collinear, are colored in red and blue arbitrarily, then it suffices to draw $\lfloor n / 2\rfloor$ lines to reach the goal.

We proceed by induction on $n$. If $n \leqslant 2$ then the statement is obvious. Now assume that $n \geqslant 3$, and consider a line $\ell$ containing two marked points $A$ and $B$ such that all the other marked points are on one side of $\ell$; for instance, any line containing a side of the convex hull works.

Remove for a moment the points $A$ and $B$. By the induction hypothesis, for the remaining configuration it suffices to draw $\lfloor n / 2\rfloor-1$ lines to reach the goal. Now return the points $A$ and $B$ back. Three cases are possible.

Case 1. If $A$ and $B$ have the same color, then one may draw a line parallel to $\ell$ and separating $A$ and $B$ from the other points. Obviously, the obtained configuration of $\lfloor n / 2\rfloor$ lines works.

Case 2. If $A$ and $B$ have different colors, but they are separated by some drawn line, then again the same line parallel to $\ell$ works.

Case 3. Finally, assume that $A$ and $B$ have different colors and lie in one of the regions defined by the drawn lines. By the induction assumption, this region contains no other points of one of the colors - without loss of generality, the only blue point it contains is $A$. Then it suffices to draw a line separating $A$ from all other points.

Thus the step of the induction is proved.

