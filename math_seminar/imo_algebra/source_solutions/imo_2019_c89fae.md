# imo_2019_c89fae

IMO-SL | IMO | 2019 | Algebra | A6

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2019_c89fae](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_c89fae.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems
- Subtitle: with solutions
- Year: 2019
- Editors: Gardiner, Tony; Crane, Edward; Betts, Alexander; Cranch, James; Myers, Joseph; Aaronson, James; Carlotti, Andrew; Kós, Géza; Bogdanov, Ilya I.; Shotton, Jack
- Organization: 60th International Mathematical Olympiad
- Place: Bath, United Kingdom
- Series: International Mathematical Olympiad
- Volume: 60th
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Solution 1. In the first two steps, we deal with any polynomial $P(x, y, z)$ satisfying $P(x, y, z) = P(x, y, x y - z)$. Call such a polynomial weakly symmetric, and call a polynomial satisfying the full conditions in the problem symmetric.

Step 1. We start with the description of weakly symmetric polynomials. We claim that they are exactly the polynomials in $x, y$, and $z(x y - z)$. Clearly, all such polynomials are weakly symmetric. For the converse statement, consider $P_{1}(x, y, z) := P\left(x, y, z + \frac{1}{2} x y\right)$, which satisfies $P_{1}(x, y, z) = P_{1}(x, y, -z)$ and is therefore a polynomial in $x, y$, and $z^{2}$. This means that $P$ is a polynomial in $x, y$, and $\left(z - \frac{1}{2} x y\right)^{2} = -z(x y - z) + \frac{1}{4} x^{2} y^{2}$, and therefore a polynomial in $x, y$, and $z(x y - z)$.

Step 2. Suppose that $P$ is weakly symmetric. Consider the monomials in $P(x, y, z)$ of highest total degree. Our aim is to show that in each such monomial $\mu x^{a} y^{b} z^{c}$ we have $a, b \geqslant c$. Consider the expansion
$$
P(x, y, z) = \sum_{i, j, k} \mu_{i j k} x^{i} y^{j} (z(x y - z))^{k} \tag{1.1}
$$
The maximal total degree of a summand in (1.1) is $m = \max_{i, j, k: \mu_{i j k} \neq 0}(i + j + 3k)$. Now, for any $i, j, k$ satisfying $i + j + 3k = m$ the summand $\mu_{i, j, k} x^{i} y^{j} (z(x y - z))^{k}$ has leading term of the form $\mu x^{i + k} y^{j + k} z^{k}$. No other nonzero summand in (1.1) may have a term of this form in its expansion, hence this term does not cancel in the whole sum. Therefore, $\operatorname{deg} P = m$, and the leading component of $P$ is exactly
$$
\sum_{i + j + 3k = m} \mu_{i, j, k} x^{i + k} y^{j + k} z^{k}
$$
and each summand in this sum satisfies the condition claimed above.

Step 3. We now prove the problem statement by induction on $m = \operatorname{deg} P$. For $m = 0$ the claim is trivial. Consider now a symmetric polynomial $P$ with $\operatorname{deg} P > 0$. By Step 2, each of its monomials $\mu x^{a} y^{b} z^{c}$ of the highest total degree satisfies $a, b \geqslant c$. Applying other weak symmetries, we obtain $a, c \geqslant b$ and $b, c \geqslant a$; therefore, $P$ has a unique leading monomial of the form $\mu(x y z)^{c}$. The polynomial $P_{0}(x, y, z) = P(x, y, z) - \mu\left(x y z - x^{2} - y^{2} - z^{2}\right)^{c}$ has smaller total degree. Since $P_{0}$ is symmetric, it is representable as a polynomial function of $x y z - x^{2} - y^{2} - z^{2}$. Then $P$ is also of this form, completing the inductive step.


Solution 2. We will rely on the well-known identity
$$
\cos^{2} u + \cos^{2} v + \cos^{2} w - 2 \cos u \cos v \cos w - 1 = 0 \quad \text{whenever} \ u + v + w = 0. \tag{2.1}
$$
Claim 1. The polynomial $P(x, y, z)$ is constant on the surface
$$
\mathfrak{S} = \{(2 \cos u, 2 \cos v, 2 \cos w): u + v + w = 0\}
$$
Proof. Notice that for $x = 2 \cos u, y = 2 \cos v, z = 2 \cos w$, the Vieta jumps $x \mapsto y z - x$, $y \mapsto z x - y, z \mapsto x y - z$ in ( $*$ ) replace ( $u, v, w$ ) by ( $v - w, -v, w$ ), ( $u, w - u, -w$ ) and ( $-u, v, u - v$ ), respectively. For example, for the first type of jump we have
$$
y z - x = 4 \cos v \cos w - 2 \cos u = 2 \cos (v + w) + 2 \cos (v - w) - 2 \cos u = 2 \cos (v - w).
$$
Define $G(u, v, w) = P(2 \cos u, 2 \cos v, 2 \cos w)$. For $u + v + w = 0$, the jumps give
$$
\begin{aligned}
G(u, v, w) & = G(v - w, -v, w) = G(w - v, -v, (v - w) - (-v)) = G(-u - 2v, -v, 2v - w) \\
& = G(u + 2v, v, w - 2v)
\end{aligned}
$$
By induction,
$$
G(u, v, w) = G(u + 2k v, v, w - 2k v) \quad (k \in \mathbb{Z}). \tag{2.2}
$$
Similarly,
$$
G(u, v, w) = G(u, v - 2\ell u, w + 2\ell u) \quad (\ell \in \mathbb{Z}). \tag{2.3}
$$
And, of course, we have
$$
G(u, v, w) = G(u + 2p \pi, v + 2q \pi, w - 2(p + q) \pi) \quad (p, q \in \mathbb{Z}) \tag{2.4}
$$
Take two nonzero real numbers $u, v$ such that $u, v$ and $\pi$ are linearly independent over $\mathbb{Q}$. By combining (2.2-2.4), we can see that $G$ is constant on a dense subset of the plane $u + v + w = 0$. By continuity, $G$ is constant on the entire plane and therefore $P$ is constant on $\mathfrak{S}$.

Claim 2. The polynomial $T(x, y, z) = x^{2} + y^{2} + z^{2} - x y z - 4$ divides $P(x, y, z) - P(2,2,2)$.
Proof. By dividing $P$ by $T$ with remainders, there exist some polynomials $R(x, y, z), A(y, z)$ and $B(y, z)$ such that
$$
P(x, y, z) - P(2,2,2) = T(x, y, z) \cdot R(x, y, z) + A(y, z) x + B(y, z). \tag{2.5}
$$
On the surface $\mathfrak{S}$ the LHS of (2.5) is zero by Claim 1 (since $(2,2,2) \in \mathfrak{S}$ ) and $T = 0$ by (2.1). Hence, $A(y, z) x + B(y, z)$ vanishes on $\mathfrak{S}$.
Notice that for every $y = 2 \cos v$ and $z = 2 \cos w$ with $\frac{\pi}{3} < v, w < \frac{2\pi}{3}$, there are two distinct values of $x$ such that $(x, y, z) \in \mathfrak{S}$, namely $x_{1} = 2 \cos (v + w)$ (which is negative), and $x_{2} = 2 \cos (v - w)$ (which is positive). This can happen only if $A(y, z) = B(y, z) = 0$. Hence, $A(y, z) = B(y, z) = 0$ for $|y| < 1, |z| < 1$. The polynomials $A$ and $B$ vanish on an open set, so $A$ and $B$ are both the zero polynomial.
The quotient $(P(x, y, z) - P(2,2,2)) / T(x, y, z)$ is a polynomial of lower degree than $P$ and it also satisfies (*). The problem statement can now be proven by induction on the degree of $P$.


Solution 3 (using algebraic geometry, just for interest). Let $Q = x^{2} + y^{2} + z^{2} - x y z$ and let $t \in \mathbb{C}$. Checking where $Q - t, \frac{\partial Q}{\partial x}, \frac{\partial Q}{\partial y}$ and $\frac{\partial Q}{\partial z}$ vanish simultaneously, we find that the surface $Q = t$ is smooth except for the cases $t = 0$, when the only singular point is $(0,0,0)$, and $t = 4$, when the four points $(\pm 2, \pm 2, \pm 2)$ that satisfy $x y z = 8$ are the only singular points. The singular points are the fixed points of the group $\Gamma$ of polynomial automorphisms of $\mathbb{C}^{3}$ generated by the three Vieta involutions
$$
\iota_{1}: (x, y, z) \mapsto (x, y, x y - z), \quad \iota_{2}: (x, y, z) \mapsto (x, x z - y, z), \quad \iota_{3}: (x, y, z) \mapsto (y z - x, y, z).
$$
$\Gamma$ acts on each surface $\mathcal{V}_{t}: Q - t = 0$. If $Q - t$ were reducible then the surface $Q = t$ would contain a curve of singular points. Therefore $Q - t$ is irreducible in $\mathbb{C}[x, y, z]$. (One can also prove algebraically that $Q - t$ is irreducible, for example by checking that its discriminant as a quadratic polynomial in $x$ is not a square in $\mathbb{C}[y, z]$, and likewise for the other two variables.) In the following solution we will only use the algebraic surface $\mathcal{V}_{0}$.
Let $U$ be the $\Gamma$-orbit of $(3,3,3)$. Consider $\iota_{3} \circ \iota_{2}$, which leaves $z$ invariant. For each fixed value of $z$, $\iota_{3} \circ \iota_{2}$ acts linearly on $(x, y)$ by the matrix
$$
M_{z} := \begin{pmatrix}
z^{2} - 1 & -z \\
z & -1
\end{pmatrix}
$$
The reverse composition $\iota_{2} \circ \iota_{3}$ acts by $M_{z}^{-1} = M_{z}^{\text{adj}}$. Note $\operatorname{det} M_{z} = 1$ and $\operatorname{tr} M_{z} = z^{2} - 2$. When $z$ does not lie in the real interval $[-2, 2]$, the eigenvalues of $M_{z}$ do not have absolute value 1, so every orbit of the group generated by $M_{z}$ on $\mathbb{C}^{2} \setminus \{(0,0)\}$ is unbounded. For example, fixing $z = 3$ we find $(3 F_{2k+1}, 3 F_{2k-1}, 3) \in U$ for every $k \in \mathbb{Z}$, where $(F_{n})_{n \in \mathbb{Z}}$ is the Fibonacci sequence with $F_{0} = 0, F_{1} = 1$.
Now we may start at any point $(3 F_{2k+1}, 3 F_{2k-1}, 3)$ and iteratively apply $\iota_{1} \circ \iota_{2}$ to generate another infinite sequence of distinct points of $U$, Zariski dense in the hyperbola cut out of $\mathcal{V}_{0}$ by the plane $x - 3 F_{2k+1} = 0$. (The plane $x = a$ cuts out an irreducible conic when $a \notin \{-2, 0, 2\}$.) Thus the Zariski closure $\bar{U}$ of $U$ contains infinitely many distinct algebraic curves in $\mathcal{V}_{0}$. Since $\mathcal{V}_{0}$ is an irreducible surface this implies that $\bar{U} = \mathcal{V}_{0}$.
For any polynomial $P$ satisfying (*), we have $P - P(3,3,3) = 0$ at each point of $U$. Since $\bar{U} = \mathcal{V}_{0}$, $P - P(3,3,3)$ vanishes on $\mathcal{V}_{0}$. Then Hilbert's Nullstellensatz and the irreducibility of $Q$ imply that $P - P(3,3,3)$ is divisible by $Q$. Now $(P - P(3,3,3)) / Q$ is a polynomial also satisfying (*), so we may complete the proof by an induction on the total degree, as in the other solutions.
