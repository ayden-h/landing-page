# kor_2013_c1caf4

KMO | South Korea | 2013 | The First Day, March 23, 2013 | 2

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [kor_2013_c1caf4](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2013_c1caf4.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: South Korea
- Title: KOREAN MATHEMATICAL OLYMPIAD
- Subtitle: 26th Korean Mathematical Olympiad Final Round
- Year: 2013
- Organization: THE KOREAN MATHEMATICAL SOCIETY
- Publisher: THE KOREAN MATHEMATICAL SOCIETY
- Place: Seoul, Korea

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We prove the following
**Lemma** For all real $p, q, r$ that satisfy $p^2 + q^2 = r^2$, the following equality holds.
$$
f(p) + f(q) = f(r)
$$
**Proof** Put $a = \frac{p-q+r}{2}$, $b = \frac{p-q-r}{2}$, $c = \frac{p+q+r}{2}$. Then we have $ab+bc+cd = \frac{1}{2}(p^2+q^2-r^2)$. So if $p^2+q^2 = r^2$ then $ab + bc + cd = 0$ and we have
$$
f(r) + f\left(\frac{p-q-r}{2}\right) = f\left(\frac{p-q-r}{2}\right) + f(p) + f(q)
$$
Thus we have $f(p) + f(q) = f(r)$ and the proof is complete.

For $(p, q, r) = (0, 0, 0)$, we have, by the Lemma, $f(0) = 0$, and for $(p, q, r) = (p, 0, -p)$ we have $f(-p) = f(p)$ and thus $f$ is an even function.

Now for any $t \ge 0$ define $g : [0, \infty) \to [0, \infty)$ by $g(t) := f(\sqrt{t})$. Then we have $g(a+b) = g(a) + g(b)$. And for $a \ge b \ge 0$ we have $g(a) = g(a-b) + g(b) \ge g(b)$. So

g is monotone increasing. So $g(x) = g(1) \cdot x$ ($x \ge 0$). Thus $f(x) = f(1) \cdot x^2$ ($x \ge 0$) and $f$ is an even function. So $f(x) = f(1) \cdot x^2$ for any real $x$. And $f(1) \ge 0$ since $f(x) \ge 0$. Thus the functions satisfying given equality are of the form $f(x) = \lambda x^2$, ($\lambda \ge 0$) and it is easy to check that those functions satisfy the given equality. $\square$
