# usa_2013_bfa49c

IMO-TST | United States | 2013 | TSTST 2013 Problems | 1.

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [usa_2013_bfa49c](https://mathnet.mit.edu/data_v2/full/united-states/usa_2013_bfa49c.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: United States
- Title: USA and International Mathematical Olympiads
- Year: 2013-2014
- Editors: Feng, Zuming; Lian, Carl; Sun, Yi
- Organization: Mathematical Association of America

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

The only solution is to have $a_k = 2k - 1$ for all $k$, giving the sequence $1, 3, 5, \dots$.

Let $a_1 = m$. First, we show that for any such sequence, we must have $a_{k+m} - a_k \ge 2m$ for all positive integers $k$. Suppose for some $k$ that this was not the case. Then $a_k, a_{k+1}, \dots, a_{k+m}$ are $m+1$ terms of the sequence that are all in the set $S = \{a_k, a_k+1, \dots, a_k+2m-1\}$. Partition $S$ into $m$ two-element sets of the form $\{b, b+m\}$. By the pigeonhole principle, one of the $m$ two-element sets is such that both of its elements are terms of the sequence, so that $a_{i_1} + m = a_{i_2}$ for some $k \le i_1, i_2 \le k+m$. But we have $a_1 = m$, so this contradicts (b). Thus we have established $a_{k+m} - a_k \ge 2m$ for all $k$.

Now suppose we have $m$ consecutive terms of the sequence $a_j, a_{j+1}, \dots, a_{j+m-1}$ such that for all $k$ between $j$ and $j+m-1$ inclusive, $a_k > 2k-1$. By (c), there must exist some index $i$ greater than $j$ satisfying $a_i = 2i-1$. Write $i-j = mq+r$ for $q \ge 0$ and $0 \le r < m$ using the division algorithm. Then $a_i \ge 2m + a_{i-m} \ge \dots \ge 2qm + a_{i-qm} = 2qm + a_{j+r}$. By assumption $a_{j+r} > 2(j+r)-1$, so $a_i > 2qm + 2(j+r) - 1 = 2i-1$, a contradiction. Therefore, for any block of $m$ consecutive terms of the sequence, one of them satisfies $a_k \le 2k-1$.

Because of (a), we have $a_k \ge m + (k-1)$. Consider $a_1, a_2, \dots, a_m$. The previous inequality implies that for all $i < m$ we have $a_i > 2i-1$, and $a_m \ge 2m-1$. By the previous paragraph one of these terms must satisfy $a_i \le 2i-1$. Therefore we must have $a_m = 2m-1$ and by (a) $a_i = m+i-1$ for all $1 \le i \le m$.

Likewise, for $a_{m+1}, a_{m+2}, \dots, a_{2m}$, we have $a_{m+i} \ge 2m + a_i > 2(m+i) - 1$ for all $i < m$ and $a_{2m} \ge 4m-1$, so since one of these $m$ terms must satisfy $a_i \le 2i-1$ we must have $a_{2m} = 4m-1$ and then by (a) $a_{m+i} = 3m + i - 1$ for all $1 \le i \le m$.

Now suppose $m > 1$. Observe that $a_m + a_m = 4m - 2 = a_{2m-1}$, contradicting (b). Therefore $m = a_1 = 1$. Furthermore, we know from the second paragraph that every term of the sequence satisfies $a_k \le 2k-1$. At the same time, the first paragraph says $a_{k+1} - a_k \ge 2$, or $a_k \ge 2k - 2 + a_1 = 2k-1$. Therefore $a_k = 2k-1$ for every $k$.
