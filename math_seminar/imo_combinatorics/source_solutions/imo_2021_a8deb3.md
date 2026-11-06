# imo_2021_a8deb3

IMO-SL | IMO | 2021 | Combinatorics | C4

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2021_a8deb3](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_a8deb3.json.gz)

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

We write $X \rightarrow Y$ (or $Y \leftarrow X$) if the road between $X$ and $Y$ goes from $X$ to $Y$. Notice that, if there is any route moving from $X$ to $Y$ (possibly passing through some cities more than once), then there is a path from $X$ to $Y$ consisting of some roads in the route. Indeed, any cycle in the route may be removed harmlessly; after some removals one obtains a path.

Say that a path is short if it consists of one or two roads.

Partition all cities different from $A$ and $B$ into four groups, $\mathcal{I}$, $\mathcal{O}$, $\mathcal{A}$, and $\mathcal{B}$ according to the following rules: for each city $C$,
$$
\begin{array}{ll}
C \in \mathcal{I} \Longleftrightarrow A \rightarrow C \leftarrow B ; & C \in \mathcal{O} \Longleftrightarrow A \leftarrow C \rightarrow B ; \\
C \in \mathcal{A} \Longleftrightarrow A \rightarrow C \rightarrow B ; & C \in \mathcal{B} \Longleftrightarrow A \leftarrow C \leftarrow B .
\end{array}
$$

Lemma. Let $\mathcal{P}$ be a diverse collection consisting of $p$ paths from $A$ to $B$. Then there exists a diverse collection consisting of at least $p$ paths from $A$ to $B$ and containing all short paths from $A$ to $B$.

Proof. In order to obtain the desired collection, modify $\mathcal{P}$ as follows.
If there is a direct road $A \rightarrow B$ and the path consisting of this single road is not in $\mathcal{P}$, merely add it to $\mathcal{P}$.
Now consider any city $C \in \mathcal{A}$ such that the path $A \rightarrow C \rightarrow B$ is not in $\mathcal{P}$. If $\mathcal{P}$ contains at most one path containing a road $A \rightarrow C$ or $C \rightarrow B$, remove that path (if it exists), and add the path $A \rightarrow C \rightarrow B$ to $\mathcal{P}$ instead. Otherwise, $\mathcal{P}$ contains two paths of the forms $A \rightarrow C \rightarrow B$ and $A \rightarrow C \rightarrow B$, where $C \rightarrow B$ and $A \rightarrow C$ are some paths. In this case, we recombine the edges to form two new paths $A \rightarrow C \rightarrow B$ and $A \rightarrow C \rightarrow B$ (removing cycles from the latter if needed). Now we replace the old two paths in $\mathcal{P}$ with the two new ones.
After any operation described above, the number of paths in the collection does not decrease, and the collection remains diverse. Applying such operation to each $C \in \mathcal{A}$, we obtain the desired collection. $\square$

Back to the problem, assume, without loss of generality, that there is a road $A \rightarrow B$, and let $a$ and $b$ denote the numbers of roads going out from $A$ and $B$, respectively. Choose a diverse collection $\mathcal{P}$ consisting of $N_{A B}$ paths from $A$ to $B$. We will transform it into a diverse collection $\mathcal{Q}$ consisting of at least $N_{A B}+(b-a)$ paths from $B$ to $A$. This construction yields
$$
N_{B A} \geqslant N_{A B}+(b-a) ; \quad \text{similarly, we get} \quad N_{A B} \geqslant N_{B A}+(a-b),
$$
whence $N_{B A}-N_{A B}=b-a$. This yields the desired equivalence.

Apply the lemma to get a diverse collection $\mathcal{P}^{\prime}$ of at least $N_{A B}$ paths containing all $|\mathcal{A}|+1$ short paths from $A$ to $B$. Notice that the paths in $\mathcal{P}^{\prime}$ contain no edge of a short path from $B$ to $A$. Each non-short path in $\mathcal{P}^{\prime}$ has the form $A \rightarrow C \rightarrow D \rightarrow B$, where $C \rightarrow D$ is a path from some city $C \in \mathcal{I}$ to some city $D \in \mathcal{O}$. For each such path, put into $\mathcal{Q}$ the path $B \rightarrow C \rightarrow D \rightarrow A$; also put into $\mathcal{Q}$ all short paths from $B$ to $A$. Clearly, the collection $\mathcal{Q}$ is diverse.

