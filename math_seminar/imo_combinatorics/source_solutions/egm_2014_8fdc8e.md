# egm_2014_8fdc8e

EGMO | European Girls' Mathematical Olympiad (EGMO) | 2014 | Day 2 | 5.

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [egm_2014_8fdc8e](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2014_8fdc8e.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: European Girls' Mathematical Olympiad (EGMO)

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Number the boxes from $1$ through $n$ and denote a configuration by $x = (x_{1}, x_{2}, \ldots, x_{n})$ where $x_{i}$ is the number of pebbles in the $i$th box. Let
$$
D(x) = \sum_{i=1}^{n} \left\lfloor \frac{x_{i} - 1}{2} \right\rfloor
$$
for a configuration $x$. We can rewrite this in the form
$$
D(x) = \frac{1}{2} N(x) - n + \frac{1}{2} O(x)
$$
where $N(x)$ is the total number of pebbles and $O(x)$ is the number of boxes with an odd number of pebbles for the configuration $x$.

Note that a move either leaves $D$ the same (if it is made into a box containing an even number of pebbles) or decreases it by $1$ (if it is made into a box with an odd number of pebbles). As $D$ is nonnegative for any configuration which does not have any empty boxes, it is also nonnegative for any solvable configuration. On the other hand, if a configuration has nonnegative $D$, then making $m_{i} = \left\lfloor (x_{i} - 1) / 2 \right\rfloor$ moves from the $i$th box into $m_{i}$ empty boxes for each $i$ with $m_{i} > 0$ fills all boxes as $D(x) \geq 0$ means $\sum_{m_{i} > 0} m_{i} \geq$ (number of empty boxes).

As $N(x)$ and $O(x)$ have the same parity, a configuration $x$ is solvable exactly when $O(x) \geq 2n - N(x)$, and unsolvable exactly when $O(x) \leq 2n - 2 - N(x)$. In particular, any configuration with $2n - 1$ pebbles is solvable, and a configuration with $2n - 2$ pebbles is unsolvable if and only if all boxes contain even numbers of pebbles.

Suppose that $x'$ is obtained from $x$ by adding a pebble in some box. Then $O(x') = O(x) + 1$ or $O(x') = O(x) - 1$. If $x$ is unsolvable and $x'$ is solvable, then we must have $O(x) \leq 2n - 2 - N(x)$ and $O(x') \geq 2n - N(x') = 2n - 1 - N(x)$, and hence $O(x') = O(x) + 1$. That is, the pebble must be added to a box with an even number of pebbles. This can be the case irrespective of where the pebble is added only if all boxes contain even numbers of pebbles, and $0 = O(x) \leq 2n - 2 - N(x)$ and $1 = O(x') \geq 2n - 1 - N(x)$; that is, $N(x) = 2n - 2$.

## Supplied solution 2

Let $x$ be a configuration and $\tilde{x}$ be another configuration obtained from $x$ by removing two pebbles from a box and depositing them in another box.

Claim 1: $\tilde{x}$ is solvable if and only if $x$ is solvable.

Let us call two configurations equivalent if they have the same total number of pebbles and parities of the number of pebbles in the corresponding boxes are the same. (It does not matter whether we consider this equivalence for a fixed ordering of the boxes or up to permutation.) From Claim 1 it follows that two equivalent configurations are both solvable or both unsolvable. In particular, any configuration with $2n - 1$ or more pebbles is solvable, because it is equivalent to a configuration with no empty boxes.

Let us call a configuration with all boxes containing two or fewer pebbles scant. Every unsolvable configuration is equivalent to a scant configuration.

Claim 2: A scant configuration is solvable if and only if it contains no empty boxes.

By Claim 1 and Claim 2, addition of a pebble to a scant unsolvable configuration makes it solvable if and only if the configuration has exactly one empty box and the pebble is added to the empty box or to a box containing two pebbles. Hence, the addition of a pebble makes an unsolvable scant configuration into a solvable configuration irrespective of where it is added if and only if all boxes have even numbers of pebbles and exactly one of them is empty. Therefore, the addition of a pebble makes an unsolvable configuration into a solvable one irrespective of where the pebble is added if and only if the configuration has $2n - 2$ pebbles and all boxes have even numbers of pebbles.

Proof of Claim 1: Suppose that the two pebbles were moved from box $B$ in $x$ to box $\tilde{B}$ in $\tilde{x}$, and $x$ is solvable. Then we perform exactly the same sequence of moves for $\tilde{x}$ as we did for $x$ except that instead of the first move that is made out of $B$ we make a move from $\tilde{B}$ (into the same box), and if there was no move from $B$, then at the end we make a move from $\tilde{B}$ to $B$ in case $B$ is now empty.

Proof of Claim 2: Any move from a scant configuration either leaves the number of empty boxes the same and the resulting configuration is also scant (if it is made into an empty box), or increases the number of empty boxes by one (if it is made into a nonempty box). In the second case, if the move was made into a box containing one pebble, then the resulting configuration is still scant. On the other hand, if it is made into a box containing two pebbles, then the resulting configuration is equivalent to the scant configuration which has one pebble in the box the move was made into and exactly the same number of pebbles in all other boxes as the original configuration. Therefore, any sequence of moves from a scant configuration results in a configuration with more or the same number of empty boxes.

