# vnm_2023_3ebb4e

IMO-TST | Vietnam | 2023 | Day 1 (April 13th, 2023) | 1

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [vnm_2023_3ebb4e](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2023_3ebb4e.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Vietnam
- Title: VIETNAMESE MATHEMATICAL COMPETITIONS
- Year: 2023
- Editors: Lữ, Lê Phúc; Nghĩa, Trương Tuấn
- Place: Hanoi
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Arrange $m+n$ students on a circle forming the arcs on which any two students are in the same class, and as few arcs as possible. Obviously with this division, two adjacent arcs contain students who are not in the same class. We claim that the number of students have candies is exactly the same as the number of arcs with at least $i+1$ people. Indeed, if there is a student $X$ with $i$ candies, that means on the left hand side of $X$, there are exactly $i$ classmates, so the arc contains at least $i+1$ people. On the other hand, for each arc that has at least $i+1$ people, the $i+1$ students from the left side has exactly $i$ candies.

a) Since the number of students with $i$ candies is equal to the number of arcs with at least $i+1$ people, the number of students without candy is exactly the same as the number of arcs. On the other hand, the number of students with $i$ candies is equal to the number of arcs with at least $i+1$ people, and does not exceed the number of arcs of people, so the number of students that have $0$ candies is the largest. We will prove that the maximum number of arcs is
$$
2 \min(m, n).
$$
Suppose that $m \le n$. Obviously, the maximum number of arcs that students are both in class $A$ is $m$. On the other hand, the number of arcs containing students from $A$ is equal to the number of arcs containing students from $B$, because between $2$ consecutive arcs containing $A$ classmates there is exactly $1$ arc containing $B$ classmates. So the number of arcs is twice times the number of arcs containing students from $A$ and no more than $2m$. Equivalently, a group has at most $2m$ students. The equality is obtained when we arrange the $m$ arcs with $1$ student from class $A$, and $m$ arcs of students from $B$.

b) For the same argument as above, the number of arcs containing at least $2$ people is equal to the number of students having $1$ of candy, an arc contains at least $i+1$ where $i > 1$ does not exceed the number of arcs containing at least $2$ people, so we count the number of arcs containing at least $2$ person and find the maximum number of such arcs. Assume $m \le n$. If there are $x$ arcs of students from $A$ then there are $x$ arcs of students from $B$. Suppose there are $a$ arcs with at least $2$ classmate of $A$ and $b$ arcs with at least $2$ classmate of $B$. We have two cases.
* If $m < n$ or $m = n$ and they are even. Since the number of arcs includes exactly $1$ classmate of $A$ does not exceed $m - 2a$, so the maximum number of arcs is $m - a$. Thus, $m - a \ge x \ge b$ or $m \ge a + b$. We show the equality holds.
* If $m = 2k$ then divide $A$ into $k$ arcs, each arc has at least $2$ students, this is possible because $m \le n$. So there are $2k$ arcs.

◦ If $m = 2k - 1$ then divide class $A$ into $k - 1$ arcs of $2$ person and remaining $1$ person. Since $m < n$, then $n \ge 2k$, class $B$ can be divided into $k$ arcs, each of which has at least $2$ people. Therefore, we get $2k - 1$ arcs with at least $2$ students and a group has at most $m$ students.
• If $m = n = 2k + 1$. It's easy to see $2a < m$ and $2b < n$ so $a, b < k$ or having a maximum of $2k$ also has at least $2$ people. The equality holds if dividing each class into $k$ arcs, where $k - 1$ contains $2$ friends and $1$ arc contains $3$ friends and then alternates on the circle.

In conclusion, the answer is $m - 1$ when $m = n$ is odd and $\min(m, n)$ in the rest of the cases. $\square$

