# imo_2021_96bcae

IMO-SL | IMO | 2021 | Geometry | G3

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2021_96bcae](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_96bcae.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems
- Subtitle: IMO 2021: 62nd International Mathematical Olympiad Saint-Petersburg Russia
- Year: 2021
- Editors: Kós, Géza; Woeginger, Gerhard; Ustinov, Alexey; Krachun, Dmitry; Mitrofanov, Ivan; Berlov, Sergey; Petrov, Fedor; Frolov, Ivan; Vaderlind, Paul; Golovanov, Alexander; Bogdanov, Ilya I.
- Organization: International Mathematical Olympiad
- Place: Saint-Petersburg — Russia
- Series: International Mathematical Olympiad
- Volume: 62nd

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Answer for both Versions: The largest possible sum of areas is $\Sigma(n) := \frac{1}{3} n^2 (2n+1)(2n-1)$.

Common remarks. Throughout all solutions, the area of a polygon $P$ will be denoted by $[P]$.
We say that a polygon is legal if all its vertices belong to $S$. Let $O = \left(n - \frac{1}{2}, n - \frac{1}{2}\right)$ be the centre of $S$. We say that a legal square is central if its centre is situated at $O$. Finally, say that a set $\mathcal{F}$ of polygons is acceptable if it satisfies the problem requirements, i.e. if all polygons in $\mathcal{F}$ are legal, and each point in $S$ is a vertex of exactly one polygon in $\mathcal{F}$. For an acceptable set $\mathcal{F}$, we denote by $\Sigma(\mathcal{F})$ the sum of areas of polygons in $\mathcal{F}$.


Solution 1, for both Versions. Each point in $S$ is a vertex of a unique central square. Thus the set $\mathcal{G}$ of central squares is acceptable. We will show that
$$
\begin{equation*}
\Sigma(\mathcal{F}) \leqslant \Sigma(\mathcal{G}) = \Sigma(n) \tag{1}
\end{equation*}
$$
thus establishing the answer.
We will use the following key lemma.

Lemma 1. Let $P = A_1 A_2 \ldots A_m$ be a polygon, and let $O$ be an arbitrary point in the plane. Then
$$
\begin{equation*}
[P] \leqslant \frac{1}{2} \sum_{i=1}^m OA_i^2 \tag{2}
\end{equation*}
$$
moreover, if $P$ is a square centred at $O$, then the inequality (2) turns into an equality.

Proof. Put $A_{n+1} = A_1$. For each $i = 1, 2, \ldots, m$, we have
$$
\left[OA_i A_{i+1}\right] \leqslant \frac{OA_i \cdot OA_{i+1}}{2} \leqslant \frac{OA_i^2 + OA_{i+1}^2}{4}.
$$
Therefore,
$$
[P] \leqslant \sum_{i=1}^m \left[OA_i A_{i+1}\right] \leqslant \frac{1}{4} \sum_{i=1}^m \left(OA_i^2 + OA_{i+1}^2\right) = \frac{1}{2} \sum_{i=1}^m OA_i^2
$$
which proves (2). Finally, all the above inequalities turn into equalities when $P$ is a square centred at $O$.

Back to the problem, consider an arbitrary acceptable set $\mathcal{F}$. Applying Lemma 1 to each element in $\mathcal{F}$ and to each element in $\mathcal{G}$ (achieving equality in the latter case), we obtain
$$
\Sigma(\mathcal{F}) \leqslant \frac{1}{2} \sum_{A \in S} OA^2 = \Sigma(\mathcal{G})
$$
which establishes the left inequality in (1).

It remains to compute $\Sigma(\mathcal{G})$. We have
$$
\begin{aligned}
\Sigma(\mathcal{G}) = & \frac{1}{2} \sum_{A \in S} OA^2 = \frac{1}{2} \sum_{i=0}^{2n-1} \sum_{j=0}^{2n-1} \left(\left(n - \frac{1}{2} - i\right)^2 + \left(n - \frac{1}{2} - j\right)^2\right) \\
& = \frac{1}{8} \cdot 4 \cdot 2n \sum_{i=0}^{n-1} (2n - 2i - 1)^2 = n \sum_{j=0}^{n-1} (2j + 1)^2 = n \left(\sum_{j=1}^{2n} j^2 - \sum_{j=1}^n (2j)^2\right) \\
& = n \left(\frac{2n(2n+1)(4n+1)}{6} - 4 \cdot \frac{n(n+1)(2n+1)}{6}\right) = \frac{n^2 (2n+1)(2n-1)}{3} = \Sigma(n)
\end{aligned}
$$


Solution 2, for Version 1. Let $\mathcal{F}$ be an accessible set of quadrilaterals. For every quadrilateral $ABCD$ in $\mathcal{F}$ write
$$
\begin{equation*}
[ABCD] = \frac{AC \cdot BD}{2} \sin \phi \leqslant \frac{AC^2 + BD^2}{4} \tag{3}
\end{equation*}
$$
where $\phi$ is the angle between $AC$ and $BD$. Applying this estimate to all members in $\mathcal{F}$ we obtain
$$
\Sigma(\mathcal{F}) \leqslant \frac{1}{4} \sum_{i=1}^{2n^2} A_i B_i^2
$$
where $A_1, A_2, \ldots, A_{2n^2}, B_1, B_2, \ldots, B_{2n^2}$ is some permutation of $S$. For brevity, denote
$$
f\left(\left(A_i\right), \left(B_i\right)\right) := \sum_{i=1}^{2n^2} A_i B_i^2
$$
The rest of the solution is based on the following lemma.

Lemma 2. The maximal value of $f\left(\left(A_i\right), \left(B_i\right)\right)$ over all permutations of $S$ equals $\frac{4}{3} n^2 (4n^2 - 1)$ and is achieved when $A_i$ is symmetric to $B_i$ with respect to $O$, for every $i = 1, 2, \ldots, 2n^2$.

Proof. Let $A_i = (p_i, q_i)$ and $B_i = (r_i, s_i)$, for $i = 1, 2, \ldots, 2n^2$. We have
$$
f\left(\left(A_i\right), \left(B_i\right)\right) = \sum_{i=1}^{2n^2} (p_i - r_i)^2 + \sum_{i=1}^{2n^2} (q_i - s_i)^2
$$
it suffices to bound the first sum, the second is bounded similarly. This can be done, e.g., by means of the QM-AM inequality as follows:
$$
\begin{aligned}
\sum_{i=1}^{2n^2} (p_i - r_i)^2 & = \sum_{i=1}^{2n^2} (2p_i^2 + 2r_i^2 - (p_i + r_i)^2) = 4n \sum_{j=0}^{2n-1} j^2 - \sum_{i=1}^{2n^2} (p_i + r_i)^2 \\
\leqslant 4n \sum_{j=0}^{2n-1} j^2 & - \frac{1}{2n^2} \left(\sum_{i=1}^{2n^2} (p_i + r_i)\right)^2 = 4n \sum_{j=0}^{2n-1} j^2 - \frac{1}{2n^2} \left(2n \cdot \sum_{j=0}^{2n-1} j\right)^2 \\
& = 4n \cdot \frac{2n(2n-1)(4n-1)}{6} - 2n^2 (2n-1)^2 = \frac{2n^2 (2n-1)(2n+1)}{3}
\end{aligned}
$$
All the estimates are sharp if $p_i + r_i = 2n-1$ for all $i$. Thus,
$$
f\left(\left(A_i\right), \left(B_i\right)\right) \leqslant \frac{4n^2 (4n^2 - 1)}{3}
$$
and the estimate is sharp when $p_i + r_i = q_i + s_i = 2n-1$ for all $i$, i.e. when $A_i$ and $B_i$ are symmetric with respect to $O$.

Lemma 2 yields
$$
\Sigma(\mathcal{F}) \leqslant \frac{1}{4} \cdot \frac{4n^2 (4n^2 - 1)}{3} = \frac{n^2 (2n-1)(2n+1)}{3}
$$
