# bmo_2010_ced32c

BMO-SL | Balkan Mathematical Olympiad | 2010 | ALGEBRA | A2

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2010_ced32c](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2010_ced32c.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: Balkan Mathematical Olympiad Shortlist 2010: Problems and Solutions
- Year: 2010
- Organization: Balkan Mathematical Olympiad
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

For every $n \in N^*$ from the given recurrence relation we have
$$
a_{n+1} - a_n = (a_n - 1)^2.
$$
So, the sequence $(a_n)$ is increasing and therefore, since $a_1 = 2 > 1$, we have for every $n \in N^*$
$$
a_{n+1} > a_n > 1.
$$
From the given recurrence relation for every $n \geq 2$ we obtain the equalities
$$
a_n - 1 = a_{n-1} (a_{n-1} - 1),
$$
$$
a_{n-1} - 1 = a_{n-2} (a_{n-2} - 1),
$$
$\vdots$
$$
a_2 - 1 = a_1 (a_1 - 1).
$$
$$
a_n = 1 + a_1 a_2 \cdots a_{n-1}.
$$
Dividing both sides of the last relation by $a_1 a_2 \cdots a_{n-1} a_n$ we get
$$
\frac{1}{a_1 a_2 \cdots a_{n-1}} = \frac{1}{a_1 a_2 \cdots a_{n-1} a_n} + \frac{1}{a_n}
$$
or
$$
\frac{1}{a_n} = \frac{1}{a_1 a_2 \cdots a_{n-1}} - \frac{1}{a_1 a_2 \cdots a_{n-1} a_n} \quad (1)
$$
We put $n = 2, 3, 4, \dots, k$ in (1) and adding recursively the relations we get
$$
\sum_{i=2}^{k} \frac{1}{a_i} = \frac{1}{a_1} - \frac{1}{a_1 a_2 \cdots a_{k-1} a_k} \quad \Leftrightarrow \quad \sum_{i=1}^{k} \frac{1}{a_i} = 1 - \frac{1}{a_1 a_2 \cdots a_{k-1} a_k} < 1 \quad (2)
$$
for every $k \in N^*$, since $a_i > 1$ for every $i \in N^*$.
For every $n \in N^*$, $n \ge 2$, from the hypothesis we have $a_n - a_{n-1} = (a_{n-1} - 1)^2 \ge 1$. Therefore, inductively we get
$$
a_n \ge n - 1 + 2 = n + 1 > n.
$$
So, for every $k \in N^*$ we have
$$
0 < \frac{1}{a_1 a_2 \cdots a_{k-1} a_k} < \frac{1}{a_k} < \frac{1}{k}
$$
and
$$
1 - \frac{1}{a_1 a_2 \cdots a_{k-1} a_k} > 1 - \frac{1}{k} \quad (3)
$$
For every $0 \le \alpha < 1$ we'll find $k \in N^*$ such that
$$
\sum_{i=1}^{k} \frac{1}{a_i} > \alpha. \quad (4)
$$
For if
$$
1 - \frac{1}{a_i} > \alpha \Leftrightarrow k-1 > k\alpha \Leftrightarrow k > \frac{1}{1-\alpha} \Leftrightarrow k \ge \left\lfloor \frac{1}{1-\alpha} \right\rfloor + 1, \quad (5)
$$
where $[x]$ denote the largest integer less than or equal to $x$. From the relations (2),(3),(5) we obtain (4). So, $L = 1$. $\square$
