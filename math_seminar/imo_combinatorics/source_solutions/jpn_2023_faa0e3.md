# jpn_2023_faa0e3

JMO | Japan | 2023 | Final Round | 5

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2023_faa0e3](https://mathnet.mit.edu/data_v2/full/japan/jpn_2023_faa0e3.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: Japan Mathematical Olympiad
- Subtitle: The 33rd Japanese Mathematical Olympiad: The First Round • The Final Round
- Year: 2023
- Organization: The Mathematical Olympiad Foundation of Japan
- Publisher: The Mathematical Olympiad Foundation of Japan
- Edition: 33rd
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We denote
$$
X_{\max}(f,g) = \sum_{k=1}^{3000} \max\{f(f(k)), f(g(k)), g(f(k)), g(g(k))\},
$$
$$
X_{\min}(f,g) = \sum_{k=1}^{3000} \min\{f(f(k)), f(g(k)), g(f(k)), g(g(k))\},
$$
and $X(f,g) = X_{\max}(f,g) - X_{\min}(f,g)$. Moreover, for a finite set $T$, we denote the number of its elements by $|T|$.

First, we will prove that the answer is at most $6000000$. When the bijection $f$ is the identity map, for any bijection $g$ on $S$, we have $f \circ g = g \circ f$. For any $a \in S$, since the function $f \circ f$ is bijective, the equation $f(f(x)) = a$ for $x$ has at most one solution. The same is true for the bijections $f \circ g = g \circ f$ and $g \circ g$. Therefore, the equation $\max\{f(f(x)), f(g(x)), g(f(x)), g(g(x))\} = a$ for $x$ has at most three solutions. Hence we have
$$
X_{\max}(f,g) \le 3 \times 3000 + 3 \times 2999 + \dots + 3 \times 2001 = \sum_{k=2001}^{3000} 3k,
$$
and similarly,
$$
X_{\min}(f,g) \ge 3 \times 1 + 3 \times 2 + \dots + 3 \times 1000 = \sum_{k=1}^{1000} 3k.
$$
Therefore,
$$
X(f,g) \le \sum_{k=2001}^{3000} 3k - \sum_{k=1}^{1000} 3k = 6000000.
$$
Hence, the answer is at most $6000000$.

In the following, we will prove that $X = 6000000$ satisfies the condition. We denote
$$
S_1 = \{1, 2, \dots, 1000\}, \quad S_2 = \{1001, 1002, \dots, 2000\}, \quad S_3 = \{2001, 2002, \dots, 3000\}.
$$
Additionally, for $a, b \in \{1, 2, 3\}$, let $S_{a,b} = \{x \in S_a \mid f(x) \in S_b\}$ and $n_{a,b} = |S_{a,b}|$. Now, for any $x \in S$, there exists exactly one pair $(a, b) \in \{1, 2, 3\}^2$ such that $x \in S_{a,b}$.

**Lemma.** For any bijection $f$ on $S$, there exists a partition $\{Z_1, Z_2, \dots, Z_{1000}\}$ of $S$ satisfying the following condition:
For any $1 \le i \le 1000$, $|Z_i| = 3$ and when $a_1, a_2, a_3$ denote the elements of $Z_i$ in ascending order, we have $a_1 \in S_1, a_2 \in S_2$ and $a_3 \in S_3$. In addition, exactly one element of $\{f(a_1), f(a_2), f(a_3)\}$ belongs to $S_b$ for every $b \in \{1, 2, 3\}$.

**Proof.** Assume that there exists a tuple $(A_1, B_1, A_2, B_2, A_3, B_3)$ of non-negative integers satisfying the equations:
$$
\begin{align*}
A_1 + B_1 &= n_{1,1}, & A_2 + B_2 &= n_{1,2}, & A_3 + B_3 &= n_{1,3}, \\
A_3 + B_2 &= n_{2,1}, & A_1 + B_3 &= n_{2,2}, & A_2 + B_1 &= n_{2,3}, & (*) \\
A_2 + B_3 &= n_{3,1}, & A_3 + B_1 &= n_{3,2}, & A_1 + B_2 &= n_{3,3}.
\end{align*}
$$
Then, we have a partition $\{Z_1, \dots, Z_{1000}\}$ of $S$ which satisfies the condition in the lemma and the following condition:
For each $Z_i = \{a_1, a_2, a_3\}$ with $a_1 < a_2 < a_3$, define a permutation $\sigma_i$ of $\{1, 2, 3\}$ such that $a_k \in S_{k, \sigma_i(k)}$ for $k = 1, 2, 3$. Then the number of $Z_i$ such that $(\sigma_i(1), \sigma_i(2), \sigma_i(3))$ is equal to $(1, 2, 3)$, $(1, 3, 2)$, $(2, 3, 1)$, $(2, 1, 3)$, $(3, 1, 2)$, and $(3, 2, 1)$ is equal to $A_1, B_1, A_2, B_2, A_3$ and $B_3$, respectively.
Hence it is sufficient to prove that a tuple $(A_1, B_1, A_2, B_2, A_3, B_3)$ satisfying the equations $(*)$ exists.

Without loss of generality, we can assume that $n_{1,1}$ is the smallest among nine integers $n_{a,b}$ ($a, b \in \{1, 2, 3\}$). Setting
$$
(A_1, B_1, A_2, B_2, A_3, B_3) = (n_{1,1}, 0, n_{2,3}, n_{3,3} - n_{1,1}, n_{3,2}, n_{2,2} - n_{1,1}),
$$
this is a tuple of non-negative integers by the minimality of $n_{1,1}$, and satisfies the first, fifth, sixth, eighth, and ninth equations in $(*)$. Furthermore, for any $a \in \{1, 2, 3\}$, we have
$$
\begin{align*}
n_{a,1} + n_{a,2} + n_{a,3} &= |S_a| = 1000, \\
n_{1,a} + n_{2,a} + n_{3,a} &= |\{x \in S \mid f(x) \in S_a\}| = 1000.
\end{align*}
$$
Thus, we find that the tuple satisfies the second, third, fourth, and seventh equations in $(*)$:
$$
A_2 + B_2 = n_{2,3} + n_{3,3} - n_{1,1} = (n_{1,3} + n_{2,3} + n_{3,3}) - (n_{1,1} + n_{1,2} + n_{1,3}) + n_{1,2} = n_{1,2},
$$
$$
A_3 + B_3 = n_{3,2} + n_{2,2} - n_{1,1} = (n_{1,2} + n_{2,2} + n_{3,2}) - (n_{1,1} + n_{1,2} + n_{1,3}) + n_{1,3} = n_{1,3},
$$
$$
A_3 + B_2 = n_{3,2} + n_{3,3} - n_{1,1} = (n_{3,1} + n_{3,2} + n_{3,3}) - (n_{1,1} + n_{2,1} + n_{3,1}) + n_{2,1} = n_{2,1},
$$
$$
A_2 + B_3 = n_{2,3} + n_{2,2} - n_{1,1} = (n_{2,1} + n_{2,2} + n_{2,3}) - (n_{1,1} + n_{2,1} + n_{3,1}) + n_{3,1} = n_{3,1},
$$
which completes the proof. ■

Let us consider $Z_j = \{a_1, a_2, a_3\}$ with $a_1 < a_2 < a_3$. Then $a_1 \in S_1$, $a_2 \in S_2$ and $a_3 \in S_3$. For each $i \in \{1, 2, 3\}$, we define $k_i$ by $f(k_i) = a_i$. Since $g(k_i) = h(f(k_i)) = h(a_i) = a_{i+1}$, we obtain
$$
\begin{aligned} \max\{f(f(k_i)), f(g(k_i)), g(f(k_i)), g(g(k_i))\} &= \max\{f(a_i), f(a_{i+1}), g(a_i), g(a_{i+1})\} \\ &= \max\{f(a_i), f(a_{i+1}), h(f(a_i)), h(f(a_{i+1}))\}, \end{aligned}
$$
where $a_4 = a_1$. Let us define $F_1, F_2, F_3$ by $\{f(a_1), f(a_2), f(a_3)\} = \{F_1, F_2, F_3\}$ and $F_1 < F_2 < F_3$. By the condition of the lemma, we have $F_1 \in S_1$, $F_2 \in S_2$ and $F_3 \in S_3$. Furthermore, we have $h(F_1) \in S_2$, $h(F_2) \in S_3$ and $h(F_3) \in S_1$, by the definition of $h$. Therefore, we obtain
$$
\begin{aligned} & \sum_{i=1}^{3} \max\{f(f(k_i)), f(g(k_i)), g(f(k_i)), g(g(k_i))\} \\ &= \max\{F_1, F_2, h(F_1), h(F_2)\} + \max\{F_2, F_3, h(F_2), h(F_3)\} + \max\{F_3, F_1, h(F_3), h(F_1)\} \\ &= h(F_2) + \max\{F_3, h(F_2)\} + F_3 \\ & \geq h(F_2) + \frac{1}{2}(F_3 + h(F_2)) + F_3 \\ &= \frac{3}{2}F_3 + \frac{3}{2}h(F_2). \end{aligned} \quad (**)
$$
Every element of $S$ appears exactly once as $a_1, a_2$ or $a_3$ for some $Z_j$. Since $f$ is bijective, the same is true for $k_1, k_2$ or $k_3$. Furthermore, since $f$ and $h$ are both bijections, each element of $S_3$ appears exactly once as $F_3$, and as $h(F_2)$, for some $Z_j$. Hence, by taking sums of both sides of $(**)$ for $Z_1, \dots, Z_{1000}$, we have
$$
X_{\max}(f,g) \geq \frac{3}{2} \sum_{k=2001}^{3000} k + \frac{3}{2} \sum_{k=2001}^{3000} k = \sum_{k=2001}^{3000} 3k.
$$
Similarly, we have $X_{\min}(f,g) \leq \sum_{k=1}^{1000} 3k$. Therefore, we can conclude that
$$
X(f,g) \geq \sum_{k=2001}^{3000} 3k - \sum_{k=1}^{1000} 3k = 6000000.
$$
This completes the proof that $X = 6000000$ satisfies the condition, hence the answer is $6000000$.

