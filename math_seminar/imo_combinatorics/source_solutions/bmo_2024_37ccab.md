# bmo_2024_37ccab

BMO-SL | Balkan Mathematical Olympiad | 2024 | Combinatorics | C3.

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2024_37ccab](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_37ccab.json.gz)

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

Let $1 \le a_1 < a_2 < \dots < a_k \le n$ be the numbers Alice chose. For a sequence $x_1 < x_2 < \dots < x_k$ of positive integers, we call its *deficit* the set $N \cap [x_1, x_k] \setminus \{x_1, x_2, \dots, x_k\}$.

Bob has the following strategy: he starts with $a_1 < a_2 < \dots < a_k$. Let $t$ be the maximum number of its deficit. If we denote $\delta = t - a_1 < n - 1$, Bob writes under $a_1$ the number $a'_1 = \delta$. Then $a_1 + a'_1 = t$. If $t < a_2$, then $a_2, a_3, \dots, a_k$ are consecutive and $t = a_2 - 1$. So Bob writes under all the rest $0$, and he gets on the third row a progression with unit ratio.

Otherwise, we have $t > a_2$ and Bob repeats the process, but for the sequence $t, a_2, \dots, a_k$. The lowest term is $a_2$ and its deficit does not have $t$, so has lower cardinal. Therefore, each step decreases the cardinality of the deficit. As long as the deficit is not empty, Bob can perform another step, so in the end the deficit will be empty and the numbers on the third row will form an arithmetic progression with unit ratio.

As the $\delta$ values are strictly decreasing, Bob fulfils the requirement of using numbers from $1$ to $n$ only once. $\square$

