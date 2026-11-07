# jpn_2007_ed31dc

JMO | Japan | 2007 | The First Round | 5

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2007_ed31dc](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_ed31dc.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: The 17 Japanese Mathematical Olympiad
- Subtitle: The First Round, The Final Round And The 5 Japanese Junior Mathematical Olympiad
- Year: 2007
- Organization: The Mathematical Olympiad Foundation of Japan
- Series: Japan Mathematical Olympiad

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We will show that in case of $n$ rectangles the answer is $2n^2 - 2n + 2$. We call each divided part region.

$n$ rectangles $R_{1,n}, \dots, R_{i,n+1-i}, \dots, R_{n,1}$ divide plane into $2n^2 - 2n + 2$ regions, where $R_{x,y}$ is a rectangle with corners at $(x, y)$, $(x, -y)$, $(-x, y)$, $(-x, -y)$. Therefore we only have to show that $n$ rectangles cannot divide the plane into more than $2n^2 - 2n + 2$ regions.

Induction. The case $n = 1$ is trivial. Suppose that the case $n = k$ is true. Let $R_1, \dots, R_{k+1}$ be $k+1$ rectangles with the property in the problem, and $D_1, \dots, D_m$ be the regions divided by $R_1, \dots, R_k$. By the induction's hypothesis, we have $m \le 2k^2 - 2k + 2$.

Let $C_i$ be the border of $R_i$. Suppose that for $i \ne j$, $C_i$ and $C_j$ shares finitely many points. (The proof goes the same way if it's not satisfied). Let $P_1, \dots, P_l$ be the intersection of $C_{k+1}$ and $C_1, \dots, C_n$, ordered along $C_{k+1}$. $l \le 4k$ since $C_i$ and $C_{k+1}$ crosses at 4 or less points. Add polygonal lines $P_1P_2, \dots, P_iP_{i+1}, \dots, P_lP_1$ one by one to $D_1, \dots, D_m$. One line increases the number of region by 1 or less, So adding all polygonal lines increases the number of region by $l$ or less.

Since adding $P_1P_2, \dots, P_iP_{i+1}, \dots, P_lP_1$ is equivalent to adding $C_{k+1}$, the number of regions divided by $R_1, \dots, R_{k+1}$ is
$$
m+l \le (2k^2 - 2k + 2) + 4k = 2(k+1)^2 - 2(k+1) + 2.
$$
So we have completed the induction. Therefore, the answer of the problem is 14.
