# bmo_2017_5eecca

BMO-SL | Balkan Mathematical Olympiad | 2017 | COMBINATORICS | C5

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2017_5eecca](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2017_5eecca.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: PROBLEM SHORTLIST
- Subtitle: (with solutions)
- Year: 2017
- Authors: Malcheski, Risto; Petrushevski, Mirko; Dimovski, Pavel; Velinov, Daniel; Dimovski, Tomi
- Organization: Union of Mathematicians of Macedonia
- Publisher: Union of Mathematicians of Macedonia
- Place: Ohrid, Macedonia
- Series: Balkan Mathematical Olympiad
- Issue: 34
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

The answer turns out to be $\binom{2n-1}{n}$ if $n$ is odd and $\binom{2n-1}{n} - 2\binom{3n-1}{n}$ if $n$ is even.

Case 1. Suppose $n$ is odd, say $n=2m+1$. In this case we will show that any distribution of candies is legal. Thus the number of legal distributions is indeed $\binom{2n-1}{n}$.

In this case we can achieve the above claim by letting each student to always distribute all of its candies to its two neighbouring students in some way. Thus at each step each candy will move either one position clockwise or one anticlockwise.

We now look at the initial distribution of candies and the required final distribution. We specify arbitrarily for each candy in the initial distribution, the position we wish this candy to end up in the required final distribution. Because $n$ is odd, either the clockwise distance or the anticlockwise distance between the initial position of the candy and the required final position is even and at most $m$.

Thus after an even number of steps (at most $m$) we can move each candy to its required final position. (Note that if the candy reaches the required position earlier, we can move it back and forth until all candies reach their required position.) This completes the proof of our claim in this case.

Case 2. Suppose $n$ is even, say $n=2m$. Let $x_1, \dots, x_{2m}$ be the students in this cyclic order.

Observe that initially the students with even indices (even students) have at least one candy in total, and so do the students with odd indices (odd students). This property is preserved after each step.

We will show that every distribution in which the even students have at least one candy in total and the odd students also have at least one candy in total is legal.

Let us suppose that the required final distribution has $a$ candies in odd positions and $b$ candies in even positions. (Where $a, b \ge 1$.) It will be enough to reach any position with $a$ candies in even positions and $b$ candies in odd positions as then we can follow the same approach as in Case 1.

To achieve this we will first move all candies to students $x_1$ and $x_2$. This is easy by specifying that at each step $x_1$ moves all of its candies to $x_2$ while for $1 \le r \le 2m-1$ student $x_{r+1}$ moves all of its candies to $x_r$.

Suppose that we now have $a+k$ candies at $x_1$ and $b-k$ candies at $x_2$ where without loss of generality $k \ge 0$. If $k=0$ we have reached our target. If not, in the next step $x_1$ moves a candy to $x_2$ and $x_2$ moves a candy to $x_3$. In the next step $x_1$ (it still has $a+k-1 \ge a > 0$ candies) moves a candy to $x_2$, $x_2$ moves a candy to $x_1$ and $x_3$ moves a candy to $x_2$. We now have $a+k-1$ candies in $x_1$ and $b+1-k$ in $x_2$. Repeating this process another $k-1$ times we end up with $a$ candies in $x_1$ and $b$ candies in $x_2$ as required.

It remains to count the total number of legal configurations in this case. This is indeed equal to
$$
\binom{2n-1}{n} - 2\binom{3n-1}{n}
$$
as $\binom{2n-1}{n}$ counts the total number of configurations while $\binom{3n-1}{n}$ counts the number of illegal configurations where either all $n$ candies belong to the $\frac{n}{2}$ odd positions or all $n$ candies belong to the $\frac{n}{2}$ even positions.

