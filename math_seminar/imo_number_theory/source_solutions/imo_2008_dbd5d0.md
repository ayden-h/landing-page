# imo_2008_dbd5d0

IMO-SL | IMO | 2008 | Number Theory | N1

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2008_dbd5d0](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_dbd5d0.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: 49th International Mathematical Olympiad
- Subtitle: Shortlisted Problems with Solutions
- Year: 2008
- Editors: Velázquez, Vicente Muñoz; Calero, Juan Manuel Conde; Kós, Géza; Kuczma, Marcin; Medarde, Daniel Lasaosa; Riera, Ignasi Mundet i; Savchev, Svetoslav
- Place: Madrid, Spain
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

Checked rewritten solution: [N04](../reviewed_solutions/N04.md).

## Supplied solution 1

If two of $a, b, c$ are equal, it is immediate that all the three are equal. So we may assume that $a \neq b \neq c \neq a$. Subtracting the equations we get $a^{n}-b^{n}=-p(b-c)$ and two cyclic copies of this equation, which upon multiplication yield
$$
\frac{a^{n}-b^{n}}{a-b} \cdot \frac{b^{n}-c^{n}}{b-c} \cdot \frac{c^{n}-a^{n}}{c-a}=-p^{3} .
$$
If $n$ is odd then the differences $a^{n}-b^{n}$ and $a-b$ have the same sign and the product on the left is positive, while $-p^{3}$ is negative. So $n$ must be even.
Let $d$ be the greatest common divisor of the three differences $a-b, b-c, c-a$, so that $a-b=d u, b-c=d v, c-a=d w ; \operatorname{gcd}(u, v, w)=1, u+v+w=0$.
From $a^{n}-b^{n}=-p(b-c)$ we see that $(a-b) \mid p(b-c)$, i.e., $u \mid p v$; and cyclically $v|p w, w| p u$. As $\operatorname{gcd}(u, v, w)=1$ and $u+v+w=0$, at most one of $u, v, w$ can be divisible by $p$. Supposing that the prime $p$ does not divide any one of them, we get $u|v, v| w, w \mid u$, whence $|u|=|v|=|w|=1$; but this quarrels with $u+v+w=0$.
Thus $p$ must divide exactly one of these numbers. Let e.g. $p \mid u$ and write $u=p u_{1}$. Now we obtain, similarly as before, $u_{1}|v, v| w, w \mid u_{1}$ so that $\left|u_{1}\right|=|v|=|w|=1$. The equation $p u_{1}+v+w=0$ forces that the prime $p$ must be even; i.e. $p=2$. Hence $v+w=-2 u_{1}= \pm 2$, implying $v=w(= \pm 1)$ and $u=-2 v$. Consequently $a-b=-2(b-c)$.
Knowing that $n$ is even, say $n=2 k$, we rewrite the equation $a^{n}-b^{n}=-p(b-c)$ with $p=2$ in the form
$$
\left(a^{k}+b^{k}\right)\left(a^{k}-b^{k}\right)=-2(b-c)=a-b .
$$
The second factor on the left is divisible by $a-b$, so the first factor ( $a^{k}+b^{k}$ ) must be $\pm 1$. Then exactly one of $a$ and $b$ must be odd; yet $a-b=-2(b-c)$ is even. Contradiction ends the proof.

## Supplied solution 2

The beginning is as in the first solution. Assuming that $a, b, c$ are not all equal, hence are all distinct, we derive equation (1) with the conclusion that $n$ is even. Write $n=2 k$.
Suppose that $p$ is odd. Then the integer
$$
\frac{a^{n}-b^{n}}{a-b}=a^{n-1}+a^{n-2} b+\cdots+b^{n-1},
$$
which is a factor in (1), must be odd as well. This sum of $n=2 k$ summands is odd only if $a$ and $b$ have different parities. The same conclusion holding for $b, c$ and for $c, a$, we get that $a, b, c, a$ alternate in their parities, which is clearly impossible.
Thus $p=2$. The original system shows that $a, b, c$ must be of the same parity. So we may divide (1) by $p^{3}$, i.e. $2^{3}$, to obtain the following product of six integer factors:
$$
\frac{a^{k}+b^{k}}{2} \cdot \frac{a^{k}-b^{k}}{a-b} \cdot \frac{b^{k}+c^{k}}{2} \cdot \frac{b^{k}-c^{k}}{b-c} \cdot \frac{c^{k}+a^{k}}{2} \cdot \frac{c^{k}-a^{k}}{c-a}=-1 .
$$
Each one of the factors must be equal to $\pm 1$. In particular, $a^{k}+b^{k}= \pm 2$. If $k$ is even, this becomes $a^{k}+b^{k}=2$ and yields $|a|=|b|=1$, whence $a^{k}-b^{k}=0$, contradicting (2).
Let now $k$ be odd. Then the sum $a^{k}+b^{k}$, with value $\pm 2$, has $a+b$ as a factor. Since $a$ and $b$ are of the same parity, this means that $a+b= \pm 2$; and cyclically, $b+c= \pm 2, c+a= \pm 2$. In some two of these equations the signs must coincide, hence some two of $a, b, c$ are equal. This is the desired contradiction.
