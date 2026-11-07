# bmo_2014_5daa9c

BMO-SL | Balkan Mathematical Olympiad | 2014 | Combinatorics | C2

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2014_5daa9c](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_5daa9c.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: 31st Balkan Mathematical Olympiad
- Subtitle: Problem Shortlist with solutions
- Year: 2014
- Editors: Kolev, Emil; Ivanov, Alexander; Beluhov, Nikolay
- Organization: Balkan Mathematical Olympiad
- Place: Pleven, Bulgaria
- Series: Balkan Mathematical Olympiad
- Volume: 31
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We will prove that this is possible. Total number of subsets of the set $M$ is $2^{2013}$. On circle $\Gamma$ we arbitrarily choose $2^{2013}$ points which are vertices of a regular $2^{2013}$-gon. We join subsets of the set $M$ and chosen points in the following manner: if we join subset $\mathcal{A}$ with some point on $\Gamma$, we join subset $\mathcal{A}^c = M\setminus \mathcal{A}$ with a point symmetric to the point joined with $\mathcal{A}$ with respect to the center of $\Gamma$ (number $2^{2013}$ is even, so this is possible). If $A_1, A_2, \dots, A_k$ are some of the points joined with subsets, which are vertices of a regular $k$-gon, then it follows that $k\mid 2^{2013}$, so $k$ is a number divisible by $4$, say $k = 4t$. That is why all points $A_1, A_2, \dots, A_k$ can be divided in $\frac{k}{2} = 2t$ pairs of symmetric points with respect to center of $\Gamma$. Using that
$$
S(\mathcal{A}) + S(\mathcal{A}^c) = 1 + 2 + \dots + 2013 = 1007 \cdot 2013,
$$
we get $S(\mathcal{A}_1) + \dots + S(\mathcal{A}_k) = 2t \cdot 1007 \cdot 2013 = 2014 \cdot 2013 \cdot t$, so all conditions are fulfilled.
