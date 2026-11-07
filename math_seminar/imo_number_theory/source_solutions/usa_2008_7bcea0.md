# usa_2008_7bcea0

IMO-TST | United States | 2008 | TST 2008 Problems | 6

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [usa_2008_7bcea0](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_7bcea0.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: United States
- Title: USA and International Mathematical Olympiads 2007-2008
- Editors: Feng, Zuming; Sun, Yi
- Organization: University of Nebraska-Lincoln

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $p_1 \cdots p_r q_1^2 \cdots q_s$ be the prime factorization of $n$. Then the number of achievable signatures is $p_1^{p_1} \cdots p_r^{p_r} q_1^{3q_1} \cdots q_s^{3q_s}$.

We begin by reducing to the case in which $n$ is a prime or the square of a prime. Assume for now that our claim holds in these cases. Observe that the signature of a polynomial $f(x)$ modulo $n$ is completely determined by the collection of its signatures modulo $p_1, \dots, p_r, q_1^2, \dots, q_s^2$. Indeed, for each such modulus $m_i$, the sequence $f(1), \dots, f(m_i)$ modulo $m_i$ determines the entire sequence $f(1), \dots, f(n)$ modulo $m_i$ because $a \equiv b \pmod{m_i}$ implies $f(a) \equiv f(b) \pmod{m_i}$. Since the moduli $p_1, \dots, p_r, q_1^2, \dots, q_s^2$ are relatively prime with product $n$, it follows by the Chinese Remainder Theorem that specifying $f(1), \dots, f(n)$ modulo all $m_i$ is equivalent to specifying the sequence modulo $n$.

Conversely, we need to show that every sequence $y_1, \dots, y_n \pmod{n}$ obtained by applying the above procedure to a collection of signatures $f_i(1), \dots, f_i(m_i) \pmod{m_i}$ is actually the signature of a polynomial $f(x)$. To do this, we apply the Chinese Remainder Theorem once more: define $f(x)$ by choosing its coefficients such that
$$
[x^k]f(x) \equiv [x^k]f_i(x) \pmod{m_i}
$$
for all $i$. Then $f(x) \equiv f_i(x) \pmod{m_i}$ for all $i$, and the claim follows.

By the above, it suffices to show that the number of achievable signatures modulo $p$ is $p^p$ and the number of achievable signatures modulo $p^2$ is $p^{3p}$. In the first case, this amounts to showing that all $p$-term sequences modulo $p$ can be realized as $f(1), \dots, f(p)$ for some polynomial $f(x)$. There are a number of quick proofs of this result, all of which ultimately use the fact that the integers modulo $p$ form a field. A direct approach is to use Lagrange interpolation; another method is to use Lagrange's theorem to deduce that no two polynomials in $\mathbb{Z}/p\mathbb{Z}$ of degree less than $p$ have the same signature modulo $p$. Yet another approach is to show that the linear transformation (over $\mathbb{Z}/p\mathbb{Z}$) that sends the coefficient vector ($[x^0]f(x), \dots, [x^{p-1}]f(x)$) to the values ($f(1), \dots, f(p)$) is nonsingular; this can be done by evaluating the Vandermonde determinant.

The modulus $p^2$ is trickier to handle. We begin by using an idea similar to Lagrange interpolation to exhibit a set of polynomials achieving $p^{3p}$ distinct signatures modulo $p^2$, thus obtaining a lower bound. We then establish a matching upper bound by finding a (different!) set of $p^{3p}$ polynomials such that all integer-coefficient polynomials can be easily “reduced” to one of these, keeping the signature fixed during the reduction.

To prove our lower bound, we begin by defining
$$
f_k(x) = ((x-1) \cdots (x-(k-1))(x-(k+1)) \cdots (x-p))^2
$$
and
$$
g_k(x) = (x-k)f_k(x).
$$
Consider all polynomials of the form
$$
\sum_{k=1}^{p} a_k f_k(x) + b_k g_k(x)
$$
where $1 \le a_k \le p^2$ and $1 \le b_k \le p$. We claim that no two such polynomials have the same signature modulo $p^2$; this will establish our lower bound.

By subtracting, it is enough to show that the only polynomial
$$
f(x) = \sum_{k=1}^{p} a_k f_k(x) + b_k g_k(x)
$$
satisfying $f(1) \equiv \cdots \equiv f(p^2) \equiv 0 \pmod{p^2}$ with $|a_k| < p^2$ and $|b_k| < p$ is the zero polynomial. In fact, it suffices to evaluate $f(x) \pmod{p^2}$ at $x = 1, \dots, 2p$. For $j = 1, \dots, p$, we have $g_k(j) = 0$ for all $k$ and $f_k(j) = 0$ unless $k = j$, in which case $f_j(j)$ is invertible modulo $p^2$. It follows that $0 \equiv f(j) = a_j f_j(j)$ and hence $a_j \equiv 0 \pmod{p^2}$, so $a_k = 0$ for all $k$.

Next we evaluate $f(x)$ at $j = p + 1, \dots, 2p$. This time, all $g_k(j)$ vanish modulo $p^2$ except when $k = j - p$, in which case $g_{j-p}(j)$ is divisible by $p$ but not $p^2$. Thus, $0 \equiv f(j) \equiv b_{j-p}g_{j-p}(j) \pmod{p^2}$ and hence $b_{j-p} \equiv 0 \pmod{p}$, so $b_k = 0$ for all $k$, completing the proof of the lower bound.

It remains to prove that no more than $p^{3p}$ signatures modulo $p^2$ are attainable. Given two polynomials $f(x)$ and $g(x)$, we say that they are equivalent, denoted $f(x) \sim g(x)$, if they have the same signature modulo $p^2$. It is easy to see that $f(x) \sim g(x)$ implies $f(x)h(x) \sim g(x)h(x)$ and $f(x) + h(x) \sim g(x) + h(x)$ for any polynomial $h(x)$. We claim that every polynomial $f(x)$ is equivalent to a polynomial $g(x)$ such that
$$
[x^k]g(x) \in \{1, \dots, p^2\} \quad \text{for } 0 \le k < p
$$
and
$$
[x^k]g(x) \in \{1, \dots, p\} \quad \text{for } p \le k < 2p.
$$
The key observation is that by Fermat, $x^p - x$ vanishes modulo $p$ when evaluated at any integer. Therefore, $(x^p - x)^2$ and $p(x^p - x)$ both vanish modulo $p^2$ at all integers, i.e.
$$
x^{2p} \sim 2x^{p+1} - x^2 \quad \text{and} \quad px^p \sim px.
$$
Using the properties of $\sim$ stated above, the first relation allows us to reduce $f(x)$ to a polynomial of degree less than $p$; the second relation then allows us to further reduce to a polynomial with all coefficients of $x^p, \dots, x^{2p-1}$ in $\{1, \dots, p\}$. Finally, the remaining coefficients can be reduced modulo $p^2$ to lie in $\{1, \dots, p^2\}$, completing the proof.
