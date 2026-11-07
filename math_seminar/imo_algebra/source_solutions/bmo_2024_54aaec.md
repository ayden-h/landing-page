# bmo_2024_54aaec

BMO-SL | Balkan Mathematical Olympiad | 2024 | Number Theory | N1.

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2024_54aaec](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_54aaec.json.gz)

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

For $n = 1$, the answer is negative. For $n > 1$ we will show that answer is positive. In contrary, since $|S_n| = 4^n$, we see that the set $S_n$ is complete system of remainders modulo $4^n$. Thus,
$$
\sum_{x \in S_n} x^3 \equiv \sum_{i=1}^{4^n} i^3 \pmod{4^n} \equiv \left(\frac{4^n(4^n+1)}{2}\right)^2 \pmod{4^n} \equiv 0 \pmod{4^n}. \quad (\heartsuit)
$$
Let us calculate $\sum_{x \in S_n} x^3$. Denote by $A_n = \sum_{x \in S_n} x$, $B_n = \sum_{x \in S_n} x^2$ and $C_n = \sum_{x \in S_n} x^3$, for all $n \in \mathbb{N}$.
Then:
$$
A_n = \sum_{k=1}^{n} 10^{k-1} 4^{n-1} (1+2+3+4) \equiv 2 \cdot 4^{n-1} \pmod{4^n}, \quad (1)
$$
$$
\begin{aligned}
B_{n+1} &= \sum_{(c,x_n) \in \{1,2,3,4\} \times S_n} (10^n \cdot c + x_n)^2 = \sum_{(c,x_n) \in \{1,2,3,4\} \times S_n} (10^{2n} \cdot c^2 + 2 \cdot 10^n \cdot c \cdot x_n + x_n^2) \\
&= 4^n \cdot 10^{2n} \cdot \sum_{c=1}^{4} c^2 + 2 \cdot 10^n \cdot \sum_{c=1}^{4} c \cdot A_n + 4 \cdot B_n \equiv 4B_n \pmod{4^{n+1}}.
\end{aligned}
$$
Since $B_1 = 1^2 + 2^2 + 3^2 + 4^2 = 30 \equiv 2 \pmod 4$, by induction, it follows that
$$
B_n \equiv 2 \cdot 4^{n-1} \pmod{4^n} \quad (2)
$$
holds for all $n \in \mathbb{N}$.

So, by using (1) and (2), we have:
$$
\begin{align*}
C_{n+1} &= \sum_{(c,x_n) \in \{1,2,3,4\} \times S_n} (10^n \cdot c + x_n)^3 \\
&= \sum_{(c,x_n) \in \{1,2,3,4\} \times S_n} (10^{3n} \cdot c^3 + 3 \cdot 10^{2n} \cdot c^2 \cdot x_n + 3 \cdot 10^n \cdot c \cdot x_n^2 + x_n^3) \\
&= 4^n \cdot 10^{3n} \cdot \sum_{c=1}^{4} c^3 + 3 \cdot 10^{2n} \cdot \sum_{c=1}^{4} c^2 \cdot A_n + 3 \cdot 10^n \cdot \sum_{c=1}^{4} c \cdot B_n + 4 \cdot C_n \\
&\equiv 0 + 0 + 3 \cdot 10^{n+1} \cdot B_n + 4C_n \pmod{4^{n+1}} \\
&\equiv 3 \cdot 10^{n+1} \cdot (k \cdot 4^n + 2 \cdot 4^{n-1}) + 4C_n \pmod{4^{n+1}} \tag{3} \\
&\equiv 3 \cdot 5^{n+1} \cdot 2^{n+2} \cdot 4^{n-1} + 4C_n \pmod{4^{n+1}}. \tag{4}
\end{align*}
$$
Since $C_1 = 100$, from (3), we obtain $C_2 \equiv 1000 \pmod{16} \equiv 8 \pmod{16}$ and for $n \ge 2$,
since $4^2 \mid 2^{n+2}$, we get
$$
C_{n+1} \equiv 4C_n \equiv 4^{n+1}. \qquad (5)
$$
Finally, from (5), by induction, we see that for all $n \in \mathbb{N} \setminus \{1\}$
$$
C_n \equiv {}_{4n}2 \cdot 4^{n-1} \qquad (\diamond)
$$
holds and by (\cap) and (\diamond) we arrive at a contradiction.

## Supplied solution 2

**Alternative Solution.** Assume such $x$ and $y$ do not exist and let $n > 1$. Since $|S_n| = 4^n$,
we see that the set $S_n$ is complete system of remainders modulo $4^n$.
Note that the numbers
$$
\overline{c_n c_{n-1} \dots c_2 1}, \overline{c_n c_{n-1} \dots c_2 2}, \overline{c_n c_{n-1} \dots c_2 3}, \overline{c_n c_{n-1} \dots c_2 4}
$$
give four consecutive remainders modulo $4^n$. Call such four consecutive remainders a
block.
Therefore all $4^n$ remainders modulo $4^n$ can be split into blocks.
Thus, the difference of any two of the $4^{n-1}$ numbers $\overline{c_n c_{n-1} \dots c_2 0}$ is congruent to $4t$ modulo
$4^n$. But
$$
\overline{c_n c_{n-1} \dots c_3 20} - \overline{c_n c_{n-1} \dots c_3 10} = 10,
$$
implying $4t \equiv 10 \pmod{4^n}$, a contradiction.
