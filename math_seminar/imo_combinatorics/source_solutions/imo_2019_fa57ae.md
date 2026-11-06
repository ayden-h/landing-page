# imo_2019_fa57ae

IMO-SL | IMO | 2019 | Combinatorics | C9

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2019_fa57ae](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_fa57ae.json.gz)

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

We first construct a set $\mathcal{F}$ with $2^{k}$ members, each member having at most $k$ different scales in $\mathcal{F}$. Take $\mathcal{F} = \{0, 1, 2, \ldots, 2^{k} - 1\}$. The scale between any two members of $\mathcal{F}$ is in the set $\{0, 1, \ldots, k-1\}$.

We now show that $2^{k}$ is an upper bound on the size of $\mathcal{F}$. For every finite set $\mathcal{S}$ of real numbers, and every real $x$, let $r_{\mathcal{S}}(x)$ denote the number of different scales of $x$ in $\mathcal{S}$. That is, $r_{\mathcal{S}}(x) = |\{D(x, y): x \neq y \in \mathcal{S}\}|$. Thus, for every element $x$ of the set $\mathcal{F}$ in the problem statement, we have $r_{\mathcal{F}}(x) \leqslant k$. The condition $|\mathcal{F}| \leqslant 2^{k}$ is an immediate consequence of the following lemma.

Lemma. Let $\mathcal{S}$ be a finite set of real numbers, and define
$$
w(\mathcal{S}) = \sum_{x \in \mathcal{S}} 2^{-r_{\mathcal{S}}(x)}
$$
Then $w(\mathcal{S}) \leqslant 1$.

Proof. Induction on $n = |\mathcal{S}|$. If $\mathcal{S} = \{x\}$, then $r_{\mathcal{S}}(x) = 0$, so $w(\mathcal{S}) = 1$.

Assume now $n \geqslant 2$, and let $x_{1} < \cdots < x_{n}$ list the members of $\mathcal{S}$. Let $d$ be the minimal scale between two distinct elements of $\mathcal{S}$; then there exist neighbours $x_{t}$ and $x_{t+1}$ with $D(x_{t}, x_{t+1}) = d$. Notice that for any two indices $i$ and $j$ with $j - i > 1$ we have $D(x_{i}, x_{j}) > d$, since
$$
|x_{i} - x_{j}| = |x_{i+1} - x_{i}| + |x_{j} - x_{i+1}| \geqslant 2^{d} + 2^{d} = 2^{d+1}
$$
Now choose the minimal $i \leqslant t$ and the maximal $j \geqslant t+1$ such that $D(x_{i}, x_{i+1}) = D(x_{i+1}, x_{i+2}) = \cdots = D(x_{j-1}, x_{j}) = d$.

Let $E$ be the set of all the $x_{s}$ with even indices $i \leqslant s \leqslant j$, $O$ be the set of those with odd indices $i \leqslant s \leqslant j$, and $R$ be the rest of the elements (so that $\mathcal{S}$ is the disjoint union of $E$, $O$ and $R$). Set $\mathcal{S}_{O} = R \cup O$ and $\mathcal{S}_{E} = R \cup E$; we have $|\mathcal{S}_{O}| < |\mathcal{S}|$ and $|\mathcal{S}_{E}| < |\mathcal{S}|$, so $w(\mathcal{S}_{O}), w(\mathcal{S}_{E}) \leqslant 1$ by the inductive hypothesis.

Clearly, $r_{\mathcal{S}_{O}}(x) \leqslant r_{\mathcal{S}}(x)$ and $r_{\mathcal{S}_{E}}(x) \leqslant r_{\mathcal{S}}(x)$ for any $x \in R$, and thus
$$
\begin{aligned}
\sum_{x \in R} 2^{-r_{\mathcal{S}}(x)} & = \frac{1}{2} \sum_{x \in R} \left(2^{-r_{\mathcal{S}}(x)} + 2^{-r_{\mathcal{S}}(x)}\right) \\
& \leqslant \frac{1}{2} \sum_{x \in R} \left(2^{-r_{\mathcal{S}_{O}}(x)} + 2^{-r_{\mathcal{S}_{E}}(x)}\right)
\end{aligned}
$$
On the other hand, for every $x \in O$, there is no $y \in \mathcal{S}_{O}$ such that $D_{\mathcal{S}_{O}}(x, y) = d$ (as all candidates from $\mathcal{S}$ were in $E$). Hence, we have $r_{\mathcal{S}_{O}}(x) \leqslant r_{\mathcal{S}}(x) - 1$, and thus
$$
\sum_{x \in O} 2^{-r_{\mathcal{S}}(x)} \leqslant \frac{1}{2} \sum_{x \in O} 2^{-r_{S_{O}}(x)}
$$
Similarly, for every $x \in E$, we have
$$
\sum_{x \in E} 2^{-r_{\mathcal{S}}(x)} \leqslant \frac{1}{2} \sum_{x \in E} 2^{-r_{\mathcal{S}_{E}}(x)}
$$
We can then combine these to give
$$
\begin{aligned}
w(S) & = \sum_{x \in R} 2^{-r_{\mathcal{S}}(x)} + \sum_{x \in O} 2^{-r_{\mathcal{S}}(x)} + \sum_{x \in E} 2^{-r_{\mathcal{S}}(x)} \\
& \leqslant \frac{1}{2} \sum_{x \in R} \left(2^{-r_{\mathcal{S}_{O}}(x)} + 2^{-r_{\mathcal{S}_{E}}(x)}\right) + \frac{1}{2} \sum_{x \in O} 2^{-r_{\mathcal{S}_{O}}(x)} + \frac{1}{2} \sum_{x \in E} 2^{-r_{\mathcal{S}_{E}}(x)} \\
& = \frac{1}{2} \left(\sum_{x \in \mathcal{S}_{O}} 2^{-r_{\mathcal{S}_{O}}(x)} + \sum_{x \in \mathcal{S}_{E}} 2^{-r_{\mathcal{S}_{E}}(x)}\right) \quad (\text{since } \mathcal{S}_{O} = O \cup R \text{ and } \mathcal{S}_{E} = E \cup R) \\
& = \frac{1}{2} \left(w(\mathcal{S}_{O}) + w(\mathcal{S}_{E})\right) \quad \text{(by definition of } w(\cdot)) \\
& \leqslant 1 \quad (\text{by the inductive hypothesis})
\end{aligned}
$$
which completes the induction.

