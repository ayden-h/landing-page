# imo_2021_bfcfa1

IMO-SL | IMO | 2021 | Number Theory | N8

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2021_bfcfa1](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_bfcfa1.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems
- Subtitle: IMO 2021: 62nd International Mathematical Olympiad Saint-Petersburg Russia
- Year: 2021
- Editors: Kós, Géza; Woeginger, Gerhard; Ustinov, Alexey; Krachun, Dmitry; Mitrofanov, Ivan; Berlov, Sergey; Petrov, Fedor; Frolov, Ivan; Vaderlind, Paul; Golovanov, Alexander; Bogdanov, Ilya I.
- Organization: International Mathematical Olympiad
- Place: Saint-Petersburg — Russia
- Series: International Mathematical Olympiad
- Volume: 62nd

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Answer: All powers of 2 and all primes.

Denote the set of residues modulo $\ell$ by $\mathbb{Z}_{\ell}$. Observe that $P$ can be regarded as a function $\mathbb{Z}_{\ell} \rightarrow \mathbb{Z}_{\ell}$ for any positive integer $\ell$. Denote the cardinality of the set $P^{m}\left(\mathbb{Z}_{\ell}\right)$ by $f_{m, \ell}$. Note that $f_{m, n}=\left\lceil n / 2^{m}\right\rceil$ for all $m \geqslant 1$ if and only if $f_{m+1, n}=\left\lceil f_{m, n} / 2\right\rceil$ for all $m \geqslant 0$.

Part 1. The required polynomial exists when $n$ is a power of 2 or a prime.
If $n$ is a power of 2, set $P(x)=2x$.
If $n=p$ is an odd prime, every function $f: \mathbb{Z}_{p} \rightarrow \mathbb{Z}_{p}$ coincides with some polynomial with integer coefficients. So we can pick the function that sends $x \in \{0,1, \ldots, p-1\}$ to $\lfloor x / 2\rfloor$.

Part 2. The required polynomial does not exist when $n$ is not a prime power.
Let $n=ab$ where $a, b>1$ and $\operatorname{gcd}(a, b)=1$. Note that, since $\operatorname{gcd}(a, b)=1$,
$$
f_{m, ab}=f_{m, a} f_{m, b}
$$
by the Chinese remainder theorem. Also, note that, if $f_{m, \ell}=f_{m+1, \ell}$, then $P$ permutes the image of $P^{m}$ on $\mathbb{Z}_{\ell}$, and therefore $f_{s, \ell}=f_{m, \ell}$ for all $s>m$. So, as $f_{m, ab}=1$ for sufficiently large $m$, we have for each $m$
$$
f_{m, a}>f_{m+1, a} \quad \text{or} \quad f_{m, a}=1, \quad f_{m, b}>f_{m+1, b} \quad \text{or} \quad f_{m, b}=1.
$$
Choose the smallest $m$ such that $f_{m+1, a}=1$ or $f_{m+1, b}=1$. Without loss of generality assume that $f_{m+1, a}=1$. Then $f_{m+1, ab}=f_{m+1, b}<f_{m, b} \leqslant f_{m, ab} / 2 \leqslant f_{m+1, ab}$, a contradiction.

Part 3. The required polynomial does not exist when $n$ is an odd prime power that is not a prime.
Let $n=p^{k}$, where $p \geqslant 3$ is prime and $k \geqslant 2$. For $r \in \mathbb{Z}_{p}$ let $S_{r}$ denote the subset of $\mathbb{Z}_{p^{k}}$ consisting of numbers congruent to $r$ modulo $p$. We denote the cardinality of a set $S$ by $|S|$.

Claim. For any residue $r$ modulo $p$, either $|P(S_{r})|=p^{k-1}$ or $|P(S_{r})| \leqslant p^{k-2}$.

Proof. Recall that $P(r+h)=P(r)+h P^{\prime}(r)+h^{2} Q(r, h)$, where $Q$ is an integer polynomial.
If $p \mid P^{\prime}(r)$, then $P(r+ps) \equiv P(r)\pmod{p^{2}}$, hence all elements of $P(S_{r})$ are congruent modulo $p^{2}$. So in this case $|P(S_{r})| \leqslant p^{k-2}$.
Now we show that $p \nmid P^{\prime}(r)$ implies $|P(S_{r})|=p^{k-1}$ for all $k$.
Suppose the contrary: $|P(S_{r})|<p^{k-1}$ for some $k>1$. Let us choose the smallest $k$ for which this is so. To each residue in $P(S_{r})$ we assign its residue modulo $p^{k-1}$; denote the resulting set by $\bar{P}(S, r)$. We have $|\bar{P}(S, r)|=p^{k-2}$ by virtue of minimality of $k$. Then $|P(S_{r})|<p^{k-1}=p \cdot|\bar{P}(S, r)|$, that is, there is $u=P(x) \in P(S_{r})(x \equiv r\pmod{p})$ and $t \not\equiv 0 \pmod{p}$ such that $u+p^{k-1} t \notin P(S_{r})$.
Note that $P(x+p^{k-1} s) \equiv u+p^{k-1} s P^{\prime}(x)\pmod{p^{k}}$. Since $P(x+p^{k-1} s) \not\equiv u+p^{k-1} t \pmod{p^{k}}$, the congruence $p^{k-1} s P^{\prime}(x) \equiv p^{k-1} t\pmod{p^{k}}$ has no solutions. So the congruence $s P^{\prime}(x) \equiv t\pmod{p}$ has no solutions, which contradicts $p \nmid P^{\prime}(r)$. $\square$

Since the image of $P^{m}$ consists of one element for sufficiently large $m$, we can take the smallest $m$ such that $|P^{m-1}(S_{r})|=p^{k-1}$ for some $r \in \mathbb{Z}_{p}$, but $|P^{m}(S_{q})| \leqslant p^{k-2}$ for all $q \in \mathbb{Z}_{p}$.
From now on, we fix $m$ and $r$.
Since the image of $P^{m-1}(\mathbb{Z}_{p^{k}}) \backslash P^{m-1}(S_{r})$ under $P$ contains $P^{m}(\mathbb{Z}_{p^{k}}) \backslash P^{m}(S_{r})$, we have
$$
a:=|P^{m}(\mathbb{Z}_{p^{k}}) \backslash P^{m}(S_{r})| \leqslant|P^{m-1}(\mathbb{Z}_{p^{k}}) \backslash P^{m-1}(S_{r})|
$$
thus
$$
a+p^{k-1} \leqslant f_{m-1, p^{k}} \leqslant 2 f_{m, p^{k}} \leqslant 2 p^{k-2}+2 a
$$
so
$$
(p-2) p^{k-2} \leqslant a
$$
Since $f_{i, p}=1$ for sufficiently large $i$, there is exactly one $t \in \mathbb{Z}_{p}$ such that $P(t) \equiv t\pmod{p}$. Moreover, as $i$ increases, the cardinality of the set $\{s \in \mathbb{Z}_{p} \mid P^{i}(s) \equiv t\pmod{p}\}$ increases (strictly), until it reaches the value $p$. So either
$$
|\{s \in \mathbb{Z}_{p} \mid P^{m-1}(s) \equiv t \quad\pmod{p}\}|=p \quad \text{or} \quad|\{s \in \mathbb{Z}_{p} \mid P^{m-1}(s) \equiv t \quad\pmod{p}\}| \geqslant m
$$
Therefore, either $f_{m-1, p}=1$ or there exists a subset $X \subset \mathbb{Z}_{p}$ of cardinality at least $m$ such that $P^{m-1}(x) \equiv t\pmod{p}$ for all $x \in X$.
In the first case $|P^{m-1}(\mathbb{Z}_{p^{k}})| \leqslant p^{k-1}=|P^{m-1}(S_{r})|$, so $a=0$, a contradiction.
In the second case let $Y$ be the set of all elements of $\mathbb{Z}_{p^{k}}$ congruent to some element of $X$ modulo $p$. Let $Z=\mathbb{Z}_{p^{k}} \backslash Y$. Then $P^{m-1}(Y) \subset S_{t}, P(S_{t}) \subsetneq S_{t}$, and $Z=\bigcup_{i \in \mathbb{Z}_{p} \backslash X} S_{i}$, so
$$
|P^{m}(Y)| \leqslant|P(S_{t})| \leqslant p^{k-2} \quad \text{and} \quad|P^{m}(Z)| \leqslant|\mathbb{Z}_{p} \backslash X| \cdot p^{k-2} \leqslant(p-m) p^{k-2}
$$
Hence,
$$
(p-2) p^{k-2} \leqslant a<|P^{m}(\mathbb{Z}_{p^{k}})| \leqslant|P^{m}(Y)|+|P^{m}(Z)| \leqslant(p-m+1) p^{k-2}
$$
and $m<3$. Then $|P^{2}(S_{q})| \leqslant p^{k-2}$ for all $q \in \mathbb{Z}_{p}$, so
$$
p^{k} / 4 \leqslant|P^{2}(\mathbb{Z}_{p^{k}})| \leqslant p^{k-1}
$$
which is impossible for $p \geqslant 5$. It remains to consider the case $p=3$.
As before, let $t$ be the only residue modulo 3 such that $P(t) \equiv t\pmod{3}$.
If $3 \nmid P^{\prime}(t)$, then $P(S_{t})=S_{t}$ by the proof of the Claim above, which is impossible.
So $3 \mid P^{\prime}(t)$. By substituting $h=3^{i} s$ into the formula $P(t+h)=P(t)+h P^{\prime}(t)+h^{2} Q(t, h)$, we obtain $P\left(t+3^{i} s\right) \equiv P(t)\pmod{3^{i+1}}$. Using induction on $i$ we see that all elements of $P^{i}(S_{t})$ are congruent modulo $3^{i+1}$. Thus, $|P^{k-1}(S_{t})|=1$.
Note that $f_{1,3} \leqslant 2$ and $f_{2,3} \leqslant 1$, so $P^{2}(\mathbb{Z}_{3^{k}}) \subset S_{t}$. Therefore, $|P^{k+1}(\mathbb{Z}_{3^{k}})| \leqslant|P^{k-1}(S_{t})|=1$. It follows that $3^{k} \leqslant 2^{k+1}$, which is impossible for $k \geqslant 2$.
