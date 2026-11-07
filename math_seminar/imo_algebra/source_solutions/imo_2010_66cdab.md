# imo_2010_66cdab

IMO-SL | IMO | 2010 | Algebra | A2

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2010_66cdab](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_66cdab.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: 51st International Mathematical Olympiad
- Subtitle: Shortlisted Problems with Solutions
- Year: 2010
- Editors: Baissalov, Yerzhan; Bogdanov, Ilya; Kós, Géza; Sedrakyan, Nairi; Yeliussizov, Damir; Yessenov, Kuat
- Organization: International Mathematical Olympiad
- Place: Astana, Kazakhstan
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

Checked rewritten solution: [A05](../reviewed_solutions/A05.md).

## Supplied solution 1

Observe that
$$
\begin{gathered}
4\left(a^{3}+b^{3}+c^{3}+d^{3}\right)-\left(a^{4}+b^{4}+c^{4}+d^{4}\right)=-\left((a-1)^{4}+(b-1)^{4}+(c-1)^{4}+(d-1)^{4}\right) \\
+6\left(a^{2}+b^{2}+c^{2}+d^{2}\right)-4(a+b+c+d)+4 \\
=-\left((a-1)^{4}+(b-1)^{4}+(c-1)^{4}+(d-1)^{4}\right)+52
\end{gathered}
$$
Now, introducing $x=a-1, y=b-1, z=c-1, t=d-1$, we need to prove the inequalities
$$
16 \geq x^{4}+y^{4}+z^{4}+t^{4} \geq 4
$$
under the constraint
$$
\begin{equation*}
x^{2}+y^{2}+z^{2}+t^{2}=\left(a^{2}+b^{2}+c^{2}+d^{2}\right)-2(a+b+c+d)+4=4 \tag{1}
\end{equation*}
$$
(we will not use the value of $x+y+z+t$ though it can be found).
Now the rightmost inequality in (1) follows from the power mean inequality:
$$
x^{4}+y^{4}+z^{4}+t^{4} \geq \frac{\left(x^{2}+y^{2}+z^{2}+t^{2}\right)^{2}}{4}=4
$$
For the other one, expanding the brackets we note that
$$
\left(x^{2}+y^{2}+z^{2}+t^{2}\right)^{2}=\left(x^{4}+y^{4}+z^{4}+t^{4}\right)+q
$$
where $q$ is a nonnegative number, so
$$
x^{4}+y^{4}+z^{4}+t^{4} \leq\left(x^{2}+y^{2}+z^{2}+t^{2}\right)^{2}=16
$$
and we are done.

## Supplied solution 2

First, we claim that $0 \leq a, b, c, d \leq 3$. Actually, we have
$$
a+b+c=6-d, \quad a^{2}+b^{2}+c^{2}=12-d^{2}
$$
hence the power mean inequality
$$
a^{2}+b^{2}+c^{2} \geq \frac{(a+b+c)^{2}}{3}
$$
rewrites as
$$
12-d^{2} \geq \frac{(6-d)^{2}}{3} \quad \Longleftrightarrow \quad 2 d(d-3) \leq 0
$$
which implies the desired inequalities for $d$; since the conditions are symmetric, we also have the same estimate for the other variables.
Now, to prove the rightmost inequality, we use the obvious inequality $x^{2}(x-2)^{2} \geq 0$ for each real $x$; this inequality rewrites as $4 x^{3}-x^{4} \leq 4 x^{2}$. It follows that
$$
\left(4 a^{3}-a^{4}\right)+\left(4 b^{3}-b^{4}\right)+\left(4 c^{3}-c^{4}\right)+\left(4 d^{3}-d^{4}\right) \leq 4\left(a^{2}+b^{2}+c^{2}+d^{2}\right)=48
$$
as desired.

Now we prove the leftmost inequality in an analogous way. For each $x \in[0,3]$, we have $(x+1)(x-1)^{2}(x-3) \leq 0$ which is equivalent to $4 x^{3}-x^{4} \geq 2 x^{2}+4 x-3$. This implies that $\left(4 a^{3}-a^{4}\right)+\left(4 b^{3}-b^{4}\right)+\left(4 c^{3}-c^{4}\right)+\left(4 d^{3}-d^{4}\right) \geq 2\left(a^{2}+b^{2}+c^{2}+d^{2}\right)+4(a+b+c+d)-12=36$, as desired.

## Supplied solution 3

First, expanding $48=4\left(a^{2}+b^{2}+c^{2}+d^{2}\right)$ and applying the AM-GM inequality, we have
$$
\begin{aligned}
a^{4}+b^{4}+c^{4}+d^{4}+48 & =\left(a^{4}+4 a^{2}\right)+\left(b^{4}+4 b^{2}\right)+\left(c^{4}+4 c^{2}\right)+\left(d^{4}+4 d^{2}\right) \\
& \geq 2\left(\sqrt{a^{4} \cdot 4 a^{2}}+\sqrt{b^{4} \cdot 4 b^{2}}+\sqrt{c^{4} \cdot 4 c^{2}}+\sqrt{d^{4} \cdot 4 d^{2}}\right) \\
& =4\left(\left|a^{3}\right|+\left|b^{3}\right|+\left|c^{3}\right|+\left|d^{3}\right|\right) \geq 4\left(a^{3}+b^{3}+c^{3}+d^{3}\right)
\end{aligned}
$$
which establishes the rightmost inequality.
To prove the leftmost inequality, we first show that $a, b, c, d \in[0,3]$ as in the previous solution. Moreover, we can assume that $0 \leq a \leq b \leq c \leq d$. Then we have $a+b \leq b+c \leq \frac{2}{3}(b+c+d) \leq \frac{2}{3} \cdot 6=4$.
Next, we show that $4 b-b^{2} \leq 4 c-c^{2}$. Actually, this inequality rewrites as $(c-b)(b+c-4) \leq 0$, which follows from the previous estimate. The inequality $4 a-a^{2} \leq 4 b-b^{2}$ can be proved analogously.
Further, the inequalities $a \leq b \leq c$ together with $4 a-a^{2} \leq 4 b-b^{2} \leq 4 c-c^{2}$ allow us to apply the Chebyshev inequality obtaining
$$
\begin{aligned}
a^{2}\left(4 a-a^{2}\right)+b^{2}\left(4 b-b^{2}\right)+c^{2}\left(4 c-c^{2}\right) & \geq \frac{1}{3}\left(a^{2}+b^{2}+c^{2}\right)\left(4(a+b+c)-\left(a^{2}+b^{2}+c^{2}\right)\right) \\
& =\frac{\left(12-d^{2}\right)\left(4(6-d)-\left(12-d^{2}\right)\right)}{3} .
\end{aligned}
$$
This implies that
$$
\begin{align*}
\left(4 a^{3}-a^{4}\right) & +\left(4 b^{3}-b^{4}\right)+\left(4 c^{3}-c^{4}\right)+\left(4 d^{3}-d^{4}\right) \geq \frac{\left(12-d^{2}\right)\left(d^{2}-4 d+12\right)}{3}+4 d^{3}-d^{4} \\
& =\frac{144-48 d+16 d^{3}-4 d^{4}}{3}=36+\frac{4}{3}(3-d)(d-1)\left(d^{2}-3\right) \tag{2}
\end{align*}
$$
Finally, we have $d^{2} \geq \frac{1}{4}\left(a^{2}+b^{2}+c^{2}+d^{2}\right)=3$ (which implies $d>1$ ); so, the expression $\frac{4}{3}(3-d)(d-1)\left(d^{2}-3\right)$ in the right-hand part of (2) is nonnegative, and the desired inequality is proved.
