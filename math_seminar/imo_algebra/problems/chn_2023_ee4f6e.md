# chn_2023_ee4f6e

CMO-China | China | 2023 | Day One | 3

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [chn_2023_ee4f6e](https://mathnet.mit.edu/data_v2/full/china/chn_2023_ee4f6e.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: China
- Title: The 39th Chinese Mathematical Olympiad
- Year: 2023
- Organization: Chinese Mathematical Olympiad
- Place: Wuhan, Hubei
- Language: English

## Problem

Fix a prime number $p \ge 5$, and put $\Omega = \{1, 2, \dots, p\}$. For any $x, y \in \Omega$, define
$$
r(x, y) = \begin{cases} y - x, & \text{if } y \ge x, \\ y - x + p, & \text{if } y < x. \end{cases}
$$
For a nonempty subset $A$ of $\Omega$, define
$$
f(A) = \sum_{x \in A} \sum_{y \in A} (r(x, y))^2.
$$
We say that a subset $A$ of $\Omega$ is *good* if $0 < |A| < p$ and for any subset $B$ of $\Omega$ with $|B| = |A|$, we have $f(B) \ge f(A)$.
Determine the maximal positive integer $L$, such that there exist pairwise distinct good subsets $A_1, A_2, \dots, A_L$ of $\Omega$ such that $A_1 \subset A_2 \subset \dots \subset A_L$.
