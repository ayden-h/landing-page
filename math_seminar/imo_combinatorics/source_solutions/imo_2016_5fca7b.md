# imo_2016_5fca7b

IMO-SL | IMO | 2016 | Combinatorics | C6

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2016_5fca7b](https://mathnet.mit.edu/data_v2/full/imo/imo_2016_5fca7b.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems with Solutions
- Subtitle: 57th International Mathematical Olympiad
- Year: 2016
- Organization: International Mathematical Olympiad
- Place: Hong Kong
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Initially, we pick any pair of islands $A$ and $B$ which are connected by a ferry route and put $A$ in set $\mathcal{A}$ and $B$ in set $\mathcal{B}$. From the condition, without loss of generality there must be another island which is connected to $A$. We put such an island $C$ in set $\mathcal{B}$. We say that two sets of islands form a network if each island in one set is connected to each island in the other set.

Next, we shall include all islands to $\mathcal{A} \cup \mathcal{B}$ one by one. Suppose we have two sets $\mathcal{A}$ and $\mathcal{B}$ which form a network where $3 \leqslant |\mathcal{A} \cup \mathcal{B}| < n$. This relation no longer holds only when a ferry route between islands $A \in \mathcal{A}$ and $B \in \mathcal{B}$ is closed. In that case, we define $\mathcal{A}' = \{A, B\}$, and $\mathcal{B}' = (\mathcal{A} \cup \mathcal{B}) - \{A, B\}$. Note that $\mathcal{B}'$ is nonempty. Consider any island $C \in \mathcal{A} - \{A\}$. From the relation of $\mathcal{A}$ and $\mathcal{B}$, we know that $C$ is connected to $B$. If $C$ was not connected to $A$ before the route between $A$ and $B$ closes, then there will be a route added between $C$ and $A$ afterwards. Hence, $C$ must now be connected to both $A$ and $B$. The same holds true for any island in $\mathcal{B} - \{B\}$. Therefore, $\mathcal{A}'$ and $\mathcal{B}'$ form a network, and $\mathcal{A}' \cup \mathcal{B}' = \mathcal{A} \cup \mathcal{B}$. Hence these islands can always be partitioned into sets $\mathcal{A}$ and $\mathcal{B}$ which form a network.

As $|\mathcal{A} \cup \mathcal{B}| < n$, there are some islands which are not included in $\mathcal{A} \cup \mathcal{B}$. From the condition, after some years there must be a ferry route between an island $A$ in $\mathcal{A} \cup \mathcal{B}$ and an island $D$ outside $\mathcal{A} \cup \mathcal{B}$ which closes. Without loss of generality assume $A \in \mathcal{A}$. Then each island in $\mathcal{B}$ must then be connected to $D$, no matter it was or not before. Hence, we can put $D$ in set $\mathcal{A}$ so that the new sets $\mathcal{A}$ and $\mathcal{B}$ still form a network and the size of $\mathcal{A} \cup \mathcal{B}$ is increased by $1$. The same process can be done to increase the size of $\mathcal{A} \cup \mathcal{B}$. Eventually, all islands are included in this way so we may now assume $|\mathcal{A} \cup \mathcal{B}| = n$.

Suppose a ferry route between $A \in \mathcal{A}$ and $B \in \mathcal{B}$ is closed after some years. We put $A$ and $B$ in set $\mathcal{A}'$ and all remaining islands in set $\mathcal{B}'$. Then $\mathcal{A}'$ and $\mathcal{B}'$ form a network. This relation no longer holds only when a route between $A$, without loss of generality, and $C \in \mathcal{B}'$ is closed. Since this must eventually occur, at that time island $B$ will be connected to all other islands and the result follows.

