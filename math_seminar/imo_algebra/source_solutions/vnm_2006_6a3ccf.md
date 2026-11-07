# vnm_2006_6a3ccf

VMO | Vietnam | 2006 | Second day | Problem 4

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [vnm_2006_6a3ccf](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2006_6a3ccf.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Vietnam
- Title: 2006 VIETNAMESE MATHEMATICAL OLYMPIAD
- Year: 2006

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

It is easily seen that $f(x)$ is a continuous function on $[0, \infty)$. We shall prove the following assertions:

i) $f(x)$ is strictly increasing on $[0, \infty)$;

ii) $f(0) = \sqrt{ab}$, $\lim_{x \to \infty} f(x) = \frac{a+b}{2}$;

iii) for every $s$ with $0 < s < 1$, we have:
$$
\sqrt{ab} < \left(\frac{a^s + b^s}{2}\right)^{\frac{1}{s}} \le \frac{a+b}{2}.
$$
With these assertions, the intermediate value theorem of continuous functions proves the existence of a unique $\alpha$ such that $f(\alpha) = \left(\frac{a^s + b^s}{2}\right)^{\frac{1}{s}}$.

Proof of i):
$$
f'(x) = -1 + \frac{2x+a+b}{2\sqrt{(a+x)(b+x)}} = \frac{(\sqrt{a+x}-\sqrt{b+x})^2}{2\sqrt{(a+x)(b+x)}} > 0.
$$

Proof of ii):
It is evident that $f(0) = \sqrt{ab}$ and:
$$
\lim_{x \to \infty} f(x) = \lim_{x \to \infty} \frac{-x^2 + (a+x)(b+x)}{x + \sqrt{(a+x)(b+x)}} = \lim_{x \to \infty} \frac{a+b+\frac{ab}{x}}{1+\sqrt{\left(\frac{a}{x}+1\right)\left(\frac{b}{x}+1\right)}} = \frac{a+b}{2}.
$$

Proof of iii):
The first inequality is deduced from the A-G-mean inequality.
Put $m = \left(\frac{a^s + b^s}{2}\right)^{\frac{1}{s}}$, $x = \frac{a}{m}$, $y = \frac{b}{m}$. Clearly, $x^s + y^s = 2$ and Bernoulli inequality implies that:
$$
x = (1 + x^s - 1)^{\frac{1}{s}} \ge 1 + \frac{x^s - 1}{s}
$$
$$
y = (1 + y^s - 1)^{\frac{1}{s}} \ge 1 + \frac{y^s - 1}{s}
$$
(both equalities do not hold simultaneously). From these inequalities, by adding both left sides together and both right sides together, we get $x + y > 2$.
