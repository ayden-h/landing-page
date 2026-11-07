# imo_2015_b5a2eb

IMO-SL | IMO | 2015 | Number Theory | N7

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2015_b5a2eb](https://mathnet.mit.edu/data_v2/full/imo/imo_2015_b5a2eb.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems
- Subtitle: with Solutions
- Year: 2015
- Editors: Shiowattana, Dungjade; Bogdanov, Ilya I.; Khandhawit, Tirasan; Kositwattanarerk, Wittawat; Kós, Géza; Neeranartvong, Weerachai; Pitimanaaree, Nipun; Reiher, Christian; Sothanaphan, Nat; Suksompong, Warut; Trongsiriwat, Wuttisak; Yangjit, Wijit
- Organization: 56th International Mathematical Olympiad
- Place: Chiang Mai, Thailand
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We first show that there is no $1$-good function. Suppose that there exists a function $f$ such that $G_{f}(m, n)=1$ for all $m \neq n$. Now, if there are two distinct even numbers $m$ and $n$ such that $f(m)$ and $f(n)$ are both even, then $2 \mid G_{f}(m, n)$, a contradiction. A similar argument holds if there are two distinct odd numbers $m$ and $n$ such that $f(m)$ and $f(n)$ are both odd. Hence we can choose an even $m$ and an odd $n$ such that $f(m)$ is odd and $f(n)$ is even. This also implies that $2 \mid G_{f}(m, n)$, a contradiction.

We now construct a $2$-good function. Define $f(n)=2^{g(n)+1}-n-1$, where $g$ is defined recursively by $g(1)=1$ and $g(n+1)=\left(2^{g(n)+1}\right)!$.

For any positive integers $m>n$, set
$$
A=f(m)+n=2^{g(m)+1}-m+n-1, \quad B=f(n)+m=2^{g(n)+1}-n+m-1 .
$$
We need to show that $\operatorname{gcd}(A, B) \leqslant 2$. First, note that $A+B=2^{g(m)+1}+2^{g(n)+1}-2$ is not divisible by $4$, so that $4 \nmid \operatorname{gcd}(A, B)$. Now we suppose that there is an odd prime $p$ for which $p \mid \operatorname{gcd}(A, B)$ and derive a contradiction.

We first claim that $2^{g(m-1)+1} \geqslant B$. This is a rather weak bound; one way to prove it is as follows. Observe that $g(k+1)>g(k)$ and hence $2^{g(k+1)+1} \geqslant 2^{g(k)+1}+1$ for every positive integer $k$. By repeatedly applying this inequality, we obtain $2^{g(m-1)+1} \geqslant 2^{g(n)+1}+(m-1)-n=B$.

Now, since $p \mid B$, we have $p-1<B \leqslant 2^{g(m-1)+1}$, so that $p-1 \mid\left(2^{g(m-1)+1}\right)!=g(m)$. Hence $2^{g(m)} \equiv 1(\bmod p)$, which yields $A+B \equiv 2^{g(n)+1}(\bmod p)$. However, since $p \mid A+B$, this implies that $p=2$, a contradiction.

## Supplied solution 2

We provide an alternative construction of a $2$-good function $f$.
Let $\mathcal{P}$ be the set consisting of $4$ and all odd primes. For every $p \in \mathcal{P}$, we say that a number $a \in\{0,1, \ldots, p-1\}$ is $p$-useful if $a \not \equiv -a(\bmod p)$. Note that a residue modulo $p$ which is neither $0$ nor $2$ is $p$-useful (the latter is needed only when $p=4$).

We will construct $f$ recursively; in some steps, we will also define a $p$-useful number $a_{p}$. After the $m^{\text{th}}$ step, the construction will satisfy the following conditions:
(i) The values of $f(n)$ have already been defined for all $n \leqslant m$, and $p$-useful numbers $a_{p}$ have already been defined for all $p \leqslant m+2$;
(ii) If $n \leqslant m$ and $p \leqslant m+2$, then $f(n)+n \not \equiv a_{p}(\bmod p)$;
(iii) $\operatorname{gcd}\left(f\left(n_{1}\right)+n_{2}, f\left(n_{2}\right)+n_{1}\right) \leqslant 2$ for all $n_{1}<n_{2} \leqslant m$.
If these conditions are satisfied, then $f$ will be a $2$-good function.

**Step 1.** Set $f(1)=1$ and $a_{3}=1$. Clearly, all the conditions are satisfied.

**Step $m$, for $m \geqslant 2$.** We need to determine $f(m)$ and, if $m+2 \in \mathcal{P}$, the number $a_{m+2}$.

Defining $f(m)$. Let $X_{m}=\{p \in \mathcal{P}: p \mid f(n)+m$ for some $n<m\}$. We will determine $f(m) \bmod p$ for all $p \in X_{m}$ and then choose $f(m)$ using the Chinese Remainder Theorem.
Take any $p \in X_{m}$. If $p \leqslant m+1$, then we define $f(m) \equiv -a_{p}-m(\bmod p)$. Otherwise, if $p \geqslant m+2$, then we define $f(m) \equiv 0(\bmod p)$.

Defining $a_{m+2}$. Now let $p=m+2$ and suppose that $p \in \mathcal{P}$. We choose $a_{p}$ to be a residue modulo $p$ that is not congruent to $0,2$, or $f(n)+n$ for any $n \leqslant m$. Since $f(1)+1=2$, there are at most $m+1<p$ residues to avoid, so we can always choose a remaining residue.

We first check that (ii) is satisfied. We only need to check it if $p=m+2$ or $n=m$. In the former case, we have $f(n)+n \not \equiv a_{p}(\bmod p)$ by construction. In the latter case, if $n=m$ and $p \leqslant m+1$, then we have $f(m)+m \equiv -a_{p} \not \equiv a_{p}(\bmod p)$, where we make use of the fact that $a_{p}$ is $p$-useful.

Now we check that (iii) holds. Suppose, to the contrary, that $p \mid \operatorname{gcd}(f(n)+m, f(m)+n)$ for some $n<m$. Then $p \in X_{m}$ and $p \mid f(m)+n$. If $p \geqslant m+2$, then $0 \equiv f(m)+n \equiv n(\bmod p)$, which is impossible since $n<m<p$.
Otherwise, if $p \leqslant m+1$, then
$$
0 \equiv (f(m)+n)+(f(n)+m) \equiv (f(n)+n)+(f(m)+m) \equiv (f(n)+n)-a_{p}(\bmod p) .
$$
This implies that $f(n)+n \equiv a_{p}(\bmod p)$, a contradiction with (ii).
