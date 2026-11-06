# vnm_2012_e6adf8

VMO | Vietnam | 2012 | Southern Winter School 2012. MOCK TEST FOR VMO PREPARATION 2013 | Problem 7.

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [vnm_2012_e6adf8](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_e6adf8.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Vietnam

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

a. We call a pair $(a, b)$ regular if the difference between $a$ and $b$ is less than $2013$. Suppose that in the given regular partition, $a_1$ is paired with $b_i$, $1 \le i \le n$ and $b_1$ is paired with $a_j$, $1 \le j \le n$.
We have $-2013 < a_1 - b_i < 2013$ and $-2013 < a_j - b_1 < 2013$.
Therefore, $a_1 - b_1 \ge a_j - b_1 > -2013$ and $a_1 - b_1 \le a_1 - b_j < 2013$, or
$$
-2013 < a_1 - b_1 < 2013.
$$
Similarly, we also have $-2013 < a_j - b_i < 2013$. Hence, if we change pairs $(a_1, b_i), (a_j, b_1)$ into pairs $(a_1, b_1), (a_j, b_i)$ then we still have a regular partition. Remove the pair $(a_1, b_1)$, we have $2(n-1)$ numbers that can be divided into $n-1$ regular pairs. Repeating this argument, we see that $(a_2, b_2)$ is also a regular pair and generally, all $(a_i, b_i)$, $i=1,2,3,...,n$ are regular.
This implies that the partition $(a_1, b_1), (a_2, b_2),..., (a_n, b_n)$ is regular. The first part of the problem is solved.

b. We will prove by induction that the least number of regular partitions for such $2n$ numbers is $2^{\lfloor(n+1)/2\rfloor}$ for all positive integer $n$. $(*)$
- For $n=2$, we have four numbers $a_1 > a_2$ and $b_1 > b_2$. From the given assumption, $(a_1, b_2), (a_2, b_1)$ is a regular partition. From part a, the partition $(a_1, b_1), (a_2, b_2)$ is also regular. The statement $(*)$ holds for $n=2$.

- For $n=3$, we have six numbers $a_1 > a_2 > a_3$ and $b_1 > b_2 > b_3$. Suppose that $(a_1, b_2)$ is a regular pair in the given regular partition (similarly in the case $(a_1, b_3)$ is regular). Then $(a_2, b_3), (a_3, b_1)$ are the remaining regular pairs in the given partition. We have $-2013 < a_1 - b_2 < 2013$, $a_2 - b_1 < a_1 - b_1 < 2013$ and $a_2 - b_1 > a_3 - b_1 > -2013$ so the pair $(a_2, b_1)$ is regular. We also have $-2013 < a_2 - b_3 < 2013$, $a_3 - b_2 < a_2 - b_2 < 2013$ and $a_3 - b_2 > a_3 - b_1 > -2013$, so the pair $(a_3, b_2)$ is also regular.
Therefore, we have at least $4$ regular partitions when $n=3$:
$$
\begin{cases}
(a_1, b_1), (a_2, b_2), (a_3, b_3) \\
(a_1, b_1), (a_2, b_3), (a_3, b_2) \\
(a_1, b_2), (a_2, b_3), (a_3, b_1) \\
(a_1, b_2), (a_2, b_1), (a_3, b_3)
\end{cases}
$$

- Suppose that the statement $(*)$ holds up to $n-1 \ge 3$, consider $2n$ positive reals
$$
a_1 > a_2 > a_3 > \dots > a_n \text{ and } b_1 > b_2 > b_3 > \dots > b_n.
$$
By the assumption, there exists a regular partition such that $i \ne j$ for each pair $(a_i, b_j)$ in this partition. Suppose that $(a_1, b_1)$ and $(a_j, b_n)$ ($1 < i, j \le n$) are two regular pairs in this partition. From part a), the partition $(a_1, b_1), (a_2, b_2), \dots, (a_n, b_n)$ is also regular.
We have two cases:
- If $a_1 \ge b_2$ then $a_1 - b_2 \ge a_i - b_2 > -2013$ and $a_1 - b_2 \le a_1 - b_j < 2013$. Hence, $(a_1, b_2)$ is a regular pair.
- If $a_1 < b_2$ then $a_1 - b_2 \le a_1 - b_i < 2013$ and $a_1 - b_2 > a_1 - b_1 > -2013$. Hence, $(a_1, b_2)$ is a regular pair.
Therefore, in any case, $(a_1, b_2)$ is regular. Similarly, $(a_2, b_1)$ is also regular.
For the pair $(a_3, b_4)$, we also have two cases:
Case 1. Suppose that $(a_3, b_4)$ is non-regular. In this case, $(a_3, b_3)$ is regular so $b_3 > b_4 > a_3$ is impossible. Hence $a_3 > b_4$ and $a_3 - b_4 > 2013$.

