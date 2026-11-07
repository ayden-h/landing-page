# bmo_2014_96ebbd

BMO-SL | Balkan Mathematical Olympiad | 2014 | Algebra | A3

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2014_96ebbd](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_96ebbd.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: 31st Balkan Mathematical Olympiad
- Subtitle: Problem Shortlist with solutions
- Year: 2014
- Editors: Kolev, Emil; Ivanov, Alexander; Beluhov, Nikolay
- Organization: Balkan Mathematical Olympiad
- Place: Pleven, Bulgaria
- Series: Balkan Mathematical Olympiad
- Volume: 31
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

First, for $k \in \mathbb{N}$, $k \ge 2$, we have
$$
a_{2k+1} + a_{2k-1} = 2a_{2k} - a_k + a_{2k-1} = 5a_{2k-1} - a_k \equiv -a_k \pmod{5}. \quad (1)
$$
We prove the assertion of the problem by induction on $k$, where $n = 8k+3$. For the base case $k=1$, we compute $a_3 = 1$, $a_4 = 2$, $a_5 = 3$, $a_6 = 6$, $a_7 = 11$, $a_8 = 22$, $a_9 = 42$, $a_{10} = 84$ and $a_{11} = 165$.
By repeatedly applying (1), we have
$$
\begin{align*}
a_{8(k+1)+3} - a_{8k+3} &= (a_{8k+11} + a_{8k+9}) - (a_{8k+9} + a_{8k+7}) \\
&\quad +(a_{8k+7} + a_{8k+5}) - (a_{8k+5} + a_{8k+3}) \\
&\equiv -a_{4k+5} + a_{4k+4} - a_{4k+3} + a_{4k+2} \\
&\quad = -a_{4k+5} + a_{4k+3} + 2a_{4k+1} \\
&\quad = -(a_{4k+5} + a_{4k+3}) + 2(a_{4k+3} + a_{4k+1}) \\
&\equiv a_{2k+2} - 2a_{2k+1} = 0 \pmod{5}.
\end{align*}
$$
Therefore, if $a_{8k+3}$ is divisible by 5, so is $a_{8(k+1)+3}$. This completes the proof.