Now, all roads going out from $A$ end in the cities from $\mathcal{I} \cup \mathcal{A} \cup \{B\}$, while all roads going out from $B$ end in the cities from $\mathcal{I} \cup \mathcal{B}$. Therefore,
$$
a=|\mathcal{I}|+|\mathcal{A}|+1, \quad b=|\mathcal{I}|+|\mathcal{B}|, \quad \text{and hence} \quad a-b=|\mathcal{A}|-|\mathcal{B}|+1 .
$$
On the other hand, since there are $|\mathcal{A}|+1$ short paths from $A$ to $B$ (including $A \rightarrow B$) and $|\mathcal{B}|$ short paths from $B$ to $A$, we infer
$$
|\mathcal{Q}|=\left|\mathcal{P}^{\prime}\right|-(|\mathcal{A}|+1)+|\mathcal{B}| \geqslant N_{A B}+(b-a),
$$
as desired.

## Supplied solution 2

We recall some graph-theoretical notions. Let $G$ be a finite graph, and let $V$ be the set of its vertices; fix two distinct vertices $s, t \in V$. An $(s, t)$-cut is a partition of $V$ into two parts $V=S \sqcup T$ such that $s \in S$ and $t \in T$. The cut-edges in the cut $(S, T)$ are the edges going from $S$ to $T$, and the size $e(S, T)$ of the cut is the number of cut-edges.

We will make use of the following theorem (which is a partial case of the Ford-Fulkerson "min-cut max-flow" theorem).

Theorem (Menger). Let $G$ be a directed graph, and let $s$ and $t$ be its distinct vertices. Then the maximal number of edge-disjoint paths from $s$ to $t$ is equal to the minimal size of an $(s, t)$-cut.

Back to the problem. Consider a directed graph $G$ whose vertices are the cities, and edges correspond to the roads. Then $N_{A B}$ is the maximal number of edge-disjoint paths from $A$ to $B$ in this graph; the number $N_{B A}$ is interpreted similarly.

As in the previous solution, denote by $a$ and $b$ the out-degrees of vertices $A$ and $B$, respectively. To solve the problem, we show that for any $(A, B)$-cut $(S_{A}, T_{A})$ in our graph there exists a $(B, A)$-cut $(S_{B}, T_{B})$ satisfying
$$
e\left(S_{B}, T_{B}\right)=e\left(S_{A}, T_{A}\right)+(b-a)
$$
This yields
$$
N_{B A} \leqslant N_{A B}+(b-a) ; \quad \text{similarly, we get} \quad N_{A B} \leqslant N_{B A}+(a-b),
$$
whence again $N_{B A}-N_{A B}=b-a$.

The construction is simple: we put $S_{B}=S_{A} \cup \{B\} \backslash \{A\}$ and hence $T_{B}=T_{A} \cup \{A\} \backslash \{B\}$. To show that it works, let A and B denote the sets of cut-edges in $(S_{A}, T_{A})$ and $(S_{B}, T_{B})$, respectively. Let $a_{s}$ and $a_{t}=a-a_{s}$ denote the numbers of edges going from $A$ to $S_{A}$ and $T_{A}$, respectively. Similarly, denote by $b_{s}$ and $b_{t}=b-b_{s}$ the numbers of edges going from $B$ to $S_{B}$ and $T_{B}$, respectively.

Notice that any edge incident to none of $A$ and $B$ either belongs to both A and B, or belongs to none of them. Denote the number of such edges belonging to A by $c$. The edges in A which are not yet accounted for split into two categories: those going out from $A$ to $T_{A}$ (including $A \rightarrow B$ if it exists), and those going from $S_{A} \backslash \{A\}$ to $B$ - in other words, going from $S_{B}$ to $B$. The numbers of edges in the two categories are $a_{t}$ and $|S_{B}|-1-b_{s}$, respectively. Therefore,
$$
|\mathrm{A}|=c+a_{t}+\left(|S_{B}|-b_{s}-1\right) . \quad \text{Similarly, we get} \quad|\mathrm{B}|=c+b_{t}+\left(|S_{A}|-a_{s}-1\right),
$$
and hence
$$
|\mathrm{B}|-|\mathrm{A}|=\left(b_{t}+b_{s}\right)-\left(a_{t}+a_{s}\right)=b-a,
$$
since $|S_{A}|=|S_{B}|$. This finishes the solution.