It means $a_3 - b_i > 2013, i \ge 4$, or $(a_3, b_i), i \ge 4$ are all non-regular. This implies that $a_3$ can only be paired with $b_1, b_2, b_3$ to make a regular pair.
We also have $a_1 - b_4 > a_2 - b_4 > a_3 - b_4 > 2013$ so all $(a_1, b_i), (a_2, b_i), i \ge 4$ are non-regular. Therefore, $a_1, a_2, a_3$ can only be paired with $b_1, b_2, b_3$.
By the induction assumption, the least number of regular partitions for the first three pairs is $2^2$, and the least number of regular partitions for the remaining $n-3$ pairs is $2^{[(n-3)/2]}$. Hence, the least number of regular partitions in total is $2^{2+[(n-3)/2]} = 2^{[(n+1)/2]}$.

Case 2. Suppose that $(a_3, b_4)$ is regular. Then we have $(a_4, b_3)$ is also regular. We move to the pair $a_5, b_6$; if $(a_5, b_6)$ is non-regular then we can do similar as the above, $a_1, a_2, a_3, a_4, a_5$ can only be paired with $b_1, b_2, b_3, b_4, b_5$. Repeating the above arguments, we have only one case left: all considered pairs are regular. We then have two subcases:

Subcase 2.1. Suppose that $n$ is even. We have $n/2$ pairs of indexes and $(a_{2i-1}, b_{2i}), (a_{2i}, b_{2i-1})$ ($1 \le i \le n/2$) are all regular. This implies that we have $2^{n/2} = 2^{[(n+1)/2]}$ regular partitions in this case.

Subcase 2.2. Suppose that $n$ is odd. We have the following regular partitions:
$$
(a_{2k+1}, b_{2k}), (a_{2k}, b_{2k+1}), (a_{2k-1}, b_{2k-2}), (a_{2k-2}, b_{2k-1}), \dots, (a_5, b_4), (a_4, b_5).
$$
For the first six numbers $a_1, a_2, a_3, b_1, b_2, b_3$, we have two possibilities:
- If there exists a regular pair $(a_1, b_3)$ or $(a_3, b_1)$ then there are at least $4$ regular partitions in these numbers (as in the case $n=3$.)
- If $(a_1, b_3)$ and $(a_3, b_1)$ are non-regular then we can divide these $2n$ numbers into two disjoint parts: a pair $(a_1, a_2)$ and the remaining $2(n-1)$ numbers. By the induction assumption, the least number of regular partitions in this case is $2^1 \cdot 2^{(n-1)/2} = 2^{(n+1)/2}$.

- Suppose that $n$ is even. We have two sequences:
$$
a_{2i} = b_{2i} = (n/2 - i)k + n/2 - i + 1,\quad a_{2i-1} = b_{2i-1} = (n/2 - i)k + n/2 - i + 2,\quad i \ge 1.
$$
| Index | n | n-1 | n-2 | n-3 | n-4 | n-5 | n-6 | n-7 | ... |
|-------|---|-----|-----|-----|-----|-----|-----|-----|-----|
| $a_i$ | 1 | 2   | $k+2$ | $k+3$ | $2k+3$ | $2k+4$ | $3k+4$ | $3k+5$ |     |
| $b_i$ | 1 | 2   | $k+2$ | $k+3$ | $2k+3$ | $2k+4$ | $3k+4$ | $3k+5$ |     |

- Suppose that $n$ is odd. We have two sequences:
$a_n = b_n = 1, a_{n-1} = b_{n-1} = k-1, a_{n-2} = k, b_{n-2} = k+1$, and
$$
a_{2k} = b_{2k} = ((n-2k+1)i/2 + ((n-2k-1)i/2),\quad a_{2k-1} = b_{2k-1} = ((n-2k+1)i/2 + ((n-2k+1)i/2) \text{ when } 2k+1 < n.
$$
| Index | n | n-1 | n-2 | n-3 | n-4 | n-5 | n-6 | ... | ... |
|-------|---|-----|-----|-----|-----|-----|-----|-----|-----|
| $a_i$ | 1 | $k-1$ | $k$ | $2k+1$ | $2k+2$ | $3k+2$ | $3k+3$ |     |     |
| $b_i$ | 1 | $k-1$ | $k+1$ | $2k+1$ | $2k+2$ | $3k+2$ | $3k+3$ |     |     |

It is easy to check that the above sequences satisfy the given condition.
Therefore, the least number of regular partitions is $2^{\lfloor \frac{n+1}{2} \rfloor}$, $n \ge 2$.

