# mkd_2015_de03cc

EGMO | North Macedonia | 2015 | Day 1 | 3

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [mkd_2015_de03cc](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2015_de03cc.json.gz)

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

Suppose without loss of generality that $a_1$ is the smallest of the $a_i$. If $a_1 \ge n^m - 1$, then the problem is simple: either all the $a_i$ are equal, or $a_1 = n^m - 1$ and $a_j = n^m$ for some $j$. In the first case we can take (say) $b_1 = 1$, $b_2 = 2$, and the rest of the $b_i$ can be arbitrary, and we have
$$
\text{gcd}(a_1 + b_1, a_2 + b_2, a_3 + b_3, \dots, a_m + b_m) \le \text{gcd}(a_1 + b_1, a_2 + b_2) = 1.
$$
In the second case, we can take $b_1 = 1$, $b_j = 1$, and the rest of the $b_i$ arbitrary, and again
$$
\text{gcd}(a_1 + b_1, a_2 + b_2, a_3 + b_3, \dots, a_m + b_m) \le \text{gcd}(a_1 + b_1, a_j + b_j) = 1.
$$
So from now on we can suppose that $a_1 \le n^m - 2$.

Now, let us suppose the desired $b_1, \dots, b_m$ do not exist, and seek a contradiction. Then, for any choice of $b_1, b_2, \dots, b_m \in \{1, 2, \dots, n\}$, we have
$$
\text{gcd}(a_1 + b_1, a_2 + b_2, \dots, a_m + b_m) \geq n.
$$
Also, we have
$$
\text{gcd}(a_1 + b_1, a_2 + b_2, \dots, a_m + b_m) \leq a_1 + b_1 \leq n^m + n - 2.
$$
Thus there are at most $n^m - 1$ possible values for the greatest common divisor. However, there are $n^m$ choices for the $m$-tuple $(b_1, \dots, b_m)$. Then, by the pigeonhole principle, there are two $m$-tuples that yield the same values for the greatest common divisor, say $d$. But since $d \ge n$, for each $i$ there can be at most one choice of $b_i \in \{1, 2, \dots, n\}$ such that $a_i + b_i$ is divisible by $d$ and therefore there can be at most one $m$-tuple $(b_1, \dots, b_m)$ yielding $d$ as the greatest common divisor. This is the desired contradiction.

## Supplied solution 2

Similarly to Solution 1 suppose that $a_1 \le n^m - 2$. The gcd of $a_1 + 1, a_2 + 1, \dots, a_m + 1$ is coprime with the gcd of $a_1 + 1, a_2 + 1, \dots, a_m + 1$, thus $a_1 + 1 \ge n^2$. Now change another 1 into 2 and so on. After $m-1$ changes we get $a_1 + 1 \ge n^m$ which gives us a contradiction.

## Supplied solution 3

We will prove a stronger version of this problem:
For $m, n > 1$, let $a_1, a_2, \dots, a_m$ be positive integers with at least one $a_i \le n^{2^{m-1}}$. Then there are integers $b_1, b_2, \dots, b_m$, each equal to $1$ or $2$, such that $\text{gcd}(a_1 + b_1, a_2 + b_2, \dots, a_m + b_m) < n$.

**Proof:** Suppose otherwise. Then the $2^{m-1}$ integers $\text{gcd}(a_1 + b_1, a_2 + b_2, \dots, a_m + b_m)$ with $b_1 = 1$ and $b_i = 1$ or $2$ for $i > 1$ are all pairwise coprime, since for any two of them, there is some $i > 1$ with $a_i + 1$ appearing in one and $a_i + 2$ in the other. Since each of these $2^{m-1}$ integers divides $a_1 + 1$, and each is $\ge n$ with at most one equal to $n$, it follows that $a_1 + 1 \ge n(n+1)^{2^{m-1}-1}$ so $a_1 \ge n^{2^{m-1}}$. The same is true for each $a_i$, $i = 1, 2, \dots, n$, a contradiction.
