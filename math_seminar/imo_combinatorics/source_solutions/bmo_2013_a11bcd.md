# bmo_2013_a11bcd

BMO | Balkan Mathematical Olympiad | 2013 | Combinatorics | 4

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [bmo_2013_a11bcd](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2013_a11bcd.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: Shortlist Problems and Solution
- Subtitle: Balkan Mathematical Olympiad 2013
- Year: 2013
- Organization: Balkan Mathematical Olympiad
- Place: Agros, Cyprus
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Colour all board squares lying on the outside of $L$ in blue and introduce a Cartesian coordinate system such that the board's lower left and upper right corners have coordinates $(0, 0)$ and $(2n+1, 2n+1)$, respectively. Add one more row, consisting of blue squares only, on top of the board: the lower left corners of the added squares will have coordinates $(i, 2n+1)$ for $0 \le i < 2n$.

No $2 \times 2$ four-square region can contain four squares of the same colour (for in this case the region's center would be a square's vertex in the original board which is not visited by $L$), nor four squares coloured in a checkerboard pattern (for in this case $L$ would intersect itself in the region's center). It follows, then, that every $2 \times 2$ region contains either exactly one pair of horizontally adjacent red squares or exactly one pair of vertically adjacent blue ones. We will refer to neighbouring pairs of these two types as "special" pairs.

Let us fix $y$ and count the total number of special pairs contained in the $2 \times 2$ regions of centers $(i, y)$ for $1 \le i \le 2n$. Each one of these $2n$ regions contains exactly one special pair; each blue special pair is counted exactly twice (a blue special pair cannot lie in the leftmost or rightmost columns for in this case a square vertex in the original board will not be visited by $L$); and each red special pair is counted exactly once. Since the number of regions is even and each blue special pair is counted an even number of times, it follows that the total number of red special pairs in rows $y$ and $y+1$ is even.

The numbers of neighbouring pairs of red squares in all rows must have the same parity, then. The added all-blue top row contains zero neighbouring red pairs, though – an even number – and this completes the proof.

