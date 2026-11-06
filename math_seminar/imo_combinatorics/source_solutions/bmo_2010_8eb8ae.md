# bmo_2010_8eb8ae

BMO-SL | Balkan Mathematical Olympiad | 2010 | COMBINATORICS | C5

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2010_8eb8ae](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2010_8eb8ae.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: Balkan Mathematical Olympiad Shortlist 2010: Problems and Solutions
- Year: 2010
- Organization: Balkan Mathematical Olympiad
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We will prove that a single measurement is sufficient to do the job. Let $a_1 < a_2 < \dots < a_n$ and $b_1 > b_2 > \dots > b_n$, $n \ge 2$ be arbitrary real numbers. For each permutation $\pi$ of the set $\{1, 2, \dots, n\}$ define
$$
Z(\pi) = a_1 b_{\pi(1)} + a_2 b_{\pi(2)} + \dots + a_n b_{\pi(n)}.
$$
The rearrangement inequality says that $Z(\pi)$ is the least possible if and only if $\pi$ is the identical permutation. The next lemma tells us where one should look for those permutations $\pi$ for which the value of $Z(\pi)$ is the second least.

Lemma. Denote by $\pi_i, 1 \le i \le n-1$, the permutation of the set $\{1, 2, \dots, n\}$ given by
$$
\pi_i: \begin{pmatrix} 1 & 2 & \dots & i-1 & i & i+1 & i+2 & \dots & n \\ 1 & 2 & \dots & i-1 & i+1 & i & i+2 & \dots & n \end{pmatrix}.
$$
For each permutation $\mu \notin \{\text{id}, \pi_1, \pi_2, \dots, \pi_{n-1}\}$ we have that
$$
Z(\mu) > \min\{Z(\pi_1), Z(\pi_2), \dots, Z(\pi_{n-1})\}. \quad (1)
$$
**Proof.** Let $\pi$ be a permutation such that the value $Z(\pi)$ is the least among all nonidentical permutations. Then there must be a positive integer that is not mapped to itself by $\pi$.
Let $i$ be the least such integer. Clearly, we have $\pi(i) > i$. Hence there is a $j > i$ such that $\pi(j) = i$. Consider the permutation $\tau$ that coincides with $\pi$ everywhere except on the numbers $i$ and $j$ where $\tau(i) = i$ and $\tau(j) = \pi(i)$.
Then
$$
\begin{aligned}
Z(\pi) - Z(\tau) &= a_i b_{\pi(i)} + a_j b_{\pi(j)} - a_i b_{\tau(i)} - a_j b_{\tau(j)} = a_i b_{\pi(i)} + a_j b_i - a_i b_j - a_j b_{\pi(i)} = \\
&= (a_i - a_j)(b_{\pi(i)} - b_i) > 0
\end{aligned}
$$
(because from $i < j$ and $\pi(i) > i$ it follows that $a_i - a_j < 0$ and $b_{\pi(i)} - b_i < 0$).
Whereas $\pi$ is a permutation for which $Z$ takes its minimal value for all nonidentical permutations, it follows that $\tau = \text{id}$. This shows that $\pi$ has the form
$$
\pi: \begin{pmatrix} 1 & 2 & \dots & i-1 & i & i+1 & \dots & j-1 & j & j+1 & \dots & n \\ 1 & 2 & \dots & i-1 & j & i+1 & \dots & j-1 & i & j+1 & \dots & n \end{pmatrix}.
$$
Let us show that $j = i + 1$. Suppose to the contrary, namely suppose that $j > i + 1$. Consider the permutation $\sigma$ that coincides with $\pi$ everywhere except on the numbers $i$ and $i+1$ where $\sigma(i) = i+1$ and $\sigma(i+1) = j$. Then $\sigma$ is another nonidentical permutation and
$$
Z(\pi) - Z(\sigma) = a_i b_j + a_{i+1} b_{i+1} - a_i b_{i+1} - a_{i+1} b_j = (a_i - a_{i+1})(b_j - b_{i+1}) > 0.
$$
Thus we have that $Z(\pi) > Z(\sigma)$. This contradicts the selection of $\pi$, which gives the minimal value of $Z$ among all nonidentical permutations. Thus the permutation $\pi$ is one of the following: $\pi_1, \pi_2, \dots, \pi_{n-1}$, which implies (1). The Lemma is proved. $\square$

We shall prove that for arbitrary weights $m_1 < m_2 < \dots < m_{n+1}$, $n \ge 2$, one measurement is sufficient to do the job.
Let us note that this will follow immediately if we show that there are $k_1, k_2, \dots, k_n, k_{n+1}$
$$
k_1 m_1 + k_2 m_2 + \dots + k_n m_n < k_{n+1} m_{n+1}, \quad (1)
$$
$$
\text{and such that}\qquad k_1 m_{\pi(1)} + k_2 m_{\pi(2)} + \dots + k_n m_{\pi(n)} > k_{n+1} m_{\pi(n+1)} \quad (2)
$$
for any nonidentical permutation $\pi$ of the set $(1, 2, \dots, n+1)$.

Suppose there are such integers. In this case the controller takes $k_1$ coins from the wagon labelled $m_1$, $k_2$ coins from the wagon labelled $m_2$, ..., $k_n$ coins from the wagon labelled $m_n$ and puts all of them on the left plate of scales. He takes $k_{n+1}$ coins from the wagon labelled $m_{n+1}$ and puts them on the right plate. Then this measurement does the job. Indeed, if all wagons were labelled properly, the left hand side will weigh less than the right hand side, whereas otherwise it will be the right hand side that will weigh less.
It is clear that we are forced to choose and fix the integers $k_1, k_2, ..., k_n, k_{n+1}$ so that "the second least weight" on the left hand side exceeds the maximal weight of the right hand side, i.e. $k_{n+1}m_{n+1}$. It is clear that "the second least weight" of the left hand side does not contain weights $m_{n+1}$.
To accomplish this let us choose $k_1, k_2, ..., k_n$ such that $k_1 > k_2 > ... > k_n$. If they are ordered in such a way, then by Lemma "the second least weight" of the left hand side is of the form
$$
k_1 m_1 + k_2 m_2 + \dots + k_{i-1} m_{i-1} + k_i m_{i+1} + k_{i+1} m_i + k_{i+2} m_{i+2} + \dots + k_n m_n,
$$
for some $1 \le i \le n-1$. Thus, for (1) and (2) to hold it suffices that
$$
k_{n+1} > \frac{k_1 m_1 + k_2 m_2 + \dots + k_n m_n}{m_{n+1}},
$$
as well as
$$
k_{n+1} < \frac{k_1 m_1 + k_2 m_2 + \dots + k_{i-1} m_{i-1} + k_i m_{i+1} + k_{i+1} m_i + k_{i+2} m_{i+2} + \dots + k_n m_n}{m_{n+1}}
$$
for each $1 \le i \le n-1$.
Also we must make sure that $k_{n+1}$ is indeed a positive integer. The existence of such an integer would be guaranteed if
$$
\frac{k_1 m_1 + k_2 m_2 + \dots + k_{i-1} m_{i-1} + k_i m_{i+1} + k_{i+1} m_i + k_{i+2} m_{i+2} + \dots + k_n m_n}{m_{n+1}} > 1 + \frac{k_1 m_1 + k_2 m_2 + \dots + k_n m_n}{m_{n+1}},
$$
holds for each $1 \le i \le n-1$. The last condition is equivalent to $(k_i - k_{i+1})(m_{i+1} - m_i) > m_{n+1}$, for each $1 \le i \le n-1$. This is easily achieved if we take
$$
k_n = 1,\quad k_{n-1} = k_n + \left[ \frac{m_{n+1}}{m_n - m_{n-1}} \right] + 1,\quad k_{n-2} = k_{n-1} + \left[ \frac{m_{n+1}}{m_{n-1} - m_{n-2}} \right] + 1,\dots,\quad k_2 = k_3 + \left[ \frac{m_{n+1}}{m_2 - m_1} \right] + 1,\quad k_1 = k_2 + \left[ \frac{m_{n+1}}{m_1 - m_2} \right] + 1.
$$
Finally we can set
$$
k_{n+1} = 1 + \left[ \frac{k_1 m_1 + k_2 m_2 + \dots + k_n m_n}{m_{n+1}} \right]. \quad \square

