# ind_2013_abf1b9

IMO-TST | India | 2013 |  | 4

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [ind_2013_abf1b9](https://mathnet.mit.edu/data_v2/full/india/ind_2013_abf1b9.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: India
- Title: Selected Problems from Team Selection Tests
- Year: 2013
- Organization: India

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $A_n$ denote the set of chosen integers after $n$ turns. We claim (by induction) that after Calvin's move he can ensure that if $a \in A_n$ then $-a \in A_n$, and that the marker is at $(r, -r)$ for some non-zero integer $r$ in $A_n$.

Let Calvin move the marker to $(-1, 1)$ in his first turn. Suppose that, after $n$ turns, the marker is at $(r, -r)$ and that Hobbes then moves it to $(r+a, -r+b)$. If $a \ne b$ then Calvin can move it back to $(r, -r)$. If $a = -b$ then Calvin can move the marker to $(c, -c)$ or $(-c, c)$ where $c$ is the largest element of $A_{n+1}$, so the claim follows. Hence Calvin can prevent Hobbes from winning. $\square$

