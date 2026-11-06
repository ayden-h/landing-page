# usa_2009_ddbe0d

USAMO | United States | 2009 | 1.1 USAMO 2009 Problems | 2

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [usa_2009_ddbe0d](https://mathnet.mit.edu/data_v2/full/united-states/usa_2009_ddbe0d.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: United States
- Title: USA and International Mathematical Olympiads
- Year: 2009-2010
- Editors: Feng, Zuming; Sun, Yi

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

The maximum size is $n$ if $n$ is even, and $n+1$ if $n$ is odd, achieved by the subset
$$
\{-n, \dots, -\lfloor \frac{n}{2} \rfloor - 1, \lfloor \frac{n}{2} \rfloor + 1, \dots, n\}.
$$
**Lemma 1.** Let $A, B$ be finite nonempty subsets of $\mathbb{Z}$. Then the set $A + B = \{a + b : a \in A, b \in B\}$ has cardinality at least $|A| + |B| - 1$.
*Proof.* Write $A = \{a_1, \dots, a_l\}$ and $B = \{b_1, \dots, b_m\}$ with $a_1 < \dots < a_l$ and $b_1 < \dots < b_m$. Then
$$
a_1 + b_1, \dots, a_1 + b_m, a_2 + b_m, \dots, a_l + b_m
$$
is a strictly increasing sequence of $l+m-1$ elements of $A+B$. $\square$

Let $S$ be a subset of $\{-n, \dots, n\}$ with the desired property; clearly $0 \notin S$. Put $A = S \cap \{-n, \dots, -1\}$ and $B = S \cap \{1, \dots, n\}$. Then $A+B$ and $-S = \{-s : s \in S\}$ are disjoint subsets of $\{-n, \dots, n\}$, so by the lemma,
$$
2n + 1 \ge |A + B| + | - S| \ge |A| + |B| - 1 + |S| = 2|S| - 1,
$$
or $|S| \le n+1$. If $n$ is odd, we are done.

If $n$ is even, we must still show that $|S| = n+1$ is impossible. Since $A+B \subseteq \{-n+1, \dots, n-1\}$, we cannot achieve the equality $2n+1 = |A+B| + |-S|$ unless $-n, n \in -S$, or equivalently $-n, n \in S$. Since $-n \in S$, each of the sets $\{1, n-1\}, \dots, \{n/2-1, n/2+1\}, \{n/2\}$ must contain an element not in $B$. Thus $|B| \le n/2$, and similarly $|A| \le n/2$, contradicting the hypothesis $|S| = n+1$.

