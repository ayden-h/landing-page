# jpn_2025_fd4cdd

JMO | Japan | 2025 | FINAL ROUND | 4

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2025_fd4cdd](https://mathnet.mit.edu/data_v2/full/japan/jpn_2025_fd4cdd.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: The 35th Japanese Mathematical Olympiad
- Year: 2025
- Organization: The Mathematical Olympiad Foundation of Japan
- Publisher: The Mathematical Olympiad Foundation of Japan
- Series: Japan Mathematical Olympiad
- Volume: 35
- Issue: The First Round • The Final Round
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

**Solution:** We will show that $f(x) = (x-1)^m$ provides an answer. For $n \ge 2$ we have $f(n) = (n-1)^m > 0$, thus the first condition is satisfied.

**Lemma 1.** Let $d, t, x$ be positive integers. If $x-1$ is a multiple of $d^t$, then $x^d-1$ is a multiple of $d^{t+1}$.

**Proof.** Since $x \equiv 1 \pmod d$, we have $x^{d-1} + \dots + x + 1 \equiv 1 + \dots + 1 \equiv 0 \pmod d$. Thus $x^d - 1 = (x-1)(x^{d-1} + \dots + x + 1)$ is a multiple of $d^{t+1}$ as desired. $\blacksquare$

Let $n \ge 2$. Since $n^{(n-1)0} - 1 = n-1$ is a multiple of $n-1$, an induction using Lemma 1 shows that $n^{(n-1)m} - 1$ is a multiple of $(n-1)^{m+1}$ for $m \ge 0$. Thus, we conclude that $f(x) = (x-1)^m$ is an answer for $m \ge 0$.

Next we will show that no other answers exist. For integers $a, b$ with $b \ne 0$, we write $b \mid a$ to mean that $a$ is divisible by $b$.

**Lemma 2.** For a positive integer $n$ and integers $a$ and $b$, $a \equiv b \pmod n$ implies $f(a) \equiv f(b) \pmod n$.

**Proof.** Write $f(x) = a_0 + a_1x + \dots + a_d x^d$, where $d$ is a nonnegative integer and $a_0, a_1, \dots, a_d$ are integers. Since $n \mid a-b$,
$$
f(a) - f(b) = \sum_{i=1}^{d} a_i (a^i - b^i) = (a-b) \sum_{i=1}^{d} a_i (a^{i-1} + a^{i-2}b + \dots + ab^{i-2} + b^{i-1})
$$
is divisible by $n$. $\blacksquare$

We will show that, for an odd prime $p$ and an integer $n \ge 2$, $p \mid f(n)$ implies $p \mid n-1$. For a nonnegative integer $k$, Lemma 2 shows that $f(n + kp) \equiv f(n) \equiv 0 \pmod p$. Thus we have
$$
0 \equiv (n + kp)^{f(n+kp)} - 1 \equiv n^{f(n+kp)} - 1 \pmod p
$$
Since $p$ and $p-1$ are coprime, we can take a nonnegative integer $k$ such that $p-1 \mid n + kp$.
Then $f(n + kp) \equiv f(p-1) \pmod{p-1}$ holds and thus Fermat's little theorem shows that
$$
0 \equiv n^{f(n+kp)} - 1 \equiv n^{f(p-1)} - 1, \pmod{p}
$$
therefore we have
$$
n^{f(p-1)} \equiv 1. \pmod{p}
$$
Since $f(p-1) \mid (p-1)^{f(p-1)} - 1$, $f(p-1)$ and $p-1$ are coprime. Thus, there exists a positive integer $r$ such that $f(p-1)r \equiv 1 \pmod{p-1}$. By Fermat's little theorem we have
$$
n \equiv n^{f(p-1)r} \equiv 1^r \equiv 1, \pmod{p}
$$
that is, $p \mid n-1$.

We have shown that, for an odd prime $p$ and an integer $n \ge 2$, $p \mid f(n)$ implies $p \mid n-1$. In particular, for an odd prime $p$, any prime factor of $f(p+1)$ is also a prime factor of $p+1-1 = p$, which means that $f(p+1)$ is a power of $p$.

Write $f(x+1) = x^m(b_0 + b_1x + \dots + b_lx^l)$ where $l$ and $m$ are nonnegative integers and $b_0 \ne 0, b_1, \dots, b_l$ are integers. Let $p$ be an odd prime greater than $|b_0|$. Then $f(p+1)$ is a multiple of $p^m$, while $f(p+1) \equiv b_0p^m \ne 0 \pmod{p^{m+1}}$. The argument above shows that $f(p+1) = p^m$.

Let $g(x) = f(x) - (x-1)^m$. Then there exist infinitely many integers $n$ such that $g(n) = 0$. It follows that $g(x) = 0$ as polynomials. We conclude that $f(x) = (x-1)^m$.
