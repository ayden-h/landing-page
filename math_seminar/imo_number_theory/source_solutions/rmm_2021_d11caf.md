# rmm_2021_d11caf

RMM | Romanian Master of Mathematics (RMM) | 2021 | Day 1 | Problem 2

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [rmm_2021_d11caf](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2021_d11caf.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Romanian Master of Mathematics (RMM)

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Sergey can determine Xenia's number in $2$ but not fewer moves.

We first show that $2$ moves are sufficient. Let Sergey provide the set $\{17,18\}$ on his first move, and the set $\{18,19\}$ on the second move. In Xenia's two responses, exactly one number occurs twice, namely, $a_{18}$. Thus, Sergey is able to identify $a_{17}, a_{18}$, and $a_{19}$, and thence the residue of $N$ modulo $17 \cdot 18 \cdot 19 = 5814 > 5000$, by the Chinese Remainder Theorem. This means that the given range contains a single number satisfying all congruences, and Sergey achieves his goal.

To show that $1$ move is not sufficient, let $M = \operatorname{lcm}(1,2, \ldots, 10) = 2^{3} \cdot 3^{2} \cdot 5 \cdot 7 = 2520$. Notice that $M$ is divisible by the greatest common divisor of every pair of distinct positive integers not exceeding $20$. Let Sergey provide the set $S = \{s_{1}, s_{2}, \ldots, s_{k}\}$. We show that there exist pairwise distinct positive integers $b_{1}, b_{2}, \ldots, b_{k}$ such that $1 \equiv b_{i} \pmod{s_{i}}$ and $M+1 \equiv b_{i-1} \pmod{s_{i}}$ (indices are reduced modulo $k$). Thus, if in response Xenia provides the set $\{b_{1}, b_{2}, \ldots, b_{k}\}$, then Sergey will be unable to distinguish $1$ from $M+1$, as desired.

To this end, notice that, for each $i$, the numbers of the form $1 + m s_{i}$, $m \in \mathbb{Z}$, cover all residues modulo $s_{i+1}$ which are congruent to $1 (\equiv M+1)$ modulo $\operatorname{gcd}(s_{i}, s_{i+1}) \mid M$. Xenia can therefore choose a positive integer $b_{i}$ such that $b_{i} \equiv 1 \pmod{s_{i}}$ and $b_{i} \equiv M+1 \pmod{s_{i+1}}$. Clearly, such choices can be performed so as to make the $b_{i}$ pairwise distinct, as required.
