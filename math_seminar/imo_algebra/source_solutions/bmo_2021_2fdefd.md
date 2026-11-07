# bmo_2021_2fdefd

BMO-SL | Balkan Mathematical Olympiad | 2021 | ALGEBRA | A4

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2021_2fdefd](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2021_2fdefd.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: 38th Balkan Mathematical Olympiad
- Subtitle: Shortlisted Problems with Solutions
- Year: 2021
- Editors: Christofides, Demetres; Karantanos, Demetris; Kouzaris, Stelios; Parayiou, Theoklitos; Stylianou, Stelios; Voskou, Marios
- Organization: BMO 2021 Organising Committee and Problem Selection Committee
- Place: Cyprus
- Series: Balkan Mathematical Olympiad
- Volume: 38

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

(a) Yes it is always possible. The key idea is the following: Let $b(n)$ be the number of 1's in the binary expansion of $n = 0, 1, 2, \dots$.

**Lemma:** Given a polynomial $f$ with integer coefficients and degree at most $d$, then
$$
\sum_{k=0}^{2^{d+1}-1} (-1)^{b(k)} f(n+k) = f(n) - f(n+1) - f(n+2) + \dots + \pm f(n + (2^{d+1} - 1)) = 0.
$$
**Proof of Lemma:** The result is clear for $d=0$. For $d \ge 1$, we have
$$
\sum_{k=0}^{2^{d+1}-1} (-1)^{b(k)} f(n+k) = \sum_{k=0}^{2^d-1} (-1)^{b(k)} [f(n+k) - f(n+k+2^d)].
$$
So set $\tilde{f}(n) = f(n) - f(n + 2^d)$, which is a polynomial of degree at most $d-1$. Then
$$
\sum_{k=0}^{2^{d+1}-1} (-1)^{b(k)} f(n+k) = \sum_{k=0}^{2^d-1} \tilde{f}(n+k) = 0,
$$
by induction, completing the proof of the lemma. $\square$

In particular, if we take
$$
\mathbf{x}_n - \mathbf{x}_{n-1} = ((-1)^{b(n)} f(n), (-1)^{b(n)} g(n)),
$$
then $\mathbf{x}_D = \mathbf{0}$ whenever $D$ is a multiple of $2^{1+\max(\deg(f),\deg(g))}$.

(b) No, it is not always possible. Let $g$ be any suitable function. Then, we construct $f$ inductively. There are at most $8^{n-1}$ possibilities for $\mathbf{x}_{n-1}$, so choose $f(n)$ to be greater than the magnitude of all of them. Consequently $\mathbf{x}_n$ cannot be $\mathbf{0}$.

## Supplied solution 2

(a) Given a polynomial $f$ of degree at most $d$ and integers $n, r$, we claim that
$$
\sum_{k=0}^{2^{d+1}-1} \varepsilon_k f(2^d n + r + k) = 0
$$
for some choice of $\varepsilon_0, \varepsilon_1, \dots, \varepsilon_{2^{d+1}-1} \in \{-1, 1\}$. (Which are allowed to depend on $d$ and $f$.)

We proceed by induction on $d$, the case $d = 0$ being immediate. For the inductive step we define the polynomial $g(n) = f(2n + r + 1) - f(2n + r)$ which is a polynomial of degree at most $d - 1$. Then
$$
\sum_{k=0}^{2^d-1} \varepsilon_k g(2^{d-1}n + k) = 0
$$
for some choice of the $\varepsilon_k$'s giving
$$
\sum_{k=0}^{2^{d+1}-1} \varepsilon'_k f(2^d n + r + k) = 0
$$
where $\varepsilon'_{2k} = -\varepsilon_k$ and $\varepsilon'_{2k+1} = \varepsilon_k$. This completes the proof of the claim.

Now the proof can be completed as in Solution 1.

(b) Apart from magnitude arguments, one could also use modulo arguments. For example, taking $f(0), g(0)$ to be odd and $f(n), g(n)$ to be even for every $n \ge 1$ works.
