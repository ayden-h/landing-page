# vnm_2023_3e5eba

VMO | Vietnam | 2023 | Day 1 (February 24th, 2023) | 3

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [vnm_2023_3e5eba](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2023_3e5eba.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Vietnam
- Title: VIETNAMESE MATHEMATICAL COMPETITIONS
- Year: 2023
- Editors: Lữ, Lê Phúc; Nghĩa, Trương Tuấn
- Place: Hanoi
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $a \to 0^+$ and $b = c = 1$, one can get
$$
2 + \frac{1}{k} \geq \frac{k+3}{2}
$$
so $k \leq 2$. For $k = 2$, we need to prove that
$$
\frac{1}{2ab + c^2} + \frac{1}{2bc + a^2} + \frac{1}{2ca + b^2} \geq \frac{5}{a^2 + b^2 + c^2}
$$
is true for all positive triples $(a, b, c)$ satisfying $a^2 + b^2 + c^2 = 2(ab + bc + ca)$. First, we will prove that
$$
\frac{1}{a^2 + 2bc} + \frac{1}{b^2 + 2ac} + \frac{1}{c^2 + 2ab} \geq \frac{2}{ab + bc + ac} + \frac{1}{a^2 + b^2 + c^2}
$$
true for all positive real numbers $a, b, c$. Indeed, the above inequality can be rewritten as
$$
\frac{a^2 + b^2 + c^2}{a^2 + 2bc} + \frac{a^2 + b^2 + c^2}{b^2 + 2ac} + \frac{a^2 + b^2 + c^2}{c^2 + 2ab} \geq \frac{2(a^2 + b^2 + c^2)}{ab + bc + ca} + 1,
$$
thus
$$
\frac{(b-c)^2}{a^2+2bc} + \frac{(c-a)^2}{b^2+2ca} + \frac{(a-b)^2}{c^2+2ab} \geq \frac{(a-b)^2 + (b-c)^2 + (c-a)^2}{ab+bc+ac}.
$$
If $(a-b)(b-c)(c-a) = 0$ then the above inequality is true. Now consider the case $(a-b)(b-c)(c-a) \neq 0$, then
$$
\begin{aligned}
LHS &\ge \frac{\left[\sum (b-c)^2\right]^2}{\sum (a^2+2bc)(b-c)^2} = \frac{\left[\sum (b-c)^2\right]^2}{(ab+bc+ca)\left[\sum (b-c)^2\right]} \\
&= \frac{(a-b)^2 + (b-c)^2 + (c-a)^2}{ab+bc+ac} = RHS.
\end{aligned}
$$
Back to the original problem, applying the above inequality, combined with $a^2 + b^2 + c^2 = 2(ab + bc + ca)$, we get
$$
\begin{aligned}
\frac{1}{a^2+2bc} + \frac{1}{b^2+2ac} + \frac{1}{c^2+2ab} &\ge \frac{2}{ab+bc+ac} + \frac{1}{a^2+b^2+c^2} \\
&= \frac{5}{a^2+b^2+c^2}.
\end{aligned}
$$
So the maximum positive real number $k$ is 2. $\Box$
