# apm_2010_bde43c

APMO | Asia Pacific Mathematics Olympiad (APMO) | 2010 |  | 3

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [apm_2010_bde43c](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2010_bde43c.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Asia Pacific Mathematics Olympiad (APMO)
- Title: SOLUTIONS FOR 2010 APMO PROBLEMS
- Year: 2010
- Series: APMO Problems
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

When 1 participant, say the person $A$, is mutually acquainted with each of the remaining $n-1$ participants, and if there are no other acquaintance relationships among the participants, then for any pair of participants not involving $A$, the two are not mutual acquaintances, but they have a common acquaintance, namely $A$, so any such pair satisfies the requirement. Thus, the number desired in this case is $\frac{(n-1)(n-2)}{2} = \frac{n^{2}-3 n+2}{2}$.

Let us show that $\frac{n^{2}-3 n+2}{2}$ is the maximum possible number of the pairs satisfying the requirement of the problem. First, let us observe that in the process of trying to find the maximum possible number of such pairs, if we split the participants into two non-empty subsets $T$ and $S$ which are disjoint, we may assume that there is a pair consisting of one person chosen from $T$ and the other chosen from $S$ who are mutual acquaintances. This is so, since if there are no such pair for some splitting $T$ and $S$, then among the pairs consisting of one person chosen from $T$ and the other chosen from $S$, there is no pair for which the two have a common acquaintance among participants, and therefore, if we arbitrarily choose a person $A \in T$ and $B \in S$ and declare that $A$ and $B$ are mutual acquaintances, the number of the pairs satisfying the requirement of the problem does not decrease.

Let us now call a set of participants a group if it satisfies the following 2 conditions:
- One can connect any person in the set with any other person in the set by tracing a chain of mutually acquainted pairs. More precisely, for any pair of people $A, B$ in the set there exists a sequence of people $A_{0}, A_{1}, \cdots, A_{n}$ for which $A_{0}=A, A_{n}=B$ and, for each $i: 0 \leq i \leq n-1, A_{i}$ and $A_{i+1}$ are mutual acquaintances.
- No person in this set can be connected with a person not belonging to this set by tracing a chain of mutually acquainted pairs.

In view of the discussions made above, we may assume that the set of all the participants to the party forms a group of $n$ people. Let us next consider the following lemma.

Lemma. In a group of $n$ people, there are at least $n-1$ pairs of mutual acquaintances.

Proof: If you choose a mutually acquainted pair in a group and declare the two in the pair are not mutually acquainted, then either the group stays the same or splits into 2 groups. This means that by changing the status of a mutually acquainted pair in a group to that of a non-acquainted pair, one can increase the number of groups at most by 1. Now if in a group of $n$ people you change the status of all of the mutually acquainted pairs to that of non-acquainted pairs, then obviously, the number of groups increases from 1 to $n$. Therefore, there must be at least $n-1$ pairs of mutually acquainted pairs in a group consisting of $n$ people.

The lemma implies that there are at most $\frac{n(n-1)}{2}-(n-1)=\frac{n^{2}-3 n+2}{2}$ pairs satisfying the condition of the problem. Thus the desired maximum number of pairs satisfying the requirement of the problem is $\frac{n^{2}-3 n+2}{2}$.

## Supplied solution 2

Alternate Solution 1:

The construction of an example for the case for which the number $\frac{n^{2}-3 n+2}{2}$ appears, and the argument for the case where there is only 1 group would be the same as in the preceding proof.

Suppose, then, $n$ participants are separated into $k$ ($k \geq 2$) groups, and the number of people in each group is given by $a_{i}, i=1, \cdots, k$. In such a case, the number of pairs for which paired people are not mutually acquainted but have a common acquaintance is at most $\sum_{i=1}^{k} {a_{i} \choose 2}$, where we set ${1 \choose 2}=0$ for convenience. Since ${a \choose 2}+{b \choose 2} \leq {a+b \choose 2}$ holds for any pair of positive integers $a, b$, we have $\sum_{i=1}^{k} {a_{i} \choose 2} \leq {a_{1} \choose 2}+{n-a_{1} \choose 2}$.

From
$$
{a_{1} \choose 2}+{n-a_{1} \choose 2}=a_{1}^{2}-n a_{1}+\frac{n^{2}-n}{2}=\left(a_{1}-\frac{n}{2}\right)^{2}+\frac{n^{2}-2 n}{4}
$$
it follows that ${a_{1} \choose 2}+{n-a_{1} \choose 2}$ takes its maximum value when $a_{1}=1, n-1$. Therefore, we have $\sum_{i=1}^{k} {a_{i} \choose 2} \leq {n-1 \choose 2}$, which shows that in the case where the number of groups are 2 or more, the number of the pairs for which paired people are not mutually acquainted but have a common acquaintance is at most ${n-1 \choose 2}=\frac{n^{2}-3 n+2}{2}$, and hence the desired maximum number of the pairs satisfying the requirement is $\frac{n^{2}-3 n+2}{2}$.

## Supplied solution 3

Alternate Solution 2:

Construction of an example would be the same as the preceding proof.

For a participant, say $A$, call another participant, say $B$, a familiar face if $A$ and $B$ are not mutually acquainted but they have a common acquaintance among the participants, and in this case call the pair $A, B$ a familiar pair.

Suppose there is a participant $P$ who is mutually acquainted with $d$ participants. Denote by $S$ the set of these $d$ participants, and by $T$ the set of participants different from $P$ and not belonging to the set $S$. Suppose there are $e$ pairs formed by a person in $S$ and a person in $T$ who are mutually acquainted.

Then the number of participants who are familiar faces to $P$ is at most $e$. The number of pairs formed by two people belonging to the set $S$ and are mutually acquainted is at most ${d \choose 2}$. The number of familiar pairs formed by two people belonging to the set $T$ is at most ${n-d-1 \choose 2}$. Since there are $e$ pairs formed by a person in the set $S$ and a person in the set $T$ who are mutually acquainted (and so the pairs are not familiar pairs), we have at most $d(n-1-d)-e$ familiar pairs formed by a person chosen from $S$ and a person chosen from $T$.

Putting these together we conclude that there are at most $e+{d \choose 2}+{n-1-d \choose 2}+d(n-1-d)-e$ familiar pairs. Since
$$
e+{d \choose 2}+{n-1-d \choose 2}+d(n-1-d)-e=\frac{n^{2}-3 n+2}{2}
$$
the number we seek is at most $\frac{n^{2}-3 n+2}{2}$, and hence this is the desired solution to the problem.

