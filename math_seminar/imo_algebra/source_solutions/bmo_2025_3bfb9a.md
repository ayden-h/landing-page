# bmo_2025_3bfb9a

BMO-SL | Balkan Mathematical Olympiad | 2025 | Algebra | A5

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2025_3bfb9a](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_3bfb9a.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: Shortlisted Problems
- Subtitle: (with solutions)
- Year: 2025
- Editors: Smajlović, Lejla; Beširević, Admir; Đonlagić, Azur; Hindija, Harun; Velašević, Boris; Bolić, Adisa; Kurić, Amar; Macić, Ervin; Vuković, Jovan
- Organization: 42nd Balkan Mathematical Olympiad
- Place: Sarajevo — Bosnia and Herzegovina
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $P(x, y)$ denote the given relation. If there is an $a \in \mathbb{R}$ such that $f(a) = 0$, then $P(a, y)$ gives that $y = a y + f(a + y)$, and so $f$ must be linear. Then we can easily check and get that the only linear solutions are $f(x) = x$ and $f(x) = 2 - x$ ($x \in \mathbb{R}$).

Now suppose that $f(x) \neq 0$ for all real numbers $x$. From $P(x - y, y)$ we get that:
$$
f(x - y + y f(x - y)) = -y^2 + y(x - 1) + f(x).
$$
Since $f(t) \neq 0$ for all real numbers $t$, it follows that $-y^2 + y(x - 1) + f(x) \neq 0$ for all real numbers $x, y$, and so, its discriminant (as a polynomial in $y$) must be negative. That is, $(x - 1)^2 + 4 f(x) < 0$, which gives us
$$
f(x) < -\frac{(x-1)^2}{4} \leq 0
$$
for all real numbers $x$. Since $(x + 1)^2 \geq 0$ implies that $-\frac{(x-1)^2}{4} \leq x$, we see that
$$
f(x) < -\frac{(x-1)^2}{4} \leq x
$$
for all real numbers $x$. Now from $P(x, y)$ for $y > 0$ and $x \in \mathbb{R}$, we get that
$$
x y - y + f(x + y) = f(x + y f(x)) < x + y f(x) < x - y \frac{(x-1)^2}{4}
$$
and so
$$
f(x + y) < x + y - y(x + \frac{(x-1)^2}{4}) = x + y - y \frac{(x+1)^2}{4}.
$$
Setting $x = -y$ above, we get that:
$$
f(0) < -y \frac{(-y + 1)^2}{4}.
$$
for all positive real numbers $y$. Letting $y \to +\infty$ above, we reach a contradiction. Hence, the only solutions in this functional equation are $f(x) = x$ and $f(x) = 2 - x$.

## Supplied solution 2

Let $P(x, y)$ denote the given relation. Similarly to the first solution, if a root exists ($f(a) = 0$ for any $a$), we get that the function is linear and that the two solutions are $f(x) = x$ and $f(x) = 2 - x$. Assertion $P(x, c - x)$ gives us the following relation:
$$
f(x + (c - x) f(x)) = (c - x)(x - 1) + f(c) = -x^2 + (c + 1)x + (f(c) - c)
$$
The right hand side of the expression is a quadratic equation in $x$ with the discriminant $\Delta = \Delta(c) = (c + 1)^2 + 4(f(c) - c) = (c - 1)^2 + 4 f(c)$. Therefore, if there exists a $c$ such that $(c - 1)^2 + 4 f(c) \geq 0$, the quadratic equation has a real solution which implies the existence of a root, in which case we are done.
If $f(1) = 0$, then we found a root and are done. If $f(1) = 1$, then by taking $c = 1$ we obtain that $\Delta(1) = 4$, implying the existence of a root. We now check the case when $f(1) = -1$. From the assertion $P(1 - x, x)$, we obtain:
$$
f(1 - x + x f(1 - x)) = -x^2 - 1
$$
Plugging in $x = 1$, in the above assertion, we obtain that $f(f(0)) = -2$. Now plugging in $x = 1 - f(0)$ in the above assertion we get that $f(f(0) + (1 - f(0)) f(f(0))) = -(1 - f(0))^2 - 1$, simplifying and utilizing $f(f(0)) = -2$ we obtain $f(3 f(0) - 2) = -f(0)^2 + 2 f(0) - 2$. Note that if $f(0) \ge 0$, we have that $\Delta(0) = 1 + 4 f(0) > 0$, implying the existence of a root, so assume that $f(0) < 0$. Now using $c = 3 f(0) - 2$ for our discriminant value, we obtain $\Delta(3 f(0) - 2) = (3 f(0) - 3)^2 + 4 f(3 f(0) - 2) = 9(f(0) - 1)^2 + 4(-f(0)^2 + 2 f(0) - 2) = 5 f(0)^2 - 10 f(0) + 1 > 0$, implying the existence of a root, and resolving the case when $f(1) = -1$.
Now assume that $f(1) \notin \{0, 1, -1\}$. From $P(1, y)$, we obtain the relation that $f(1 + y f(1)) = f(1 + y)$. As $f(1) \ne 0$, we can inductively show that $f(1 + y f(1)^k) = f(1 + y)$ for all $k \in \mathbb{Z}$. Since $f(1) \notin \{1, -1\}$, there exists an unbounded sequence $a_n$ such that $f(a_n)$ is constant. Namely, one can take $a_n = 1 + f(1)^{2n}$ if $|f(1)| > 1$, and $a_n = 1 + f(1)^{-2n}$ if $|f(1)| < 1$, both times it holds that $f(a_n) = f(2)$. The value of the discriminant along this sequence is $\Delta(a_n) = (a_n - 1)^2 + 4 f(a_n) = (a_n - 1)^2 + 4 f(2)$, and since $a_n$ is unbounded this there exists $n$ where the value of the discriminant is positive, yielding our root. This finishes the problem.
