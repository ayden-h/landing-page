# bmo_2016_bcac10

BMO-SL | Balkan Mathematical Olympiad | 2016 | Combinatorics | C2.

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2016_bcac10](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2016_bcac10.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: 33rd Balkan Mathematical Olympiad
- Subtitle: Shortlisted problems and solutions
- Year: 2016
- Editors: Hoxha, Fatmir; Hysnelaj, Enkel; Puka, Llukan; Baxhaku, Artur; Bojaxhiu, Elton
- Organization: Balkan Mathematical Olympiad
- Place: Tirana, Albania
- Series: Balkan Mathematical Olympiad
- Volume: 33

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

First we show that no larger $k$ can be achieved: We break the day at $45$ disjoint time intervals and assume that at each time interval there were exactly $45$ customers who stayed in the shop only during that time interval (except in the last interval in which there were only $36$ customers). We observe that there are no $46$ people with the required property.

Now we show that $k = 45$ can be achieved: Suppose that customers $C_1, C_2, \dots, C_{2016}$ visited the shop in this order. (If two or more customers entered the shop at exactly the same time then we break ties arbitrarily.)

We define groups $A_1, A_2, \dots$ of customers as follows: Starting with $C_1$ and proceeding in order, we place customer $C_j$ into the group $A_i$ where $i$ is the smallest index such that $A_i$ contains no customer $C_{j'}$ with $j' < j$ and such that $C_{j'}$ was inside the shop once $C_j$ entered it.

Clearly no two customers who are in the same group were inside the shop at the exact same time. So we may assume that every $A_i$ has at most $45$ customers. Since $44 \cdot 45 < 2016$, by the pigeonhole principle there must be at least $45$ (non-empty) groups.

Let $C_j$ be a person in group $A_{45}$ and suppose that $C_j$ entered the shop at time $t_j$. Since we placed $C_j$ in group $A_{45}$ this means that for each $i < 45$, there is a $j_i < j$ such that $C_{j_i} \in A_i$ and $C_{j_i}$ is still inside the shop at time $t_j$.

Thus we have found a specific time instance, namely $t_j$, during which at least $45$ customers were all inside the shop.

