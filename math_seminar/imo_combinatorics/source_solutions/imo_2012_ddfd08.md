# imo_2012_ddfd08

IMO-SL | IMO | 2012 | Combinatorics | C5

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2012_ddfd08](https://mathnet.mit.edu/data_v2/full/imo/imo_2012_ddfd08.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems with Solutions
- Subtitle: 53rd International Mathematical Olympiad
- Year: 2012
- Editors: Avendaño, Martín; di Fiore, Carlos; Kós, Géza; Savchev, Svetoslav
- Organization: International Mathematical Olympiad
- Place: Mar del Plata, Argentina

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Without loss of generality it suffices to prove that the A-tokens can be moved to distinct A-squares in such a way that each A-token is moved to a distance at most $d+2$ from its original place. This means we need a perfect matching between the $3n^{2}$ A-squares and the $3n^{2}$ A-tokens such that the distance in each pair of the matching is at most $d+2$.

To find the matching, we construct a bipartite graph. The A-squares will be the vertices in one class of the graph; the vertices in the other class will be the A-tokens.

Split the board into $3 \times 1$ horizontal triminos; then each trimino contains exactly one A-square. Take a permutation $\pi$ of the tokens which moves A-tokens to B-tokens, B-tokens to C-tokens, and C-tokens to A-tokens, in each case to a distance at most $d$. For each A-square $S$, and for each A-token $T$, connect $S$ and $T$ by an edge if $T$, $\pi(T)$ or $\pi^{-1}(T)$ is on the trimino containing $S$. We allow multiple edges; it is even possible that the same square and the same token are connected with three edges. Obviously the lengths of the edges in the graph do not exceed $d+2$. By length of an edge we mean the distance between the A-square and the A-token it connects.

Each A-token $T$ is connected with the three A-squares whose triminos contain $T$, $\pi(T)$ and $\pi^{-1}(T)$. Therefore in the graph all tokens are of degree $3$. We show that the same is true for the A-squares. Let $S$ be an arbitrary A-square, and let $T_{1}, T_{2}, T_{3}$ be the three tokens on the trimino containing $S$. For $i=1,2,3$, if $T_{i}$ is an A-token, then $S$ is connected with $T_{i}$; if $T_{i}$ is a B-token then $S$ is connected with $\pi^{-1}\left(T_{i}\right)$; finally, if $T_{i}$ is a C-token then $S$ is connected with $\pi\left(T_{i}\right)$. Hence in the graph the A-squares also are of degree $3$.

Since the A-squares are of degree $3$, from every set $\mathcal{S}$ of A-squares exactly $3|\mathcal{S}|$ edges start. These edges end in at least $|\mathcal{S}|$ tokens because the A-tokens also are of degree $3$. Hence every set $\mathcal{S}$ of A-squares has at least $|\mathcal{S}|$ neighbors among the A-tokens.

Therefore, by Hall's marriage theorem, the graph contains a perfect matching between the two vertex classes. So there is a perfect matching between the A-squares and A-tokens with edges no longer than $d+2$. It follows that the tokens can be permuted as specified in the problem statement.

