# chn_2025_9cc0fb

IMO-TST | China | 2025 | Test 3 · Day 2 | Problem 6.

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [chn_2025_9cc0fb](https://mathnet.mit.edu/data_v2/full/china/chn_2025_9cc0fb.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: China
- Title: 2025 International Mathematical Olympiad China National Team Selection Test
- Year: 2025
- Organization: International Mathematical Olympiad China
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $L$ denote the maximum squared modulus of the polynomial $f(z) = az^3 + bz^2 + cz + d$ on the unit circle.
By choosing a unit complex number $s$ with $s^3 = d/a$ and considering $f_1(z) = d^{-1}f(sz)$, we may assume without loss of generality that $a = d = 1$. Thus we only need to consider polynomials of the form $f(z) = z^3 + bz^2 + cz + 1$.

First consider the symmetric case $b = c = u + vi$. The polynomial factors as $f(z) = (1+z)(1+(b-1)z + z^2)$. For $z = x + yi$ on the unit circle ($x^2 + y^2 = 1$), we have:
$$
\begin{aligned}
|1+z|^2 &= 2+2x, \\
|1+(b-1)z+z^2|^2 &= 4x^2 + (2x-1)(2u-2), \\
|f(z)|^2 &= 8 \left( x^3 + ux^2 + \frac{u-1}{2}x - \frac{u-1}{2} \right).
\end{aligned}
$$
Let $h(x) = x^3 + ux^2 + \frac{u-1}{2}x - \frac{u-1}{2}$. We seek to minimize $\max_{x \in [-1,1]} h(x)$.
Heuristically, the minimum occurs when $h(x)$ has a double root at $x_0$ and a simple root at 1. Solving gives $u = 2 - \sqrt{5}$. Indeed, for this value:
$$
h(x) - (3 - \sqrt{5}) = \left( x + \frac{3 - \sqrt{5}}{2} \right)^2 (x - 1) \leq 0,
$$
$$
\text{so } |f(z)|^2 \leq 8(3 - \sqrt{5}) = (2\sqrt{5} - 2)^2.
$$
For the general case where $b = c = u + vi$, consider
$$
|f(z)|^2 = 8h(x) = (2x + 2) [(4x^2 - 4x + 2) + 2(2x - 1)u]
$$
evaluated at the "endpoint":
$$
|f(1)|^2 = 8h(1) = 8 + 8u,
$$
and at the point $z = z_{\star} = \frac{\sqrt{5}-3}{2} + \frac{\sqrt{5}-1}{2}i\sqrt{5}$ (corresponding to a possible vertex of $h(x)$):
$$
|f(z_{\star})|^2 = 8h\left(\frac{\sqrt{5}-3}{2}\right) = (30\sqrt{5}-62) + (18-10\sqrt{5})u.
$$
We have
$$
|f(z^*)|^2 + \frac{5\sqrt{5}-9}{4} \cdot |f(1)|^2 = 40\sqrt{5}-80 = \frac{5\sqrt{5}-5}{4} \cdot (2\sqrt{5}-2)^2.
$$
---

This shows that a certain weighted average of them equals $(2\sqrt{5}-2)^2$, therefore when $b=c$ we always have
$$
L \ge \max \{|f(1)|^2, |f(z_\star)|^2\} \ge (2\sqrt{5}-2)^2.
$$
For general $b, c$, we still attempt to prove $L \ge (2\sqrt{5}-2)^2$.
Let $\omega = \frac{-1+\sqrt{3}i}{2}$ be a primitive cube root of unity. Since $f(z) = z^3 + bz^2 + cz + 1$, we have $f(\omega z) = z^3 + \omega^2 bz^2 + \omega cz + 1$ and $f(\omega^2 z) = z^3 + \omega bz^2 + \omega^2 cz + 1$, all corresponding to the same $L$ value. Moreover, $(b+c) + (\omega^2 b + \omega c) + (\omega b + \omega^2 c) = 0$, and at least one of these has real part $\le 0$. Without loss of generality, assume $\frac{b+c}{2} = u + vi$ with $u \le 0$.
Since $|b| = |c| = 1$, we have $\frac{c-b}{b+c} = wi$ being purely imaginary. We may assume $w \ge 0$ (otherwise consider the reciprocal polynomial $f_2(z) = z^3 + cz^2 + bz + 1$ which has the same $L$ value). Thus $\frac{c-b}{2} = (u+vi)wi$, and $|\frac{b+c}{2}|^2 + |\frac{c-b}{2}|^2 = (u^2+v^2)(1+w^2) = 1$. Now we can express:
$$
f(z) = z^3+1+\frac{b+c}{2}(z^2+z)+\frac{c-b}{2}(z-z^2) = z(z+1) \left[ z + z^{-1} - 1 + u + vi + \frac{1-z}{1+z} \cdot wi \cdot (u+vi) \right].
$$
Note that $\frac{1-z}{1+z} \cdot wi = t$ is real. Writing the unit complex number $z = x + yi$, we have $|z+1|^2 = 2x+2$, $z+z^{-1}-1 = 2x-1$, and $u^2+v^2 = \frac{1}{1+w^2}$. Therefore:
$$
\begin{aligned}
|f(z)|^2 &= |z+1|^2 \cdot |z+z^{-1}-1+(u+vi)(1+t)|^2 \\
&= (2x+2) \left[ (2x-1+u+ut)^2 + (v+vt)^2 \right] \\
&= (2x+2) \left[ (2x-1)^2 + (u^2+v^2)(1+2t+t^2) + 2(2x-1)u + 2(2x-1)ut \right] \\
&= (2x+2) \left[ (4x^2-4x+2) + 2(2x-1)u + \frac{2t+t^2-w^2}{1+w^2} + 2(2x-1)ut \right].
\end{aligned}
$$
To prove $L \ge (2\sqrt{5}-2)^2$, we want to show:
$$
T = |f(z_\star)|^2 + \frac{5\sqrt{5}-9}{4} \cdot |f(1)|^2 - (40\sqrt{5}-80) \ge 0.
$$
First, for $z = z_\star = \frac{\sqrt{5}-3}{2} + \frac{\sqrt{5}-1}{2}\sqrt{5}i$ (where $x = \frac{\sqrt{5}-3}{2}$ and $\frac{1-z}{1+z} = -\sqrt{5}i$), we have $t = \sqrt{5}w$. Comparing with the case $b=c$, consider:
$$
\begin{aligned}
T_1 &= |f(z_\star)|^2 - \left[ (30\sqrt{5}-62) + (18-10\sqrt{5})u \right] \\
&= |f(z_\star)|^2 - (2x+2) \left[ (4x^2-4x+2) + 2(2x-1)u \right] \\
&= (2x+2) \left( \frac{2t+t^2-w^2}{1+w^2} + 2(2x-1)ut \right) \\
&= (\sqrt{5}-1) \cdot \left( \frac{2\sqrt{5}w + (\sqrt{5}-1)w^2}{1+w^2} + 2(\sqrt{5}-4)ut \right) \\
&\ge (\sqrt{5}-1) \cdot \frac{2\sqrt{5}w + (\sqrt{5}-1)w^2}{1+w^2}.
\end{aligned}
$$
---

Second, since $f(1) = 2 + 2(u + vi)$, we have $|f(1)|^2 = 4 + 4u^2 + 4v^2 + 8u$, and:
$$
T_2 = |f(1)|^2 - (8 + 8u) = 4(u^2 + v^2 - 1) = -\frac{4w^2}{1 + w^2}.
$$
Therefore:
$$
T = T_1 + \frac{5\sqrt{5}-9}{4} T_2 \ge (\sqrt{5}-1) \cdot \frac{2\sqrt[4]{5}w + (\sqrt{5}-1)w^2}{1+w^2} - (5\sqrt{5}-9) \cdot \frac{w^2}{1+w^2}.
$$
We want $T \ge 0$, which holds if:
$$
2\sqrt[4]{5}(\sqrt{5}-1)w + ((\sqrt{5}-1)^2 - (5\sqrt{5}-9))w^2 \ge 0,
$$
i.e., when:
$$
0 \le w \le \frac{2(\sqrt{5}-1)\sqrt[4]{5}}{7\sqrt{5}-15} = \frac{4+2\sqrt{5}}{\sqrt[4]{5}} \approx 5.666.
$$
Through appropriate substitutions or transformations, we have ensured $u \le 0$ and $w \ge 0$.
If $0 \le w \le 2$, then $T \ge 0$, meaning a certain weighted average of $|f(z_\star)|^2$ and $|f(1)|^2$ is $\ge (2\sqrt{5}-2)^2$, so $L \ge (2\sqrt{5}-2)^2$.
If $w \ge 2$, then $|f(1)|^2 = 4 + 4u^2 + 4v^2 + 8u \le 4 + 4 \cdot \frac{1}{1+w^2} \le 4.8$. Since:
$$
|f(1)|^2 + |f(\omega)|^2 + |f(\omega^2)|^2 = |2+b+c|^2 + |2+\omega c+\omega^2 b|^2 + |2+\omega^2 c+\omega b|^2 = 18,
$$
we have:
$$
L \ge \frac{|f(\omega)|^2 + |f(\omega^2)|^2}{2} \ge \frac{18 - 4.8}{2} = 6.6 > (2\sqrt{5} - 2)^2.
$$
Therefore, we always have $L \ge (2\sqrt{5}-2)^2$, and equality can be achieved. Thus, the minimal real number we seek is $M = 2\sqrt{5}-2$.
□
