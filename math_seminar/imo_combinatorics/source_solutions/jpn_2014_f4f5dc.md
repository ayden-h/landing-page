# jpn_2014_f4f5dc

JMO | Japan | 2014 |  | 10

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2014_f4f5dc](https://mathnet.mit.edu/data_v2/full/japan/jpn_2014_f4f5dc.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: The 24th Japanese Mathematical Olympiad
- Subtitle: The First Round, The Final Round
- Year: 2014
- Organization: The Mathematical Olympiad Foundation of Japan
- Series: Japan Mathematical Olympiad
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

$784$

First, we show that the answer we seek is at least $784$.
Let us call the vertices of the squares of the grid lattice points. There are $56^2$ lattice points. For each lattice point, call the set of all the squares of the grid having this lattice point as a vertex its neighborhood. We will first show that in order to reach the configuration satisfying the conditions of the problem, it is necessary to include in the sequence of operations, for every lattice point, an operation involving a rectangle for which it is a vertex.

Note that if a configuration satisfies the conditions of the problem, then for every lattice point there must be at least one black square in its neighborhood. For a lattice point $P$, let us say that an operation is an operation containing $P$ if it chooses a rectangle having $P$ either in its interior or on its sides. If for some lattice point $P$, no operation containing $P$ is performed throughout the process, then all the squares in the neighborhood of $P$ remain white, so the process does not attain the configuration desired. Therefore, at least one operation containing $P$ must be performed.

So, suppose for a lattice point $P$ we consider the last operation containing $P$ that has been performed. If this operation chooses a rectangle containing $P$ in the interior (hence $P$ is not a vertex of the rectangle), then some pair of adjacent squares in the neighborhood of $P$ must have the same color. Thus this process cannot reach the desired configuration, and this implies that the last operation containing $P$ must pick a rectangle having $P$ as its one of the vertices.

Since there are $4$ vertices for a rectangle chosen for an operation, and since there are $56^2$ lattice points, we see that number of operations in a process necessary to achieve the desired configuration is at least $\frac{56^2}{4} = 784$.

Next, we show that there is a process consisting of exactly $784$ operations to reach the desired configuration.
For this purpose, let us consider $28$ rectangles consisting of all the squares lying on $1$st, $3$rd, ... $55$-th row (i.e., odd-numbered rows) from the top and go through $28$ operations of coloring all the squares in the rectangle black starting with the top row. Next take $27$ rectangles consisting of all the squares lying on $2$nd, $4$-th, ... $54$-th column (i.e., even-numbered columns) from the left and go through $27$ operations of coloring all the squares in the rectangle white starting with the left-most row. After these operations, all the squares located at the intersection of an odd-numbered row and an odd-numbered column are colored black and all other squares in the grid are colored white. Finally, for each of $27^2$ squares located at the intersection of an even-numbered row and an even-numbered column, we go through the operation of picking one of these squares in some order and coloring it black till we exhaust all of these squares. Then, we see that we end up with the configuration for which all the three conditions of the problem are satisfied. The number of operations necessary to go through this process is $28 + 27 + 27^2 = 784$, and therefore, the answer we seek is $784$.

