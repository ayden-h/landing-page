# jpn_2009_be6d0b

JMO | Japan | 2009 | PROBLEMS | 1

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2009_be6d0b](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_be6d0b.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: Japan Mathematical Olympiad
- Subtitle: The 19 Japanese Mathematical Olympiad: The First Round, The Final Round And The 7 Japanese Junior Mathematical Olympiad
- Year: 2009
- Organization: The Mathematical Olympiad Foundation of Japan
- Publisher: The Mathematical Olympiad Foundation of Japan

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

To begin with, we transform $8^n + n$ into the following expression:
$$
8^n + n = (2n)^3 + n = (2^n + n)((2^n)^2 - n \cdot 2^n + n^2) - (n^3 - n).
$$
Since $(2^n)^2 - n \cdot 2^n + n^2$ is an integer, from the expression above it follows that the statement $8^n + n$ is divisible by $2^n + n$ is equivalent to the statement $n^3 - n$ is divisible by $2^n + n$.
If $n=1$, then $n^3 - n = 0$, so $8^n + n$ is divisible by $2^n + n$ in this case. If $n \ge 2$, $n^3 - n > 0$, so we must have $n^3 - n \ge 2^n + n$; in particular, it is necessary that $n^3 > 2^n$. Let us, therefore, set $f(n) = \frac{n^3}{2^n}$. Then, if $n \ge 4$ we have
$$
\frac{f(n+1)}{f(n)} = \frac{1}{2} \cdot \left(\frac{n+1}{n}\right)^3 = \frac{1}{2} \cdot \left(1 + \frac{1}{n}\right)^3 \le \frac{1}{2} \cdot \left(1 + \frac{1}{4}\right)^3 = \frac{125}{128} < 1.
$$
Therefore, we get $f(4) > f(5) > \dots$. Since $f(10) = \frac{1000}{1024} < 1$, we see that if $n \ge 10$, then $f(n) < 1$, i.e., $n^3 < 2^n$.
Thus, we see that it is enough to check that for which $n$ satisfying $2 \le n < 10$, $n^3 - n$ is divisible by $2^n + n$. For, $n = 2, 3, 4, 5, 6, 7, 8, 9$ we get
$$
(n^3 - n, 2^n + n) = (6, 6), (24, 11), (60, 20), (120, 37), (210, 70) \\
(336, 135), (504, 264), (720, 521),
$$
and we conclude that $n^3 - n$ is divisible by $2^n + n$, when $n = 2, 4, 6$. Together with $n = 1$, we get that the desired solution is $n = 1, 2, 4, 6$.
