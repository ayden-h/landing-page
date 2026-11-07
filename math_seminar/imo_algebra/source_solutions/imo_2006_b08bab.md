# imo_2006_b08bab

IMO-SL | IMO | 2006 | Algebra | A5

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2006_b08bab](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_b08bab.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems with Solutions
- Year: 2006
- Editors: Bauer, Andrej; Geretschläger, Robert; Kós, Géza; Kuczma, Marcin; Savchev, Svetoslav
- Organization: International Mathematical Olympiad
- Place: Slovenia
- Series: International Mathematical Olympiad
- Volume: 47
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Note first that the denominators are all positive, e.g. $\sqrt{a}+\sqrt{b}>\sqrt{a+b}>\sqrt{c}$.
Let $x=\sqrt{b}+\sqrt{c}-\sqrt{a}$, $y=\sqrt{c}+\sqrt{a}-\sqrt{b}$ and $z=\sqrt{a}+\sqrt{b}-\sqrt{c}$. Then
$b+c-a=\left(\frac{z+x}{2}\right)^{2}+\left(\frac{x+y}{2}\right)^{2}-\left(\frac{y+z}{2}\right)^{2}=\frac{x^{2}+x y+x z-y z}{2}=x^{2}-\frac{1}{2}(x-y)(x-z)$
and
$$
\frac{\sqrt{b+c-a}}{\sqrt{b}+\sqrt{c}-\sqrt{a}}=\sqrt{1-\frac{(x-y)(x-z)}{2 x^{2}}} \leq 1-\frac{(x-y)(x-z)}{4 x^{2}},
$$
applying $\sqrt{1+2 u} \leq 1+u$ in the last step. Similarly we obtain
$$
\frac{\sqrt{c+a-b}}{\sqrt{c}+\sqrt{a}-\sqrt{b}} \leq 1-\frac{(z-x)(z-y)}{4 z^{2}} \quad \text{ and } \quad \frac{\sqrt{a+b-c}}{\sqrt{a}+\sqrt{b}-\sqrt{c}} \leq 1-\frac{(y-z)(y-x)}{4 y^{2}} .
$$
Substituting these quantities into the statement, it is sufficient to prove that
$$
\begin{equation*}
\frac{(x-y)(x-z)}{x^{2}}+\frac{(y-z)(y-x)}{y^{2}}+\frac{(z-x)(z-y)}{z^{2}} \geq 0 . \tag{1}
\end{equation*}
$$
By symmetry we can assume $x \leq y \leq z$. Then
$$
\begin{gathered}
\frac{(x-y)(x-z)}{x^{2}}=\frac{(y-x)(z-x)}{x^{2}} \geq \frac{(y-x)(z-y)}{y^{2}}=-\frac{(y-z)(y-x)}{y^{2}} \\
\frac{(z-x)(z-y)}{z^{2}} \geq 0
\end{gathered}
$$
and (1) follows.

## Supplied solution 2

Due to the symmetry of variables, it can be assumed that $a \geq b \geq c$. We claim that
$$
\frac{\sqrt{a+b-c}}{\sqrt{a}+\sqrt{b}-\sqrt{c}} \leq 1 \quad \text{ and } \quad \frac{\sqrt{b+c-a}}{\sqrt{b}+\sqrt{c}-\sqrt{a}}+\frac{\sqrt{c+a-b}}{\sqrt{c}+\sqrt{a}-\sqrt{b}} \leq 2 .
$$
The first inequality follows from
$$
\sqrt{a+b-c}-\sqrt{a}=\frac{(a+b-c)-a}{\sqrt{a+b-c}+\sqrt{a}} \leq \frac{b-c}{\sqrt{b}+\sqrt{c}}=\sqrt{b}-\sqrt{c} .
$$
For proving the second inequality, let $p=\sqrt{a}+\sqrt{b}$ and $q=\sqrt{a}-\sqrt{b}$. Then $a-b=p q$ and the inequality becomes
$$
\frac{\sqrt{c-p q}}{\sqrt{c}-q}+\frac{\sqrt{c+p q}}{\sqrt{c}+q} \leq 2 .
$$
From $a \geq b \geq c$ we have $p \geq 2 \sqrt{c}$. Applying the Cauchy-Schwarz inequality,
$$
\begin{gathered}
\left(\frac{\sqrt{c-p q}}{\sqrt{c}-q}+\frac{\sqrt{c+p q}}{\sqrt{c}+q}\right)^{2} \leq\left(\frac{c-p q}{\sqrt{c}-q}+\frac{c+p q}{\sqrt{c}+q}\right)\left(\frac{1}{\sqrt{c}-q}+\frac{1}{\sqrt{c}+q}\right) \\
=\frac{2\left(c \sqrt{c}-p q^{2}\right)}{c-q^{2}} \cdot \frac{2 \sqrt{c}}{c-q^{2}}=4 \cdot \frac{c^{2}-\sqrt{c} p q^{2}}{\left(c-q^{2}\right)^{2}} \leq 4 \cdot \frac{c^{2}-2 c q^{2}}{\left(c-q^{2}\right)^{2}} \leq 4
\end{gathered}
$$
