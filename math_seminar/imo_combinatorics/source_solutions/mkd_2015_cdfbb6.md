# mkd_2015_cdfbb6

EGMO | North Macedonia | 2015 | Day 2 | 5

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [mkd_2015_cdfbb6](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2015_cdfbb6.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: North Macedonia
- Title: MATHEMATICAL OLYMPIADS
- Subtitle: Macedonian Mathematical Olympiads; Balkan Mathematical Olympiads; European Girl's Mathematical Olympiad; European Mathematical Cup
- Year: 2015
- Authors: Malčeski, Aleksa; Manova-Erakovik, Vesna; Brsakoska, Slagjana; Shoptrajanov, Martin; Prangoski, Bojan; Jovcheski, Ilija; Petrushevski, Mirko; Dimovski, Pavel; Dimovski, Tomi; Andova, Vesna; Filiposki, Slobodan; Angeleska, Jasmina
- Organization: Macedonian Mathematical Society
- Publisher: Union of mathematicians of Macedonia
- Place: Skopje
- Series: Library Olympiads
- Language: English
- Isbn: 978-9989-646-48-5

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Define the following ordered partitions:

$$
P_1 = (\{1,2\}, \{3,4\}, \dots, \{2m-1,2m\})
$$
$$
P_2 = (\{1,m+1\}, \{2,m+2\}, \dots, \{m,2m\})
$$
$$
P_3 = (\{1,2m\}, \{2,m+1\}, \{3,m+2\}, \dots, \{m,2m-1\}).
$$
For each $P_j$ we will compute the possible values for the expression $s = a_1 + \dots + a_m$, where $a_i \in P_{j,i}$, are the chosen integers. Here $P_{j,i}$ denotes the $i$-th coordinate of the ordered partition $P_j$. We will denote by $\sigma$ the number $\sum_{i=1}^m i = \frac{m^2+m}{2}$.

* Consider the partition $P_1$ and a certain choice with corresponding $s$. We find that
$$
m^2 = \sum_{i=1}^{m} (2i-1) \le s \le \sum_{i=1}^{m} 2i = m^2 + m.
$$
Hence, if $n < m^2$ or $n > m^2 + m$, this partition gives a positive answer.

* Consider the partition $P_2$ and a certain choice with corresponding $s$. We find that
$$
s \equiv \sum_{i=1}^{m} i \equiv \sigma (\text{mod } m).
$$
Hence, if $m^2 \le n^2 \le m^2 + m$ and $n \not\equiv \sigma (\text{mod } m)$, this partition solves the problem.

* Consider the partition $P_3$ and a certain choice with corresponding $s$. We set
$$
d_i = \begin{cases} 0, & \text{if } a_i = i \\ 1, & \text{if } a_i \neq i \end{cases}.
$$
We also put $d = \sum_{i=1}^m d_i$, and note that $0 \le d \le m$. Note also that if $a_i \neq i$, then $a_i \equiv i-1 (\text{mod } m)$. Hence, for all $a_i \in P_{3,i}$ it holds that
$$
a_i \equiv i - d_i (\text{mod } m).
$$
Hence,
$$
s \equiv \sum_{i=1}^m a_i \equiv \sum_{i=1}^m (i-d_i) \equiv \sigma - d \pmod{m},
$$
which can only be congruent to $\sigma$ modulo $m$ if all $d_i$ are equal, which forces $s = \frac{m^2+m}{2}$ or $s = \frac{3m^2+m}{2}$. Since $m>1$, it holds that
$$
\frac{m^2+m}{2} < m^2 < m^2+m < \frac{3m^2+m}{2}.
$$
Hence if $m^2 \le n \le m^2+m$ and $n \equiv \sigma \pmod{m}$, then $s$ cannot be equal to $n$, so partition $P_3$ suffices for such $n$.

Note that all $n$ are treated in one of the cases above, so we are done.


**Solution 1B:**

Consider the partition $\{\{1, m+2\}, \{2, m+3\}, \dots, \{m-1, 2m\}, \{m, m+1\}\}$. We consider possible sums mod $m+1$. For the first $m-1$ pairs, the elements of each pair are congruent mod $m+1$, so the sum of one element of each pair is (mod $m+1$) congruent to $\frac{1}{2}m(m+1)-m$, which is congruent to 1 if $m+1$ is odd and $1+\frac{m+1}{2}$ if $m+1$ is even. Now the elements of the last pair are congruent to $-1$ and $0$, so any achievable value of $n$ is congruent to 0 or 1 if $m+1$ is odd, and to 0 or 1 plus $\frac{m+1}{2}$ if $m+1$ is even. If $m$ is even then $m^2+\frac{m}{2}=1+\frac{m}{2}$, which is not congruent to 0 or 1. If $m$ is odd then $m^2 \equiv 1$ and $m^2+m \equiv 0$, neither of which can equal 0 or 1 plus $\frac{m+1}{2}$.


**Solution 1C:**

Similarly, consider the partition $\{\{1, m\}, \{2, m+1\}, \dots, \{m-1, 2m-2\}, \{2m-1, 2m\}\}$ this considering sums of elements of pairs mod $m-1$. If $m-1$ is odd, the sum is congruent to 1 or 2; if $m-1$ is even, to 1 or 2 plus $\frac{m-1}{2}$. If $m$ is even then $m^2+\frac{m}{2}=1+\frac{m}{2}$, and this can only be congruent to 1 or 2 when $m=2$. If $m$ is odd, $m^2$ and $m^2+m$ are congruent to 1 and 2, and these can only be congruent to 1 or 2 plus $\frac{m-1}{2}$ when $m=3$. Now the cases of $m=2$ and $m=3$ need considering separately (by finding explicit partitions excluding each $n$).


Solution 2:

This solution does not use modulo arguments. Use only $P_1$ from the solution 1A to conclude that $m^2 \le n \le m^2+m$. Now consider the partition $\{\{1, 2m\}, \{2, 3\}, \dots, \{2m-2, 2m-1\}\}$. If 1 is chosen from the first pair, the sum is at most $m^2$; if $2m$ is chosen, the sum is at least $m^2+m$. So either $n=m^2$ or $n=m^2+m$. Now consider the partition $\{\{1, 2m-1\}, \{2, 2m\}, \{3, 4\}, \{5, 6\}, \dots, \{2m-3, 2m-2\}\}$. Sums of one element from each of the last $m-2$ pairs are in the range from each $(m-2)m=m^2-2m$ to $(m-2)(m+1)=m^2-m-2$ inclusive. Sums of one element from each of the first two pairs are $3, 2m+1$ and $4m-1$. In the first case we have $n \le m^2-m+1 < m^2$ in the second $m^2+1 \le n \le m^2+m-1$ and in the third $n \ge m^2+2m-1 > m^2+m$. So these three partitions together have eliminated all $n$.

