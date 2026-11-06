# vnm_2002_ddb25c

VMO | Vietnam | 2002 | First Day (March 12, 2002) | Problem 3

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [vnm_2002_ddb25c](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2002_ddb25c.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Vietnam
- Title: THE 2002 VIETNAMESE MATHEMATICAL OLYMPIAD
- Year: 2002
- Organization: MINISTRY OF EDUCATION AND TRAINING OF VIETNAM
- Place: Hanoi
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We enlarge the problem by replacing $2001$ by $p$, $2002$ by $q$ ($m \le p, n \le q$) and prove by induction on $p+q$ that $s \ge (p-m)(q-n)$ (1).
It is easily seen that the assertion (1) is true for $p+q=2, 3, 4$. Suppose that it is true for $p+q=k$.
Consider a $(p, q)$-board with $p+q=k+1$. It is easy to see that (1) is true if $m=p$ or $n=q$. Consider the case where $m<p$ and $n<q$. We call a little square of the board is bad by row or row-bad (resp. bad by column or column-bad) if the number written in this little square is less than at least $n$ numbers (resp. $m$ numbers) written on the same row (resp. column) as the considered little square.
If in the $(p, q)$-board, each row-bad little square is also a column-bad one and each column-bad little square is also a row-bad little square one then it is easily seen that $s = (p-m)(q-n)$, thus (1) is true. Suppose that in the $(p, q)$-board there are little squares that are bad only by row or bad only by column. Let $a$ be the least number written in these little squares. Suppose w. l. o. g. that the little square filling by $a$ is row-bad. Then all $(p-m)$ column-bad little squares lying on the same column as $a$ are bad little squares of the board. By erasing the column containing the little square filling by $a$, we obtain a $(p, q-1)$-board such that a little square of which is bad if and only if it is bad in the previous $(p, q)$-board. Because $p+(q-1)=k$, by induction, we deduce that the number of bad little squares in the $(p, q-1)$-board is not less than $(p-m)(q-1-n)$. Therefore, the number of bad little squares in the $(p, q)$-board is not less than
$$
(p - m)(q - 1 - n) + (p - m) = (p - m)(q - n).
$$
Thus the assertion (1) is proved.
Now we indicate a filling in the $(p, q)$-board such that the number of bad little squares equals $(p-m)(q-n)$: arrange $p \times q$ given numbers in increasing order and put them one after another into the little squares of the board downwards and from left to right.
$$
\text{Thus } s_{\min} = (p - m)(q - n) \text{ and the answer to the given problem is } (2001 - m)(2002 - n)
$$

