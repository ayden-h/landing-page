# bmo_2023_be5fcc

BMO-SL | Balkan Mathematical Olympiad | 2023 | Combinatorics | C5

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2023_be5fcc](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_be5fcc.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: Shortlisted Problems with Solutions
- Year: 2023
- Editors: Üçer, Melih; Bahadır, Selim; Kadan, Fehmi Emre; Yıldız, Mehmet Akif; İleri, Ahmet; Kaymak, Ozan
- Place: Antalya-Türkiye
- Series: BMO
- Volume: 2023

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Answer: 592.
For $k \ge 593$, Alice can color the greatest 593 numbers $1431, 1432, \dots, 2023$ and any other $(k-593)$ numbers so that their sum $s$ would satisfy
$$
s \ge \frac{2023 \cdot 2024}{2} - \frac{1430 \cdot 1431}{2} > \frac{1}{2} \cdot \left( \frac{2023 \cdot 2024}{2} \right),
$$
thus anyhow Bob chooses his numbers, the sum of his numbers will be less than Alice's numbers' sum.
We now show that $k = 592$ satisfies the condition. Let $s$ be the sum of Alice's 592 numbers; note that $s < \frac{1}{2} \cdot \left(\frac{2023 \cdot 2024}{2}\right)$. Below is a strategy for Bob to find some of the remaining 1431 numbers so that their sum is
$$
s_0 = \min \left\{ s, \frac{2023 \cdot 2024}{2} - 2s \right\} \le \frac{1}{3} \cdot \left( \frac{2023 \cdot 2024}{2} \right),
$$
(Clearly, if Bob finds some numbers whose sum is $\frac{2023 \cdot 2024}{2} - 2s$, then the sum of remaining numbers will be $s$).
**Case 1.** $s_0 \ge 2024$. Let $s_0 = 2024a + b$, where $0 \le b \le 2023$. Bob finds two of the remaining numbers with sum $b$ or $2024+b$, then he finds $a$ (or $a-1$) pairs among the remaining numbers with sum 2024. Note that $a \le 337$ since $s_0 \le \frac{1}{3} \cdot \left(\frac{2023 \cdot 2024}{2}\right)$.
The $\lfloor \frac{b-1}{2} \rfloor$ pairs
$$
(1, b-1), (2, b-2), \dots, \left( \left\lfloor \frac{b-1}{2} \right\rfloor, b - \left\lfloor \frac{b-1}{2} \right\rfloor \right),
$$
have sum of their components equal to $b$ and the $\lfloor \frac{2023+b}{2} \rfloor - b$ pairs
$$
(2023, b+1), (2022, b+2), \dots, \left( 2024 + b - \left\lfloor \frac{2023+b}{2} \right\rfloor, \left\lfloor \frac{2023+b}{2} \right\rfloor \right)
$$
have sum of their components equal to $2024 + b$. The total number of these pairs is
$$
\left\lfloor \frac{2023+b}{2} \right\rfloor - b + \left\lfloor \frac{b-1}{2} \right\rfloor \ge \frac{2022+b}{2} + \frac{b-2}{2} - b = \frac{2020}{2} = 1010 > 592,
$$
hence some of these pairs have no red-colored components, so Bob can choose one of these pairs and color those two numbers in blue. Thus 594 numbers are colored so far.
Further, the 1011 pairs
$$
(1, 2023), (2, 2022), \dots, (1011, 1013)
$$
have sum of the components equal to 2024. Among these, at least $1011 - 594 = 417 > 337 \ge a$ pairs have no components colored, so Bob can choose $a$ (or $a-1$) uncolored pairs and color them all blue to achieve a collection of blue numbers with their sum equal to $s_0$.
**Case 2.** $s_0 \le 2023$. Note that $s \ge 1 + 2 + \dots + 592 > 2023$, thus we have $s_0 = \frac{2023 \cdot 2024}{2} - 2s$, i.e. $s = \frac{2023 \cdot 2024}{4} - \frac{s_0}{2}$.
If $s_0 > 2 \cdot 593$, at least one of the 593 pairs
$$
(1, s_0 - 1), (2, s_0 - 2), \dots, (593, s_0 - 593)
$$
have no red-colored components, so Bob can choose these two numbers and immediately achieve the sum of $s_0$. And if $s_0 \le 2 \cdot 593$, then
$$
s = \frac{2023 \cdot 2024}{4} - \frac{s_0}{2} \ge (1432 + 1433 + \dots + 2023) - 593 = 839 + (1434 + 1435 + \dots + 2023),
$$
hence Alice cannot have colored any of the numbers 1, 2, ..., 838. Then Bob can easily choose one or two of these numbers having the sum of $s_0$.
**Remark.** The problem can be asked for any $n$ large enough ($n \ge 100$ suffices as it's originally proposed), and in that case the answer would be $k = \lfloor \frac{(2n + 1) - \sqrt{n^2 + (n + 1)^2}}{2} \rfloor$, the largest value guaranteeing that sum of any $k$ numbers is less than half of the sum of all numbers in the set.

