# kor_2016_3ddc3f

KMO | South Korea | 2016 | March 19, 2016 (Day 1) | Problem 2

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [kor_2016_3ddc3f](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2016_3ddc3f.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: South Korea
- Title: The 29th KOREAN MATHEMATICAL OLYMPIAD
- Year: 2016
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $a_i$ be the number of chosen points on the line $y = i$. If $a_i \ge 2$ and $x_1 < x_2 < \dots < x_{a_i}$ are the x-coordinates of the chosen points on the line $y = i$, then because
$$
x_1 + x_2 < x_1 + x_3 < x_2 + x_3 < x_2 + x_4 < x_3 + x_4 < \dots < x_{a_1-1} + x_{a_1}
$$
we deduce that the number of distinct sums of two x-coordinates among chosen points on $y = i$ is at least $2a_i - 3$. This also holds trivially if $a_i < 2$.
There are $2n - 3$ distinct values that can be obtained as a sum of two integers between 1 and $n$. Since
$$
\sum_{i=1}^{n} (2a_i - 3) = 2k - 3n \ge 5n - 2 - 3n = 2n - 2 > 2n - 3,
$$
by the pigeonhole principle, there exist four distinct chosen points $(x_1, y_1)$, $(x'_1, y'_1)$, $(x_2, y_2)$ such that $x_1 + x'_1 = x_2 + x'_2$ and $y_1 \ne y_2$. There exists a circle going through these four points.
