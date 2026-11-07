# usa_2014_eef9b1

USAMO | United States | 2014 | USAMO 2014 Problems | 3.

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [usa_2014_eef9b1](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_eef9b1.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: United States
- Title: USA and International Mathematical Olympiads
- Year: 2013-2014
- Editors: Feng, Zuming; Lian, Carl; Sun, Yi
- Organization: Mathematical Association of America

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

**Solution 1** (by Razvan Gelca). We claim that defining $P_n$ to be the point with coordinates $(n, n^3 - 2014n^2)$ will satisfy the conditions of the problem. Recall that points $(x_1, y_1)$, $(x_2, y_2)$ and $(x_3, y_3)$ are collinear if and only if
$$
\begin{vmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{vmatrix} = 0.
$$
Therefore we examine the determinant
$$
\begin{vmatrix} a & a^3 - 2014a^2 & 1 \\ b & b^3 - 2014b^2 & 1 \\ c & c^3 - 2014c^2 & 1 \end{vmatrix} = \begin{vmatrix} a & a^3 & 1 \\ b & b^3 & 1 \\ c & c^3 & 1 \end{vmatrix} - 2014 \begin{vmatrix} a & a^2 & 1 \\ b & b^2 & 1 \\ c & c^2 & 1 \end{vmatrix}.
$$
The first determinant on the right is a homogenous polynomial of degree four divisible by $(a-b)(b-c)(c-a)$. The remaining factor has degree one, is symmetric, and yields an $ab^3$ term when the product is expanded, hence must be $(a+b+c)$. The second determinant is a homogenous polynomial of degree three divisible by $(a-b)(b-c)(c-a)$, and comparing coefficients of the $ab^2$ term we see that this is the desired polynomial. Thus
$$
\begin{vmatrix} a & a^3 - 2014a^2 & 1 \\ b & b^3 - 2014b^2 & 1 \\ c & c^3 - 2014c^2 & 1 \end{vmatrix} = (a-b)(b-c)(c-a)(a+b+c-2014).
$$
It follows that for distinct $a, b$ and $c$ this expression will equal zero if and only if $a + b + c = 2014$, as desired.

## Supplied solution 2

**Solution 2** (by Sam Vandervelde). First, note that the translation $x \mapsto x - 671$ in the indices allows us to replace 2014 in the statement by 1. Now it comes natural to look for a polynomial pattern $(P(x), Q(x))$ in the coordinates of a point. The collinearity condition translates, in coordinates, into
$$
P(a)Q(b) + P(b)Q(c) + P(c)Q(a) - P(a)Q(c) - P(b)Q(a) - P(c)Q(b) = 0.
$$
This should happen only when $a+b+c-1=0$ or when two of $a, b, c$ are equal. Hence the left-hand side should be of the form $(a+b+c-1)(b-a)(c-b)(a-c)R(a,b,c)$. We can try the simplest case $R=1$ so that the dominant coefficients of both $P(x)$ and $Q(x)$ are 1. $P(x)$ and $Q(x)$ cannot both have even degree because then the 4th degree terms on the left cancel out, while on the right there are clearly 4th degree terms. Hence one of the polynomials $P(x)$ and $Q(x)$ has degree 3, the other has degree 1. By a translation we can turn the degree 1 polynomial into $x$, thus we may assume that $P(x) = x$. Thus we should have
$$
\begin{aligned}
& (c-b)Q(a) + (a-c)Q(b) + (b-a)Q(c) \\
&= (a+b+c-1)(b-a)(c-b)(a-c).
\end{aligned}
$$
So we let $Q(x) = x^3 + \alpha x^2 + \beta x + \gamma$. Note that we are free to choose $\beta$ and $\gamma$ any way we want, since they cancel out. So we let $Q(x) = x^3 + \alpha x^2$.
For $a=0, b=-1, c=1$ the above identity yields $-2Q(0) - Q(-1) - Q(1) = 2$, and hence $\alpha = -1$.
Returning to the case of the problem with 2014 instead of 1, we have the points $P_n = (n - 671, (n - 671)^3 - (n - 671)^2)$. But we can simplify this since we can replace $P(x)$ by $x$ and ignore the linear part of $Q(x)$. We thus obtain the simpler infinite family of points
$$
P_n = (n, n^3 - 3 \cdot 671n^2 - n^2) = (n, n^3 - 2014n^2)
$$
satisfying the conditions of the problem.
