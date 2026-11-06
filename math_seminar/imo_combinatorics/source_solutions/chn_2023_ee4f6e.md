# chn_2023_ee4f6e

CMO-China | China | 2023 | Day One | 3

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [chn_2023_ee4f6e](https://mathnet.mit.edu/data_v2/full/china/chn_2023_ee4f6e.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: China
- Title: The 39th Chinese Mathematical Olympiad
- Year: 2023
- Organization: Chinese Mathematical Olympiad
- Place: Wuhan, Hubei
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

(1) For an intuitive understanding, place numbers $1, 2, \dots, p$ equidistantly in a clockwise direction on the circumference of a circle with a perimeter exactly equal to $p$. Then $r(x, y)$ is precisely the distance from $x$ to $y$ in a clockwise direction.
For an $m$-element subset $A = \{x_1, x_2, \dots, x_m\}$ of $\Omega$ (with elements arranged from smallest to largest), we have
$$
f(A) = \sum_{x,y \in A} r(x,y)^2 = \sum_{k=1}^{m-1} \sum_{i=1}^{m} r(x_i, x_{i+k})^2.
$$
Here, indices are considered modulo $m$.
For $k = 1, 2, \dots, m-1$, notice that $\sum_{i=1}^{m} r(x_i, x_{i+k}) = kp$, as the $m$ arcs from $x_1$ to $x_{1+k}$, from $x_2$ to $x_{2+k}$, $\dots$, from $x_m$ to $x_k$ can be recombined to form $k$ circles. By the AM-GM inequality, the minimum value of the partial sum $S_k = \sum_{i=1}^{m} r(x_i, x_{i+k})^2$ is obtained when each $d(x_i, x_{i+k}) = \lfloor \frac{kp}{m} \rfloor$ or $\lceil \frac{kp}{m} \rceil$. For all $S_k$ to reach their minimum values, it is equivalent to, for any $i, j = 1, 2, \dots, m$,
$$
\left| x_j - x_i - \frac{(j-i)p}{m} \right| < 1.
$$
That is, the differences between any two numbers in the set $D = \{x_1 - \frac{p}{m}, x_2 - \frac{2p}{m}, \dots, x_m - \frac{mp}{m}\}$ are less than 1. (In other words, this requires $x_1, \dots, x_m$ to be almost equidistantly distributed on the circle.) Since multiplying the numbers in $D$ by $m$ yields distinct integers, we can set $D = \{\frac{r}{m}, \frac{r-1}{m}, \dots, \frac{r-(m-1)}{m}\}$. Thus for $k = 1, 2, \dots, m$, $x_k$ is the only integer among $\frac{kp+r}{m}, \frac{kp+r-1}{m}, \dots, \frac{kp+r-(m-1)}{m}$, i.e., $x_k = \lfloor \frac{kp+r}{m} \rfloor$. From $x_1 \ge 1$ we know $r \ge m-p$, and from $x_m \le p$ we know $r \le m-1$.
Therefore, each of the aforementioned partial sums $S_k$ reaches its minimum value if and only if the set
$$
A = \left\{ x_k = \left\lfloor \frac{kp+r}{m} \right\rfloor \mid k = 1, 2, \dots, m \right\},
$$
where $r \in \{m-p, m-p+1, \dots, m-1\}$. Specifically, at this time $f$ takes its minimum value among all $m$-element subsets, meaning these $A$ are precisely all the $m$-element good subsets. Since every element of a good subset $A$ plus $k$ (modulo $p$) is still a good subset, all $m$-element good subsets are "rotationally equivalent" (they are rotations of $\{\lfloor \frac{kp}{m} \rfloor \mid k = 1, \dots, m\}$).

(2) For convenience of explanation and understanding, we define a graph $G$ with $V = \{1, 2, \dots, p-1\}$ as vertices. If there exists an $a$-element good subset $A$ and a $b$-element good subset $B$ such that $A \subset B$, then we draw a directed edge $a \to b$. Due to the rotational equivalence of good subsets: if some $b$-element good subset contains an $a$-element good subset, then every $b$-element good subset contains some $a$-element good subset, and every $a$-element good subset is also contained in some $b$-element good subset. (Clearly, graph $G$ forms a poset, i.e., if $a \to b, b \to c$ then $a \to c$). Therefore, the problem transforms into considering the chains $a_1 \to a_2 \to \dots \to a_L$ in graph $G$, (where $L$ is the length of the chain).

We prove the following conclusions:

**Conclusion 1:** The complement $A^c$ of any $m$-element good subset $A$ is also a good subset.
*Proof of Conclusion 1:* Observe the following identity:
$$
f(A) - f(A^c) = \left( \sum_{x \in A} \sum_{y \in \Omega} r(x, y)^2 - \sum_{x \in A} \sum_{y \in A^c} r(x, y)^2 \right) - \left( \sum_{x \in \Omega} \sum_{y \in A^c} r(x, y)^2 - \sum_{x \in A} \sum_{y \in A^c} r(x, y)^2 \right) \\
= \sum_{x \in A} \sum_{y \in \Omega} r(x, y)^2 - \sum_{x \in \Omega} \sum_{y \in A^c} r(x, y)^2 = |A| \times \sum_{k=0}^{m-1} \left(\frac{k}{m}\right)^2 - \sum_{k=0}^{m-1} \left(\frac{k}{m}\right)^2 \times |A^c|,
$$
i.e., $f(A) - f(A^c)$ is a constant value. Therefore, $f(A)$ reaching its minimum is equivalent to $f(A^c)$ reaching its minimum.
Thus, a good subset $A \subset B$ is also equivalent to good subset $B^c \subset A^c$, i.e., in graph $G$ there is an edge $a \to b$ if and only if there is an edge $(p-b) \to (p-a)$.

**Conclusion 2:** When $m < \frac{p}{2}$, any $m$-element good subset $A$ can be contained within a rotation of its complement $A^c$, i.e., graph $G$ has an edge $m \to (p-m)$.
*Proof of Conclusion 2:* Take the $2m$-element good subset $C = \{\lfloor \frac{kp}{2m} \rfloor \mid k = 1, 2, \dots, 2m\}$, then
$$
A = \left\{ y_k = x_{2k} = \left\lfloor \frac{kp}{m} \right\rfloor \right\} \quad \text{and} \quad B = \left\{ z_k = x_{2k-1} = \left\lfloor \frac{kp + \left(-\frac{p+1}{2}\right)}{m} \right\rfloor \right\}
$$
are both $m$-element good subsets, and $B^c$ is a $p-m$-element good subset. Thus $A \subset B^c$.
*Alternate proof of Conclusion 2:* Since $m < \frac{p}{2}$, $A$ and $A+1 = \{x+1 \mid x \in A\}$ do not intersect. Hence $A \subset (A+1)^c$. Conclusion 2 holds.

The aforementioned symmetry of graph $G$ means that we only need to consider the longest chain from 1 to some number $< \frac{p}{2}$. This is because for a chain $a_1 \to a_2 \to \dots \to a_L$, let $a_k < \frac{p}{2}$, $a_{k+1} > \frac{p}{2}$, then we can form two new chains
$$
\begin{align*}
a_1 &\to \dots \to a_k \to (p-a_k) \to \dots \to (p-a_1) \quad \text{(length 2k)}, \\
p-a_L &\to \dots \to p-a_{k+1} \to a_{k+1} \to \dots \to a_L \quad \text{(length 2L-2k)}.\end{align*}
$$
At least one of these has length $\ge L$. Therefore, we only need to consider "self-symmetric" chains.

**Conclusion 3:** When $a$ divides $b$, there is an edge $a \to b$, because the good subset
$$
B = \{x_k = \lfloor \frac{kp}{b} \rfloor, k = 1, 2, \dots, b\} \supset A = \{y_k = x_{k \times \frac{b}{a}} = \lfloor \frac{kp}{a} \rfloor, k = 1, 2, \dots, a\}.
$$
From this, we know that when $2^u < p < 2^{u+1}$, there is always a chain of length $2u$
$$
1 \to 2 \to 4 \to \dots \to 2^{u-1} \to (p-2^{u-1}) \to (p-2^{u-2}) \to \dots \to (p-2) \to (p-1). \quad (2)
$$
If the length of a chain $L > 2u$, by symmetry, we may assume $a_{u+1} < \frac{p}{2}$.
Next, we consider the necessary conditions for an edge $a \to b$ in graph $G$ when $a < b < \frac{p}{2}$.

**Conclusion 4:** When $a < b < \frac{p}{3}$, if an $a$-element good subset $A$ is contained in a $b$-element good subset $B$, i.e., $a \to b$, then $a$ must be a divisor of $b$.
*Proof of Conclusion 4:* Without loss of generality, assume good subset $B = \{x_k = \lfloor \frac{kp}{b} \rfloor, k = 1, 2, \dots, b\}$ contains good subset $A = \{y_j = x_{k_j}, j = 1, 2, \dots, a\}$. If $k_1, k_2, \dots, k_a$ are not equally spaced, for example, $k_2 - k_1 > k_3 - k_2$, then the difference between adjacent elements in $A$ is
$$
y_2 - y_1 = x_{k_2} - x_{k_1} \ge \lfloor \frac{(k_2 - k_1)p}{b} \rfloor \ge \lfloor \frac{(k_2 - k_1 - 1)p}{b} \rfloor + \lfloor \frac{p}{b} \rfloor \\
\ge \lfloor \frac{(k_3 - k_2)p}{b} \rfloor + 3 \ge x_{k_3} - x_{k_2} + 2 = y_3 - y_2 + 2,
$$
which contradicts the fact that $A$ is a good subset. Therefore, $a$ must be a divisor of $b$.

**Conclusion 5:** When $\frac{p}{4} < a < b < \frac{p}{2}$, except when $p \equiv 3 \pmod 4$ with an edge $\frac{p+1}{4} \to \frac{p-1}{2}$, there is no edge between $a$ and $b$.
*Proof of Conclusion 5:* From Conclusion 4, we know at this point $\frac{p}{3} < b < \frac{p}{2}$, otherwise $b < \frac{p}{3}$ and is a multiple of $a$, which is impossible. As in the proof of Conclusion 4, assume good subset $B = \{x_k = \lfloor \frac{kp}{b} \rfloor, k = 1, 2, \dots, b\}$ contains good subset $A = \{y_j = x_{k_j}, j = 1, 2, \dots, a\}$. Let the interval in $B$ be $h_k = x_{k+1} - x_k = \lfloor \frac{kp+p}{b} \rfloor - \lfloor \frac{kp}{b} \rfloor \in \{2, 3\}$. Hence, there exists an interval in $A$ $y_{j+1} - y_j \ge x_{k+2} - x_k \ge 4$, so $|A| = a < \frac{p}{3}$, i.e., intervals in $A$ $g_j = y_{j+1} - y_j \in \{\lfloor \frac{p}{a} \rfloor, \lceil \frac{p}{a} \rceil\} = \{3, 4\}$. Clearly, the sequence $\mathbf{h} = (h_1, h_2, \dots, h_b)$ is obtained from $\mathbf{g} = (g_1, g_2, \dots, g_a)$ by replacing each 4 with two consecutive 2s.
If the sequence $\mathbf{h}$ contains at least two 3s, consider the number of 2s between each pair of adjacent 3s. These numbers can differ by at most 1 (otherwise, in $\mathbf{h}$ there is a segment with $t+2$ consecutive 2s, another with at most $t$ 2s between two 3s, with a total difference of at least 2, contradicting $B$ being a good subset), and all these numbers are even, so they are all equal. This makes the sequence $\mathbf{h}$ have a smaller period, contradicting the total sum of $\mathbf{h}$ being the prime number $p$. Therefore, $\mathbf{h}$ contains one 3 and $b-1$ 2s, i.e., $p = 2b+1$. The sequence $\mathbf{g}$ contains one 3 and $a-1$ 4s, i.e., $p = 4a-1$. In this case, take
$$
A = \{1, 5, 9, \dots, p-2\} \subset B = \{1, 3, 5, \dots, p-2\}
$$
to prove Conclusion 5.

Combining Conclusions 4 and 5, we know that when $2^u < p < 2^{u+1}$, for any chain $a_1 \to a_2 \to \dots \to a_L$, the sequence $a_1, a_2, a_3, \dots$ before $\frac{p}{4}$ multiplies by several times each step, so there are at most $u-1$ numbers (since $\frac{p}{4} < 2^{u-1}$), thus $a_u > \frac{p}{4}$. If $a_{u+1} < \frac{p}{2}$, then necessarily $a_u = \frac{p+1}{4}$, $a_{u+1} = \frac{p-1}{2}$, in which case only $a_u = 2^{u-1}$ (otherwise $a_u \ge 3 \times 2^{u-2} > \frac{p-1}{4}$), i.e., $p = 2^{u+1}-1$.

In summary, $L_{\max} = 2 \times \lfloor \log_2(p+1) \rfloor$. Thus, when $2^u < p < 2^{u+1} - 1$, $L \le 2u$, with equality in chain (2). When $p = 2^{u+1} - 1$, $L \le 2(u+1)$, with equality in the following chain:
$$
1 \to 2 \to \dots \to 2^{u-1} \to 2^u - 1 \to 2^u \to (p-2^{u-1}) \to (p-2^{u-2}) \to \dots \to (p-2) \to (p-1).
$$

## Supplied solution 2

The characterization of good subsets is similar to part (1) in Solution 1. The following discussion simplifies the subsequent proof. Notice that
$$
\lfloor \frac{kp}{m} \rfloor \cdot m \equiv \{\frac{kp}{m}\} \cdot m \quad \mod p.
$$
And when $k = 0, 1, \dots, m-1$, $\{\frac{kp}{m}\}$ takes all values from $0, 1, \dots, m-1$. Hence, modulo $p$, $\{m\lfloor \frac{kp}{m} \rfloor\}$ is equal to $\{0, -1, \dots, -(m-1)\}$. Due to the uniqueness of rotation, any $m$-element good subset multiplied by $m$ (in the sense of modulo $p$) consists of consecutive $m$ numbers. Conversely, if an $m$-element subset multiplied by $m$ consists of consecutive $m$ numbers, it must be an $m$-element good subset.
Let $r$ be the modular multiplicative inverse of $m$ modulo $p$, then $\{\lfloor \frac{kp}{m} \rfloor\} \equiv \{0, -r, \dots, -(m-1)r\} \mod p$. Therefore, any $m$-element set is a good subset if and only if it can be written as $\{a, a+r, \dots, a+(m-1)r\} \mod p$.

The following steps are similar to Conclusions 1–5 in Solution 1, but the proofs are relatively simpler.

**Conclusion 1:** The complement of any $m$-element good subset is a $p-m$-element good subset.
*Proof of Conclusion 1:* Based on the above characterization, assume the $m$-element good subset is $\{a, a+r, \dots, a+(m-1)r\}$ (in the sense of modulo $p$), then its complement can be written as $\{a-r, a-2r, \dots, a-(p-m)r\}$ modulo $p$. Since the modular multiplicative inverse of $p-m$ modulo $p$ is $-r$ modulo $p$, the set $\{a-r, a-2r, \dots, a-(p-m)r\}$ is a good subset.

**Conclusion 2:** If $m < \frac{p}{2}$, then any $m$-element good subset is contained in some $p-m$-element good subset.
*Proof of Conclusion 2:* Without loss of generality, assume the $m$-element good subset is $\{a, a+r, \dots, a+(m-1)r\}$ (in the sense of modulo $p$), then it is contained in the $p-m$-element good subset $\{a+(p-m-1)r, a+(p-m-2)r, \dots, a\}$.

**Conclusion 3:** If $km < p$, then any $m$-element good subset is contained in some $km$-element good subset.
*Proof of Conclusion 3:* Assume the $m$-element good subset is $A = \{a, a+r, \dots, a+(m-1)r\}$ (in the sense of modulo $p$). Let $s$ be the modular multiplicative inverse of $km$ modulo $p$, so $ks \equiv r \pmod p$. Then $A$ is contained in the $km$-element good subset $B = \{a, a+s, \dots, a+(km-1)s\}$.

**Conclusion 4:** If $p \equiv 3 \pmod 4$, then any $\frac{p+1}{4}$-element good subset is contained in some $\frac{p-1}{2}$-element good subset.
*Proof of Conclusion 4:* Note that the modular multiplicative inverse of $\frac{p+1}{4}$ modulo $p$ is 4, and for $\frac{p-1}{2}$ modulo $p$ it is -2. Suppose the $\frac{p+1}{4}$-element good subset is $\{a, a+2, \dots, a+p-3\}$, then it is contained in the $\frac{p-1}{2}$-element good subset $\{a+p-3, a+p-5, \dots, a+2, a\}$.

**Conclusion 5:** If $1 \le n < m \le \frac{p}{2}$, and some $m$-element good subset is contained in some $n$-element good subset, then $m \ge 2n - 1$, and equality holds if and only if $n = \frac{p+1}{4}$ and $m = \frac{p-1}{2}$.

*Proof of Conclusion 5:* Multiply all numbers by $m$. Then, in the sense of modulo $p$, an $m$-element good subset becomes a sequence of consecutive $m$ numbers (since the original common difference was the modular inverse of $m$ modulo $p$), and the $n$-element good subset also becomes an arithmetic sequence $T$, with a common difference congruent to $\frac{m}{n}$ modulo $p$, i.e., not congruent to $\pm 1$ modulo $p$. Assume the transformed $m$-element good subset is $\{0, 1, \dots, m-1\}$, with the first term $a$ of $T$ in $\{0, 1, \dots, m-1\}$, and let the common difference be $\beta$, where $|\beta| < \frac{p}{2}$. Note that $p - (m-1) > \frac{p}{2}$, so every term of $T$ must be in $\{0, 1, \dots, m-1\}$, hence $m = (m-1) + 1 \ge (n-1)|\beta| + 1 \ge 2n-1$. When equality holds, $|\beta| = 2$ must be true, thus $\frac{m}{n} \equiv \pm 2 \pmod p$, meaning $2n-1 \equiv \pm 2n \pmod p$. As $n \le \frac{m+1}{2} \le \frac{p+1}{4}$, the only possibility is $n = \frac{p+1}{4}$ and $m = \frac{p-1}{2}$.

Now returning to the original problem, for any chain of good subsets $A_1 \subset A_2 \subset \dots \subset A_L$, let $|A_q| < \frac{p}{2}$ and $|A_{q+1}| > \frac{p}{2}$. By Conclusion 5, we have
$$
\frac{p+1}{2} \ge 2|A_{q-1}| \ge 2^2|A_{q-2}| \ge \dots \ge 2^{q-1}|A_1| = 2^{q-1}.
$$
Thus, $q \le \lfloor \log_2(p+1) \rfloor$. By Conclusion 1, the chain of complements $A_L^c \subset A_{L-1}^c \subset \dots \subset A_{q+1}^c$ also forms a chain of good subsets, and similarly, we find $L-q \le \lfloor \log_2(p+1) \rfloor$. Therefore, $L \le 2\lfloor \log_2(p+1) \rfloor$.

When $2^q < p+1 < 2^{q+1}$, by Conclusions 1, 2, and 3, there exists a chain of good subsets $A_1 \subset A_2 \subset \dots \subset A_{2q}$, where $|A_i| = 2^{i-1}$, $|A_{2q+1-i}| = p-2^{i-1}$, for $i=1, 2, \dots, q$.

When $p=2^q-1$, by Conclusions 1, 2, 3, and 4, there exists a chain of good subsets $A_1 \subset A_2 \subset \dots \subset A_{2q}$, where $|A_i| = 2^{i-1}$, $|A_{2q+1-i}| = p-2^{i-1}$, for $i=1, 2, \dots, q-1$, $|A_q| = 2^{q-1}-1$, and $|A_{q+1}| = 2^{q-1}$.

In summary, the maximum $L$ sought is $2\lfloor \log_2(p+1) \rfloor$.

