# kor_2011_babdb4

KMO | South Korea | 2011 | The First Day, March 26, 2011 | 1

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [kor_2011_babdb4](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2011_babdb4.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: South Korea
- Title: The 24th Korean Mathematical Olympiad
- Subtitle: Final Round
- Year: 2011
- Organization: KOREAN MATHEMATICAL OLYMPIAD COMMITTEE
- Publisher: THE KOREAN MATHEMATICAL SOCIETY
- Place: Seoul, KOREA
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We will prove this statement by contradiction. Assume that there are positive integers $x, y, z$ satisfying the equation
$$
x^2 y^4 - x^4 y^2 + 4x^2 y^2 z^2 + x^2 z^4 - y^2 z^4 = 0. \quad (1)
$$
It is easy to check that $x \neq y$. If there are solutions of the equation (1), we have a solution of the equation (1) such that $\gcd(x, y) = (x, y) = 1$. Now let $x, y, z$ be a positive integer solution of the equation (1) such that $(x, y) = 1$.
By factoring the equation (1), we get
$$
\begin{aligned}
0 &= x^2 y^4 - x^4 y^2 + 4x^2 y^2 z^2 + x^2 z^4 - y^2 z^4 \\
&= x^2(y^4 + 2y^2 z^2 + z^4) - y^2(x^4 - 2x^2 z^2 + z^4) \\
&= x^2(y^2 + z^2)^2 - y^2(x^2 - z^2)^2 \\
&= (x(y^2 + z^2) + y(x^2 - z^2))(x(y^2 + z^2) - y(x^2 - z^2)) \\
&= ((x - y)z^2 + x y(x + y))((x + y)z^2 + x y(y - x)).
\end{aligned}
$$
Then
$$
(y - x)z^2 = x y(x + y) \quad \text{or} \quad (x + y)z^2 = x y(x - y).
$$
By multiplying both sides of the first equation by $y - x$ we have
$$
(y - x)^2 z^2 = x y(y^2 - x^2). \quad (2)
$$
By multiplying both sides of the second equation by $x + y$ we have
$$
(x + y)^2 z^2 = x y(x^2 - y^2) \quad (3)
$$
Since we can solve the equation (3) by the same way in which we solve the equation (2), we are going to solve the equation (2).
Because $(x, y) = 1$, $(x, y^2 - x^2) = (y, y^2 - x^2) = 1$. Now the left hand side of the equation (2) is a perfect square of an integer. We know that $x, y$, and $y^2 - x^2$ are perfect squares. So there are positive integers $a, b, c$ such that $x = a^2, y = b^2, y^2 - x^2 = c^2$. Therefore we have the equation
$$
b^4 - a^4 = c^2.
$$
But it is well-known that there are no positive integers $a, b, c$ satisfying the above equation. It can be proved by infinite descent. Therefore, we prove the statement by contradiction. $\square$
