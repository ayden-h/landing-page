# bmo_2020_dff0bd

BMO-SL | Balkan Mathematical Olympiad | 2020 | Combinatorics | C1

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2020_dff0bd](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2020_dff0bd.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: BMO Short List
- Year: 2020
- Authors: Banerjee, Agnijo; Bealing, Sam; Christofides, Demetres; Gerdjikov, Stefan; Ivanov, Alexander; Mironov, Miroslav; Parayiou, Theoklitos; Silouanos, Brazitikos; Winter, Patrick
- Organization: BMO
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Fix a member $A$ of $\mathcal{A}$. Note that there are at most $\binom{k}{2}n^{k-2}$ $k$-tuples that share at least two entries with $A$. Indeed, there are $n^{k-2}$ $k$-tuples sharing any two given entries. The bound now follows, since the two entries can be chosen in $\binom{k}{2}$ different ways.

Therefore, the number of members of $\mathcal{A}$ that share a single entry with $A$ is at least
$$
|\mathcal{A}| - \binom{k}{2} n^{k-2} \ge 2sk^2n^{k-2} - k^2n^{k-2} > sk^2n^{k-2}.
$$
Letting $\mathcal{B}_p$ be the set of all members of $\mathcal{A}$ that share the $p$-th entry alone with $A$, the above estimate yields $\sum_{p=1}^k |\mathcal{B}_p| > sk^2n^{k-2}$, and hence $|\mathcal{B}_p| > skn^{k-2}$ for some $p$.

Let $B$ be an arbitrary member of this $\mathcal{B}_p$. Then there are at most $(k-1)n^{k-2}$ $k$-tuples that share the $p$-th entry and some other entry with $B$. Now, let $t$ be maximal with the property that there are $B_1, B_2, \dots, B_t$ in $\mathcal{B}_p$ such that any two $B_i$ and $B_j$ share the $p$-th entry alone for $i \ne j$. Hence any other member $B'$ of $\mathcal{B}_p$ shares with some $B_i$ at least one entry different from the $p$-th. Consequently, $|\mathcal{B}_p| \le t(k-1)n^{k-2}$.

Finally, compare the two bounds for $|\mathcal{B}_p|$ to get $t > s$, and conclude that $A, B_1, \dots, B_t$ are $t+1 \ge s+2$ members of $\mathcal{A}$ every two of which share the $p$-th entry alone.

