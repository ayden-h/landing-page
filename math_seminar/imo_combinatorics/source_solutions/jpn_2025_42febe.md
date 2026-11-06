# jpn_2025_42febe

JMO | Japan | 2025 | FIRST ROUND | 7

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2025_42febe](https://mathnet.mit.edu/data_v2/full/japan/jpn_2025_42febe.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: The 35th Japanese Mathematical Olympiad
- Year: 2025
- Organization: The Mathematical Olympiad Foundation of Japan
- Publisher: The Mathematical Olympiad Foundation of Japan
- Series: Japan Mathematical Olympiad
- Volume: 35
- Issue: The First Round • The Final Round
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

$20!^3$

Let $k$ and $l$ be positive integers. We denote by $(k, l)$ the cell in the $k$-th column from the left and the $l$-th row from the bottom. For the cell $(k, l)$, we define its *height* as $k + l - 1$. Note that the possible values for the height of a cell range from 1 to 44. For each integer $1 \le i \le 44$, the sequence formed by the numbers written in the cells of height $i$, listed from the upper-left to the lower-right, is called the *level-$i$ sequence* or *level sequence of height $i$*.

In the operation, for the chosen cells $A_1, \dots, A_k$, the height of $A_{i+1}$ is one more than that of $A_i$ for every $1 \le i \le k-1$. In particular, the following properties hold:
(1) For every $1 \le i \le 44$, the level-$i$ sequence contains no repeated numbers.
(2) Let $p$ and $q$ be integers with $1 \le p < q \le 44$, and let $n$ be a positive integer. If there are cells of height $p$ and $q$ with the number $n$ written in them, then for every integer $i$ with $p \le i \le q$, there exists a cell of height $i$ that has the number $n$ written in it.
(3) Let $i$ and $n$ be positive integers. If there exist cells of height $i$ and $i+1$ that both have the number $n$ written in them, then these two cells are adjacent.

Since there are 20 cells of height 20, Alice must perform at least 20 turns. Conversely, in the $n$-th turn ($1 \le n \le 20$), if Alice chooses $k=25$ and $A_i = (i, n)$ for $1 \le i \le 25$, she can fill the entire board in exactly 20 turns. Therefore, the minimum number of turns is 20.

From now on, we consider the possible numberings when the game ends in exactly 20 turns.
In this case, since only the numbers 1 through 20 are filled, by (1), the level-20 sequence must be a permutation of 1, 2, ..., 20.

**Lemma 1.** The level sequences of height 20, 21, ..., 25 are all identical.
**Proof.** Since there are also 20 cells of each height 21, 22, 23, 24, and 25, by the same reason as in the case of height 20, the level sequences of height 20, 21, ..., 25 are all permutations of 1, 2, ..., 20.
Let $l$ be the first term of the level-20 sequence. That is, $l$ is the number written in the cell $(1, 20)$. Then, by (3), the cell of height 21 in which $l$ is written must be $(2, 20)$.
Let $m$ be the second term of the level-20 sequence. That is, $m$ is the number written in the cell $(2, 19)$. Then, by (3), the possible cells of height 21 where $m$ could be written are $(2, 20)$ or $(3, 19)$. However, since $l$ is already written in $(2, 20)$, $m$ must be written in $(3, 19)$.
Continuing this consideration, for every integer $k$ with $1 \le k \le 20$, it turns out that the cell $(k+1, 21-k)$ contains the $k$-th term of the level-20 sequence. Therefore, the level-21 sequence is identical to the level-20 sequence. Similarly, the level sequences of heights 22, 23, 24, and 25 are also identical to it. ■

**Lemma 2.** For each integer $1 \le i \le 19$, the level-$i$ sequence is equal to the sequence obtained from the level-$(i+1)$ sequence by deleting exactly one term while preserving the order.
**Proof.** Suppose that $n$ appears in the level-$i$ sequence. Since the level-20 sequence is a permutation of $1, 2, \dots, 20$, the number $n$ also appears in the level-20 sequence. Therefore, by (2), $n$ must also appear in the level-$(i+1)$ sequence. This shows that exactly one number appears in the level-$(i+1)$ sequence but not in the level-$i$ sequence. Let this number be the $j$-th term of the level-$(i+1)$ sequence.
Then, by applying the same argument in the proof of Lemma 1 in the order $k = 1, 2, \dots, j-1$, we can show that for any integer $k$ with $1 \le k \le j-1$, the $k$-th term of the level-$i$ sequence is equal to the $k$-th term of the level-$(i+1)$ sequence. Similarly, by applying the same argument in the reverse order $k = i, i-1, \dots, j+1$, we can show that for any integer $k$ with $j+1 \le k \le i$, the $k$-th term of the level-$i$ sequence is equal to the $(k+1)$-th term of the level-$(i+1)$ sequence, thus the lemma is proved. ■

**Lemma 3.** For each integer $25 \le i \le 43$, the level-$(i+1)$ sequence is equal to the sequence obtained from the level-$i$ sequence by deleting exactly one term while preserving the order.
**Proof.** The proof is similar to that of Lemma 2. ■

(i) The level sequences of height 20, 21, ..., 25 are all identical and are permutations of 1, 2, ..., 20.
(ii) For every integer $1 \le i \le 19$, the level-$i$ sequence is obtained from the level-$(i+1)$ sequence by deleting exactly one term while preserving the order.
(iii) For every integer $25 \le i \le 43$, the level-$(i+1)$ sequence is obtained from the level-$i$ sequence by deleting exactly one term while preserving the order.

Conversely, we will show that any numbering that satisfies the conditions (i), (ii), and (iii) can be realized as the final result of the game. Let $X$ be a numbering that satisfies (i), (ii), and (iii). Fix an integer $n$ with $1 \le n \le 20$, and let $m$ be the minimum and $M$ the maximum of the heights in which the number $n$ appears in $X$. From (i), we have $m \le 20$ and $M \ge 25$. From (ii) and (iii), it follows that for any $m \le i \le M$, the level-$i$ sequence also contains the number $n$ exactly once. Suppose that $n$ appears in the $l_i$-th term of the level-$i$ sequence. Then, by conditions (i), (ii), and (iii), for any $m \le i < M$, the $l_{i+1}$-th cell in the level-$(i+1)$ sequence is either to the right or above the $l_i$-th cell of the level-$i$ sequence. Therefore, in the $n$-th turn, Alice can choose $k = M - m + 1$, and $A_i$ as the $l_{m+i-1}$-th cell in the level-$(m + i - 1)$ sequence for each $i = 1, 2, \dots, k$, and in this case, the final numbering coincides with $X$.

Hence, it is sufficient to count the numberings satisfying (i), (ii), and (iii). First, there are $20!$ ways to fill the cells of heights 20, 21, ..., 25 satisfying (i). Fix one such filling. Then, the number of ways to fill the cells of heights 1, 2, ..., 19 satisfying (ii) is equal to the number of ways to successively remove one integer at a time from the set $\{1, 2, ..., 20\}$, which is $20!$. Similarly, the number of ways to fill the cells of heights 26, 27, ..., 44 satisfying (iii) is also $20!$. Therefore, the total number of possible final numberings is $20! \cdot 20! \cdot 20! = 20!^3$.

