# imo_2009_c42bed

IMO-SL | IMO | 2009 | Algebra | A2

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2009_c42bed](https://mathnet.mit.edu/data_v2/full/imo/imo_2009_c42bed.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Problem Shortlist with solutions
- Year: 2009
- Editors: Engel, Konrad; Fegert, Karl; Felgenhauer, Andreas; Gronau, Hans-Dietrich; Labahn, Roger; Mulansky, Bernd; Prestin, Jürgen; Reiher, Christian; Scholze, Peter; Specht, Eckard; Strich, Robert; Welk, Martin
- Organization: Federal Ministry of Education and Research; Die Senatorin für Bildung und Wissenschaft; Freie Hansestadt Bremen; Bildung Begabung; JACOBS UNIVERSITY
- Place: Bremen, Germany
- Series: International Mathematical Olympiad
- Volume: 50th
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

Checked rewritten solution: [A12](../reviewed_solutions/A12.md).

## Supplied solution 1

For positive real numbers $x$, $y$, $z$, from the arithmetic-geometric-mean inequality,
$$
2x + y + z = (x + y) + (x + z) \geq 2 \sqrt{(x + y)(x + z)}
$$
we obtain
$$
\frac{1}{(2x + y + z)^2} \leq \frac{1}{4(x + y)(x + z)}
$$
Applying this to the left-hand side terms of the inequality to prove, we get
$$
\begin{align*}
\frac{1}{(2a + b + c)^2} &+ \frac{1}{(2b + c + a)^2} + \frac{1}{(2c + a + b)^2} \\
&\leq \frac{1}{4(a + b)(a + c)} + \frac{1}{4(b + c)(b + a)} + \frac{1}{4(c + a)(c + b)} \\
&= \frac{(b + c) + (c + a) + (a + b)}{4(a + b)(b + c)(c + a)} = \frac{a + b + c}{2(a + b)(b + c)(c + a)} \tag{1}
\end{align*}
$$
A second application of the inequality of the arithmetic-geometric mean yields
$$
a^2 b + a^2 c + b^2 a + b^2 c + c^2 a + c^2 b \geq 6abc
$$
or, equivalently,
$$
\begin{equation*}
9(a + b)(b + c)(c + a) \geq 8(a + b + c)(ab + bc + ca) \tag{2}
\end{equation*}
$$
The supposition $\frac{1}{a} + \frac{1}{b} + \frac{1}{c} = a + b + c$ can be written as
$$
\begin{equation*}
ab + bc + ca = abc(a + b + c) . \tag{3}
\end{equation*}
$$
Applying the arithmetic-geometric-mean inequality $x^2 y^2 + x^2 z^2 \geq 2x^2 y z$ thrice, we get
$$
a^2 b^2 + b^2 c^2 + c^2 a^2 \geq a^2 b c + a b^2 c + a b c^2
$$
which is equivalent to
$$
\begin{equation*}
(ab + bc + ca)^2 \geq 3abc(a + b + c) \tag{4}
\end{equation*}
$$
Combining (1), (2), (3), and (4), we will finish the proof:
$$
\begin{aligned}
\frac{a + b + c}{2(a + b)(b + c)(c + a)} &= \frac{(a + b + c)(ab + bc + ca)}{2(a + b)(b + c)(c + a)} \cdot \frac{ab + bc + ca}{abc(a + b + c)} \cdot \frac{abc(a + b + c)}{(ab + bc + ca)^2} \\
&\leq \frac{9}{2 \cdot 8} \cdot 1 \cdot \frac{1}{3} = \frac{3}{16}
\end{aligned}
$$

## Supplied solution 2

Equivalently, we prove the homogenized inequality
$$
\frac{(a + b + c)^2}{(2a + b + c)^2} + \frac{(a + b + c)^2}{(a + 2b + c)^2} + \frac{(a + b + c)^2}{(a + b + 2c)^2} \leq \frac{3}{16}(a + b + c)\left(\frac{1}{a} + \frac{1}{b} + \frac{1}{c}\right)
$$
for all positive real numbers $a$, $b$, $c$. Without loss of generality we choose $a + b + c = 1$. Thus, the problem is equivalent to prove for all $a$, $b$, $c > 0$, fulfilling this condition, the inequality
$$
\begin{equation*}
\frac{1}{(1 + a)^2} + \frac{1}{(1 + b)^2} + \frac{1}{(1 + c)^2} \leq \frac{3}{16}\left(\frac{1}{a} + \frac{1}{b} + \frac{1}{c}\right) \tag{5}
\end{equation*}
$$
Applying Jensen's inequality to the function $f(x) = \frac{x}{(1 + x)^2}$, which is concave for $0 \leq x \leq 2$ and increasing for $0 \leq x \leq 1$, we obtain
$$
\alpha \frac{a}{(1 + a)^2} + \beta \frac{b}{(1 + b)^2} + \gamma \frac{c}{(1 + c)^2} \leq (\alpha + \beta + \gamma) \frac{A}{(1 + A)^2}, \quad \text{ where } \quad A = \frac{\alpha a + \beta b + \gamma c}{\alpha + \beta + \gamma} .
$$
Choosing $\alpha = \frac{1}{a}$, $\beta = \frac{1}{b}$, and $\gamma = \frac{1}{c}$, we can apply the harmonic-arithmetic-mean inequality
$$
A = \frac{3}{\frac{1}{a} + \frac{1}{b} + \frac{1}{c}} \leq \frac{a + b + c}{3} = \frac{1}{3} < 1
$$
Finally we prove (5):
$$
\begin{aligned}
\frac{1}{(1 + a)^2} + \frac{1}{(1 + b)^2} + \frac{1}{(1 + c)^2} &\leq \left(\frac{1}{a} + \frac{1}{b} + \frac{1}{c}\right) \frac{A}{(1 + A)^2} \\
&\leq \left(\frac{1}{a} + \frac{1}{b} + \frac{1}{c}\right) \frac{\frac{1}{3}}{\left(1 + \frac{1}{3}\right)^2} = \frac{3}{16}\left(\frac{1}{a} + \frac{1}{b} + \frac{1}{c}\right)
\end{aligned}
