# usa_2008_4ddab6

IMO-TST | United States | 2008 | TST 2008 Problems | 1

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [usa_2008_4ddab6](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_4ddab6.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: United States
- Title: USA and International Mathematical Olympiads 2007-2008
- Editors: Feng, Zuming; Sun, Yi
- Organization: University of Nebraska-Lincoln

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

The only such $n$ are $1$ and odd $n$ at least $7$. We divide into cases: $n$ even, $n = 1$, $n = 3$, $n = 5$, and $n \ge 7$ odd.

**Case 1:** $n$ even. Suppose for contradiction that such a set exists, and choose one with minimal total weight. Let $s$ be the sum of the weights, and note that
$$
s - w_1 \equiv \dots \equiv s - w_n \equiv 0 \pmod{2}.
$$
Hence
$$
w_1 \equiv \dots \equiv w_n \pmod{2}.
$$
Since $n$ is even, it follows that $s$ is even, and so also that $w_i$ is even for all $i$. But then the set $\{w_i/2\}$ is another set of $n$ weights with the desired property, contradicting minimality. Hence $n$ odd fails.

**Case 2:** $n = 1$. Trivially yes.

**Case 3:** $n = 3$. Removing any weight leaves two unequal weights.

**Case 4:** $n = 5$. Suppose for contradiction that such a set exists: order the weights such that $w_1 < w_2 < w_3 < w_4 < w_5$. Let $t = w_2 + w_3 + w_4$. For each $i \in \{2, 3, 4\}$, the only possible ways to split the weights other than $w_i$ are as $w_5 = t - w_i + w_1$ or $w_5 + w_1 = t - w_i$ (in all other combinations, the side with $w_5$ is strictly heavier than the other). By pigeonhole, one of the equations is satisfied for two values of $i$, and the corresponding weights are equal, contradiction.

**Case 5:** $n \ge 7$ odd. Checking the cases $n = 7$, $n = 9$, and $n = 11$ is straightforward casework: the sets $\{1, 3, 5, \dots, 2n - 1\}$ suffice. For example, if $n = 7$, the set is $\{1, 3, 5, \dots, 13\}$ and
$$
\begin{aligned}
3 + 5 + 7 + 9 &= 11 + 13 \\
1 + 9 + 13 &= 5 + 7 + 11 \\
1 + 3 + 7 + 11 &= 9 + 13 \\
1 + 9 + 11 &= 3 + 5 + 13 \\
1 + 3 + 5 + 11 &= 7 + 13 \\
1 + 5 + 13 &= 3 + 7 + 9 \\
1 + 3 + 5 + 9 &= 7 + 11.
\end{aligned}
$$
Suppose there exists such a set for $n = k$ and $n = j$, let $w_1 < w_2 < \dots < w_k$ and $v_1 < \dots < v_j$ be the corresponding set of weights and let $s = v_1 + \dots + v_j$. Consider the set of weights $w_1v_1, w_1v_2, \dots, w_1v_j, w_2s, w_3s, \dots, w_ks$. These are distinct (each is less than the next in the list by assumption). If weight $w_1v_i$ is removed, then by the inductive hypothesis the other $v$'s can be sorted into two groups of equal weight, as can the $w$'s other than $w_1$, so the remaining weights can be divided into two groups of equal weight. If weight $w_is$ is removed, then put all the weights $w_1v_1, \dots, w_1v_j$ together to get weights $w_1s, w_2s, \dots, w_{i-1}s, w_{i+1}s, \dots, w_ks$. By the inductive hypothesis these can be divided into two groups of equal weight. Hence if such a set exists for $n = k$ and $n = j$, it exists for $k + j - 1$.

Taking $j = 7$, we see that if a set exists for $n = k$, one also exists for $n = k + 6$. By induction, it follows that a set exists for all $n$ of the form $6m + 7$, $6m + 9$, and $6m + 11$, where $m$ is a non-negative integer. Since this covers all odd numbers greater than $7$, we are done.
