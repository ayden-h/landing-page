# imo_2009_fa6aa0

IMO-SL | IMO | 2009 | Combinatorics | C5

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2009_fa6aa0](https://mathnet.mit.edu/data_v2/full/imo/imo_2009_fa6aa0.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Problem Shortlist with solutions
- Year: 2009
- Editors: Engel, Konrad; Fegert, Karl; Felgenhauer, Andreas; Gronau, Hans-Dietrich; Labahn, Roger; Mulansky, Bernd; Prestin, Jürgen; Reiher, Christian; Scholze, Peter; Specht, Eckard; Strich, Robert; Welk, Martin
- Organization: Federal Ministry of Education and Research; Die Senatorin für Bildung und Wissenschaft; Freie Hansestadt Bremen; Bildung Begabung; JACOBS UNIVERSITY
- Place: Bremen, Germany
- Series: International Mathematical Olympiad
- Volume: 50th
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

No, the Stepmother cannot enforce a bucket overflow and Cinderella can keep playing forever. Throughout we denote the five buckets by $B_{0}, B_{1}, B_{2}, B_{3}$, and $B_{4}$, where $B_{k}$ is adjacent to bucket $B_{k-1}$ and $B_{k+1}$ ($k=0,1,2,3,4$) and all indices are taken modulo $5$. Cinderella enforces that the following three conditions are satisfied at the beginning of every round:

(1) Two adjacent buckets (say $B_{1}$ and $B_{2}$) are empty.

(2) The two buckets standing next to these adjacent buckets (here $B_{0}$ and $B_{3}$) have total contents at most $1$.

(3) The remaining bucket (here $B_{4}$) has contents at most $1$.

These conditions clearly hold at the beginning of the first round, when all buckets are empty.

Assume that Cinderella manages to maintain them until the beginning of the $r$-th round ($r \geq 1$). Denote by $x_{k}$ ($k=0,1,2,3,4$) the contents of bucket $B_{k}$ at the beginning of this round and by $y_{k}$ the corresponding contents after the Stepmother has distributed her liter of water in this round.

By the conditions, we can assume $x_{1}=x_{2}=0$, $x_{0}+x_{3} \leq 1$ and $x_{4} \leq 1$. Then, since the Stepmother adds one liter, we conclude $y_{0}+y_{1}+y_{2}+y_{3} \leq 2$. This inequality implies $y_{0}+y_{2} \leq 1$ or $y_{1}+y_{3} \leq 1$. For reasons of symmetry, we only consider the second case.

Then Cinderella empties buckets $B_{0}$ and $B_{4}$.

At the beginning of the next round $B_{0}$ and $B_{4}$ are empty (condition (1) is fulfilled), due to $y_{1}+y_{3} \leq 1$ condition (2) is fulfilled and finally since $x_{2}=0$ we also must have $y_{2} \leq 1$ (condition (3) is fulfilled).

Therefore, Cinderella can indeed manage to maintain the three conditions (1)-(3) also at the beginning of the $(r+1)$-th round. By induction, she thus manages to maintain them at the beginning of every round. In particular she manages to keep the contents of every single bucket at most $1$ liter. Therefore, the buckets of $2$-liter capacity will never overflow.

## Supplied solution 2

We prove that Cinderella can maintain the following two conditions and hence she can prevent the buckets from overflow:

(1') Every two non-adjacent buckets contain a total of at most $1$.

(2') The total contents of all five buckets is at most $\frac{3}{2}$.

We use the same notations as in the first solution. The two conditions again clearly hold at the beginning. Assume that Cinderella maintained these two conditions until the beginning of the $r$-th round. A pair of non-neighboring buckets $(B_{i}, B_{i+2}), i=0,1,2,3,4$ is called critical if $y_{i}+y_{i+2}>1$. By condition (2), after the Stepmother has distributed her water we have $y_{0}+y_{1}+y_{2}+y_{3}+y_{4} \leq \frac{5}{2}$. Therefore,

$$
(y_{0}+y_{2})+(y_{1}+y_{3})+(y_{2}+y_{4})+(y_{3}+y_{0})+(y_{4}+y_{1})=2(y_{0}+y_{1}+y_{2}+y_{3}+y_{4}) \leq 5
$$

and hence there is a pair of non-neighboring buckets which is not critical, say $(B_{0}, B_{2})$. Now, if both of the pairs $(B_{3}, B_{0})$ and $(B_{2}, B_{4})$ are critical, we must have $y_{1}<\frac{1}{2}$ and Cinderella can empty the buckets $B_{3}$ and $B_{4}$. This clearly leaves no critical pair of buckets and the total contents of all the buckets is then $y_{1}+(y_{0}+y_{2}) \leq \frac{3}{2}$. Therefore, conditions (1') and (2') are fulfilled.

Now suppose that without loss of generality the pair $(B_{3}, B_{0})$ is not critical. If in this case $y_{0} \leq \frac{1}{2}$, then one of the inequalities $y_{0}+y_{1}+y_{2} \leq \frac{3}{2}$ and $y_{0}+y_{3}+y_{4} \leq \frac{3}{2}$ must hold. But then Cinderella can empty $B_{3}$ and $B_{4}$ or $B_{1}$ and $B_{2}$, respectively and clearly fulfill the conditions.

Finally consider the case $y_{0}>\frac{1}{2}$. By $y_{0}+y_{1}+y_{2}+y_{3}+y_{4} \leq \frac{5}{2}$, at least one of the pairs $(B_{1}, B_{3})$ and $(B_{2}, B_{4})$ is not critical. Without loss of generality let this be the pair $(B_{1}, B_{3})$. Since the pair $(B_{3}, B_{0})$ is not critical and $y_{0}>\frac{1}{2}$, we must have $y_{3} \leq \frac{1}{2}$. But then, as before, Cinderella can maintain the two conditions at the beginning of the next round by either emptying $B_{1}$ and $B_{2}$ or $B_{4}$ and $B_{0}$.

