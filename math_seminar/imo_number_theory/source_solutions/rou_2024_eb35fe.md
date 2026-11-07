# rou_2024_eb35fe

RMM | Romania | 2024 | First Day | Problem 2.

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [rou_2024_eb35fe](https://mathnet.mit.edu/data_v2/full/romania/rou_2024_eb35fe.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Romania
- Title: ROMANIAN MATHEMATICAL COMPETITIONS
- Year: 2024
- Editors: Negrescu, Alexandru; Gologan, Radu; Gherghe, Cătălin
- Organization: Romanian Mathematical Society
- Series: Romanian Mathematical Contests
- Volume: 31
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

**Lemma.** Let $n$ be a positive integer and let $c_1, c_2, \dots, c_n$ be a list of positive integers less than $p$ such that each specific value occurs at most $\frac{1}{2}(n+1)$ times. Fix a residue $r \neq c_1 + c_2 + \dots + c_n \pmod{p}$. Then there exists a permutation $d_1, d_2, \dots, d_n$ of the $c_i$ such that $r \neq d_1 + d_2 + \dots + d_k \pmod{p}$ for all $k = 1, 2, \dots, n$.
**Proof.** Induct on $n$. The base case, $n=1$, is clear, so let $n \ge 2$. Consider the residue $a$ that occurs the most times amongst the $c_i$.

If $a \not\equiv r \pmod{p}$, set $d_1 = a$ and complete the rest of the list using the inductive hypothesis with $r$ replaced by $r-a$, as any residue will occur amongst the remaining $c_i$ at most $\frac{1}{2}((n-1)+1)$ times. Indeed, if no other residue occurs as many times as $a$, then the number of occurrences of any residue amongst the remaining $c_i$ is at most $\frac{1}{2}(n+1)-1 = \frac{1}{2}(n-1) < \frac{1}{2}((n-1)+1)$. Otherwise, if there is another residue that occurs as many times as $a$, their number of occurrences has to be at most $\frac{1}{2}n = \frac{1}{2}((n-1)+1)$.

If $a \equiv r \pmod{p}$, choose a residue $b \not\equiv a \pmod{p}$ amongst the $c_i$; the choice is possible, as $\frac{1}{2}(n+1) < n$. Set $d_1 = b$ and $d_2 = a$, noting that $d_1 + d_2 = b + a \equiv r + b \not\equiv r \pmod{p}$. If no other residue occurs as many times as $a$, then each residue occurs amongst the remaining $c_i$ at most $\frac{1}{2}(n+1)-1 = \frac{1}{2}(n-1) = \frac{1}{2}((n-2)+1)$ times. If $a$ occurs at most $\frac{1}{2}(n-1)$ times, then clearly the same will hold for any residue in the remaining $c_i$. The remaining possibility is that $a$ and another residue both occur $\frac{1}{2}n$ times and $n$ is even, meaning that the other residue has to be $b$, and there are no other residues; it is clear that the occurrences in the remaining $c_i$ are precisely $\frac{1}{2}(n-2) < \frac{1}{2}((n-2)+1)$. The inductive hypothesis then applies with $r$ replaced by $-b$ to complete the list. This establishes the lemma.

Back to the problem, if each residue occurs at most $\frac{1}{2}(N+1)$ times, the conclusion follows by the Lemma.

Otherwise, there is exactly one residue $a$ that occurs $M > \frac{1}{2}(N+1)$ times amongst the $a_i$. Note that $2M - N > (N+1) - N = 1$, to set $b_i = a$, $i = 1, 2, \dots, 2M - N$. Letting $\alpha = 50$, note also that $2M - N \le 2 \cdot \frac{\alpha+1}{2\alpha}N - N = \frac{1}{\alpha}N < p$, so none of the first $2M - N$ partial sums is divisible by $p$, as $p$ is prime.

To complete the proof, apply the Lemma with $r = (N-2M)a$ to the remaining $a_i$. There are left $N - (2M - N) = 2(N - M)$ such, $a$ occurs $M - (2M - N) = N - M$ times amongst these and any other residue occurs at most $N - M$ times, both of which do not exceed $\frac{1}{2}(2(N - M) + 1)$.


*Alternative solution.* The permutation will be constructed step by step, first choosing $b_1$, then $b_2$, and so on. At every step, sort the remaining values by their number of appearances from most frequent to least frequent, and from largest to smallest for the situations where the number of appearances is the same. After that, attempt to select the first value from the sorted list; if this results in a partial sum that is divisible by $p$, then attempt to select the second value from the list, which will result in a partial sum that is not divisible by $p$ as the first and second values are different modulo $p$. Label the step as type (I) if the first value has been selected and as type (II) if the second value has been selected.

**Lemma.** Any step of type (II) is followed by a step of type (I).

**Proof.** Suppose that step $j$ is of type (II). Denote the first two values according to the sorting order with $a$ and $b$, and let $s$ be the partial sum until this step. Since step $j$ is type (II), $s + a \equiv 0 \pmod{p}$. At step $j + 1$, the first value according to the sorting order will still be $a$. Since $s + b + a \not\equiv 0 \pmod{p}$, $a$ can be selected for step $j + 1$, so step $j + 1$ is of type (I).

Now suppose, for the sake of contradiction, that this procedure fails. Let $k+1 < N$ be the first step when neither (I) nor (II) is possible. In particular, this means that there is a single value $a$ remaining, and it occurs $N - k$ times. Let $j$ be the smallest number with the following property: at every step between $j$ and $k + 1$, the value $a$ is the first one according to the sorting order; in particular, $a$ is the most frequently occurring one. Such a $j$ exists because $k + 1$ satisfies this property.

If $j > 1$, then at step $j-1$ there is another value $b$ that comes before $a$ in the sorted order. Suppose that at step $j-1$ there are $q$ values of $a$ remaining; then there are at least $q$ values of $b$ remaining. According to the lemma, at least half of the steps $j, j+1, \dots, k$ are of type (I), which means that $a$ is selected in them. Denote $\ell = k-j+1$, then $a$ has been selected at least $\lfloor \ell/2 \rfloor$ steps between $j$ and $k$. Since at step $k+1$, there are $N-k \ge 2$ values of $a$ remaining, it means that $q \ge \lfloor \ell/2 \rfloor + 2$. At the same time, at step $k+1$ there are no values of $b$ remaining, so between steps $j$ and $k$ all the remaining $b$ values have been selected, and this can happen at most $\ell - \lfloor \ell/2 \rfloor$ times. Combining these two leads to $\ell - \lfloor \ell/2 \rfloor \ge q \ge \lfloor \ell/2 \rfloor + 2$, or $\ell \ge 2\lfloor \ell/2 \rfloor + 2$, a contradiction.

If $j = 1$, then $a$ is always the first in the sorted order. Therefore, the first $p-1$ steps are of type (I), and step $p$ is of type (II). If $k \ge p$, from steps $p+1$ to $k$, at least every other step is of type (I), meaning that $a$ is selected. Once step $k$ is done, there are $N-k$ remaining values of $a$. Therefore, in the beginning, there were at least
$$
(p-1) + \frac{k-p}{2} + N-k = N - \frac{k}{2} + \frac{p}{2} - 1 > N - \frac{N-2}{2} + \frac{N}{2\alpha} - 1 = \frac{\alpha+1}{2\alpha}N
$$
values of $a$, contradiction. In the situation when $k < p$, there are at least $N - 1$ values of $a$, which is also a contradiction.
