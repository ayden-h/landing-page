# ind_2024_be9bfd

IMO-TST | India | 2024 | IMO TST 2024 Day 1 | 3

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [ind_2024_be9bfd](https://mathnet.mit.edu/data_v2/full/india/ind_2024_be9bfd.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: India
- Title: INDIAN MATHEMATICAL OLYMPIADS
- Subtitle: Problems Booklet
- Year: 2023-24
- Organization: INDIAN MATHEMATICAL OLYMPIADS
- Series: Indian Mathematical Olympiads

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

FTSOC, assume that there is such a sequence.
We proceed with the solution in two steps. In the first step, we show that all $a_i$ must be of the form $\frac{k_i}{n}$ where $k_i \in \mathbb{Z}$ and $n$ is a fixed natural dependent only on $P$ and $a_1$.
First, we write the polynomial $P$ as $\frac{Q}{N}$ where $Q = \sum_{i=0}^{d} b_i x^i$ is an integer polynomial, $N$ is the lcm of the denominators of all coefficients and $d$ is the degree of $P$.
**Claim 1.** For any prime $p$ and $i \in \mathbb{N}$, we have
$$
\nu_p(a_i) \geq \min(-\nu_p(b_d), \nu_p(a_1))
$$
*Proof.* Suppose $\nu_p(a_i) < -\nu_p(b_d)$. Now,
$$
\nu(b_d a_i^d) = \nu(b_d) + d \nu_p(a_i) < j \nu_p(a_i) \text{ for any } j < d \text{ as } \nu_p(a_i) < 0, -\nu_p(b_d).
$$
Thus, $\nu_p(b_d a_i^d) < \nu_p(b_j a_i^j)$ for all other $j$. Thus, $\nu_p(b_d a_i^d) = \nu_p Q(a_i) \implies \nu_p(P(a_i)) = \nu_p(Q(a_i)) - \nu_p(N) < \nu_p(a_i) < 0$ since $d \ge 2$. Since $\nu_p(i) \ge 0$,
$$
\nu_p(a_{i-1}) = \nu_p(P(a_i) - i) = \nu_p(P(a_i)) < \nu_p(a_i).
$$
Repeating this, we get that
$$
\nu_p(a_1) < \nu_p(a_2) < \dots < \nu_p(a_i)
$$
Thus, if $\nu_p(a_i) < -\nu_p(b_d)$ then $\nu_p(a_i) > \nu_p(a_1)$ implying the claim! $\square$
**Lemma 1.** There exists an $N$ such that for all $i \in \mathbb{N}$, we have that $N \cdot a_i$ is integral.
*Proof.* Follows directly from Claim 1. $\square$
**Claim 2.** The sequence $a_i$ is unbounded.
*Proof.* If $a_i$ are bounded then $P(a_i)$ are also bounded (since $P$ is a continuous function). Thus $P(a_i) - a_{i-1} = i$ is bounded which is ridiculous. Thus, $a_i$ are unbounded. $\square$

**Solution A** We will first show that $P$ can have degree at most 2 by a counting argument.
**Claim A1.** There exists $m \in \mathbb{N}$ such that $\forall i > m, |a_i| < i$.
*Proof.* Let $n_1$ be a number such that for all $x$ with $|x| > n_1$, we have $|P(x)| > 2|x|$.
Now, consider the minimal $j \ge 1$, such we have that $|a_j| > \max(j, n_1, |a_0|)$, then observe that:
$$
|a_{j-1}| \ge |P(a_j)| - j > 2|a_j| - j > |a_j|
$$
This contradicts the minimality of $j$. Thus, there is no such $j$. But since the sequence is unbounded, we must have that for all large $j$ such that
$$
\max(n_1, |a_0|) < j \implies |a_j| < j. \quad \square
$$
**Claim A2.** (Few distinct $a_i$) There exists some $\alpha > 0$ such that $|\{a_1, a_2, \dots, a_n\}| < \alpha n^{\frac{1}{d}}$ for all $n \in \mathbb{N}$.
*Proof.* From the previous claim, we get that there exists a $c > 0$ such that $|a_n| < cn$ for all $n$.
Now, we have that
$$
\{a_0, a_1, \dots, a_n\} \subset [-cn, cn] \implies \{P(a_1) - 1, P(a_2) - 2, \dots, P(a_{n+1}) - n - 1\} \subset [-cn, cn]
$$
Thus, $\{P(a_1), P(a_2), \dots, P(a_n)\} \subset [-(c+2)n, (c+2)n]$ for all large enough $n$.
Now, there exists a $c' > 0$ such that for all $n > 0$, we have that for any $r$ with $|r| > c'n^{\frac{1}{d}}$,
$$
|P(r)| > (c+2)n
$$
Thus,
$$
\{a_1, a_2, \dots, a_n\} \subset [-c'n^{\frac{1}{d}}, c'n^{\frac{1}{d}}]
$$
but then since $Na_i$ is integral for all $i$, we get that $|\{a_1, a_2, \dots, a_n\}| < 4Nc'n^{\frac{1}{d}}$ where $4Nc'$ is a constant. So we just use $\alpha$ to denote this constant. Thus, we have
$$
|\{a_1, a_2, \dots, a_n\}| < \alpha n^{\frac{1}{d}}. \quad \square
$$
**Claim A3.** There exists a $\beta > 0$ such that for all large $n$, we have that some value $b$ (which may depend on $n$) appears at least $\beta n^{1-\frac{1}{d}}$ times in $a_1, a_2, \dots, a_n$.
*Proof.* This follows simply by pigeon hole principle on Claim A2. $\square$
**Lemma A1.** For any $i \neq j$ with $i, j \ge 1$, we have that $a_i = a_j \implies a_{i-1} \neq a_{j-1}$.
*Proof.*
$$
a_i = a_j \implies P(a_i) = P(a_j) \implies P(a_i) - i \neq P(a_j) - j \implies a_{i-1} \neq a_{j-1}. \quad \square
$$
Due to Claim A3, we may suppose $a_{x_1} = a_{x_2} = \dots = a_{x_m}$ where $1 \le x_i \le n$ for all $i$, and $m = \beta n^{1-\frac{1}{d}}$. Then by Lemma A1, all of $a_{x_{1-1}}, a_{x_{2-1}}, \dots, a_{x_{m-1}}$ are all pairwise distinct.
Thus, for all large enough $n$, we have
$$
\beta n^{1-\frac{1}{d}} \le |\{a_{x_1-1}, a_{x_2-1}, \dots, a_{x_m-1}\}| \le |\{a_0, \dots, a_n\}| \le \alpha n^{\frac{1}{d}} + 1 \le 2\alpha n^{\frac{1}{d}}.
$$
Thus, for all large enough $n$, we have $n^{1-\frac{2}{d}} \le 2\alpha\beta^{-1}$. This is a contradiction if $d > 2!$.
Observe that the same proof gives us a contradiction if $|\{a_1, \dots, a_n\}| = o(\sqrt{n})$ even when $d = 2$.
Thus, we can assume that there exists a $\gamma > 0$ such that for infinitely many $n$, $|a_n| > \sqrt{\gamma n}$.
Now, we handle $d = 2$ separately.
By completing the square, we assume that our polynomial is of the form $P(x) = c(x - a)^2 + b$ for some $a, b, c \in \mathbb{R}$ and $c \neq 0$. We can assume the $N$ from Lemma 1 also satisfies $Na \in \mathbb{Z}$ by increasing it if necessary.
Thus,
$$
P(x) - P(y) = c(x - y)(x + y - 2a)
$$
If $M > |P(x) - P(y)| > 0$, then $0 < |x - y| \cdot |x + y - 2a| < \frac{M}{|c|}$. Thus, both are non zero. If we also know that $xN, yN$ and $aN$ are integral then we get that $|Nx - Ny| \cdot |Nx + Ny - 2Na| < \frac{MN^2}{|c|}$. Now, since both elements are at least 1, we get that there exists a $\delta > 0$ such that $|x|, |y| < \delta$.
**Corollary.** For any integer $M$, there exists a constant $\delta_M > 0$ such that if $a_{n_1} = a_{n_2}$ and $0 < |n_1 - n_2| \le M$ then $\max(|a_{n_1+1}|, |a_{n_2+1}|) < \delta_M$.
Now, consider some $n$ large enough such that $|a_{n+2}| > \sqrt{\gamma n}$.
$$
a_{n+2} - a_{n+1} = P(a_{n+3}) - P(a_{n+2}) - 1
$$
$$
a_{n+1} - a_n = P(a_{n+2}) - P(a_{n+1}) - 1
$$
$$
a_n - a_{n-1} = P(a_{n+1}) - P(a_n) - 1
$$
Thus, we have
$$
P(a_{n+3}) - P(a_{n+2}) = c(a_{n+3} - a_{n+2})(a_{n+3} + a_{n+2} - 2a).
$$
Observe that at least one of $|a_{n+3} - a_{n+2}|$ and $|a_{n+2} + a_{n+3} - 2a|$ is $\ge \sqrt{\gamma n} - |a|$ as their sum is $\ge 2\sqrt{\gamma n} - 2|a|$. This in fact holds for any $a_i, a_j$ as long as one of them is big.
Also, observe that either the terms are 0 or both at least $\frac{1}{N}$.
Thus, there exists a $\varepsilon > 0$ such that for all large $n$, we have that $|a_{n+2} - a_{n+1}| > \sqrt{\varepsilon n}$ if $a_{n+2} > \sqrt{\gamma n}$ (we can take any $\varepsilon < \frac{c^2\gamma}{N^2}$) unless $a_{n+3} = a_{n+2}$ or $a_{n+3} + a_{n+2} = 2a$ (again, this holds for any $a_i, a_j$ as long as one of them is big). The first case would be a contradiction since then we would need
$$
\sqrt{\gamma n} < |a_{n+2}| = |a_{n+3}| < \delta_1
$$
but we have picked a sufficiently large $n$ so that this does not happen. Thus, $a_{n+2} \neq a_{n+3}$.
All in all, either $|a_{n+2} - a_{n+1}| > \sqrt{\varepsilon n}$ or $a_{n+2} + a_{n+3} = 2a$.
Recall from proof of Claim A2 that $|a_i| = O(\sqrt{n})$ for $i \le n + 5$. Thus for any $i \le n + 4$, if $|a_i - a_{i-1}| > \sqrt{\varepsilon n}$, then
$$
|a_i + a_{i-1} - 2a| < \frac{|a_{i-1} - a_{i-2}| + 1}{|c|\sqrt{\varepsilon n}} = O(1).
$$
Thus either $|a_{n+2} + a_{n+1} - 2a| = O(1)$, which would imply $|a_{n+1}| > \sqrt{\gamma n} - O(1)$, or $a_{n+3} + a_{n+2} = 2a$, which implies $P(a_{n+2}) = P(a_{n+3})$, so $a_{n+1} = a_{n+2} + 1$, so $|a_{n+1}| > \sqrt{\gamma n} - O(1)$ in any case. Thus $|a_{n+1}|$ is also large, so we can repeat the above arguments. Since "largeness" can be cascaded down, we can also assume $|a_{n+3}|, |a_{n+4}|, |a_{n+5}|$ are large, by shifting the indices if needed (there won't be any issues as long as we shift by $O(1)$ indices).
Again we get either $|a_{n+1} + a_n - 2a| = O(1)$, or $a_{n+1} + a_{n+2} = 2a$ and $a_n = a_{n+1} + 1$. Also $|a_n| > \sqrt{\gamma n} - O(1)$.
However, if $a_{n+2} + a_{n+3} = 2a$, then $a_{n+1} = a_{n+2} + 1$, so then we can't have $a_{n+1} + a_{n+2} = 2a$, so $|a_{n+1} + a_n - 2a| = O(1)$, and $2a - a_{n+3} + 1 = a_{n+2} + 1 = a_{n+1}$. This means $|a_{n+3} - a_n| = O(1)$, which implies $|P(a_{n+4}) - P(a_{n+1})| = O(1)$. If $P(a_{n+4}) \neq P(a_{n+1})$, we get a contradiction since $|a_{n+1}|$ is big. Thus equality must hold, so $a_{n+4} = a_{n+1}$ (impossible since $|a_{n+2}| > \delta_3$ is large), or $a_{n+4} + a_{n+1} = 2a$, so $a_{n+4} = a_{n+3} - 1$, so $a_{n+5} = 2a - a_{n+4} = a_{n+1}$ which is impossible since $|a_{n+2}| > \delta_4$ is large.
Therefore $a_i + a_{i+1} \neq 2a$ for any $i$ in the $|a_i|$ large range. So $|a_i + a_{i+1} - 2a| = O(1)$ always (i.e., $a_i$ "flips" around $a$ every time), which implies $|a_{n+2} - a_n| = O(1)$ and $|a_{n+3} - a_{n+1}| = O(1)$ by using triangle inequality on two consecutive such bounds. Thus $|P(a_{n+3}) - P(a_{n+1})| = O(1)$. Similar to the above analysis, we must have $P(a_{n+3}) = P(a_{n+1})$, and $a_{n+3} = a_{n+1}$ is impossible since $|a_{n+2}| > \delta_2$, so we must have $a_{n+3} + a_{n+1} = 2a$, which contradicts $|a_{n+3} - a_{n+1}| = O(1)$. This gives us our final contradiction, and we are done.


**Solution B** First, we consider the case that $d$ is odd. Then, $\exists M, c > 0$, such that if $|x| > M$ and $y$ is some real then if $|a_{i+1}| \ge 2M, |a_i|, |a_{i-1}|, |a_{i-2}|, \dots, |a_1|$, we get
$$
\frac{|P(x) - P(y)|}{|x - y|} \ge c(|x|)^{d-1}.
$$
Thus,
$$
c(a_{i+1}^{d-1})|a_{i+1} - a_i| \le |P(a_{i+1} - P(a_i))| \le |a_i - a_{i-1}| + 1 \le 2|a_{i+1}| + 1
$$
Thus,
$$
|a_{i+1} - a_i| \le \frac{2}{a_{i+1}^{d-2}} + \frac{1}{a_{i+1}^{d-2}}
$$
but as $|a_{i+1}|$ becomes very large, this forces $a_{i+1} = a_i$ since we know that either $|a_k - a_l| = 0$ or $|a_k - a_l| > \frac{1}{n}$ since all $a_i$ are of the form $\frac{k_i}{n}$.
Thus, $a_{i+1} = a_i$ and $a_i$ satisfies the same conditions, thus, $a_i = a_{i-1}$. Thus, $P(a_i) = a_i + i$ and $P(a_i) = a_i + i - 1$ which is a contradiction!

Now, if $d \ge 4$ is even. Observe that there exists $M, c > 0$ such that if $|x| > M$ then $|P(x) - P(x - \frac{1}{n})| \ge cx^{d-1}$.
Now, let $\alpha$ be such that $P(x) - P(\alpha - x) = R(x)$ is of degree at most $d-2$. There is a unique such $\alpha$ as the coefficient of $x^{d-1}$ in $R(x, y) = P(x) - P(y - x)$ is linear in $y$.
Now, there is also a $M', c' > 0$ such that if $x \neq y, |x| > M$, then
$$
|P(x) - P(y)| \geq c' \min(|x - y|, |x + y - \alpha|) \cdot x^{d-1}
$$
Thus, if we have $|a_{i+1}| \geq 10^{100} M' n^{100}$, $|a_i| - M'$, $|a_{i-1}| - 2M'$, $|a_{i-2}| - 3M'$.
$$
\min(|(a_{i+1} - a_i)|, |(a_{i+1} + a_i - \alpha)|) \cdot |a_{i+1}|^{d-1} \leq |P(a_{i+1}) - P(a_i)| \leq |a_i - a_{i-1}| + 1
$$
Thus,
$$
\min(|a_{i+1} - a_i|, |a_{i+1} + a_i - \alpha|) \leq \frac{|a_i - a_{i-1}|}{|a_{i+1}|^{d-1}} + \frac{1}{a_{i+1}^{d-1}} \quad (4)
$$
But then this gets arbitrarily small as $|a_{i+1}|$ gets larger and larger. Again since $a_i$ are of the form $\frac{k_i}{n}$, the LHS is bounded below unless it's 0. Thus, eventually, for all large terms, we have $a_{i+1} - a_i = 0$ or $a_{i+1} + a_i = \alpha$. But then the sequence is not unbounded which is a contradiction!
Now, finally we consider $d=2$.
First, we get that $\min(|a_{i+1} - a_i|, |a_{i+1} + a_i - \alpha|)$ is bounded by some constant $\beta$.
Now, if $|a_i - a_{i-1}| < \beta$ and $|a_{i+1}|$ is large then we get that either $a_{i+1} = a_i$ or $a_{i+1} + a_i = \alpha$. But repeating this in the case that $a_{i+1} = a_i$, tells us $a_{i+2} = a_{i+1}$ which is a contradiction as before.
Thus, if $|a_i - a_{i-1}| < \beta$, then $a_{i+1} + a_i = \alpha$. Now, observe that $R(x)$ is a constant as it is of degree at most 2. So, we have that $P(\alpha - x) + R = P(x)$ where $R$ is a constant.
We have $|P(a_{i+1}) - P(a_i)| = |a_{i+1} - a_i + 1|$ if $a_{i+1} + a_i = \alpha$ but then $P(a_{i+1}) - P(a_i) = R$. Thus, $|\alpha + 1 - 2a_i| = |a_{i+1} - a_i + 1| = R$. Thus, $a_i$ is bounded. Thus, if $a_i$ is large then $a_{i+1} + a_i \neq \alpha$.
Thus, $|a_{i+1} - a_i|$ cannot be $< \beta$ if $a_i$ is large. Thus, we always have $|a_{i+1} + a_i - \alpha| < \beta$ for all large enough $i$. Thus, let $\beta_i = \alpha - a_{i+1} - a_i$.
Now,
$$
-2a_i + 1 - \beta_i + \alpha = a_{i+1} - a_i + 1 = P(a_{i+1}) - P(a_i) = P(\alpha - a_{i+1}) - P(a_i) + R \\ = P(a_i + \beta_i) - P(a_i) + R = P'(a_i)b_i + \frac{P''(a_i)}{2}b_i^2
$$
This fixes $b_i$ as the coefficient of $a_i$ gets fixed. Thus, $a_i + a_{i+1}$ is fixed when $a_i$ is large. That means $a_i = a_{i+2}$ and thus not unbounded. This is a contradiction!

Thus, we are done!

