# jpn_2013_b3ca6b

JMO | Japan | 2013 | PROBLEMS | 2

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2013_b3ca6b](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_b3ca6b.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: Japan Mathematical Olympiad
- Subtitle: The 23rd Japanese Mathematical Olympiad: The First Round, The Final Round
- Year: 2013
- Organization: The Mathematical Olympiad Foundation of Japan
- Publisher: The Mathematical Olympiad Foundation of Japan
- Edition: 23rd
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $f(1) = a$. By letting $n = 1$, we get from the given equation that $f(m) + f(1) = f(m) + f(2m + 1)$ is valid for any integer $m$. Thus we see that $f(d) = a$ must hold for any odd integer $d$.

An arbitrary non-zero integer can be written in the form $2^k d$ where $d$ is an odd integer and $k$ is a non-negative integer. By taking $m = d$ and $n = 2^k$, we obtain from the given equation that $f(d) + f(2^k) = f(2^k d) + f(2^k(d + 1) + d)$. Since both $d$ and $2^k(d + 1) + d$ are odd integers, we get from the preceding identity that $a + f(2^k) = f(2^k d) + a$, from which it follows further that $f(2^k d) = f(2^k)$. Consequently, we see that if we can determine $f(2^k)$ for all $k = 0, 1, 2, \cdots$ and $f(0)$, then $f(n)$ is determined completely for all integers $n$.

For $k \ge 2$, substitute $m = 2^k, n = 2$ into the given equation we obtain $f(2^k) + f(2) = f(2^{k+1}) + f(2^k \cdot 3 + 2)$. Since $2^k \cdot 3 + 2$ is an odd multiple of 2, we have $f(2^k \cdot 3 + 2) = f(2)$ by what we observed in the preceding paragraph. Hence, we have $f(2^k) = f(2^{k+1})$ for any $k \ge 2$. If we put $f(2^2) = b$, we then get $f(2^2) = f(2^3) = \cdots = b$. Letting $m = n = 2$ in the given equation, we get $2f(2) = f(4) + f(8) = 2b$, which says that $f(2) = b$ holds as well. What we have seen so far tells us that $f(n) = b$ holds for all even integer different from 0. Finally, by letting $m = n = -2$ in the given equation, we get $2f(-2) = f(4) + f(0)$, which implies that $f(0) = b$ holds as well. Thus, we can conclude that any function $f$ satisfying the given equation must have the form
$$
(*) \qquad f(n) = \begin{cases} a & (n \text{ odd}) \\ b & (n \text{ even or } 0). \end{cases}
$$
for some pair $a, b$ of real numbers.

Conversely, let us show that for an arbitrary pair $a, b$ of real numbers the function defined by $(*)$ satisfies the given equation.

* When both $m$ and $n$ are even, $mn$ and $m+n+mn$ are both even, so both sides of the given equation are equal to $2b$.

* When both $m$ and $n$ are odd, $mn$ and $m+n+mn$ are both odd, so both sides of the given equation are equal to $2a$.

* If one of $m, n$ is even and the other is odd, $mn$ is even and $m+n+mn$ is odd, so both sides of the given equation are equal to $a+b$.

Thus, the function defined by $(*)$ satisfies the given equation for any choice of a pair $a, b$ of real numbers and thus the desired functions $f$ are all functions of this form.
