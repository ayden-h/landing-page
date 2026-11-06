# apm_2016_6dfebe

APMO | Asia Pacific Mathematics Olympiad (APMO) | 2016 |  | 4

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [apm_2016_6dfebe](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2016_6dfebe.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Asia Pacific Mathematics Olympiad (APMO)
- Title: Solutions of APMO 2016
- Year: 2016
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

The flights established by Starways yield a directed graph $G$ on 2016 vertices in which each vertex has out-degree equal to 1.

We first show that we need at least 57 groups. For this, suppose that $G$ has a directed cycle of length 57. Then, for any two cities in the cycle, one is reachable from the other using at most 28 flights. So no two cities in the cycle can belong to the same group. Hence, we need at least 57 groups.

We will now show that 57 groups are enough. Consider another auxiliary directed graph $H$ in which the vertices are the cities of Dreamland and there is an arrow from city $u$ to city $v$ if $u$ can be reached from $v$ using at most 28 flights. Each city has out-degree at most 28. We will be done if we can split the cities of $H$ in at most 57 groups such that there are no arrows between vertices of the same group. We prove the following stronger statement.

Lemma: Suppose we have a directed graph on $n \geq 1$ vertices such that each vertex has out-degree at most 28. Then the vertices can be partitioned into 57 groups in such a way that no vertices in the same group are connected by an arrow.

Proof: We apply induction. The result is clear for 1 vertex. Now suppose we have more than one vertex. Since the out-degree of each vertex is at most 28, there is a vertex, say $v$, with in-degree at most 28. If we remove the vertex $v$ we obtain a graph with fewer vertices which still satisfies the conditions, so by inductive hypothesis we may split it into at most 57 groups with no adjacent vertices in the same group. Since $v$ has in-degree and out-degree at most 28, it has at most 56 neighbors in the original directed graph. Therefore, we may add $v$ back and place it in a group in which it has no neighbors. This completes the inductive step.

