# rou_2016_dce07f

RMM | Romania | 2016 | First Day | Problem 2.

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [rou_2016_dce07f](https://mathnet.mit.edu/data_v2/full/romania/rou_2016_dce07f.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Romania
- Title: ROMANIAN MATHEMATICAL COMPETITIONS
- Year: 2016
- Authors: Andronache, Mariean; Bălună, Mihail; Eckstein, Andrei; Enescu, Bogdan; Gherghe, Cătălin; Gologan, Radu; Perianu, Marius; Popescu, Călin; Şerbănescu, Dinu
- Editors: Negrescu, Alexandru
- Organization: Romanian Mathematical Society
- Series: Romanian Mathematical Contests
- Volume: 23
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

The required maximum is $mn - \lfloor m/2 \rfloor$ and is achieved by the brick-like vertically symmetric arrangement of blocks of $n$ and $n-1$ horizontal dominoes placed on alternate rows, so that the bottom row of the board is completely covered by $n$ dominoes.
To show that the number of dominoes in an arrangement satisfying the conditions in the statement does not exceed $mn - \lfloor m/2 \rfloor$, label the rows upwards $0, 1, \ldots, m-1$, and, for each $i$ in this range, draw a vertically symmetric block of $n-i$ fictitious horizontal dominoes in the $i$-th row (so the block on the $i$-th row leaves out $i$ cells on either side) – Figure 4 illustrates the case $m=n=6$. A fictitious domino is *good* if it is completely covered by a domino in the arrangement; otherwise, it is *bad*.
If the fictitious dominoes are all good, then the dominoes in the arrangement that cover no fictitious domino, if any, all lie in two triangular regions of side-length $m-1$ at the upper-left and upper-right corners of the board. Colour the cells of the board chess-like and notice that in each of the two triangular regions the number of black cells and the number of white cells differ by $\lfloor m/2 \rfloor$. Since each domino covers two cells of different colours, at least $\lfloor m/2 \rfloor$ cells are not covered in each of these regions, and the conclusion follows.

To deal with the remaining case where bad fictitious dominoes are present, we show that an arrangement satisfying the conditions in the statement can be transformed into another such with at least as many dominoes, but fewer bad fictitious dominoes. A finite number of such transformations eventually leads to an arrangement of at least as many dominoes all of whose fictitious dominoes are good, and the conclusion follows by the preceding.

Consider the row of minimal rank containing bad fictitious dominoes – this is certainly not the bottom row – and let $D$ be one such. Let $\ell$, respectively $r$, be the left, respectively right, cell of $D$ and notice that the cell below $\ell$, respectively $r$, is the right, respectively left, cell of a domino $D_1$, respectively $D_2$, in the arrangement.
If $\ell$ is covered by a domino $D_\ell$ in the arrangement, since $D$ is bad and no two dominoes in the arrangement form a square, it follows that $D_\ell$ is vertical. If $r$ were also covered by a domino $D_r$ in the arrangement, then $D_r$ would also be vertical, and would therefore form a square with $D_\ell$ – a contradiction. Hence $r$ is not covered, and there is room for $D_\ell$ to be placed so as to cover $D$, to obtain a new arrangement satisfying the conditions in the statement; the latter has as many dominoes as the former, but fewer bad fictitious dominoes. The case where $r$ is covered is dealt with similarly.
Finally, if neither cell of $D$ is covered, addition of an extra domino to cover $D$ and, if necessary, removal of the domino above $D$ to avoid formation of a square, yields a new arrangement satisfying the conditions in the statement; the latter has at least as many dominoes as the former, but fewer bad fictitious dominoes. (Figure 5 illustrates the two cases.)

## Supplied solution 2

*Alternative Solution.* (sketch by Ilya Bogdanov) We present an alternative proof of the bound.

Label the rows upwards $0, 1, \dots, m-1$, and the columns from the left to the right by $0, 1, \dots, 2n-1$; label each cell by the pair of its column's and row's numbers, so that $(1, 0)$ is the second left cell in the bottom row. Colour the cells chess-like so that $(0, 0)$ is white. For $0 \le i \le n-1$, we say that the *$i$th white diagonal* is the set of cells of the form $(2i + k, k)$, where $k$ ranges over all appropriate indices. Similarly, the *$i$th black diagonal* is the set of cells of the form $(2i + 1 - k, k)$. (Notice that the white cells in the upper-left corner and the black cells in the upper-right corner are not covered by these diagonals.)

**Claim.** Assume that $K$ lowest cells of some white diagonal are all covered by dominoes. Then all these $K$ dominoes face right or up from the diagonal. (In other words, the black cell of any such domino is to the right or to the top of its white cell.) Similarly, if $K$ lowest cells of some black diagonal are covered by dominoes, then all these dominoes face left or up from the diagonal.

*Proof.* By symmetry, it suffices to prove the first statement. Assume that $K$ lowest cells of the $i$th white diagonal is completely covered. We prove by induction on $k < K$ that the required claim holds for the domino covering $(2i + k, k)$. The base case $k = 0$ holds due to the problem condition. To establish the step, one observes that if $(2i + k, k)$ is covered by a domino facing up or right, while $(2i + k + 1, k + 1)$ is covered by a domino facing down or left, then these two dominoes form a square.

We turn to the solution. We will prove that there are at least $d = \lfloor m/2 \rfloor$ empty white cells. Since each domino covers exactly one white cell, the required bound follows.
If each of the first $d$ white diagonals contains an empty cell, the result is clear. Otherwise, let $i < d$ be the least index of a completely covered white diagonal. We say that the dominoes covering our diagonal are *distinguished*. After removing the distinguished dominoes, the board splits into two parts; the left part $L$ contains $i$ empty white cells on the previous diagonals. So, it suffices to prove that the right part $R$ contains at least $d - i$ empty white cells.

