# imo_2019_aeca2a

IMO-SL | IMO | 2019 | Algebra | A7

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2019_aeca2a](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_aeca2a.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems
- Subtitle: with solutions
- Year: 2019
- Editors: Gardiner, Tony; Crane, Edward; Betts, Alexander; Cranch, James; Myers, Joseph; Aaronson, James; Carlotti, Andrew; Kós, Géza; Bogdanov, Ilya I.; Shotton, Jack
- Organization: 60th International Mathematical Olympiad
- Place: Bath, United Kingdom
- Series: International Mathematical Olympiad
- Volume: 60th
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

a) Let $f$ be the function where $f(0)=0$ and $f(x)$ is the largest power of $2$ dividing $2x$ for $x \neq 0$. The integer $0$ is evidently $f$-rare, so it remains to verify the functional equation.

Since $f(2x)=2f(x)$ for all $x$, it suffices to verify the functional equation when at least one of $x$ and $y$ is odd (the case $x=y=0$ being trivial). If $y$ is odd, then we have
$$
f(f(x+y)+y)=2=f(f(x)+y)
$$
since all the values attained by $f$ are even. If, on the other hand, $x$ is odd and $y$ is even, then we already have
$$
f(x+y)=2=f(x)
$$
from which the functional equation follows immediately.

b) An easy inductive argument (substituting $x+ky$ for $x$) shows that
$$
f(f(x+ky)+y)=f(f(x)+y)
$$
for all integers $x$, $y$ and $k$. If $v$ is an $f$-rare integer and $a$ is the least element of $X_{v}$, then by substituting $y=a-f(x)$ in the above, we see that
$$
f(x+k \cdot (a-f(x)))-f(x)+a \in X_{v}
$$
for all integers $x$ and $k$, so that in particular
$$
f(x+k \cdot (a-f(x))) \geqslant f(x)
$$
for all integers $x$ and $k$, by assumption on $a$. This says that on the (possibly degenerate) arithmetic progression through $x$ with common difference $a-f(x)$, the function $f$ attains its minimal value at $x$.

Repeating the same argument with $a$ replaced by the greatest element $b$ of $X_{v}$ shows that
$$
f(x+k \cdot (b-f(x))) \leqslant f(x)
$$
for all integers $x$ and $k$. Combined with the above inequality, we therefore have
$$
f(x+k \cdot (a-f(x)) \cdot (b-f(x)))=f(x)
$$
for all integers $x$ and $k$.

Thus if $f(x) \neq a, b$, then the set $X_{f(x)}$ contains a nondegenerate arithmetic progression, so is infinite. So the only possible $f$-rare integers are $a$ and $b$.

In particular, the $f$-rare integer $v$ we started with must be one of $a$ or $b$, so that $f(v)=f(a)=f(b)=v$. This means that there cannot be any other $f$-rare integers $v'$, as they would on the one hand have to be either $a$ or $b$, and on the other would have to satisfy $f(v')=v'$. Thus $v$ is the unique $f$-rare integer.

## Supplied solution 2

Part (b) only. Suppose $v$ is $f$-rare, and let $a$ and $b$ be the least and greatest elements of $X_{v}$, respectively. Substituting $x=v$ and $y=a-v$ into the equation shows that
$$
f(v)-v+a \in X_{v}
$$
and in particular $f(v) \geqslant v$. Repeating the same argument with $x=v$ and $y=b-v$ shows that $f(v) \leqslant v$, and hence $f(v)=v$.

Suppose now that $v'$ is a second $f$-rare integer. We may assume that $v=0$ (see Comment 1). We've seen that $f(v')=v'$; we claim that in fact $f(kv')=v'$ for all positive integers $k$. This gives a contradiction unless $v'=v=0$.

This claim is proved by induction on $k$. Supposing it to be true for $k$, we substitute $y=kv'$ and $x=0$ into the functional equation to yield
$$
f((k+1)v')=f(f(0)+kv')=f(kv')=v'
$$
using that $f(0)=0$. This completes the induction, and hence the proof.
