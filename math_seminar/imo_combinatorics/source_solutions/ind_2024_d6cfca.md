# ind_2024_d6cfca

IMO-TST | India | 2024 | Day 2 | 3.

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [ind_2024_d6cfca](https://mathnet.mit.edu/data_v2/full/india/ind_2024_d6cfca.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: India
- Title: Indian Mathematical Olympiads
- Subtitle: Problems Booklet
- Year: 2023-24
- Authors: Srivastava, Pranjal; Bhattacharya, Sutanay; Somasundaran, Muralidharan; Mudgal, Anant; Goyal, Rohan; Nene, Shantanu; Nadig, Atul Shatavart; Tejaswi, N.V.; Ghosh, Mainak; Saini, Rijul; Amin, Kazi Aryan; Sudharshan, K.V.

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Consider obvious graph theory interpretation, with vertices being labelled by the ages. Whenever we say an increasing path, we refer to the labels being monotonically increasing. For any vertex $w$, let $S(w)$ be the set of all $m \pmod k$ such that there exists an increasing path $v_1, v_2, \dots, v_m = w$ with $v_1$ being small. Thus each $S(w)$ is a subset of $\mathbb{Z}/k\mathbb{Z}$. Further, $S(w)$ can't be empty, because by going backwards, there is at least one increasing path starting from a small vertex that ends at $w$. Moreover, $S(w) \ne \mathbb{Z}/k\mathbb{Z}$, because there is an increasing path starting from $w$ ending at a big vertex (just by picking a larger neighbour every time), and by picking a suitable path from a small vertex to $w$ (whose length is the required residue modulo $k$), we get a good path passing through $w$ whose number of vertices is divisible by $k$.
We properly color the vertices in $k$ colors $c_0, c_1, \dots, c_{k-1}$, just based on $S(w)$. Indeed, since $S(w)$ is a non-empty proper subset of $\mathbb{Z}/k\mathbb{Z}$, there exists a $j \in S(w)$ such that $j+1 \notin S(w)$. Choose any such $j$ and color $w$ with $c_j$.
We claim that this is a proper coloring. Indeed, suppose two neighbours $u, v$ have been assigned the same color $c_i$. WLOG the label of $u$ is smaller than the label of $v$. Then, adding edge $uv$ to any increasing path ending at $u$, we get an increasing path ending at $v$, so $S(u)+1 \subset S(v)$. But $v$ being colored $c_j$ implies $j+1 \pmod k \notin S(v)$, while $u$ being colored $c_j$ implies $j \in S(u)$, which implies $j+1 \in S(u)+1 \subset S(v)$, contradiction! Hence the coloring is proper, as required.

## Supplied solution 2

It is easy to see that every edge is part of a *photogenic* sequence. We color the vertices in $k$ colors $c_0, \dots, c_{k-1}$ (indices modulo $k$), based on the following algorithm:

Step 1: Color all juniors $c_1$.

Step 2: Pick the youngest uncolored vertex $P$, and pick a color $c_i$ such that no friend of $P$ younger than $P$ has color $c_i$, while some friend of $P$ younger than $P$ has color $c_{i-1}$.

We can prove inductively that if $P$ has color $c_i$, then there is a path of (vertex-)length $i \pmod k$. Thus the only way Step 2 fails is if $P$ has neighbors younger than them of every color. But in that case there is an increasing path starting from a junior to $P$ with length $i \pmod k$ for every $i$, which is impossible as seen in Solution A.

