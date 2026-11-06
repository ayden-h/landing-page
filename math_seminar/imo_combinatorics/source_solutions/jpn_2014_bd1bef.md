# jpn_2014_bd1bef

JMO | Japan | 2014 |  | 11

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2014_bd1bef](https://mathnet.mit.edu/data_v2/full/japan/jpn_2014_bd1bef.json.gz)

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

First, we consider how we can obtain an operation that satisfies the two conditions of the problem. Let us begin with the following Lemma:
**Lemma 1:** For every pair of integers $i$ and $j$ with $1 \le i, j \le 6$, $i \diamond j$ is the only integer which appears in both $i$-th row and $j$-th column.
**Proof of Lemma 1:** It is clear that the number $i \diamond j$ appears in both $i$-th row and $j$-th column. Suppose now that for some pair of integers $j'$, $i'$ both lying in between $1$ and $6$, some integer $k$ appears in both the square located on $i$-th row and $j$-th column and the square located on $i'$-th row and $j$-th column, then we have $k \diamond k = (i \diamond j')(i' \diamond j) = i \diamond j$, which implies that $i \diamond j$ is the only number that can appear in both $i$-th row and $j$-th column.

Next, we note that since for any choice of positive integers $i, j, k$ lying in between $1$ and $6$ the identity
$$
i \diamond k = (i \diamond j) \diamond (k \diamond k) \diamond k
$$
holds, we see that distribution of numbers in $i$-th row and $(i \diamond j)$-th row must coincide. Consequently, for any pair of numbers $i_1, i_2$ lying in between $1$ and $6$, no pair $j_1, j_2$ exists for which $i_1 \diamond j_1 = i_2 \diamond j_2$, if the distribution of numbers in $i_1$-th and $i_2$-th rows are different. In other words, for any pair of rows the distributions of integers in them either coincide or there exists no integer which appears in both rows.

On the other hand, for any integer $i$ lying in between $1$ and $6$, $i \diamond i = i$ holds; therefore, in $i$-th row number $i$ appears at least once. In view of this fact and the fact mentioned above, we can conclude that the set $\{1, 2, \dots, 6\}$ of positive integers is partitioned into the collection $I_1, I_2, \dots, I_m$, (where $m$ is a positive integer $\le 6$), of non-empty subsets, which satisfies the following condition:
For any $x \in \{1, 2, \dots, m\}$ and for any $i \in I_x$, the set $I_x$ coincides with the set of all numbers appearing in $i$-th row.

By considering columns instead of rows, we can also obtain the following:
The set $\{1, 2, \dots, 6\}$ of positive integers is partitioned into the collection $J_1, J_2, \dots, J_n$, (where $n$ is a positive integer $\le 6$), of non-empty subsets, which satisfies the following condition:
For any $y \in \{1, 2, \dots, n\}$ and for any $j \in J_y$, the set $J_y$ coincides with the set of all numbers appearing in $j$-th column.

From Lemma 1 it follows that for any pair of numbers $x, y$ with $1 \le x \le m$ and $1 \le y \le n$, there is a unique integer belonging to the set $I_x \cap J_y$. Denote this integer by $(x, y)$. Then we can show the following:
**Lemma 2:** For any choice of $x_1, x_2, y_1, y_2$, $(x_1, y_1) \diamond (x_2, y_2) = (x_1, y_2)$.
**Proof of Lemma 2:** First, we note that for any pair $i \in I_x, j \in J_y$, $(x, y) = i \diamond j$ holds. Therefore, we see that for $i_1 \in I_{x_1}, i_2 \in I_{x_2}, j_1 \in J_{y_1}, j_2 \in J_{y_2}$, we have
$$
\langle x_1, y_1 \rangle \diamond \langle x_2, y_2 \rangle = (i_1 \diamond j_1) \diamond (i_2 \diamond j_2) = i_1 \diamond j_2 = \langle x_1, y_2 \rangle,
$$
proving the Lemma.

Now, since both $I_1, I_2, \dots, I_m$ and $J_1, J_2, \dots, J_n$ are partitions of the set $\{1, 2, \dots, 6\}$, we see that in the enumeration
$$
(\dagger) \quad \langle 1, 1 \rangle, \langle 1, 2 \rangle, \dots, \langle 1, n \rangle, \langle 2, 1 \rangle, \langle 2, 2 \rangle, \dots, \langle 2, n \rangle, \dots \dots \langle m, 1 \rangle, \langle m, 2 \rangle, \dots \langle m, n \rangle,
$$

**Lemma 3:** When positive integers $m, n$ satisfying $mn = 6$ and enumeration ($\dagger$) above of the numbers $1, 2, ..., 6$ are given, assignment of numbers into squares to satisfy the statement of Lemma 2 is uniquely determined, and this assignment satisfies the conditions of the problem.
**Proof of Lemma 3:** First, we note that the two conditions of the problem can be stated in terms of $\langle x, y \rangle$ as follows:
$$
\bullet \quad \langle x, y \rangle \diamond \langle x, y \rangle = \langle x, y \rangle
$$
$$
\bullet \quad (\langle x_1, y_1 \rangle \diamond \langle x_2, y_2 \rangle) \diamond (\langle x_3, y_3 \rangle \diamond \langle x_4, y_4 \rangle) = \langle x_1, y_2 \rangle \diamond \langle x_3, y_4 \rangle = \langle x_1, y_4 \rangle \\ = \langle x_1, y_1 \rangle \diamond \langle x_4, y_4 \rangle.
$$
Since for each $i$ lying in between $1$ and $6$, there is a unique pair $x$ and $y$ for which $i = \langle x, y \rangle$, we see that the claim of Lemma 3 is valid.

Now if we consider an assignment of numbers satisfying the conditions of the problem, then there are $m! \cdot n!$ enumeration ($\dagger$)'s giving this assignment corresponding to the number of permutations of sets $I_1, I_2, \dots, I_m$ and $J_1, J_2, \dots, J_n$. For each pair $m, n$ satisfying $mn = 6$ there are $6!$ different ($\dagger$)'s, and therefore, the number of ways of assignments satisfying the conditions of the problem is $\frac{6!}{m!n!}$, which yields
$$
\frac{6!}{1! \cdot 6!} + \frac{6!}{2! \cdot 3!} + \frac{6!}{3! \cdot 2!} + \frac{6!}{6! \cdot 1!} = 122
$$

