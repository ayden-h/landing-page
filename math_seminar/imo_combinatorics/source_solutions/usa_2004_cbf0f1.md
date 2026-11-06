# usa_2004_cbf0f1

IMO-TST | United States | 2004 | Team Selection Test | 2

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [usa_2004_cbf0f1](https://mathnet.mit.edu/data_v2/full/united-states/usa_2004_cbf0f1.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: United States
- Title: Mathematical Olympiads
- Year: 2004
- Editors: Feng, Zuming; Loh, Po-Shen
- Publisher: MAA American Mathematics Competitions
- Place: Lincoln, NE
- Series: Problem Book series

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

**First Solution:** The answer is $(n-1)^n - (n-1)$ for part (a) and $(n-1)((n-2)^{n-1} - 1)$ for part (b).

a. Observe that the number of good sequences is clearly the same for any choice of $a_0$. For fixed $a_0$, call the condition $a_i - a_{i-1} \not\equiv i \pmod n$ *condition (i)*. Now let $S_i$ be the set of sequences $A = \{a_i\}_{i=1}^n, a_i \in \{1, 2, \dots, n\}$ such that $A$ satisfies conditions (1), (2), \dots, $(n-i)$ and fails to satisfy conditions $(n-i+2)$, $(n-i+3)$, \dots, $(n)$. Note that there is no constraint on whether or not $A$ satisfies condition $(n-i+1)$. Finally, let $F$ be the set of sequences that fails all conditions (1), (2), \dots, $(n)$. Then we claim that the number of good sequences starting with $a_0$ is
$$
m = |S_1| - |S_2| + |S_3| - \dots + |S_n| - |F|.
$$
Consider the following table, representing the conditions on sequences in $S_i$.
$$
\begin{array}{c|ccccccc}
S_1 & (1) & (2) & (3) & \dots & (n-2) & (n-1) & \\
\hline
S_2 & (1) & (2) & (3) & \dots & (n-2) & \overline{(n)} & \\
\hline
S_3 & (1) & (2) & (3) & \dots & \overline{(n-1)} & \overline{(n)} & \\
\hline
\vdots & \vdots & \vdots & \vdots & \dots & \vdots & \vdots & \vdots \\
\hline
S_n & \overline{(2)} & \overline{(3)} & \dots & \overline{(n-2)} & \overline{(n-1)} & \overline{(n)} & \\
\hline
F & (1) & (2) & (3) & \dots & \overline{(n-2)} & \overline{(n-1)} & \overline{(n)}
\end{array}
$$
Conditions that appear as $(j)$ in row $i$ are satisfied by sequences in $S_i$, and those that appear as $\overline{(j)}$ are failed.

Now take any sequence $A$. If $A$ is good, then $A$ is counted exactly once in $|S_1|$ and is not counted anywhere else. Otherwise, if $A$ is not good, let $(i)$ be the first condition that $A$ fails. If $i > 1$, then $A$ belongs to exactly the sets $S_{n-1}, S_{n-2}$. As one of $|S_{n-1}|, |S_{n-2}|$ is added and one is subtracted, $A$ has no net contribution to $m$. Finally, if $i = 1$, then $A$ belongs to $S_n$ and $F$, so again $A$ does not contribute to $m$. Therefore, $m$ is indeed the number of good sequences.

We are left with computing the sizes of the $S_i$'s and $F$. This is easy, as the failure of the final $i-1$ conditions determines the terms $a_{n-1}, a_{n-2}, \dots, a_{n-i+1}$, whereas there are just $n-1$ ways to satisfy each of the conditions (1), (2), \dots, $(n-i)$, producing $(n-1)^{n-i}$ subsequences $a_0, a_1, \dots, a_{n-i}$. As there is no constraint on $a_{n-i+1} - a_{n-i}$, we have found all sequences in $S_i$. Hence, $|S_i| = (n-1)^{n-i}$. As for $F$, there is clearly exactly one way to fail every single condition, because $1+2+\dots+(n-1) = \frac{n(n-1)}{2}$ is divisible by $n$. Therefore, $|S_n| - F = 0$ and
$$
\begin{align*}
m &= |S_1| - |S_2| + \dots - |S_{n-1}| \\
&= (n-1)^{n-1} - (n-1)^{n-2} + \dots - (n-1) \\
&= \frac{(n-1)^n - (n-1)}{n}.
\end{align*}
$$
As there were originally $n$ choices for $a_0$, multiplying by $n$ gives the desired answer.

b. We can use the same argument as in part (a), but we must recompute the values of $|S_i|$ and $|F|$. Note that for $1 \le i \le n-1$, there are exactly two ways to fail condition (i) (because $n$ is odd) while condition (n) is degenerate and reduces to the single restriction $a_n - a_{n-1} \not\equiv 0 \pmod{n}$. Hence, we have
$$
|S_1| = (n-2)^{n-1} \quad \text{and} \quad |S_i| = 2^{i-2}(n-2)^{n-i},
$$
for $2 \le i \le n$. Finding $|F|$ is trickier in this case, however. Considering the differences $b_i = a_i - a_{i-1}$, $i = 1, 2, \dots, n$, we wish to count the number of choices of $\{b_i\}_{i=1}^n$ such that
$$
b_1 + b_2 + \dots + b_n \equiv 0 \pmod{n},
$$
where $b_i = i$ or $2i \pmod{n}$ for each $i$. Note that because of the degenerate condition $(n)$, $b_n \equiv 0 \pmod{n}$ is forced; hence, we are actually looking at $2^{n-1}$ sums $b_1 + b_2 + \dots + b_{n-1}$ rather than $2^n$. Now, as $n \mid [1 + 2 + \dots + (n-1)] = \frac{n(n-1)}{2}$, we can equivalently consider sums of terms $c_i = b_i - i$. That is, we wish to find the number of choices of $c_1, c_2, \dots, c_{n-1}$ such that
$$
c_1 + c_2 + \dots + c_{n-1} \equiv 0 \pmod{n},
$$
where $c_i = 0$ or $i$ for each $i$. We now introduce an extra term $c_n$ that can be either 0 or $n$. The only effect of this extra term is to double the number of choices of $\{c_i\}_{i=1}^n$ compared to the number of choices of $\{c_i\}_{i=1}^{n-1}$. That is, letting
$$
F' = \{(c_1, c_2, \dots, c_n) \mid \begin{aligned}[t] & c_i = 0 \text{ or } i, \\ & c_1 + c_2 + \dots + c_n \equiv 0 \pmod{n} \end{aligned}\},
$$
we have $|F| = \frac{1}{2}|F'|$.

Observe that we can identify choices $(c_1, c_2, \dots, c_n)$ with subsets of $T = \{1, 2, \dots, n\}$; the elements of $F'$ are then simply the subsets of $T$ that have sum divisible by $n$. The empty set and the set $T$ are two sets that clearly satisfy this property. All remaining subsets $U \subset T$ have from 1 to $n-1$ elements. Write $U+k$ for the set $\{x+k \mid x \in U\}$ (taken mod $n$); this is the rotation of $U$ by $k$ shifts to the right. Then because $n$ is prime and $0 < |U| < n$, the subsets $U, U+1, U+2, \dots, U+(n-1)$ form an equivalence class of exactly $n$ distinct subsets. Furthermore, the sums of the elements in $U$ and $U + k$ differ by $k|U|(\text{mod } n)$, so exactly one element of each class has sum divisible by $n$. It follows that
$$
|F'| = 2 + \frac{2^n - 2}{n}, \quad |F| = \frac{1}{2}|F'| = \frac{2^{n-1} + n - 1}{n}.
$$
Therefore,
$$
\begin{align*}
m &= |S_1| - |S_2| + |S_3| - \dots + |S_n| - |F| \\
&= (n-2)^{n-1} - (n-2)^{n-2} + 2(n-2)^{n-3} \\
&\quad - 2^2(n-2)^{n-4} + \dots + 2^{n-2} - \frac{2^{n-1} + n-1}{n} \\
&= (n-2)^{n-1} - \frac{(n-2)^{n-1} - 2^{n-1}}{n} - \frac{2^{n-1} + n-1}{n} \\
&= \frac{(n-1)(n-2)^{n-1} - (n-1)}{n}.
\end{align*}
$$
As before, multiplying by $n$ gives the desired answer.


**Second Solution:** The answer is $(n-1)^n - (n-1)$ for part (a) and $(n-1)((n-2)^{n-1} - 1)$ for part (b). Observe that the number of good sequences is clearly the same for any choice of $a_0$. Fixing $a_0$, we represent the choices for the differences $a_i - a_{i-1} \pmod n$ with the generating function
$$
g_i(x) = 1 + x + x^2 + \dots + x^{i-1} + x^{i+1} + \dots + x^{n-1} = p(x) - x^i,
$$
where $p(x) = 1 + x + x^2 + \cdots + x^{n-1}$. Then the generating function representing all the possibilities for $a_1 - a_0, a_2 - a_1, \ldots, a_{n-1} - a_{n-2}$ is
$$
g(x) = \prod_{i=1}^{n-1} g_i(x) = \prod_{i=1}^{n-1} (p(x) - x^i).
$$
The condition that $a_0 - a_{n-1} \not\equiv 0 \pmod{n}$ means that we wish to sum the coefficients of the $x^k$ terms of $g(x)$ for $n \not\mid k$.

Now the sum of all the coefficients is simply $g(1) = (n-1)^{n-1}$. The sum of the coefficients of the $x^k$ terms for $n \mid k$ can be obtained by taking
$$
\frac{1}{n} \sum_{j=0}^{n-1} g(\epsilon^j),
$$
where $\epsilon = e^{2\pi i/n}$ is a primitive $n^{\text{th}}$ root of unity. As we noted above, $g(1) = (n-1)^{n-1}$. For $n > j > 0$, note that $p(\epsilon^j) = 0$, so
$$
g(\epsilon^j) = \prod_{k=1}^{n-1} -\epsilon^{kj} = (-1)^{n-1} \epsilon^{n(n-1)/2} j = 1,
$$
as $n$ is odd. Therefore, the sum of the coefficients of the terms with powers not dividing $n$ is
$$
(n-1)^{n-1} - \frac{1}{n}((n-1)^{n-1} + (n-1)) = \frac{1}{n}((n-1)^n - (n-1)).
$$
Remembering that we had $n$ choices of $a_0$ to begin with, we obtain $(n-1)^n - (n-1)$ as the answer to part (a).

For part (b), we change our generating functions to
$$
h_i(x) = p(x) - (x^i + x^{2i}), \quad h(x) = \prod_{i=1}^{n-1} h_i(x).
$$
Note that for $1 \le i \le n-1$, the terms $x^i$ and $x^{2i}$ both appear because $i \ne 2i \pmod n$ as $n$ is odd. For the final condition, however, $n \equiv 2n \equiv 0 \pmod n$, so we are still counting those terms—and only those terms—with powers not divisible by $n$. Hence, using the same method as before, we have $h(1) = (n-2)^{n-1}$,
$$
h(\epsilon^j) = \prod_{k=1}^{n-1} -\epsilon^{kj}(1 + \epsilon^{kj}) = \prod_{k=1}^{n-1} (1 + \epsilon^k),
$$
for $1 \le j \le n-1$, as $n$ is prime. Now, $1+\epsilon^i$, $i=0,1,\dots,n-1$, are all of the roots of the polynomial $(x-1)^n-1$. Therefore, their product is $(-1)^n = -1$ times the constant coefficient of the polynomial, $-2$. Hence, the product of the roots not including $i=0$ (in which case $1+\epsilon^0 = 2$) is 1. Therefore, $h(\epsilon^j) = 1$.

It follows that the number of sequences for a fixed $a_0$ is
$$
(n-2)^{n-1} - \frac{1}{n}((n-2)^{n-1} + (n-1)) = \frac{1}{n}((n-1)((n-2)^{n-1} - 1)),
$$
so the answer to part (b) is $(n-1)((n-2)^{n-1} - 1)$.

