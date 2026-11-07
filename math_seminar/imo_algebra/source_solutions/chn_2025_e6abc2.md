# chn_2025_e6abc2

IMO-TST | China | 2025 | Test 4 · Day 2 | Problem 12.

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [chn_2025_e6abc2](https://mathnet.mit.edu/data_v2/full/china/chn_2025_e6abc2.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: China
- Title: 2025 International Mathematical Olympiad China National Team Selection Test
- Year: 2025
- Organization: International Mathematical Olympiad China
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $\alpha = 3 + 2\sqrt{2}$. All functions satisfying the given conditions are of the form $f(n) = \frac{1}{2}(\alpha^{2n} + \alpha^{-2n})$ for some fixed positive integer $t$.

First, we verify that such $f(n)$ satisfies $(\star)$. The left-hand side of $(\star)$ becomes:
$$
2 \cdot \frac{\alpha^{2tm} + \alpha^{-2tm}}{2} \cdot \frac{\alpha^{2tn} + \alpha^{-2tn}}{2} - \frac{\alpha^{2t(m-n)} + \alpha^{-2t(m-n)}}{2} - 1 \\
= \frac{\alpha^{2t(m+n)} + \alpha^{-2t(m+n)}}{2} - 1 = \left( \frac{\alpha^{t(m+n)} - \alpha^{-t(m+n)}}{\sqrt{2}} \right)^2 .
$$
Note that $\frac{\alpha^{t(m+n)} - \alpha^{-t(m+n)}}{\sqrt{2}} = \frac{(3+2\sqrt{2})^{t(m+n)} - (3-2\sqrt{2})^{t(m+n)}}{\sqrt{2}}$ is an integer, so the above expression is indeed a perfect square.

We now show that these are the only solutions to the functional equation $(\star)$. Let $A_{m,n}$ be the non-negative integer such that:
$$
2f(m)f(n) - f(m - n) - 1 = A_{m,n}^2. \qquad (\star\star)
$$

**Step 1:** All $f(n)$ have the same sign. This follows by setting $n = 0$ in $(\star\star)$, which gives $(2f(0) - 1)f(m) > 0$. Thus, all $f(n)$ have the same sign as $2f(0) - 1$.

**Step 2:** $f(n)$ is an even function. For a fixed $t \in \mathbb{Z}^+$, let $M_t = \max\{|f(t)|, |f(-t)|\}$. Since $f$ is unbounded, there exists $N$ such that $|f(N + t)| > (M_t + 1)^2$. Substituting $m = N + t, n = N$ and $m = N, n = N + t$ into $(\star\star)$ yields:
$$
2f(N + t)f(N) - f(t) - 1 = A_{N,N+t}^2, \quad 2f(N + t)f(N) - f(-t) - 1 = A_{N+t,N}^2.
$$
This implies $A_{N,N+t}^2 > 2(M_t+1)^2 - M_t - 1 > M_t^2$, so $A_{N,N+t} > M_t$; similarly, $A_{N+t,N} > M_t$. Subtracting these equations gives:
$$
f(-t) - f(t) = (A_{N,N+t} - A_{N+t,N})(A_{N,N+t} + A_{N+t,N}).
$$
The left-hand side satisfies $|f(-t) - f(t)| < 2M_t$, while $A_{N,N+t} + A_{N+t,N} > 2M_t$. Analyzing the magnitudes shows that $A_{N,N+t} = A_{N+t,N}$, so $f(t) = f(-t)$, proving $f$ is even.

**Step 3:** Determine the general form of $f(n)$. Setting $m = n$ in $(\star\star)$ gives:
$$
2f(n)^2 - f(0) - 1 = A_{n,n}^2 \quad \text{ i.e., } \quad A_{n,n}^2 - 2f(n)^2 = -f(0) - 1. \qquad (5)
$$
Thus, $(A_{n,n}, f(n))$ is a solution to the generalized Pell equation:
$$
X^2 - 2Y^2 = -f(0) - 1. \qquad (6)
$$
We use the theory of solutions to generalized Pell equations. Let $\mathbb{Z}[\sqrt{2}]$ be the ring of numbers $Z = X + \sqrt{2}Y$ with $X, Y \in \mathbb{Z}$. The conjugate of $Z$ is $Z' = X - \sqrt{2}Y$, and $(Z_1Z_2)' = Z'_1Z'_2$. For $\alpha = 3+2\sqrt{2}$, we have $\alpha' = \alpha^{-1}$. Solving (6) is equivalent to solving $ZZ' = -f(0) - 1$ in $\mathbb{Z}[\sqrt{2}]$. If $Z$ is a solution, then all $Z\alpha^{2s}$ ($s \in \mathbb{Z}$) are also solutions.

**Lemma:** There exist finitely many fundamental solutions $Z_i = X_i + \sqrt{2}Y_i \in \mathbb{Z}[\sqrt{2}]$ ($i = 1, \dots, t$) to (6) such that for any solution $(X, Y)$, there exists $i \in \{1, \dots, t\}$ and $s \in \mathbb{Z}_{\ge 0}$ with $X + \sqrt{2}Y = Z_i\alpha^{2s}$.

**Proof of Lemma:** Consider the lattice $L := \{(a + \sqrt{2}b, a - \sqrt{2}b) \mid a, b \in \mathbb{Z}\}$. Solutions $(X, Y)$ to (6) correspond to points $(x, y) = (X + \sqrt{2}Y, X - \sqrt{2}Y)$ on the hyperbola $xy = -f(0) - 1$. Multiplying $X + \sqrt{2}Y$ by $\alpha^2$ or $\alpha^{-2}$ generates new solutions, equivalent to moving $(x, y)$ to $(\alpha^2x, \alpha^{-2}y)$ or $(\alpha^{-2}x, \alpha^2y)$ on the hyperbola. By these transformations, any solution can be mapped to a region where $|x| \le \alpha\sqrt{|f(0) + 1|}$ and $|y| \le \alpha\sqrt{|f(0) + 1|}$, corresponding to finitely many lattice points $(X_i + \sqrt{2}Y_i, X_i - \sqrt{2}Y_i)$ ($i = 1, \dots, t$). Thus, any solution can be written as $(X_i + \sqrt{2}Y_i)\alpha^{2s}$. $\square$

Fix the fundamental solutions $Z_i = X_i + \sqrt{2}Y_i$ ($i = 1, \dots, t$) from the lemma, with $Z_iZ'_i = -f(0) - 1$. We may assume no two $Z_i$ differ by a power of $\alpha^2$. For each $n \in \mathbb{Z}$, there exist unique $i_n \in \{1, \dots, t\}$ and $s_n \in \mathbb{Z}$ such that:
$$
f(n) = \frac{Z_{i_n}\alpha^{2s_n} - Z'_{i_n}\alpha^{-2s_n}}{2\sqrt{2}}. \qquad (7)
$$
Let $N = \max_i\{|Z_i|, |Z'_i|, |Z_i|^{-1}, |Z'_i|^{-1}\}$. From (7), we have the estimate:
$$
N^{-1}\alpha^{2|s_n|} - N \le |f(n)| \le N\alpha^{2|s_n|} + N. \qquad (8)
$$

**Step 4:** For positive integers $m > n$, we have the growth estimate:
$$
\left||s_{m+n} - |s_m|\right| < |s_n| + 2 \log_{\alpha} N + 2. \qquad (9)
$$
This follows from substituting $-n$ for $n$ in $(\star\star)$, yielding:
$$
|f(m+n)| < 2f(m)f(-n) = 2f(m)f(n). \qquad (10)
$$
Combining with (8) gives:
$$
N^{-1}\alpha^{2|s_{m+n}|} - N \le 2(N\alpha^{2|s_n|} + N)(N\alpha^{2|s_m|} + N).
$$
Simplifying, we obtain:
$$
N^{-1} \cdot \alpha^{2|s_{m+n}|} \le 2N^2 \cdot ((\alpha^{2|s_n|} + 1)(\alpha^{2|s_m|} + 1) + 1) \le N^2 \cdot \alpha^{2|s_n|+2|s_m|+3}
$$
which implies $|s_{m+n}| < |s_n| + |s_m| + 2 \log_{\alpha} N + 2$.
Similarly, substituting $m+n$ for $m$ in $(\star\star)$ gives:
$$
2f(m+n)f(n) > |f(m)|, \qquad (11)
$$
leading to $|s_{m+n}| + |s_n| + 2 \log_{\alpha} N + 2 > |s_m|$. Combining these inequalities proves (9).

**Step 5:** Prove that $f(0) = 1$.
First, let's explain the basic idea. Suppose for indices $m, n$ we have $Z_{i_m} = Z_{i_n}$ and $s_n$ has the same sign as $s_m$. Substituting the expressions for $f(m)$ and $f(n)$ from (7) into $(\star\star)$, we obtain:
$$
\begin{align}
B_{m,n}^2 &= 2f(m)f(n) - f(m-n) - 1 \\
&= \frac{(Z_{i_m} \alpha^{2s_m} - Z'_{i_m} \alpha^{-2s_m})(Z_{i_n} \alpha^{2s_n} - Z'_{i_n} \alpha^{-2s_n})}{4} - \frac{Z_{i_{m-n}} \alpha^{2s_{m-n}} - Z'_{i_{m-n}} \alpha^{-2s_{m-n}}}{2\sqrt{2}} - 1 \\
&= \left( \frac{Z_{i_m} \alpha^{s_m+s_n} + Z'_{i_m} \alpha^{-s_m-s_n}}{2} \right)^2 - \frac{Z_{i_m} Z'_{i_m} (\alpha^{s_m-s_n} + \alpha^{s_n-s_m})^2}{4} \\
&\quad - \frac{(Z_{i_{m-n}} \alpha^{2s_{m-n}} - Z'_{i_{m-n}} \alpha^{-2s_{m-n}})}{2\sqrt{2}} - 1 \\
&= \left( \frac{Z_{i_m} \alpha^{s_m+s_n} + Z'_{i_m} \alpha^{-s_m-s_n}}{2} \right)^2 + (f(0)+1) \frac{(\alpha^{s_m-s_n} + \alpha^{s_n-s_m})^2}{4} \\
&\quad - \frac{(Z_{i_{m-n}} \alpha^{2s_{m-n}} - Z'_{i_{m-n}} \alpha^{-2s_{m-n}})}{2\sqrt{2}} - 1. \tag{12}
\end{align}
$$
Note that $\frac{1}{2}(Z_{i_m} \alpha^{s_m+s_n} + Z'_{i_m} \alpha^{-s_m-s_n})$ is an integer greater than $(2N)^{-1} \alpha^{|s_m+s_n|-1} - N$.
Therefore, if $s_m$ and $s_n$ are very close and both have large absolute values, all terms except this squared term sum to zero.
Now we use this property specifically to show $f(0) = 1$. Assume by contradiction that $f(0) \neq 1$. First, we show that for any $i \in \{1, \dots, t\}$, the sets $\{\frac{1}{2\sqrt{2}}Z_i\alpha^{2s} \mid s \in \mathbb{Z}_{\ge 0}\} \cup \{\frac{1}{2\sqrt{2}}Z'_i\alpha^{2s} \mid s \in \mathbb{Z}_{\ge 0}\}$ and $\{\frac{1}{4}(f(0)+1)\alpha^{2s}\}$ have no common elements. This is because the product of these numbers with their conjugates differs:
$$
\frac{1}{2\sqrt{2}} Z_i \alpha^{2s} \cdot \frac{1}{-2\sqrt{2}} Z'_i \alpha^{-2s} = \frac{f(0) + 1}{8} \neq \frac{1}{16} (f(0) + 1)^2,
$$
(since $f(0) \neq 1$). Thus there exists an integer $M > 2 \log_{\alpha}(N) + 2$ such that all numbers of the form $\frac{f(0)+1}{4}\alpha^{2s}$ and $\frac{Z_i}{2\sqrt{2}}\alpha^{2s}$ or $\frac{Z'_i}{2\sqrt{2}}\alpha^{2s}$ (for $|s| \ge M$) are pairwise separated by more than $|f(0) - 1| + N^2$.
Since $f$ is unbounded, there exist $n_1 < \dots < n_{2t+1}$ satisfying:
$$
|s_{n_1}| > 2M, \quad |s_{n_{i+1}}| > 2|s_{n_i}| \quad (i = 1, \dots, 2t).
$$
Choose $L$ such that $|s_L| > 5 \cdot 2^{2t+1}M$. Consider:
$$
i_{L+n_1}, i_{L+n_2}, \dots, i_{L+n_{2t+1}} \in \{1, \dots, t\}
$$
and the signs of $s_{L+n_j}$. By the pigeonhole principle, there must exist $x > y \ge 1$ such that $i_{L+n_x} = i_{L+n_y} = i$ and $s_{L+n_x}$ has the same sign as $s_{L+n_y}$.
From inequality (9), we estimate:
$$
|s_{(L+n_x)-(L+n_y)}| = |s_{n_x-n_y}| > |s_{n_x} - s_{n_y}| - (2 \log_{\alpha}(N) + 2) > M.
$$
$$
|s_{L+n_x}| > |s_L| - |s_{n_x}| - 2 \log_{\alpha}(N) + 2 > 4 \cdot 2^{t+1}M; \quad |s_{L+n_y}| > 4 \cdot 2^{t+1}M.
$$
Returning to our earlier situation, set $m = L + n_x$, $n = L + n_y$, and observe that:
$$
\left| \frac{Z_i \alpha^{s_m + s_n} + Z'_i \alpha^{-s_m - s_n}}{2} \right| > N^{-1} \alpha^{4 \cdot 2^{t+1} M} - N
$$
is much larger than the square of the remaining terms. Therefore, we must have:
$$
(f(0) + 1) \frac{(\alpha^{s_m - s_n} + \alpha^{s_n - s_m})^2}{4} = \frac{(Z_{i_{m-n}} \alpha^{2s_m - n} - Z'_{i_{m-n}} \alpha^{-2s_m - n})}{2\sqrt{2}} + 1.
$$
But by the definition of $M$, this equality cannot hold. Contradiction!

**Step 6:** Complete the proof. With $f(0) = 1$, (5) simplifies to:
$$
2f(n)^2 - 2 = A_{n,n}^2.
$$
Thus, $A_{n,n}$ is even, and we rewrite the equation as:
$$
f(n)^2 - 2 \left( \frac{A_{n,n}}{2} \right)^2 = 1.
$$
The solutions to this standard Pell equation are:
$$
f(n) = \frac{\alpha^{t_n} + \alpha^{-t_n}}{2}, \quad t_n \in \mathbb{Z}_{\ge 0}.
$$
Substituting $n = 0$ into (★) gives:
$$
A_{m,0}^2 = 2f(m)f(0) - f(m) - 1 = f(m) - 1 = \left( \frac{(\sqrt{2} + 1)^{t_m} - (\sqrt{2} - 1)^{t_m}}{\sqrt{2}} \right)^2,
$$
implying $t_n$ must be even. Let $t_n = 2s_n$.
Substituting into (10) and (11), we obtain for $m > n$:
$$
\frac{1}{2}(\alpha^{2s_m} + \alpha^{-2s_m})(\alpha^{2s_n} + \alpha^{-2s_n}) > \frac{1}{2}(\alpha^{2s_{m+n}} + \alpha^{-2s_{m+n}}),
$$
$$
\frac{1}{2}(\alpha^{2s_{m+n}} + \alpha^{-2s_{m+n}})(\alpha^{2s_n} + \alpha^{-2s_n}) > \frac{1}{2}(\alpha^{2s_m} + \alpha^{-2s_m}),
$$
which implies:
$$
s_m + s_n \ge s_{m+n} \quad \text{and} \quad s_{m+n} + s_n \ge s_m. \qquad (13)
$$
The following shows that for any $\ell \in \mathbb{N}$, we have $s_\ell = \ell s_1$. Fix $\ell$, and let $D := \max\{2, s_1, \dots, s_\ell\}$.

Consider any positive integer $N > \ell$ satisfying $s_N > 5D$. From the given conditions, for $i = -1, 0, \dots, \ell - 1$, we have $s_{N+i} > 4D$. For $i = 0, \dots, \ell - 1$, taking $m = N + i$ and $n = N - 1$ in (12) yields:
$$
\begin{aligned}
B_{N+i,N-1}^2 &= \frac{1}{2}(\alpha^{2s_{N+i}} + \alpha^{-2s_{N+i}})(\alpha^{2s_{N-1}} + \alpha^{-2s_{N-1}}) - \frac{1}{2}(\alpha^{2s_{i+1}} - \alpha^{-2s_{i+1}}) - 1 \\
&= \left( \frac{\alpha^{s_{N+i}+s_{N-1}} - \alpha^{-s_{N+i}-s_{N-1}}}{\sqrt{2}} \right)^2 \\
&\quad + \frac{(\alpha^{2s_{N+\ell}-2s_{N-1}} + \alpha^{2s_{N-1}-2s_{N+\ell}}) - (\alpha^{2s_{i+1}} + \alpha^{-2s_{i+1}})}{2}
\end{aligned}
$$
Since $\frac{\alpha^{s_{N+i}+s_{N-1}}-\alpha^{-s_{N+i}+s_{N-1}}}{\sqrt{2}}$ is an integer greater than $\alpha^{6D-1}$, while the remaining terms are less than $\alpha^{2D+1}$, it must hold that:
$$
\alpha^{2s_{N+\ell}-2s_{N-1}} + \alpha^{2s_{N-1}-2s_{N+\ell}} = \alpha^{2s_{i+1}} + \alpha^{-2s_{i+1}}.
$$
This implies $|s_{N+i} - s_{N-1}| = s_{i+1}$.
Since $f$ is unbounded, choose $N > \ell$ such that $s_N > 6D$ and $s_N > s_{N-1}$. From the above discussion, we have:
$$
|s_{N+1} - s_N| = s_1, \quad s_N - s_{N-1} = s_1, \quad |s_{N+1} - s_{N-1}| = s_2,
$$
so either $s_2 = 0$ or $s_2 = 2s_1$. If $s_2 = 0$, we can use $s_N > 6D$ and (13) to inductively prove that $s_{N+u+2} = s_{N+u}$ for all $u \in \mathbb{N}$. This contradicts the unboundedness of $f$.

Therefore, $s_2 = 2s_1$, which implies $s_{N+1} = s_{N-1} + 2s_1$. Next, we examine the conditions that $s_{N+2}$ must satisfy:
$$
|s_{N+2} - s_N| = s_2 = 2s_1, \quad |s_{N+2} - s_{N+1}| = s_1.
$$
Thus $s_{N+2} = s_N + 2s_1 = s_{N-1} + 3s_1$, which gives $s_3 = |s_{N+2} - s_{N-1}| = 3s_1$. Continuing this recursion, we obtain $s_\ell = \ell s_1$. This proves that all solutions $f$ satisfying the functional equation are of the form:
$$
f(n) = \frac{1}{2}(\alpha^{2ns_1} + \alpha^{-2ns_1}).
$$
