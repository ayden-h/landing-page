# bmo_2024_4b7efa

BMO-SL | Balkan Mathematical Olympiad | 2024 | Combinatorics | C2.

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2024_4b7efa](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_4b7efa.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: Problem Shortlist
- Subtitle: with solutions
- Year: 2024
- Authors: Harizanov, Stanislav; Kolev, Emil; Cherkashin, Danila; Boev, Stoyan; Gerdjikov, Stefan
- Organization: Balkan Mathematical Olympiad
- Place: Varna, Bulgaria
- Series: Balkan Mathematical Olympiad
- Volume: 41st
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We show that the answer is all values from $2n$ to $2n^2 + 1$. Assume $f$ has $k \in \{0, 1, \dots, n^2\}$ fixed points. Then say $|\text{Im}(f)| = p$. Also let $s = \max_{k \in S} |f^{-1}(k)|$.

Upper Bound: From the definitions of $s$ and $p$, we get $sp \ge n^2$. We also have the bound $s \le n^2 - p + 1$ (as $p$ values are in the image, each of which has at least 1 preimage). We deduce the upper bound:
$$
k + p + s \le 2k + i + (n^2 - p + 1) = n^2 + k + 1 \le 2n^2 + 1.
$$

Lower Bound: For the minimum value, using AM-GM we get $k + p + s \ge k + p + \frac{n^2}{p} \ge k + 2n \ge 2n$.

Now we show all those values are achievable by induction on $n$. A manual check solves the base case of $n = 2$ (the identity achieves the maximum value of 9, a 2-to-1 function can take the values 4, 5, 6 depending on the number of fixed points, and a function that's 3-to-1 on three of the inputs can achieve 7 and 8). For the inductive hypothesis now, suppose we have a function $g : S \to S$ and let $T = \{1, 2, \dots, (n+1)^2\}$. We will build a function $f : T \to T$ from $g$ by $f(x) = g(x)$ for $x \le n^2$.

Values from $4n+1$ to $2(n+1)^2+1$: For the values bigger than $n^2$, $f$ can now be defined as any permutation of the numbers $\{n^2+1, \dots, (n+1)^2\}$. Obviously, this won't add to the maximum size of a preimage, and it will add $2n+1$ to the size of the image. For the number of fixed points, this can be any number from 0, 1, ..., $2n+1$. So using this, we can add any number from $2n+1$ to $4n+2$ to the value of the expression for $g$, which means, by the inductive hypothesis, we can hit all values $4n+1$ to $2n^2+1+(4n+2) = 2(n+1)^2+1$.

Values from $2n+2$ to $4n$: If $s \ge n+1$, then send $n$ of the new points (from $n^2+1$ to $(n+1)^2$) to one of those new points and the other $n+1$ points to another one of the new points in such a way that we don't add new fixed points. This way, we don't increase the maximum preimage size or the number of fixed points, but we add 2 to the image size. On the other hand, if $s \le n$, then $|\text{Im}(f)| \ge n$. If $|\text{Im}(f)| \ge n+1$, take $n+1$ of the new points, assign each of them to exactly one of the elements in $\text{Im}(f)$. The other $n$ new points will all get mapped to another new point (again, with no new fixed points). This way we add no fixed points, we add 1 point in the image, and we increase the maximum preimage by 1, so again we add 2 overall. The remaining case is when $s = |\mathrm{Im}(f)| = n$. In this case we can only assign $n$ of the new points to exactly one of the new elements in $\mathrm{Im}(f)$ and we map the other $n+1$ to a single new point.

In all cases, we add 2 to the expression overall, so we can get all values $2n+2, \dots, 2n^2+3$, and that covers all values. $\Box$
